# v15.7.3 → v15.7.4 · 最優先の変更候補 (78)

[一覧の目次](README.md)

<a id="compare-78bd70beb4f93184f666f43310f098c9"></a>

### [`00bb4b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4b8c.md) → [`00bb4bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb4/00bb4bd0.md) _ZNSt6__ndk112ctype_bynameIcED1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00be19b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19b0.md) [`00be1ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ce0.md) · 呼出先 3件 [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00bdef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef40.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md)
- 新版 呼出元 2件 [`00be1a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a00.md) [`00be1d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d30.md) · 呼出先 3件 [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md) [`00bdef90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef90.md) [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md)

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
      "definition_site": "00bb4bf0",
      "incomplete_value": true,
      "site": "00bb4bf4",
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
      "definition_site": "00bb4bac",
      "incomplete_value": true,
      "site": "00bb4bb0",
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
      "definition_site": "00bb4c08",
      "incomplete_value": true,
      "site": "00bb4c0c",
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
      "definition_site": "00bb4bc4",
      "incomplete_value": true,
      "site": "00bb4bc8",
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
      "00bb4be8",
      "READ",
      [
        "storage",
        "00c1bf50",
        null,
        "pointer"
      ]
    ],
    [
      "00bb4bf4",
      "DATA",
      [
        "storage",
        "00c139d8",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00bb4c00",
      "READ",
      [
        "storage",
        "00c1bf48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb4be8",
      "READ",
      [
        "storage",
        "00c1bfa0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb4bf4",
      "DATA",
      [
        "storage",
        "00c13a28",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00bb4c00",
      "READ",
      [
        "storage",
        "00c1bf98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb4ba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4b8c.md#insn-00bb4ba4) · [`00bb4bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4b8c.md#insn-00bb4bb4) · [`00bb4bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4b8c.md#insn-00bb4bbc)
- 新版 `00bb4be8`（命令位置の公開資料なし） · `00bb4bf8`（命令位置の公開資料なし） · `00bb4c00`（命令位置の公開資料なし）

~~~diff
- 00bb4ba4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
- 00bb4ba4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb4be8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
+ 00bb4be8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb4ba4 bytes 08a947f9
+ 00bb4be8 bytes 08d147f9
- 00bb4bb4 ["INT_ADD", "register:40f0:8", ["const:bb4bb4:8", "const:4:8"]]
- 00bb4bb4 ["CALL", null, ["callee:00be1930:8"]]
+ 00bb4bf8 ["INT_ADD", "register:40f0:8", ["const:bb4bf8:8", "const:4:8"]]
+ 00bb4bf8 ["CALL", null, ["callee:00be1930:8"]]
- 00bb4bb4 bytes 4bb30094
+ 00bb4bf8 bytes 4eb30094
- 00bb4bbc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
- 00bb4bbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb4c00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f98:8"]]
+ 00bb4c00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb4bbc bytes 08a547f9
+ 00bb4c00 bytes 08cd47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b8fd19f5379ce86b73de00b66c80f8e"></a>

### [`00bb4bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4bf4.md) → [`00bb4c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb4/00bb4c38.md) _ZNSt6__ndk118__time_get_storageIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1850.md) · 呼出先 7件 [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00bdef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef40.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md) [`00be19a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19a0.md)
- 新版 呼出元 1件 [`00be18a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be18a0.md) · 呼出先 7件 [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md) [`00bdef90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef90.md) [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md) [`00be19f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19f0.md)

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
      "definition_site": "00bb4c80",
      "incomplete_value": false,
      "site": "00bb4c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c15000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb4c3c",
      "incomplete_value": false,
      "site": "00bb4c40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c15000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
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
      "definition_site": "00bb4ca0",
      "incomplete_value": true,
      "site": "00bb4ca4",
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
      "definition_site": "00bb4c5c",
      "incomplete_value": true,
      "site": "00bb4c60",
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
      "definition_site": "00bb4cb8",
      "incomplete_value": true,
      "site": "00bb4cbc",
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
      "definition_site": "00bb4c74",
      "incomplete_value": true,
      "site": "00bb4c78",
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
      "00bb4c84",
      "DATA",
      [
        "storage",
        "00c15ea8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bb4c98",
      "READ",
      [
        "storage",
        "00c1bf50",
        null,
        "pointer"
      ]
    ],
    [
      "00bb4ca4",
      "DATA",
      [
        "storage",
        "00c139d8",
        null,
        "undefined1[104]"
      ]
    ]
  ],
  "added": [
    [
      "00bb4c84",
      "DATA",
      [
        "storage",
        "00c15ef8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bb4c98",
      "READ",
      [
        "storage",
        "00c1bfa0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb4ca4",
      "DATA",
      [
        "storage",
        "00c13a28",
        null,
        "undefined1[104]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb4c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4bf4.md#insn-00bb4c34) · [`00bb4c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4bf4.md#insn-00bb4c14) · [`00bb4c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4bf4.md#insn-00bb4c24)
- 新版 `00bb4c78`（命令位置の公開資料なし） · `00bb4c58`（命令位置の公開資料なし） · `00bb4c68`（命令位置の公開資料なし）

~~~diff
- 00bb4c34 ["INT_ADD", "register:40f0:8", ["const:bb4c34:8", "const:4:8"]]
- 00bb4c34 ["CALL", null, ["callee:00be19f0:8"]]
+ 00bb4c78 ["INT_ADD", "register:40f0:8", ["const:bb4c78:8", "const:4:8"]]
+ 00bb4c78 ["CALL", null, ["callee:00be19f0:8"]]
- 00bb4c34 bytes 5bb30094
+ 00bb4c78 bytes 5eb30094
- 00bb4c14 ["INT_ADD", "register:40f0:8", ["const:bb4c14:8", "const:4:8"]]
- 00bb4c14 ["CALL", null, ["callee:00be1cd0:8"]]
+ 00bb4c58 ["INT_ADD", "register:40f0:8", ["const:bb4c58:8", "const:4:8"]]
+ 00bb4c58 ["CALL", null, ["callee:00be1cd0:8"]]
- 00bb4c14 bytes 1bb40094
+ 00bb4c58 bytes 1eb40094
- 00bb4c24 ["INT_ADD", "register:40f0:8", ["const:bb4c24:8", "const:4:8"]]
- 00bb4c24 ["CALL", null, ["callee:00bdb240:8"]]
+ 00bb4c68 ["INT_ADD", "register:40f0:8", ["const:bb4c68:8", "const:4:8"]]
+ 00bb4c68 ["CALL", null, ["callee:00bdb240:8"]]
- 00bb4c24 bytes 73990094
+ 00bb4c68 bytes 76990094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b921d7feb125da43b5dfb4351317bc24"></a>

### [`00bb4ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4ed4.md) → [`00bb4f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb4/00bb4f18.md) _ZNSt6__ndk118__time_get_storageIwEC1EPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md) [`00be19c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19c0.md) [`00be19d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19d0.md) [`00be1c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1c70.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md) [`00be1a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a10.md) [`00be1a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a20.md) [`00be1cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1cc0.md)

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
      "definition_site": "00bb4f60",
      "incomplete_value": false,
      "site": "00bb4f64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c15000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb4f1c",
      "incomplete_value": false,
      "site": "00bb4f20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c15000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "definition_site": "00bb4f80",
      "incomplete_value": true,
      "site": "00bb4f84",
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
      "definition_site": "00bb4f3c",
      "incomplete_value": true,
      "site": "00bb4f40",
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
      "00bb4f64",
      "DATA",
      [
        "storage",
        "00c15f28",
        null,
        "undefined *"
      ]
    ],
    [
      "00bb4f78",
      "READ",
      [
        "storage",
        "00c1bf58",
        null,
        "pointer"
      ]
    ],
    [
      "00bb4f84",
      "DATA",
      [
        "storage",
        "00c13a40",
        null,
        "undefined1[136]"
      ]
    ]
  ],
  "added": [
    [
      "00bb4f64",
      "DATA",
      [
        "storage",
        "00c15f78",
        null,
        "undefined *"
      ]
    ],
    [
      "00bb4f78",
      "READ",
      [
        "storage",
        "00c1bfa8",
        null,
        "pointer"
      ]
    ],
    [
      "00bb4f84",
      "DATA",
      [
        "storage",
        "00c13a90",
        null,
        "undefined1[136]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb4ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4ed4.md#insn-00bb4ef4) · [`00bb4f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4ed4.md#insn-00bb4f04) · [`00bb4f14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4ed4.md#insn-00bb4f14)
- 新版 `00bb4f38`（命令位置の公開資料なし） · `00bb4f48`（命令位置の公開資料なし） · `00bb4f58`（命令位置の公開資料なし）

~~~diff
- 00bb4ef4 ["INT_ADD", "register:40f0:8", ["const:bb4ef4:8", "const:4:8"]]
- 00bb4ef4 ["CALL", null, ["callee:00be1cc0:8"]]
+ 00bb4f38 ["INT_ADD", "register:40f0:8", ["const:bb4f38:8", "const:4:8"]]
+ 00bb4f38 ["CALL", null, ["callee:00be1cc0:8"]]
- 00bb4ef4 bytes 5fb30094
+ 00bb4f38 bytes 62b30094
- 00bb4f04 ["INT_ADD", "register:40f0:8", ["const:bb4f04:8", "const:4:8"]]
- 00bb4f04 ["CALL", null, ["callee:00bdb240:8"]]
+ 00bb4f48 ["INT_ADD", "register:40f0:8", ["const:bb4f48:8", "const:4:8"]]
+ 00bb4f48 ["CALL", null, ["callee:00bdb240:8"]]
- 00bb4f04 bytes bb980094
+ 00bb4f48 bytes be980094
- 00bb4f14 ["INT_ADD", "register:40f0:8", ["const:bb4f14:8", "const:4:8"]]
- 00bb4f14 ["CALL", null, ["callee:00be1a10:8"]]
+ 00bb4f58 ["INT_ADD", "register:40f0:8", ["const:bb4f58:8", "const:4:8"]]
+ 00bb4f58 ["CALL", null, ["callee:00be1a10:8"]]
- 00bb4f14 bytes abb20094
+ 00bb4f58 bytes aeb20094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7cdd7c47b96d08c69151fa42e4f2e7b"></a>

### [`00bb5190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5190.md) → [`00bb51d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb51d4.md) _ZNSt6__ndk112ctype_bynameIwED1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00be19f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19f0.md) [`00be1cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1cf0.md) · 呼出先 2件 [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md) [`00be19d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19d0.md)
- 新版 呼出元 2件 [`00be1a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a40.md) [`00be1d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d40.md) · 呼出先 2件 [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md) [`00be1a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb51f4",
      "incomplete_value": true,
      "site": "00bb51f8",
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
      "definition_site": "00bb51b0",
      "incomplete_value": true,
      "site": "00bb51b4",
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
      "00bb51ec",
      "READ",
      [
        "storage",
        "00c1bf58",
        null,
        "pointer"
      ]
    ],
    [
      "00bb51f8",
      "DATA",
      [
        "storage",
        "00c13a40",
        null,
        "undefined1[136]"
      ]
    ]
  ],
  "added": [
    [
      "00bb51ec",
      "READ",
      [
        "storage",
        "00c1bfa8",
        null,
        "pointer"
      ]
    ],
    [
      "00bb51f8",
      "DATA",
      [
        "storage",
        "00c13a90",
        null,
        "undefined1[136]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb51a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5190.md#insn-00bb51a8) · [`00bb51b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5190.md#insn-00bb51b8)
- 新版 `00bb51ec`（命令位置の公開資料なし） · `00bb51fc`（命令位置の公開資料なし）

~~~diff
- 00bb51a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f58:8"]]
- 00bb51a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb51ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa8:8"]]
+ 00bb51ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb51a8 bytes 08ad47f9
+ 00bb51ec bytes 08d547f9
- 00bb51b8 ["INT_ADD", "register:40f0:8", ["const:bb51b8:8", "const:4:8"]]
- 00bb51b8 ["CALL", null, ["callee:00be1930:8"]]
+ 00bb51fc ["INT_ADD", "register:40f0:8", ["const:bb51fc:8", "const:4:8"]]
+ 00bb51fc ["CALL", null, ["callee:00be1930:8"]]
- 00bb51b8 bytes cab10094
+ 00bb51fc bytes cdb10094
~~~


<a id="compare-60790edf9d4aef5f1a96aa2e586e4298"></a>

### [`00bb51d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb51d4.md) → [`00bb5218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5218.md) _ZNSt6__ndk118__time_get_storageIwEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1860.md) · 呼出先 6件 [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md) [`00be19d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19d0.md) [`00be19e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19e0.md) [`00be1c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1c80.md)
- 新版 呼出元 1件 [`00be18b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be18b0.md) · 呼出先 6件 [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md) [`00be1a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a20.md) [`00be1a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a30.md) [`00be1cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1cd0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.49% / 新版 86.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb5260",
      "incomplete_value": false,
      "site": "00bb5264",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c15000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb521c",
      "incomplete_value": false,
      "site": "00bb5220",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c15000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "definition_site": "00bb5280",
      "incomplete_value": true,
      "site": "00bb5284",
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
      "definition_site": "00bb523c",
      "incomplete_value": true,
      "site": "00bb5240",
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
      "00bb5264",
      "DATA",
      [
        "storage",
        "00c15f28",
        null,
        "undefined *"
      ]
    ],
    [
      "00bb5278",
      "READ",
      [
        "storage",
        "00c1bf58",
        null,
        "pointer"
      ]
    ],
    [
      "00bb5284",
      "DATA",
      [
        "storage",
        "00c13a40",
        null,
        "undefined1[136]"
      ]
    ]
  ],
  "added": [
    [
      "00bb5264",
      "DATA",
      [
        "storage",
        "00c15f78",
        null,
        "undefined *"
      ]
    ],
    [
      "00bb5278",
      "READ",
      [
        "storage",
        "00c1bfa8",
        null,
        "pointer"
      ]
    ],
    [
      "00bb5284",
      "DATA",
      [
        "storage",
        "00c13a90",
        null,
        "undefined1[136]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb51f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb51d4.md#insn-00bb51f4) · [`00bb5204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb51d4.md#insn-00bb5204) · [`00bb5214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb51d4.md#insn-00bb5214)
- 新版 `00bb5238`（命令位置の公開資料なし） · `00bb5248`（命令位置の公開資料なし） · `00bb5258`（命令位置の公開資料なし）

~~~diff
- 00bb51f4 ["INT_ADD", "register:40f0:8", ["const:bb51f4:8", "const:4:8"]]
- 00bb51f4 ["CALL", null, ["callee:00be1cd0:8"]]
+ 00bb5238 ["INT_ADD", "register:40f0:8", ["const:bb5238:8", "const:4:8"]]
+ 00bb5238 ["CALL", null, ["callee:00be1cd0:8"]]
- 00bb51f4 bytes a3b20094
+ 00bb5238 bytes a6b20094
- 00bb5204 ["INT_ADD", "register:40f0:8", ["const:bb5204:8", "const:4:8"]]
- 00bb5204 ["CALL", null, ["callee:00bdb240:8"]]
+ 00bb5248 ["INT_ADD", "register:40f0:8", ["const:bb5248:8", "const:4:8"]]
+ 00bb5248 ["CALL", null, ["callee:00bdb240:8"]]
- 00bb5204 bytes fb970094
+ 00bb5248 bytes fe970094
- 00bb5214 ["INT_ADD", "register:40f0:8", ["const:bb5214:8", "const:4:8"]]
- 00bb5214 ["CALL", null, ["callee:00be1a30:8"]]
+ 00bb5258 ["INT_ADD", "register:40f0:8", ["const:bb5258:8", "const:4:8"]]
+ 00bb5258 ["CALL", null, ["callee:00be1a30:8"]]
- 00bb5214 bytes f3b10094
+ 00bb5258 bytes f6b10094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebe7418dbab8c42419871f84cca4f868"></a>

### [`00bb59c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb59c0.md) → [`00bb5a04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5a04.md) _ZNSt6__ndk110__time_putC1EPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00ba8ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8ac4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md)

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
      "definition_site": "00bb5a58",
      "incomplete_value": false,
      "site": "00bb5a68",
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
            "const:103:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb5a14",
      "incomplete_value": false,
      "site": "00bb5a24",
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
            "const:78:8"
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
      "00bb5a58",
      "PARAM",
      [
        "storage",
        "002a2078",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb5a58",
      "PARAM",
      [
        "storage",
        "002a2103",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb5a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb59c0.md#insn-00bb5a24) · [`00bb59e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb59c0.md#insn-00bb59e4) · [`00bb5a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb59c0.md#insn-00bb5a0c)
- 新版 `00bb5a68`（命令位置の公開資料なし） · `00bb5a28`（命令位置の公開資料なし） · `00bb5a50`（命令位置の公開資料なし）

~~~diff
- 00bb5a24 ["INT_ADD", "register:40f0:8", ["const:bb5a24:8", "const:4:8"]]
- 00bb5a24 ["CALL", null, ["callee:00ba8ac4:8"]]
+ 00bb5a68 ["INT_ADD", "register:40f0:8", ["const:bb5a68:8", "const:4:8"]]
+ 00bb5a68 ["CALL", null, ["callee:00ba8ac4:8"]]
- 00bb5a24 bytes 17ccff97
+ 00bb5a68 bytes 17ccff97
- 00bb59e4 ["INT_ADD", "register:40f0:8", ["const:bb59e4:8", "const:4:8"]]
- 00bb59e4 ["CALL", null, ["callee:00be1570:8"]]
+ 00bb5a28 ["INT_ADD", "register:40f0:8", ["const:bb5a28:8", "const:4:8"]]
+ 00bb5a28 ["CALL", null, ["callee:00be1570:8"]]
- 00bb59e4 bytes cfae0094
+ 00bb5a28 bytes d2ae0094
- 00bb5a0c ["INT_ADD", "register:40f0:8", ["const:bb5a0c:8", "const:4:8"]]
- 00bb5a0c ["CALL", null, ["callee:0041b298:8"]]
+ 00bb5a50 ["INT_ADD", "register:40f0:8", ["const:bb5a50:8", "const:4:8"]]
+ 00bb5a50 ["CALL", null, ["callee:0041b298:8"]]
- 00bb5a0c bytes 2396e197
+ 00bb5a50 bytes 1296e197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-411f40608cd00fa33a1cc29dbda9609b"></a>

### [`00bb5a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5a88.md) → [`00bb5acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5acc.md) _ZNSt6__ndk110__time_putC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1870.md) · 呼出先 5件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)
- 新版 呼出元 1件 [`00be18c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be18c0.md) · 呼出先 5件 [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md)

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
      "definition_site": "00bb5b24",
      "incomplete_value": false,
      "site": "00bb5b34",
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
            "const:103:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb5ae0",
      "incomplete_value": false,
      "site": "00bb5af0",
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
            "const:78:8"
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
      "00bb5b24",
      "PARAM",
      [
        "storage",
        "002a2078",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb5b24",
      "PARAM",
      [
        "storage",
        "002a2103",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb5af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5a88.md#insn-00bb5af0) · [`00bb5abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5a88.md#insn-00bb5abc) · [`00bb5ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5a88.md#insn-00bb5ae0)
- 新版 `00bb5b34`（命令位置の公開資料なし） · `00bb5b00`（命令位置の公開資料なし） · `00bb5b24`（命令位置の公開資料なし）

~~~diff
- 00bb5af0 ["INT_ADD", "register:40f0:8", ["const:bb5af0:8", "const:4:8"]]
- 00bb5af0 ["CALL", null, ["callee:00bdb260:8"]]
+ 00bb5b34 ["INT_ADD", "register:40f0:8", ["const:bb5b34:8", "const:4:8"]]
+ 00bb5b34 ["CALL", null, ["callee:00bdb260:8"]]
- 00bb5af0 bytes c8950094
+ 00bb5b34 bytes cb950094
- 00bb5abc ["INT_ADD", "register:40f0:8", ["const:bb5abc:8", "const:4:8"]]
- 00bb5abc ["CALL", null, ["callee:00be1570:8"]]
+ 00bb5b00 ["INT_ADD", "register:40f0:8", ["const:bb5b00:8", "const:4:8"]]
+ 00bb5b00 ["CALL", null, ["callee:00be1570:8"]]
- 00bb5abc bytes 99ae0094
+ 00bb5b00 bytes 9cae0094
- 00bb5ae0 ["COPY", "tmp:0:8", ["const:78:8"]]
- 00bb5ae0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb5ae0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb5ae0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb5b24 ["COPY", "tmp:0:8", ["const:103:8"]]
+ 00bb5b24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb5b24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb5b24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb5ae0 bytes 00e00191
+ 00bb5b24 bytes 000c0491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d88c78133300c404390b4e603f717dfc"></a>

### [`00bb5b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5b24.md) → [`00bb5b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5b68.md) _ZNSt6__ndk110__time_putD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d20.md) · 呼出先 4件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md)
- 新版 呼出元 1件 [`00be1d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d70.md) · 呼出先 4件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md) [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb5be4",
      "incomplete_value": true,
      "site": "00bb5be4",
      "value": [
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
    "old": {
      "definition_site": "00bb5ba0",
      "incomplete_value": true,
      "site": "00bb5ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:950:8"
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
      "definition_site": "00bb5b9c",
      "incomplete_value": true,
      "site": "00bb5ba0",
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
      "definition_site": "00bb5b58",
      "incomplete_value": true,
      "site": "00bb5b5c",
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
      "definition_site": "00bb5bc4",
      "incomplete_value": false,
      "site": "00bb5bc8",
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
      "definition_site": "00bb5b80",
      "incomplete_value": false,
      "site": "00bb5b84",
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
      "00bb5b88",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb5b98",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb5bc4",
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
      "00bb5b88",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb5b98",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb5bc4",
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

- 旧版 [`00bb5b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5b24.md#insn-00bb5b84) · [`00bb5ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5b24.md#insn-00bb5ba0) · [`00bb5bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5b24.md#insn-00bb5bac)
- 新版 `00bb5bc8`（命令位置の公開資料なし） · `00bb5be4`（命令位置の公開資料なし） · `00bb5bf0`（命令位置の公開資料なし）

~~~diff
- 00bb5b84 ["INT_ADD", "register:40f0:8", ["const:bb5b84:8", "const:4:8"]]
- 00bb5b84 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb5bc8 ["INT_ADD", "register:40f0:8", ["const:bb5bc8:8", "const:4:8"]]
+ 00bb5bc8 ["CALL", null, ["callee:00bdb000:8"]]
- 00bb5b84 bytes 0b950094
+ 00bb5bc8 bytes 0e950094
- 00bb5ba0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:950:8"]]
- 00bb5ba0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb5be4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:990:8"]]
+ 00bb5be4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb5ba0 bytes a0aa04f9
+ 00bb5be4 bytes a0ca04f9
- 00bb5bac ["INT_ADD", "register:40f0:8", ["const:bb5bac:8", "const:4:8"]]
- 00bb5bac ["CALL", null, ["callee:00bdb020:8"]]
+ 00bb5bf0 ["INT_ADD", "register:40f0:8", ["const:bb5bf0:8", "const:4:8"]]
+ 00bb5bf0 ["CALL", null, ["callee:00bdb020:8"]]
- 00bb5bac bytes 09950094
+ 00bb5bf0 bytes 0c950094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbbd24e9d9a06487dcb1e52dc4963ac5"></a>

### [`00bb5bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5bd0.md) → [`00bb5c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5c14.md) _ZNSt6__ndk117moneypunct_bynameIcLb0EE4initEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1890.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00b750e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750e4.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md)
- 新版 呼出元 1件 [`00be18e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be18e0.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00b75128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75128.md) [`00ba8ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8ac4.md)

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
      "definition_site": "00bb5f3c",
      "incomplete_value": false,
      "site": "00bb5f4c",
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
            "const:16d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb5ef8",
      "incomplete_value": false,
      "site": "00bb5f08",
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
            "const:e2:8"
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
      "00bb5f3c",
      "PARAM",
      [
        "storage",
        "002a10e2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb5f3c",
      "PARAM",
      [
        "storage",
        "002a116d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb5f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5bd0.md#insn-00bb5f08) · [`00bb5bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5bd0.md#insn-00bb5bfc) · [`00bb5c0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5bd0.md#insn-00bb5c0c)
- 新版 `00bb5f4c`（命令位置の公開資料なし） · `00bb5c40`（命令位置の公開資料なし） · `00bb5c50`（命令位置の公開資料なし）

~~~diff
- 00bb5f08 ["INT_ADD", "register:40f0:8", ["const:bb5f08:8", "const:4:8"]]
- 00bb5f08 ["CALL", null, ["callee:00ba8ac4:8"]]
+ 00bb5f4c ["INT_ADD", "register:40f0:8", ["const:bb5f4c:8", "const:4:8"]]
+ 00bb5f4c ["CALL", null, ["callee:00ba8ac4:8"]]
- 00bb5f08 bytes decaff97
+ 00bb5f4c bytes decaff97
- 00bb5bfc ["INT_ADD", "register:40f0:8", ["const:bb5bfc:8", "const:4:8"]]
- 00bb5bfc ["CALL", null, ["callee:00be1570:8"]]
+ 00bb5c40 ["INT_ADD", "register:40f0:8", ["const:bb5c40:8", "const:4:8"]]
+ 00bb5c40 ["CALL", null, ["callee:00be1570:8"]]
- 00bb5bfc bytes 49ae0094
+ 00bb5c40 bytes 4cae0094
- 00bb5c0c ["INT_ADD", "register:40f0:8", ["const:bb5c0c:8", "const:4:8"]]
- 00bb5c0c ["CALL", null, ["callee:00be1580:8"]]
+ 00bb5c50 ["INT_ADD", "register:40f0:8", ["const:bb5c50:8", "const:4:8"]]
+ 00bb5c50 ["CALL", null, ["callee:00be1580:8"]]
- 00bb5c0c bytes 49ae0094
+ 00bb5c50 bytes 4cae0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd9122b1590213c33dea57388afe5ff7"></a>

### [`00bb64e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb6/00bb64e4.md) → [`00bb6528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb6/00bb6528.md) _ZNSt6__ndk117moneypunct_bynameIcLb1EE4initEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be18a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18a0.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00b750e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750e4.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md)
- 新版 呼出元 1件 [`00be18f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be18f0.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00b75128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75128.md) [`00ba8ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8ac4.md)

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
      "definition_site": "00bb6850",
      "incomplete_value": false,
      "site": "00bb6860",
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
            "const:16d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb680c",
      "incomplete_value": false,
      "site": "00bb681c",
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
            "const:e2:8"
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
      "00bb6850",
      "PARAM",
      [
        "storage",
        "002a10e2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb6850",
      "PARAM",
      [
        "storage",
        "002a116d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb6/00bb64e4.md#insn-00bb681c) · [`00bb6510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb6/00bb64e4.md#insn-00bb6510) · [`00bb6520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb6/00bb64e4.md#insn-00bb6520)
- 新版 `00bb6860`（命令位置の公開資料なし） · `00bb6554`（命令位置の公開資料なし） · `00bb6564`（命令位置の公開資料なし）

~~~diff
- 00bb681c ["INT_ADD", "register:40f0:8", ["const:bb681c:8", "const:4:8"]]
- 00bb681c ["CALL", null, ["callee:00ba8ac4:8"]]
+ 00bb6860 ["INT_ADD", "register:40f0:8", ["const:bb6860:8", "const:4:8"]]
+ 00bb6860 ["CALL", null, ["callee:00ba8ac4:8"]]
- 00bb681c bytes 99c8ff97
+ 00bb6860 bytes 99c8ff97
- 00bb6510 ["INT_ADD", "register:40f0:8", ["const:bb6510:8", "const:4:8"]]
- 00bb6510 ["CALL", null, ["callee:00be1570:8"]]
+ 00bb6554 ["INT_ADD", "register:40f0:8", ["const:bb6554:8", "const:4:8"]]
+ 00bb6554 ["CALL", null, ["callee:00be1570:8"]]
- 00bb6510 bytes 04ac0094
+ 00bb6554 bytes 07ac0094
- 00bb6520 ["INT_ADD", "register:40f0:8", ["const:bb6520:8", "const:4:8"]]
- 00bb6520 ["CALL", null, ["callee:00be1580:8"]]
+ 00bb6564 ["INT_ADD", "register:40f0:8", ["const:bb6564:8", "const:4:8"]]
+ 00bb6564 ["CALL", null, ["callee:00be1580:8"]]
- 00bb6520 bytes 04ac0094
+ 00bb6564 bytes 07ac0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59ec1d06ef375a38e8d6b9975e5bd9fa"></a>

### [`00bb68cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb6/00bb68cc.md) → [`00bb6910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb6/00bb6910.md) _ZNSt6__ndk117moneypunct_bynameIwLb0EE4initEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be18b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18b0.md) · 呼出先 17件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`006ad8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8e8.md) [`00b750e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750e4.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00baf6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf6e4.md)
- 新版 呼出元 1件 [`00be1900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1900.md) · 呼出先 17件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`006ad8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8e8.md) [`00b75128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75128.md) [`00ba8ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8ac4.md) [`00baf728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf728.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.78% / 新版 99.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb6fe0",
      "incomplete_value": false,
      "site": "00bb6ff0",
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
            "const:16d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6f9c",
      "incomplete_value": false,
      "site": "00bb6fac",
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
            "const:e2:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb6fe0",
      "PARAM",
      [
        "storage",
        "002a10e2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb6fe0",
      "PARAM",
      [
        "storage",
        "002a116d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb6/00bb68cc.md#insn-00bb6fac) · [`00bb68fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb6/00bb68cc.md#insn-00bb68fc) · [`00bb690c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb6/00bb68cc.md#insn-00bb690c)
- 新版 `00bb6ff0`（命令位置の公開資料なし） · `00bb6940`（命令位置の公開資料なし） · `00bb6950`（命令位置の公開資料なし）

~~~diff
- 00bb6fac ["INT_ADD", "register:40f0:8", ["const:bb6fac:8", "const:4:8"]]
- 00bb6fac ["CALL", null, ["callee:00ba8ac4:8"]]
+ 00bb6ff0 ["INT_ADD", "register:40f0:8", ["const:bb6ff0:8", "const:4:8"]]
+ 00bb6ff0 ["CALL", null, ["callee:00ba8ac4:8"]]
- 00bb6fac bytes b5c6ff97
+ 00bb6ff0 bytes b5c6ff97
- 00bb68fc ["INT_ADD", "register:40f0:8", ["const:bb68fc:8", "const:4:8"]]
- 00bb68fc ["CALL", null, ["callee:00be1570:8"]]
+ 00bb6940 ["INT_ADD", "register:40f0:8", ["const:bb6940:8", "const:4:8"]]
+ 00bb6940 ["CALL", null, ["callee:00be1570:8"]]
- 00bb68fc bytes 09ab0094
+ 00bb6940 bytes 0cab0094
- 00bb690c ["INT_ADD", "register:40f0:8", ["const:bb690c:8", "const:4:8"]]
- 00bb690c ["CALL", null, ["callee:00be1580:8"]]
+ 00bb6950 ["INT_ADD", "register:40f0:8", ["const:bb6950:8", "const:4:8"]]
+ 00bb6950 ["CALL", null, ["callee:00be1580:8"]]
- 00bb690c bytes 09ab0094
+ 00bb6950 bytes 0cab0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3324f6d21dd3f5df80404e5ab6dd6c7"></a>

### [`00bb75c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb75c8.md) → [`00bb760c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb760c.md) _ZNSt6__ndk117moneypunct_bynameIwLb1EE4initEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be18c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18c0.md) · 呼出先 17件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`006ad8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8e8.md) [`00b750e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750e4.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00baf6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf6e4.md)
- 新版 呼出元 1件 [`00be1910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1910.md) · 呼出先 17件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`006ad8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8e8.md) [`00b75128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75128.md) [`00ba8ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8ac4.md) [`00baf728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf728.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.78% / 新版 99.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb7cdc",
      "incomplete_value": false,
      "site": "00bb7cec",
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
            "const:16d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb7c98",
      "incomplete_value": false,
      "site": "00bb7ca8",
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
            "const:e2:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb7cdc",
      "PARAM",
      [
        "storage",
        "002a10e2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb7cdc",
      "PARAM",
      [
        "storage",
        "002a116d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb7ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb75c8.md#insn-00bb7ca8) · [`00bb75f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb75c8.md#insn-00bb75f8) · [`00bb7608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb75c8.md#insn-00bb7608)
- 新版 `00bb7cec`（命令位置の公開資料なし） · `00bb763c`（命令位置の公開資料なし） · `00bb764c`（命令位置の公開資料なし）

~~~diff
- 00bb7ca8 ["INT_ADD", "register:40f0:8", ["const:bb7ca8:8", "const:4:8"]]
- 00bb7ca8 ["CALL", null, ["callee:00ba8ac4:8"]]
+ 00bb7cec ["INT_ADD", "register:40f0:8", ["const:bb7cec:8", "const:4:8"]]
+ 00bb7cec ["CALL", null, ["callee:00ba8ac4:8"]]
- 00bb7ca8 bytes 76c3ff97
+ 00bb7cec bytes 76c3ff97
- 00bb75f8 ["INT_ADD", "register:40f0:8", ["const:bb75f8:8", "const:4:8"]]
- 00bb75f8 ["CALL", null, ["callee:00be1570:8"]]
+ 00bb763c ["INT_ADD", "register:40f0:8", ["const:bb763c:8", "const:4:8"]]
+ 00bb763c ["CALL", null, ["callee:00be1570:8"]]
- 00bb75f8 bytes caa70094
+ 00bb763c bytes cda70094
- 00bb7608 ["INT_ADD", "register:40f0:8", ["const:bb7608:8", "const:4:8"]]
- 00bb7608 ["CALL", null, ["callee:00be1580:8"]]
+ 00bb764c ["INT_ADD", "register:40f0:8", ["const:bb764c:8", "const:4:8"]]
+ 00bb764c ["CALL", null, ["callee:00be1580:8"]]
- 00bb7608 bytes caa70094
+ 00bb764c bytes cda70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-561f21ce8f1a4f9a5a1e5888cb3c60d1"></a>

### [`00bb7f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7f08.md) → [`00bb7f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7f4c.md) _ZNSt6__ndk17codecvtIwc9mbstate_tED2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00bdd9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9e0.md) [`00be1ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ae0.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md)
- 新版 呼出元 2件 [`00bdda30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda30.md) [`00be1b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1b30.md) · 呼出先 5件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md) [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md)

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
      "definition_site": "00bb7f74",
      "incomplete_value": true,
      "site": "00bb7f78",
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
      "definition_site": "00bb7f30",
      "incomplete_value": true,
      "site": "00bb7f34",
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
      "definition_site": "00bb7fdc",
      "incomplete_value": true,
      "site": "00bb7fdc",
      "value": [
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
    "old": {
      "definition_site": "00bb7f98",
      "incomplete_value": true,
      "site": "00bb7f98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:950:8"
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
      "definition_site": "00bb7f90",
      "incomplete_value": true,
      "site": "00bb7f94",
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
      "definition_site": "00bb7f4c",
      "incomplete_value": true,
      "site": "00bb7f50",
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
      "00bb7f6c",
      "READ",
      [
        "storage",
        "00c1bf60",
        null,
        "pointer"
      ]
    ],
    [
      "00bb7f78",
      "DATA",
      [
        "storage",
        "00c13ac8",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00bb7f84",
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
      "00bb7f6c",
      "READ",
      [
        "storage",
        "00c1bfb0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb7f78",
      "DATA",
      [
        "storage",
        "00c13b18",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00bb7f84",
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

- 旧版 [`00bb7f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7f08.md#insn-00bb7f78) · [`00bb7f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7f08.md#insn-00bb7f7c)
- 新版 `00bb7fbc`（命令位置の公開資料なし） · `00bb7fc0`（命令位置の公開資料なし） · `00bb7f7c`（命令位置の公開資料なし）

~~~diff
- 00bb7f78 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00bb7f78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb7f78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb7f78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb7fbc ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00bb7fbc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb7fbc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb7fbc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb7f78 bytes 00602591
+ 00bb7fbc bytes 00602691
- 00bb7f7c ["INT_ADD", "register:40f0:8", ["const:bb7f7c:8", "const:4:8"]]
- 00bb7f7c ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb7fc0 ["INT_ADD", "register:40f0:8", ["const:bb7fc0:8", "const:4:8"]]
+ 00bb7fc0 ["CALL", null, ["callee:00bdb000:8"]]
- 00bb7f7c bytes 0d8c0094
+ 00bb7fc0 bytes 108c0094
+ 00bb7f7c ["COPY", "register:4040:8", ["const:10a2000:8"]]
+ 00bb7f7c bytes 482700f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb54bb0ec729d25a7d4eb88b6ad5a05b"></a>

### [`00bb858c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb858c.md) → [`00bb85d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb85d0.md) FUN_00bb85d0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bb8620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8620.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 1件 [`00bb8664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8664.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

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
      "definition_site": "00bb85f0",
      "incomplete_value": true,
      "site": "00bb85f4",
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
      "definition_site": "00bb85ac",
      "incomplete_value": true,
      "site": "00bb85b0",
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
      "00bb85e8",
      "READ",
      [
        "storage",
        "00c1bf18",
        null,
        "pointer"
      ]
    ],
    [
      "00bb85f4",
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
      "00bb85e8",
      "READ",
      [
        "storage",
        "00c1bf68",
        null,
        "pointer"
      ]
    ],
    [
      "00bb85f4",
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

- 旧版 [`00bb85a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb858c.md#insn-00bb85a4) · [`00bb85d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb858c.md#insn-00bb85d4) · [`00bb85f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb858c.md#insn-00bb85f0)
- 新版 `00bb85e8`（命令位置の公開資料なし） · `00bb8618`（命令位置の公開資料なし） · `00bb8634`（命令位置の公開資料なし）

~~~diff
- 00bb85a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f18:8"]]
- 00bb85a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb85e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f68:8"]]
+ 00bb85e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb85a4 bytes 088d47f9
+ 00bb85e8 bytes 08b547f9
- 00bb85d4 ["INT_ADD", "register:40f0:8", ["const:bb85d4:8", "const:4:8"]]
- 00bb85d4 ["CALL", null, ["callee:00bdb060:8"]]
+ 00bb8618 ["INT_ADD", "register:40f0:8", ["const:bb8618:8", "const:4:8"]]
+ 00bb8618 ["CALL", null, ["callee:00bdb060:8"]]
- 00bb85d4 bytes 8f8a0094
+ 00bb8618 bytes 928a0094
- 00bb85f0 ["INT_ADD", "register:40f0:8", ["const:bb85f0:8", "const:4:8"]]
- 00bb85f0 ["CALL", null, ["callee:00bdb060:8"]]
+ 00bb8634 ["INT_ADD", "register:40f0:8", ["const:bb8634:8", "const:4:8"]]
+ 00bb8634 ["CALL", null, ["callee:00bdb060:8"]]
- 00bb85f0 bytes 888a0094
+ 00bb8634 bytes 8b8a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c26addce7345215baa6d90282d768420"></a>

### [`00bb864c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb864c.md) → [`00bb8690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8690.md) FUN_00bb8690

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bb86e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb86e0.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 1件 [`00bb8724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8724.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

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
      "definition_site": "00bb86b0",
      "incomplete_value": true,
      "site": "00bb86b4",
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
      "definition_site": "00bb866c",
      "incomplete_value": true,
      "site": "00bb8670",
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
      "00bb86a8",
      "READ",
      [
        "storage",
        "00c1bf20",
        null,
        "pointer"
      ]
    ],
    [
      "00bb86b4",
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
      "00bb86a8",
      "READ",
      [
        "storage",
        "00c1bf70",
        null,
        "pointer"
      ]
    ],
    [
      "00bb86b4",
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

- 旧版 [`00bb8664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb864c.md#insn-00bb8664) · [`00bb8694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb864c.md#insn-00bb8694) · [`00bb86b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb864c.md#insn-00bb86b0)
- 新版 `00bb86a8`（命令位置の公開資料なし） · `00bb86d8`（命令位置の公開資料なし） · `00bb86f4`（命令位置の公開資料なし）

~~~diff
- 00bb8664 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
- 00bb8664 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb86a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f70:8"]]
+ 00bb86a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb8664 bytes 089147f9
+ 00bb86a8 bytes 08b947f9
- 00bb8694 ["INT_ADD", "register:40f0:8", ["const:bb8694:8", "const:4:8"]]
- 00bb8694 ["CALL", null, ["callee:00bdb060:8"]]
+ 00bb86d8 ["INT_ADD", "register:40f0:8", ["const:bb86d8:8", "const:4:8"]]
+ 00bb86d8 ["CALL", null, ["callee:00bdb060:8"]]
- 00bb8694 bytes 5f8a0094
+ 00bb86d8 bytes 628a0094
- 00bb86b0 ["INT_ADD", "register:40f0:8", ["const:bb86b0:8", "const:4:8"]]
- 00bb86b0 ["CALL", null, ["callee:00bdb060:8"]]
+ 00bb86f4 ["INT_ADD", "register:40f0:8", ["const:bb86f4:8", "const:4:8"]]
+ 00bb86f4 ["CALL", null, ["callee:00bdb060:8"]]
- 00bb86b0 bytes 588a0094
+ 00bb86f4 bytes 5b8a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e2a8cd33c850e5612b77569fae39b35"></a>

### [`00bb870c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb870c.md) → [`00bb8750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8750.md) FUN_00bb8750

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bb87a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb87a0.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 1件 [`00bb87e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb87e4.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

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
      "definition_site": "00bb8770",
      "incomplete_value": true,
      "site": "00bb8774",
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
      "definition_site": "00bb872c",
      "incomplete_value": true,
      "site": "00bb8730",
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
      "00bb8768",
      "READ",
      [
        "storage",
        "00c1bf28",
        null,
        "pointer"
      ]
    ],
    [
      "00bb8774",
      "DATA",
      [
        "storage",
        "00c15718",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00bb8768",
      "READ",
      [
        "storage",
        "00c1bf78",
        null,
        "pointer"
      ]
    ],
    [
      "00bb8774",
      "DATA",
      [
        "storage",
        "00c15768",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb870c.md#insn-00bb8724) · [`00bb8754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb870c.md#insn-00bb8754) · [`00bb8770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb870c.md#insn-00bb8770)
- 新版 `00bb8768`（命令位置の公開資料なし） · `00bb8798`（命令位置の公開資料なし） · `00bb87b4`（命令位置の公開資料なし）

~~~diff
- 00bb8724 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f28:8"]]
- 00bb8724 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb8768 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f78:8"]]
+ 00bb8768 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb8724 bytes 089547f9
+ 00bb8768 bytes 08bd47f9
- 00bb8754 ["INT_ADD", "register:40f0:8", ["const:bb8754:8", "const:4:8"]]
- 00bb8754 ["CALL", null, ["callee:00bdb060:8"]]
+ 00bb8798 ["INT_ADD", "register:40f0:8", ["const:bb8798:8", "const:4:8"]]
+ 00bb8798 ["CALL", null, ["callee:00bdb060:8"]]
- 00bb8754 bytes 2f8a0094
+ 00bb8798 bytes 328a0094
- 00bb8770 ["INT_ADD", "register:40f0:8", ["const:bb8770:8", "const:4:8"]]
- 00bb8770 ["CALL", null, ["callee:00bdb060:8"]]
+ 00bb87b4 ["INT_ADD", "register:40f0:8", ["const:bb87b4:8", "const:4:8"]]
+ 00bb87b4 ["CALL", null, ["callee:00bdb060:8"]]
- 00bb8770 bytes 288a0094
+ 00bb87b4 bytes 2b8a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-322c8f0b286ed5c9db23def04d88c2e8"></a>

### [`00bb87cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb87cc.md) → [`00bb8810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8810.md) FUN_00bb8810

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bb8860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8860.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 1件 [`00bb88a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb88a4.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

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
      "definition_site": "00bb8830",
      "incomplete_value": true,
      "site": "00bb8834",
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
      "definition_site": "00bb87ec",
      "incomplete_value": true,
      "site": "00bb87f0",
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
      "00bb8828",
      "READ",
      [
        "storage",
        "00c1bf30",
        null,
        "pointer"
      ]
    ],
    [
      "00bb8834",
      "DATA",
      [
        "storage",
        "00c157a0",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00bb8828",
      "READ",
      [
        "storage",
        "00c1bf80",
        null,
        "pointer"
      ]
    ],
    [
      "00bb8834",
      "DATA",
      [
        "storage",
        "00c157f0",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb87e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb87cc.md#insn-00bb87e4) · [`00bb8814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb87cc.md#insn-00bb8814) · [`00bb8830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb87cc.md#insn-00bb8830)
- 新版 `00bb8828`（命令位置の公開資料なし） · `00bb8858`（命令位置の公開資料なし） · `00bb8874`（命令位置の公開資料なし）

~~~diff
- 00bb87e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f30:8"]]
- 00bb87e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb8828 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f80:8"]]
+ 00bb8828 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb87e4 bytes 089947f9
+ 00bb8828 bytes 08c147f9
- 00bb8814 ["INT_ADD", "register:40f0:8", ["const:bb8814:8", "const:4:8"]]
- 00bb8814 ["CALL", null, ["callee:00bdb060:8"]]
+ 00bb8858 ["INT_ADD", "register:40f0:8", ["const:bb8858:8", "const:4:8"]]
+ 00bb8858 ["CALL", null, ["callee:00bdb060:8"]]
- 00bb8814 bytes ff890094
+ 00bb8858 bytes 028a0094
- 00bb8830 ["INT_ADD", "register:40f0:8", ["const:bb8830:8", "const:4:8"]]
- 00bb8830 ["CALL", null, ["callee:00bdb060:8"]]
+ 00bb8874 ["INT_ADD", "register:40f0:8", ["const:bb8874:8", "const:4:8"]]
+ 00bb8874 ["CALL", null, ["callee:00bdb060:8"]]
- 00bb8830 bytes f8890094
+ 00bb8874 bytes fb890094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b61f16878e0679f453309cc85e8a510a"></a>

### [`00bb8a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8a1c.md) → [`00bb8a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8a60.md) FUN_00bb8a60

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00ba7a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7a20.md) [`00bb8a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8a34.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`00ba7a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7a64.md) [`00bb8a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8a78.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00bb8a70",
      "incomplete_value": false,
      "site": "00bb8a74",
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
            "const:39d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8a2c",
      "incomplete_value": false,
      "site": "00bb8a30",
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
            "const:303:8"
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
      "00bb8a70",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb8a70",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8a1c.md#insn-00bb8a30) · [`00bb8a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8a1c.md#insn-00bb8a2c)
- 新版 `00bb8a74`（命令位置の公開資料なし） · `00bb8a70`（命令位置の公開資料なし）

~~~diff
- 00bb8a30 ["INT_ADD", "register:40f0:8", ["const:bb8a30:8", "const:4:8"]]
- 00bb8a30 ["CALL", null, ["callee:00418c38:8"]]
+ 00bb8a74 ["INT_ADD", "register:40f0:8", ["const:bb8a74:8", "const:4:8"]]
+ 00bb8a74 ["CALL", null, ["callee:00418c38:8"]]
- 00bb8a30 bytes 8280e197
+ 00bb8a74 bytes 7180e197
- 00bb8a2c ["COPY", "tmp:0:8", ["const:303:8"]]
- 00bb8a2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb8a2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb8a2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb8a70 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00bb8a70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb8a70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb8a70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb8a2c bytes 000c0c91
+ 00bb8a70 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7e405969791417a200ddf09ccc12c71"></a>

### [`00bb8cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8cec.md) → [`00bb8d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8d30.md) FUN_00bb8d30

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bafc28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafc28.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00bafc6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00bafc6c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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
      "definition_site": "00bb8d4c",
      "incomplete_value": true,
      "site": "00bb8d50",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a2000:8"
              ],
              [
                "leaf",
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8d08",
      "incomplete_value": true,
      "site": "00bb8d0c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a2000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb8d64",
      "incomplete_value": true,
      "site": "00bb8d68",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a2000:8"
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
      "definition_site": "00bb8d20",
      "incomplete_value": true,
      "site": "00bb8d24",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a2000:8"
              ],
              [
                "leaf",
                "const:d90:8"
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
      "definition_site": "00bb8d7c",
      "incomplete_value": true,
      "site": "00bb8d80",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a2000:8"
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
    "old": {
      "definition_site": "00bb8d38",
      "incomplete_value": true,
      "site": "00bb8d3c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a2000:8"
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
      "00bb8d40",
      "READ",
      [
        "storage",
        "010a2d98",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb8d4c",
      "READ",
      [
        "storage",
        "010a2da8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8d58",
      "READ",
      [
        "storage",
        "010a2d80",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb8d40",
      "READ",
      [
        "storage",
        "010a2dd8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb8d4c",
      "READ",
      [
        "storage",
        "010a2de8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8d58",
      "READ",
      [
        "storage",
        "010a2dc0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8cec.md#insn-00bb8d0c) · [`00bb8d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8cec.md#insn-00bb8d24) · [`00bb8d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8cec.md#insn-00bb8d3c)
- 新版 `00bb8d50`（命令位置の公開資料なし） · `00bb8d68`（命令位置の公開資料なし） · `00bb8d80`（命令位置の公開資料なし）

~~~diff
- 00bb8d0c ["INT_ADD", "register:40f0:8", ["const:bb8d0c:8", "const:4:8"]]
- 00bb8d0c ["CALL", null, ["callee:00bdb060:8"]]
+ 00bb8d50 ["INT_ADD", "register:40f0:8", ["const:bb8d50:8", "const:4:8"]]
+ 00bb8d50 ["CALL", null, ["callee:00bdb060:8"]]
- 00bb8d0c bytes c1880094
+ 00bb8d50 bytes c4880094
- 00bb8d24 ["INT_ADD", "register:40f0:8", ["const:bb8d24:8", "const:4:8"]]
- 00bb8d24 ["CALL", null, ["callee:00bdb060:8"]]
+ 00bb8d68 ["INT_ADD", "register:40f0:8", ["const:bb8d68:8", "const:4:8"]]
+ 00bb8d68 ["CALL", null, ["callee:00bdb060:8"]]
- 00bb8d24 bytes bb880094
+ 00bb8d68 bytes be880094
- 00bb8d3c ["INT_ADD", "register:40f0:8", ["const:bb8d3c:8", "const:4:8"]]
- 00bb8d3c ["CALL", null, ["callee:00bdb060:8"]]
+ 00bb8d80 ["INT_ADD", "register:40f0:8", ["const:bb8d80:8", "const:4:8"]]
+ 00bb8d80 ["CALL", null, ["callee:00bdb060:8"]]
- 00bb8d3c bytes b5880094
+ 00bb8d80 bytes b8880094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b94032c3baf4a407c772488a6aabd327"></a>

### [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) → [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) FUN_00bb9148

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 96件 [`00b8a9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a9d8.md) [`00b8d680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8d680.md) [`00b8deb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8deb0.md) [`00b90af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b90af4.md) [`00b911d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b911d8.md) · 呼出先 1件 [`00bd6df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6df0.md)
- 新版 呼出元 96件 [`00b8aa1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aa1c.md) [`00b8d6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d6c4.md) [`00b8def4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8def4.md) [`00b90b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90b38.md) [`00b9121c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b9121c.md) · 呼出先 1件 [`00bd6e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e30.md)

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
      "definition_site": "00bb916c",
      "incomplete_value": true,
      "site": "00bb9170",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9128",
      "incomplete_value": true,
      "site": "00bb912c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f88:8"
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
      "00bb916c",
      "READ",
      [
        "storage",
        "00c1bf88",
        null,
        "pointer"
      ]
    ],
    [
      "00bb916c",
      "PARAM",
      [
        "storage",
        "010a2ab8",
        "_ZNSt6__ndk16locale2id9__next_idE",
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00bb916c",
      "READ",
      [
        "storage",
        "00c1bfd8",
        null,
        "pointer"
      ]
    ],
    [
      "00bb916c",
      "PARAM",
      [
        "storage",
        "010a2af8",
        "_ZNSt6__ndk16locale2id9__next_idE",
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb912c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md#insn-00bb912c) · [`00bb9128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md#insn-00bb9128)
- 新版 `00bb9170`（命令位置の公開資料なし） · `00bb916c`（命令位置の公開資料なし）

~~~diff
- 00bb912c ["INT_ADD", "register:40f0:8", ["const:bb912c:8", "const:4:8"]]
- 00bb912c ["CALL", null, ["callee:00bd6e30:8"]]
+ 00bb9170 ["INT_ADD", "register:40f0:8", ["const:bb9170:8", "const:4:8"]]
+ 00bb9170 ["CALL", null, ["callee:00bd6e30:8"]]
- 00bb912c bytes 31770094
+ 00bb9170 bytes 30770094
- 00bb9128 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f88:8"]]
- 00bb9128 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb916c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fd8:8"]]
+ 00bb916c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb9128 bytes 21c447f9
+ 00bb916c bytes 21ec47f9
~~~


<a id="compare-fd9bf6e62cd7fa76da4c24295dbc2836"></a>

### [`00bb9148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9148.md) → [`00bb918c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb918c.md) FUN_00bb918c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00bdef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef40.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md) [`00bdef90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef90.md) [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md)

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
      "definition_site": "00bb91ac",
      "incomplete_value": true,
      "site": "00bb91b0",
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
      "definition_site": "00bb9168",
      "incomplete_value": true,
      "site": "00bb916c",
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
      "definition_site": "00bb91c4",
      "incomplete_value": true,
      "site": "00bb91c8",
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
      "definition_site": "00bb9180",
      "incomplete_value": true,
      "site": "00bb9184",
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
      "00bb91a4",
      "READ",
      [
        "storage",
        "00c1bf50",
        null,
        "pointer"
      ]
    ],
    [
      "00bb91b0",
      "DATA",
      [
        "storage",
        "00c139d8",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00bb91bc",
      "READ",
      [
        "storage",
        "00c1bf48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb91a4",
      "READ",
      [
        "storage",
        "00c1bfa0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb91b0",
      "DATA",
      [
        "storage",
        "00c13a28",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00bb91bc",
      "READ",
      [
        "storage",
        "00c1bf98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9148.md#insn-00bb9160) · [`00bb9170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9148.md#insn-00bb9170) · [`00bb9178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9148.md#insn-00bb9178)
- 新版 `00bb91a4`（命令位置の公開資料なし） · `00bb91b4`（命令位置の公開資料なし） · `00bb91bc`（命令位置の公開資料なし）

~~~diff
- 00bb9160 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
- 00bb9160 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb91a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
+ 00bb91a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb9160 bytes 08a947f9
+ 00bb91a4 bytes 08d147f9
- 00bb9170 ["INT_ADD", "register:40f0:8", ["const:bb9170:8", "const:4:8"]]
- 00bb9170 ["CALL", null, ["callee:00be1930:8"]]
+ 00bb91b4 ["INT_ADD", "register:40f0:8", ["const:bb91b4:8", "const:4:8"]]
+ 00bb91b4 ["CALL", null, ["callee:00be1930:8"]]
- 00bb9170 bytes dca10094
+ 00bb91b4 bytes dfa10094
- 00bb9178 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
- 00bb9178 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb91bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f98:8"]]
+ 00bb91bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb9178 bytes 08a547f9
+ 00bb91bc bytes 08cd47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4392e768cc357eca942cfa027b55bc8"></a>

### [`00bb92b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb92b8.md) → [`00bb92fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb92fc.md) FUN_00bb92fc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b8b0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b0d8.md) [`00b8e5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e5b8.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be1d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d30.md)
- 新版 呼出元 2件 [`00b8b11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b11c.md) [`00b8e5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e5fc.md) · 呼出先 5件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md) [`00be1d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d80.md)

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
      "definition_site": "00bb93f8",
      "incomplete_value": true,
      "site": "00bb93f8",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb93b4",
      "incomplete_value": true,
      "site": "00bb93b4",
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
      "definition_site": "00bb9354",
      "incomplete_value": true,
      "site": "00bb9364",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:990:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9310",
      "incomplete_value": true,
      "site": "00bb9320",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:950:8"
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
      "definition_site": "00bb93d8",
      "incomplete_value": false,
      "site": "00bb93dc",
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
      "definition_site": "00bb9394",
      "incomplete_value": false,
      "site": "00bb9398",
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
      "00bb934c",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9354",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb93d8",
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
      "00bb934c",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9354",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb93d8",
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

- 旧版 [`00bb9320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb92b8.md#insn-00bb9320) · [`00bb9398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb92b8.md#insn-00bb9398) · [`00bb93b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb92b8.md#insn-00bb93b0)
- 新版 `00bb9364`（命令位置の公開資料なし） · `00bb93dc`（命令位置の公開資料なし） · `00bb93f4`（命令位置の公開資料なし）

~~~diff
- 00bb9320 ["INT_ADD", "register:40f0:8", ["const:bb9320:8", "const:4:8"]]
- 00bb9320 ["CALL", null, ["callee:00be1d80:8"]]
+ 00bb9364 ["INT_ADD", "register:40f0:8", ["const:bb9364:8", "const:4:8"]]
+ 00bb9364 ["CALL", null, ["callee:00be1d80:8"]]
- 00bb9320 bytes 84a20094
+ 00bb9364 bytes 87a20094
- 00bb9398 ["INT_ADD", "register:40f0:8", ["const:bb9398:8", "const:4:8"]]
- 00bb9398 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb93dc ["INT_ADD", "register:40f0:8", ["const:bb93dc:8", "const:4:8"]]
+ 00bb93dc ["CALL", null, ["callee:00bdb000:8"]]
- 00bb9398 bytes 06870094
+ 00bb93dc bytes 09870094
- 00bb93b0 ["INT_ADD", "register:40f0:8", ["const:bb93b0:8", "const:4:8"]]
- 00bb93b0 ["CALL", null, ["callee:00be1570:8"]]
+ 00bb93f4 ["INT_ADD", "register:40f0:8", ["const:bb93f4:8", "const:4:8"]]
+ 00bb93f4 ["CALL", null, ["callee:00be1570:8"]]
- 00bb93b0 bytes 5ca00094
+ 00bb93f4 bytes 5fa00094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-480d8697f5c715366fb0f8b65980e13c"></a>

### [`00bb93e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb93e0.md) → [`00bb9424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9424.md) FUN_00bb9424

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b8b514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b514.md) [`00b8e9e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e9e8.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be1d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d30.md)
- 新版 呼出元 2件 [`00b8b558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b558.md) [`00b8ea2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ea2c.md) · 呼出先 5件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md) [`00be1d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d80.md)

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
      "definition_site": "00bb9520",
      "incomplete_value": true,
      "site": "00bb9520",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb94dc",
      "incomplete_value": true,
      "site": "00bb94dc",
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
      "definition_site": "00bb947c",
      "incomplete_value": true,
      "site": "00bb948c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:990:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9438",
      "incomplete_value": true,
      "site": "00bb9448",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:950:8"
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
      "definition_site": "00bb9500",
      "incomplete_value": false,
      "site": "00bb9504",
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
      "definition_site": "00bb94bc",
      "incomplete_value": false,
      "site": "00bb94c0",
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
      "00bb9474",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb947c",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9500",
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
      "00bb9474",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb947c",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9500",
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

- 旧版 [`00bb9448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb93e0.md#insn-00bb9448) · [`00bb94c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb93e0.md#insn-00bb94c0) · [`00bb94d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb93e0.md#insn-00bb94d8)
- 新版 `00bb948c`（命令位置の公開資料なし） · `00bb9504`（命令位置の公開資料なし） · `00bb951c`（命令位置の公開資料なし）

~~~diff
- 00bb9448 ["INT_ADD", "register:40f0:8", ["const:bb9448:8", "const:4:8"]]
- 00bb9448 ["CALL", null, ["callee:00be1d80:8"]]
+ 00bb948c ["INT_ADD", "register:40f0:8", ["const:bb948c:8", "const:4:8"]]
+ 00bb948c ["CALL", null, ["callee:00be1d80:8"]]
- 00bb9448 bytes 3aa20094
+ 00bb948c bytes 3da20094
- 00bb94c0 ["INT_ADD", "register:40f0:8", ["const:bb94c0:8", "const:4:8"]]
- 00bb94c0 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb9504 ["INT_ADD", "register:40f0:8", ["const:bb9504:8", "const:4:8"]]
+ 00bb9504 ["CALL", null, ["callee:00bdb000:8"]]
- 00bb94c0 bytes bc860094
+ 00bb9504 bytes bf860094
- 00bb94d8 ["INT_ADD", "register:40f0:8", ["const:bb94d8:8", "const:4:8"]]
- 00bb94d8 ["CALL", null, ["callee:00be1570:8"]]
+ 00bb951c ["INT_ADD", "register:40f0:8", ["const:bb951c:8", "const:4:8"]]
+ 00bb951c ["CALL", null, ["callee:00be1570:8"]]
- 00bb94d8 bytes 12a00094
+ 00bb951c bytes 15a00094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9be1faa8aa7a6bf9ce926b9d22e729a7"></a>

### [`00bb9508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9508.md) → [`00bb954c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb954c.md) FUN_00bb954c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b8b950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b950.md) [`00b8ee18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8ee18.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be1d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d40.md)
- 新版 呼出元 2件 [`00b8b994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b994.md) [`00b8ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ee5c.md) · 呼出先 5件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md) [`00be1d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d90.md)

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
      "definition_site": "00bb9678",
      "incomplete_value": true,
      "site": "00bb9678",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9634",
      "incomplete_value": true,
      "site": "00bb9634",
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
      "definition_site": "00bb95c0",
      "incomplete_value": true,
      "site": "00bb95d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:990:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb957c",
      "incomplete_value": true,
      "site": "00bb958c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:950:8"
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
      "definition_site": "00bb9658",
      "incomplete_value": false,
      "site": "00bb965c",
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
      "definition_site": "00bb9614",
      "incomplete_value": false,
      "site": "00bb9618",
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
      "00bb95b8",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb95c0",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9658",
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
      "00bb95b8",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb95c0",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9658",
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

- 旧版 [`00bb958c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9508.md#insn-00bb958c) · [`00bb9618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9508.md#insn-00bb9618) · [`00bb9630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9508.md#insn-00bb9630)
- 新版 `00bb95d0`（命令位置の公開資料なし） · `00bb965c`（命令位置の公開資料なし） · `00bb9674`（命令位置の公開資料なし）

~~~diff
- 00bb958c ["INT_ADD", "register:40f0:8", ["const:bb958c:8", "const:4:8"]]
- 00bb958c ["CALL", null, ["callee:00be1d90:8"]]
+ 00bb95d0 ["INT_ADD", "register:40f0:8", ["const:bb95d0:8", "const:4:8"]]
+ 00bb95d0 ["CALL", null, ["callee:00be1d90:8"]]
- 00bb958c bytes eda10094
+ 00bb95d0 bytes f0a10094
- 00bb9618 ["INT_ADD", "register:40f0:8", ["const:bb9618:8", "const:4:8"]]
- 00bb9618 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb965c ["INT_ADD", "register:40f0:8", ["const:bb965c:8", "const:4:8"]]
+ 00bb965c ["CALL", null, ["callee:00bdb000:8"]]
- 00bb9618 bytes 66860094
+ 00bb965c bytes 69860094
- 00bb9630 ["INT_ADD", "register:40f0:8", ["const:bb9630:8", "const:4:8"]]
- 00bb9630 ["CALL", null, ["callee:00be1570:8"]]
+ 00bb9674 ["INT_ADD", "register:40f0:8", ["const:bb9674:8", "const:4:8"]]
+ 00bb9674 ["CALL", null, ["callee:00be1570:8"]]
- 00bb9630 bytes bc9f0094
+ 00bb9674 bytes bf9f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc804b78801d6a0725447c3550ecf02f"></a>

### [`00bb9660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9660.md) → [`00bb96a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb96a4.md) FUN_00bb96a4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b8bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8bd8c.md) [`00b8f248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8f248.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be1d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d40.md)
- 新版 呼出元 2件 [`00b8bdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8bdd0.md) [`00b8f28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f28c.md) · 呼出先 5件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md) [`00be1d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d90.md)

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
      "definition_site": "00bb97cc",
      "incomplete_value": true,
      "site": "00bb97cc",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9788",
      "incomplete_value": true,
      "site": "00bb9788",
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
      "definition_site": "00bb9718",
      "incomplete_value": true,
      "site": "00bb9728",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:990:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb96d4",
      "incomplete_value": true,
      "site": "00bb96e4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:950:8"
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
      "definition_site": "00bb97ac",
      "incomplete_value": false,
      "site": "00bb97b0",
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
      "definition_site": "00bb9768",
      "incomplete_value": false,
      "site": "00bb976c",
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
      "00bb9710",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9718",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb97ac",
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
      "00bb9710",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9718",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb97ac",
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

- 旧版 [`00bb96e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9660.md#insn-00bb96e4) · [`00bb976c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9660.md#insn-00bb976c) · [`00bb9784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9660.md#insn-00bb9784)
- 新版 `00bb9728`（命令位置の公開資料なし） · `00bb97b0`（命令位置の公開資料なし） · `00bb97c8`（命令位置の公開資料なし）

~~~diff
- 00bb96e4 ["INT_ADD", "register:40f0:8", ["const:bb96e4:8", "const:4:8"]]
- 00bb96e4 ["CALL", null, ["callee:00be1d90:8"]]
+ 00bb9728 ["INT_ADD", "register:40f0:8", ["const:bb9728:8", "const:4:8"]]
+ 00bb9728 ["CALL", null, ["callee:00be1d90:8"]]
- 00bb96e4 bytes 97a10094
+ 00bb9728 bytes 9aa10094
- 00bb976c ["INT_ADD", "register:40f0:8", ["const:bb976c:8", "const:4:8"]]
- 00bb976c ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb97b0 ["INT_ADD", "register:40f0:8", ["const:bb97b0:8", "const:4:8"]]
+ 00bb97b0 ["CALL", null, ["callee:00bdb000:8"]]
- 00bb976c bytes 11860094
+ 00bb97b0 bytes 14860094
- 00bb9784 ["INT_ADD", "register:40f0:8", ["const:bb9784:8", "const:4:8"]]
- 00bb9784 ["CALL", null, ["callee:00be1570:8"]]
+ 00bb97c8 ["INT_ADD", "register:40f0:8", ["const:bb97c8:8", "const:4:8"]]
+ 00bb97c8 ["CALL", null, ["callee:00be1570:8"]]
- 00bb9784 bytes 679f0094
+ 00bb97c8 bytes 6a9f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20b09edb3b8698a33a7f757a9dfc3e01"></a>

### [`00bb97b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb97b4.md) → [`00bb97f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb97f8.md) FUN_00bb97f8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b8c1c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8c1c8.md) [`00b8f678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8f678.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be1d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d40.md)
- 新版 呼出元 2件 [`00b8c20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c20c.md) [`00b8f6bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f6bc.md) · 呼出先 5件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md) [`00be1d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d90.md)

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
      "definition_site": "00bb9914",
      "incomplete_value": true,
      "site": "00bb9914",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb98d0",
      "incomplete_value": true,
      "site": "00bb98d0",
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
      "definition_site": "00bb986c",
      "incomplete_value": true,
      "site": "00bb987c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:990:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9828",
      "incomplete_value": true,
      "site": "00bb9838",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:950:8"
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
      "definition_site": "00bb98f4",
      "incomplete_value": false,
      "site": "00bb98f8",
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
      "definition_site": "00bb98b0",
      "incomplete_value": false,
      "site": "00bb98b4",
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
      "00bb9864",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb986c",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb98f4",
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
      "00bb9864",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb986c",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb98f4",
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

- 旧版 [`00bb9838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb97b4.md#insn-00bb9838) · [`00bb98b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb97b4.md#insn-00bb98b4) · [`00bb98cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb97b4.md#insn-00bb98cc)
- 新版 `00bb987c`（命令位置の公開資料なし） · `00bb98f8`（命令位置の公開資料なし） · `00bb9910`（命令位置の公開資料なし）

~~~diff
- 00bb9838 ["INT_ADD", "register:40f0:8", ["const:bb9838:8", "const:4:8"]]
- 00bb9838 ["CALL", null, ["callee:00be1d90:8"]]
+ 00bb987c ["INT_ADD", "register:40f0:8", ["const:bb987c:8", "const:4:8"]]
+ 00bb987c ["CALL", null, ["callee:00be1d90:8"]]
- 00bb9838 bytes 42a10094
+ 00bb987c bytes 45a10094
- 00bb98b4 ["INT_ADD", "register:40f0:8", ["const:bb98b4:8", "const:4:8"]]
- 00bb98b4 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb98f8 ["INT_ADD", "register:40f0:8", ["const:bb98f8:8", "const:4:8"]]
+ 00bb98f8 ["CALL", null, ["callee:00bdb000:8"]]
- 00bb98b4 bytes bf850094
+ 00bb98f8 bytes c2850094
- 00bb98cc ["INT_ADD", "register:40f0:8", ["const:bb98cc:8", "const:4:8"]]
- 00bb98cc ["CALL", null, ["callee:00be1570:8"]]
+ 00bb9910 ["INT_ADD", "register:40f0:8", ["const:bb9910:8", "const:4:8"]]
+ 00bb9910 ["CALL", null, ["callee:00be1570:8"]]
- 00bb98cc bytes 159f0094
+ 00bb9910 bytes 189f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf69f4b0f101c942d5d0f661b233df47"></a>

### [`00bb98fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb98fc.md) → [`00bb9940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9940.md) FUN_00bb9940

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b8c604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8c604.md) [`00b8faa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8faa8.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be1d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d40.md)
- 新版 呼出元 2件 [`00b8c648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c648.md) [`00b8faec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8faec.md) · 呼出先 5件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md) [`00be1d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d90.md)

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
      "definition_site": "00bb9a5c",
      "incomplete_value": true,
      "site": "00bb9a5c",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9a18",
      "incomplete_value": true,
      "site": "00bb9a18",
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
      "definition_site": "00bb99b4",
      "incomplete_value": true,
      "site": "00bb99c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:990:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9970",
      "incomplete_value": true,
      "site": "00bb9980",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:950:8"
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
      "definition_site": "00bb9a3c",
      "incomplete_value": false,
      "site": "00bb9a40",
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
      "definition_site": "00bb99f8",
      "incomplete_value": false,
      "site": "00bb99fc",
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
      "00bb99ac",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb99b4",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9a3c",
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
      "00bb99ac",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb99b4",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9a3c",
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

- 旧版 [`00bb9980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb98fc.md#insn-00bb9980) · [`00bb99fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb98fc.md#insn-00bb99fc) · [`00bb9a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb98fc.md#insn-00bb9a14)
- 新版 `00bb99c4`（命令位置の公開資料なし） · `00bb9a40`（命令位置の公開資料なし） · `00bb9a58`（命令位置の公開資料なし）

~~~diff
- 00bb9980 ["INT_ADD", "register:40f0:8", ["const:bb9980:8", "const:4:8"]]
- 00bb9980 ["CALL", null, ["callee:00be1d90:8"]]
+ 00bb99c4 ["INT_ADD", "register:40f0:8", ["const:bb99c4:8", "const:4:8"]]
+ 00bb99c4 ["CALL", null, ["callee:00be1d90:8"]]
- 00bb9980 bytes f0a00094
+ 00bb99c4 bytes f3a00094
- 00bb99fc ["INT_ADD", "register:40f0:8", ["const:bb99fc:8", "const:4:8"]]
- 00bb99fc ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb9a40 ["INT_ADD", "register:40f0:8", ["const:bb9a40:8", "const:4:8"]]
+ 00bb9a40 ["CALL", null, ["callee:00bdb000:8"]]
- 00bb99fc bytes 6d850094
+ 00bb9a40 bytes 70850094
- 00bb9a14 ["INT_ADD", "register:40f0:8", ["const:bb9a14:8", "const:4:8"]]
- 00bb9a14 ["CALL", null, ["callee:00be1570:8"]]
+ 00bb9a58 ["INT_ADD", "register:40f0:8", ["const:bb9a58:8", "const:4:8"]]
+ 00bb9a58 ["CALL", null, ["callee:00be1570:8"]]
- 00bb9a14 bytes c39e0094
+ 00bb9a58 bytes c69e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c04331808578bbda8ce1089aed794ee3"></a>

### [`00bb9a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9a44.md) → [`00bb9a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9a88.md) FUN_00bb9a88

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b8ca40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8ca40.md) [`00b8fed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8fed8.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb710.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)
- 新版 呼出元 2件 [`00b8ca84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ca84.md) [`00b8ff1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8ff1c.md) · 呼出先 5件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00bdb760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb760.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "definition_site": "00bb9b74",
      "incomplete_value": false,
      "site": "00bb9b74",
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
      "definition_site": "00bb9b30",
      "incomplete_value": false,
      "site": "00bb9b30",
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
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9b50",
      "incomplete_value": false,
      "site": "00bb9b54",
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
      "definition_site": "00bb9b0c",
      "incomplete_value": false,
      "site": "00bb9b10",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9b60",
      "incomplete_value": false,
      "site": "00bb9b6c",
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
      "definition_site": "00bb9b1c",
      "incomplete_value": false,
      "site": "00bb9b28",
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
      "00bb9acc",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9b50",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9b60",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb9acc",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9b50",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9b60",
      "PARAM",
      [
        "storage",
        "002a570e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9a44.md#insn-00bb9b10) · [`00bb9b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9a44.md#insn-00bb9b28) · [`00bb9b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9a44.md#insn-00bb9b30)
- 新版 `00bb9b54`（命令位置の公開資料なし） · `00bb9b6c`（命令位置の公開資料なし） · `00bb9b74`（命令位置の公開資料なし）

~~~diff
- 00bb9b10 ["INT_ADD", "register:40f0:8", ["const:bb9b10:8", "const:4:8"]]
- 00bb9b10 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb9b54 ["INT_ADD", "register:40f0:8", ["const:bb9b54:8", "const:4:8"]]
+ 00bb9b54 ["CALL", null, ["callee:00bdb000:8"]]
- 00bb9b10 bytes 28850094
+ 00bb9b54 bytes 2b850094
- 00bb9b28 ["INT_ADD", "register:40f0:8", ["const:bb9b28:8", "const:4:8"]]
- 00bb9b28 ["CALL", null, ["callee:00be1570:8"]]
+ 00bb9b6c ["INT_ADD", "register:40f0:8", ["const:bb9b6c:8", "const:4:8"]]
+ 00bb9b6c ["CALL", null, ["callee:00be1570:8"]]
- 00bb9b28 bytes 7e9e0094
+ 00bb9b6c bytes 819e0094
- 00bb9b30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:950:8"]]
- 00bb9b30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb9b74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:990:8"]]
+ 00bb9b74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb9b30 bytes 00a904f9
+ 00bb9b74 bytes 00c904f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ace9d18dd135858e4e11ca6dfcc981c"></a>

### [`00bb9b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9b5c.md) → [`00bb9ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9ba0.md) FUN_00bb9ba0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b8ce58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8ce58.md) [`00b902e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b902e4.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb720.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)
- 新版 呼出元 2件 [`00b8ce9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ce9c.md) [`00b90328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90328.md) · 呼出先 5件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00bdb770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb770.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.19% / 新版 92.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb9c8c",
      "incomplete_value": false,
      "site": "00bb9c8c",
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
      "definition_site": "00bb9c48",
      "incomplete_value": false,
      "site": "00bb9c48",
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
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9c68",
      "incomplete_value": false,
      "site": "00bb9c6c",
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
      "definition_site": "00bb9c24",
      "incomplete_value": false,
      "site": "00bb9c28",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9c94",
      "incomplete_value": false,
      "site": "00bb9c98",
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
      "definition_site": "00bb9c50",
      "incomplete_value": false,
      "site": "00bb9c54",
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
      "00bb9be4",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9c68",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9c78",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb9be4",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9c68",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9c78",
      "PARAM",
      [
        "storage",
        "002a570e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9b5c.md#insn-00bb9c28) · [`00bb9c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9b5c.md#insn-00bb9c48) · [`00bb9c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9b5c.md#insn-00bb9c54)
- 新版 `00bb9c6c`（命令位置の公開資料なし） · `00bb9c8c`（命令位置の公開資料なし） · `00bb9c98`（命令位置の公開資料なし）

~~~diff
- 00bb9c28 ["INT_ADD", "register:40f0:8", ["const:bb9c28:8", "const:4:8"]]
- 00bb9c28 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb9c6c ["INT_ADD", "register:40f0:8", ["const:bb9c6c:8", "const:4:8"]]
+ 00bb9c6c ["CALL", null, ["callee:00bdb000:8"]]
- 00bb9c28 bytes e2840094
+ 00bb9c6c bytes e5840094
- 00bb9c48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:950:8"]]
- 00bb9c48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb9c8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:990:8"]]
+ 00bb9c8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb9c48 bytes 00a904f9
+ 00bb9c8c bytes 00c904f9
- 00bb9c54 ["INT_ADD", "register:40f0:8", ["const:bb9c54:8", "const:4:8"]]
- 00bb9c54 ["CALL", null, ["callee:00bdb020:8"]]
+ 00bb9c98 ["INT_ADD", "register:40f0:8", ["const:bb9c98:8", "const:4:8"]]
+ 00bb9c98 ["CALL", null, ["callee:00bdb020:8"]]
- 00bb9c54 bytes df840094
+ 00bb9c98 bytes e2840094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f27fb25e6099ada3afe281729e77c4f1"></a>

### [`00bb9c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9c74.md) → [`00bb9cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9cb8.md) FUN_00bb9cb8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b8d270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8d270.md) [`00b906f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b906f0.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be1d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d50.md)
- 新版 呼出元 2件 [`00b8d2b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d2b4.md) [`00b90734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90734.md) · 呼出先 5件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md) [`00be1da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1da0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 88.06% / 新版 88.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb9db0",
      "incomplete_value": true,
      "site": "00bb9db0",
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
      "definition_site": "00bb9d6c",
      "incomplete_value": true,
      "site": "00bb9d6c",
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
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9d0c",
      "incomplete_value": true,
      "site": "00bb9d18",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
      "definition_site": "00bb9cc8",
      "incomplete_value": true,
      "site": "00bb9cd4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9d90",
      "incomplete_value": false,
      "site": "00bb9d94",
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
      "definition_site": "00bb9d4c",
      "incomplete_value": false,
      "site": "00bb9d50",
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
      "00bb9d04",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9d0c",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9d90",
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
      "00bb9d04",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9d0c",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9d90",
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

- 旧版 [`00bb9cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9c74.md#insn-00bb9cd4) · [`00bb9d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9c74.md#insn-00bb9d50) · [`00bb9d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9c74.md#insn-00bb9d68)
- 新版 `00bb9d18`（命令位置の公開資料なし） · `00bb9d94`（命令位置の公開資料なし） · `00bb9dac`（命令位置の公開資料なし）

~~~diff
- 00bb9cd4 ["INT_ADD", "register:40f0:8", ["const:bb9cd4:8", "const:4:8"]]
- 00bb9cd4 ["CALL", null, ["callee:00be1da0:8"]]
+ 00bb9d18 ["INT_ADD", "register:40f0:8", ["const:bb9d18:8", "const:4:8"]]
+ 00bb9d18 ["CALL", null, ["callee:00be1da0:8"]]
- 00bb9cd4 bytes 1fa00094
+ 00bb9d18 bytes 22a00094
- 00bb9d50 ["INT_ADD", "register:40f0:8", ["const:bb9d50:8", "const:4:8"]]
- 00bb9d50 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb9d94 ["INT_ADD", "register:40f0:8", ["const:bb9d94:8", "const:4:8"]]
+ 00bb9d94 ["CALL", null, ["callee:00bdb000:8"]]
- 00bb9d50 bytes 98840094
+ 00bb9d94 bytes 9b840094
- 00bb9d68 ["INT_ADD", "register:40f0:8", ["const:bb9d68:8", "const:4:8"]]
- 00bb9d68 ["CALL", null, ["callee:00be1570:8"]]
+ 00bb9dac ["INT_ADD", "register:40f0:8", ["const:bb9dac:8", "const:4:8"]]
+ 00bb9dac ["CALL", null, ["callee:00be1570:8"]]
- 00bb9d68 bytes ee9d0094
+ 00bb9dac bytes f19d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55b7d063e04a3b47340155c2555a5fd2"></a>

### [`00bba1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba1f8.md) → [`00bba23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba23c.md) _ZNSt6__ndk111__call_onceERVmPvPFvS2_E

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md) · 呼出先 4件 [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md) [`00be1170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1170.md) [`00be1180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1180.md)
- 新版 呼出元 1件 [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md) · 呼出先 4件 [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md) [`00be11c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11c0.md) [`00be11d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 85.94% / 新版 85.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bba2e4",
      "incomplete_value": false,
      "site": "00bba2e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba2a0",
      "incomplete_value": false,
      "site": "00bba2a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "definition_site": "00bba2f8",
      "incomplete_value": false,
      "site": "00bba2fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba2b4",
      "incomplete_value": false,
      "site": "00bba2b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "definition_site": "00bba30c",
      "incomplete_value": true,
      "site": "00bba310",
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
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba2c8",
      "incomplete_value": true,
      "site": "00bba2cc",
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
            "const:668:8"
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
      "00bba260",
      "PARAM",
      [
        "storage",
        "010a3668",
        null,
        null
      ]
    ],
    [
      "00bba28c",
      "PARAM",
      [
        "storage",
        "010a3690",
        null,
        null
      ]
    ],
    [
      "00bba290",
      "PARAM",
      [
        "storage",
        "010a3668",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bba260",
      "PARAM",
      [
        "storage",
        "010a36a8",
        null,
        null
      ]
    ],
    [
      "00bba28c",
      "PARAM",
      [
        "storage",
        "010a36d0",
        null,
        null
      ]
    ],
    [
      "00bba290",
      "PARAM",
      [
        "storage",
        "010a36a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba2a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba1f8.md#insn-00bba2a4) · [`00bba2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba1f8.md#insn-00bba2b8) · [`00bba2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba1f8.md#insn-00bba2cc)
- 新版 `00bba2e8`（命令位置の公開資料なし） · `00bba2fc`（命令位置の公開資料なし） · `00bba310`（命令位置の公開資料なし）

~~~diff
- 00bba2a4 ["INT_ADD", "register:40f0:8", ["const:bba2a4:8", "const:4:8"]]
- 00bba2a4 ["CALL", null, ["callee:00bde830:8"]]
+ 00bba2e8 ["INT_ADD", "register:40f0:8", ["const:bba2e8:8", "const:4:8"]]
+ 00bba2e8 ["CALL", null, ["callee:00bde830:8"]]
- 00bba2a4 bytes 4f910094
+ 00bba2e8 bytes 52910094
- 00bba2b8 ["INT_ADD", "register:40f0:8", ["const:bba2b8:8", "const:4:8"]]
- 00bba2b8 ["CALL", null, ["callee:00bde820:8"]]
+ 00bba2fc ["INT_ADD", "register:40f0:8", ["const:bba2fc:8", "const:4:8"]]
+ 00bba2fc ["CALL", null, ["callee:00bde820:8"]]
- 00bba2b8 bytes 46910094
+ 00bba2fc bytes 49910094
- 00bba2cc ["INT_ADD", "register:40f0:8", ["const:bba2cc:8", "const:4:8"]]
- 00bba2cc ["CALL", null, ["callee:00bde830:8"]]
+ 00bba310 ["INT_ADD", "register:40f0:8", ["const:bba310:8", "const:4:8"]]
+ 00bba310 ["CALL", null, ["callee:00bde830:8"]]
- 00bba2cc bytes 45910094
+ 00bba310 bytes 48910094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f2e95ed582973c3f015b74992307551"></a>

### [`00bba30c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba30c.md) → [`00bba350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba350.md) FUN_00bba350

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md) [`00be1170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1170.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md) [`00be11c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bba370",
      "incomplete_value": false,
      "site": "00bba374",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba32c",
      "incomplete_value": false,
      "site": "00bba330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "definition_site": "00bba384",
      "incomplete_value": true,
      "site": "00bba388",
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
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba340",
      "incomplete_value": true,
      "site": "00bba344",
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
            "const:668:8"
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
      "definition_site": "00bba390",
      "incomplete_value": false,
      "site": "00bba394",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba34c",
      "incomplete_value": false,
      "site": "00bba350",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:690:8"
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
      "00bba370",
      "PARAM",
      [
        "storage",
        "010a3668",
        null,
        null
      ]
    ],
    [
      "00bba384",
      "PARAM",
      [
        "storage",
        "010a3668",
        null,
        null
      ]
    ],
    [
      "00bba390",
      "PARAM",
      [
        "storage",
        "010a3690",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bba370",
      "PARAM",
      [
        "storage",
        "010a36a8",
        null,
        null
      ]
    ],
    [
      "00bba384",
      "PARAM",
      [
        "storage",
        "010a36a8",
        null,
        null
      ]
    ],
    [
      "00bba390",
      "PARAM",
      [
        "storage",
        "010a36d0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba30c.md#insn-00bba330) · [`00bba344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba30c.md#insn-00bba344) · [`00bba350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba30c.md#insn-00bba350)
- 新版 `00bba374`（命令位置の公開資料なし） · `00bba388`（命令位置の公開資料なし） · `00bba394`（命令位置の公開資料なし）

~~~diff
- 00bba330 ["INT_ADD", "register:40f0:8", ["const:bba330:8", "const:4:8"]]
- 00bba330 ["CALL", null, ["callee:00bde820:8"]]
+ 00bba374 ["INT_ADD", "register:40f0:8", ["const:bba374:8", "const:4:8"]]
+ 00bba374 ["CALL", null, ["callee:00bde820:8"]]
- 00bba330 bytes 28910094
+ 00bba374 bytes 2b910094
- 00bba344 ["INT_ADD", "register:40f0:8", ["const:bba344:8", "const:4:8"]]
- 00bba344 ["CALL", null, ["callee:00bde830:8"]]
+ 00bba388 ["INT_ADD", "register:40f0:8", ["const:bba388:8", "const:4:8"]]
+ 00bba388 ["CALL", null, ["callee:00bde830:8"]]
- 00bba344 bytes 27910094
+ 00bba388 bytes 2a910094
- 00bba350 ["INT_ADD", "register:40f0:8", ["const:bba350:8", "const:4:8"]]
- 00bba350 ["CALL", null, ["callee:00be11c0:8"]]
+ 00bba394 ["INT_ADD", "register:40f0:8", ["const:bba394:8", "const:4:8"]]
+ 00bba394 ["CALL", null, ["callee:00be11c0:8"]]
- 00bba350 bytes 889b0094
+ 00bba394 bytes 8b9b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b300ab801328630b316482174d4f9221"></a>

### [`00bba408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba408.md) → [`00bba44c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba44c.md) _ZNSt6__ndk120__get_collation_nameEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdd960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd960.md) · 呼出先 1件 [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)
- 新版 呼出元 1件 [`00bdd9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9b0.md) · 呼出先 1件 [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)

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
      "definition_site": "00bba4b0",
      "incomplete_value": true,
      "site": "00bba4b8",
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
      "definition_site": "00bba46c",
      "incomplete_value": true,
      "site": "00bba474",
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
      "00bba484",
      "READ",
      [
        "storage",
        "00c16350",
        null,
        "pointer"
      ]
    ],
    [
      "00bba484",
      "PARAM",
      [
        "storage",
        "002a6442",
        null,
        "string"
      ]
    ],
    [
      "00bba484",
      "READ",
      [
        "storage",
        "00c16190",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bba484",
      "READ",
      [
        "storage",
        "00c163a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bba484",
      "PARAM",
      [
        "storage",
        "002a64dc",
        null,
        "string"
      ]
    ],
    [
      "00bba484",
      "READ",
      [
        "storage",
        "00c161e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba408.md#insn-00bba430) · [`00bba444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba408.md#insn-00bba444) · [`00bba464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba408.md#insn-00bba464)
- 新版 `00bba474`（命令位置の公開資料なし） · `00bba488`（命令位置の公開資料なし） · `00bba4a8`（命令位置の公開資料なし）

~~~diff
- 00bba430 ["COPY", "register:40a8:8", ["const:c15fe0:8"]]
+ 00bba474 ["COPY", "register:40a8:8", ["const:c16030:8"]]
- 00bba430 bytes 95dd2d10
+ 00bba474 bytes f5dd2d10
- 00bba444 ["INT_ADD", "register:40f0:8", ["const:bba444:8", "const:4:8"]]
- 00bba444 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00bba488 ["INT_ADD", "register:40f0:8", ["const:bba488:8", "const:4:8"]]
+ 00bba488 ["CALL", null, ["callee:00bde9d0:8"]]
- 00bba444 bytes 4f910094
+ 00bba488 bytes 52910094
- 00bba464 ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 00bba464 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bba464 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bba464 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bba4a8 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 00bba4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bba4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bba4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bba464 bytes 08411b91
+ 00bba4a8 bytes 08811c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75d6fecec0e55d9d4639db93f316b4a3"></a>

### [`00bba64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba64c.md) → [`00bba690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba690.md) __cxa_bad_typeid

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bbb114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb114.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00be1d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d60.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bbb158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb158.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00be1db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1db0.md)

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
      "definition_site": "00bba6c0",
      "incomplete_value": true,
      "site": "00bba6c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
              ],
              [
                "leaf",
                "const:ff0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba67c",
      "incomplete_value": true,
      "site": "00bba680",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
              ],
              [
                "leaf",
                "const:fa0:8"
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
      "00bba6bc",
      "READ",
      [
        "storage",
        "00c1bf98",
        null,
        "pointer"
      ]
    ],
    [
      "00bba6bc",
      "PARAM",
      [
        "storage",
        "00c16ba8",
        "_ZTISt10bad_typeid",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bba6c0",
      "READ",
      [
        "storage",
        "00c1bfa0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bba6bc",
      "READ",
      [
        "storage",
        "00c1bfe8",
        null,
        "pointer"
      ]
    ],
    [
      "00bba6bc",
      "PARAM",
      [
        "storage",
        "00c16bf8",
        "_ZTISt10bad_typeid",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bba6c0",
      "READ",
      [
        "storage",
        "00c1bff0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba64c.md#insn-00bba680) · [`00bba660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba64c.md#insn-00bba660) · [`00bba668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba64c.md#insn-00bba668)
- 新版 `00bba6c4`（命令位置の公開資料なし） · `00bba6a4`（命令位置の公開資料なし） · `00bba6ac`（命令位置の公開資料なし）

~~~diff
- 00bba680 ["INT_ADD", "register:40f0:8", ["const:bba680:8", "const:4:8"]]
- 00bba680 ["CALL", null, ["callee:00bdb0c0:8"]]
+ 00bba6c4 ["INT_ADD", "register:40f0:8", ["const:bba6c4:8", "const:4:8"]]
+ 00bba6c4 ["CALL", null, ["callee:00bdb0c0:8"]]
- 00bba680 bytes 7c820094
+ 00bba6c4 bytes 7f820094
- 00bba660 ["INT_ADD", "register:40f0:8", ["const:bba660:8", "const:4:8"]]
- 00bba660 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00bba6a4 ["INT_ADD", "register:40f0:8", ["const:bba6a4:8", "const:4:8"]]
+ 00bba6a4 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00bba660 bytes 7c820094
+ 00bba6a4 bytes 7f820094
- 00bba668 ["INT_ADD", "register:40f0:8", ["const:bba668:8", "const:4:8"]]
- 00bba668 ["CALL", null, ["callee:00be1db0:8"]]
+ 00bba6ac ["INT_ADD", "register:40f0:8", ["const:bba6ac:8", "const:4:8"]]
+ 00bba6ac ["CALL", null, ["callee:00be1db0:8"]]
- 00bba668 bytes be9d0094
+ 00bba6ac bytes c19d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f146c4c9eb5e05fa90e8aae7e2eeec5"></a>

### [`00bba684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba684.md) → [`00bba6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba6c8.md) __cxa_throw_bad_array_new_length

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb190.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1e0.md)

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
      "definition_site": "00bba6f4",
      "incomplete_value": true,
      "site": "00bba6fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:de0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba6b0",
      "incomplete_value": true,
      "site": "00bba6b8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d90:8"
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
      "definition_site": "00bba6f8",
      "incomplete_value": true,
      "site": "00bba6fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
              ],
              [
                "leaf",
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba6b4",
      "incomplete_value": true,
      "site": "00bba6b8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
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
      "00bba6f4",
      "READ",
      [
        "storage",
        "00c1ad90",
        null,
        "pointer"
      ]
    ],
    [
      "00bba6f4",
      "PARAM",
      [
        "storage",
        "00c168b8",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bba6f8",
      "READ",
      [
        "storage",
        "00c1ad98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bba6f4",
      "READ",
      [
        "storage",
        "00c1ade0",
        null,
        "pointer"
      ]
    ],
    [
      "00bba6f4",
      "PARAM",
      [
        "storage",
        "00c16908",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bba6f8",
      "READ",
      [
        "storage",
        "00c1ade8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba6b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba684.md#insn-00bba6b8) · [`00bba698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba684.md#insn-00bba698) · [`00bba6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba684.md#insn-00bba6a0)
- 新版 `00bba6fc`（命令位置の公開資料なし） · `00bba6dc`（命令位置の公開資料なし） · `00bba6e4`（命令位置の公開資料なし）

~~~diff
- 00bba6b8 ["INT_ADD", "register:40f0:8", ["const:bba6b8:8", "const:4:8"]]
- 00bba6b8 ["CALL", null, ["callee:00bdb0c0:8"]]
+ 00bba6fc ["INT_ADD", "register:40f0:8", ["const:bba6fc:8", "const:4:8"]]
+ 00bba6fc ["CALL", null, ["callee:00bdb0c0:8"]]
- 00bba6b8 bytes 6e820094
+ 00bba6fc bytes 71820094
- 00bba698 ["INT_ADD", "register:40f0:8", ["const:bba698:8", "const:4:8"]]
- 00bba698 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00bba6dc ["INT_ADD", "register:40f0:8", ["const:bba6dc:8", "const:4:8"]]
+ 00bba6dc ["CALL", null, ["callee:00bdb0a0:8"]]
- 00bba698 bytes 6e820094
+ 00bba6dc bytes 71820094
- 00bba6a0 ["INT_ADD", "register:40f0:8", ["const:bba6a0:8", "const:4:8"]]
- 00bba6a0 ["CALL", null, ["callee:00bdb1e0:8"]]
+ 00bba6e4 ["INT_ADD", "register:40f0:8", ["const:bba6e4:8", "const:4:8"]]
+ 00bba6e4 ["CALL", null, ["callee:00bdb1e0:8"]]
- 00bba6a0 bytes bc820094
+ 00bba6e4 bytes bf820094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07a55b8acbe31945fe294a8848478cf8"></a>

### [`00bba6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba6bc.md) → [`00bba700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba700.md) __cxa_guard_acquire

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) · 呼出先 5件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md) [`00be1180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1180.md) [`00be1da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1da0.md)
- 新版 呼出元 1件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) · 呼出先 5件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md) [`00be11d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11d0.md) [`00be1df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1df0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 87.84% / 新版 87.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bba73c",
      "incomplete_value": false,
      "site": "00bba744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba6f8",
      "incomplete_value": false,
      "site": "00bba700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      "definition_site": "00bba7c4",
      "incomplete_value": false,
      "site": "00bba7c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba780",
      "incomplete_value": false,
      "site": "00bba784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bba7f8",
      "incomplete_value": false,
      "site": "00bba804",
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
            "const:783:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba7b4",
      "incomplete_value": false,
      "site": "00bba7c0",
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
            "const:810:8"
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
      "00bba73c",
      "PARAM",
      [
        "storage",
        "010a36c0",
        null,
        null
      ]
    ],
    [
      "00bba740",
      "DATA",
      [
        "storage",
        "002a722d",
        null,
        "string"
      ]
    ],
    [
      "00bba78c",
      "PARAM",
      [
        "storage",
        "010a36e8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bba73c",
      "PARAM",
      [
        "storage",
        "010a3700",
        null,
        null
      ]
    ],
    [
      "00bba740",
      "DATA",
      [
        "storage",
        "002a72c7",
        null,
        "string"
      ]
    ],
    [
      "00bba78c",
      "PARAM",
      [
        "storage",
        "010a3728",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba6bc.md#insn-00bba700) · [`00bba784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba6bc.md#insn-00bba784) · [`00bba7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba6bc.md#insn-00bba7c0)
- 新版 `00bba744`（命令位置の公開資料なし） · `00bba7c8`（命令位置の公開資料なし） · `00bba804`（命令位置の公開資料なし）

~~~diff
- 00bba700 ["INT_ADD", "register:40f0:8", ["const:bba700:8", "const:4:8"]]
- 00bba700 ["CALL", null, ["callee:00bde820:8"]]
+ 00bba744 ["INT_ADD", "register:40f0:8", ["const:bba744:8", "const:4:8"]]
+ 00bba744 ["CALL", null, ["callee:00bde820:8"]]
- 00bba700 bytes 34900094
+ 00bba744 bytes 37900094
- 00bba784 ["INT_ADD", "register:40f0:8", ["const:bba784:8", "const:4:8"]]
- 00bba784 ["CALL", null, ["callee:00bde830:8"]]
+ 00bba7c8 ["INT_ADD", "register:40f0:8", ["const:bba7c8:8", "const:4:8"]]
+ 00bba7c8 ["CALL", null, ["callee:00bde830:8"]]
- 00bba784 bytes 17900094
+ 00bba7c8 bytes 1a900094
- 00bba7c0 ["INT_ADD", "register:40f0:8", ["const:bba7c0:8", "const:4:8"]]
- 00bba7c0 ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bba804 ["INT_ADD", "register:40f0:8", ["const:bba804:8", "const:4:8"]]
+ 00bba804 ["CALL", null, ["callee:00bbb19c:8"]]
- 00bba7c0 bytes 66020094
+ 00bba804 bytes 66020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-767ff45fb6d11f9445b8d39a6ac4fd91"></a>

### [`00bba800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba800.md) → [`00bba844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba844.md) __cxa_guard_release

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) · 呼出先 4件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md) [`00be1170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1170.md)
- 新版 呼出元 1件 [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) · 呼出先 4件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md) [`00be11c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.37% / 新版 85.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bba880",
      "incomplete_value": false,
      "site": "00bba884",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba83c",
      "incomplete_value": false,
      "site": "00bba840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      "definition_site": "00bba8cc",
      "incomplete_value": false,
      "site": "00bba8d0",
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
            "const:9e9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba888",
      "incomplete_value": false,
      "site": "00bba88c",
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
            "const:a76:8"
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
      "definition_site": "00bba8e0",
      "incomplete_value": false,
      "site": "00bba8e4",
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
            "const:9e9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba89c",
      "incomplete_value": false,
      "site": "00bba8a0",
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
            "const:a76:8"
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
      "00bba868",
      "PARAM",
      [
        "storage",
        "010a36c0",
        null,
        null
      ]
    ],
    [
      "00bba880",
      "PARAM",
      [
        "storage",
        "010a36c0",
        null,
        null
      ]
    ],
    [
      "00bba894",
      "PARAM",
      [
        "storage",
        "010a36e8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bba868",
      "PARAM",
      [
        "storage",
        "010a3700",
        null,
        null
      ]
    ],
    [
      "00bba880",
      "PARAM",
      [
        "storage",
        "010a3700",
        null,
        null
      ]
    ],
    [
      "00bba894",
      "PARAM",
      [
        "storage",
        "010a3728",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba800.md#insn-00bba840) · [`00bba88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba800.md#insn-00bba88c) · [`00bba8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba800.md#insn-00bba8a0)
- 新版 `00bba884`（命令位置の公開資料なし） · `00bba8d0`（命令位置の公開資料なし） · `00bba8e4`（命令位置の公開資料なし）

~~~diff
- 00bba840 ["INT_ADD", "register:40f0:8", ["const:bba840:8", "const:4:8"]]
- 00bba840 ["CALL", null, ["callee:00bde830:8"]]
+ 00bba884 ["INT_ADD", "register:40f0:8", ["const:bba884:8", "const:4:8"]]
+ 00bba884 ["CALL", null, ["callee:00bde830:8"]]
- 00bba840 bytes e88f0094
+ 00bba884 bytes eb8f0094
- 00bba88c ["INT_ADD", "register:40f0:8", ["const:bba88c:8", "const:4:8"]]
- 00bba88c ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bba8d0 ["INT_ADD", "register:40f0:8", ["const:bba8d0:8", "const:4:8"]]
+ 00bba8d0 ["CALL", null, ["callee:00bbb19c:8"]]
- 00bba88c bytes 33020094
+ 00bba8d0 bytes 33020094
- 00bba8a0 ["INT_ADD", "register:40f0:8", ["const:bba8a0:8", "const:4:8"]]
- 00bba8a0 ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bba8e4 ["INT_ADD", "register:40f0:8", ["const:bba8e4:8", "const:4:8"]]
+ 00bba8e4 ["CALL", null, ["callee:00bbb19c:8"]]
- 00bba8a0 bytes 2e020094
+ 00bba8e4 bytes 2e020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c68c0bdfaca03d78c29ea18673b32e6"></a>

### [`00bba8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba8a8.md) → [`00bba8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba8ec.md) __cxa_guard_abort

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb0f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0f0.md) · 呼出先 4件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md) [`00be1170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1170.md)
- 新版 呼出元 1件 [`00bdb140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb140.md) · 呼出先 4件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md) [`00be11c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bba904",
      "incomplete_value": false,
      "site": "00bba908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba8c0",
      "incomplete_value": false,
      "site": "00bba8c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      "definition_site": "00bba920",
      "incomplete_value": true,
      "site": "00bba924",
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
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba8dc",
      "incomplete_value": true,
      "site": "00bba8e0",
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
            "const:6c0:8"
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
      "definition_site": "00bba968",
      "incomplete_value": false,
      "site": "00bba96c",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba924",
      "incomplete_value": false,
      "site": "00bba928",
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
            "const:29d:8"
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
      "00bba904",
      "PARAM",
      [
        "storage",
        "010a36c0",
        null,
        null
      ]
    ],
    [
      "00bba920",
      "PARAM",
      [
        "storage",
        "010a36c0",
        null,
        null
      ]
    ],
    [
      "00bba934",
      "PARAM",
      [
        "storage",
        "010a36e8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bba904",
      "PARAM",
      [
        "storage",
        "010a3700",
        null,
        null
      ]
    ],
    [
      "00bba920",
      "PARAM",
      [
        "storage",
        "010a3700",
        null,
        null
      ]
    ],
    [
      "00bba934",
      "PARAM",
      [
        "storage",
        "010a3728",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba8a8.md#insn-00bba8c4) · [`00bba8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba8a8.md#insn-00bba8e0) · [`00bba924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba8a8.md#insn-00bba924)
- 新版 `00bba908`（命令位置の公開資料なし） · `00bba924`（命令位置の公開資料なし） · `00bba968`（命令位置の公開資料なし）

~~~diff
- 00bba8c4 ["INT_ADD", "register:40f0:8", ["const:bba8c4:8", "const:4:8"]]
- 00bba8c4 ["CALL", null, ["callee:00bde820:8"]]
+ 00bba908 ["INT_ADD", "register:40f0:8", ["const:bba908:8", "const:4:8"]]
+ 00bba908 ["CALL", null, ["callee:00bde820:8"]]
- 00bba8c4 bytes c38f0094
+ 00bba908 bytes c68f0094
- 00bba8e0 ["INT_ADD", "register:40f0:8", ["const:bba8e0:8", "const:4:8"]]
- 00bba8e0 ["CALL", null, ["callee:00bde830:8"]]
+ 00bba924 ["INT_ADD", "register:40f0:8", ["const:bba924:8", "const:4:8"]]
+ 00bba924 ["CALL", null, ["callee:00bde830:8"]]
- 00bba8e0 bytes c08f0094
+ 00bba924 bytes c38f0094
- 00bba924 ["COPY", "tmp:0:8", ["const:29d:8"]]
- 00bba924 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bba924 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bba924 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bba968 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 00bba968 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bba968 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bba968 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bba924 bytes 21740a91
+ 00bba968 bytes 21a00c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de70167ff522a964a05bbe6f4ff12c39"></a>

### [`00bba944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba944.md) → [`00bba988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba988.md) FUN_00bba988

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)

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
      "definition_site": "00bba9a0",
      "incomplete_value": false,
      "site": "00bba9a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba95c",
      "incomplete_value": false,
      "site": "00bba960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      "00bba9a0",
      "PARAM",
      [
        "storage",
        "010a36c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bba9a0",
      "PARAM",
      [
        "storage",
        "010a3700",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba944.md#insn-00bba960) · [`00bba95c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba944.md#insn-00bba95c) · [`00bba984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba944.md#insn-00bba984)
- 新版 `00bba9a4`（命令位置の公開資料なし） · `00bba9a0`（命令位置の公開資料なし） · `00bba9c8`（命令位置の公開資料なし）

~~~diff
- 00bba960 ["INT_ADD", "register:40f0:8", ["const:bba960:8", "const:4:8"]]
- 00bba960 ["CALL", null, ["callee:00bde830:8"]]
+ 00bba9a4 ["INT_ADD", "register:40f0:8", ["const:bba9a4:8", "const:4:8"]]
+ 00bba9a4 ["CALL", null, ["callee:00bde830:8"]]
- 00bba960 bytes a08f0094
+ 00bba9a4 bytes a38f0094
- 00bba95c ["COPY", "tmp:0:8", ["const:6c0:8"]]
- 00bba95c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bba95c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bba95c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bba9a0 ["COPY", "tmp:0:8", ["const:700:8"]]
+ 00bba9a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bba9a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bba9a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bba95c bytes 00001b91
+ 00bba9a0 bytes 00001c91
- 00bba984 ["INT_ADD", "register:40f0:8", ["const:bba984:8", "const:4:8"]]
- 00bba984 ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bba9c8 ["INT_ADD", "register:40f0:8", ["const:bba9c8:8", "const:4:8"]]
+ 00bba9c8 ["CALL", null, ["callee:00bbb19c:8"]]
- 00bba984 bytes f5010094
+ 00bba9c8 bytes f5010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c2543d58d446a71e78ed38b6d9e4e92"></a>

### [`00bba9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9e0.md) → [`00bbaa24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa24.md) FUN_00bbaa24

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bba9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9fc.md) [`00bd6030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6030.md) · 呼出先 1件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md)
- 新版 呼出元 2件 [`00bbaa40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa40.md) [`00bd6074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6074.md) · 呼出先 1件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md)

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
      "definition_site": "00bbaa38",
      "incomplete_value": false,
      "site": "00bbaa3c",
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
            "const:613:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba9f4",
      "incomplete_value": false,
      "site": "00bba9f8",
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
            "const:6a0:8"
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
      "00bbaa38",
      "PARAM",
      [
        "storage",
        "002936a0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbaa38",
      "PARAM",
      [
        "storage",
        "00293613",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9e0.md#insn-00bba9f8) · [`00bba9ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9e0.md#insn-00bba9ec) · [`00bba9f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9e0.md#insn-00bba9f4)
- 新版 `00bbaa3c`（命令位置の公開資料なし） · `00bbaa30`（命令位置の公開資料なし） · `00bbaa38`（命令位置の公開資料なし）

~~~diff
- 00bba9f8 ["INT_ADD", "register:40f0:8", ["const:bba9f8:8", "const:4:8"]]
- 00bba9f8 ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bbaa3c ["INT_ADD", "register:40f0:8", ["const:bbaa3c:8", "const:4:8"]]
+ 00bbaa3c ["CALL", null, ["callee:00bbb19c:8"]]
- 00bba9f8 bytes d8010094
+ 00bbaa3c bytes d8010094
- 00bba9ec ["COPY", "register:0:8", ["register:4000:8"]]
- 00bba9ec ["INT_ADD", "register:40f0:8", ["const:bba9ec:8", "const:4:8"]]
- 00bba9ec ["CALLIND", null, ["register:0:8"]]
+ 00bbaa30 ["COPY", "register:0:8", ["register:4000:8"]]
+ 00bbaa30 ["INT_ADD", "register:40f0:8", ["const:bbaa30:8", "const:4:8"]]
+ 00bbaa30 ["CALLIND", null, ["register:0:8"]]
- 00bba9ec bytes 00003fd6
+ 00bbaa30 bytes 00003fd6
- 00bba9f4 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 00bba9f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bba9f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bba9f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bbaa38 ["COPY", "tmp:0:8", ["const:613:8"]]
+ 00bbaa38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bbaa38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bbaa38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bba9f4 bytes 00801a91
+ 00bbaa38 bytes 004c1891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6a1926a606d1b1bc0ba4d67aca0f4db"></a>

### [`00bbaa18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa18.md) → [`00bbaa5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa5c.md) _ZSt13get_terminatev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1dc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1dc0.md) · 呼出先 1件 [`00bbaa70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa70.md)
- 新版 呼出元 1件 [`00be1e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e10.md) · 呼出先 1件 [`00bbaab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaab4.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bbaa68",
      "incomplete_value": true,
      "site": "00bbaa6c",
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
              [
                "leaf",
                "const:c1c000:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbaa24",
      "incomplete_value": true,
      "site": "00bbaa28",
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
      "00bbaa64",
      "READ",
      [
        "storage",
        "00c1bfb0",
        null,
        "pointer"
      ]
    ],
    [
      "00bbaa68",
      "READ",
      [
        "storage",
        "00c24940",
        "__cxa_terminate_handler",
        "pointer"
      ]
    ],
    [
      "00bbaa68",
      "DATA",
      [
        "storage",
        "00bbaa70",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bbaa64",
      "READ",
      [
        "storage",
        "00c1c000",
        null,
        "pointer"
      ]
    ],
    [
      "00bbaa68",
      "READ",
      [
        "storage",
        "00c24990",
        "__cxa_terminate_handler",
        "pointer"
      ]
    ],
    [
      "00bbaa68",
      "DATA",
      [
        "storage",
        "00bbaab4",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbaa1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa18.md#insn-00bbaa1c) · [`00bbaa20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa18.md#insn-00bbaa20)
- 新版 `00bbaa60`（命令位置の公開資料なし） · `00bbaa64`（命令位置の公開資料なし）

~~~diff
- 00bbaa1c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00bbaa60 ["COPY", "register:4040:8", ["const:c1c000:8"]]
- 00bbaa1c bytes 080300b0
+ 00bbaa60 bytes 080300d0
- 00bbaa20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fb0:8"]]
- 00bbaa20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbaa64 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00bbaa64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbaa20 bytes 08d947f9
+ 00bbaa64 bytes 080140f9
~~~


<a id="compare-38b251ab7d4beb1477769a4e6776acbb"></a>

### [`00bbaa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md) → [`00bbaa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md) FUN_00bbaa70

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`00bba9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9a0.md) [`00bd5144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5144.md) [`00bd524c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd524c.md) [`00bd5414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5414.md) [`00bd56c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd56c4.md) · 呼出先 1件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md)
- 新版 呼出元 8件 [`00bba9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba9e4.md) [`00bd5188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5188.md) [`00bd5290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5290.md) [`00bd5458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5458.md) [`00bd5708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5708.md) · 呼出先 1件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md)

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
      "definition_site": "00bbaa84",
      "incomplete_value": false,
      "site": "00bbaa88",
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
            "const:ac4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbaa40",
      "incomplete_value": false,
      "site": "00bbaa44",
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
            "const:b51:8"
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
      "00bbaa84",
      "PARAM",
      [
        "storage",
        "00298b51",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbaa84",
      "PARAM",
      [
        "storage",
        "00298ac4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbaa44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md#insn-00bbaa44) · [`00bbaa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md#insn-00bbaa38) · [`00bbaa40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md#insn-00bbaa40)
- 新版 `00bbaa88`（命令位置の公開資料なし） · `00bbaa7c`（命令位置の公開資料なし） · `00bbaa84`（命令位置の公開資料なし）

~~~diff
- 00bbaa44 ["INT_ADD", "register:40f0:8", ["const:bbaa44:8", "const:4:8"]]
- 00bbaa44 ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bbaa88 ["INT_ADD", "register:40f0:8", ["const:bbaa88:8", "const:4:8"]]
+ 00bbaa88 ["CALL", null, ["callee:00bbb19c:8"]]
- 00bbaa44 bytes c5010094
+ 00bbaa88 bytes c5010094
- 00bbaa38 ["COPY", "register:0:8", ["register:4000:8"]]
- 00bbaa38 ["INT_ADD", "register:40f0:8", ["const:bbaa38:8", "const:4:8"]]
- 00bbaa38 ["CALLIND", null, ["register:0:8"]]
+ 00bbaa7c ["COPY", "register:0:8", ["register:4000:8"]]
+ 00bbaa7c ["INT_ADD", "register:40f0:8", ["const:bbaa7c:8", "const:4:8"]]
+ 00bbaa7c ["CALLIND", null, ["register:0:8"]]
- 00bbaa38 bytes 00003fd6
+ 00bbaa7c bytes 00003fd6
- 00bbaa40 ["COPY", "tmp:0:8", ["const:b51:8"]]
- 00bbaa40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bbaa40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bbaa40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bbaa84 ["COPY", "tmp:0:8", ["const:ac4:8"]]
+ 00bbaa84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bbaa84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bbaa84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bbaa40 bytes 00442d91
+ 00bbaa84 bytes 00102b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe515bab60102bd67df3aacb51e14157"></a>

### [`00bbaa70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa70.md) → [`00bbaab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaab4.md) FUN_00bbaab4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00bba9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9a0.md) [`00bbaa18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa18.md) [`00bbac10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbac10.md) · 呼出先 6件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bbb47c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb47c.md) [`00bd4f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4f94.md) [`00bd4fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4fa0.md) [`00be1d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d90.md)
- 新版 呼出元 3件 [`00bba9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba9e4.md) [`00bbaa5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa5c.md) [`00bbac54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac54.md) · 呼出先 6件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bbb4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb4c0.md) [`00bd4fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4fd8.md) [`00bd4fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4fe4.md) [`00be1de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1de0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.78% / 新版 91.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbab24",
      "incomplete_value": true,
      "site": "00bbab28",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:9a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbaae0",
      "incomplete_value": true,
      "site": "00bbaae4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:950:8"
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
      "00bbab20",
      "PARAM",
      [
        "storage",
        "002a024b",
        null,
        "string"
      ]
    ],
    [
      "00bbab24",
      "READ",
      [
        "storage",
        "00c24950",
        null,
        "pointer"
      ]
    ],
    [
      "00bbab24",
      "PARAM",
      [
        "storage",
        "00299a8a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbab20",
      "PARAM",
      [
        "storage",
        "002a02d6",
        null,
        "string"
      ]
    ],
    [
      "00bbab24",
      "READ",
      [
        "storage",
        "00c249a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bbab24",
      "PARAM",
      [
        "storage",
        "002999fd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbaae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa70.md#insn-00bbaae4) · [`00bbaa84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa70.md#insn-00bbaa84) · [`00bbaa9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa70.md#insn-00bbaa9c)
- 新版 `00bbab28`（命令位置の公開資料なし） · `00bbaac8`（命令位置の公開資料なし） · `00bbaae0`（命令位置の公開資料なし）

~~~diff
- 00bbaae4 ["INT_ADD", "register:40f0:8", ["const:bbaae4:8", "const:4:8"]]
- 00bbaae4 ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bbab28 ["INT_ADD", "register:40f0:8", ["const:bbab28:8", "const:4:8"]]
+ 00bbab28 ["CALL", null, ["callee:00bbb19c:8"]]
- 00bbaae4 bytes 9d010094
+ 00bbab28 bytes 9d010094
- 00bbaa84 ["INT_ADD", "register:40f0:8", ["const:bbaa84:8", "const:4:8"]]
- 00bbaa84 ["CALL", null, ["callee:00be1de0:8"]]
+ 00bbaac8 ["INT_ADD", "register:40f0:8", ["const:bbaac8:8", "const:4:8"]]
+ 00bbaac8 ["CALL", null, ["callee:00be1de0:8"]]
- 00bbaa84 bytes c39c0094
+ 00bbaac8 bytes c69c0094
- 00bbaa9c ["INT_ADD", "register:40f0:8", ["const:bbaa9c:8", "const:4:8"]]
- 00bbaa9c ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bbaae0 ["INT_ADD", "register:40f0:8", ["const:bbaae0:8", "const:4:8"]]
+ 00bbaae0 ["CALL", null, ["callee:00bbb19c:8"]]
- 00bbaa9c bytes af010094
+ 00bbaae0 bytes af010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e08bbd64bd56e2e3817e6ce525693676"></a>

### [`00bbabbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbabbc.md) → [`00bbac00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac00.md) FUN_00bbac00

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00bba98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba98c.md) [`00bba9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9fc.md) [`00bbabdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbabdc.md) · 呼出先 1件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md)
- 新版 呼出元 3件 [`00bba9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba9d0.md) [`00bbaa40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa40.md) [`00bbac20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac20.md) · 呼出先 1件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbac18",
      "incomplete_value": true,
      "site": "00bbac18",
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
            "const:9a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbabd4",
      "incomplete_value": true,
      "site": "00bbabd4",
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
            "const:950:8"
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
      "00bbac18",
      "WRITE",
      [
        "storage",
        "00c24950",
        null,
        "pointer"
      ]
    ],
    [
      "00bbac18",
      "DATA",
      [
        "storage",
        "002a11af",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbac18",
      "WRITE",
      [
        "storage",
        "00c249a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bbac18",
      "DATA",
      [
        "storage",
        "002a123a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbabd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbabbc.md#insn-00bbabd4) · [`00bbabd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbabbc.md#insn-00bbabd0) · [`00bbabd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbabbc.md#insn-00bbabd8)
- 新版 `00bbac18`（命令位置の公開資料なし） · `00bbac14`（命令位置の公開資料なし） · `00bbac1c`（命令位置の公開資料なし）

~~~diff
- 00bbabd4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:950:8"]]
- 00bbabd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00bbac18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a0:8"]]
+ 00bbac18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bbabd4 bytes 09a904f9
+ 00bbac18 bytes 09d104f9
- 00bbabd0 ["COPY", "tmp:0:8", ["const:1af:8"]]
- 00bbabd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bbabd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bbabd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bbac14 ["COPY", "tmp:0:8", ["const:23a:8"]]
+ 00bbac14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bbac14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bbac14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bbabd0 bytes 29bd0691
+ 00bbac14 bytes 29e90891
- 00bbabd8 ["INT_ADD", "register:40f0:8", ["const:bbabd8:8", "const:4:8"]]
- 00bbabd8 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bbac1c ["INT_ADD", "register:40f0:8", ["const:bbac1c:8", "const:4:8"]]
+ 00bbac1c ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bbabd8 bytes 6a810094
+ 00bbac1c bytes 6d810094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d802bfb403122a36c84e212e615ae07"></a>

### [`00bbaea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaea8.md) → [`00bbaeec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaeec.md) _ZNSt14overflow_errorD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`006ad854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad854.md) [`00b732d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b732d4.md) [`00b73a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73a3c.md) [`00bdda20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda20.md) [`00be0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f20.md) · 呼出先 3件 [`00bd6df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6df0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 8件 [`006ad854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad854.md) [`00b73318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73318.md) [`00b73a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73a80.md) [`00bdda70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda70.md) [`00be0f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f70.md) · 呼出先 3件 [`00bd6e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e30.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "00bbaf0c",
      "incomplete_value": true,
      "site": "00bbaf14",
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
      "definition_site": "00bbaec8",
      "incomplete_value": true,
      "site": "00bbaed0",
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
      "00bbaf04",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "00bbaf14",
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
      "00bbaf04",
      "READ",
      [
        "storage",
        "00c1bc68",
        null,
        "pointer"
      ]
    ],
    [
      "00bbaf14",
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

- 旧版 [`00bbaec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaea8.md#insn-00bbaec0) · [`00bbaed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaea8.md#insn-00bbaed8) · [`00bbaee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaea8.md#insn-00bbaee8)
- 新版 `00bbaf04`（命令位置の公開資料なし） · `00bbaf1c`（命令位置の公開資料なし） · `00bbaf2c`（命令位置の公開資料なし）

~~~diff
- 00bbaec0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c18:8"]]
- 00bbaec0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbaf04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c68:8"]]
+ 00bbaf04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbaec0 bytes 080d46f9
+ 00bbaf04 bytes 083546f9
- 00bbaed8 ["INT_ADD", "register:40f0:8", ["const:bbaed8:8", "const:4:8"]]
- 00bbaed8 ["CALL", null, ["callee:00bd6e30:8"]]
+ 00bbaf1c ["INT_ADD", "register:40f0:8", ["const:bbaf1c:8", "const:4:8"]]
+ 00bbaf1c ["CALL", null, ["callee:00bd6e30:8"]]
- 00bbaed8 bytes c66f0094
+ 00bbaf1c bytes c56f0094
- 00bbaee8 ["INT_ADD", "register:40f0:8", ["const:bbaee8:8", "const:4:8"]]
- 00bbaee8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00bbaf2c ["INT_ADD", "register:40f0:8", ["const:bbaf2c:8", "const:4:8"]]
+ 00bbaf2c ["CALL", null, ["callee:00bdb060:8"]]
- 00bbaee8 bytes 4a800094
+ 00bbaf2c bytes 4d800094
~~~


<a id="compare-5c1a6ad6df23a884679410515631728b"></a>

### [`00bbb0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb0ec.md) → [`00bbb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb130.md) _ZNKSt8bad_cast4whatEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bbb138",
      "incomplete_value": false,
      "site": "00bbb13c",
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
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb0f4",
      "incomplete_value": false,
      "site": "00bbb0f8",
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
            "const:505:8"
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
      "00bbb138",
      "DATA",
      [
        "storage",
        "00294505",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbb138",
      "DATA",
      [
        "storage",
        "00294478",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb0ec.md#insn-00bbb0f4)
- 新版 `00bbb138`（命令位置の公開資料なし）

~~~diff
- 00bbb0f4 ["COPY", "tmp:0:8", ["const:505:8"]]
- 00bbb0f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bbb0f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bbb0f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bbb138 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 00bbb138 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bbb138 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bbb138 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bbb0f4 bytes 00141491
+ 00bbb138 bytes 00e01191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95ba704a9d69ed2976c6c7fe6a7f997f"></a>

### [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) → [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) FUN_00bbb19c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 22件 [`00bba6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba6bc.md) [`00bba800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba800.md) [`00bba8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba8a8.md) [`00bba944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba944.md) [`00bba9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9e0.md) · 呼出先 10件 [`00bdd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd380.md) [`00bdd3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd3e0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be16c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be16c0.md) [`00be1e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1e60.md)
- 新版 呼出元 22件 [`00bba700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba700.md) [`00bba844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba844.md) [`00bba8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba8ec.md) [`00bba988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba988.md) [`00bbaa24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa24.md) · 呼出先 10件 [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md) [`00bdd430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd430.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1710.md) [`00be1eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.85% / 新版 93.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbb1d0",
      "incomplete_value": false,
      "site": "00bbb1fc",
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
            "const:7a4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb18c",
      "incomplete_value": false,
      "site": "00bbb1b8",
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
            "const:838:8"
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
      "definition_site": "00bbb1f8",
      "incomplete_value": true,
      "site": "00bbb1fc",
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
      "definition_site": "00bbb1b4",
      "incomplete_value": true,
      "site": "00bbb1b8",
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
      "definition_site": "00bbb28c",
      "incomplete_value": false,
      "site": "00bbb294",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb248",
      "incomplete_value": false,
      "site": "00bbb250",
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
            "const:d0d:8"
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
      "00bbb1d0",
      "PARAM",
      [
        "storage",
        "002af838",
        null,
        "string"
      ]
    ],
    [
      "00bbb1f4",
      "READ",
      [
        "storage",
        "00c1bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "00bbb28c",
      "PARAM",
      [
        "storage",
        "0029dd0d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bbb1d0",
      "PARAM",
      [
        "storage",
        "002af7a4",
        null,
        "string"
      ]
    ],
    [
      "00bbb1f4",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ],
    [
      "00bbb28c",
      "PARAM",
      [
        "storage",
        "0029dd98",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md#insn-00bbb1b8) · [`00bbb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md#insn-00bbb250) · [`00bbb18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md#insn-00bbb18c)
- 新版 `00bbb1fc`（命令位置の公開資料なし） · `00bbb294`（命令位置の公開資料なし） · `00bbb1d0`（命令位置の公開資料なし）

~~~diff
- 00bbb1b8 ["INT_ADD", "register:40f0:8", ["const:bbb1b8:8", "const:4:8"]]
- 00bbb1b8 ["CALL", null, ["callee:00bdd3d0:8"]]
+ 00bbb1fc ["INT_ADD", "register:40f0:8", ["const:bbb1fc:8", "const:4:8"]]
+ 00bbb1fc ["CALL", null, ["callee:00bdd3d0:8"]]
- 00bbb1b8 bytes 72880094
+ 00bbb1fc bytes 75880094
- 00bbb250 ["INT_ADD", "register:40f0:8", ["const:bbb250:8", "const:4:8"]]
- 00bbb250 ["CALL", null, ["callee:00be1ee0:8"]]
+ 00bbb294 ["INT_ADD", "register:40f0:8", ["const:bbb294:8", "const:4:8"]]
+ 00bbb294 ["CALL", null, ["callee:00be1ee0:8"]]
- 00bbb250 bytes 109b0094
+ 00bbb294 bytes 139b0094
- 00bbb18c ["COPY", "tmp:0:8", ["const:838:8"]]
- 00bbb18c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bbb18c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bbb18c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bbb1d0 ["COPY", "tmp:0:8", ["const:7a4:8"]]
+ 00bbb1d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bbb1d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bbb1d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bbb18c bytes 00e02091
+ 00bbb1d0 bytes 00901e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2d1ce23fa5aa437ed944145fe4f2bca"></a>

### [`00bbb47c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb47c.md) → [`00bbb4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb4c0.md) FUN_00bbb4c0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bbaa70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa70.md) · 呼出先 2件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)
- 新版 呼出元 1件 [`00bbaab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaab4.md) · 呼出先 2件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.22% / 新版 93.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbb4f4",
      "incomplete_value": true,
      "site": "00bbb508",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
              ],
              [
                "leaf",
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb4b0",
      "incomplete_value": true,
      "site": "00bbb4c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:4010:8"
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
      "00bbb4f0",
      "READ",
      [
        "storage",
        "00c1bff8",
        null,
        "pointer"
      ]
    ],
    [
      "00bbb4f4",
      "READ",
      [
        "storage",
        "00c1c000",
        null,
        "pointer"
      ]
    ],
    [
      "00bbb4f4",
      "PARAM",
      [
        "storage",
        "00c16bd8",
        "_ZTIN10__cxxabiv117__class_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00bbb4f0",
      "READ",
      [
        "storage",
        "00c1c048",
        null,
        "pointer"
      ]
    ],
    [
      "00bbb4f4",
      "READ",
      [
        "storage",
        "00c1c050",
        null,
        "pointer"
      ]
    ],
    [
      "00bbb4f4",
      "PARAM",
      [
        "storage",
        "00c16c28",
        "_ZTIN10__cxxabiv117__class_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb4c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb47c.md#insn-00bbb4c4) · [`00bbb4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb47c.md#insn-00bbb4a0) · [`00bbb4ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb47c.md#insn-00bbb4ac)
- 新版 `00bbb508`（命令位置の公開資料なし） · `00bbb4e4`（命令位置の公開資料なし） · `00bbb4f0`（命令位置の公開資料なし）

~~~diff
- 00bbb4c4 ["INT_ADD", "register:40f0:8", ["const:bbb4c4:8", "const:4:8"]]
- 00bbb4c4 ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00bbb508 ["INT_ADD", "register:40f0:8", ["const:bbb508:8", "const:4:8"]]
+ 00bbb508 ["CALL", null, ["callee:00bdb7c0:8"]]
- 00bbb4c4 bytes ab800094
+ 00bbb508 bytes ae800094
- 00bbb4a0 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00bbb4e4 ["COPY", "register:4040:8", ["const:c1c000:8"]]
- 00bbb4a0 bytes 08030090
+ 00bbb4e4 bytes 080300b0
- 00bbb4ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff8:8"]]
- 00bbb4ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbb4f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
+ 00bbb4f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbb4ac bytes 08fd47f9
+ 00bbb4f0 bytes 082540f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88c5717465e408885f0281f3d69f8d9a"></a>

### [`00bbba60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbba60.md) → [`00bbbaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbaa4.md) FUN_00bbbaa4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md) [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md) [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbbb04",
      "incomplete_value": true,
      "site": "00bbbb08",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1c000:8"
              ],
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbac0",
      "incomplete_value": true,
      "site": "00bbbac4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
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
      "definition_site": "00bbbaf4",
      "incomplete_value": true,
      "site": "00bbbb08",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1c000:8"
              ],
              [
                "leaf",
                "const:58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbab0",
      "incomplete_value": true,
      "site": "00bbbac4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1c000:8"
              ],
              [
                "leaf",
                "const:8:8"
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
      "00bbbaf0",
      "READ",
      [
        "storage",
        "00c1bff8",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbaf4",
      "READ",
      [
        "storage",
        "00c1c008",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbaf4",
      "PARAM",
      [
        "storage",
        "00c16bf0",
        "_ZTIN10__cxxabiv117__pbase_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00bbbaf0",
      "READ",
      [
        "storage",
        "00c1c048",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbaf4",
      "READ",
      [
        "storage",
        "00c1c058",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbaf4",
      "PARAM",
      [
        "storage",
        "00c16c40",
        "_ZTIN10__cxxabiv117__pbase_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbba60.md#insn-00bbbac4) · [`00bbba8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbba60.md#insn-00bbba8c) · [`00bbbaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbba60.md#insn-00bbbaa0)
- 新版 `00bbbb08`（命令位置の公開資料なし） · `00bbbad0`（命令位置の公開資料なし） · `00bbbae4`（命令位置の公開資料なし）

~~~diff
- 00bbbac4 ["INT_ADD", "register:40f0:8", ["const:bbbac4:8", "const:4:8"]]
- 00bbbac4 ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00bbbb08 ["INT_ADD", "register:40f0:8", ["const:bbbb08:8", "const:4:8"]]
+ 00bbbb08 ["CALL", null, ["callee:00bdb7c0:8"]]
- 00bbbac4 bytes 2b7f0094
+ 00bbbb08 bytes 2e7f0094
- 00bbba8c ["INT_ADD", "register:40f0:8", ["const:bbba8c:8", "const:4:8"]]
- 00bbba8c ["CALL", null, ["callee:00bde9d0:8"]]
+ 00bbbad0 ["INT_ADD", "register:40f0:8", ["const:bbbad0:8", "const:4:8"]]
+ 00bbbad0 ["CALL", null, ["callee:00bde9d0:8"]]
- 00bbba8c bytes bd8b0094
+ 00bbbad0 bytes c08b0094
- 00bbbaa0 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00bbbae4 ["COPY", "register:4040:8", ["const:c1c000:8"]]
- 00bbbaa0 bytes 08030090
+ 00bbbae4 bytes 080300b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d380dba5f2f6f8b34a63efad70b2c83"></a>

### [`00bbbb0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbb0c.md) → [`00bbbb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbb50.md) FUN_00bbbb50

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bbbdc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbdc8.md) [`00bbbebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbebc.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md) [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bbbe0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbe0c.md) [`00bbbf00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbf00.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md) [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 89.14% / 新版 89.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 9件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbbb7c",
      "incomplete_value": true,
      "site": "00bbbb80",
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
      "definition_site": "00bbbb38",
      "incomplete_value": true,
      "site": "00bbbb3c",
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
      "definition_site": "00bbbc90",
      "incomplete_value": true,
      "site": "00bbbc94",
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
                "register:4040:8"
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
      "definition_site": "00bbbc4c",
      "incomplete_value": true,
      "site": "00bbbc50",
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
                "register:4040:8"
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
    "ordinal": 13,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbbc18",
      "incomplete_value": true,
      "site": "00bbbc24",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1c000:8"
              ],
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbbd4",
      "incomplete_value": true,
      "site": "00bbbbe0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
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
      "00bbbb78",
      "READ",
      [
        "storage",
        "00c1c010",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbbe0",
      "READ",
      [
        "storage",
        "00c1bff8",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbbe0",
      "PARAM",
      [
        "storage",
        "00c16bc0",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00bbbb78",
      "READ",
      [
        "storage",
        "00c1c060",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbbe0",
      "READ",
      [
        "storage",
        "00c1c048",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbbe0",
      "PARAM",
      [
        "storage",
        "00c16c10",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbb9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbb0c.md#insn-00bbbb9c) · [`00bbbbc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbb0c.md#insn-00bbbbc8) · [`00bbbbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbb0c.md#insn-00bbbbe0)
- 新版 `00bbbbe0`（命令位置の公開資料なし） · `00bbbc0c`（命令位置の公開資料なし） · `00bbbc24`（命令位置の公開資料なし）

~~~diff
- 00bbbb9c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ff8:8"]]
- 00bbbb9c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbbbe0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:48:8"]]
+ 00bbbbe0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbbb9c bytes 21fc47f9
+ 00bbbbe0 bytes 212440f9
- 00bbbbc8 ["COPY", "register:4008:8", ["const:c1b000:8"]]
+ 00bbbc0c ["COPY", "register:4008:8", ["const:c1c000:8"]]
- 00bbbbc8 bytes 01030090
+ 00bbbc0c bytes 010300b0
- 00bbbbe0 ["INT_ADD", "register:40f0:8", ["const:bbbbe0:8", "const:4:8"]]
- 00bbbbe0 ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00bbbc24 ["INT_ADD", "register:40f0:8", ["const:bbbc24:8", "const:4:8"]]
+ 00bbbc24 ["CALL", null, ["callee:00bdb7c0:8"]]
- 00bbbbe0 bytes e47e0094
+ 00bbbc24 bytes e77e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d209222d6d6441168c05e7571dee1561"></a>

### [`00bbbdc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbdc8.md) → [`00bbbe0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbe0c.md) FUN_00bbbe0c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbbb0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbb0c.md) · 呼出先 2件 [`00bbbebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbebc.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)
- 新版 呼出元 1件 [`00bbbb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbb50.md) · 呼出先 2件 [`00bbbf00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbf00.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.44% / 新版 93.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbbeac",
      "incomplete_value": true,
      "site": "00bbbeb8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1c000:8"
              ],
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbe68",
      "incomplete_value": true,
      "site": "00bbbe74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
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
      "definition_site": "00bbbeb0",
      "incomplete_value": true,
      "site": "00bbbeb8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1c000:8"
              ],
              [
                "leaf",
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbe6c",
      "incomplete_value": true,
      "site": "00bbbe74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1c000:8"
              ],
              [
                "leaf",
                "const:30:8"
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
      "00bbbe30",
      "READ",
      [
        "storage",
        "00c1bff8",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbe34",
      "READ",
      [
        "storage",
        "00c1c018",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbe44",
      "PARAM",
      [
        "storage",
        "00c16bc0",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00bbbe30",
      "READ",
      [
        "storage",
        "00c1c048",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbe34",
      "READ",
      [
        "storage",
        "00c1c068",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbe44",
      "PARAM",
      [
        "storage",
        "00c16c10",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbe74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbdc8.md#insn-00bbbe74) · [`00bbbde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbdc8.md#insn-00bbbde0) · [`00bbbdec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbdc8.md#insn-00bbbdec)
- 新版 `00bbbeb8`（命令位置の公開資料なし） · `00bbbe24`（命令位置の公開資料なし） · `00bbbe30`（命令位置の公開資料なし）

~~~diff
- 00bbbe74 ["INT_ADD", "register:40f0:8", ["const:bbbe74:8", "const:4:8"]]
- 00bbbe74 ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00bbbeb8 ["INT_ADD", "register:40f0:8", ["const:bbbeb8:8", "const:4:8"]]
+ 00bbbeb8 ["CALL", null, ["callee:00bdb7c0:8"]]
- 00bbbe74 bytes 3f7e0094
+ 00bbbeb8 bytes 427e0094
- 00bbbde0 ["COPY", "register:40a0:8", ["const:c1b000:8"]]
+ 00bbbe24 ["COPY", "register:40a0:8", ["const:c1c000:8"]]
- 00bbbde0 bytes 14030090
+ 00bbbe24 bytes 140300b0
- 00bbbdec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ff8:8"]]
- 00bbbdec ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbbe30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:48:8"]]
+ 00bbbe30 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbbdec bytes 94fe47f9
+ 00bbbe30 bytes 942640f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91c8a77b823f33b29b3df49f95249431"></a>

### [`00bbbf5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbf5c.md) → [`00bbbfa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbfa0.md) FUN_00bbbfa0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md) [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md) [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.21% / 新版 91.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbc010",
      "incomplete_value": true,
      "site": "00bbc020",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1c000:8"
              ],
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbfcc",
      "incomplete_value": true,
      "site": "00bbbfdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
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
      "definition_site": "00bbc01c",
      "incomplete_value": true,
      "site": "00bbc020",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1c000:8"
              ],
              [
                "leaf",
                "const:78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbfd8",
      "incomplete_value": true,
      "site": "00bbbfdc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1c000:8"
              ],
              [
                "leaf",
                "const:28:8"
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
      "definition_site": "00bbc044",
      "incomplete_value": true,
      "site": "00bbc050",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1c000:8"
              ],
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbc000",
      "incomplete_value": true,
      "site": "00bbc00c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
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
      "00bbbfc0",
      "READ",
      [
        "storage",
        "00c1c010",
        null,
        "pointer"
      ]
    ],
    [
      "00bbc010",
      "READ",
      [
        "storage",
        "00c1bff8",
        null,
        "pointer"
      ]
    ],
    [
      "00bbc010",
      "PARAM",
      [
        "storage",
        "00c16bc0",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00bbbfc0",
      "READ",
      [
        "storage",
        "00c1c060",
        null,
        "pointer"
      ]
    ],
    [
      "00bbc010",
      "READ",
      [
        "storage",
        "00c1c048",
        null,
        "pointer"
      ]
    ],
    [
      "00bbc010",
      "PARAM",
      [
        "storage",
        "00c16c10",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbfdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbf5c.md#insn-00bbbfdc) · [`00bbc000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbf5c.md#insn-00bbc000) · [`00bbc00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbf5c.md#insn-00bbc00c)
- 新版 `00bbc020`（命令位置の公開資料なし） · `00bbc044`（命令位置の公開資料なし） · `00bbc050`（命令位置の公開資料なし）

~~~diff
- 00bbbfdc ["INT_ADD", "register:40f0:8", ["const:bbbfdc:8", "const:4:8"]]
- 00bbbfdc ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00bbc020 ["INT_ADD", "register:40f0:8", ["const:bbc020:8", "const:4:8"]]
+ 00bbc020 ["CALL", null, ["callee:00bdb7c0:8"]]
- 00bbbfdc bytes e57d0094
+ 00bbc020 bytes e87d0094
- 00bbc000 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ff8:8"]]
- 00bbc000 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbc044 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:48:8"]]
+ 00bbc044 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbc000 bytes 21fc47f9
+ 00bbc044 bytes 212440f9
- 00bbc00c ["INT_ADD", "register:40f0:8", ["const:bbc00c:8", "const:4:8"]]
- 00bbc00c ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00bbc050 ["INT_ADD", "register:40f0:8", ["const:bbc050:8", "const:4:8"]]
+ 00bbc050 ["CALL", null, ["callee:00bdb7c0:8"]]
- 00bbc00c bytes d97d0094
+ 00bbc050 bytes dc7d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00ba1c9454457b90313a1e24325147fa"></a>

### [`00bbcbcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbcbcc.md) → [`00bbcc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbcc10.md) __cxa_demangle

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1de0.md) · 呼出先 10件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbdd64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdd64.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00be1e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e30.md) · 呼出先 10件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbdda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdda8.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbcf58",
      "incomplete_value": false,
      "site": "00bbcf58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbcf14",
      "incomplete_value": false,
      "site": "00bbcf14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
          ]
        ]
      ]
    },
    "ordinal": 90,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbd1a8",
      "incomplete_value": false,
      "site": "00bbd1b0",
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
            "const:7d9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbd164",
      "incomplete_value": false,
      "site": "00bbd16c",
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
            "const:866:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbcf58",
      "DATA",
      [
        "storage",
        "00c199e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbd0b0",
      "PARAM",
      [
        "storage",
        "002a90e2",
        null,
        "string"
      ]
    ],
    [
      "00bbd1a8",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bbcf58",
      "DATA",
      [
        "storage",
        "00c19a38",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbd0b0",
      "PARAM",
      [
        "storage",
        "002a917c",
        null,
        "string"
      ]
    ],
    [
      "00bbd1a8",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbd16c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbcbcc.md#insn-00bbd16c) · [`00bbcc28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbcbcc.md#insn-00bbcc28) · [`00bbcdb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbcbcc.md#insn-00bbcdb4)
- 新版 `00bbd1b0`（命令位置の公開資料なし） · `00bbcc6c`（命令位置の公開資料なし） · `00bbcdf8`（命令位置の公開資料なし）

~~~diff
- 00bbd16c ["INT_ADD", "register:40f0:8", ["const:bbd16c:8", "const:4:8"]]
- 00bbd16c ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bbd1b0 ["INT_ADD", "register:40f0:8", ["const:bbd1b0:8", "const:4:8"]]
+ 00bbd1b0 ["CALL", null, ["callee:00bbb19c:8"]]
- 00bbd16c bytes fbf7ff97
+ 00bbd1b0 bytes fbf7ff97
- 00bbcc28 ["INT_ADD", "register:40f0:8", ["const:bbcc28:8", "const:4:8"]]
- 00bbcc28 ["CALL", null, ["callee:00bdb190:8"]]
+ 00bbcc6c ["INT_ADD", "register:40f0:8", ["const:bbcc6c:8", "const:4:8"]]
+ 00bbcc6c ["CALL", null, ["callee:00bdb190:8"]]
- 00bbcc28 bytes 46790094
+ 00bbcc6c bytes 49790094
- 00bbcdb4 ["INT_ADD", "register:40f0:8", ["const:bbcdb4:8", "const:4:8"]]
- 00bbcdb4 ["CALL", null, ["callee:00bbde5c:8"]]
+ 00bbcdf8 ["INT_ADD", "register:40f0:8", ["const:bbcdf8:8", "const:4:8"]]
+ 00bbcdf8 ["CALL", null, ["callee:00bbde5c:8"]]
- 00bbcdb4 bytes 19040094
+ 00bbcdf8 bytes 19040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93ca8925c429d499bdc40ce17ffbc89d"></a>

### [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) → [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) FUN_00bbd308

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00bbcbcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbcbcc.md) [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bc489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md) · 呼出先 31件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbdcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdcd8.md) [`00bbdd64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdd64.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md)
- 新版 呼出元 5件 [`00bbcc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbcc10.md) [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) · 呼出先 31件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbdd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdd1c.md) [`00bbdda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdda8.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.42% / 新版 98.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbd530",
      "incomplete_value": false,
      "site": "00bbd530",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbd4ec",
      "incomplete_value": false,
      "site": "00bbd4ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbd974",
      "incomplete_value": false,
      "site": "00bbd974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbd930",
      "incomplete_value": false,
      "site": "00bbd930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "ordinal": 67,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbdb78",
      "incomplete_value": false,
      "site": "00bbdb84",
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
            "const:4ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbdb34",
      "incomplete_value": false,
      "site": "00bbdb40",
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
            "const:454:8"
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbd530",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbd7d4",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbd7f8",
      "DATA",
      [
        "storage",
        "002a029c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbd530",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbd7d4",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbd7f8",
      "DATA",
      [
        "storage",
        "002a0327",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbd974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md#insn-00bbd974) · [`00bbdb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md#insn-00bbdb40) · [`00bbdc88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md#insn-00bbdc88)
- 新版 `00bbd9b8`（命令位置の公開資料なし） · `00bbdb84`（命令位置の公開資料なし） · `00bbdccc`（命令位置の公開資料なし）

~~~diff
- 00bbd974 ["INT_ADD", "register:40f0:8", ["const:bbd974:8", "const:4:8"]]
- 00bbd974 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bbd9b8 ["INT_ADD", "register:40f0:8", ["const:bbd9b8:8", "const:4:8"]]
+ 00bbd9b8 ["CALL", null, ["callee:00bdd250:8"]]
- 00bbd974 bytes 237e0094
+ 00bbd9b8 bytes 267e0094
- 00bbdb40 ["INT_ADD", "register:40f0:8", ["const:bbdb40:8", "const:4:8"]]
- 00bbdb40 ["CALL", null, ["callee:00bbdda8:8"]]
+ 00bbdb84 ["INT_ADD", "register:40f0:8", ["const:bbdb84:8", "const:4:8"]]
+ 00bbdb84 ["CALL", null, ["callee:00bbdda8:8"]]
- 00bbdb40 bytes 89000094
+ 00bbdb84 bytes 89000094
- 00bbdc88 ["INT_ADD", "register:40f0:8", ["const:bbdc88:8", "const:4:8"]]
- 00bbdc88 ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bbdccc ["INT_ADD", "register:40f0:8", ["const:bbdccc:8", "const:4:8"]]
+ 00bbdccc ["CALL", null, ["callee:00bbb19c:8"]]
- 00bbdc88 bytes 34f5ff97
+ 00bbdccc bytes 34f5ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bb6b7ed6e6db206a3f3a545fddb0c30"></a>

### [`00bbdd64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdd64.md) → [`00bbdda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdda8.md) FUN_00bbdda8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbcbcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbcbcc.md) [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 3件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 2件 [`00bbcc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbcc10.md) [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbde18",
      "incomplete_value": true,
      "site": "00bbde18",
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
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbddd4",
      "incomplete_value": true,
      "site": "00bbddd4",
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
            "const:758:8"
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
      "00bbde18",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bbde18",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbdd9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdd64.md#insn-00bbdd9c) · [`00bbddc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdd64.md#insn-00bbddc4) · [`00bbddcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdd64.md#insn-00bbddcc)
- 新版 `00bbdde0`（命令位置の公開資料なし） · `00bbde08`（命令位置の公開資料なし） · `00bbde10`（命令位置の公開資料なし）

~~~diff
- 00bbdd9c ["INT_ADD", "register:40f0:8", ["const:bbdd9c:8", "const:4:8"]]
- 00bbdd9c ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bbdde0 ["INT_ADD", "register:40f0:8", ["const:bbdde0:8", "const:4:8"]]
+ 00bbdde0 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bbdd9c bytes f97c0094
+ 00bbdde0 bytes fc7c0094
- 00bbddc4 ["INT_ADD", "register:40f0:8", ["const:bbddc4:8", "const:4:8"]]
- 00bbddc4 ["CALL", null, ["callee:00bdb190:8"]]
+ 00bbde08 ["INT_ADD", "register:40f0:8", ["const:bbde08:8", "const:4:8"]]
+ 00bbde08 ["CALL", null, ["callee:00bdb190:8"]]
- 00bbddc4 bytes df740094
+ 00bbde08 bytes e2740094
- 00bbddcc ["COPY", "tmp:0:8", ["const:758:8"]]
- 00bbddcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bbddcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bbddcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bbde10 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 00bbde10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bbde10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bbde10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bbddcc bytes 08611d91
+ 00bbde10 bytes 08a11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d436f25414b8a40f37ccc9d09eabc5d"></a>

### [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) → [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) FUN_00bbde5c

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 15件 [`00bbcbcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbcbcc.md) [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 38件 [`00bbdcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdcd8.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bbfdb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfdb4.md) [`00bc1328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1328.md)
- 新版 呼出元 15件 [`00bbcc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbcc10.md) [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 38件 [`00bbdd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdd1c.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bbfdf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfdf8.md) [`00bc136c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc136c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.37% / 新版 95.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 15件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbdfc0",
      "incomplete_value": false,
      "site": "00bbdfc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbdf7c",
      "incomplete_value": false,
      "site": "00bbdf7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbe040",
      "incomplete_value": false,
      "site": "00bbe040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbdffc",
      "incomplete_value": false,
      "site": "00bbdffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbe120",
      "incomplete_value": false,
      "site": "00bbe120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbe0dc",
      "incomplete_value": false,
      "site": "00bbe0dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbdea8",
      "DATA",
      [
        "storage",
        "002fcb68",
        "switchD_00bbde6c::switchdataD_002fcb68",
        "ushort"
      ]
    ],
    [
      "00bbdfc0",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbe040",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bbdea8",
      "DATA",
      [
        "storage",
        "002fcb68",
        "switchD_00bbdeb0::switchdataD_002fcb68",
        "ushort"
      ]
    ],
    [
      "00bbdfc0",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbe040",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md#insn-00bbde60) · [`00bbdf1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md#insn-00bbdf1c) · [`00bbdf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md#insn-00bbdf4c)
- 新版 `00bbdea4`（命令位置の公開資料なし） · `00bbdf60`（命令位置の公開資料なし） · `00bbdf90`（命令位置の公開資料なし）

~~~diff
- 00bbde60 ["COPY", "register:4070:8", ["const:bbde70:8"]]
+ 00bbdea4 ["COPY", "register:4070:8", ["const:bbdeb4:8"]]
- 00bbde60 bytes 8e000010
+ 00bbdea4 bytes 8e000010
- 00bbdf1c ["INT_ADD", "register:40f0:8", ["const:bbdf1c:8", "const:4:8"]]
- 00bbdf1c ["CALL", null, ["callee:00bd1778:8"]]
+ 00bbdf60 ["INT_ADD", "register:40f0:8", ["const:bbdf60:8", "const:4:8"]]
+ 00bbdf60 ["CALL", null, ["callee:00bd1778:8"]]
- 00bbdf1c bytes 064e0094
+ 00bbdf60 bytes 064e0094
- 00bbdf4c ["INT_ADD", "register:40f0:8", ["const:bbdf4c:8", "const:4:8"]]
- 00bbdf4c ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bbdf90 ["INT_ADD", "register:40f0:8", ["const:bbdf90:8", "const:4:8"]]
+ 00bbdf90 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bbdf4c bytes 8d7c0094
+ 00bbdf90 bytes 907c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46752096d0785dddebf1ed0428687fc1"></a>

### [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) → [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) FUN_00bbf39c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 7件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bc245c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc245c.md) [`00bc5b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5b0c.md) · 呼出先 19件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbdcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdcd8.md) [`00bbf1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf1b0.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bc017c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc017c.md)
- 新版 呼出元 7件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bc24a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md) [`00bc5b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5b50.md) · 呼出先 19件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbdd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdd1c.md) [`00bbf1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf1f4.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bc01c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc01c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.24% / 新版 98.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbf798",
      "incomplete_value": false,
      "site": "00bbf798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbf754",
      "incomplete_value": false,
      "site": "00bbf754",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbf7bc",
      "incomplete_value": false,
      "site": "00bbf7bc",
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
            "const:a2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbf778",
      "incomplete_value": false,
      "site": "00bbf778",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbfa84",
      "incomplete_value": false,
      "site": "00bbfa84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbfa40",
      "incomplete_value": false,
      "site": "00bbfa40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "ordinal": 74,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbf4fc",
      "PARAM",
      [
        "storage",
        "002a11e3",
        null,
        "string"
      ]
    ],
    [
      "00bbf67c",
      "DATA",
      [
        "storage",
        "00c19748",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbf798",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bbf4fc",
      "PARAM",
      [
        "storage",
        "002a126e",
        null,
        "string"
      ]
    ],
    [
      "00bbf67c",
      "DATA",
      [
        "storage",
        "00c19798",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbf798",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbf3e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md#insn-00bbf3e8) · [`00bbf438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md#insn-00bbf438) · [`00bbf444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md#insn-00bbf444)
- 新版 `00bbf42c`（命令位置の公開資料なし） · `00bbf47c`（命令位置の公開資料なし） · `00bbf488`（命令位置の公開資料なし）

~~~diff
- 00bbf3e8 ["INT_ADD", "register:40f0:8", ["const:bbf3e8:8", "const:4:8"]]
- 00bbf3e8 ["CALL", null, ["callee:00bc15e4:8"]]
+ 00bbf42c ["INT_ADD", "register:40f0:8", ["const:bbf42c:8", "const:4:8"]]
+ 00bbf42c ["CALL", null, ["callee:00bc15e4:8"]]
- 00bbf3e8 bytes 6e080094
+ 00bbf42c bytes 6e080094
- 00bbf438 ["INT_ADD", "register:40f0:8", ["const:bbf438:8", "const:4:8"]]
- 00bbf438 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bbf47c ["INT_ADD", "register:40f0:8", ["const:bbf47c:8", "const:4:8"]]
+ 00bbf47c ["CALL", null, ["callee:00bdd250:8"]]
- 00bbf438 bytes 72770094
+ 00bbf47c bytes 75770094
- 00bbf444 ["INT_ADD", "register:40f0:8", ["const:bbf444:8", "const:4:8"]]
- 00bbf444 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bbf488 ["INT_ADD", "register:40f0:8", ["const:bbf488:8", "const:4:8"]]
+ 00bbf488 ["CALL", null, ["callee:00bde2c0:8"]]
- 00bbf444 bytes 8b7b0094
+ 00bbf488 bytes 8e7b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75a549b12567d9200c67c88218008af4"></a>

### [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) → [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) FUN_00bbfad0

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bc1710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1710.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 13件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bbff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md)
- 新版 呼出元 4件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) [`00bc1754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1754.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 13件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) [`00bbff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbfd48",
      "incomplete_value": false,
      "site": "00bbfd4c",
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
            "const:779:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbfd04",
      "incomplete_value": false,
      "site": "00bbfd08",
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
            "const:806:8"
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
      "00bbfd00",
      "DATA",
      [
        "storage",
        "00c197b8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbfd00",
      "DATA",
      [
        "storage",
        "00c19828",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbfd48",
      "PARAM",
      [
        "storage",
        "00295806",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbfd00",
      "DATA",
      [
        "storage",
        "00c19808",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbfd00",
      "DATA",
      [
        "storage",
        "00c19878",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbfd48",
      "PARAM",
      [
        "storage",
        "00295779",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbfd08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md#insn-00bbfd08) · [`00bbfafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md#insn-00bbfafc) · [`00bbfb24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md#insn-00bbfb24)
- 新版 `00bbfd4c`（命令位置の公開資料なし） · `00bbfb40`（命令位置の公開資料なし） · `00bbfb68`（命令位置の公開資料なし）

~~~diff
- 00bbfd08 ["INT_ADD", "register:40f0:8", ["const:bbfd08:8", "const:4:8"]]
- 00bbfd08 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bbfd4c ["INT_ADD", "register:40f0:8", ["const:bbfd4c:8", "const:4:8"]]
+ 00bbfd4c ["CALL", null, ["callee:00bdb180:8"]]
- 00bbfd08 bytes 0a6d0094
+ 00bbfd4c bytes 0d6d0094
- 00bbfafc ["INT_ADD", "register:40f0:8", ["const:bbfafc:8", "const:4:8"]]
- 00bbfafc ["CALL", null, ["callee:00bbd308:8"]]
+ 00bbfb40 ["INT_ADD", "register:40f0:8", ["const:bbfb40:8", "const:4:8"]]
+ 00bbfb40 ["CALL", null, ["callee:00bbd308:8"]]
- 00bbfafc bytes f2f5ff97
+ 00bbfb40 bytes f2f5ff97
- 00bbfb24 ["INT_ADD", "register:40f0:8", ["const:bbfb24:8", "const:4:8"]]
- 00bbfb24 ["CALL", null, ["callee:00bc2f0c:8"]]
+ 00bbfb68 ["INT_ADD", "register:40f0:8", ["const:bbfb68:8", "const:4:8"]]
+ 00bbfb68 ["CALL", null, ["callee:00bc2f0c:8"]]
- 00bbfb24 bytes e90c0094
+ 00bbfb68 bytes e90c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e551a570f71c504018f3c9bfaba22e07"></a>

### [`00bbfe8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfe8c.md) → [`00bbfed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfed0.md) FUN_00bbfed0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbff34",
      "incomplete_value": false,
      "site": "00bbff34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbfef0",
      "incomplete_value": false,
      "site": "00bbfef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbff34",
      "DATA",
      [
        "storage",
        "00c19898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bbff34",
      "DATA",
      [
        "storage",
        "00c198e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbfec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfe8c.md#insn-00bbfec0) · [`00bbfee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfe8c.md#insn-00bbfee4) · [`00bbff28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfe8c.md#insn-00bbff28)
- 新版 `00bbff04`（命令位置の公開資料なし） · `00bbff28`（命令位置の公開資料なし） · `00bbff6c`（命令位置の公開資料なし）

~~~diff
- 00bbfec0 ["INT_ADD", "register:40f0:8", ["const:bbfec0:8", "const:4:8"]]
- 00bbfec0 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bbff04 ["INT_ADD", "register:40f0:8", ["const:bbff04:8", "const:4:8"]]
+ 00bbff04 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bbfec0 bytes b0740094
+ 00bbff04 bytes b3740094
- 00bbfee4 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00bbfee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bbfee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bbfee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bbff28 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 00bbff28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bbff28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bbff28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bbfee4 bytes 08612291
+ 00bbff28 bytes 08a12391
- 00bbff28 ["INT_ADD", "register:40f0:8", ["const:bbff28:8", "const:4:8"]]
- 00bbff28 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bbff6c ["INT_ADD", "register:40f0:8", ["const:bbff6c:8", "const:4:8"]]
+ 00bbff6c ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bbff28 bytes 966c0094
+ 00bbff6c bytes 996c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac070929a58c79cb0bf04958d27aa4bf"></a>

### [`00bbff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md) → [`00bbff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md) FUN_00bbff70

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bc1710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1710.md) [`00bc245c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc245c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 4件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 10件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) [`00bc1754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1754.md) [`00bc24a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 4件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc0094",
      "incomplete_value": false,
      "site": "00bc00a4",
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
            "const:195:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0050",
      "incomplete_value": false,
      "site": "00bc0060",
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
            "const:10a:8"
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
      "definition_site": "00bc009c",
      "incomplete_value": false,
      "site": "00bc00a4",
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
            "const:7d9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0058",
      "incomplete_value": false,
      "site": "00bc0060",
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
            "const:866:8"
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
      "definition_site": "00bc00b4",
      "incomplete_value": false,
      "site": "00bc00c4",
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
            "const:195:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0070",
      "incomplete_value": false,
      "site": "00bc0080",
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
            "const:10a:8"
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
      "00bc0094",
      "PARAM",
      [
        "storage",
        "002a210a",
        null,
        "string"
      ]
    ],
    [
      "00bc009c",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc00b4",
      "PARAM",
      [
        "storage",
        "002a210a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc0094",
      "PARAM",
      [
        "storage",
        "002a2195",
        null,
        "string"
      ]
    ],
    [
      "00bc009c",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc00b4",
      "PARAM",
      [
        "storage",
        "002a2195",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md#insn-00bc0060) · [`00bc0080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md#insn-00bc0080) · [`00bbff98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md#insn-00bbff98)
- 新版 `00bc00a4`（命令位置の公開資料なし） · `00bc00c4`（命令位置の公開資料なし） · `00bbffdc`（命令位置の公開資料なし）

~~~diff
- 00bc0060 ["INT_ADD", "register:40f0:8", ["const:bc0060:8", "const:4:8"]]
- 00bc0060 ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bc00a4 ["INT_ADD", "register:40f0:8", ["const:bc00a4:8", "const:4:8"]]
+ 00bc00a4 ["CALL", null, ["callee:00bbb19c:8"]]
- 00bc0060 bytes 3eecff97
+ 00bc00a4 bytes 3eecff97
- 00bc0080 ["INT_ADD", "register:40f0:8", ["const:bc0080:8", "const:4:8"]]
- 00bc0080 ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bc00c4 ["INT_ADD", "register:40f0:8", ["const:bc00c4:8", "const:4:8"]]
+ 00bc00c4 ["CALL", null, ["callee:00bbb19c:8"]]
- 00bc0080 bytes 36ecff97
+ 00bc00c4 bytes 36ecff97
- 00bbff98 ["INT_ADD", "register:40f0:8", ["const:bbff98:8", "const:4:8"]]
- 00bbff98 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bbffdc ["INT_ADD", "register:40f0:8", ["const:bbffdc:8", "const:4:8"]]
+ 00bbffdc ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bbff98 bytes 7a740094
+ 00bbffdc bytes 7d740094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3106443b9330c18ef4f39bb864178b3"></a>

### [`00bc0088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0088.md) → [`00bc00cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc00cc.md) FUN_00bc00cc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0154",
      "incomplete_value": false,
      "site": "00bc0154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0110",
      "incomplete_value": false,
      "site": "00bc0110",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc0154",
      "DATA",
      [
        "storage",
        "00c19978",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc0154",
      "DATA",
      [
        "storage",
        "00c199c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc00e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0088.md#insn-00bc00e0) · [`00bc0104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0088.md#insn-00bc0104) · [`00bc0178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0088.md#insn-00bc0178)
- 新版 `00bc0124`（命令位置の公開資料なし） · `00bc0148`（命令位置の公開資料なし） · `00bc01bc`（命令位置の公開資料なし）

~~~diff
- 00bc00e0 ["INT_ADD", "register:40f0:8", ["const:bc00e0:8", "const:4:8"]]
- 00bc00e0 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc0124 ["INT_ADD", "register:40f0:8", ["const:bc0124:8", "const:4:8"]]
+ 00bc0124 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc00e0 bytes 28740094
+ 00bc0124 bytes 2b740094
- 00bc0104 ["COPY", "tmp:0:8", ["const:978:8"]]
- 00bc0104 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0104 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0104 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0148 ["COPY", "tmp:0:8", ["const:9c8:8"]]
+ 00bc0148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0104 bytes 08e12591
+ 00bc0148 bytes 08212791
- 00bc0178 ["INT_ADD", "register:40f0:8", ["const:bc0178:8", "const:4:8"]]
- 00bc0178 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc01bc ["INT_ADD", "register:40f0:8", ["const:bc01bc:8", "const:4:8"]]
+ 00bc01bc ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc0178 bytes 026c0094
+ 00bc01bc bytes 056c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfe80cb41e0c0827e1c4215d56d5e07f"></a>

### [`00bc035c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc035c.md) → [`00bc03a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc03a0.md) FUN_00bc03a0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0404",
      "incomplete_value": false,
      "site": "00bc0404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc03c0",
      "incomplete_value": false,
      "site": "00bc03c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc0404",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc0404",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc035c.md#insn-00bc0390) · [`00bc03b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc035c.md#insn-00bc03b4) · [`00bc0408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc035c.md#insn-00bc0408)
- 新版 `00bc03d4`（命令位置の公開資料なし） · `00bc03f8`（命令位置の公開資料なし） · `00bc044c`（命令位置の公開資料なし）

~~~diff
- 00bc0390 ["INT_ADD", "register:40f0:8", ["const:bc0390:8", "const:4:8"]]
- 00bc0390 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc03d4 ["INT_ADD", "register:40f0:8", ["const:bc03d4:8", "const:4:8"]]
+ 00bc03d4 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc0390 bytes 7c730094
+ 00bc03d4 bytes 7f730094
- 00bc03b4 ["COPY", "tmp:0:8", ["const:758:8"]]
- 00bc03b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc03b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc03b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc03f8 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 00bc03f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc03f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc03f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc03b4 bytes 08611d91
+ 00bc03f8 bytes 08a11e91
- 00bc0408 ["INT_ADD", "register:40f0:8", ["const:bc0408:8", "const:4:8"]]
- 00bc0408 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc044c ["INT_ADD", "register:40f0:8", ["const:bc044c:8", "const:4:8"]]
+ 00bc044c ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc0408 bytes 5e6b0094
+ 00bc044c bytes 616b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94e751fa53ba92254c2834f881ff9a76"></a>

### [`00bc040c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc040c.md) → [`00bc0450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0450.md) FUN_00bc0450

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc04b4",
      "incomplete_value": false,
      "site": "00bc04b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0470",
      "incomplete_value": false,
      "site": "00bc0470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc04d8",
      "incomplete_value": false,
      "site": "00bc04d8",
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
            "const:245:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0494",
      "incomplete_value": false,
      "site": "00bc0494",
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
            "const:1ba:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc04b4",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc04d8",
      "DATA",
      [
        "storage",
        "002a11ba",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc04b4",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc04d8",
      "DATA",
      [
        "storage",
        "002a1245",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc040c.md#insn-00bc0440) · [`00bc0464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc040c.md#insn-00bc0464) · [`00bc048c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc040c.md#insn-00bc048c)
- 新版 `00bc0484`（命令位置の公開資料なし） · `00bc04a8`（命令位置の公開資料なし） · `00bc04d0`（命令位置の公開資料なし）

~~~diff
- 00bc0440 ["INT_ADD", "register:40f0:8", ["const:bc0440:8", "const:4:8"]]
- 00bc0440 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc0484 ["INT_ADD", "register:40f0:8", ["const:bc0484:8", "const:4:8"]]
+ 00bc0484 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc0440 bytes 50730094
+ 00bc0484 bytes 53730094
- 00bc0464 ["COPY", "tmp:0:8", ["const:758:8"]]
- 00bc0464 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0464 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0464 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc04a8 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 00bc04a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc04a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc04a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0464 bytes 08611d91
+ 00bc04a8 bytes 08a11e91
- 00bc048c ["COPY", "tmp:0:8", ["const:1ba:8"]]
- 00bc048c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc048c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc048c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc04d0 ["COPY", "tmp:0:8", ["const:245:8"]]
+ 00bc04d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc04d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc04d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc048c bytes 08e90691
+ 00bc04d0 bytes 08150991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98b26f3307f34a0cbe5bc7196088377b"></a>

### [`00bc04bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc04bc.md) → [`00bc0500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0500.md) FUN_00bc0500

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0564",
      "incomplete_value": false,
      "site": "00bc0564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0520",
      "incomplete_value": false,
      "site": "00bc0520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc0564",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc0564",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc04f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc04bc.md#insn-00bc04f0) · [`00bc0514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc04bc.md#insn-00bc0514) · [`00bc0568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc04bc.md#insn-00bc0568)
- 新版 `00bc0534`（命令位置の公開資料なし） · `00bc0558`（命令位置の公開資料なし） · `00bc05ac`（命令位置の公開資料なし）

~~~diff
- 00bc04f0 ["INT_ADD", "register:40f0:8", ["const:bc04f0:8", "const:4:8"]]
- 00bc04f0 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc0534 ["INT_ADD", "register:40f0:8", ["const:bc0534:8", "const:4:8"]]
+ 00bc0534 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc04f0 bytes 24730094
+ 00bc0534 bytes 27730094
- 00bc0514 ["COPY", "tmp:0:8", ["const:758:8"]]
- 00bc0514 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0514 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0514 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0558 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 00bc0558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0514 bytes 08611d91
+ 00bc0558 bytes 08a11e91
- 00bc0568 ["INT_ADD", "register:40f0:8", ["const:bc0568:8", "const:4:8"]]
- 00bc0568 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc05ac ["INT_ADD", "register:40f0:8", ["const:bc05ac:8", "const:4:8"]]
+ 00bc05ac ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc0568 bytes 066b0094
+ 00bc05ac bytes 096b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4636045b9f585a72663162c24c70250"></a>

### [`00bc056c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc056c.md) → [`00bc05b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc05b0.md) FUN_00bc05b0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0614",
      "incomplete_value": false,
      "site": "00bc0614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc05d0",
      "incomplete_value": false,
      "site": "00bc05d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0638",
      "incomplete_value": false,
      "site": "00bc0638",
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
            "const:187:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc05f4",
      "incomplete_value": false,
      "site": "00bc05f4",
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
            "const:fc:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc0614",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc0638",
      "DATA",
      [
        "storage",
        "002a20fc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc0614",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc0638",
      "DATA",
      [
        "storage",
        "002a2187",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc05a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc056c.md#insn-00bc05a0) · [`00bc05c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc056c.md#insn-00bc05c4) · [`00bc05ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc056c.md#insn-00bc05ec)
- 新版 `00bc05e4`（命令位置の公開資料なし） · `00bc0608`（命令位置の公開資料なし） · `00bc0630`（命令位置の公開資料なし）

~~~diff
- 00bc05a0 ["INT_ADD", "register:40f0:8", ["const:bc05a0:8", "const:4:8"]]
- 00bc05a0 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc05e4 ["INT_ADD", "register:40f0:8", ["const:bc05e4:8", "const:4:8"]]
+ 00bc05e4 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc05a0 bytes f8720094
+ 00bc05e4 bytes fb720094
- 00bc05c4 ["COPY", "tmp:0:8", ["const:758:8"]]
- 00bc05c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc05c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc05c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0608 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 00bc0608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc05c4 bytes 08611d91
+ 00bc0608 bytes 08a11e91
- 00bc05ec ["COPY", "tmp:0:8", ["const:fc:8"]]
- 00bc05ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc05ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc05ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0630 ["COPY", "tmp:0:8", ["const:187:8"]]
+ 00bc0630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc05ec bytes 08f10391
+ 00bc0630 bytes 081d0691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a86df126a9d326fe0c804a0d19a590bd"></a>

### [`00bc061c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc061c.md) → [`00bc0660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0660.md) FUN_00bc0660

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc06c4",
      "incomplete_value": false,
      "site": "00bc06c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0680",
      "incomplete_value": false,
      "site": "00bc0680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc06e8",
      "incomplete_value": false,
      "site": "00bc06e8",
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
            "const:a06:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc06a4",
      "incomplete_value": false,
      "site": "00bc06a4",
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
            "const:a93:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc06c4",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc06e8",
      "DATA",
      [
        "storage",
        "00299a93",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc06c4",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc06e8",
      "DATA",
      [
        "storage",
        "00299a06",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc061c.md#insn-00bc0650) · [`00bc0674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc061c.md#insn-00bc0674) · [`00bc069c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc061c.md#insn-00bc069c)
- 新版 `00bc0694`（命令位置の公開資料なし） · `00bc06b8`（命令位置の公開資料なし） · `00bc06e0`（命令位置の公開資料なし）

~~~diff
- 00bc0650 ["INT_ADD", "register:40f0:8", ["const:bc0650:8", "const:4:8"]]
- 00bc0650 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc0694 ["INT_ADD", "register:40f0:8", ["const:bc0694:8", "const:4:8"]]
+ 00bc0694 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc0650 bytes cc720094
+ 00bc0694 bytes cf720094
- 00bc0674 ["COPY", "tmp:0:8", ["const:758:8"]]
- 00bc0674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc06b8 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 00bc06b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc06b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc06b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0674 bytes 08611d91
+ 00bc06b8 bytes 08a11e91
- 00bc069c ["COPY", "tmp:0:8", ["const:a93:8"]]
- 00bc069c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc069c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc069c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc06e0 ["COPY", "tmp:0:8", ["const:a06:8"]]
+ 00bc06e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc06e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc06e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc069c bytes 084d2a91
+ 00bc06e0 bytes 08192891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7f5e6774c4734cb0b611ad8b58869f2"></a>

### [`00bc087c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc087c.md) → [`00bc08c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc08c0.md) FUN_00bc08c0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0924",
      "incomplete_value": false,
      "site": "00bc0924",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc08e0",
      "incomplete_value": false,
      "site": "00bc08e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0948",
      "incomplete_value": false,
      "site": "00bc0948",
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
            "const:19e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0904",
      "incomplete_value": false,
      "site": "00bc0904",
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
            "const:104:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc0924",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc0948",
      "DATA",
      [
        "storage",
        "002a9104",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc0924",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc0948",
      "DATA",
      [
        "storage",
        "002a919e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc08b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc087c.md#insn-00bc08b0) · [`00bc08d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc087c.md#insn-00bc08d4) · [`00bc08fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc087c.md#insn-00bc08fc)
- 新版 `00bc08f4`（命令位置の公開資料なし） · `00bc0918`（命令位置の公開資料なし） · `00bc0940`（命令位置の公開資料なし）

~~~diff
- 00bc08b0 ["INT_ADD", "register:40f0:8", ["const:bc08b0:8", "const:4:8"]]
- 00bc08b0 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc08f4 ["INT_ADD", "register:40f0:8", ["const:bc08f4:8", "const:4:8"]]
+ 00bc08f4 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc08b0 bytes 34720094
+ 00bc08f4 bytes 37720094
- 00bc08d4 ["COPY", "tmp:0:8", ["const:758:8"]]
- 00bc08d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc08d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc08d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0918 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 00bc0918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc08d4 bytes 08611d91
+ 00bc0918 bytes 08a11e91
- 00bc08fc ["COPY", "tmp:0:8", ["const:104:8"]]
- 00bc08fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc08fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc08fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0940 ["COPY", "tmp:0:8", ["const:19e:8"]]
+ 00bc0940 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0940 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0940 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc08fc bytes 08110491
+ 00bc0940 bytes 08790691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21b27ffade41a448cc59d6dce67ec310"></a>

### [`00bc092c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc092c.md) → [`00bc0970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0970.md) FUN_00bc0970

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc09d8",
      "incomplete_value": false,
      "site": "00bc09d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0994",
      "incomplete_value": false,
      "site": "00bc0994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
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
      "00bc09d8",
      "DATA",
      [
        "storage",
        "00c177d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc09d8",
      "DATA",
      [
        "storage",
        "00c17828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc092c.md#insn-00bc0964) · [`00bc0988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc092c.md#insn-00bc0988) · [`00bc09d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc092c.md#insn-00bc09d0)
- 新版 `00bc09a8`（命令位置の公開資料なし） · `00bc09cc`（命令位置の公開資料なし） · `00bc0a14`（命令位置の公開資料なし）

~~~diff
- 00bc0964 ["INT_ADD", "register:40f0:8", ["const:bc0964:8", "const:4:8"]]
- 00bc0964 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc09a8 ["INT_ADD", "register:40f0:8", ["const:bc09a8:8", "const:4:8"]]
+ 00bc09a8 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc0964 bytes 07720094
+ 00bc09a8 bytes 0a720094
- 00bc0988 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 00bc0988 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0988 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0988 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc09cc ["COPY", "tmp:0:8", ["const:828:8"]]
+ 00bc09cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc09cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc09cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0988 bytes 08611f91
+ 00bc09cc bytes 08a12091
- 00bc09d0 ["INT_ADD", "register:40f0:8", ["const:bc09d0:8", "const:4:8"]]
- 00bc09d0 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc0a14 ["INT_ADD", "register:40f0:8", ["const:bc0a14:8", "const:4:8"]]
+ 00bc0a14 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc09d0 bytes ec690094
+ 00bc0a14 bytes ef690094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85ac912d3bc23a9c5ad89943bf31c7d6"></a>

### [`00bc09d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc09d4.md) → [`00bc0a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0a18.md) FUN_00bc0a18

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0a7c",
      "incomplete_value": false,
      "site": "00bc0a7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0a38",
      "incomplete_value": false,
      "site": "00bc0a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0aa0",
      "incomplete_value": false,
      "site": "00bc0aa0",
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
            "const:2fe:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0a5c",
      "incomplete_value": false,
      "site": "00bc0a5c",
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
            "const:273:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc0a7c",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc0aa0",
      "DATA",
      [
        "storage",
        "002a0273",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc0a7c",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc0aa0",
      "DATA",
      [
        "storage",
        "002a02fe",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc09d4.md#insn-00bc0a08) · [`00bc0a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc09d4.md#insn-00bc0a2c) · [`00bc0a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc09d4.md#insn-00bc0a54)
- 新版 `00bc0a4c`（命令位置の公開資料なし） · `00bc0a70`（命令位置の公開資料なし） · `00bc0a98`（命令位置の公開資料なし）

~~~diff
- 00bc0a08 ["INT_ADD", "register:40f0:8", ["const:bc0a08:8", "const:4:8"]]
- 00bc0a08 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc0a4c ["INT_ADD", "register:40f0:8", ["const:bc0a4c:8", "const:4:8"]]
+ 00bc0a4c ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc0a08 bytes de710094
+ 00bc0a4c bytes e1710094
- 00bc0a2c ["COPY", "tmp:0:8", ["const:758:8"]]
- 00bc0a2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0a2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0a2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0a70 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 00bc0a70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0a70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0a70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0a2c bytes 08611d91
+ 00bc0a70 bytes 08a11e91
- 00bc0a54 ["COPY", "tmp:0:8", ["const:273:8"]]
- 00bc0a54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0a54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0a54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0a98 ["COPY", "tmp:0:8", ["const:2fe:8"]]
+ 00bc0a98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0a98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0a98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0a54 bytes 08cd0991
+ 00bc0a98 bytes 08f90b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-642c7931587a9e1b38e584634c057d6e"></a>

### [`00bc0a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0a84.md) → [`00bc0ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0ac8.md) FUN_00bc0ac8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0b2c",
      "incomplete_value": false,
      "site": "00bc0b2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0ae8",
      "incomplete_value": false,
      "site": "00bc0ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0b50",
      "incomplete_value": false,
      "site": "00bc0b50",
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
            "const:7b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0b0c",
      "incomplete_value": false,
      "site": "00bc0b0c",
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
            "const:844:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc0b2c",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc0b50",
      "DATA",
      [
        "storage",
        "002af844",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc0b2c",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc0b50",
      "DATA",
      [
        "storage",
        "002af7b0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0a84.md#insn-00bc0ab8) · [`00bc0adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0a84.md#insn-00bc0adc) · [`00bc0b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0a84.md#insn-00bc0b04)
- 新版 `00bc0afc`（命令位置の公開資料なし） · `00bc0b20`（命令位置の公開資料なし） · `00bc0b48`（命令位置の公開資料なし）

~~~diff
- 00bc0ab8 ["INT_ADD", "register:40f0:8", ["const:bc0ab8:8", "const:4:8"]]
- 00bc0ab8 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc0afc ["INT_ADD", "register:40f0:8", ["const:bc0afc:8", "const:4:8"]]
+ 00bc0afc ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc0ab8 bytes b2710094
+ 00bc0afc bytes b5710094
- 00bc0adc ["COPY", "tmp:0:8", ["const:758:8"]]
- 00bc0adc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0adc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0adc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0b20 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 00bc0b20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0b20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0b20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0adc bytes 08611d91
+ 00bc0b20 bytes 08a11e91
- 00bc0b04 ["COPY", "tmp:0:8", ["const:844:8"]]
- 00bc0b04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0b04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0b04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0b48 ["COPY", "tmp:0:8", ["const:7b0:8"]]
+ 00bc0b48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0b48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0b48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0b04 bytes 08112191
+ 00bc0b48 bytes 08c11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80d60ac8c1dff9f8bd9870d6ea92f44a"></a>

### [`00bc0b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0b34.md) → [`00bc0b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0b78.md) FUN_00bc0b78

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0bdc",
      "incomplete_value": false,
      "site": "00bc0bdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0b98",
      "incomplete_value": false,
      "site": "00bc0b98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc0bdc",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc0c00",
      "DATA",
      [
        "storage",
        "00298b9d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc0bdc",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc0c00",
      "DATA",
      [
        "storage",
        "00298b10",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0b34.md#insn-00bc0bdc) · [`00bc0b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0b34.md#insn-00bc0b68) · [`00bc0b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0b34.md#insn-00bc0b8c)
- 新版 `00bc0c20`（命令位置の公開資料なし） · `00bc0bac`（命令位置の公開資料なし） · `00bc0bd0`（命令位置の公開資料なし）

~~~diff
- 00bc0bdc ["INT_ADD", "register:40f0:8", ["const:bc0bdc:8", "const:4:8"]]
- 00bc0bdc ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc0c20 ["INT_ADD", "register:40f0:8", ["const:bc0c20:8", "const:4:8"]]
+ 00bc0c20 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc0bdc bytes 69690094
+ 00bc0c20 bytes 6c690094
- 00bc0b68 ["INT_ADD", "register:40f0:8", ["const:bc0b68:8", "const:4:8"]]
- 00bc0b68 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc0bac ["INT_ADD", "register:40f0:8", ["const:bc0bac:8", "const:4:8"]]
+ 00bc0bac ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc0b68 bytes 86710094
+ 00bc0bac bytes 89710094
- 00bc0b8c ["COPY", "tmp:0:8", ["const:758:8"]]
- 00bc0b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0bd0 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 00bc0bd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0bd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0bd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0b8c bytes 08611d91
+ 00bc0bd0 bytes 08a11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db253481a86338d07e22f07d4b5d469f"></a>

### [`00bc0be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0be0.md) → [`00bc0c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0c24.md) FUN_00bc0c24

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0c88",
      "incomplete_value": false,
      "site": "00bc0c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0c44",
      "incomplete_value": false,
      "site": "00bc0c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc0c88",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc0c88",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0be0.md#insn-00bc0c14) · [`00bc0c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0be0.md#insn-00bc0c38) · [`00bc0c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0be0.md#insn-00bc0c8c)
- 新版 `00bc0c58`（命令位置の公開資料なし） · `00bc0c7c`（命令位置の公開資料なし） · `00bc0cd0`（命令位置の公開資料なし）

~~~diff
- 00bc0c14 ["INT_ADD", "register:40f0:8", ["const:bc0c14:8", "const:4:8"]]
- 00bc0c14 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc0c58 ["INT_ADD", "register:40f0:8", ["const:bc0c58:8", "const:4:8"]]
+ 00bc0c58 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc0c14 bytes 5b710094
+ 00bc0c58 bytes 5e710094
- 00bc0c38 ["COPY", "tmp:0:8", ["const:758:8"]]
- 00bc0c38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0c38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0c38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0c7c ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 00bc0c7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0c7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0c7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0c38 bytes 08611d91
+ 00bc0c7c bytes 08a11e91
- 00bc0c8c ["INT_ADD", "register:40f0:8", ["const:bc0c8c:8", "const:4:8"]]
- 00bc0c8c ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc0cd0 ["INT_ADD", "register:40f0:8", ["const:bc0cd0:8", "const:4:8"]]
+ 00bc0cd0 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc0c8c bytes 3d690094
+ 00bc0cd0 bytes 40690094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-481b3239dd20c0d5758c10ec64984d49"></a>

### [`00bc10fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc10fc.md) → [`00bc1140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1140.md) FUN_00bc1140

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 7件 [`00bc0c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0c90.md) [`00bc245c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc245c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bc55d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc55d8.md) [`00bc67b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc67b8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 7件 [`00bc0cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0cd4.md) [`00bc24a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bc561c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc561c.md) [`00bc67fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc67fc.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.26% / 新版 96.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc1260",
      "incomplete_value": false,
      "site": "00bc1260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc121c",
      "incomplete_value": false,
      "site": "00bc121c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "00bc1260",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc126c",
      "DATA",
      [
        "storage",
        "0029f286",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc1260",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc126c",
      "DATA",
      [
        "storage",
        "0029f311",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc11ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc10fc.md#insn-00bc11ec) · [`00bc1210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc10fc.md#insn-00bc1210) · [`00bc1274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc10fc.md#insn-00bc1274)
- 新版 `00bc1230`（命令位置の公開資料なし） · `00bc1254`（命令位置の公開資料なし） · `00bc12b8`（命令位置の公開資料なし）

~~~diff
- 00bc11ec ["INT_ADD", "register:40f0:8", ["const:bc11ec:8", "const:4:8"]]
- 00bc11ec ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc1230 ["INT_ADD", "register:40f0:8", ["const:bc1230:8", "const:4:8"]]
+ 00bc1230 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc11ec bytes e56f0094
+ 00bc1230 bytes e86f0094
- 00bc1210 ["COPY", "tmp:0:8", ["const:848:8"]]
- 00bc1210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc1254 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00bc1254 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1254 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1254 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc1210 bytes 08212191
+ 00bc1254 bytes 08612291
- 00bc1274 ["INT_ADD", "register:40f0:8", ["const:bc1274:8", "const:4:8"]]
- 00bc1274 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc12b8 ["INT_ADD", "register:40f0:8", ["const:bc12b8:8", "const:4:8"]]
+ 00bc12b8 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc1274 bytes c36f0094
+ 00bc12b8 bytes c66f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f14d6172db6fc8eadaf810e00e126d0"></a>

### [`00bc1328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1328.md) → [`00bc136c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc136c.md) FUN_00bc136c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc13d0",
      "incomplete_value": false,
      "site": "00bc13d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc138c",
      "incomplete_value": false,
      "site": "00bc138c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc13d0",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc13d0",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc135c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1328.md#insn-00bc135c) · [`00bc1380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1328.md#insn-00bc1380) · [`00bc13c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1328.md#insn-00bc13c4)
- 新版 `00bc13a0`（命令位置の公開資料なし） · `00bc13c4`（命令位置の公開資料なし） · `00bc1408`（命令位置の公開資料なし）

~~~diff
- 00bc135c ["INT_ADD", "register:40f0:8", ["const:bc135c:8", "const:4:8"]]
- 00bc135c ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc13a0 ["INT_ADD", "register:40f0:8", ["const:bc13a0:8", "const:4:8"]]
+ 00bc13a0 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc135c bytes 896f0094
+ 00bc13a0 bytes 8c6f0094
- 00bc1380 ["COPY", "tmp:0:8", ["const:848:8"]]
- 00bc1380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc13c4 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00bc13c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc13c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc13c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc1380 bytes 08212191
+ 00bc13c4 bytes 08612291
- 00bc13c4 ["INT_ADD", "register:40f0:8", ["const:bc13c4:8", "const:4:8"]]
- 00bc13c4 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc1408 ["INT_ADD", "register:40f0:8", ["const:bc1408:8", "const:4:8"]]
+ 00bc1408 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc13c4 bytes 6f670094
+ 00bc1408 bytes 72670094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3017175d7086762f5ac70d729772e731"></a>

### [`00bc15a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc15a0.md) → [`00bc15e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc15e4.md) FUN_00bc15e4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) · 呼出先 4件 [`00bc2180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2180.md) [`00bc245c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc245c.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 2件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) · 呼出先 4件 [`00bc21c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc21c4.md) [`00bc24a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc16cc",
      "incomplete_value": false,
      "site": "00bc16cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1688",
      "incomplete_value": false,
      "site": "00bc1688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc16e8",
      "incomplete_value": false,
      "site": "00bc16f4",
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
            "const:a2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc16a4",
      "incomplete_value": false,
      "site": "00bc16b0",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc16cc",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc16f4",
      "DATA",
      [
        "storage",
        "002a8008",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc16cc",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc16f4",
      "DATA",
      [
        "storage",
        "002a80a2",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc15f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc15a0.md#insn-00bc15f8) · [`00bc1648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc15a0.md#insn-00bc1648) · [`00bc167c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc15a0.md#insn-00bc167c)
- 新版 `00bc163c`（命令位置の公開資料なし） · `00bc168c`（命令位置の公開資料なし） · `00bc16c0`（命令位置の公開資料なし）

~~~diff
- 00bc15f8 ["INT_ADD", "register:40f0:8", ["const:bc15f8:8", "const:4:8"]]
- 00bc15f8 ["CALL", null, ["callee:00bc21c4:8"]]
+ 00bc163c ["INT_ADD", "register:40f0:8", ["const:bc163c:8", "const:4:8"]]
+ 00bc163c ["CALL", null, ["callee:00bc21c4:8"]]
- 00bc15f8 bytes e2020094
+ 00bc163c bytes e2020094
- 00bc1648 ["INT_ADD", "register:40f0:8", ["const:bc1648:8", "const:4:8"]]
- 00bc1648 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc168c ["INT_ADD", "register:40f0:8", ["const:bc168c:8", "const:4:8"]]
+ 00bc168c ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc1648 bytes ce6e0094
+ 00bc168c bytes d16e0094
- 00bc167c ["COPY", "tmp:0:8", ["const:848:8"]]
- 00bc167c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bc167c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bc167c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bc16c0 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00bc16c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc16c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc16c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bc167c bytes 29212191
+ 00bc16c0 bytes 29612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2d78ba14a843c6a7ffb3e0121f83838"></a>

### [`00bc1710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1710.md) → [`00bc1754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1754.md) FUN_00bc1754

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 5件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bc67b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc67b8.md) [`00bce8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce8f8.md) [`00bd1734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1734.md) · 呼出先 8件 [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bbff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md)
- 新版 呼出元 5件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bc67fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc67fc.md) [`00bce93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce93c.md) [`00bd1778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1778.md) · 呼出先 8件 [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) [`00bbff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc1968",
      "incomplete_value": false,
      "site": "00bc1968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1924",
      "incomplete_value": false,
      "site": "00bc1924",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc1bd4",
      "incomplete_value": false,
      "site": "00bc1bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1b90",
      "incomplete_value": false,
      "site": "00bc1b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "ordinal": 59,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc1968",
      "DATA",
      [
        "storage",
        "00c19668",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc1bd4",
      "DATA",
      [
        "storage",
        "00c196d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc1968",
      "DATA",
      [
        "storage",
        "00c196b8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc1bd4",
      "DATA",
      [
        "storage",
        "00c19728",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1710.md#insn-00bc1bd4) · [`00bc1784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1710.md#insn-00bc1784) · [`00bc1790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1710.md#insn-00bc1790)
- 新版 `00bc1c18`（命令位置の公開資料なし） · `00bc17c8`（命令位置の公開資料なし） · `00bc17d4`（命令位置の公開資料なし）

~~~diff
- 00bc1bd4 ["INT_ADD", "register:40f0:8", ["const:bc1bd4:8", "const:4:8"]]
- 00bc1bd4 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bc1c18 ["INT_ADD", "register:40f0:8", ["const:bc1c18:8", "const:4:8"]]
+ 00bc1c18 ["CALL", null, ["callee:00bde2c0:8"]]
- 00bc1bd4 bytes a7710094
+ 00bc1c18 bytes aa710094
- 00bc1784 ["INT_ADD", "register:40f0:8", ["const:bc1784:8", "const:4:8"]]
- 00bc1784 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc17c8 ["INT_ADD", "register:40f0:8", ["const:bc17c8:8", "const:4:8"]]
+ 00bc17c8 ["CALL", null, ["callee:00bdd250:8"]]
- 00bc1784 bytes 9f6e0094
+ 00bc17c8 bytes a26e0094
- 00bc1790 ["INT_ADD", "register:40f0:8", ["const:bc1790:8", "const:4:8"]]
- 00bc1790 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bc17d4 ["INT_ADD", "register:40f0:8", ["const:bc17d4:8", "const:4:8"]]
+ 00bc17d4 ["CALL", null, ["callee:00bde2c0:8"]]
- 00bc1790 bytes b8720094
+ 00bc17d4 bytes bb720094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5669ae224b619b5b2f2723148de983a5"></a>

### [`00bc1be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1be0.md) → [`00bc1c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1c24.md) FUN_00bc1c24

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bc67b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc67b8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 2件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bc67fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc67fc.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc1c8c",
      "incomplete_value": false,
      "site": "00bc1c8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1c48",
      "incomplete_value": false,
      "site": "00bc1c48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:748:8"
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
      "00bc1c8c",
      "DATA",
      [
        "storage",
        "00c19748",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc1c8c",
      "DATA",
      [
        "storage",
        "00c19798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1be0.md#insn-00bc1c18) · [`00bc1c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1be0.md#insn-00bc1c3c) · [`00bc1c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1be0.md#insn-00bc1c84)
- 新版 `00bc1c5c`（命令位置の公開資料なし） · `00bc1c80`（命令位置の公開資料なし） · `00bc1cc8`（命令位置の公開資料なし）

~~~diff
- 00bc1c18 ["INT_ADD", "register:40f0:8", ["const:bc1c18:8", "const:4:8"]]
- 00bc1c18 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc1c5c ["INT_ADD", "register:40f0:8", ["const:bc1c5c:8", "const:4:8"]]
+ 00bc1c5c ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc1c18 bytes 5a6d0094
+ 00bc1c5c bytes 5d6d0094
- 00bc1c3c ["COPY", "tmp:0:8", ["const:748:8"]]
- 00bc1c3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1c3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1c3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc1c80 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 00bc1c80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1c80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1c80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc1c3c bytes 08211d91
+ 00bc1c80 bytes 08611e91
- 00bc1c84 ["INT_ADD", "register:40f0:8", ["const:bc1c84:8", "const:4:8"]]
- 00bc1c84 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc1cc8 ["INT_ADD", "register:40f0:8", ["const:bc1cc8:8", "const:4:8"]]
+ 00bc1cc8 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc1c84 bytes 3f650094
+ 00bc1cc8 bytes 42650094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dfe747c4e38eada18f1082acdaf4641"></a>

### [`00bc1c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1c88.md) → [`00bc1ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1ccc.md) FUN_00bc1ccc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 4件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bce774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce774.md) · 呼出先 7件 [`00bc2abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2abc.md) [`00bc2b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2b94.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 4件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bce7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce7b8.md) · 呼出先 7件 [`00bc2b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2b00.md) [`00bc2bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2bd8.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.93% / 新版 97.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc1e20",
      "incomplete_value": false,
      "site": "00bc1e20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1ddc",
      "incomplete_value": false,
      "site": "00bc1ddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc1f38",
      "incomplete_value": false,
      "site": "00bc1f38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1ef4",
      "incomplete_value": false,
      "site": "00bc1ef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc1e20",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc1f38",
      "DATA",
      [
        "storage",
        "00c17928",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc2018",
      "PARAM",
      [
        "storage",
        "00292649",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc1e20",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc1f38",
      "DATA",
      [
        "storage",
        "00c17978",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc2018",
      "PARAM",
      [
        "storage",
        "002925bc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1dac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1c88.md#insn-00bc1dac) · [`00bc1dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1c88.md#insn-00bc1dd0) · [`00bc1ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1c88.md#insn-00bc1ebc)
- 新版 `00bc1df0`（命令位置の公開資料なし） · `00bc1e14`（命令位置の公開資料なし） · `00bc1f00`（命令位置の公開資料なし）

~~~diff
- 00bc1dac ["INT_ADD", "register:40f0:8", ["const:bc1dac:8", "const:4:8"]]
- 00bc1dac ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc1df0 ["INT_ADD", "register:40f0:8", ["const:bc1df0:8", "const:4:8"]]
+ 00bc1df0 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc1dac bytes f56c0094
+ 00bc1df0 bytes f86c0094
- 00bc1dd0 ["COPY", "tmp:0:8", ["const:848:8"]]
- 00bc1dd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1dd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1dd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc1e14 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00bc1e14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1e14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1e14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc1dd0 bytes 08212191
+ 00bc1e14 bytes 08612291
- 00bc1ebc ["INT_ADD", "register:40f0:8", ["const:bc1ebc:8", "const:4:8"]]
- 00bc1ebc ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc1f00 ["INT_ADD", "register:40f0:8", ["const:bc1f00:8", "const:4:8"]]
+ 00bc1f00 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc1ebc bytes b16c0094
+ 00bc1f00 bytes b46c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45ff43252b1c18ab58df51e67367fc58"></a>

### [`00bc204c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc204c.md) → [`00bc2090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2090.md) FUN_00bc2090

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bce774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce774.md) · 呼出先 3件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 3件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bce7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce7b8.md) · 呼出先 3件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc216c",
      "incomplete_value": false,
      "site": "00bc216c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2128",
      "incomplete_value": false,
      "site": "00bc2128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc218c",
      "incomplete_value": false,
      "site": "00bc218c",
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
            "const:1c7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2148",
      "incomplete_value": false,
      "site": "00bc2148",
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
            "const:13c:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc216c",
      "DATA",
      [
        "storage",
        "00c18248",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc218c",
      "DATA",
      [
        "storage",
        "0029e13c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc216c",
      "DATA",
      [
        "storage",
        "00c18298",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc218c",
      "DATA",
      [
        "storage",
        "0029e1c7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc20ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc204c.md#insn-00bc20ac) · [`00bc20f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc204c.md#insn-00bc20f4) · [`00bc211c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc204c.md#insn-00bc211c)
- 新版 `00bc20f0`（命令位置の公開資料なし） · `00bc2138`（命令位置の公開資料なし） · `00bc2160`（命令位置の公開資料なし）

~~~diff
- 00bc20ac ["INT_ADD", "register:40f0:8", ["const:bc20ac:8", "const:4:8"]]
- 00bc20ac ["CALL", null, ["callee:00bc2f0c:8"]]
+ 00bc20f0 ["INT_ADD", "register:40f0:8", ["const:bc20f0:8", "const:4:8"]]
+ 00bc20f0 ["CALL", null, ["callee:00bc2f0c:8"]]
- 00bc20ac bytes 87030094
+ 00bc20f0 bytes 87030094
- 00bc20f4 ["INT_ADD", "register:40f0:8", ["const:bc20f4:8", "const:4:8"]]
- 00bc20f4 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc2138 ["INT_ADD", "register:40f0:8", ["const:bc2138:8", "const:4:8"]]
+ 00bc2138 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc20f4 bytes 236c0094
+ 00bc2138 bytes 266c0094
- 00bc211c ["COPY", "tmp:0:8", ["const:248:8"]]
- 00bc211c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bc211c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bc211c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bc2160 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00bc2160 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00bc2160 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00bc2160 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bc211c bytes 4a210991
+ 00bc2160 bytes 4a610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de3c828b483b31ba991d3bac6ce8a68c"></a>

### [`00bc2180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2180.md) → [`00bc21c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc21c4.md) FUN_00bc21c4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bc15a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc15a0.md) [`00bce774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce774.md) · 呼出先 6件 [`00bcf374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf374.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md)
- 新版 呼出元 3件 [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bc15e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc15e4.md) [`00bce7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce7b8.md) · 呼出先 6件 [`00bcf3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf3b8.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc23e8",
      "incomplete_value": false,
      "site": "00bc23ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc23a4",
      "incomplete_value": false,
      "site": "00bc23a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc23ec",
      "DATA",
      [
        "storage",
        "00c19278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc23ec",
      "DATA",
      [
        "storage",
        "00c192c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc234c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2180.md#insn-00bc234c) · [`00bc23a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2180.md#insn-00bc23a4) · [`00bc23ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2180.md#insn-00bc23ac)
- 新版 `00bc2390`（命令位置の公開資料なし） · `00bc23e8`（命令位置の公開資料なし） · `00bc23f0`（命令位置の公開資料なし）

~~~diff
- 00bc234c ["INT_ADD", "register:40f0:8", ["const:bc234c:8", "const:4:8"]]
- 00bc234c ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc2390 ["INT_ADD", "register:40f0:8", ["const:bc2390:8", "const:4:8"]]
+ 00bc2390 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc234c bytes 8d6b0094
+ 00bc2390 bytes 906b0094
- 00bc23a4 ["COPY", "tmp:0:8", ["const:278:8"]]
- 00bc23a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc23a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc23a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc23e8 ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 00bc23e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc23e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc23e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc23a4 bytes 08e10991
+ 00bc23e8 bytes 08210b91
- 00bc23ac ["INT_ADD", "register:40f0:8", ["const:bc23ac:8", "const:4:8"]]
- 00bc23ac ["CALL", null, ["callee:00bcf3b8:8"]]
+ 00bc23f0 ["INT_ADD", "register:40f0:8", ["const:bc23f0:8", "const:4:8"]]
+ 00bc23f0 ["CALL", null, ["callee:00bcf3b8:8"]]
- 00bc23ac bytes f2330094
+ 00bc23f0 bytes f2330094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03d267ca23a1671e99cc9960b0bbc9f6"></a>

### [`00bc245c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc245c.md) → [`00bc24a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md) FUN_00bc24a0

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bc15a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc15a0.md) · 呼出先 13件 [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bbff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md) [`00bc0c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0c90.md) [`00bc10fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc10fc.md) [`00bc966c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc966c.md)
- 新版 呼出元 2件 [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bc15e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc15e4.md) · 呼出先 13件 [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bbff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md) [`00bc0cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0cd4.md) [`00bc1140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1140.md) [`00bc96b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc96b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc2620",
      "incomplete_value": false,
      "site": "00bc262c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc25dc",
      "incomplete_value": false,
      "site": "00bc25e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc26e8",
      "incomplete_value": false,
      "site": "00bc26e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc26a4",
      "incomplete_value": false,
      "site": "00bc26a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc2950",
      "incomplete_value": false,
      "site": "00bc2950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc290c",
      "incomplete_value": false,
      "site": "00bc290c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "ordinal": 58,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc262c",
      "DATA",
      [
        "storage",
        "00c19300",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc26e8",
      "DATA",
      [
        "storage",
        "00c194a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc27d8",
      "DATA",
      [
        "storage",
        "00c19588",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc262c",
      "DATA",
      [
        "storage",
        "00c19350",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc26e8",
      "DATA",
      [
        "storage",
        "00c194f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc27d8",
      "DATA",
      [
        "storage",
        "00c195d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc245c.md#insn-00bc2490) · [`00bc2514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc245c.md#insn-00bc2514) · [`00bc2534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc245c.md#insn-00bc2534)
- 新版 `00bc24d4`（命令位置の公開資料なし） · `00bc2558`（命令位置の公開資料なし） · `00bc2578`（命令位置の公開資料なし）

~~~diff
- 00bc2490 ["INT_ADD", "register:40f0:8", ["const:bc2490:8", "const:4:8"]]
- 00bc2490 ["CALL", null, ["callee:00bc0cd4:8"]]
+ 00bc24d4 ["INT_ADD", "register:40f0:8", ["const:bc24d4:8", "const:4:8"]]
+ 00bc24d4 ["CALL", null, ["callee:00bc0cd4:8"]]
- 00bc2490 bytes 00faff97
+ 00bc24d4 bytes 00faff97
- 00bc2514 ["INT_ADD", "register:40f0:8", ["const:bc2514:8", "const:4:8"]]
- 00bc2514 ["CALL", null, ["callee:00bc1140:8"]]
+ 00bc2558 ["INT_ADD", "register:40f0:8", ["const:bc2558:8", "const:4:8"]]
+ 00bc2558 ["CALL", null, ["callee:00bc1140:8"]]
- 00bc2514 bytes fafaff97
+ 00bc2558 bytes fafaff97
- 00bc2534 ["INT_ADD", "register:40f0:8", ["const:bc2534:8", "const:4:8"]]
- 00bc2534 ["CALL", null, ["callee:00bc96b0:8"]]
+ 00bc2578 ["INT_ADD", "register:40f0:8", ["const:bc2578:8", "const:4:8"]]
+ 00bc2578 ["CALL", null, ["callee:00bc96b0:8"]]
- 00bc2534 bytes 4e1c0094
+ 00bc2578 bytes 4e1c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a985361c1acd39978f051aa21689b67"></a>

### [`00bc2a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2a1c.md) → [`00bc2a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2a60.md) FUN_00bc2a60

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc2ac4",
      "incomplete_value": false,
      "site": "00bc2ac4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2a80",
      "incomplete_value": false,
      "site": "00bc2a80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc2ac4",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc2ac4",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2a1c.md#insn-00bc2a50) · [`00bc2a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2a1c.md#insn-00bc2a74) · [`00bc2ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2a1c.md#insn-00bc2ab8)
- 新版 `00bc2a94`（命令位置の公開資料なし） · `00bc2ab8`（命令位置の公開資料なし） · `00bc2afc`（命令位置の公開資料なし）

~~~diff
- 00bc2a50 ["INT_ADD", "register:40f0:8", ["const:bc2a50:8", "const:4:8"]]
- 00bc2a50 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc2a94 ["INT_ADD", "register:40f0:8", ["const:bc2a94:8", "const:4:8"]]
+ 00bc2a94 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc2a50 bytes cc690094
+ 00bc2a94 bytes cf690094
- 00bc2a74 ["COPY", "tmp:0:8", ["const:848:8"]]
- 00bc2a74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2a74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2a74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc2ab8 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00bc2ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc2ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc2ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc2a74 bytes 08212191
+ 00bc2ab8 bytes 08612291
- 00bc2ab8 ["INT_ADD", "register:40f0:8", ["const:bc2ab8:8", "const:4:8"]]
- 00bc2ab8 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc2afc ["INT_ADD", "register:40f0:8", ["const:bc2afc:8", "const:4:8"]]
+ 00bc2afc ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc2ab8 bytes b2610094
+ 00bc2afc bytes b5610094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30ba1c41432e569153ae8dfc0edd0688"></a>

### [`00bc2b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2b94.md) → [`00bc2bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2bd8.md) FUN_00bc2bd8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bc1c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1c88.md) · 呼出先 3件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 2件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bc1ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1ccc.md) · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc2c44",
      "incomplete_value": false,
      "site": "00bc2c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2c00",
      "incomplete_value": false,
      "site": "00bc2c00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc2c44",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc2c44",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2b94.md#insn-00bc2bc8) · [`00bc2bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2b94.md#insn-00bc2bf0) · [`00bc2bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2b94.md#insn-00bc2bf8)
- 新版 `00bc2c0c`（命令位置の公開資料なし） · `00bc2c34`（命令位置の公開資料なし） · `00bc2c3c`（命令位置の公開資料なし）

~~~diff
- 00bc2bc8 ["INT_ADD", "register:40f0:8", ["const:bc2bc8:8", "const:4:8"]]
- 00bc2bc8 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc2c0c ["INT_ADD", "register:40f0:8", ["const:bc2c0c:8", "const:4:8"]]
+ 00bc2c0c ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc2bc8 bytes 6e690094
+ 00bc2c0c bytes 71690094
- 00bc2bf0 ["INT_ADD", "register:40f0:8", ["const:bc2bf0:8", "const:4:8"]]
- 00bc2bf0 ["CALL", null, ["callee:00bdb190:8"]]
+ 00bc2c34 ["INT_ADD", "register:40f0:8", ["const:bc2c34:8", "const:4:8"]]
+ 00bc2c34 ["CALL", null, ["callee:00bdb190:8"]]
- 00bc2bf0 bytes 54610094
+ 00bc2c34 bytes 57610094
- 00bc2bf8 ["COPY", "tmp:0:8", ["const:848:8"]]
- 00bc2bf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bc2bf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bc2bf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bc2c3c ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00bc2c3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc2c3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc2c3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bc2bf8 bytes 29212191
+ 00bc2c3c bytes 29612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f4f976a49a975c0d0ddad41202f866b"></a>

### [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) → [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) FUN_00bc2f0c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 14件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bc1710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1710.md) [`00bc204c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc204c.md) · 呼出先 42件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bbd264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd264.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bbfdb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfdb4.md)
- 新版 呼出元 14件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) [`00bc1754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1754.md) [`00bc2090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2090.md) · 呼出先 42件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bbd2a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd2a8.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) [`00bbfdf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfdf8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.80% / 新版 98.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc325c",
      "incomplete_value": false,
      "site": "00bc325c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3218",
      "incomplete_value": false,
      "site": "00bc3218",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc36a0",
      "incomplete_value": false,
      "site": "00bc36a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc365c",
      "incomplete_value": false,
      "site": "00bc365c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 63,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc3ae0",
      "incomplete_value": false,
      "site": "00bc3ae0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3a9c",
      "incomplete_value": false,
      "site": "00bc3a9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "ordinal": 105,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc2fe0",
      "READ",
      [
        "storage",
        "00c17b68",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2ff0",
      "READ",
      [
        "storage",
        "00c17b69",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc301c",
      "READ",
      [
        "storage",
        "00c17b78",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc2fe0",
      "READ",
      [
        "storage",
        "00c17bb8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2ff0",
      "READ",
      [
        "storage",
        "00c17bb9",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc301c",
      "READ",
      [
        "storage",
        "00c17bc8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md#insn-00bc3380) · [`00bc33e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md#insn-00bc33e0) · [`00bc3984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md#insn-00bc3984)
- 新版 `00bc33c4`（命令位置の公開資料なし） · `00bc3424`（命令位置の公開資料なし） · `00bc39c8`（命令位置の公開資料なし）

~~~diff
- 00bc3380 ["INT_ADD", "register:40f0:8", ["const:bc3380:8", "const:4:8"]]
- 00bc3380 ["CALL", null, ["callee:00bbd2a8:8"]]
+ 00bc33c4 ["INT_ADD", "register:40f0:8", ["const:bc33c4:8", "const:4:8"]]
+ 00bc33c4 ["CALL", null, ["callee:00bbd2a8:8"]]
- 00bc3380 bytes b9e7ff97
+ 00bc33c4 bytes b9e7ff97
- 00bc33e0 ["INT_ADD", "register:40f0:8", ["const:bc33e0:8", "const:4:8"]]
- 00bc33e0 ["CALL", null, ["callee:00bbd2a8:8"]]
+ 00bc3424 ["INT_ADD", "register:40f0:8", ["const:bc3424:8", "const:4:8"]]
+ 00bc3424 ["CALL", null, ["callee:00bbd2a8:8"]]
- 00bc33e0 bytes a1e7ff97
+ 00bc3424 bytes a1e7ff97
- 00bc3984 ["INT_ADD", "register:40f0:8", ["const:bc3984:8", "const:4:8"]]
- 00bc3984 ["CALL", null, ["callee:00bbd2a8:8"]]
+ 00bc39c8 ["INT_ADD", "register:40f0:8", ["const:bc39c8:8", "const:4:8"]]
+ 00bc39c8 ["CALL", null, ["callee:00bbd2a8:8"]]
- 00bc3984 bytes 38e6ff97
+ 00bc39c8 bytes 38e6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cc08bdd24096ddfc252e6b5ae375c25"></a>

### [`00bc4318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc4318.md) → [`00bc435c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc435c.md) FUN_00bc435c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc43cc",
      "incomplete_value": false,
      "site": "00bc43cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc4388",
      "incomplete_value": false,
      "site": "00bc4388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc43cc",
      "DATA",
      [
        "storage",
        "00c17ec8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc43cc",
      "DATA",
      [
        "storage",
        "00c17f18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc4318.md#insn-00bc4358) · [`00bc437c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc4318.md#insn-00bc437c) · [`00bc43d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc4318.md#insn-00bc43d0)
- 新版 `00bc439c`（命令位置の公開資料なし） · `00bc43c0`（命令位置の公開資料なし） · `00bc4414`（命令位置の公開資料なし）

~~~diff
- 00bc4358 ["INT_ADD", "register:40f0:8", ["const:bc4358:8", "const:4:8"]]
- 00bc4358 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc439c ["INT_ADD", "register:40f0:8", ["const:bc439c:8", "const:4:8"]]
+ 00bc439c ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc4358 bytes 8a630094
+ 00bc439c bytes 8d630094
- 00bc437c ["COPY", "tmp:0:8", ["const:ec8:8"]]
- 00bc437c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc437c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc437c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc43c0 ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 00bc43c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc43c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc43c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc437c bytes 08213b91
+ 00bc43c0 bytes 08613c91
- 00bc43d0 ["INT_ADD", "register:40f0:8", ["const:bc43d0:8", "const:4:8"]]
- 00bc43d0 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc4414 ["INT_ADD", "register:40f0:8", ["const:bc4414:8", "const:4:8"]]
+ 00bc4414 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc43d0 bytes 6c5b0094
+ 00bc4414 bytes 6f5b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc0a7031b5e51cf47a65cf4b9cf542ac"></a>

### [`00bc43d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc43d4.md) → [`00bc4418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc4418.md) FUN_00bc4418

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc448c",
      "incomplete_value": false,
      "site": "00bc448c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc4448",
      "incomplete_value": false,
      "site": "00bc4448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "00bc448c",
      "DATA",
      [
        "storage",
        "00c17f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc448c",
      "DATA",
      [
        "storage",
        "00c17f88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc43d4.md#insn-00bc4418) · [`00bc443c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc43d4.md#insn-00bc443c) · [`00bc449c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc43d4.md#insn-00bc449c)
- 新版 `00bc445c`（命令位置の公開資料なし） · `00bc4480`（命令位置の公開資料なし） · `00bc44e0`（命令位置の公開資料なし）

~~~diff
- 00bc4418 ["INT_ADD", "register:40f0:8", ["const:bc4418:8", "const:4:8"]]
- 00bc4418 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc445c ["INT_ADD", "register:40f0:8", ["const:bc445c:8", "const:4:8"]]
+ 00bc445c ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc4418 bytes 5a630094
+ 00bc445c bytes 5d630094
- 00bc443c ["COPY", "tmp:0:8", ["const:f38:8"]]
- 00bc443c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc443c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc443c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc4480 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 00bc4480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc4480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc4480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc443c bytes 08e13c91
+ 00bc4480 bytes 08213e91
- 00bc449c ["INT_ADD", "register:40f0:8", ["const:bc449c:8", "const:4:8"]]
- 00bc449c ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc44e0 ["INT_ADD", "register:40f0:8", ["const:bc44e0:8", "const:4:8"]]
+ 00bc44e0 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc449c bytes 395b0094
+ 00bc44e0 bytes 3c5b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa80cfaf793e8c58302d9b769d8ca047"></a>

### [`00bc44a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc44a0.md) → [`00bc44e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc44e4.md) FUN_00bc44e4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc4564",
      "incomplete_value": false,
      "site": "00bc4564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc4520",
      "incomplete_value": false,
      "site": "00bc4520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc4564",
      "DATA",
      [
        "storage",
        "00c17fa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc4564",
      "DATA",
      [
        "storage",
        "00c17ff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc44f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc44a0.md#insn-00bc44f0) · [`00bc4514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc44a0.md#insn-00bc4514) · [`00bc4588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc44a0.md#insn-00bc4588)
- 新版 `00bc4534`（命令位置の公開資料なし） · `00bc4558`（命令位置の公開資料なし） · `00bc45cc`（命令位置の公開資料なし）

~~~diff
- 00bc44f0 ["INT_ADD", "register:40f0:8", ["const:bc44f0:8", "const:4:8"]]
- 00bc44f0 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc4534 ["INT_ADD", "register:40f0:8", ["const:bc4534:8", "const:4:8"]]
+ 00bc4534 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc44f0 bytes 24630094
+ 00bc4534 bytes 27630094
- 00bc4514 ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 00bc4514 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc4514 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc4514 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc4558 ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 00bc4558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc4558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc4558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc4514 bytes 08a13e91
+ 00bc4558 bytes 08e13f91
- 00bc4588 ["INT_ADD", "register:40f0:8", ["const:bc4588:8", "const:4:8"]]
- 00bc4588 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc45cc ["INT_ADD", "register:40f0:8", ["const:bc45cc:8", "const:4:8"]]
+ 00bc45cc ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc4588 bytes fe5a0094
+ 00bc45cc bytes 015b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-602be3f6c5f88f109be6dbbca74329a8"></a>

### [`00bc458c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc458c.md) → [`00bc45d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc45d0.md) FUN_00bc45d0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc4640",
      "incomplete_value": false,
      "site": "00bc4640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc45fc",
      "incomplete_value": false,
      "site": "00bc45fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc4640",
      "DATA",
      [
        "storage",
        "00c18088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc4640",
      "DATA",
      [
        "storage",
        "00c180d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc45cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc458c.md#insn-00bc45cc) · [`00bc45f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc458c.md#insn-00bc45f0) · [`00bc4648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc458c.md#insn-00bc4648)
- 新版 `00bc4610`（命令位置の公開資料なし） · `00bc4634`（命令位置の公開資料なし） · `00bc468c`（命令位置の公開資料なし）

~~~diff
- 00bc45cc ["INT_ADD", "register:40f0:8", ["const:bc45cc:8", "const:4:8"]]
- 00bc45cc ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc4610 ["INT_ADD", "register:40f0:8", ["const:bc4610:8", "const:4:8"]]
+ 00bc4610 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc45cc bytes ed620094
+ 00bc4610 bytes f0620094
- 00bc45f0 ["COPY", "tmp:0:8", ["const:88:8"]]
- 00bc45f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc45f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc45f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc4634 ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 00bc4634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc4634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc4634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc45f0 bytes 08210291
+ 00bc4634 bytes 08610391
- 00bc4648 ["INT_ADD", "register:40f0:8", ["const:bc4648:8", "const:4:8"]]
- 00bc4648 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc468c ["INT_ADD", "register:40f0:8", ["const:bc468c:8", "const:4:8"]]
+ 00bc468c ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc4648 bytes ce5a0094
+ 00bc468c bytes d15a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5a996ad2b30323a4fe8d6b6ad34aa75"></a>

### [`00bc464c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc464c.md) → [`00bc4690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc4690.md) FUN_00bc4690

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc4700",
      "incomplete_value": false,
      "site": "00bc4700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc46bc",
      "incomplete_value": false,
      "site": "00bc46bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:f8:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc4700",
      "DATA",
      [
        "storage",
        "00c180f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc4700",
      "DATA",
      [
        "storage",
        "00c18148",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc468c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc464c.md#insn-00bc468c) · [`00bc46b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc464c.md#insn-00bc46b0) · [`00bc4708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc464c.md#insn-00bc4708)
- 新版 `00bc46d0`（命令位置の公開資料なし） · `00bc46f4`（命令位置の公開資料なし） · `00bc474c`（命令位置の公開資料なし）

~~~diff
- 00bc468c ["INT_ADD", "register:40f0:8", ["const:bc468c:8", "const:4:8"]]
- 00bc468c ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc46d0 ["INT_ADD", "register:40f0:8", ["const:bc46d0:8", "const:4:8"]]
+ 00bc46d0 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc468c bytes bd620094
+ 00bc46d0 bytes c0620094
- 00bc46b0 ["COPY", "tmp:0:8", ["const:f8:8"]]
- 00bc46b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc46b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc46b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc46f4 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 00bc46f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc46f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc46f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc46b0 bytes 08e10391
+ 00bc46f4 bytes 08210591
- 00bc4708 ["INT_ADD", "register:40f0:8", ["const:bc4708:8", "const:4:8"]]
- 00bc4708 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc474c ["INT_ADD", "register:40f0:8", ["const:bc474c:8", "const:4:8"]]
+ 00bc474c ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc4708 bytes 9e5a0094
+ 00bc474c bytes a15a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e888abb49c781dab748f754874dcea31"></a>

### [`00bc470c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc470c.md) → [`00bc4750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc4750.md) FUN_00bc4750

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc47c4",
      "incomplete_value": false,
      "site": "00bc47c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc4780",
      "incomplete_value": false,
      "site": "00bc4780",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:168:8"
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
      "00bc47c4",
      "DATA",
      [
        "storage",
        "00c18168",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc47c4",
      "DATA",
      [
        "storage",
        "00c181b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc470c.md#insn-00bc4750) · [`00bc4774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc470c.md#insn-00bc4774) · [`00bc47d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc470c.md#insn-00bc47d0)
- 新版 `00bc4794`（命令位置の公開資料なし） · `00bc47b8`（命令位置の公開資料なし） · `00bc4814`（命令位置の公開資料なし）

~~~diff
- 00bc4750 ["INT_ADD", "register:40f0:8", ["const:bc4750:8", "const:4:8"]]
- 00bc4750 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc4794 ["INT_ADD", "register:40f0:8", ["const:bc4794:8", "const:4:8"]]
+ 00bc4794 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc4750 bytes 8c620094
+ 00bc4794 bytes 8f620094
- 00bc4774 ["COPY", "tmp:0:8", ["const:168:8"]]
- 00bc4774 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc4774 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc4774 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc47b8 ["COPY", "tmp:0:8", ["const:1b8:8"]]
+ 00bc47b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc47b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc47b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc4774 bytes 08a10591
+ 00bc47b8 bytes 08e10691
- 00bc47d0 ["INT_ADD", "register:40f0:8", ["const:bc47d0:8", "const:4:8"]]
- 00bc47d0 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc4814 ["INT_ADD", "register:40f0:8", ["const:bc4814:8", "const:4:8"]]
+ 00bc4814 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc47d0 bytes 6c5a0094
+ 00bc4814 bytes 6f5a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b12a12e02356009bc858f3b8ad06ecf8"></a>

### [`00bc489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md) → [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) FUN_00bc48e0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 12件 [`00bbd264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd264.md) [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bc9384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9384.md) [`00bc9478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9478.md)
- 新版 呼出元 2件 [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 12件 [`00bbd2a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd2a8.md) [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bc93c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc93c8.md) [`00bc94bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc94bc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.20% / 新版 97.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc4f40",
      "incomplete_value": false,
      "site": "00bc4f40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc4efc",
      "incomplete_value": false,
      "site": "00bc4efc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "definition_site": "00bc51bc",
      "incomplete_value": false,
      "site": "00bc51bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5178",
      "incomplete_value": false,
      "site": "00bc5178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "ordinal": 53,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc4940",
      "DATA",
      [
        "storage",
        "002fcc64",
        "switchD_00bc4904::switchdataD_002fcc64",
        "ushort"
      ]
    ],
    [
      "00bc4a78",
      "PARAM",
      [
        "storage",
        "0029cebe",
        null,
        "string"
      ]
    ],
    [
      "00bc4a90",
      "PARAM",
      [
        "storage",
        "0029c264",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc4940",
      "DATA",
      [
        "storage",
        "002fcc64",
        "switchD_00bc4948::switchdataD_002fcc64",
        "ushort"
      ]
    ],
    [
      "00bc4a78",
      "PARAM",
      [
        "storage",
        "0029cf49",
        null,
        "string"
      ]
    ],
    [
      "00bc4a90",
      "PARAM",
      [
        "storage",
        "0029c262",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc48f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md#insn-00bc48f8) · [`00bc4910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md#insn-00bc4910) · [`00bc4944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md#insn-00bc4944)
- 新版 `00bc493c`（命令位置の公開資料なし） · `00bc4954`（命令位置の公開資料なし） · `00bc4988`（命令位置の公開資料なし）

~~~diff
- 00bc48f8 ["COPY", "register:4078:8", ["const:bc4908:8"]]
+ 00bc493c ["COPY", "register:4078:8", ["const:bc494c:8"]]
- 00bc48f8 bytes 8f000010
+ 00bc493c bytes 8f000010
- 00bc4910 ["INT_ADD", "register:40f0:8", ["const:bc4910:8", "const:4:8"]]
- 00bc4910 ["CALL", null, ["callee:00bbde5c:8"]]
+ 00bc4954 ["INT_ADD", "register:40f0:8", ["const:bc4954:8", "const:4:8"]]
+ 00bc4954 ["CALL", null, ["callee:00bbde5c:8"]]
- 00bc4910 bytes 42e5ff97
+ 00bc4954 bytes 42e5ff97
- 00bc4944 ["INT_ADD", "register:40f0:8", ["const:bc4944:8", "const:4:8"]]
- 00bc4944 ["CALL", null, ["callee:00bc9564:8"]]
+ 00bc4988 ["INT_ADD", "register:40f0:8", ["const:bc4988:8", "const:4:8"]]
+ 00bc4988 ["CALL", null, ["callee:00bc9564:8"]]
- 00bc4944 bytes f7120094
+ 00bc4988 bytes f7120094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb3c9fd1f9abdb979643d5554bfb6dea"></a>

### [`00bc521c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc521c.md) → [`00bc5260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5260.md) FUN_00bc5260

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 3件 [`00bcc6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc6a8.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 3件 [`00bcc6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc6ec.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.91% / 新版 97.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc548c",
      "incomplete_value": false,
      "site": "00bc548c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5448",
      "incomplete_value": false,
      "site": "00bc5448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc5564",
      "incomplete_value": false,
      "site": "00bc5564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5520",
      "incomplete_value": false,
      "site": "00bc5520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "00bc548c",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc54b4",
      "DATA",
      [
        "storage",
        "002af88b",
        null,
        null
      ]
    ],
    [
      "00bc5564",
      "DATA",
      [
        "storage",
        "00c189b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc548c",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc54b4",
      "DATA",
      [
        "storage",
        "002af7f7",
        null,
        null
      ]
    ],
    [
      "00bc5564",
      "DATA",
      [
        "storage",
        "00c18a08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc521c.md#insn-00bc5418) · [`00bc543c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc521c.md#insn-00bc543c) · [`00bc5460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc521c.md#insn-00bc5460)
- 新版 `00bc545c`（命令位置の公開資料なし） · `00bc5480`（命令位置の公開資料なし） · `00bc54a4`（命令位置の公開資料なし）

~~~diff
- 00bc5418 ["INT_ADD", "register:40f0:8", ["const:bc5418:8", "const:4:8"]]
- 00bc5418 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc545c ["INT_ADD", "register:40f0:8", ["const:bc545c:8", "const:4:8"]]
+ 00bc545c ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc5418 bytes 5a5f0094
+ 00bc545c bytes 5d5f0094
- 00bc543c ["COPY", "tmp:0:8", ["const:848:8"]]
- 00bc543c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bc543c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bc543c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bc5480 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00bc5480 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00bc5480 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00bc5480 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bc543c bytes 4a212191
+ 00bc5480 bytes 4a612291
- 00bc5460 ["COPY", "tmp:0:8", ["const:88b:8"]]
- 00bc5460 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bc5460 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bc5460 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bc54a4 ["COPY", "tmp:0:8", ["const:7f7:8"]]
+ 00bc54a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00bc54a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00bc54a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bc5460 bytes 4a2d2291
+ 00bc54a4 bytes 4add1f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0460a6e4932fc51e27a9a9a0d9acaae4"></a>

### [`00bc55d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc55d8.md) → [`00bc561c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc561c.md) FUN_00bc561c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bc55d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc55d8.md) · 呼出先 5件 [`00bc10fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc10fc.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bc55d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc55d8.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 2件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bc561c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc561c.md) · 呼出先 5件 [`00bc1140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1140.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bc561c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc561c.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc56e4",
      "incomplete_value": false,
      "site": "00bc56e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc56a0",
      "incomplete_value": false,
      "site": "00bc56a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:b08:8"
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
      "definition_site": "00bc5794",
      "incomplete_value": true,
      "site": "00bc5794",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5750",
      "incomplete_value": true,
      "site": "00bc5750",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc5844",
      "incomplete_value": false,
      "site": "00bc5844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5800",
      "incomplete_value": false,
      "site": "00bc5800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc56e4",
      "DATA",
      [
        "storage",
        "00c18b08",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5794",
      "DATA",
      [
        "storage",
        "00c18b08",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5844",
      "DATA",
      [
        "storage",
        "00c18b78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc56e4",
      "DATA",
      [
        "storage",
        "00c18b58",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5794",
      "DATA",
      [
        "storage",
        "00c18b58",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5844",
      "DATA",
      [
        "storage",
        "00c18bc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc55d8.md#insn-00bc5638) · [`00bc5648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc55d8.md#insn-00bc5648) · [`00bc5670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc55d8.md#insn-00bc5670)
- 新版 `00bc567c`（命令位置の公開資料なし） · `00bc568c`（命令位置の公開資料なし） · `00bc56b4`（命令位置の公開資料なし）

~~~diff
- 00bc5638 ["INT_ADD", "register:40f0:8", ["const:bc5638:8", "const:4:8"]]
- 00bc5638 ["CALL", null, ["callee:00bc1140:8"]]
+ 00bc567c ["INT_ADD", "register:40f0:8", ["const:bc567c:8", "const:4:8"]]
+ 00bc567c ["CALL", null, ["callee:00bc1140:8"]]
- 00bc5638 bytes b1eeff97
+ 00bc567c bytes b1eeff97
- 00bc5648 ["INT_ADD", "register:40f0:8", ["const:bc5648:8", "const:4:8"]]
- 00bc5648 ["CALL", null, ["local:b0:8"]]
+ 00bc568c ["INT_ADD", "register:40f0:8", ["const:bc568c:8", "const:4:8"]]
+ 00bc568c ["CALL", null, ["local:b0:8"]]
- 00bc5648 bytes e4ffff97
+ 00bc568c bytes e4ffff97
- 00bc5670 ["INT_ADD", "register:40f0:8", ["const:bc5670:8", "const:4:8"]]
- 00bc5670 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc56b4 ["INT_ADD", "register:40f0:8", ["const:bc56b4:8", "const:4:8"]]
+ 00bc56b4 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc5670 bytes c45e0094
+ 00bc56b4 bytes c75e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-944e30e131dec5a1ea97a45ba13bcc2c"></a>

### [`00bc5840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5840.md) → [`00bc5884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5884.md) FUN_00bc5884

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc58e8",
      "incomplete_value": false,
      "site": "00bc58e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc58a4",
      "incomplete_value": false,
      "site": "00bc58a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc58e8",
      "DATA",
      [
        "storage",
        "00c18be8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc58e8",
      "DATA",
      [
        "storage",
        "00c18c38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5840.md#insn-00bc5874) · [`00bc5898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5840.md#insn-00bc5898) · [`00bc58e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5840.md#insn-00bc58e0)
- 新版 `00bc58b8`（命令位置の公開資料なし） · `00bc58dc`（命令位置の公開資料なし） · `00bc5924`（命令位置の公開資料なし）

~~~diff
- 00bc5874 ["INT_ADD", "register:40f0:8", ["const:bc5874:8", "const:4:8"]]
- 00bc5874 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc58b8 ["INT_ADD", "register:40f0:8", ["const:bc58b8:8", "const:4:8"]]
+ 00bc58b8 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc5874 bytes 435e0094
+ 00bc58b8 bytes 465e0094
- 00bc5898 ["COPY", "tmp:0:8", ["const:be8:8"]]
- 00bc5898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc5898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc5898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc58dc ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 00bc58dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc58dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc58dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc5898 bytes 08a12f91
+ 00bc58dc bytes 08e13091
- 00bc58e0 ["INT_ADD", "register:40f0:8", ["const:bc58e0:8", "const:4:8"]]
- 00bc58e0 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc5924 ["INT_ADD", "register:40f0:8", ["const:bc5924:8", "const:4:8"]]
+ 00bc5924 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc58e0 bytes 28560094
+ 00bc5924 bytes 2b560094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-069bbb4bb79904b5831d98647e01bee4"></a>

### [`00bc58e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc58e4.md) → [`00bc5928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5928.md) FUN_00bc5928

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 4件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 4件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.78% / 新版 97.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc5a44",
      "incomplete_value": false,
      "site": "00bc5a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5a00",
      "incomplete_value": false,
      "site": "00bc5a00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc5a44",
      "DATA",
      [
        "storage",
        "00c18c58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc5a44",
      "DATA",
      [
        "storage",
        "00c18ca8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc58e4.md#insn-00bc5900) · [`00bc5910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc58e4.md#insn-00bc5910) · [`00bc59cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc58e4.md#insn-00bc59cc)
- 新版 `00bc5944`（命令位置の公開資料なし） · `00bc5954`（命令位置の公開資料なし） · `00bc5a10`（命令位置の公開資料なし）

~~~diff
- 00bc5900 ["INT_ADD", "register:40f0:8", ["const:bc5900:8", "const:4:8"]]
- 00bc5900 ["CALL", null, ["callee:00bbde5c:8"]]
+ 00bc5944 ["INT_ADD", "register:40f0:8", ["const:bc5944:8", "const:4:8"]]
+ 00bc5944 ["CALL", null, ["callee:00bbde5c:8"]]
- 00bc5900 bytes 46e1ff97
+ 00bc5944 bytes 46e1ff97
- 00bc5910 ["INT_ADD", "register:40f0:8", ["const:bc5910:8", "const:4:8"]]
- 00bc5910 ["CALL", null, ["callee:00bc2f0c:8"]]
+ 00bc5954 ["INT_ADD", "register:40f0:8", ["const:bc5954:8", "const:4:8"]]
+ 00bc5954 ["CALL", null, ["callee:00bc2f0c:8"]]
- 00bc5910 bytes 6ef5ff97
+ 00bc5954 bytes 6ef5ff97
- 00bc59cc ["INT_ADD", "register:40f0:8", ["const:bc59cc:8", "const:4:8"]]
- 00bc59cc ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc5a10 ["INT_ADD", "register:40f0:8", ["const:bc5a10:8", "const:4:8"]]
+ 00bc5a10 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc59cc bytes ed5d0094
+ 00bc5a10 bytes f05d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03f61e56297e72256974138b25d84cac"></a>

### [`00bc5a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5a4c.md) → [`00bc5a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5a90.md) FUN_00bc5a90

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc5af8",
      "incomplete_value": false,
      "site": "00bc5af8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5ab4",
      "incomplete_value": false,
      "site": "00bc5ab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:248:8"
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
      "definition_site": "00bc5b24",
      "incomplete_value": false,
      "site": "00bc5b24",
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
            "const:2db:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5ae0",
      "incomplete_value": false,
      "site": "00bc5ae0",
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
            "const:241:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc5af8",
      "DATA",
      [
        "storage",
        "00c18248",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5b24",
      "DATA",
      [
        "storage",
        "002a7241",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc5af8",
      "DATA",
      [
        "storage",
        "00c18298",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5b24",
      "DATA",
      [
        "storage",
        "002a72db",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5a4c.md#insn-00bc5a84) · [`00bc5aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5a4c.md#insn-00bc5aa8) · [`00bc5ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5a4c.md#insn-00bc5ac8)
- 新版 `00bc5ac8`（命令位置の公開資料なし） · `00bc5aec`（命令位置の公開資料なし） · `00bc5b0c`（命令位置の公開資料なし）

~~~diff
- 00bc5a84 ["INT_ADD", "register:40f0:8", ["const:bc5a84:8", "const:4:8"]]
- 00bc5a84 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc5ac8 ["INT_ADD", "register:40f0:8", ["const:bc5ac8:8", "const:4:8"]]
+ 00bc5ac8 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc5a84 bytes bf5d0094
+ 00bc5ac8 bytes c25d0094
- 00bc5aa8 ["COPY", "tmp:0:8", ["const:248:8"]]
- 00bc5aa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc5aa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc5aa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc5aec ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00bc5aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc5aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc5aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc5aa8 bytes 08210991
+ 00bc5aec bytes 08610a91
- 00bc5ac8 ["COPY", "tmp:0:8", ["const:241:8"]]
- 00bc5ac8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bc5ac8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bc5ac8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bc5b0c ["COPY", "tmp:0:8", ["const:2db:8"]]
+ 00bc5b0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc5b0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc5b0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bc5ac8 bytes 29050991
+ 00bc5b0c bytes 296d0b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0d8b50868e009ba9f5fab15346c4fa9"></a>

### [`00bc5b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5b0c.md) → [`00bc5b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5b50.md) FUN_00bc5b50

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 9件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bbff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 9件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bbff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.38% / 新版 98.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc5fe0",
      "incomplete_value": false,
      "site": "00bc5fe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5f9c",
      "incomplete_value": false,
      "site": "00bc5f9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "ordinal": 60,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc5e3c",
      "DATA",
      [
        "storage",
        "00c18cc8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5ed0",
      "DATA",
      [
        "storage",
        "00c18d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5ed0",
      "DATA",
      [
        "storage",
        "00c18da8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc5e3c",
      "DATA",
      [
        "storage",
        "00c18d18",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5ed0",
      "DATA",
      [
        "storage",
        "00c18d88",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5ed0",
      "DATA",
      [
        "storage",
        "00c18df8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5b0c.md#insn-00bc5ba8) · [`00bc5bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5b0c.md#insn-00bc5bf0) · [`00bc5c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5b0c.md#insn-00bc5c20)
- 新版 `00bc5bec`（命令位置の公開資料なし） · `00bc5c34`（命令位置の公開資料なし） · `00bc5c64`（命令位置の公開資料なし）

~~~diff
- 00bc5ba8 ["INT_ADD", "register:40f0:8", ["const:bc5ba8:8", "const:4:8"]]
- 00bc5ba8 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bc5bec ["INT_ADD", "register:40f0:8", ["const:bc5bec:8", "const:4:8"]]
+ 00bc5bec ["CALL", null, ["callee:00bdd250:8"]]
- 00bc5ba8 bytes 965d0094
+ 00bc5bec bytes 995d0094
- 00bc5bf0 ["INT_ADD", "register:40f0:8", ["const:bc5bf0:8", "const:4:8"]]
- 00bc5bf0 ["CALL", null, ["callee:00bbde5c:8"]]
+ 00bc5c34 ["INT_ADD", "register:40f0:8", ["const:bc5c34:8", "const:4:8"]]
+ 00bc5c34 ["CALL", null, ["callee:00bbde5c:8"]]
- 00bc5bf0 bytes 8ae0ff97
+ 00bc5c34 bytes 8ae0ff97
- 00bc5c20 ["INT_ADD", "register:40f0:8", ["const:bc5c20:8", "const:4:8"]]
- 00bc5c20 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc5c64 ["INT_ADD", "register:40f0:8", ["const:bc5c64:8", "const:4:8"]]
+ 00bc5c64 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc5c20 bytes 585d0094
+ 00bc5c64 bytes 5b5d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b432108463ec1bc734fc458e9b8ab39"></a>

### [`00bc5fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5fdc.md) → [`00bc6020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6020.md) FUN_00bc6020

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 8件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 8件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc6304",
      "incomplete_value": false,
      "site": "00bc6304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc62c0",
      "incomplete_value": false,
      "site": "00bc62c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:e88:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc612c",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc6304",
      "DATA",
      [
        "storage",
        "00c18e88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc612c",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc6304",
      "DATA",
      [
        "storage",
        "00c18ed8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc6004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5fdc.md#insn-00bc6004) · [`00bc6014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5fdc.md#insn-00bc6014) · [`00bc60ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5fdc.md#insn-00bc60ac)
- 新版 `00bc6048`（命令位置の公開資料なし） · `00bc6058`（命令位置の公開資料なし） · `00bc60f0`（命令位置の公開資料なし）

~~~diff
- 00bc6004 ["INT_ADD", "register:40f0:8", ["const:bc6004:8", "const:4:8"]]
- 00bc6004 ["CALL", null, ["callee:00bbde5c:8"]]
+ 00bc6048 ["INT_ADD", "register:40f0:8", ["const:bc6048:8", "const:4:8"]]
+ 00bc6048 ["CALL", null, ["callee:00bbde5c:8"]]
- 00bc6004 bytes 85dfff97
+ 00bc6048 bytes 85dfff97
- 00bc6014 ["INT_ADD", "register:40f0:8", ["const:bc6014:8", "const:4:8"]]
- 00bc6014 ["CALL", null, ["callee:00bc2f0c:8"]]
+ 00bc6058 ["INT_ADD", "register:40f0:8", ["const:bc6058:8", "const:4:8"]]
+ 00bc6058 ["CALL", null, ["callee:00bc2f0c:8"]]
- 00bc6014 bytes adf3ff97
+ 00bc6058 bytes adf3ff97
- 00bc60ac ["COPY", "tmp:0:8", ["const:848:8"]]
- 00bc60ac ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
- 00bc60ac ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
- 00bc60ac ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
+ 00bc60f0 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00bc60f0 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
+ 00bc60f0 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
+ 00bc60f0 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
- 00bc60ac bytes 9c232191
+ 00bc60f0 bytes 9c632291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-989490d76fee12418ea4f87d6d1c2a75"></a>

### [`00bc63d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc63d0.md) → [`00bc6414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6414.md) FUN_00bc6414

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc6478",
      "incomplete_value": false,
      "site": "00bc6478",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:f48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc6434",
      "incomplete_value": false,
      "site": "00bc6434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc6478",
      "DATA",
      [
        "storage",
        "00c18ef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc6478",
      "DATA",
      [
        "storage",
        "00c18f48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc6404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc63d0.md#insn-00bc6404) · [`00bc6428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc63d0.md#insn-00bc6428) · [`00bc646c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc63d0.md#insn-00bc646c)
- 新版 `00bc6448`（命令位置の公開資料なし） · `00bc646c`（命令位置の公開資料なし） · `00bc64b0`（命令位置の公開資料なし）

~~~diff
- 00bc6404 ["INT_ADD", "register:40f0:8", ["const:bc6404:8", "const:4:8"]]
- 00bc6404 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc6448 ["INT_ADD", "register:40f0:8", ["const:bc6448:8", "const:4:8"]]
+ 00bc6448 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc6404 bytes 5f5b0094
+ 00bc6448 bytes 625b0094
- 00bc6428 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 00bc6428 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc6428 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc6428 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc646c ["COPY", "tmp:0:8", ["const:f48:8"]]
+ 00bc646c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc646c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc646c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc6428 bytes 08e13b91
+ 00bc646c bytes 08213d91
- 00bc646c ["INT_ADD", "register:40f0:8", ["const:bc646c:8", "const:4:8"]]
- 00bc646c ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc64b0 ["INT_ADD", "register:40f0:8", ["const:bc64b0:8", "const:4:8"]]
+ 00bc64b0 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc646c bytes 45530094
+ 00bc64b0 bytes 48530094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70c203ecf725eec336ff06927e9e534c"></a>

### [`00bc6470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6470.md) → [`00bc64b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc64b4.md) FUN_00bc64b4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc651c",
      "incomplete_value": false,
      "site": "00bc651c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc64d8",
      "incomplete_value": false,
      "site": "00bc64d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc6534",
      "incomplete_value": false,
      "site": "00bc6534",
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
            "const:276:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc64f0",
      "incomplete_value": false,
      "site": "00bc64f0",
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
            "const:1eb:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc651c",
      "DATA",
      [
        "storage",
        "00c18248",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc6534",
      "DATA",
      [
        "storage",
        "0029d1eb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc651c",
      "DATA",
      [
        "storage",
        "00c18298",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc6534",
      "DATA",
      [
        "storage",
        "0029d276",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc64a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6470.md#insn-00bc64a4) · [`00bc64c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6470.md#insn-00bc64c8) · [`00bc64d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6470.md#insn-00bc64d0)
- 新版 `00bc64e8`（命令位置の公開資料なし） · `00bc650c`（命令位置の公開資料なし）

~~~diff
- 00bc64a4 ["INT_ADD", "register:40f0:8", ["const:bc64a4:8", "const:4:8"]]
- 00bc64a4 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc64e8 ["INT_ADD", "register:40f0:8", ["const:bc64e8:8", "const:4:8"]]
+ 00bc64e8 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc64a4 bytes 375b0094
+ 00bc64e8 bytes 3a5b0094
- 00bc64c8 ["COPY", "tmp:0:8", ["const:248:8"]]
- 00bc64c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc64c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc64c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc650c ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00bc650c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc650c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc650c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc64c8 bytes 08210991
+ 00bc650c bytes 08610a91
- 00bc64d0 ["COPY", "register:4048:8", ["const:29d000:8"]]
- 00bc64d0 bytes a9b6fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

