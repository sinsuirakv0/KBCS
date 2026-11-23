# v15.7.3 → v15.7.4 · 最優先の変更候補 (11)

[一覧の目次](README.md)

<a id="compare-abd06dc27842e133456c63b998621ad3"></a>

### [`004e15f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e1/004e15f0.md) → [`004e15f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e15f0.md) _ZNK5Botan10Data_Store4get1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.73% / 新版 97.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e1700",
      "incomplete_value": false,
      "site": "004e170c",
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
            "const:b7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e1700",
      "incomplete_value": false,
      "site": "004e170c",
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
            "const:c07:8"
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
      "definition_site": "004e173c",
      "incomplete_value": true,
      "site": "004e1748",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e173c",
      "incomplete_value": true,
      "site": "004e1748",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
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
      "004e1700",
      "PARAM",
      [
        "storage",
        "00297c07",
        null,
        "string"
      ]
    ],
    [
      "004e173c",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "004e173c",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e1700",
      "PARAM",
      [
        "storage",
        "00297b7a",
        null,
        "string"
      ]
    ],
    [
      "004e173c",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "004e173c",
      "PARAM",
      [
        "storage",
        "00be93d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e1700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e1/004e15f0.md#insn-004e1700) · [`004e173c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e1/004e15f0.md#insn-004e173c)
- 新版 `004e1700`（命令位置の公開資料なし） · `004e173c`（命令位置の公開資料なし）

~~~diff
- 004e1700 ["COPY", "tmp:0:8", ["const:c07:8"]]
- 004e1700 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004e1700 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004e1700 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004e1700 ["COPY", "tmp:0:8", ["const:b7a:8"]]
+ 004e1700 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004e1700 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004e1700 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004e1700 bytes 001c3091
+ 004e1700 bytes 00e82d91
- 004e173c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 004e173c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e173c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 004e173c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e173c bytes 218447f9
+ 004e173c bytes 21ac47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c0450166086bc22afbb1a30d4674ce9"></a>

### [`004e17a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e1/004e17a8.md) → [`004e17a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e17a8.md) _ZNK5Botan10Data_Store11get1_memvecERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.85% / 新版 98.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e18f0",
      "incomplete_value": true,
      "site": "004e18fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e18f0",
      "incomplete_value": true,
      "site": "004e18fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
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
      "004e18f0",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "004e18f0",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e18f0",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "004e18f0",
      "PARAM",
      [
        "storage",
        "00be93d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e18f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e1/004e17a8.md#insn-004e18f0)
- 新版 `004e18f0`（命令位置の公開資料なし）

~~~diff
- 004e18f0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 004e18f0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e18f0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 004e18f0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e18f0 bytes 218447f9
+ 004e18f0 bytes 21ac47f9
~~~


<a id="compare-a65d9043f0f80d9f7b4396c05663ab46"></a>

### [`004e195c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e1/004e195c.md) → [`004e195c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e195c.md) _ZNK5Botan10Data_Store11get1_uint32ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEj

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e1a44",
      "incomplete_value": false,
      "site": "004e1a50",
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
            "const:b19:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e1a44",
      "incomplete_value": false,
      "site": "004e1a50",
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
            "const:ba6:8"
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
      "definition_site": "004e1a80",
      "incomplete_value": true,
      "site": "004e1a8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e1a80",
      "incomplete_value": true,
      "site": "004e1a8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
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
      "004e1a44",
      "PARAM",
      [
        "storage",
        "00295ba6",
        null,
        "string"
      ]
    ],
    [
      "004e1a80",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "004e1a80",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e1a44",
      "PARAM",
      [
        "storage",
        "00295b19",
        null,
        "string"
      ]
    ],
    [
      "004e1a80",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "004e1a80",
      "PARAM",
      [
        "storage",
        "00be93d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e1a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e1/004e195c.md#insn-004e1a44) · [`004e1a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e1/004e195c.md#insn-004e1a80)
- 新版 `004e1a44`（命令位置の公開資料なし） · `004e1a80`（命令位置の公開資料なし）

~~~diff
- 004e1a44 ["COPY", "tmp:0:8", ["const:ba6:8"]]
- 004e1a44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004e1a44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004e1a44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004e1a44 ["COPY", "tmp:0:8", ["const:b19:8"]]
+ 004e1a44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004e1a44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004e1a44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004e1a44 bytes 00982e91
+ 004e1a44 bytes 00642c91
- 004e1a80 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 004e1a80 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e1a80 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 004e1a80 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e1a80 bytes 218447f9
+ 004e1a80 bytes 21ac47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2b9407c570f346231628efc5dca1ecc"></a>

### [`004e1f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e1/004e1f38.md) → [`004e1f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e1f38.md) _ZN5Botan9create_dnERKNS_10Data_StoreE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00526374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00526/00526374.md) [`00526378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00526/00526378.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00526374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526374.md) [`00526378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526378.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004e1f58",
      "incomplete_value": false,
      "site": "004e1f68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e1f58",
      "incomplete_value": false,
      "site": "004e1f68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "definition_site": "004e1fd4",
      "incomplete_value": true,
      "site": "004e1fd4",
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
      "definition_site": "004e1fd4",
      "incomplete_value": true,
      "site": "004e1fd4",
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
      "004e1f68",
      "DATA",
      [
        "storage",
        "00bed870",
        null,
        "undefined *"
      ]
    ],
    [
      "004e1fa0",
      "READ",
      [
        "storage",
        "00bed890",
        null,
        "pointer"
      ]
    ],
    [
      "004e1fa0",
      "READ",
      [
        "storage",
        "00bed898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004e1f68",
      "DATA",
      [
        "storage",
        "00bed8c0",
        null,
        "undefined *"
      ]
    ],
    [
      "004e1fa0",
      "READ",
      [
        "storage",
        "00bed8e0",
        null,
        "pointer"
      ]
    ],
    [
      "004e1fa0",
      "READ",
      [
        "storage",
        "00bed8e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e1f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e1/004e1f38.md#insn-004e1f58) · [`004e1fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e1/004e1f38.md#insn-004e1fb4)
- 新版 `004e1f58`（命令位置の公開資料なし） · `004e1fb4`（命令位置の公開資料なし）

~~~diff
- 004e1f58 ["COPY", "tmp:0:8", ["const:870:8"]]
- 004e1f58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004e1f58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004e1f58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004e1f58 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 004e1f58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004e1f58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004e1f58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004e1f58 bytes 29c12191
+ 004e1f58 bytes 29012391
- 004e1fb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
- 004e1fb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e1fb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
+ 004e1fb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e1fb4 bytes 084941f9
+ 004e1fb4 bytes 087141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0ad9b934b16787f3e4b3e4e6481402c"></a>

### [`004e21a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e2/004e21a8.md) → [`004e21a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e21a8.md) _ZN5Botan15create_alt_nameERKNS_10Data_StoreE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0052647c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00526/0052647c.md) [`00526480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00526/00526480.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0052647c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/0052647c.md) [`00526480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526480.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.96% / 新版 97.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004e21d8",
      "incomplete_value": false,
      "site": "004e21d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e21d8",
      "incomplete_value": false,
      "site": "004e21d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:900:8"
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
      "004e21d8",
      "DATA",
      [
        "storage",
        "00bed900",
        null,
        "undefined *"
      ]
    ],
    [
      "004e2210",
      "READ",
      [
        "storage",
        "00bed920",
        null,
        "pointer"
      ]
    ],
    [
      "004e2210",
      "READ",
      [
        "storage",
        "00bed928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004e21d8",
      "DATA",
      [
        "storage",
        "00bed950",
        null,
        "undefined *"
      ]
    ],
    [
      "004e2210",
      "READ",
      [
        "storage",
        "00bed970",
        null,
        "pointer"
      ]
    ],
    [
      "004e2210",
      "READ",
      [
        "storage",
        "00bed978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e21c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e2/004e21a8.md#insn-004e21c8)
- 新版 `004e21c8`（命令位置の公開資料なし）

~~~diff
- 004e21c8 ["COPY", "tmp:0:8", ["const:900:8"]]
- 004e21c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004e21c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004e21c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004e21c8 ["COPY", "tmp:0:8", ["const:950:8"]]
+ 004e21c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004e21c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004e21c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004e21c8 bytes 29012491
+ 004e21c8 bytes 29412591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94a289a7344837551df7a18f36433bbf"></a>

### [`004e242c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e2/004e242c.md) → [`004e242c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e242c.md) _ZN5Botan25key_constraints_to_stringENS_15Key_ConstraintsE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc80.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00bdccd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdccd0.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.98% / 新版 97.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e2498",
      "incomplete_value": true,
      "site": "004e2498",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:297000:8"
              ],
              [
                "leaf",
                "const:ba5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e2498",
      "incomplete_value": true,
      "site": "004e2498",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:297000:8"
              ],
              [
                "leaf",
                "const:c32:8"
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
      "definition_site": "004e249c",
      "incomplete_value": true,
      "site": "004e249c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004e249c",
      "incomplete_value": true,
      "site": "004e249c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004e24d0",
      "incomplete_value": true,
      "site": "004e24d0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:46b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e24d0",
      "incomplete_value": true,
      "site": "004e24d0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:3e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e2488",
      "READ",
      [
        "storage",
        "00297c32",
        null,
        "string"
      ]
    ],
    [
      "004e248c",
      "READ",
      [
        "storage",
        "00297c38",
        null,
        "string"
      ]
    ],
    [
      "004e24b8",
      "READ",
      [
        "storage",
        "002a23e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004e2488",
      "READ",
      [
        "storage",
        "00297ba5",
        null,
        "string"
      ]
    ],
    [
      "004e248c",
      "READ",
      [
        "storage",
        "00297bab",
        null,
        "string"
      ]
    ],
    [
      "004e24b8",
      "READ",
      [
        "storage",
        "002a246b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e2480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e2/004e242c.md#insn-004e2480) · [`004e24b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e2/004e242c.md#insn-004e24b0) · [`004e2550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e2/004e242c.md#insn-004e2550)
- 新版 `004e2480`（命令位置の公開資料なし） · `004e24b0`（命令位置の公開資料なし） · `004e2550`（命令位置の公開資料なし）

~~~diff
- 004e2480 ["COPY", "tmp:0:8", ["const:c32:8"]]
- 004e2480 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004e2480 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004e2480 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004e2480 ["COPY", "tmp:0:8", ["const:ba5:8"]]
+ 004e2480 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004e2480 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004e2480 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004e2480 bytes 29c93091
+ 004e2480 bytes 29952e91
- 004e24b0 ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 004e24b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004e24b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004e24b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004e24b0 ["COPY", "tmp:0:8", ["const:46b:8"]]
+ 004e24b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004e24b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004e24b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004e24b0 bytes 29810f91
+ 004e24b0 bytes 29ad1191
- 004e2550 ["COPY", "tmp:0:8", ["const:90d:8"]]
- 004e2550 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004e2550 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004e2550 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004e2550 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 004e2550 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004e2550 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004e2550 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004e2550 bytes 4a352491
+ 004e2550 bytes 4a012291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24f335a6222d81b73e03791f68cfcaae"></a>

### [`004e3024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3024.md) → [`004e3024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3024.md) _ZN5Botan42verify_cert_constraints_valid_for_key_typeERKNS_10Public_KeyENS_15Key_ConstraintsE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc90.md) · 呼出先 10件 [`00483974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdcce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcce0.md) · 呼出先 10件 [`00483974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.06% / 新版 99.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e32f0",
      "incomplete_value": false,
      "site": "004e32f8",
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
            "const:b33:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e32f0",
      "incomplete_value": false,
      "site": "004e32f8",
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
            "const:bc0:8"
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
      "definition_site": "004e3360",
      "incomplete_value": true,
      "site": "004e336c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e3360",
      "incomplete_value": true,
      "site": "004e336c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f48:8"
              ]
            ]
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
      "004e32f0",
      "PARAM",
      [
        "storage",
        "00296bc0",
        null,
        "string"
      ]
    ],
    [
      "004e3360",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004e3360",
      "PARAM",
      [
        "storage",
        "00be9238",
        "_ZTIN5Botan9ExceptionE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e32f0",
      "PARAM",
      [
        "storage",
        "00296b33",
        null,
        "string"
      ]
    ],
    [
      "004e3360",
      "READ",
      [
        "storage",
        "00c1af98",
        null,
        "pointer"
      ]
    ],
    [
      "004e3360",
      "PARAM",
      [
        "storage",
        "00be9288",
        "_ZTIN5Botan9ExceptionE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e32f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3024.md#insn-004e32f0) · [`004e3360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3024.md#insn-004e3360)
- 新版 `004e32f0`（命令位置の公開資料なし） · `004e3360`（命令位置の公開資料なし）

~~~diff
- 004e32f0 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 004e32f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004e32f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004e32f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004e32f0 ["COPY", "tmp:0:8", ["const:b33:8"]]
+ 004e32f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004e32f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004e32f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004e32f0 bytes 21002f91
+ 004e32f0 bytes 21cc2c91
- 004e3360 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f48:8"]]
- 004e3360 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e3360 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f98:8"]]
+ 004e3360 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e3360 bytes 21a447f9
+ 004e3360 bytes 21cc47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7b1085f6e88eabe6761670d2b351d43"></a>

### [`004e3458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3458.md) → [`004e3458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3458.md) _ZN5Botan11GeneralNameC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcce0.md) · 呼出先 12件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00bdcd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd30.md) · 呼出先 12件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e349c",
      "incomplete_value": true,
      "site": "004e34a4",
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
      "definition_site": "004e349c",
      "incomplete_value": true,
      "site": "004e34a4",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e3680",
      "incomplete_value": false,
      "site": "004e3688",
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
            "const:6af:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e3680",
      "incomplete_value": false,
      "site": "004e3688",
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
            "const:624:8"
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
      "definition_site": "004e36b8",
      "incomplete_value": true,
      "site": "004e36c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e36b8",
      "incomplete_value": true,
      "site": "004e36c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
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
      "004e3484",
      "READ",
      [
        "storage",
        "00c1b2e8",
        null,
        "pointer"
      ]
    ],
    [
      "004e34a4",
      "DATA",
      [
        "storage",
        "00beb0c0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e3680",
      "PARAM",
      [
        "storage",
        "002a1624",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004e3484",
      "READ",
      [
        "storage",
        "00c1b338",
        null,
        "pointer"
      ]
    ],
    [
      "004e34a4",
      "DATA",
      [
        "storage",
        "00beb110",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e3680",
      "PARAM",
      [
        "storage",
        "002a16af",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e3484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3458.md#insn-004e3484) · [`004e3680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3458.md#insn-004e3680) · [`004e36b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3458.md#insn-004e36b8)
- 新版 `004e3484`（命令位置の公開資料なし） · `004e3680`（命令位置の公開資料なし） · `004e36b8`（命令位置の公開資料なし）

~~~diff
- 004e3484 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e8:8"]]
- 004e3484 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e3484 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:338:8"]]
+ 004e3484 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e3484 bytes 087541f9
+ 004e3484 bytes 089d41f9
- 004e3680 ["COPY", "tmp:0:8", ["const:624:8"]]
- 004e3680 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004e3680 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004e3680 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004e3680 ["COPY", "tmp:0:8", ["const:6af:8"]]
+ 004e3680 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004e3680 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004e3680 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004e3680 bytes 21901891
+ 004e3680 bytes 21bc1a91
- 004e36b8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 004e36b8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e36b8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004e36b8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e36b8 bytes 217847f9
+ 004e36b8 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbffde25735aec784faca1b2d2e32671"></a>

### [`004e3770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3770.md) → [`004e3770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3770.md) _ZNK5Botan11GeneralName11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdc640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc640.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdc690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc690.md)

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
      "definition_site": "004e37ec",
      "incomplete_value": true,
      "site": "004e37f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e37ec",
      "incomplete_value": true,
      "site": "004e37f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:190:8"
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
      "004e37ec",
      "READ",
      [
        "storage",
        "00c1b190",
        null,
        "pointer"
      ]
    ],
    [
      "004e37ec",
      "PARAM",
      [
        "storage",
        "00be9e30",
        "_ZTIN5Botan15Not_ImplementedE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e37ec",
      "READ",
      [
        "storage",
        "00c1b1e0",
        null,
        "pointer"
      ]
    ],
    [
      "004e37ec",
      "PARAM",
      [
        "storage",
        "00be9e80",
        "_ZTIN5Botan15Not_ImplementedE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e37ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3770.md#insn-004e37ec)
- 新版 `004e37ec`（命令位置の公開資料なし）

~~~diff
- 004e37ec ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:190:8"]]
- 004e37ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e37ec ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:1e0:8"]]
+ 004e37ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e37ec bytes 21c840f9
+ 004e37ec bytes 21f040f9
~~~


<a id="compare-e37d65e5b303df006b405708ea7d7948"></a>

### [`004e3840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3840.md) → [`004e3840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3840.md) _ZN5Botan11GeneralName11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 29件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md) [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md)
- 新版 呼出元 0件  · 呼出先 29件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0042e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md) [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.95% / 新版 94.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e38cc",
      "incomplete_value": true,
      "site": "004e38cc",
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
      "definition_site": "004e38cc",
      "incomplete_value": true,
      "site": "004e38cc",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e3950",
      "incomplete_value": true,
      "site": "004e3958",
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
      "definition_site": "004e3950",
      "incomplete_value": true,
      "site": "004e3958",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004e3960",
      "incomplete_value": true,
      "site": "004e3960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:b0:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
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
      "definition_site": "004e3960",
      "incomplete_value": true,
      "site": "004e3960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:b0:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
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
      "004e38b4",
      "READ",
      [
        "storage",
        "00c1b290",
        null,
        "pointer"
      ]
    ],
    [
      "004e38cc",
      "DATA",
      [
        "storage",
        "00bea9e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e3938",
      "PARAM",
      [
        "storage",
        "002a95ad",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004e38b4",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "004e38cc",
      "DATA",
      [
        "storage",
        "00beaa38",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e3938",
      "PARAM",
      [
        "storage",
        "002a9647",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e38b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3840.md#insn-004e38b4) · [`004e3938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3840.md#insn-004e3938) · [`004e394c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3840.md#insn-004e394c)
- 新版 `004e38b4`（命令位置の公開資料なし） · `004e3938`（命令位置の公開資料なし） · `004e394c`（命令位置の公開資料なし）

~~~diff
- 004e38b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
- 004e38b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e38b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
+ 004e38b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e38b4 bytes 084941f9
+ 004e38b4 bytes 087141f9
- 004e3938 ["COPY", "tmp:0:8", ["const:5ad:8"]]
- 004e3938 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004e3938 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004e3938 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004e3938 ["COPY", "tmp:0:8", ["const:647:8"]]
+ 004e3938 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004e3938 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004e3938 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004e3938 bytes 21b41691
+ 004e3938 bytes 211c1991
- 004e394c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dd0:8"]]
- 004e394c ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e394c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 004e394c ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 004e394c bytes 73ea46f9
+ 004e394c bytes 731247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19b868ef926774fd10f014245345dbf3"></a>

### [`004e40b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e40b8.md) → [`004e40b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e40b8.md) _ZN5Botan7X509_DN11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004dcf48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dcf48.md) [`004f03d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f0/004f03d8.md) [`00bdcca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcca0.md) · 呼出先 12件 [`00482aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482aa8.md) [`00525f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/00525f90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 3件 [`004dcf48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dcf48.md) [`004f03d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f03d8.md) [`00bdccf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdccf0.md) · 呼出先 12件 [`00482aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482aa8.md) [`00525f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525f90.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.85% / 新版 95.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e414c",
      "incomplete_value": true,
      "site": "004e414c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "004e414c",
      "incomplete_value": true,
      "site": "004e414c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e4284",
      "incomplete_value": true,
      "site": "004e4284",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "004e4284",
      "incomplete_value": true,
      "site": "004e4284",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
    "ordinal": 19,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e430c",
      "incomplete_value": true,
      "site": "004e430c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "004e430c",
      "incomplete_value": true,
      "site": "004e430c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
    "ordinal": 26,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e413c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004e4274",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004e42fc",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e413c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004e4274",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004e42fc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e413c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e40b8.md#insn-004e413c) · [`004e4274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e40b8.md#insn-004e4274) · [`004e42fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e40b8.md#insn-004e42fc)
- 新版 `004e413c`（命令位置の公開資料なし） · `004e4274`（命令位置の公開資料なし） · `004e42fc`（命令位置の公開資料なし）

~~~diff
- 004e413c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 004e413c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e413c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 004e413c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e413c bytes c99643f9
+ 004e413c bytes c9be43f9
- 004e4274 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 004e4274 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e4274 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 004e4274 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e4274 bytes c99643f9
+ 004e4274 bytes c9be43f9
- 004e42fc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 004e42fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e42fc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 004e42fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e42fc bytes c99643f9
+ 004e42fc bytes c9be43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-004faf7907be0cc3fbb73de82317e8bf"></a>

### [`004e4494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e4494.md) → [`004e4494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4494.md) _ZNK5Botan11GeneralName7matchesERKNS_16X509_CertificateE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdccb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdccb0.md) · 呼出先 23件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`004e4bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e4bdc.md)
- 新版 呼出元 1件 [`00bdcd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd00.md) · 呼出先 23件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`0042e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`004e4bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4bdc.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.49% / 新版 95.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 9件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e4564",
      "incomplete_value": true,
      "site": "004e4564",
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
      "definition_site": "004e4564",
      "incomplete_value": true,
      "site": "004e4564",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e4564",
      "incomplete_value": true,
      "site": "004e4564",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:348:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e4564",
      "incomplete_value": true,
      "site": "004e4564",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f8:8"
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
      "definition_site": "004e45e4",
      "incomplete_value": true,
      "site": "004e45e4",
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
      "definition_site": "004e45e4",
      "incomplete_value": true,
      "site": "004e45e4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e4544",
      "READ",
      [
        "storage",
        "00c1b2f0",
        null,
        "pointer"
      ]
    ],
    [
      "004e4548",
      "READ",
      [
        "storage",
        "00c1b2f8",
        null,
        "pointer"
      ]
    ],
    [
      "004e4564",
      "DATA",
      [
        "storage",
        "00bed980",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "004e4544",
      "READ",
      [
        "storage",
        "00c1b340",
        null,
        "pointer"
      ]
    ],
    [
      "004e4548",
      "READ",
      [
        "storage",
        "00c1b348",
        null,
        "pointer"
      ]
    ],
    [
      "004e4564",
      "DATA",
      [
        "storage",
        "00bed9d0",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e4544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e4494.md#insn-004e4544) · [`004e4548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e4494.md#insn-004e4548) · [`004e45c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e4494.md#insn-004e45c8)
- 新版 `004e4544`（命令位置の公開資料なし） · `004e4548`（命令位置の公開資料なし） · `004e45c8`（命令位置の公開資料なし）

~~~diff
- 004e4544 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f0:8"]]
- 004e4544 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e4544 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:340:8"]]
+ 004e4544 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e4544 bytes 087941f9
+ 004e4544 bytes 08a141f9
- 004e4548 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2f8:8"]]
- 004e4548 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e4548 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:348:8"]]
+ 004e4548 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e4548 bytes 297d41f9
+ 004e4548 bytes 29a541f9
- 004e45c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f0:8"]]
- 004e45c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e45c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:340:8"]]
+ 004e45c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e45c8 bytes 087941f9
+ 004e45c8 bytes 08a141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43d9f19f7a9853c78e4f1ef7b6a2f720"></a>

### [`004e4bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e4bf4.md) → [`004e4bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4bf4.md) _ZNK5Botan11GeneralName11matches_dnsERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004e4494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e4494.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`004e4494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4494.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.49% / 新版 99.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e4d00",
      "incomplete_value": false,
      "site": "004e4d10",
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
            "const:7da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e4d00",
      "incomplete_value": false,
      "site": "004e4d10",
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
            "const:867:8"
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
      "004e4d00",
      "PARAM",
      [
        "storage",
        "00296867",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004e4d00",
      "PARAM",
      [
        "storage",
        "002967da",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e4d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e4bf4.md#insn-004e4d00)
- 新版 `004e4d00`（命令位置の公開資料なし）

~~~diff
- 004e4d00 ["COPY", "tmp:0:8", ["const:867:8"]]
- 004e4d00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004e4d00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004e4d00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004e4d00 ["COPY", "tmp:0:8", ["const:7da:8"]]
+ 004e4d00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004e4d00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004e4d00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004e4d00 bytes 009c2191
+ 004e4d00 bytes 00681f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b96cb5aca3bbcbb79a2082fe12e7e5b"></a>

### [`004e50d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e50d0.md) → [`004e50d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e50d0.md) _ZNK5Botan11GeneralName10matches_dnERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004e4494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e4494.md) · 呼出先 13件 [`004e56e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e56e4.md) [`004e5d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e5d50.md) [`005180b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/005180b8.md) [`00526790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00526/00526790.md) [`005267f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00526/005267f0.md)
- 新版 呼出元 1件 [`004e4494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4494.md) · 呼出先 13件 [`004e56e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e56e4.md) [`004e5d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5d50.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00526790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526790.md) [`005267f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005267f0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.66% / 新版 94.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e5140",
      "incomplete_value": true,
      "site": "004e5140",
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
      "definition_site": "004e5140",
      "incomplete_value": true,
      "site": "004e5140",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e514c",
      "incomplete_value": true,
      "site": "004e514c",
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
      "definition_site": "004e514c",
      "incomplete_value": true,
      "site": "004e514c",
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
      "definition_site": "004e533c",
      "incomplete_value": true,
      "site": "004e5344",
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
      "definition_site": "004e533c",
      "incomplete_value": true,
      "site": "004e5344",
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
    "ordinal": 30,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e5128",
      "READ",
      [
        "storage",
        "00c1b290",
        null,
        "pointer"
      ]
    ],
    [
      "004e5140",
      "DATA",
      [
        "storage",
        "00bea9e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e514c",
      "DATA",
      [
        "storage",
        "00bea9e8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004e5128",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "004e5140",
      "DATA",
      [
        "storage",
        "00beaa38",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e514c",
      "DATA",
      [
        "storage",
        "00beaa38",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e5128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e50d0.md#insn-004e5128) · [`004e5338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e50d0.md#insn-004e5338) · [`004e5354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e50d0.md#insn-004e5354)
- 新版 `004e5128`（命令位置の公開資料なし） · `004e5338`（命令位置の公開資料なし） · `004e5354`（命令位置の公開資料なし）

~~~diff
- 004e5128 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
- 004e5128 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e5128 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
+ 004e5128 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e5128 bytes 084941f9
+ 004e5128 bytes 087141f9
- 004e5338 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dd0:8"]]
- 004e5338 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e5338 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e20:8"]]
+ 004e5338 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 004e5338 bytes b5ea46f9
+ 004e5338 bytes b51247f9
- 004e5354 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
- 004e5354 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e5354 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 004e5354 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e5354 bytes 08c146f9
+ 004e5354 bytes 08e946f9
~~~


<a id="compare-aca58ad05c4853906b2368b654d5ca77"></a>

### [`004e548c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e548c.md) → [`004e548c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e548c.md) _ZNK5Botan11GeneralName10matches_ipERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `boundary_candidate`

- 旧版 呼出元 1件 [`004e4494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e4494.md) · 呼出先 12件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00463ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00463/00463ea0.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00524c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c98.md)
- 新版 呼出元 1件 [`004e4494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4494.md) · 呼出先 15件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md) [`00463ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463ea0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00524c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c94.md)

変更の種類 branch_condition_or_target, branch_count, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.35% / 新版 82.71%

CFGの説明率　旧版 96.55% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 4件, `call_argument_candidate` 1件, `call_count` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004e54c0",
      "incomplete_value": false,
      "site": "004e54c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e54c0",
      "incomplete_value": false,
      "site": "004e54c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "004e5654"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "004e5658"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e54c8",
      "DATA",
      [
        "storage",
        "00bed6a0",
        null,
        "undefined *"
      ]
    ],
    [
      "004e5510",
      "READ",
      [
        "storage",
        "00bed6c0",
        null,
        "pointer"
      ]
    ],
    [
      "004e5510",
      "READ",
      [
        "storage",
        "00bed6c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004e54c8",
      "DATA",
      [
        "storage",
        "00bed6f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004e5510",
      "READ",
      [
        "storage",
        "00bed710",
        null,
        "pointer"
      ]
    ],
    [
      "004e5510",
      "READ",
      [
        "storage",
        "00bed718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 新版 `004e5654`（命令位置の公開資料なし） · `004e5658`（命令位置の公開資料なし） · `004e5664`（命令位置の公開資料なし）

~~~diff
+ 004e5654 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 004e5654 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 004e5654 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 004e5654 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 004e5654 bytes 68000037
+ 004e5658 ["INT_NOTEQUAL", "tmp:0:1", ["register:40a8:4", "const:0:4"]]
+ 004e5658 ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
+ 004e5658 bytes f5000035
+ 004e5664 ["INT_ADD", "register:40f0:8", ["const:4e5664:8", "const:4:8"]]
+ 004e5664 ["CALL", null, ["callee:00bdb060:8"]]
+ 004e5664 bytes 7fd61b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5268aa572d31caeed98d1412c61bed75"></a>

### [`004e56e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e56e4.md) → [`004e56e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e56e4.md) FUN_004e56e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`004dcbd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dcbd4.md) [`004e50d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e50d0.md) · 呼出先 4件 [`00525380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/00525380.md) [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb350.md) [`00bdb590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb590.md)
- 新版 呼出元 2件 [`004dcbd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dcbd4.md) [`004e50d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e50d0.md) · 呼出先 4件 [`00525380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525380.md) [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3a0.md) [`00bdb5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb5e0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 78.08% / 新版 78.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e5734",
      "incomplete_value": true,
      "site": "004e5734",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e5734",
      "incomplete_value": true,
      "site": "004e5734",
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
            "const:68:8"
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
      "definition_site": "004e5738",
      "incomplete_value": true,
      "site": "004e5738",
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
      "definition_site": "004e5738",
      "incomplete_value": true,
      "site": "004e5738",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e5730",
      "incomplete_value": true,
      "site": "004e5740",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e5730",
      "incomplete_value": true,
      "site": "004e5740",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
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
      "004e570c",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "004e5718",
      "READ",
      [
        "storage",
        "00c1add0",
        null,
        "pointer"
      ]
    ],
    [
      "004e5730",
      "READ",
      [
        "storage",
        "00c13300",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004e570c",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "004e5718",
      "READ",
      [
        "storage",
        "00c1ae20",
        null,
        "pointer"
      ]
    ],
    [
      "004e5730",
      "READ",
      [
        "storage",
        "00c13350",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e570c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e56e4.md#insn-004e570c) · [`004e5714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e56e4.md#insn-004e5714)
- 新版 `004e570c`（命令位置の公開資料なし） · `004e5714`（命令位置の公開資料なし）

~~~diff
- 004e570c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:dd8:8"]]
- 004e570c ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e570c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:e28:8"]]
+ 004e570c ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 004e570c bytes 39ef46f9
+ 004e570c bytes 391747f9
- 004e5714 ["COPY", "register:40e0:8", ["register:4000:8"]]
- 004e5714 bytes fc0300aa
+ 004e5714 ["COPY", "register:40e0:8", ["register:4000:8"]]
+ 004e5714 bytes fc0300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e876233d270cc5836ae76b79d03195e3"></a>

### [`004e5850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e5850.md) → [`004e5850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5850.md) _ZN5BotanrsERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEERNS_7X509_DNE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcaf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcaf0.md) · 呼出先 12件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004f2498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f2498.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdcb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcb40.md) · 呼出先 12件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004f2498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f2498.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.02% / 新版 99.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e5b34",
      "incomplete_value": false,
      "site": "004e5b3c",
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
            "const:b43:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e5b34",
      "incomplete_value": false,
      "site": "004e5b3c",
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
            "const:bd0:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e5b6c",
      "incomplete_value": true,
      "site": "004e5b78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e5b6c",
      "incomplete_value": true,
      "site": "004e5b78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e5b34",
      "PARAM",
      [
        "storage",
        "00296bd0",
        null,
        "string"
      ]
    ],
    [
      "004e5b6c",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004e5b6c",
      "PARAM",
      [
        "storage",
        "00be9298",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e5b34",
      "PARAM",
      [
        "storage",
        "00296b43",
        null,
        "string"
      ]
    ],
    [
      "004e5b6c",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "004e5b6c",
      "PARAM",
      [
        "storage",
        "00be92e8",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e5b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e5850.md#insn-004e5b34) · [`004e5b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e5850.md#insn-004e5b6c)
- 新版 `004e5b34`（命令位置の公開資料なし） · `004e5b6c`（命令位置の公開資料なし）

~~~diff
- 004e5b34 ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 004e5b34 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004e5b34 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004e5b34 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004e5b34 ["COPY", "tmp:0:8", ["const:b43:8"]]
+ 004e5b34 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004e5b34 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004e5b34 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004e5b34 bytes 21402f91
+ 004e5b34 bytes 210c2d91
- 004e5b6c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 004e5b6c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e5b6c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004e5b6c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e5b6c bytes 217847f9
+ 004e5b6c bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a86fbf4c840e0c5fa521b5ccbc26a08"></a>

### [`004e5d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e5d50.md) → [`004e5d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5d50.md) FUN_004e5d50

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004e50d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e50d0.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`004e50d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e50d0.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e5d88",
      "incomplete_value": true,
      "site": "004e5d8c",
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
      "definition_site": "004e5d88",
      "incomplete_value": true,
      "site": "004e5d8c",
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
      "004e5d78",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "004e5d8c",
      "DATA",
      [
        "storage",
        "00be9278",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004e5d78",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "004e5d8c",
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e5d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e5d50.md#insn-004e5d78)
- 新版 `004e5d78`（命令位置の公開資料なし）

~~~diff
- 004e5d78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
- 004e5d78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e5d78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
+ 004e5d78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e5d78 bytes 088147f9
+ 004e5d78 bytes 08a947f9
~~~


<a id="compare-e38dd751ea4c392cfa5d86be3c6b8397"></a>

### [`004e5e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e5e70.md) → [`004e5e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5e70.md) _ZN5Botan14GeneralSubtreeC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.63% / 新版 96.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e5ec0",
      "incomplete_value": true,
      "site": "004e5ec0",
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
      "definition_site": "004e5ec0",
      "incomplete_value": true,
      "site": "004e5ec0",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e5ec0",
      "incomplete_value": true,
      "site": "004e5ec0",
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
      "definition_site": "004e5ec0",
      "incomplete_value": true,
      "site": "004e5ec0",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e6164",
      "incomplete_value": false,
      "site": "004e616c",
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
            "const:6af:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e6164",
      "incomplete_value": false,
      "site": "004e616c",
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
            "const:624:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e5e9c",
      "READ",
      [
        "storage",
        "00c1b310",
        null,
        "pointer"
      ]
    ],
    [
      "004e5ea4",
      "READ",
      [
        "storage",
        "00c1b2e8",
        null,
        "pointer"
      ]
    ],
    [
      "004e5ec0",
      "DATA",
      [
        "storage",
        "00beb108",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004e5e9c",
      "READ",
      [
        "storage",
        "00c1b360",
        null,
        "pointer"
      ]
    ],
    [
      "004e5ea4",
      "READ",
      [
        "storage",
        "00c1b338",
        null,
        "pointer"
      ]
    ],
    [
      "004e5ec0",
      "DATA",
      [
        "storage",
        "00beb158",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e5e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e5e70.md#insn-004e5e9c) · [`004e5ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e5e70.md#insn-004e5ea4) · [`004e6164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e5e70.md#insn-004e6164)
- 新版 `004e5e9c`（命令位置の公開資料なし） · `004e5ea4`（命令位置の公開資料なし） · `004e6164`（命令位置の公開資料なし）

~~~diff
- 004e5e9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:310:8"]]
- 004e5e9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e5e9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:360:8"]]
+ 004e5e9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e5e9c bytes 088941f9
+ 004e5e9c bytes 08b141f9
- 004e5ea4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:2e8:8"]]
- 004e5ea4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e5ea4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:338:8"]]
+ 004e5ea4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004e5ea4 bytes 4a7541f9
+ 004e5ea4 bytes 4a9d41f9
- 004e6164 ["COPY", "tmp:0:8", ["const:624:8"]]
- 004e6164 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004e6164 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004e6164 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004e6164 ["COPY", "tmp:0:8", ["const:6af:8"]]
+ 004e6164 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004e6164 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004e6164 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004e6164 bytes 21901891
+ 004e6164 bytes 21bc1a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05dcfff7a737d1eec77c494ef343842f"></a>

### [`004e6294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6294.md) → [`004e6294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6294.md) _ZNK5Botan14GeneralSubtree11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e62d4",
      "incomplete_value": true,
      "site": "004e62e8",
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
                "const:292000:8"
              ],
              [
                "leaf",
                "const:890:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e62d4",
      "incomplete_value": true,
      "site": "004e62e8",
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
                "const:292000:8"
              ],
              [
                "leaf",
                "const:91d:8"
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
      "definition_site": "004e62d8",
      "incomplete_value": true,
      "site": "004e62ec",
      "value": [
        "LOAD",
        "8",
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e62d8",
      "incomplete_value": true,
      "site": "004e62ec",
      "value": [
        "LOAD",
        "8",
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
                "const:10:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e6320",
      "incomplete_value": true,
      "site": "004e632c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e6320",
      "incomplete_value": true,
      "site": "004e632c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:190:8"
              ]
            ]
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
      "004e62d4",
      "READ",
      [
        "storage",
        "0029291d",
        null,
        "string"
      ]
    ],
    [
      "004e62d8",
      "READ",
      [
        "storage",
        "0029292d",
        null,
        "string"
      ]
    ],
    [
      "004e6320",
      "READ",
      [
        "storage",
        "00c1b190",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e62d4",
      "READ",
      [
        "storage",
        "00292890",
        null,
        "string"
      ]
    ],
    [
      "004e62d8",
      "READ",
      [
        "storage",
        "002928a0",
        null,
        "string"
      ]
    ],
    [
      "004e6320",
      "READ",
      [
        "storage",
        "00c1b1e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e62cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6294.md#insn-004e62cc) · [`004e62d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6294.md#insn-004e62d0)
- 新版 `004e62cc`（命令位置の公開資料なし） · `004e62d0`（命令位置の公開資料なし）

~~~diff
- 004e62cc ["COPY", "tmp:0:8", ["const:91d:8"]]
- 004e62cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004e62cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004e62cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004e62cc ["COPY", "tmp:0:8", ["const:890:8"]]
+ 004e62cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004e62cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004e62cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004e62cc bytes 08752491
+ 004e62cc bytes 08412291
- 004e62d0 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 004e62d0 bytes 49eeffd0
+ 004e62d0 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 004e62d0 bytes 49eeffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6ed7902bc5aaac32d6fa849e8c3261f"></a>

### [`004e637c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e637c.md) → [`004e637c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e637c.md) _ZN5Botan14GeneralSubtree11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdccf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdccf0.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdcd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd40.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.53% / 新版 97.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e6424",
      "incomplete_value": true,
      "site": "004e6424",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
      "definition_site": "004e6424",
      "incomplete_value": true,
      "site": "004e6424",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e6474",
      "incomplete_value": false,
      "site": "004e647c",
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
            "const:e22:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e6474",
      "incomplete_value": false,
      "site": "004e647c",
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
            "const:eaf:8"
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
      "definition_site": "004e64ac",
      "incomplete_value": true,
      "site": "004e64b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e64ac",
      "incomplete_value": true,
      "site": "004e64b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
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
      "004e6414",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004e6474",
      "PARAM",
      [
        "storage",
        "00298eaf",
        null,
        "string"
      ]
    ],
    [
      "004e64ac",
      "READ",
      [
        "storage",
        "00c1af10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e6414",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004e6474",
      "PARAM",
      [
        "storage",
        "00298e22",
        null,
        "string"
      ]
    ],
    [
      "004e64ac",
      "READ",
      [
        "storage",
        "00c1af60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e637c.md#insn-004e6414) · [`004e6474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e637c.md#insn-004e6474) · [`004e64ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e637c.md#insn-004e64ac)
- 新版 `004e6414`（命令位置の公開資料なし） · `004e6474`（命令位置の公開資料なし） · `004e64ac`（命令位置の公開資料なし）

~~~diff
- 004e6414 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004e6414 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e6414 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004e6414 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e6414 bytes 299543f9
+ 004e6414 bytes 29bd43f9
- 004e6474 ["COPY", "tmp:0:8", ["const:eaf:8"]]
- 004e6474 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004e6474 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004e6474 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004e6474 ["COPY", "tmp:0:8", ["const:e22:8"]]
+ 004e6474 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004e6474 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004e6474 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004e6474 bytes 21bc3a91
+ 004e6474 bytes 21883891
- 004e64ac ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
- 004e64ac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e64ac ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f60:8"]]
+ 004e64ac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e64ac bytes 218847f9
+ 004e64ac bytes 21b047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86d88718042e904b75b8478d2f5d8116"></a>

### [`004e6520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6520.md) → [`004e6520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6520.md) FUN_004e6520

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004f7f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f7f54.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb360.md)
- 新版 呼出元 1件 [`004f7f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7f54.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.47% / 新版 92.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e658c",
      "incomplete_value": true,
      "site": "004e6590",
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
      "definition_site": "004e658c",
      "incomplete_value": true,
      "site": "004e6590",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e655c",
      "incomplete_value": false,
      "site": "004e6560",
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
            "const:ab6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e655c",
      "incomplete_value": false,
      "site": "004e6560",
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
            "const:b43:8"
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
      "definition_site": "004e6618",
      "incomplete_value": false,
      "site": "004e6620",
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
            "const:3cd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e6618",
      "incomplete_value": false,
      "site": "004e6620",
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
            "const:342:8"
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
      "004e655c",
      "PARAM",
      [
        "storage",
        "00299b43",
        null,
        null
      ]
    ],
    [
      "004e656c",
      "PARAM",
      [
        "storage",
        "00299b43",
        null,
        null
      ]
    ],
    [
      "004e6584",
      "READ",
      [
        "storage",
        "00c1b2e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e655c",
      "PARAM",
      [
        "storage",
        "00299ab6",
        null,
        null
      ]
    ],
    [
      "004e656c",
      "PARAM",
      [
        "storage",
        "00299ab6",
        null,
        null
      ]
    ],
    [
      "004e6584",
      "READ",
      [
        "storage",
        "00c1b338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6520.md#insn-004e6554) · [`004e6558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6520.md#insn-004e6558)
- 新版 `004e6554`（命令位置の公開資料なし） · `004e6558`（命令位置の公開資料なし）

~~~diff
- 004e6554 ["COPY", "tmp:0:8", ["const:b43:8"]]
- 004e6554 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 004e6554 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 004e6554 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 004e6554 ["COPY", "tmp:0:8", ["const:ab6:8"]]
+ 004e6554 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 004e6554 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 004e6554 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 004e6554 bytes b50e2d91
+ 004e6554 bytes b5da2a91
- 004e6558 ["COPY", "register:4010:8", ["const:1:8"]]
- 004e6558 bytes 22008052
+ 004e6558 ["COPY", "register:4010:8", ["const:1:8"]]
+ 004e6558 bytes 22008052
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-912711df4b57e348436effc20d8bed39"></a>

### [`004e66d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e66d0.md) → [`004e66d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e66d0.md) _ZN5Botan4OCSP7RequestC1ERKNS_16X509_CertificateES4_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00518128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/00518128.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00518128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518128.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e670c",
      "incomplete_value": true,
      "site": "004e6710",
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
      "definition_site": "004e670c",
      "incomplete_value": true,
      "site": "004e6710",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e6790",
      "incomplete_value": true,
      "site": "004e6790",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
      "definition_site": "004e6790",
      "incomplete_value": true,
      "site": "004e6790",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e67fc",
      "incomplete_value": false,
      "site": "004e6804",
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
            "const:5b3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e67fc",
      "incomplete_value": false,
      "site": "004e6804",
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
            "const:528:8"
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
      "004e6708",
      "READ",
      [
        "storage",
        "00c1b2a0",
        null,
        "pointer"
      ]
    ],
    [
      "004e6710",
      "DATA",
      [
        "storage",
        "00beaa78",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "004e6780",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e6708",
      "READ",
      [
        "storage",
        "00c1b2f0",
        null,
        "pointer"
      ]
    ],
    [
      "004e6710",
      "DATA",
      [
        "storage",
        "00beaac8",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "004e6780",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e66d0.md#insn-004e6708) · [`004e6780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e66d0.md#insn-004e6780) · [`004e67fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e66d0.md#insn-004e67fc)
- 新版 `004e6708`（命令位置の公開資料なし） · `004e6780`（命令位置の公開資料なし） · `004e67fc`（命令位置の公開資料なし）

~~~diff
- 004e6708 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
- 004e6708 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e6708 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f0:8"]]
+ 004e6708 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e6708 bytes 085141f9
+ 004e6708 bytes 087941f9
- 004e6780 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004e6780 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e6780 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004e6780 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e6780 bytes 299543f9
+ 004e6780 bytes 29bd43f9
- 004e67fc ["COPY", "tmp:0:8", ["const:528:8"]]
- 004e67fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004e67fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004e67fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004e67fc ["COPY", "tmp:0:8", ["const:5b3:8"]]
+ 004e67fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004e67fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004e67fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004e67fc bytes 21a01491
+ 004e67fc bytes 21cc1691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8bf2da1b82ba3d321e591e97ceaddaf"></a>

### [`004e697c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e697c.md) → [`004e697c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e697c.md) FUN_004e697c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

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
      "definition_site": "004e6998",
      "incomplete_value": true,
      "site": "004e699c",
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
      "definition_site": "004e6998",
      "incomplete_value": true,
      "site": "004e699c",
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
      "definition_site": "004e69d8",
      "incomplete_value": true,
      "site": "004e69dc",
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
      "definition_site": "004e69d8",
      "incomplete_value": true,
      "site": "004e69dc",
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
      "004e6990",
      "READ",
      [
        "storage",
        "00c1b2a0",
        null,
        "pointer"
      ]
    ],
    [
      "004e699c",
      "DATA",
      [
        "storage",
        "00beaa78",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "004e69d0",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e6990",
      "READ",
      [
        "storage",
        "00c1b2f0",
        null,
        "pointer"
      ]
    ],
    [
      "004e699c",
      "DATA",
      [
        "storage",
        "00beaac8",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "004e69d0",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e697c.md#insn-004e6990) · [`004e69d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e697c.md#insn-004e69d0)
- 新版 `004e6990`（命令位置の公開資料なし） · `004e69d0`（命令位置の公開資料なし）

~~~diff
- 004e6990 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
- 004e6990 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e6990 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f0:8"]]
+ 004e6990 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e6990 bytes 085141f9
+ 004e6990 bytes 087941f9
- 004e69d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 004e69d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e69d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
+ 004e69d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e69d0 bytes 088d41f9
+ 004e69d0 bytes 08b541f9
~~~


<a id="compare-904e040e2a3dc7ac576cdee6f3c8cc7b"></a>

### [`004e6aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6aac.md) → [`004e6aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6aac.md) _ZNK5Botan4OCSP7Request10BER_encodeEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd10.md) · 呼出先 10件 [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 1件 [`00bdcd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd60.md) · 呼出先 10件 [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e6b58",
      "incomplete_value": true,
      "site": "004e6b58",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e6b58",
      "incomplete_value": true,
      "site": "004e6b58",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e6c2c",
      "incomplete_value": true,
      "site": "004e6c2c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e6c2c",
      "incomplete_value": true,
      "site": "004e6c2c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e6b48",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004e6c1c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e6b48",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004e6c1c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6aac.md#insn-004e6b48) · [`004e6c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6aac.md#insn-004e6c1c)
- 新版 `004e6b48`（命令位置の公開資料なし） · `004e6c1c`（命令位置の公開資料なし）

~~~diff
- 004e6b48 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 004e6b48 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e6b48 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 004e6b48 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e6b48 bytes e99643f9
+ 004e6b48 bytes e9be43f9
- 004e6c1c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 004e6c1c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e6c1c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 004e6c1c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e6c1c bytes e99643f9
+ 004e6c1c bytes e9be43f9
~~~


<a id="compare-b0ae3d24e28b49654d1370e4a181ce0e"></a>

### [`004e6d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6d3c.md) → [`004e6d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6d3c.md) _ZN5Botan4OCSP8ResponseC2EPKhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 41件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`004828a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/004828a4.md) [`00482aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482aa8.md) [`0048bb9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bb9c.md) [`004e7aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e7/004e7aa4.md)
- 新版 呼出元 0件  · 呼出先 41件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`004828a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004828a4.md) [`00482aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482aa8.md) [`0048bb9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bb9c.md) [`004e7aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7aa4.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.21% / 新版 95.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 9件

アドレスに依存する影響 `call_target` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e6dc4",
      "incomplete_value": true,
      "site": "004e6dc4",
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
      "definition_site": "004e6dc4",
      "incomplete_value": true,
      "site": "004e6dc4",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e6dec",
      "incomplete_value": true,
      "site": "004e6dec",
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
      "definition_site": "004e6dec",
      "incomplete_value": true,
      "site": "004e6dec",
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
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e6e18",
      "incomplete_value": true,
      "site": "004e6e18",
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
      "definition_site": "004e6e18",
      "incomplete_value": true,
      "site": "004e6e18",
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
      "004e6db8",
      "READ",
      [
        "storage",
        "00c1af70",
        null,
        "pointer"
      ]
    ],
    [
      "004e6dc4",
      "DATA",
      [
        "storage",
        "00be9368",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e6dd4",
      "READ",
      [
        "storage",
        "00c1b290",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e6db8",
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ],
    [
      "004e6dc4",
      "DATA",
      [
        "storage",
        "00be93b8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e6dd4",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6d3c.md#insn-004e6db8) · [`004e6dd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6d3c.md#insn-004e6dd4) · [`004e6de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6d3c.md#insn-004e6de4)
- 新版 `004e6db8`（命令位置の公開資料なし） · `004e6dd4`（命令位置の公開資料なし）

~~~diff
- 004e6db8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f70:8"]]
- 004e6db8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e6db8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fc0:8"]]
+ 004e6db8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e6db8 bytes 08b947f9
+ 004e6db8 bytes 08e147f9
- 004e6dd4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:290:8"]]
- 004e6dd4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e6dd4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2e0:8"]]
+ 004e6dd4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e6dd4 bytes 294941f9
+ 004e6dd4 bytes 297141f9
- 004e6de4 ["COPY", "register:4048:8", ["register:40a0:8"]]
- 004e6de4 bytes e90314aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a617007ed0f7e007354b517e06a904c"></a>

### [`004e7aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e7/004e7aa4.md) → [`004e7aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7aa4.md) FUN_004e7aa4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004e6d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6d3c.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`004e6d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6d3c.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

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
      "definition_site": "004e7bac",
      "incomplete_value": true,
      "site": "004e7bb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e7bac",
      "incomplete_value": true,
      "site": "004e7bb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
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
      "004e7bac",
      "READ",
      [
        "storage",
        "00c1af10",
        null,
        "pointer"
      ]
    ],
    [
      "004e7bac",
      "PARAM",
      [
        "storage",
        "00be92b0",
        "_ZTIN5Botan14Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e7bac",
      "READ",
      [
        "storage",
        "00c1af60",
        null,
        "pointer"
      ]
    ],
    [
      "004e7bac",
      "PARAM",
      [
        "storage",
        "00be9300",
        "_ZTIN5Botan14Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e7bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e7/004e7aa4.md#insn-004e7bac)
- 新版 `004e7bac`（命令位置の公開資料なし）

~~~diff
- 004e7bac ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
- 004e7bac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e7bac ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f60:8"]]
+ 004e7bac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e7bac bytes 218847f9
+ 004e7bac bytes 21b047f9
~~~


<a id="compare-dcc8a137d35b7b2ac423854a79376aa0"></a>

### [`004e7fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e7/004e7fa0.md) → [`004e7fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7fa0.md) _ZN5Botan11BER_Decoder11decode_listINS_4OCSP14SingleResponseEEERS0_RNSt6__ndk16vectorIT_NS5_9allocatorIS7_EEEENS_8ASN1_TagESC_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdcd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd40.md) · 呼出先 10件 [`004e9fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e9fdc.md) [`005269b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00526/005269b0.md) [`00526bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00526/00526bb4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdcd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd90.md) · 呼出先 10件 [`004e9fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9fdc.md) [`005269b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005269b0.md) [`00526bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526bb4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.53% / 新版 90.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e80e4",
      "incomplete_value": true,
      "site": "004e80e4",
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
      "definition_site": "004e80e4",
      "incomplete_value": true,
      "site": "004e80e4",
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
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e8104",
      "incomplete_value": true,
      "site": "004e8104",
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
      "definition_site": "004e8104",
      "incomplete_value": true,
      "site": "004e8104",
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
    "ordinal": 39,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e8100",
      "incomplete_value": true,
      "site": "004e8110",
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
      "definition_site": "004e8100",
      "incomplete_value": true,
      "site": "004e8110",
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
      "004e7ff4",
      "READ",
      [
        "storage",
        "00c1b320",
        null,
        "pointer"
      ]
    ],
    [
      "004e7ff8",
      "READ",
      [
        "storage",
        "00c1b328",
        null,
        "pointer"
      ]
    ],
    [
      "004e7ffc",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e7ff4",
      "READ",
      [
        "storage",
        "00c1b370",
        null,
        "pointer"
      ]
    ],
    [
      "004e7ff8",
      "READ",
      [
        "storage",
        "00c1b378",
        null,
        "pointer"
      ]
    ],
    [
      "004e7ffc",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e7ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e7/004e7fa0.md#insn-004e7ff4) · [`004e7ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e7/004e7fa0.md#insn-004e7ff8) · [`004e7ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e7/004e7fa0.md#insn-004e7ffc)
- 新版 `004e7ff4`（命令位置の公開資料なし） · `004e7ff8`（命令位置の公開資料なし） · `004e7ffc`（命令位置の公開資料なし）

~~~diff
- 004e7ff4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:320:8"]]
- 004e7ff4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e7ff4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:370:8"]]
+ 004e7ff4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004e7ff4 bytes 4a9141f9
+ 004e7ff4 bytes 4ab941f9
- 004e7ff8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:328:8"]]
- 004e7ff8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e7ff8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:378:8"]]
+ 004e7ff8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e7ff8 bytes 089541f9
+ 004e7ff8 bytes 08bd41f9
- 004e7ffc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ef8:8"]]
- 004e7ffc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e7ffc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f48:8"]]
+ 004e7ffc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e7ffc bytes 297d47f9
+ 004e7ffc bytes 29a547f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab445d01ad8f635190e545b5a6ab930b"></a>

### [`004e85ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e85ec.md) → [`004e85ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e85ec.md) _ZNK5Botan4OCSP8Response16verify_signatureERKNS_16X509_CertificateE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd60.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00483d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483d44.md) [`00524c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c3c.md) [`00524c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c98.md)
- 新版 呼出元 1件 [`00bdcdb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcdb0.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00483d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483d44.md) [`00524c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c3c.md) [`00524c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c98.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.95% / 新版 98.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004e863c",
      "incomplete_value": false,
      "site": "004e863c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e863c",
      "incomplete_value": false,
      "site": "004e863c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "004e863c",
      "DATA",
      [
        "storage",
        "00bed6a0",
        null,
        "undefined *"
      ]
    ],
    [
      "004e8680",
      "READ",
      [
        "storage",
        "00bed6c0",
        null,
        "pointer"
      ]
    ],
    [
      "004e8680",
      "READ",
      [
        "storage",
        "00bed6c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004e863c",
      "DATA",
      [
        "storage",
        "00bed6f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004e8680",
      "READ",
      [
        "storage",
        "00bed710",
        null,
        "pointer"
      ]
    ],
    [
      "004e8680",
      "READ",
      [
        "storage",
        "00bed718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e8634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e85ec.md#insn-004e8634)
- 新版 `004e8634`（命令位置の公開資料なし）

~~~diff
- 004e8634 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 004e8634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004e8634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004e8634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004e8634 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 004e8634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004e8634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004e8634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004e8634 bytes 08811a91
+ 004e8634 bytes 08c11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7808bab6ffe2af68b87f2e1409ce382c"></a>

### [`004e8a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e8a14.md) → [`004e8a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8a14.md) _ZNK5Botan4OCSP8Response15check_signatureERKNSt6__ndk16vectorIPNS_17Certificate_StoreENS2_9allocatorIS5_EEEERKNS3_INS2_10shared_ptrIKNS_16X5

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd80.md) · 呼出先 13件 [`00518128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/00518128.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00bdcdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcdd0.md) · 呼出先 13件 [`00518128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518128.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.35% / 新版 97.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e8d18",
      "incomplete_value": true,
      "site": "004e8d24",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:40d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e8d18",
      "incomplete_value": true,
      "site": "004e8d24",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:382:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e8eac",
      "incomplete_value": true,
      "site": "004e8eb0",
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
      "definition_site": "004e8eac",
      "incomplete_value": true,
      "site": "004e8eb0",
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
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e8ee0",
      "incomplete_value": true,
      "site": "004e8ee4",
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
      "definition_site": "004e8ee0",
      "incomplete_value": true,
      "site": "004e8ee4",
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
    "ordinal": 31,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e8d18",
      "READ",
      [
        "storage",
        "002a4382",
        null,
        "string"
      ]
    ],
    [
      "004e8ea4",
      "READ",
      [
        "storage",
        "00c1b298",
        null,
        "pointer"
      ]
    ],
    [
      "004e8eb0",
      "DATA",
      [
        "storage",
        "00bed730",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "004e8d18",
      "READ",
      [
        "storage",
        "002a440d",
        null,
        "string"
      ]
    ],
    [
      "004e8ea4",
      "READ",
      [
        "storage",
        "00c1b2e8",
        null,
        "pointer"
      ]
    ],
    [
      "004e8eb0",
      "DATA",
      [
        "storage",
        "00bed780",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e8d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e8a14.md#insn-004e8d10) · [`004e8ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e8a14.md#insn-004e8ea4) · [`004e8ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e8a14.md#insn-004e8ed8)
- 新版 `004e8d10`（命令位置の公開資料なし） · `004e8ea4`（命令位置の公開資料なし） · `004e8ed8`（命令位置の公開資料なし）

~~~diff
- 004e8d10 ["COPY", "tmp:0:8", ["const:382:8"]]
- 004e8d10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004e8d10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004e8d10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004e8d10 ["COPY", "tmp:0:8", ["const:40d:8"]]
+ 004e8d10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004e8d10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004e8d10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004e8d10 bytes 29090e91
+ 004e8d10 bytes 29351091
- 004e8ea4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:298:8"]]
- 004e8ea4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e8ea4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e8:8"]]
+ 004e8ea4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e8ea4 bytes 084d41f9
+ 004e8ea4 bytes 087541f9
- 004e8ed8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:298:8"]]
- 004e8ed8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e8ed8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e8:8"]]
+ 004e8ed8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e8ed8 bytes 084d41f9
+ 004e8ed8 bytes 087541f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1ba4e06bc855ee36e6ab735056d144e"></a>

### [`004e8fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e8fec.md) → [`004e8fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8fec.md) _ZNK5Botan16X509_Certificate33subject_public_key_bitstring_sha1Ev

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd90.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdcde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcde0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e9064",
      "incomplete_value": false,
      "site": "004e906c",
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
            "const:b4b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e9064",
      "incomplete_value": false,
      "site": "004e906c",
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
            "const:bdf:8"
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
      "definition_site": "004e90a0",
      "incomplete_value": true,
      "site": "004e90ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e90a0",
      "incomplete_value": true,
      "site": "004e90ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
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
      "004e9064",
      "PARAM",
      [
        "storage",
        "002afbdf",
        null,
        "string"
      ]
    ],
    [
      "004e90a0",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "004e90a0",
      "PARAM",
      [
        "storage",
        "00be92e0",
        "_ZTIN5Botan14Encoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e9064",
      "PARAM",
      [
        "storage",
        "002afb4b",
        null,
        "string"
      ]
    ],
    [
      "004e90a0",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "004e90a0",
      "PARAM",
      [
        "storage",
        "00be9330",
        "_ZTIN5Botan14Encoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e9064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e8fec.md#insn-004e9064) · [`004e90a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e8fec.md#insn-004e90a0)
- 新版 `004e9064`（命令位置の公開資料なし） · `004e90a0`（命令位置の公開資料なし）

~~~diff
- 004e9064 ["COPY", "tmp:0:8", ["const:bdf:8"]]
- 004e9064 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004e9064 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004e9064 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004e9064 ["COPY", "tmp:0:8", ["const:b4b:8"]]
+ 004e9064 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004e9064 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004e9064 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004e9064 bytes 217c2f91
+ 004e9064 bytes 212c2d91
- 004e90a0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
- 004e90a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e90a0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
+ 004e90a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e90a0 bytes 21ac47f9
+ 004e90a0 bytes 21d447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64f2226cdc09ac96f7a1d40626e5bf30"></a>

### [`004e9260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e9260.md) → [`004e9260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9260.md) _ZNK5Botan4OCSP8Response10status_forERKNS_16X509_CertificateES4_NSt6__ndk16chrono10time_pointINS6_12system_clockENS6_8durationIxNS5_5ratioIL

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcdb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcdb0.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdbb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb40.md) [`00bdcbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcbd0.md) [`00bdcdc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcdc0.md)
- 新版 呼出元 1件 [`00bdce00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce00.md) · 呼出先 4件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb90.md) [`00bdcc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc20.md) [`00bdce10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce10.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e9320",
      "incomplete_value": true,
      "site": "004e9328",
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
      "definition_site": "004e9320",
      "incomplete_value": true,
      "site": "004e9328",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e9314",
      "READ",
      [
        "storage",
        "00c1af70",
        null,
        "pointer"
      ]
    ],
    [
      "004e9328",
      "DATA",
      [
        "storage",
        "00be9368",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e9364",
      "DATA",
      [
        "storage",
        "00be9368",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004e9314",
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ],
    [
      "004e9328",
      "DATA",
      [
        "storage",
        "00be93b8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e9364",
      "DATA",
      [
        "storage",
        "00be93b8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e9314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e9260.md#insn-004e9314)
- 新版 `004e9314`（命令位置の公開資料なし）

~~~diff
- 004e9314 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f70:8"]]
- 004e9314 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e9314 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fc0:8"]]
+ 004e9314 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 004e9314 bytes 73ba47f9
+ 004e9314 bytes 73e247f9
~~~


<a id="compare-5d1807b8fe7f5d2eca07292d9a4e7e23"></a>

### [`004e97e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e97e0.md) → [`004e97e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e97e0.md) _ZN5Botan4OCSP6CertIDC1ERKNS_16X509_CertificateERKNS_6BigIntE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdcd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd00.md) · 呼出先 14件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00520804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520804.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00bdcd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd50.md) · 呼出先 14件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00520804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e982c",
      "incomplete_value": true,
      "site": "004e9838",
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
      "definition_site": "004e982c",
      "incomplete_value": true,
      "site": "004e9838",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e983c",
      "incomplete_value": true,
      "site": "004e983c",
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
      "definition_site": "004e983c",
      "incomplete_value": true,
      "site": "004e983c",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e9a70",
      "incomplete_value": true,
      "site": "004e9a70",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e9a70",
      "incomplete_value": true,
      "site": "004e9a70",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e981c",
      "READ",
      [
        "storage",
        "00c1b328",
        null,
        "pointer"
      ]
    ],
    [
      "004e9820",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004e9838",
      "DATA",
      [
        "storage",
        "00bea808",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004e981c",
      "READ",
      [
        "storage",
        "00c1b378",
        null,
        "pointer"
      ]
    ],
    [
      "004e9820",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004e9838",
      "DATA",
      [
        "storage",
        "00bea858",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e981c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e97e0.md#insn-004e981c) · [`004e9820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e97e0.md#insn-004e9820) · [`004e9824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e97e0.md#insn-004e9824)
- 新版 `004e981c`（命令位置の公開資料なし） · `004e9820`（命令位置の公開資料なし）

~~~diff
- 004e981c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:328:8"]]
- 004e981c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e981c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:378:8"]]
+ 004e981c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e981c bytes 299541f9
+ 004e981c bytes 29bd41f9
- 004e9820 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
- 004e9820 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e9820 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:f48:8"]]
+ 004e9820 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004e9820 bytes 4a7d47f9
+ 004e9820 bytes 4aa547f9
- 004e9824 ["COPY", "register:4098:8", ["register:4000:8"]]
- 004e9824 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33b26e12c556bb58af981c3824e4c6a1"></a>

### [`004e9ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e9ef4.md) → [`004e9ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9ef4.md) _ZNK5Botan4OCSP14SingleResponse11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e9f34",
      "incomplete_value": true,
      "site": "004e9f48",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:b13:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e9f34",
      "incomplete_value": true,
      "site": "004e9f48",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:ba7:8"
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
      "definition_site": "004e9f38",
      "incomplete_value": true,
      "site": "004e9f4c",
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
              "INT_ADD",
              [
                "leaf",
                "const:b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e9f38",
      "incomplete_value": true,
      "site": "004e9f4c",
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
              "INT_ADD",
              [
                "leaf",
                "const:b:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e9f80",
      "incomplete_value": true,
      "site": "004e9f8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e9f80",
      "incomplete_value": true,
      "site": "004e9f8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:190:8"
              ]
            ]
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
      "004e9f34",
      "READ",
      [
        "storage",
        "002afba7",
        null,
        "string"
      ]
    ],
    [
      "004e9f38",
      "READ",
      [
        "storage",
        "002afbb2",
        null,
        "string"
      ]
    ],
    [
      "004e9f80",
      "READ",
      [
        "storage",
        "00c1b190",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e9f34",
      "READ",
      [
        "storage",
        "002afb13",
        null,
        "string"
      ]
    ],
    [
      "004e9f38",
      "READ",
      [
        "storage",
        "002afb1e",
        null,
        "string"
      ]
    ],
    [
      "004e9f80",
      "READ",
      [
        "storage",
        "00c1b1e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e9f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e9ef4.md#insn-004e9f2c) · [`004e9f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e9ef4.md#insn-004e9f30)
- 新版 `004e9f2c`（命令位置の公開資料なし） · `004e9f30`（命令位置の公開資料なし）

~~~diff
- 004e9f2c ["COPY", "tmp:0:8", ["const:ba7:8"]]
- 004e9f2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004e9f2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004e9f2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004e9f2c ["COPY", "tmp:0:8", ["const:b13:8"]]
+ 004e9f2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004e9f2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004e9f2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004e9f2c bytes 089d2e91
+ 004e9f2c bytes 084d2c91
- 004e9f30 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 004e9f30 bytes 49eeff90
+ 004e9f30 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 004e9f30 bytes 49eeff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79705eeadc6586d56f7898d6c8c4733e"></a>

### [`004e9fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e9fdc.md) → [`004e9fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9fdc.md) _ZN5Botan4OCSP14SingleResponse11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004e7fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e7/004e7fa0.md) · 呼出先 10件 [`0051854c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/0051854c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb860.md)
- 新版 呼出元 1件 [`004e7fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7fa0.md) · 呼出先 10件 [`0051854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8b0.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.97% / 新版 94.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ea024",
      "incomplete_value": true,
      "site": "004ea024",
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
      "definition_site": "004ea024",
      "incomplete_value": true,
      "site": "004ea024",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ea0ac",
      "incomplete_value": true,
      "site": "004ea0ac",
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
      "definition_site": "004ea0ac",
      "incomplete_value": true,
      "site": "004ea0ac",
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
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ea194",
      "incomplete_value": true,
      "site": "004ea194",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ea194",
      "incomplete_value": true,
      "site": "004ea194",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ea010",
      "READ",
      [
        "storage",
        "00c1b2d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea024",
      "DATA",
      [
        "storage",
        "00beb8b0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ea09c",
      "READ",
      [
        "storage",
        "00c1af70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ea010",
      "READ",
      [
        "storage",
        "00c1b320",
        null,
        "pointer"
      ]
    ],
    [
      "004ea024",
      "DATA",
      [
        "storage",
        "00beb900",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ea09c",
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ea010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e9fdc.md#insn-004ea010) · [`004ea09c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e9fdc.md#insn-004ea09c) · [`004ea184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e9fdc.md#insn-004ea184)
- 新版 `004ea010`（命令位置の公開資料なし） · `004ea09c`（命令位置の公開資料なし） · `004ea184`（命令位置の公開資料なし）

~~~diff
- 004ea010 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2d0:8"]]
- 004ea010 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea010 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:320:8"]]
+ 004ea010 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea010 bytes 946a41f9
+ 004ea010 bytes 949241f9
- 004ea09c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f70:8"]]
- 004ea09c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea09c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fc0:8"]]
+ 004ea09c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea09c bytes 08b947f9
+ 004ea09c bytes 08e147f9
- 004ea184 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
- 004ea184 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea184 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:778:8"]]
+ 004ea184 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea184 bytes 299743f9
+ 004ea184 bytes 29bf43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2b53d60c1239b80d5d3861f65e16668"></a>

### [`004ea55c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ea/004ea55c.md) → [`004ea55c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea55c.md) _ZN5Botan14PKCS10_RequestC2ERNS_10DataSourceE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md) [`00bdcde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcde0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md) [`00bdce30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ea59c",
      "incomplete_value": true,
      "site": "004ea59c",
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
      "definition_site": "004ea59c",
      "incomplete_value": true,
      "site": "004ea59c",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ea59c",
      "incomplete_value": true,
      "site": "004ea59c",
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
      "definition_site": "004ea59c",
      "incomplete_value": true,
      "site": "004ea59c",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ea5dc",
      "incomplete_value": true,
      "site": "004ea5e4",
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
      "definition_site": "004ea5dc",
      "incomplete_value": true,
      "site": "004ea5e4",
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
      "004ea57c",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      "004ea584",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004ea59c",
      "DATA",
      [
        "storage",
        "00beca10",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "004ea57c",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      "004ea584",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004ea59c",
      "DATA",
      [
        "storage",
        "00beca60",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ea57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ea/004ea55c.md#insn-004ea57c) · [`004ea584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ea/004ea55c.md#insn-004ea584) · [`004ea5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ea/004ea55c.md#insn-004ea5d0)
- 新版 `004ea57c`（命令位置の公開資料なし） · `004ea584`（命令位置の公開資料なし） · `004ea5d0`（命令位置の公開資料なし）

~~~diff
- 004ea57c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 004ea57c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea57c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
+ 004ea57c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea57c bytes 088d41f9
+ 004ea57c bytes 08b541f9
- 004ea584 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
- 004ea584 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea584 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:f48:8"]]
+ 004ea584 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea584 bytes 4a7d47f9
+ 004ea584 bytes 4aa547f9
- 004ea5d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:330:8"]]
- 004ea5d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea5d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:380:8"]]
+ 004ea5d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea5d0 bytes 089941f9
+ 004ea5d0 bytes 08c141f9
~~~


<a id="compare-04d5aaeb280ae8237984051305567b5d"></a>

### [`004ea660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ea/004ea660.md) → [`004ea660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea660.md) _ZN5Botan11X509_Object9load_dataERNS_10DataSourceE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcde0.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0042cde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042cde4.md) [`004840c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/004840c4.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051d3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d3cc.md)
- 新版 呼出元 1件 [`00bdce30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce30.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0042cde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042cde4.md) [`004840c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/004840c4.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 3件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ea6f8",
      "incomplete_value": true,
      "site": "004ea6f8",
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
      "definition_site": "004ea6f8",
      "incomplete_value": true,
      "site": "004ea6f8",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ea734",
      "incomplete_value": true,
      "site": "004ea734",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
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
      "definition_site": "004ea734",
      "incomplete_value": true,
      "site": "004ea734",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ea80c",
      "incomplete_value": true,
      "site": "004ea80c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
      "definition_site": "004ea80c",
      "incomplete_value": true,
      "site": "004ea80c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
    "ordinal": 11,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ea6e8",
      "READ",
      [
        "storage",
        "00c1afa0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea6f8",
      "DATA",
      [
        "storage",
        "00bea378",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ea724",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ea6e8",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea6f8",
      "DATA",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ea724",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ea6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ea/004ea660.md#insn-004ea6e8) · [`004ea724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ea/004ea660.md#insn-004ea724) · [`004ea7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ea/004ea660.md#insn-004ea7fc)
- 新版 `004ea6e8`（命令位置の公開資料なし） · `004ea724`（命令位置の公開資料なし） · `004ea7fc`（命令位置の公開資料なし）

~~~diff
- 004ea6e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
- 004ea6e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea6e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
+ 004ea6e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea6e8 bytes 08d147f9
+ 004ea6e8 bytes 08f947f9
- 004ea724 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 004ea724 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea724 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 004ea724 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea724 bytes a99643f9
+ 004ea724 bytes a9be43f9
- 004ea7fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004ea7fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea7fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004ea7fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea7fc bytes 299543f9
+ 004ea7fc bytes 29bd43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8aad1f9d00a86ce639fcf869dbb20fc"></a>

### [`004eaec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ea/004eaec8.md) → [`004eaec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004eaec8.md) _ZN5Botan14PKCS10_RequestC2ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdd0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd0d0.md) · 呼出先 7件 [`0051d4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d4f0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 1件 [`00bdd120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd120.md) · 呼出先 7件 [`0051d4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d4f0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.72% / 新版 84.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eaf08",
      "incomplete_value": true,
      "site": "004eaf08",
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
      "definition_site": "004eaf08",
      "incomplete_value": true,
      "site": "004eaf08",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eaf08",
      "incomplete_value": true,
      "site": "004eaf08",
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
      "definition_site": "004eaf08",
      "incomplete_value": true,
      "site": "004eaf08",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eaf50",
      "incomplete_value": true,
      "site": "004eaf5c",
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
      "definition_site": "004eaf50",
      "incomplete_value": true,
      "site": "004eaf5c",
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
      "004eaee8",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      "004eaef0",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004eaf08",
      "DATA",
      [
        "storage",
        "00beca10",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "004eaee8",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      "004eaef0",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004eaf08",
      "DATA",
      [
        "storage",
        "00beca60",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eaee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ea/004eaec8.md#insn-004eaee8) · [`004eaef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ea/004eaec8.md#insn-004eaef0) · [`004eaf44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ea/004eaec8.md#insn-004eaf44)
- 新版 `004eaee8`（命令位置の公開資料なし） · `004eaef0`（命令位置の公開資料なし） · `004eaf44`（命令位置の公開資料なし）

~~~diff
- 004eaee8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 004eaee8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004eaee8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
+ 004eaee8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004eaee8 bytes 088d41f9
+ 004eaee8 bytes 08b541f9
- 004eaef0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
- 004eaef0 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004eaef0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:f48:8"]]
+ 004eaef0 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004eaef0 bytes 4a7d47f9
+ 004eaef0 bytes 4aa547f9
- 004eaf44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:330:8"]]
- 004eaf44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004eaf44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:380:8"]]
+ 004eaf44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004eaf44 bytes 089941f9
+ 004eaf44 bytes 08c141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ea65e99cc2214b852ca5f6a3295e793"></a>

### [`004eb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004eb/004eb040.md) → [`004eb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004eb040.md) _ZN5Botan14PKCS10_RequestC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md) [`00bdc7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc7c0.md) [`00bdc7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc7d0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md) [`00bdc810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc810.md) [`00bdc820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc820.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eb080",
      "incomplete_value": true,
      "site": "004eb080",
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
      "definition_site": "004eb080",
      "incomplete_value": true,
      "site": "004eb080",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eb080",
      "incomplete_value": true,
      "site": "004eb080",
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
      "definition_site": "004eb080",
      "incomplete_value": true,
      "site": "004eb080",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eb0c0",
      "incomplete_value": true,
      "site": "004eb0c8",
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
      "definition_site": "004eb0c0",
      "incomplete_value": true,
      "site": "004eb0c8",
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
      "004eb060",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      "004eb068",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004eb080",
      "DATA",
      [
        "storage",
        "00beca10",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "004eb060",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      "004eb068",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004eb080",
      "DATA",
      [
        "storage",
        "00beca60",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eb060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004eb/004eb040.md#insn-004eb060) · [`004eb068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004eb/004eb040.md#insn-004eb068) · [`004eb0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004eb/004eb040.md#insn-004eb0b4)
- 新版 `004eb060`（命令位置の公開資料なし） · `004eb068`（命令位置の公開資料なし） · `004eb0b4`（命令位置の公開資料なし）

~~~diff
- 004eb060 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 004eb060 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004eb060 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
+ 004eb060 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004eb060 bytes 088d41f9
+ 004eb060 bytes 08b541f9
- 004eb068 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
- 004eb068 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004eb068 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:f48:8"]]
+ 004eb068 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004eb068 bytes 4a7d47f9
+ 004eb068 bytes 4aa547f9
- 004eb0b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:330:8"]]
- 004eb0b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004eb0b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:380:8"]]
+ 004eb0b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004eb0b4 bytes 089941f9
+ 004eb0b4 bytes 08c141f9
~~~


<a id="compare-31b15b66ab0a095e2dea1599c1573599"></a>

### [`004eb16c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004eb/004eb16c.md) → [`004eb16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004eb16c.md) _ZN5Botan14PKCS10_Request12force_decodeEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 40件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`004830c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/004830c8.md) [`00483d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483d44.md)
- 新版 呼出元 0件  · 呼出先 40件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`004830c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/004830c8.md) [`00483d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483d44.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.49% / 新版 97.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 3件

アドレスに依存する影響 `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eb5dc",
      "incomplete_value": true,
      "site": "004eb5ec",
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
                "const:293000:8"
              ],
              [
                "leaf",
                "const:784:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004eb5dc",
      "incomplete_value": true,
      "site": "004eb5ec",
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
                "const:293000:8"
              ],
              [
                "leaf",
                "const:811:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 58,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eb5f0",
      "incomplete_value": true,
      "site": "004eb5f0",
      "value": [
        "LOAD",
        "8",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004eb5f0",
      "incomplete_value": true,
      "site": "004eb5f0",
      "value": [
        "LOAD",
        "8",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 59,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004eba14",
      "incomplete_value": false,
      "site": "004eba14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004eba14",
      "incomplete_value": false,
      "site": "004eba14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "ordinal": 83,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004eb338",
      "READ",
      [
        "storage",
        "00c1af18",
        null,
        "pointer"
      ]
    ],
    [
      "004eb38c",
      "DATA",
      [
        "storage",
        "00be91c8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004eb3bc",
      "READ",
      [
        "storage",
        "00be91d0",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004eb338",
      "READ",
      [
        "storage",
        "00c1af68",
        null,
        "pointer"
      ]
    ],
    [
      "004eb38c",
      "DATA",
      [
        "storage",
        "00be9218",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004eb3bc",
      "READ",
      [
        "storage",
        "00be9220",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eb338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004eb/004eb16c.md#insn-004eb338) · [`004eb5d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004eb/004eb16c.md#insn-004eb5d4) · [`004eb6c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004eb/004eb16c.md#insn-004eb6c0)
- 新版 `004eb338`（命令位置の公開資料なし） · `004eb5d4`（命令位置の公開資料なし） · `004eb6c0`（命令位置の公開資料なし）

~~~diff
- 004eb338 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f18:8"]]
- 004eb338 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004eb338 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f68:8"]]
+ 004eb338 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004eb338 bytes 298d47f9
+ 004eb338 bytes 29b547f9
- 004eb5d4 ["COPY", "tmp:0:8", ["const:811:8"]]
- 004eb5d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004eb5d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004eb5d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004eb5d4 ["COPY", "tmp:0:8", ["const:784:8"]]
+ 004eb5d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004eb5d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004eb5d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004eb5d4 bytes 29452091
+ 004eb5d4 bytes 29111e91
- 004eb6c0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004eb6c0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004eb6c0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004eb6c0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004eb6c0 bytes 299543f9
+ 004eb6c0 bytes 29bd43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-feaa5af31c8c6adcca5099254e105748"></a>

### [`004ebed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004eb/004ebed4.md) → [`004ebed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004ebed4.md) _ZNK5Botan11X509_Object15check_signatureEPKNS_10Public_KeyE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdce00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce00.md) · 呼出先 8件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00bdce50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce50.md) · 呼出先 8件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)

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
      "definition_site": "004ebfe4",
      "incomplete_value": true,
      "site": "004ebff0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ebfe4",
      "incomplete_value": true,
      "site": "004ebff0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f48:8"
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
      "004ebfe4",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004ebfe4",
      "PARAM",
      [
        "storage",
        "00be9238",
        "_ZTIN5Botan9ExceptionE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004ebfe4",
      "READ",
      [
        "storage",
        "00c1af98",
        null,
        "pointer"
      ]
    ],
    [
      "004ebfe4",
      "PARAM",
      [
        "storage",
        "00be9288",
        "_ZTIN5Botan9ExceptionE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ebfe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004eb/004ebed4.md#insn-004ebfe4)
- 新版 `004ebfe4`（命令位置の公開資料なし）

~~~diff
- 004ebfe4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f48:8"]]
- 004ebfe4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ebfe4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f98:8"]]
+ 004ebfe4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004ebfe4 bytes 21a447f9
+ 004ebfe4 bytes 21cc47f9
~~~


<a id="compare-c53318809651d89a40c4458174b83cea"></a>

### [`004ec0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec0b4.md) → [`004ec0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec0b4.md) _ZNK5Botan14PKCS10_Request18subject_public_keyEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcdf0.md) · 呼出先 6件 [`00513e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513e2c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdc830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc830.md) [`00bdce20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce20.md)
- 新版 呼出元 1件 [`00bdce40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce40.md) · 呼出先 6件 [`00513e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513e2c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdc880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc880.md) [`00bdce70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce70.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ec0ec",
      "incomplete_value": true,
      "site": "004ec0ec",
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
      "definition_site": "004ec0ec",
      "incomplete_value": true,
      "site": "004ec0ec",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ec134",
      "incomplete_value": true,
      "site": "004ec134",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
      "definition_site": "004ec134",
      "incomplete_value": true,
      "site": "004ec134",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
      "004ec0dc",
      "READ",
      [
        "storage",
        "00c1afa0",
        null,
        "pointer"
      ]
    ],
    [
      "004ec0ec",
      "DATA",
      [
        "storage",
        "00bea378",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ec124",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ec0dc",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "004ec0ec",
      "DATA",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ec124",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec0dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec0b4.md#insn-004ec0dc) · [`004ec124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec0b4.md#insn-004ec124)
- 新版 `004ec0dc`（命令位置の公開資料なし） · `004ec124`（命令位置の公開資料なし）

~~~diff
- 004ec0dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
- 004ec0dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ec0dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
+ 004ec0dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ec0dc bytes 08d147f9
+ 004ec0dc bytes 08f947f9
- 004ec124 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004ec124 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ec124 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004ec124 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ec124 bytes 299543f9
+ 004ec124 bytes 29bd43f9
~~~


<a id="compare-4c35e88fbfddac454e4ca4da3d1c5dd4"></a>

### [`004ec1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec1d0.md) → [`004ec1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec1d0.md) _ZNK5Botan14PKCS10_Request4dataEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdce20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce20.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdce70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce70.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

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
      "definition_site": "004ec230",
      "incomplete_value": false,
      "site": "004ec238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:b04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec230",
      "incomplete_value": false,
      "site": "004ec238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:b91:8"
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
      "definition_site": "004ec26c",
      "incomplete_value": true,
      "site": "004ec278",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec26c",
      "incomplete_value": true,
      "site": "004ec278",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
              ]
            ]
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
      "004ec230",
      "PARAM",
      [
        "storage",
        "00291b91",
        null,
        "string"
      ]
    ],
    [
      "004ec26c",
      "READ",
      [
        "storage",
        "00c1af10",
        null,
        "pointer"
      ]
    ],
    [
      "004ec26c",
      "PARAM",
      [
        "storage",
        "00be92b0",
        "_ZTIN5Botan14Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004ec230",
      "PARAM",
      [
        "storage",
        "00291b04",
        null,
        "string"
      ]
    ],
    [
      "004ec26c",
      "READ",
      [
        "storage",
        "00c1af60",
        null,
        "pointer"
      ]
    ],
    [
      "004ec26c",
      "PARAM",
      [
        "storage",
        "00be9300",
        "_ZTIN5Botan14Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec1d0.md#insn-004ec230) · [`004ec26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec1d0.md#insn-004ec26c)
- 新版 `004ec230`（命令位置の公開資料なし） · `004ec26c`（命令位置の公開資料なし）

~~~diff
- 004ec230 ["COPY", "tmp:0:8", ["const:b91:8"]]
- 004ec230 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004ec230 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004ec230 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004ec230 ["COPY", "tmp:0:8", ["const:b04:8"]]
+ 004ec230 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004ec230 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004ec230 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004ec230 bytes 21442e91
+ 004ec230 bytes 21102c91
- 004ec26c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
- 004ec26c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ec26c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f60:8"]]
+ 004ec26c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004ec26c bytes 218847f9
+ 004ec26c bytes 21b047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf6b24ab824a77f86ee4fd43f88a10a2"></a>

### [`004ec368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec368.md) → [`004ec368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec368.md) _ZNK5Botan14PKCS10_Request11constraintsEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdce30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce30.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7e0.md) [`00bdcc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc20.md) [`00bdce20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce20.md)
- 新版 呼出元 1件 [`00bdce80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce80.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md) [`00bdcc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc70.md) [`00bdce70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce70.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ec3ac",
      "incomplete_value": true,
      "site": "004ec3ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:299000:8"
              ],
              [
                "leaf",
                "const:bb4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec3ac",
      "incomplete_value": true,
      "site": "004ec3ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:299000:8"
              ],
              [
                "leaf",
                "const:c41:8"
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
      "definition_site": "004ec3a0",
      "incomplete_value": true,
      "site": "004ec3b0",
      "value": [
        "LOAD",
        "8",
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
                "const:7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec3a0",
      "incomplete_value": true,
      "site": "004ec3b0",
      "value": [
        "LOAD",
        "8",
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
                "const:7:8"
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
      "definition_site": "004ec418",
      "incomplete_value": true,
      "site": "004ec418",
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
      "definition_site": "004ec418",
      "incomplete_value": true,
      "site": "004ec418",
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
      "004ec398",
      "READ",
      [
        "storage",
        "00299c41",
        null,
        "string"
      ]
    ],
    [
      "004ec3a0",
      "READ",
      [
        "storage",
        "00299c48",
        null,
        "string"
      ]
    ],
    [
      "004ec408",
      "READ",
      [
        "storage",
        "00c1b338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ec398",
      "READ",
      [
        "storage",
        "00299bb4",
        null,
        "string"
      ]
    ],
    [
      "004ec3a0",
      "READ",
      [
        "storage",
        "00299bbb",
        null,
        "string"
      ]
    ],
    [
      "004ec408",
      "READ",
      [
        "storage",
        "00c1b388",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec368.md#insn-004ec394) · [`004ec408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec368.md#insn-004ec408)
- 新版 `004ec394`（命令位置の公開資料なし） · `004ec408`（命令位置の公開資料なし）

~~~diff
- 004ec394 ["COPY", "tmp:0:8", ["const:c41:8"]]
- 004ec394 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004ec394 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004ec394 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004ec394 ["COPY", "tmp:0:8", ["const:bb4:8"]]
+ 004ec394 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004ec394 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004ec394 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004ec394 bytes 29053191
+ 004ec394 bytes 29d12e91
- 004ec408 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:338:8"]]
- 004ec408 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ec408 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:388:8"]]
+ 004ec408 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ec408 bytes 089d41f9
+ 004ec408 bytes 08c541f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3c60d7974f7ce52cbdfd3a1b5f442ee"></a>

### [`004ec514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec514.md) → [`004ec514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec514.md) _ZNK5Botan14PKCS10_Request14ex_constraintsEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdce50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce50.md) · 呼出先 12件 [`0050ecac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ecac.md) [`0051bf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d7fc.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md)
- 新版 呼出元 1件 [`00bdcea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcea0.md) · 呼出先 12件 [`0050ecac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ecac.md) [`0051bf98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d7fc.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_value

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ec55c",
      "incomplete_value": true,
      "site": "004ec56c",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:516:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec55c",
      "incomplete_value": true,
      "site": "004ec56c",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:47c:8"
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
      "definition_site": "004ec570",
      "incomplete_value": true,
      "site": "004ec570",
      "value": [
        "LOAD",
        "8",
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec570",
      "incomplete_value": true,
      "site": "004ec570",
      "value": [
        "LOAD",
        "8",
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
                "const:f:8"
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
      "definition_site": "004ec5e0",
      "incomplete_value": true,
      "site": "004ec5e0",
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
      "definition_site": "004ec5e0",
      "incomplete_value": true,
      "site": "004ec5e0",
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
      "004ec55c",
      "READ",
      [
        "storage",
        "002a947c",
        null,
        "string"
      ]
    ],
    [
      "004ec560",
      "READ",
      [
        "storage",
        "002a948b",
        null,
        "string"
      ]
    ],
    [
      "004ec5d0",
      "READ",
      [
        "storage",
        "00c1b340",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ec55c",
      "READ",
      [
        "storage",
        "002a9516",
        null,
        "string"
      ]
    ],
    [
      "004ec560",
      "READ",
      [
        "storage",
        "002a9525",
        null,
        "string"
      ]
    ],
    [
      "004ec5d0",
      "READ",
      [
        "storage",
        "00c1b390",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec514.md#insn-004ec554) · [`004ec558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec514.md#insn-004ec558)
- 新版 `004ec554`（命令位置の公開資料なし） · `004ec558`（命令位置の公開資料なし）

~~~diff
- 004ec554 ["COPY", "tmp:0:8", ["const:47c:8"]]
- 004ec554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004ec554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004ec554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004ec554 ["COPY", "tmp:0:8", ["const:516:8"]]
+ 004ec554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004ec554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004ec554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004ec554 bytes 08f11191
+ 004ec554 bytes 08591491
- 004ec558 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 004ec558 bytes 29eeff90
+ 004ec558 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 004ec558 bytes 29eeff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48ce975c08938678ef0e0e3c281fd56f"></a>

### [`004ec73c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec73c.md) → [`004ec73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec73c.md) _ZNK5Botan14PKCS10_Request5is_CAEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdce60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce60.md) · 呼出先 7件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7e0.md) [`00bdcc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc20.md)
- 新版 呼出元 1件 [`00bdceb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdceb0.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md) [`00bdcc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc70.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ec778",
      "incomplete_value": true,
      "site": "004ec788",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:9c3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec778",
      "incomplete_value": true,
      "site": "004ec788",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:a57:8"
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
      "definition_site": "004ec78c",
      "incomplete_value": true,
      "site": "004ec78c",
      "value": [
        "LOAD",
        "8",
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec78c",
      "incomplete_value": true,
      "site": "004ec78c",
      "value": [
        "LOAD",
        "8",
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
                "const:f:8"
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
      "definition_site": "004ec7fc",
      "incomplete_value": true,
      "site": "004ec7fc",
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
      "definition_site": "004ec7fc",
      "incomplete_value": true,
      "site": "004ec7fc",
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
      "004ec778",
      "READ",
      [
        "storage",
        "002afa57",
        null,
        "string"
      ]
    ],
    [
      "004ec77c",
      "READ",
      [
        "storage",
        "002afa66",
        null,
        "string"
      ]
    ],
    [
      "004ec7ec",
      "READ",
      [
        "storage",
        "00c1b348",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ec778",
      "READ",
      [
        "storage",
        "002af9c3",
        null,
        "string"
      ]
    ],
    [
      "004ec77c",
      "READ",
      [
        "storage",
        "002af9d2",
        null,
        "string"
      ]
    ],
    [
      "004ec7ec",
      "READ",
      [
        "storage",
        "00c1b398",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec73c.md#insn-004ec770) · [`004ec774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec73c.md#insn-004ec774)
- 新版 `004ec770`（命令位置の公開資料なし） · `004ec774`（命令位置の公開資料なし）

~~~diff
- 004ec770 ["COPY", "tmp:0:8", ["const:a57:8"]]
- 004ec770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004ec770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004ec770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004ec770 ["COPY", "tmp:0:8", ["const:9c3:8"]]
+ 004ec770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004ec770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004ec770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004ec770 bytes 085d2991
+ 004ec770 bytes 080d2791
- 004ec774 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 004ec774 bytes 29eeff90
+ 004ec774 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 004ec774 bytes 29eeff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86d0fde847c97ddb1c27ba903f657763"></a>

### [`004ec8c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec8c8.md) → [`004ec8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec8c8.md) _ZNK5Botan14PKCS10_Request10path_limitEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdce70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce70.md) · 呼出先 9件 [`0050e110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e110.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7e0.md)
- 新版 呼出元 1件 [`00bdcec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcec0.md) · 呼出先 9件 [`0050e110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e110.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ec904",
      "incomplete_value": true,
      "site": "004ec914",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:9c3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec904",
      "incomplete_value": true,
      "site": "004ec914",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:a57:8"
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
      "definition_site": "004ec918",
      "incomplete_value": true,
      "site": "004ec918",
      "value": [
        "LOAD",
        "8",
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec918",
      "incomplete_value": true,
      "site": "004ec918",
      "value": [
        "LOAD",
        "8",
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
                "const:f:8"
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
      "definition_site": "004ec988",
      "incomplete_value": true,
      "site": "004ec988",
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
      "definition_site": "004ec988",
      "incomplete_value": true,
      "site": "004ec988",
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
      "004ec904",
      "READ",
      [
        "storage",
        "002afa57",
        null,
        "string"
      ]
    ],
    [
      "004ec908",
      "READ",
      [
        "storage",
        "002afa66",
        null,
        "string"
      ]
    ],
    [
      "004ec978",
      "READ",
      [
        "storage",
        "00c1b348",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ec904",
      "READ",
      [
        "storage",
        "002af9c3",
        null,
        "string"
      ]
    ],
    [
      "004ec908",
      "READ",
      [
        "storage",
        "002af9d2",
        null,
        "string"
      ]
    ],
    [
      "004ec978",
      "READ",
      [
        "storage",
        "00c1b398",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec8fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec8c8.md#insn-004ec8fc) · [`004ec900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec8c8.md#insn-004ec900)
- 新版 `004ec8fc`（命令位置の公開資料なし） · `004ec900`（命令位置の公開資料なし）

~~~diff
- 004ec8fc ["COPY", "tmp:0:8", ["const:a57:8"]]
- 004ec8fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004ec8fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004ec8fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004ec8fc ["COPY", "tmp:0:8", ["const:9c3:8"]]
+ 004ec8fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004ec8fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004ec8fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004ec8fc bytes 085d2991
+ 004ec8fc bytes 080d2791
- 004ec900 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 004ec900 bytes 29eeff90
+ 004ec900 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 004ec900 bytes 29eeff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-748b48529cfe59055a00be70ca3dec11"></a>

### [`004eca70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004eca70.md) → [`004eca70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004eca70.md) _ZNK5Botan14Cert_Extension17Basic_Constraints14get_path_limitEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdce80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce80.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdced0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdced0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ecad4",
      "incomplete_value": false,
      "site": "004ecadc",
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
            "const:4df:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ecad4",
      "incomplete_value": false,
      "site": "004ecadc",
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
            "const:454:8"
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
      "definition_site": "004ecb10",
      "incomplete_value": true,
      "site": "004ecb1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ecb10",
      "incomplete_value": true,
      "site": "004ecb1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
              ]
            ]
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
      "004ecad4",
      "PARAM",
      [
        "storage",
        "002a2454",
        null,
        "string"
      ]
    ],
    [
      "004ecb10",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "004ecb10",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004ecad4",
      "PARAM",
      [
        "storage",
        "002a24df",
        null,
        "string"
      ]
    ],
    [
      "004ecb10",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "004ecb10",
      "PARAM",
      [
        "storage",
        "00be93d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ecad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004eca70.md#insn-004ecad4) · [`004ecb10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004eca70.md#insn-004ecb10)
- 新版 `004ecad4`（命令位置の公開資料なし） · `004ecb10`（命令位置の公開資料なし）

~~~diff
- 004ecad4 ["COPY", "tmp:0:8", ["const:454:8"]]
- 004ecad4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004ecad4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004ecad4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004ecad4 ["COPY", "tmp:0:8", ["const:4df:8"]]
+ 004ecad4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004ecad4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004ecad4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004ecad4 bytes 21501191
+ 004ecad4 bytes 217c1391
- 004ecb10 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 004ecb10 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ecb10 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 004ecb10 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004ecb10 bytes 218447f9
+ 004ecb10 bytes 21ac47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9ac9221c07d884eca4b37c4eb1b3b9c"></a>

### [`004ecb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ecb70.md) → [`004ecb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ecb70.md) _ZN5Botan7X509_CAC1ERKNS_16X509_CertificateERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS7_11char_traitsIcEENS7_9allocatorIcEEEERNS_21Ra

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 19件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`004ed050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ed050.md) [`004ed188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ed188.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`004ed050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed050.md) [`004ed188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed188.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.82% / 新版 97.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ecbb8",
      "incomplete_value": true,
      "site": "004ecbb8",
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
      "definition_site": "004ecbb8",
      "incomplete_value": true,
      "site": "004ecbb8",
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
    "kind": "store_value",
    "new": {
      "definition_site": "004ecbf4",
      "incomplete_value": true,
      "site": "004ecbf8",
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
      "definition_site": "004ecbf4",
      "incomplete_value": true,
      "site": "004ecbf8",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ecd10",
      "incomplete_value": false,
      "site": "004ecd1c",
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
            "const:692:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ecd10",
      "incomplete_value": false,
      "site": "004ecd1c",
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
            "const:607:8"
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
      "004ecb9c",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004ecbb8",
      "DATA",
      [
        "storage",
        "00be9198",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ecbf0",
      "READ",
      [
        "storage",
        "00c1b2a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ecb9c",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004ecbb8",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ecbf0",
      "READ",
      [
        "storage",
        "00c1b2f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ecb9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ecb70.md#insn-004ecb9c) · [`004ecbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ecb70.md#insn-004ecbf0) · [`004ecd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ecb70.md#insn-004ecd10)
- 新版 `004ecb9c`（命令位置の公開資料なし） · `004ecbf0`（命令位置の公開資料なし） · `004ecd10`（命令位置の公開資料なし）

~~~diff
- 004ecb9c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ef8:8"]]
- 004ecb9c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ecb9c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f48:8"]]
+ 004ecb9c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ecb9c bytes 297d47f9
+ 004ecb9c bytes 29a547f9
- 004ecbf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
- 004ecbf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ecbf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f0:8"]]
+ 004ecbf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ecbf0 bytes 085141f9
+ 004ecbf0 bytes 087941f9
- 004ecd10 ["COPY", "tmp:0:8", ["const:607:8"]]
- 004ecd10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004ecd10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004ecd10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004ecd10 ["COPY", "tmp:0:8", ["const:692:8"]]
+ 004ecd10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004ecd10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004ecd10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004ecd10 bytes 211c1891
+ 004ecd10 bytes 21481a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96905723aad34799177d452ba6107e27"></a>

### [`004ed188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ed188.md) → [`004ed188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed188.md) FUN_004ed188

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`004ecb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ecb70.md) [`004edb24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004edb24.md) [`004ef8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004ef8d4.md) [`0050a638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050b/0050b45c.md) · 呼出先 16件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0044a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 5件 [`004ecb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ecb70.md) [`004edb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004edb24.md) [`004ef8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef8d4.md) [`0050a638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050b/0050b45c.md) · 呼出先 16件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.65% / 新版 98.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ed2f0",
      "incomplete_value": false,
      "site": "004ed2fc",
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
            "const:6e6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ed2f0",
      "incomplete_value": false,
      "site": "004ed2fc",
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
            "const:64c:8"
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
      "definition_site": "004ed330",
      "incomplete_value": true,
      "site": "004ed33c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ed330",
      "incomplete_value": true,
      "site": "004ed33c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ed390",
      "incomplete_value": false,
      "site": "004ed398",
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
            "const:284:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ed390",
      "incomplete_value": false,
      "site": "004ed398",
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
            "const:286:8"
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
      "004ed2f0",
      "PARAM",
      [
        "storage",
        "002a964c",
        null,
        "string"
      ]
    ],
    [
      "004ed330",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004ed330",
      "PARAM",
      [
        "storage",
        "00be9298",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004ed2f0",
      "PARAM",
      [
        "storage",
        "002a96e6",
        null,
        "string"
      ]
    ],
    [
      "004ed330",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "004ed330",
      "PARAM",
      [
        "storage",
        "00be92e8",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ed2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ed188.md#insn-004ed2f0) · [`004ed330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ed188.md#insn-004ed330) · [`004ed390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ed188.md#insn-004ed390)
- 新版 `004ed2f0`（命令位置の公開資料なし） · `004ed330`（命令位置の公開資料なし） · `004ed390`（命令位置の公開資料なし）

~~~diff
- 004ed2f0 ["COPY", "tmp:0:8", ["const:64c:8"]]
- 004ed2f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004ed2f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004ed2f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004ed2f0 ["COPY", "tmp:0:8", ["const:6e6:8"]]
+ 004ed2f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004ed2f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004ed2f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004ed2f0 bytes 00301991
+ 004ed2f0 bytes 00981b91
- 004ed330 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 004ed330 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ed330 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004ed330 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004ed330 bytes 217847f9
+ 004ed330 bytes 21a047f9
- 004ed390 ["COPY", "tmp:0:8", ["const:286:8"]]
- 004ed390 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004ed390 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004ed390 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004ed390 ["COPY", "tmp:0:8", ["const:284:8"]]
+ 004ed390 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004ed390 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004ed390 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004ed390 bytes 21180a91
+ 004ed390 bytes 21100a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2747d48d62765f5f17f2287ff6154b2"></a>

### [`004edb24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004edb24.md) → [`004edb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004edb24.md) _ZN5Botan7X509_CAC1ERKNS_16X509_CertificateERKNS_11Private_KeyERKNSt6__ndk13mapINS7_12basic_stringIcNS7_11char_traitsIcEENS7_9allocatorIcEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004ed188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ed188.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00518128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/00518128.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004ed188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed188.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00518128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518128.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004edb70",
      "incomplete_value": true,
      "site": "004edb70",
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
      "definition_site": "004edb70",
      "incomplete_value": true,
      "site": "004edb70",
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
    "kind": "store_value",
    "new": {
      "definition_site": "004edbac",
      "incomplete_value": true,
      "site": "004edbb0",
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
      "definition_site": "004edbac",
      "incomplete_value": true,
      "site": "004edbb0",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004edcb8",
      "incomplete_value": true,
      "site": "004edcc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004edcb8",
      "incomplete_value": true,
      "site": "004edcc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
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
      "004edb50",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004edb70",
      "DATA",
      [
        "storage",
        "00be9198",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004edba8",
      "READ",
      [
        "storage",
        "00c1b2a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004edb50",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004edb70",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004edba8",
      "READ",
      [
        "storage",
        "00c1b2f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004edb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004edb24.md#insn-004edb50) · [`004edba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004edb24.md#insn-004edba8) · [`004edcb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004edb24.md#insn-004edcb8)
- 新版 `004edb50`（命令位置の公開資料なし） · `004edba8`（命令位置の公開資料なし） · `004edcb8`（命令位置の公開資料なし）

~~~diff
- 004edb50 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ef8:8"]]
- 004edb50 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004edb50 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f48:8"]]
+ 004edb50 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004edb50 bytes 297d47f9
+ 004edb50 bytes 29a547f9
- 004edba8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
- 004edba8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004edba8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f0:8"]]
+ 004edba8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004edba8 bytes 085141f9
+ 004edba8 bytes 087941f9
- 004edcb8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 004edcb8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004edcb8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004edcb8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004edcb8 bytes 217847f9
+ 004edcb8 bytes 21a047f9
~~~


<a id="compare-83e70ae4eec6157f5382f391ca90055c"></a>

### [`004ede80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ede80.md) → [`004ede80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ede80.md) _ZNK5Botan7X509_CA12sign_requestERKNS_14PKCS10_RequestERNS_21RandomNumberGeneratorERKNS_9X509_TimeES8_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 25件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`004e8484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e8484.md) [`004ee34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee34c.md) [`004ee760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee760.md) [`0051854c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/0051854c.md)
- 新版 呼出元 0件  · 呼出先 25件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`004e8484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8484.md) [`004ee34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee34c.md) [`004ee760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee760.md) [`0051854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.79% / 新版 96.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004edf6c",
      "incomplete_value": true,
      "site": "004edf70",
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
      "definition_site": "004edf6c",
      "incomplete_value": true,
      "site": "004edf70",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004edfa0",
      "incomplete_value": true,
      "site": "004edfa4",
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
      "definition_site": "004edfa0",
      "incomplete_value": true,
      "site": "004edfa4",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004edfe0",
      "incomplete_value": true,
      "site": "004edfec",
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
      "definition_site": "004edfe0",
      "incomplete_value": true,
      "site": "004edfec",
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
      "004edf60",
      "READ",
      [
        "storage",
        "00c1b348",
        null,
        "pointer"
      ]
    ],
    [
      "004edf70",
      "DATA",
      [
        "storage",
        "00bea940",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "004edf98",
      "READ",
      [
        "storage",
        "00c1b338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004edf60",
      "READ",
      [
        "storage",
        "00c1b398",
        null,
        "pointer"
      ]
    ],
    [
      "004edf70",
      "DATA",
      [
        "storage",
        "00bea990",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "004edf98",
      "READ",
      [
        "storage",
        "00c1b388",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004edf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ede80.md#insn-004edf60) · [`004edf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ede80.md#insn-004edf98) · [`004edfd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ede80.md#insn-004edfd0)
- 新版 `004edf60`（命令位置の公開資料なし） · `004edf98`（命令位置の公開資料なし） · `004edfd0`（命令位置の公開資料なし）

~~~diff
- 004edf60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:348:8"]]
- 004edf60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004edf60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:398:8"]]
+ 004edf60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004edf60 bytes 08a541f9
+ 004edf60 bytes 08cd41f9
- 004edf98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:338:8"]]
- 004edf98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004edf98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:388:8"]]
+ 004edf98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004edf98 bytes 089d41f9
+ 004edf98 bytes 08c541f9
- 004edfd0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:350:8"]]
- 004edfd0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004edfd0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a0:8"]]
+ 004edfd0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004edfd0 bytes 08a941f9
+ 004edfd0 bytes 08d141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-423818dfcdd3736049e4ad2f670d6e79"></a>

### [`004ee34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee34c.md) → [`004ee34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee34c.md) FUN_004ee34c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004ede80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ede80.md) [`00503af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/00503af8.md) [`0050a638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050b/0050b45c.md) · 呼出先 7件 [`00519534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00519/00519534.md) [`0051bf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d7fc.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md)
- 新版 呼出元 4件 [`004ede80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ede80.md) [`00503af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/00503af8.md) [`0050a638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050b/0050b45c.md) · 呼出先 7件 [`00519534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519534.md) [`0051bf98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d7fc.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ee390",
      "incomplete_value": true,
      "site": "004ee3a4",
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
      "definition_site": "004ee390",
      "incomplete_value": true,
      "site": "004ee3a4",
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
      "004ee380",
      "READ",
      [
        "storage",
        "00c1b2d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ee3a4",
      "DATA",
      [
        "storage",
        "00beb8b0",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004ee380",
      "READ",
      [
        "storage",
        "00c1b320",
        null,
        "pointer"
      ]
    ],
    [
      "004ee3a4",
      "DATA",
      [
        "storage",
        "00beb900",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ee380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee34c.md#insn-004ee380)
- 新版 `004ee380`（命令位置の公開資料なし）

~~~diff
- 004ee380 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2d0:8"]]
- 004ee380 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ee380 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:320:8"]]
+ 004ee380 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ee380 bytes 296941f9
+ 004ee380 bytes 299141f9
~~~


<a id="compare-4b185da6459a6ccfd5e338c71ab5a081"></a>

### [`004ee4f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee4f4.md) → [`004ee4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee4f4.md) _ZN5Botan10Extensions7replaceEPNS_21Certificate_ExtensionEb

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdce90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce90.md) · 呼出先 13件 [`004f3cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3cec.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`0051a850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051a/0051a850.md) [`00528a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00528/00528a6c.md) [`00528d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00528/00528d24.md)
- 新版 呼出元 1件 [`00bdcee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcee0.md) · 呼出先 13件 [`004f3cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3cec.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`0051a850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a850.md) [`00528a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528a6c.md) [`00528d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528d24.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.83% / 新版 97.83%

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
      "definition_site": "004ee588",
      "incomplete_value": true,
      "site": "004ee588",
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
      "definition_site": "004ee588",
      "incomplete_value": true,
      "site": "004ee588",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ee5cc",
      "incomplete_value": true,
      "site": "004ee5d0",
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
      "definition_site": "004ee5cc",
      "incomplete_value": true,
      "site": "004ee5d0",
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
    "ordinal": 20,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ee578",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "004ee588",
      "DATA",
      [
        "storage",
        "00bed428",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "004ee5c0",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ee578",
      "READ",
      [
        "storage",
        "00c1b330",
        null,
        "pointer"
      ]
    ],
    [
      "004ee588",
      "DATA",
      [
        "storage",
        "00bed478",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "004ee5c0",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ee578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee4f4.md#insn-004ee578) · [`004ee5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee4f4.md#insn-004ee5c0)
- 新版 `004ee578`（命令位置の公開資料なし） · `004ee5c0`（命令位置の公開資料なし）

~~~diff
- 004ee578 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
- 004ee578 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ee578 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:330:8"]]
+ 004ee578 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ee578 bytes 087141f9
+ 004ee578 bytes 089941f9
- 004ee5c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
- 004ee5c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ee5c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
+ 004ee5c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ee5c0 bytes 088147f9
+ 004ee5c0 bytes 08a947f9
~~~


<a id="compare-f8459599575e884e5e6fd2d2feae2e1c"></a>

### [`004ee7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee7d8.md) → [`004ee7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee7d8.md) _ZN5Botan7X509_CA9make_certEPNS_9PK_SignerERNS_21RandomNumberGeneratorERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS8_9allocatorIhEEEER

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdceb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdceb0.md) · 呼出先 16件 [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00bdcf00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf00.md) · 呼出先 16件 [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.40% / 新版 96.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ee8ac",
      "incomplete_value": true,
      "site": "004ee8ac",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
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
      "definition_site": "004ee8ac",
      "incomplete_value": true,
      "site": "004ee8ac",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004eea74",
      "incomplete_value": true,
      "site": "004eea74",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004eea74",
      "incomplete_value": true,
      "site": "004eea74",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004eeae0",
      "incomplete_value": true,
      "site": "004eeae0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004eeae0",
      "incomplete_value": true,
      "site": "004eeae0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ee89c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004eea64",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004eead0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ee89c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004eea64",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004eead0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ee89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee7d8.md#insn-004ee89c) · [`004eea64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee7d8.md#insn-004eea64) · [`004eead0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee7d8.md#insn-004eead0)
- 新版 `004ee89c`（命令位置の公開資料なし） · `004eea64`（命令位置の公開資料なし） · `004eead0`（命令位置の公開資料なし）

~~~diff
- 004ee89c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 004ee89c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ee89c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
+ 004ee89c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ee89c bytes 699643f9
+ 004ee89c bytes 69be43f9
- 004eea64 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:728:8"]]
- 004eea64 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004eea64 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:778:8"]]
+ 004eea64 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004eea64 bytes 899743f9
+ 004eea64 bytes 89bf43f9
- 004eead0 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:728:8"]]
- 004eead0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004eead0 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:778:8"]]
+ 004eead0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004eead0 bytes 899743f9
+ 004eead0 bytes 89bf43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf975747725f8475cb3e490d9a66d421"></a>

### [`004ef204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004ef204.md) → [`004ef204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef204.md) _ZNK5Botan7X509_CA8make_crlERKNSt6__ndk16vectorINS_9CRL_EntryENS1_9allocatorIS3_EEEEjRNS_21RandomNumberGeneratorENS1_6chrono10time_pointINSB

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdced0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdced0.md) · 呼出先 21件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`004f43b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f43b8.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`0051854c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/0051854c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00bdcf20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf20.md) · 呼出先 21件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`004f43b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f43b8.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`0051854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.50% / 新版 94.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ef258",
      "incomplete_value": true,
      "site": "004ef258",
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
      "definition_site": "004ef258",
      "incomplete_value": true,
      "site": "004ef258",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ef2a8",
      "incomplete_value": true,
      "site": "004ef2b4",
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
      "definition_site": "004ef2a8",
      "incomplete_value": true,
      "site": "004ef2b4",
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
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ef318",
      "incomplete_value": true,
      "site": "004ef31c",
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
      "definition_site": "004ef318",
      "incomplete_value": true,
      "site": "004ef31c",
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
    "ordinal": 34,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ef240",
      "READ",
      [
        "storage",
        "00c1b2d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ef258",
      "DATA",
      [
        "storage",
        "00beb8b0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ef298",
      "READ",
      [
        "storage",
        "00c1b350",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ef240",
      "READ",
      [
        "storage",
        "00c1b320",
        null,
        "pointer"
      ]
    ],
    [
      "004ef258",
      "DATA",
      [
        "storage",
        "00beb900",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ef298",
      "READ",
      [
        "storage",
        "00c1b3a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ef240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004ef204.md#insn-004ef240) · [`004ef298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004ef204.md#insn-004ef298) · [`004ef308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004ef204.md#insn-004ef308)
- 新版 `004ef240`（命令位置の公開資料なし） · `004ef298`（命令位置の公開資料なし） · `004ef308`（命令位置の公開資料なし）

~~~diff
- 004ef240 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2d0:8"]]
- 004ef240 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ef240 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:320:8"]]
+ 004ef240 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ef240 bytes 296941f9
+ 004ef240 bytes 299141f9
- 004ef298 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:350:8"]]
- 004ef298 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ef298 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a0:8"]]
+ 004ef298 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ef298 bytes 08a941f9
+ 004ef298 bytes 08d141f9
- 004ef308 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:360:8"]]
- 004ef308 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ef308 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3b0:8"]]
+ 004ef308 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ef308 bytes 08b141f9
+ 004ef308 bytes 08d941f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ab008803e3dca58707ab830b6c40104"></a>

### [`004efa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efa38.md) → [`004efa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efa38.md) _ZN5Botan8X509_CRLC2ERNS_10DataSourceE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md) [`00bdcde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcde0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md) [`00bdce30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004efa78",
      "incomplete_value": true,
      "site": "004efa78",
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
      "definition_site": "004efa78",
      "incomplete_value": true,
      "site": "004efa78",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004efa78",
      "incomplete_value": true,
      "site": "004efa78",
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
      "definition_site": "004efa78",
      "incomplete_value": true,
      "site": "004efa78",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004efab8",
      "incomplete_value": true,
      "site": "004efac0",
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
      "definition_site": "004efab8",
      "incomplete_value": true,
      "site": "004efac0",
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
      "004efa58",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      "004efa60",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004efa78",
      "DATA",
      [
        "storage",
        "00beca10",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "004efa58",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      "004efa60",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004efa78",
      "DATA",
      [
        "storage",
        "00beca60",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004efa58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efa38.md#insn-004efa58) · [`004efa60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efa38.md#insn-004efa60) · [`004efaac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efa38.md#insn-004efaac)
- 新版 `004efa58`（命令位置の公開資料なし） · `004efa60`（命令位置の公開資料なし） · `004efaac`（命令位置の公開資料なし）

~~~diff
- 004efa58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 004efa58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efa58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
+ 004efa58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004efa58 bytes 088d41f9
+ 004efa58 bytes 08b541f9
- 004efa60 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
- 004efa60 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efa60 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:f48:8"]]
+ 004efa60 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004efa60 bytes 4a7d47f9
+ 004efa60 bytes 4aa547f9
- 004efaac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b0:8"]]
- 004efaac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efaac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:300:8"]]
+ 004efaac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004efaac bytes 085941f9
+ 004efaac bytes 088141f9
~~~


<a id="compare-14f715f0649b824601435f19be4cb5a4"></a>

### [`004efb8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efb8c.md) → [`004efb8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efb8c.md) _ZN5Botan8X509_CRLC2ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcef0.md) · 呼出先 7件 [`0051d4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d4f0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 1件 [`00bdcf40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf40.md) · 呼出先 7件 [`0051d4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d4f0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.72% / 新版 84.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004efbcc",
      "incomplete_value": true,
      "site": "004efbcc",
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
      "definition_site": "004efbcc",
      "incomplete_value": true,
      "site": "004efbcc",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004efbcc",
      "incomplete_value": true,
      "site": "004efbcc",
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
      "definition_site": "004efbcc",
      "incomplete_value": true,
      "site": "004efbcc",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004efc14",
      "incomplete_value": true,
      "site": "004efc20",
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
      "definition_site": "004efc14",
      "incomplete_value": true,
      "site": "004efc20",
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
      "004efbac",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      "004efbb4",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004efbcc",
      "DATA",
      [
        "storage",
        "00beca10",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "004efbac",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      "004efbb4",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004efbcc",
      "DATA",
      [
        "storage",
        "00beca60",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004efbac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efb8c.md#insn-004efbac) · [`004efbb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efb8c.md#insn-004efbb4) · [`004efc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efb8c.md#insn-004efc08)
- 新版 `004efbac`（命令位置の公開資料なし） · `004efbb4`（命令位置の公開資料なし） · `004efc08`（命令位置の公開資料なし）

~~~diff
- 004efbac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 004efbac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efbac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
+ 004efbac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004efbac bytes 088d41f9
+ 004efbac bytes 08b541f9
- 004efbb4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
- 004efbb4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efbb4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:f48:8"]]
+ 004efbb4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004efbb4 bytes 4a7d47f9
+ 004efbb4 bytes 4aa547f9
- 004efc08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b0:8"]]
- 004efc08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efc08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:300:8"]]
+ 004efc08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004efc08 bytes 085941f9
+ 004efc08 bytes 088141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ecdefa0c2953dc0496a14d5b8e8e41b"></a>

### [`004efd04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efd04.md) → [`004efd04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efd04.md) _ZN5Botan8X509_CRLC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md) [`00bdc7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc7c0.md) [`00bdc7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc7d0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md) [`00bdc810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc810.md) [`00bdc820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc820.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004efd44",
      "incomplete_value": true,
      "site": "004efd44",
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
      "definition_site": "004efd44",
      "incomplete_value": true,
      "site": "004efd44",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004efd44",
      "incomplete_value": true,
      "site": "004efd44",
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
      "definition_site": "004efd44",
      "incomplete_value": true,
      "site": "004efd44",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004efd84",
      "incomplete_value": true,
      "site": "004efd8c",
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
      "definition_site": "004efd84",
      "incomplete_value": true,
      "site": "004efd8c",
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
      "004efd24",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      "004efd2c",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004efd44",
      "DATA",
      [
        "storage",
        "00beca10",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "004efd24",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      "004efd2c",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004efd44",
      "DATA",
      [
        "storage",
        "00beca60",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004efd24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efd04.md#insn-004efd24) · [`004efd2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efd04.md#insn-004efd2c) · [`004efd78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efd04.md#insn-004efd78)
- 新版 `004efd24`（命令位置の公開資料なし） · `004efd2c`（命令位置の公開資料なし） · `004efd78`（命令位置の公開資料なし）

~~~diff
- 004efd24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 004efd24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efd24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
+ 004efd24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004efd24 bytes 088d41f9
+ 004efd24 bytes 08b541f9
- 004efd2c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
- 004efd2c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efd2c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:f48:8"]]
+ 004efd2c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004efd2c bytes 4a7d47f9
+ 004efd2c bytes 4aa547f9
- 004efd78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b0:8"]]
- 004efd78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efd78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:300:8"]]
+ 004efd78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004efd78 bytes 085941f9
+ 004efd78 bytes 088141f9
~~~


<a id="compare-2f2eccf5c73ca5a15a7a50cfc5f48a87"></a>

### [`004efe30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efe30.md) → [`004efe30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efe30.md) _ZN5Botan8X509_CRLC2ERKNS_7X509_DNERKNS_9X509_TimeES6_RKNSt6__ndk16vectorINS_9CRL_EntryENS7_9allocatorIS9_EEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00518ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/00518ea0.md) [`00525f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/00525f90.md) [`00527c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00527/00527c8c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00518ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518ea0.md) [`00525f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525f90.md) [`00527c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527c8c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.61% / 新版 85.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004efea4",
      "incomplete_value": true,
      "site": "004efea4",
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
      "definition_site": "004efea4",
      "incomplete_value": true,
      "site": "004efea4",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004efea4",
      "incomplete_value": true,
      "site": "004efea4",
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
      "definition_site": "004efea4",
      "incomplete_value": true,
      "site": "004efea4",
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
      "definition_site": "004efee0",
      "incomplete_value": true,
      "site": "004efee8",
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
      "definition_site": "004efee0",
      "incomplete_value": true,
      "site": "004efee8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004efe8c",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      "004efe90",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004efea4",
      "DATA",
      [
        "storage",
        "00beca10",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "004efe8c",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      "004efe90",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004efea4",
      "DATA",
      [
        "storage",
        "00beca60",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004efe8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efe30.md#insn-004efe8c) · [`004efe90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efe30.md#insn-004efe90) · [`004efed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efe30.md#insn-004efed4)
- 新版 `004efe8c`（命令位置の公開資料なし） · `004efe90`（命令位置の公開資料なし） · `004efed4`（命令位置の公開資料なし）

~~~diff
- 004efe8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 004efe8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efe8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
+ 004efe8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004efe8c bytes 088d41f9
+ 004efe8c bytes 08b541f9
- 004efe90 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ef8:8"]]
- 004efe90 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efe90 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f48:8"]]
+ 004efe90 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004efe90 bytes 297d47f9
+ 004efe90 bytes 29a547f9
- 004efed4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b0:8"]]
- 004efed4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efed4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:300:8"]]
+ 004efed4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004efed4 bytes 085941f9
+ 004efed4 bytes 088141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2524c862fe9a4dce5f4ead749301f6fb"></a>

### [`004f03d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f0/004f03d8.md) → [`004f03d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f03d8.md) _ZN5Botan8X509_CRL12force_decodeEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 42件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md) [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`004828a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/004828a4.md)
- 新版 呼出元 0件  · 呼出先 42件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0042e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`004828a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004828a4.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.11% / 新版 92.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 6件, `store_destination` 1件, `store_value` 9件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f0438",
      "incomplete_value": true,
      "site": "004f0438",
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
      "definition_site": "004f0438",
      "incomplete_value": true,
      "site": "004f0438",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f0458",
      "incomplete_value": true,
      "site": "004f0458",
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
      "definition_site": "004f0458",
      "incomplete_value": true,
      "site": "004f0458",
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
      "definition_site": "004f0460",
      "incomplete_value": true,
      "site": "004f0460",
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
      "definition_site": "004f0460",
      "incomplete_value": true,
      "site": "004f0460",
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
      "004f041c",
      "READ",
      [
        "storage",
        "00c1b290",
        null,
        "pointer"
      ]
    ],
    [
      "004f0438",
      "DATA",
      [
        "storage",
        "00bea9e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004f0444",
      "READ",
      [
        "storage",
        "00c1af70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f041c",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "004f0438",
      "DATA",
      [
        "storage",
        "00beaa38",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004f0444",
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f041c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f0/004f03d8.md#insn-004f041c) · [`004f0434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f0/004f03d8.md#insn-004f0434)
- 新版 `004f041c`（命令位置の公開資料なし） · `004f0434`（命令位置の公開資料なし）

~~~diff
- 004f041c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
- 004f041c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f041c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
+ 004f041c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f041c bytes 084941f9
+ 004f041c bytes 087141f9
- 004f0434 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 004f0434 bytes f40300aa
+ 004f0434 ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 004f0434 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-593da8cb841720007e34808dec31fe86"></a>

### [`004f0f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f0/004f0f78.md) → [`004f0f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f0f78.md) _ZNK5Botan8X509_CRL4dataEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcbb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcbb0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdcc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc00.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

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
      "definition_site": "004f1014",
      "incomplete_value": true,
      "site": "004f1020",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1014",
      "incomplete_value": true,
      "site": "004f1020",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
              ]
            ]
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
      "004f1014",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "004f1014",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004f1014",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "004f1014",
      "PARAM",
      [
        "storage",
        "00be93d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f1014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f0/004f0f78.md#insn-004f1014)
- 新版 `004f1014`（命令位置の公開資料なし）

~~~diff
- 004f1014 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 004f1014 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f1014 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 004f1014 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004f1014 bytes 218447f9
+ 004f1014 bytes 21ac47f9
~~~


<a id="compare-3d942205ee4e38079ccaf6547d0256ac"></a>

### [`004f10f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f1/004f10f4.md) → [`004f10f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f10f4.md) _ZN5Botan7X509_DNC1ERKNSt6__ndk18multimapINS_3OIDENS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS1_4lessIS3_EENS7_INS1_4pair

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdccb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdccb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f113c",
      "incomplete_value": true,
      "site": "004f1144",
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
      "definition_site": "004f113c",
      "incomplete_value": true,
      "site": "004f1144",
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
      "004f1130",
      "READ",
      [
        "storage",
        "00c1b290",
        null,
        "pointer"
      ]
    ],
    [
      "004f1144",
      "DATA",
      [
        "storage",
        "00bea9e8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004f1130",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "004f1144",
      "DATA",
      [
        "storage",
        "00beaa38",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f1130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f1/004f10f4.md#insn-004f1130)
- 新版 `004f1130`（命令位置の公開資料なし）

~~~diff
- 004f1130 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
- 004f1130 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f1130 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
+ 004f1130 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f1130 bytes 084941f9
+ 004f1130 bytes 087141f9
~~~


<a id="compare-76f454531963458c4d9b3c0c050801f2"></a>

### [`004f1394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f1/004f1394.md) → [`004f1394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1394.md) _ZN5Botan7X509_DNC2ERKNSt6__ndk18multimapINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_NS1_4lessIS8_EENS6_INS1_4pairIKS8_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7e0.md) [`00bdcc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc60.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md) [`00bdccb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdccb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.52% / 新版 95.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f13f0",
      "incomplete_value": true,
      "site": "004f13f8",
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
      "definition_site": "004f13f0",
      "incomplete_value": true,
      "site": "004f13f8",
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
    "ordinal": 16,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f13e4",
      "READ",
      [
        "storage",
        "00c1b290",
        null,
        "pointer"
      ]
    ],
    [
      "004f13f8",
      "DATA",
      [
        "storage",
        "00bea9e8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004f13e4",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "004f13f8",
      "DATA",
      [
        "storage",
        "00beaa38",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f13e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f1/004f1394.md#insn-004f13e4)
- 新版 `004f13e4`（命令位置の公開資料なし）

~~~diff
- 004f13e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
- 004f13e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f13e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
+ 004f13e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f13e4 bytes 084941f9
+ 004f13e4 bytes 087141f9
~~~


<a id="compare-631d41aac1ce92f700d84784984e09de"></a>

### [`004f1734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f1/004f1734.md) → [`004f1734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1734.md) _ZN5Botan7X509_DN16deref_info_fieldERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdccd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdccd0.md) · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f354.md)
- 新版 呼出元 1件 [`00bdcd20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd20.md) · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.83% / 新版 88.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f1914",
      "incomplete_value": true,
      "site": "004f1914",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:96d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1914",
      "incomplete_value": true,
      "site": "004f1914",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:9fa:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "004f1908",
      "incomplete_value": true,
      "site": "004f1918",
      "value": [
        "LOAD",
        "8",
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
                "const:7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1908",
      "incomplete_value": true,
      "site": "004f1918",
      "value": [
        "LOAD",
        "8",
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
                "const:7:8"
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
      "definition_site": "004f192c",
      "incomplete_value": true,
      "site": "004f193c",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:51b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f192c",
      "incomplete_value": true,
      "site": "004f193c",
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
                "const:2a0000:8"
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
      "004f1888",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ],
    [
      "004f18c8",
      "PARAM",
      [
        "storage",
        "002afbc3",
        null,
        "string"
      ]
    ],
    [
      "004f18dc",
      "PARAM",
      [
        "storage",
        "002a1645",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f1888",
      "PARAM",
      [
        "storage",
        "002a570e",
        null,
        null
      ]
    ],
    [
      "004f18c8",
      "PARAM",
      [
        "storage",
        "002afb2f",
        null,
        "string"
      ]
    ],
    [
      "004f18dc",
      "PARAM",
      [
        "storage",
        "002a16d0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f1888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f1/004f1734.md#insn-004f1888) · [`004f18c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f1/004f1734.md#insn-004f18c8) · [`004f18dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f1/004f1734.md#insn-004f18dc)
- 新版 `004f1888`（命令位置の公開資料なし） · `004f18c8`（命令位置の公開資料なし） · `004f18dc`（命令位置の公開資料なし）

~~~diff
- 004f1888 ["COPY", "tmp:0:8", ["const:683:8"]]
- 004f1888 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004f1888 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004f1888 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004f1888 ["COPY", "tmp:0:8", ["const:70e:8"]]
+ 004f1888 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004f1888 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004f1888 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004f1888 bytes 210c1a91
+ 004f1888 bytes 21381c91
- 004f18c8 ["COPY", "tmp:0:8", ["const:bc3:8"]]
- 004f18c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004f18c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004f18c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004f18c8 ["COPY", "tmp:0:8", ["const:b2f:8"]]
+ 004f18c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004f18c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004f18c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004f18c8 bytes 210c2f91
+ 004f18c8 bytes 21bc2c91
- 004f18dc ["COPY", "tmp:0:8", ["const:645:8"]]
- 004f18dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004f18dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004f18dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004f18dc ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 004f18dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004f18dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004f18dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004f18dc bytes 21141991
+ 004f18dc bytes 21401b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c74d171394c1bde4ca82f337a95404b9"></a>

### [`004f1ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f1/004f1ecc.md) → [`004f1ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1ecc.md) _ZNK5Botan7X509_DN11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004dcbd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dcbd4.md) [`0050b45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050b/0050b45c.md) · 呼出先 11件 [`004f2228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f2228.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) [`00526790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00526/00526790.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 2件 [`004dcbd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dcbd4.md) [`0050b45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050b/0050b45c.md) · 呼出先 11件 [`004f2228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f2228.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00526790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526790.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.10% / 新版 90.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f1fa4",
      "incomplete_value": true,
      "site": "004f1fa4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:97d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1fa4",
      "incomplete_value": true,
      "site": "004f1fa4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:a0a:8"
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
      "definition_site": "004f1fec",
      "incomplete_value": true,
      "site": "004f1fec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a5000:8"
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
      "definition_site": "004f1fec",
      "incomplete_value": true,
      "site": "004f1fec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:46d:8"
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
      "definition_site": "004f1ff0",
      "incomplete_value": true,
      "site": "004f1ff0",
      "value": [
        "LOAD",
        "8",
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
                "const:5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1ff0",
      "incomplete_value": true,
      "site": "004f1ff0",
      "value": [
        "LOAD",
        "8",
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
                "const:5:8"
              ]
            ]
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
      "004f1f94",
      "READ",
      [
        "storage",
        "00296a0a",
        null,
        "string"
      ]
    ],
    [
      "004f1fdc",
      "READ",
      [
        "storage",
        "002a546d",
        null,
        "string"
      ]
    ],
    [
      "004f1fe0",
      "READ",
      [
        "storage",
        "002a5472",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f1f94",
      "READ",
      [
        "storage",
        "0029697d",
        null,
        "string"
      ]
    ],
    [
      "004f1fdc",
      "READ",
      [
        "storage",
        "002a54f8",
        null,
        "string"
      ]
    ],
    [
      "004f1fe0",
      "READ",
      [
        "storage",
        "002a54fd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f1f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f1/004f1ecc.md#insn-004f1f8c) · [`004f1fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f1/004f1ecc.md#insn-004f1fd4) · [`004f201c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f1/004f1ecc.md#insn-004f201c)
- 新版 `004f1f8c`（命令位置の公開資料なし） · `004f1fd4`（命令位置の公開資料なし） · `004f201c`（命令位置の公開資料なし）

~~~diff
- 004f1f8c ["COPY", "tmp:0:8", ["const:a0a:8"]]
- 004f1f8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f1f8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f1f8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f1f8c ["COPY", "tmp:0:8", ["const:97d:8"]]
+ 004f1f8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f1f8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f1f8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f1f8c bytes 29292891
+ 004f1f8c bytes 29f52591
- 004f1fd4 ["COPY", "tmp:0:8", ["const:46d:8"]]
- 004f1fd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f1fd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f1fd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f1fd4 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 004f1fd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f1fd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f1fd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f1fd4 bytes 29b51191
+ 004f1fd4 bytes 29e11391
- 004f201c ["COPY", "tmp:0:8", ["const:a01:8"]]
- 004f201c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f201c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f201c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f201c ["COPY", "tmp:0:8", ["const:974:8"]]
+ 004f201c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f201c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f201c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f201c bytes 29052891
+ 004f201c bytes 29d12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72b1f40283d4d183d078cd248fb7833e"></a>

### [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) → [`004f27ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md) _ZN5Botan10Extensions15create_extn_objERKNS_3OIDEbRKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdcf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf40.md) · 呼出先 27件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`004e0d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e0/004e0d1c.md) [`004f3788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3788.md) [`004f3830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3830.md) [`004f38d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f38d8.md)
- 新版 呼出元 1件 [`00bdcf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf90.md) · 呼出先 27件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`004e0d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0d1c.md) [`004f3788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3788.md) [`004f3830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3830.md) [`004f38d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f38d8.md)

変更の種類 call_argument_candidate, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 31.46% / 新版 31.46%

CFGの説明率　旧版 9.61% / 新版 9.61%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件, `unresolved_branch_alignment` 95件, `unresolved_call_alignment` 53件, `unresolved_store_alignment` 65件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004f2844"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004f284c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004f2850"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:004f2840",
      "READ",
      [
        "storage",
        "002a43d3",
        null,
        "string"
      ]
    ],
    [
      "unmatched:004f2844",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ],
    [
      "unmatched:004f2850",
      "WRITE",
      [
        "storage",
        "Stack[-0x8f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f2840",
      "READ",
      [
        "storage",
        "002a445e",
        null,
        "string"
      ]
    ],
    [
      "004f2844",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ],
    [
      "004f2850",
      "WRITE",
      [
        "storage",
        "Stack[-0x8f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f2844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md#insn-004f2844) · [`004f284c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md#insn-004f284c)
- 新版 `004f2844`（命令位置の公開資料なし）

~~~diff
- 004f2844 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 004f2844 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd0:8"]]
- 004f2844 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 004f2844 bytes a8031d38
+ 004f2844 ["COPY", "tmp:0:4", ["register:4040:4"]]
+ 004f2844 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd0:8"]]
+ 004f2844 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 004f2844 bytes a8031d38
- 004f284c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 004f284c ["COPY", "tmp:1:8", ["const:0:8"]]
- 004f284c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 004f284c bytes 7f0200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8704cc5130b80bc97f31f6ecdd4c33a7"></a>

### [`004f3788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3788.md) → [`004f3788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3788.md) FUN_004f3788

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f37c0",
      "incomplete_value": true,
      "site": "004f37c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:294000:8"
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
    "old": {
      "definition_site": "004f37c0",
      "incomplete_value": true,
      "site": "004f37c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:294000:8"
              ],
              [
                "leaf",
                "const:7ad:8"
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
      "004f37b0",
      "READ",
      [
        "storage",
        "002947ad",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f37b0",
      "READ",
      [
        "storage",
        "00294720",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f37a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3788.md#insn-004f37a4)
- 新版 `004f37a4`（命令位置の公開資料なし）

~~~diff
- 004f37a4 ["COPY", "tmp:0:8", ["const:7ad:8"]]
- 004f37a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f37a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f37a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f37a4 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 004f37a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f37a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f37a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f37a4 bytes 29b51e91
+ 004f37a4 bytes 29811c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ea56c0a4f707ebce8888f4808933b1a"></a>

### [`004f38d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f38d8.md) → [`004f38d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f38d8.md) FUN_004f38d8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f3910",
      "incomplete_value": true,
      "site": "004f3910",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:297000:8"
              ],
              [
                "leaf",
                "const:a54:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f3910",
      "incomplete_value": true,
      "site": "004f3910",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:297000:8"
              ],
              [
                "leaf",
                "const:ae1:8"
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
      "004f3900",
      "READ",
      [
        "storage",
        "00297ae1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f3900",
      "READ",
      [
        "storage",
        "00297a54",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f38f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f38d8.md#insn-004f38f4)
- 新版 `004f38f4`（命令位置の公開資料なし）

~~~diff
- 004f38f4 ["COPY", "tmp:0:8", ["const:ae1:8"]]
- 004f38f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f38f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f38f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f38f4 ["COPY", "tmp:0:8", ["const:a54:8"]]
+ 004f38f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f38f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f38f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f38f4 bytes 29852b91
+ 004f38f4 bytes 29512991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2b876bf4e5f49f86903920184a42fce"></a>

### [`004f3a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3a28.md) → [`004f3a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3a28.md) FUN_004f3a28

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f3a60",
      "incomplete_value": true,
      "site": "004f3a60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:477:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f3a60",
      "incomplete_value": true,
      "site": "004f3a60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:3ec:8"
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
      "004f3a50",
      "READ",
      [
        "storage",
        "0029d3ec",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f3a50",
      "READ",
      [
        "storage",
        "0029d477",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f3a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3a28.md#insn-004f3a44)
- 新版 `004f3a44`（命令位置の公開資料なし）

~~~diff
- 004f3a44 ["COPY", "tmp:0:8", ["const:3ec:8"]]
- 004f3a44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f3a44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f3a44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f3a44 ["COPY", "tmp:0:8", ["const:477:8"]]
+ 004f3a44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f3a44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f3a44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f3a44 bytes 29b10f91
+ 004f3a44 bytes 29dd1191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bd950f91974272ef758b8ff56a678ae"></a>

### [`004f3ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3ad0.md) → [`004f3ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3ad0.md) FUN_004f3ad0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f3b08",
      "incomplete_value": true,
      "site": "004f3b08",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:369:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f3b08",
      "incomplete_value": true,
      "site": "004f3b08",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:36b:8"
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
      "004f3af8",
      "READ",
      [
        "storage",
        "0029b36b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f3af8",
      "READ",
      [
        "storage",
        "0029b369",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f3aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3ad0.md#insn-004f3aec)
- 新版 `004f3aec`（命令位置の公開資料なし）

~~~diff
- 004f3aec ["COPY", "tmp:0:8", ["const:36b:8"]]
- 004f3aec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f3aec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f3aec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f3aec ["COPY", "tmp:0:8", ["const:369:8"]]
+ 004f3aec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f3aec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f3aec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f3aec bytes 29ad0d91
+ 004f3aec bytes 29a50d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ffc84c66e1e79aa4dc08018be1d8baa"></a>

### [`004f3b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3b78.md) → [`004f3b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3b78.md) FUN_004f3b78

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f3ba0",
      "incomplete_value": true,
      "site": "004f3bb0",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:49d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f3ba0",
      "incomplete_value": true,
      "site": "004f3bb0",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:412:8"
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
      "004f3ba0",
      "READ",
      [
        "storage",
        "002a0412",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f3ba0",
      "READ",
      [
        "storage",
        "002a049d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f3b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3b78.md#insn-004f3b94)
- 新版 `004f3b94`（命令位置の公開資料なし）

~~~diff
- 004f3b94 ["COPY", "tmp:0:8", ["const:412:8"]]
- 004f3b94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f3b94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f3b94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f3b94 ["COPY", "tmp:0:8", ["const:49d:8"]]
+ 004f3b94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f3b94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f3b94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f3b94 bytes 29491091
+ 004f3b94 bytes 29751291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c4ba10ea07512623dd7fd32e60a6871"></a>

### [`004f3c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3c20.md) → [`004f3c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3c20.md) FUN_004f3c20

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 5件 [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md) · 呼出先 5件 [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f3c68",
      "incomplete_value": true,
      "site": "004f3c68",
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
      "definition_site": "004f3c68",
      "incomplete_value": true,
      "site": "004f3c68",
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
    "kind": "store_value",
    "new": {
      "definition_site": "004f3c68",
      "incomplete_value": true,
      "site": "004f3c68",
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
      "definition_site": "004f3c68",
      "incomplete_value": true,
      "site": "004f3c68",
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
      "004f3c48",
      "READ",
      [
        "storage",
        "00c1b3a0",
        null,
        "pointer"
      ]
    ],
    [
      "004f3c54",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "004f3c68",
      "DATA",
      [
        "storage",
        "00bebed8",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "004f3c48",
      "READ",
      [
        "storage",
        "00c1b3f0",
        null,
        "pointer"
      ]
    ],
    [
      "004f3c54",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "004f3c68",
      "DATA",
      [
        "storage",
        "00bebf28",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f3c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3c20.md#insn-004f3c48) · [`004f3c50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3c20.md#insn-004f3c50)
- 新版 `004f3c48`（命令位置の公開資料なし） · `004f3c50`（命令位置の公開資料なし）

~~~diff
- 004f3c48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a0:8"]]
- 004f3c48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f3c48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3f0:8"]]
+ 004f3c48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f3c48 bytes 08d141f9
+ 004f3c48 bytes 08f941f9
- 004f3c50 ["COPY", "register:4098:8", ["register:4000:8"]]
- 004f3c50 bytes f30300aa
+ 004f3c50 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 004f3c50 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-329b36c709467c45821671047cef23f2"></a>

### [`004f3f14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3f14.md) → [`004f3f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3f14.md) _ZNK5Botan10Extensions20get_extension_objectERKNS_3OIDE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc20.md) · 呼出先 1件 [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 1件 [`00bdcc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc70.md) · 呼出先 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f400c",
      "incomplete_value": false,
      "site": "004f402c",
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
            "const:d8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f400c",
      "incomplete_value": false,
      "site": "004f402c",
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
            "const:d8e:8"
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
      "definition_site": "004f4014",
      "incomplete_value": false,
      "site": "004f402c",
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
      "definition_site": "004f4014",
      "incomplete_value": false,
      "site": "004f402c",
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f4024",
      "incomplete_value": false,
      "site": "004f402c",
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
            "const:cc1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f4024",
      "incomplete_value": false,
      "site": "004f402c",
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
            "const:697:8"
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
      "004f400c",
      "PARAM",
      [
        "storage",
        "00299d8e",
        null,
        "string"
      ]
    ],
    [
      "004f4014",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "004f4024",
      "PARAM",
      [
        "storage",
        "002a9697",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f400c",
      "PARAM",
      [
        "storage",
        "00299d8c",
        null,
        "string"
      ]
    ],
    [
      "004f4014",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "004f4024",
      "PARAM",
      [
        "storage",
        "00299cc1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f400c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3f14.md#insn-004f400c) · [`004f4014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3f14.md#insn-004f4014) · [`004f4020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3f14.md#insn-004f4020)
- 新版 `004f400c`（命令位置の公開資料なし） · `004f4014`（命令位置の公開資料なし） · `004f4020`（命令位置の公開資料なし）

~~~diff
- 004f400c ["COPY", "tmp:0:8", ["const:d8e:8"]]
- 004f400c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004f400c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004f400c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004f400c ["COPY", "tmp:0:8", ["const:d8c:8"]]
+ 004f400c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004f400c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004f400c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004f400c bytes 00383691
+ 004f400c bytes 00303691
- 004f4014 ["COPY", "tmp:0:8", ["const:866:8"]]
- 004f4014 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004f4014 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004f4014 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004f4014 ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 004f4014 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004f4014 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004f4014 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004f4014 bytes 21982191
+ 004f4014 bytes 21641f91
- 004f4020 ["COPY", "register:4018:8", ["const:2a9000:8"]]
+ 004f4020 ["COPY", "register:4018:8", ["const:299000:8"]]
- 004f4020 bytes a3edffb0
+ 004f4020 bytes 23edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6e751b6bb8ca8136065bf9c9a86b584"></a>

### [`004f4030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4030.md) → [`004f4030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f4030.md) _ZNK5Botan10Extensions10extensionsEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf60.md) · 呼出先 3件 [`00529214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00529/00529214.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 1件 [`00bdcfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcfb0.md) · 呼出先 3件 [`00529214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529214.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f414c",
      "incomplete_value": false,
      "site": "004f416c",
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
            "const:d8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f414c",
      "incomplete_value": false,
      "site": "004f416c",
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
            "const:d8e:8"
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
      "definition_site": "004f4154",
      "incomplete_value": false,
      "site": "004f416c",
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
      "definition_site": "004f4154",
      "incomplete_value": false,
      "site": "004f416c",
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
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f4164",
      "incomplete_value": false,
      "site": "004f416c",
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
            "const:cc1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f4164",
      "incomplete_value": false,
      "site": "004f416c",
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
            "const:697:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f414c",
      "PARAM",
      [
        "storage",
        "00299d8e",
        null,
        "string"
      ]
    ],
    [
      "004f4154",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "004f4164",
      "PARAM",
      [
        "storage",
        "002a9697",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f414c",
      "PARAM",
      [
        "storage",
        "00299d8c",
        null,
        "string"
      ]
    ],
    [
      "004f4154",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "004f4164",
      "PARAM",
      [
        "storage",
        "00299cc1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f414c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4030.md#insn-004f414c) · [`004f4154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4030.md#insn-004f4154) · [`004f4160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4030.md#insn-004f4160)
- 新版 `004f414c`（命令位置の公開資料なし） · `004f4154`（命令位置の公開資料なし） · `004f4160`（命令位置の公開資料なし）

~~~diff
- 004f414c ["COPY", "tmp:0:8", ["const:d8e:8"]]
- 004f414c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004f414c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004f414c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004f414c ["COPY", "tmp:0:8", ["const:d8c:8"]]
+ 004f414c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004f414c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004f414c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004f414c bytes 00383691
+ 004f414c bytes 00303691
- 004f4154 ["COPY", "tmp:0:8", ["const:866:8"]]
- 004f4154 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004f4154 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004f4154 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004f4154 ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 004f4154 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004f4154 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004f4154 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004f4154 bytes 21982191
+ 004f4154 bytes 21641f91
- 004f4160 ["COPY", "register:4018:8", ["const:2a9000:8"]]
+ 004f4160 ["COPY", "register:4018:8", ["const:299000:8"]]
- 004f4160 bytes a3edffb0
+ 004f4160 bytes 23edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afb045fc85d328584167cb1f6314dd81"></a>

### [`004f43b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f43b8.md) → [`004f43b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f43b8.md) _ZNK5Botan10Extensions11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004ef204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004ef204.md) · 呼出先 9件 [`004f45b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f45b0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`004ef204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef204.md) · 呼出先 9件 [`004f45b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f45b0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f4558",
      "incomplete_value": false,
      "site": "004f4578",
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
            "const:d8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f4558",
      "incomplete_value": false,
      "site": "004f4578",
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
            "const:d8e:8"
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
      "definition_site": "004f4560",
      "incomplete_value": false,
      "site": "004f4578",
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
      "definition_site": "004f4560",
      "incomplete_value": false,
      "site": "004f4578",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f4570",
      "incomplete_value": false,
      "site": "004f4578",
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
            "const:cc1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f4570",
      "incomplete_value": false,
      "site": "004f4578",
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
            "const:697:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f4558",
      "PARAM",
      [
        "storage",
        "00299d8e",
        null,
        "string"
      ]
    ],
    [
      "004f4560",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "004f4570",
      "PARAM",
      [
        "storage",
        "002a9697",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f4558",
      "PARAM",
      [
        "storage",
        "00299d8c",
        null,
        "string"
      ]
    ],
    [
      "004f4560",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "004f4570",
      "PARAM",
      [
        "storage",
        "00299cc1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f4558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f43b8.md#insn-004f4558) · [`004f4560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f43b8.md#insn-004f4560) · [`004f456c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f43b8.md#insn-004f456c)
- 新版 `004f4558`（命令位置の公開資料なし） · `004f4560`（命令位置の公開資料なし） · `004f456c`（命令位置の公開資料なし）

~~~diff
- 004f4558 ["COPY", "tmp:0:8", ["const:d8e:8"]]
- 004f4558 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004f4558 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004f4558 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004f4558 ["COPY", "tmp:0:8", ["const:d8c:8"]]
+ 004f4558 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004f4558 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004f4558 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004f4558 bytes 00383691
+ 004f4558 bytes 00303691
- 004f4560 ["COPY", "tmp:0:8", ["const:866:8"]]
- 004f4560 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004f4560 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004f4560 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004f4560 ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 004f4560 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004f4560 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004f4560 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004f4560 bytes 21982191
+ 004f4560 bytes 21641f91
- 004f456c ["COPY", "register:4018:8", ["const:2a9000:8"]]
+ 004f456c ["COPY", "register:4018:8", ["const:299000:8"]]
- 004f456c bytes a3edffb0
+ 004f456c bytes 23edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79cb791c680439ae9a7db30cef5c3efe"></a>

### [`004f45b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f45b0.md) → [`004f45b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f45b0.md) FUN_004f45b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`004f43b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f43b8.md) [`00519534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00519/00519534.md) [`005273ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00527/005273ec.md) · 呼出先 5件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 3件 [`004f43b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f43b8.md) [`00519534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519534.md) [`005273ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/005273ec.md) · 呼出先 5件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.31% / 新版 95.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f45ec",
      "incomplete_value": true,
      "site": "004f45f0",
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
      "definition_site": "004f45ec",
      "incomplete_value": true,
      "site": "004f45f0",
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
      "004f45dc",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "004f45f0",
      "DATA",
      [
        "storage",
        "00be9278",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004f45dc",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "004f45f0",
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f45dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f45b0.md#insn-004f45dc)
- 新版 `004f45dc`（命令位置の公開資料なし）

~~~diff
- 004f45dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
- 004f45dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f45dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
+ 004f45dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f45dc bytes 088147f9
+ 004f45dc bytes 08a947f9
~~~


<a id="compare-262295400ff7a87d70e718d120b2f972"></a>

### [`004f4778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4778.md) → [`004f4778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f4778.md) _ZN5Botan10Extensions11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004e0894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e0/004e0894.md) [`004f03d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f0/004f03d8.md) · 呼出先 21件 [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`004f4d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4d5c.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`0051854c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/0051854c.md) [`00528a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00528/00528a6c.md)
- 新版 呼出元 2件 [`004e0894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0894.md) [`004f03d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f03d8.md) · 呼出先 21件 [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`004f4d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f4d5c.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`0051854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md) [`00528a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528a6c.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.27% / 新版 97.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f48e8",
      "incomplete_value": true,
      "site": "004f48e8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f48e8",
      "incomplete_value": true,
      "site": "004f48e8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f4a84",
      "incomplete_value": true,
      "site": "004f4a84",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f4a84",
      "incomplete_value": true,
      "site": "004f4a84",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f4800",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "004f48d8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004f4930",
      "DATA",
      [
        "storage",
        "00be9278",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004f4800",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "004f48d8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004f4930",
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f4800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4778.md#insn-004f4800) · [`004f48d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4778.md#insn-004f48d8) · [`004f4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4778.md#insn-004f4a74)
- 新版 `004f4800`（命令位置の公開資料なし） · `004f48d8`（命令位置の公開資料なし） · `004f4a74`（命令位置の公開資料なし）

~~~diff
- 004f4800 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
- 004f4800 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f4800 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
+ 004f4800 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f4800 bytes 088147f9
+ 004f4800 bytes 08a947f9
- 004f48d8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:728:8"]]
- 004f48d8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f48d8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:778:8"]]
+ 004f48d8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f48d8 bytes 499743f9
+ 004f48d8 bytes 49bf43f9
- 004f4a74 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:728:8"]]
- 004f4a74 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f4a74 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:778:8"]]
+ 004f4a74 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f4a74 bytes 499743f9
+ 004f4a74 bytes 49bf43f9
~~~


<a id="compare-82a72c982cc213d0c62266ceaee047c0"></a>

### [`004f4d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4d5c.md) → [`004f4d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f4d5c.md) FUN_004f4d5c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f4778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4778.md) · 呼出先 3件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`004f4778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f4778.md) · 呼出先 3件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f4dac",
      "incomplete_value": true,
      "site": "004f4dac",
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
      "definition_site": "004f4dac",
      "incomplete_value": true,
      "site": "004f4dac",
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
      "004f4d98",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "004f4dac",
      "DATA",
      [
        "storage",
        "00bed428",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "004f4d98",
      "READ",
      [
        "storage",
        "00c1b330",
        null,
        "pointer"
      ]
    ],
    [
      "004f4dac",
      "DATA",
      [
        "storage",
        "00bed478",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f4d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4d5c.md#insn-004f4d98)
- 新版 `004f4d98`（命令位置の公開資料なし）

~~~diff
- 004f4d98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
- 004f4d98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f4d98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:330:8"]]
+ 004f4d98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f4d98 bytes 087141f9
+ 004f4d98 bytes 089941f9
~~~


<a id="compare-48511a67e02c7fc10095efdfebf7be2c"></a>

### [`004f4e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4e50.md) → [`004f4e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f4e50.md) _ZNK5Botan10Extensions11contents_toERNS_10Data_StoreES2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf80.md) · 呼出先 6件 [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 1件 [`00bdcfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcfd0.md) · 呼出先 6件 [`004dc2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f4fd0",
      "incomplete_value": false,
      "site": "004f4ff0",
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
            "const:d8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f4fd0",
      "incomplete_value": false,
      "site": "004f4ff0",
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
            "const:d8e:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f4fd8",
      "incomplete_value": false,
      "site": "004f4ff0",
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
      "definition_site": "004f4fd8",
      "incomplete_value": false,
      "site": "004f4ff0",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f4fe8",
      "incomplete_value": false,
      "site": "004f4ff0",
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
            "const:cc1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f4fe8",
      "incomplete_value": false,
      "site": "004f4ff0",
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
            "const:697:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f4edc",
      "PARAM",
      [
        "storage",
        "002a5685",
        null,
        "string"
      ]
    ],
    [
      "004f4fd0",
      "PARAM",
      [
        "storage",
        "00299d8e",
        null,
        "string"
      ]
    ],
    [
      "004f4fd8",
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
      "004f4edc",
      "PARAM",
      [
        "storage",
        "002a5710",
        null,
        "string"
      ]
    ],
    [
      "004f4fd0",
      "PARAM",
      [
        "storage",
        "00299d8c",
        null,
        "string"
      ]
    ],
    [
      "004f4fd8",
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

- 旧版 [`004f4e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4e50.md#insn-004f4e90) · [`004f4fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4e50.md#insn-004f4fd0) · [`004f4fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4e50.md#insn-004f4fd8)
- 新版 `004f4e90`（命令位置の公開資料なし） · `004f4fd0`（命令位置の公開資料なし） · `004f4fd8`（命令位置の公開資料なし）

~~~diff
- 004f4e90 ["COPY", "tmp:0:8", ["const:685:8"]]
- 004f4e90 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 004f4e90 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 004f4e90 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 004f4e90 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 004f4e90 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 004f4e90 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 004f4e90 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 004f4e90 bytes b5161a91
+ 004f4e90 bytes b5421c91
- 004f4fd0 ["COPY", "tmp:0:8", ["const:d8e:8"]]
- 004f4fd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004f4fd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004f4fd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004f4fd0 ["COPY", "tmp:0:8", ["const:d8c:8"]]
+ 004f4fd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004f4fd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004f4fd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004f4fd0 bytes 00383691
+ 004f4fd0 bytes 00303691
- 004f4fd8 ["COPY", "tmp:0:8", ["const:866:8"]]
- 004f4fd8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004f4fd8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004f4fd8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004f4fd8 ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 004f4fd8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004f4fd8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004f4fd8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004f4fd8 bytes 21982191
+ 004f4fd8 bytes 21641f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a54e320a33177d16d0f54e0a51e6d5f7"></a>

### [`004f52c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f52c8.md) → [`004f52c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f5/004f52c8.md) _ZN5Botan14Cert_Extension17Basic_Constraints12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb860.md) [`00bdb870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb870.md) [`00bdb9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb9e0.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md) · 呼出先 8件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8b0.md) [`00bdb8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8c0.md) [`00bdba30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba30.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f537c",
      "incomplete_value": true,
      "site": "004f537c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "004f537c",
      "incomplete_value": true,
      "site": "004f537c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f53c0",
      "incomplete_value": true,
      "site": "004f53c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "004f53c0",
      "incomplete_value": true,
      "site": "004f53c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
    "ordinal": 9,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f536c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004f53b0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f536c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004f53b0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f536c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f52c8.md#insn-004f536c) · [`004f53b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f52c8.md#insn-004f53b0)
- 新版 `004f536c`（命令位置の公開資料なし） · `004f53b0`（命令位置の公開資料なし）

~~~diff
- 004f536c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 004f536c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f536c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 004f536c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f536c bytes c99643f9
+ 004f536c bytes c9be43f9
- 004f53b0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 004f53b0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f53b0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 004f53b0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f53b0 bytes c99643f9
+ 004f53b0 bytes c9be43f9
~~~


<a id="compare-b698643712700a4aace0b6458a9468dc"></a>

### [`004f543c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f543c.md) → [`004f543c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f5/004f543c.md) _ZNK5Botan14Cert_Extension17Basic_Constraints11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8f0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004dc2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb940.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f54ec",
      "incomplete_value": true,
      "site": "004f5504",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f54ec",
      "incomplete_value": true,
      "site": "004f5504",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:5dc:8"
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
      "definition_site": "004f54ec",
      "incomplete_value": true,
      "site": "004f5504",
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
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f54ec",
      "incomplete_value": true,
      "site": "004f5504",
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
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
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
      "definition_site": "004f5508",
      "incomplete_value": true,
      "site": "004f5508",
      "value": [
        "LOAD",
        "8",
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
                "const:1f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5508",
      "incomplete_value": true,
      "site": "004f5508",
      "value": [
        "LOAD",
        "8",
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
                "const:1f:8"
              ]
            ]
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
      "004f54ec",
      "READ",
      [
        "storage",
        "002a75dc",
        null,
        "string"
      ]
    ],
    [
      "004f54ec",
      "READ",
      [
        "storage",
        "002a75ec",
        null,
        "string"
      ]
    ],
    [
      "004f54f4",
      "READ",
      [
        "storage",
        "002a75fb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f54ec",
      "READ",
      [
        "storage",
        "002a7676",
        null,
        "string"
      ]
    ],
    [
      "004f54ec",
      "READ",
      [
        "storage",
        "002a7686",
        null,
        "string"
      ]
    ],
    [
      "004f54f4",
      "READ",
      [
        "storage",
        "002a7695",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f54e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f543c.md#insn-004f54e4) · [`004f54e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f543c.md#insn-004f54e8)
- 新版 `004f54e4`（命令位置の公開資料なし） · `004f54e8`（命令位置の公開資料なし）

~~~diff
- 004f54e4 ["COPY", "tmp:0:8", ["const:5dc:8"]]
- 004f54e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004f54e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004f54e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004f54e4 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 004f54e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004f54e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004f54e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004f54e4 bytes 08711791
+ 004f54e4 bytes 08d91991
- 004f54e8 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 004f54e8 bytes c9edfff0
+ 004f54e8 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 004f54e8 bytes c9edfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae3875373359e4c17a79dbd69a98caf9"></a>

### [`004f55c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f55c0.md) → [`004f55c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f5/004f55c0.md) _ZNK5Botan14Cert_Extension9Key_Usage12encode_innerEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.07% / 新版 99.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f5888",
      "incomplete_value": false,
      "site": "004f5890",
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
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5888",
      "incomplete_value": false,
      "site": "004f5890",
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
            "const:645:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f58c0",
      "incomplete_value": true,
      "site": "004f58cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004f58c0",
      "incomplete_value": true,
      "site": "004f58cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
              ]
            ]
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
      "004f5888",
      "PARAM",
      [
        "storage",
        "002a0645",
        null,
        "string"
      ]
    ],
    [
      "004f58c0",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "004f58c0",
      "PARAM",
      [
        "storage",
        "00be92e0",
        "_ZTIN5Botan14Encoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004f5888",
      "PARAM",
      [
        "storage",
        "002a06d0",
        null,
        "string"
      ]
    ],
    [
      "004f58c0",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "004f58c0",
      "PARAM",
      [
        "storage",
        "00be9330",
        "_ZTIN5Botan14Encoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f5888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f55c0.md#insn-004f5888) · [`004f58c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f55c0.md#insn-004f58c0)
- 新版 `004f5888`（命令位置の公開資料なし） · `004f58c0`（命令位置の公開資料なし）

~~~diff
- 004f5888 ["COPY", "tmp:0:8", ["const:645:8"]]
- 004f5888 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004f5888 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004f5888 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004f5888 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 004f5888 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004f5888 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004f5888 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004f5888 bytes 21141991
+ 004f5888 bytes 21401b91
- 004f58c0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
- 004f58c0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f58c0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
+ 004f58c0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004f58c0 bytes 21ac47f9
+ 004f58c0 bytes 21d447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bab74cf448533f7f6b54444de98cd05"></a>

### [`004f5994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f5994.md) → [`004f5994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f5/004f5994.md) _ZN5Botan14Cert_Extension9Key_Usage12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.68% / 新版 96.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f5c4c",
      "incomplete_value": true,
      "site": "004f5c4c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "004f5c4c",
      "incomplete_value": true,
      "site": "004f5c4c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f5c90",
      "incomplete_value": true,
      "site": "004f5c90",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "004f5c90",
      "incomplete_value": true,
      "site": "004f5c90",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f5cd0",
      "incomplete_value": false,
      "site": "004f5cd8",
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
            "const:591:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5cd0",
      "incomplete_value": false,
      "site": "004f5cd8",
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
            "const:506:8"
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
      "004f5c3c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004f5c80",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004f5cd0",
      "PARAM",
      [
        "storage",
        "0029e506",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f5c3c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004f5c80",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004f5cd0",
      "PARAM",
      [
        "storage",
        "0029e591",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f5c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f5994.md#insn-004f5c3c) · [`004f5c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f5994.md#insn-004f5c80) · [`004f5cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f5994.md#insn-004f5cd0)
- 新版 `004f5c3c`（命令位置の公開資料なし） · `004f5c80`（命令位置の公開資料なし） · `004f5cd0`（命令位置の公開資料なし）

~~~diff
- 004f5c3c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 004f5c3c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f5c3c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 004f5c3c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f5c3c bytes c99643f9
+ 004f5c3c bytes c9be43f9
- 004f5c80 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 004f5c80 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f5c80 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 004f5c80 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f5c80 bytes c99643f9
+ 004f5c80 bytes c9be43f9
- 004f5cd0 ["COPY", "tmp:0:8", ["const:506:8"]]
- 004f5cd0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004f5cd0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004f5cd0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004f5cd0 ["COPY", "tmp:0:8", ["const:591:8"]]
+ 004f5cd0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004f5cd0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004f5cd0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004f5cd0 bytes 21181491
+ 004f5cd0 bytes 21441691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-077a36d2a0c6b3fd666e7988642c71c1"></a>

### [`004f5e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f5e48.md) → [`004f5e48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f5/004f5e48.md) _ZNK5Botan14Cert_Extension9Key_Usage11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004dc2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb940.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.80% / 新版 87.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f5e80",
      "incomplete_value": true,
      "site": "004f5e80",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:299000:8"
              ],
              [
                "leaf",
                "const:bb4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5e80",
      "incomplete_value": true,
      "site": "004f5e80",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:299000:8"
              ],
              [
                "leaf",
                "const:c41:8"
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
      "definition_site": "004f5e78",
      "incomplete_value": true,
      "site": "004f5e84",
      "value": [
        "LOAD",
        "8",
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
                "const:7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5e78",
      "incomplete_value": true,
      "site": "004f5e84",
      "value": [
        "LOAD",
        "8",
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
                "const:7:8"
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
      "004f5e68",
      "READ",
      [
        "storage",
        "00299c41",
        null,
        "string"
      ]
    ],
    [
      "004f5e78",
      "READ",
      [
        "storage",
        "00299c48",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f5e68",
      "READ",
      [
        "storage",
        "00299bb4",
        null,
        "string"
      ]
    ],
    [
      "004f5e78",
      "READ",
      [
        "storage",
        "00299bbb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f5e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f5e48.md#insn-004f5e60)
- 新版 `004f5e60`（命令位置の公開資料なし）

~~~diff
- 004f5e60 ["COPY", "tmp:0:8", ["const:c41:8"]]
- 004f5e60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f5e60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f5e60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f5e60 ["COPY", "tmp:0:8", ["const:bb4:8"]]
+ 004f5e60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f5e60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f5e60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f5e60 bytes 29053191
+ 004f5e60 bytes 29d12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-141da8ca1d7064b686afcfada50bdbab"></a>

### [`004f6118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f6/004f6118.md) → [`004f6118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f6/004f6118.md) _ZNK5Botan14Cert_Extension14Subject_Key_ID11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdcc50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc50.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdcca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcca0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.37% / 新版 85.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f6154",
      "incomplete_value": true,
      "site": "004f6164",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:334:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f6154",
      "incomplete_value": true,
      "site": "004f6164",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:2a9:8"
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
      "definition_site": "004f6158",
      "incomplete_value": true,
      "site": "004f6168",
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
              "INT_ADD",
              [
                "leaf",
                "const:b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f6158",
      "incomplete_value": true,
      "site": "004f6168",
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
              "INT_ADD",
              [
                "leaf",
                "const:b:8"
              ]
            ]
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
      "004f6154",
      "READ",
      [
        "storage",
        "002a22a9",
        null,
        "string"
      ]
    ],
    [
      "004f6158",
      "READ",
      [
        "storage",
        "002a22b4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f6154",
      "READ",
      [
        "storage",
        "002a2334",
        null,
        "string"
      ]
    ],
    [
      "004f6158",
      "READ",
      [
        "storage",
        "002a233f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f614c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f6/004f6118.md#insn-004f614c) · [`004f6150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f6/004f6118.md#insn-004f6150)
- 新版 `004f614c`（命令位置の公開資料なし） · `004f6150`（命令位置の公開資料なし）

~~~diff
- 004f614c ["COPY", "tmp:0:8", ["const:2a9:8"]]
- 004f614c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004f614c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004f614c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004f614c ["COPY", "tmp:0:8", ["const:334:8"]]
+ 004f614c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004f614c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004f614c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004f614c bytes 08a50a91
+ 004f614c bytes 08d10c91
- 004f6150 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 004f6150 bytes c9edfff0
+ 004f6150 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 004f6150 bytes c9edfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8307dafc6755ba876a3a5eb21ee99137"></a>

### [`004f61e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f6/004f61e8.md) → [`004f61e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f6/004f61e8.md) _ZN5Botan14Cert_Extension14Subject_Key_IDC2ERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEERKNS2_12basic_stringIcNS2_11char_traitsIcEENS4_IcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcea0.md) · 呼出先 7件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdcef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcef0.md) · 呼出先 7件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.46% / 新版 97.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f6228",
      "incomplete_value": true,
      "site": "004f6230",
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
      "definition_site": "004f6228",
      "incomplete_value": true,
      "site": "004f6230",
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
      "004f6224",
      "READ",
      [
        "storage",
        "00c1b370",
        null,
        "pointer"
      ]
    ],
    [
      "004f6230",
      "DATA",
      [
        "storage",
        "00beaa18",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "004f6224",
      "READ",
      [
        "storage",
        "00c1b3c0",
        null,
        "pointer"
      ]
    ],
    [
      "004f6230",
      "DATA",
      [
        "storage",
        "00beaa68",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f6224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f6/004f61e8.md#insn-004f6224)
- 新版 `004f6224`（命令位置の公開資料なし）

~~~diff
- 004f6224 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:370:8"]]
- 004f6224 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f6224 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3c0:8"]]
+ 004f6224 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f6224 bytes 29b941f9
+ 004f6224 bytes 29e141f9
~~~


<a id="compare-54ff75d732bce934a909d7069a0ae0e8"></a>

### [`004f6548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f6/004f6548.md) → [`004f6548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f6/004f6548.md) _ZN5Botan14Cert_Extension16Authority_Key_ID12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004e7de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e7/004e7de0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb860.md) [`00bdb9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb9e0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004e7de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7de0.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8b0.md) [`00bdba30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba30.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.03% / 新版 94.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f65dc",
      "incomplete_value": true,
      "site": "004f65dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
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
      "definition_site": "004f65dc",
      "incomplete_value": true,
      "site": "004f65dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f6620",
      "incomplete_value": true,
      "site": "004f6620",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
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
      "definition_site": "004f6620",
      "incomplete_value": true,
      "site": "004f6620",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
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
    "ordinal": 7,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f65cc",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004f6610",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f65cc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004f6610",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f65cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f6/004f6548.md#insn-004f65cc) · [`004f6610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f6/004f6548.md#insn-004f6610)
- 新版 `004f65cc`（命令位置の公開資料なし） · `004f6610`（命令位置の公開資料なし）

~~~diff
- 004f65cc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 004f65cc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f65cc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 004f65cc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f65cc bytes a99643f9
+ 004f65cc bytes a9be43f9
- 004f6610 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 004f6610 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f6610 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 004f6610 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f6610 bytes a99643f9
+ 004f6610 bytes a9be43f9
~~~


<a id="compare-f4e656070923e9f6495c522cc89e587c"></a>

### [`004f7170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f7170.md) → [`004f7170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7170.md) _ZNK5Botan14Cert_Extension18Extended_Key_Usage11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb960.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004dc2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.03% / 新版 94.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f71b4",
      "incomplete_value": true,
      "site": "004f71cc",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:516:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f71b4",
      "incomplete_value": true,
      "site": "004f71cc",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:47c:8"
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
      "004f71b4",
      "READ",
      [
        "storage",
        "002a947c",
        null,
        "string"
      ]
    ],
    [
      "004f71b8",
      "READ",
      [
        "storage",
        "002a948b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f71b4",
      "READ",
      [
        "storage",
        "002a9516",
        null,
        "string"
      ]
    ],
    [
      "004f71b8",
      "READ",
      [
        "storage",
        "002a9525",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f71ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f7170.md#insn-004f71ac)
- 新版 `004f71ac`（命令位置の公開資料なし）

~~~diff
- 004f71ac ["COPY", "tmp:0:8", ["const:47c:8"]]
- 004f71ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f71ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f71ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f71ac ["COPY", "tmp:0:8", ["const:516:8"]]
+ 004f71ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f71ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f71ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f71ac bytes 29f11191
+ 004f71ac bytes 29591491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72a3ffe5a90c4a7cfcbf4787391b17ad"></a>

### [`004f72c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f72c0.md) → [`004f72c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f72c0.md) _ZNK5Botan14Cert_Extension16Name_Constraints12encode_innerEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f7300",
      "incomplete_value": true,
      "site": "004f7314",
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
                "const:295000:8"
              ],
              [
                "leaf",
                "const:b47:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f7300",
      "incomplete_value": true,
      "site": "004f7314",
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
                "const:295000:8"
              ],
              [
                "leaf",
                "const:bd4:8"
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
      "definition_site": "004f7304",
      "incomplete_value": true,
      "site": "004f7318",
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
              "INT_ADD",
              [
                "leaf",
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f7304",
      "incomplete_value": true,
      "site": "004f7318",
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
              "INT_ADD",
              [
                "leaf",
                "const:9:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f734c",
      "incomplete_value": true,
      "site": "004f7358",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f734c",
      "incomplete_value": true,
      "site": "004f7358",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:190:8"
              ]
            ]
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
      "004f7300",
      "READ",
      [
        "storage",
        "00295bd4",
        null,
        "string"
      ]
    ],
    [
      "004f7304",
      "READ",
      [
        "storage",
        "00295bdd",
        null,
        "string"
      ]
    ],
    [
      "004f734c",
      "READ",
      [
        "storage",
        "00c1b190",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f7300",
      "READ",
      [
        "storage",
        "00295b47",
        null,
        "string"
      ]
    ],
    [
      "004f7304",
      "READ",
      [
        "storage",
        "00295b50",
        null,
        "string"
      ]
    ],
    [
      "004f734c",
      "READ",
      [
        "storage",
        "00c1b1e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f72f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f72c0.md#insn-004f72f8) · [`004f72fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f72c0.md#insn-004f72fc)
- 新版 `004f72f8`（命令位置の公開資料なし） · `004f72fc`（命令位置の公開資料なし）

~~~diff
- 004f72f8 ["COPY", "tmp:0:8", ["const:bd4:8"]]
- 004f72f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004f72f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004f72f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004f72f8 ["COPY", "tmp:0:8", ["const:b47:8"]]
+ 004f72f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004f72f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004f72f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004f72f8 bytes 08512f91
+ 004f72f8 bytes 081d2d91
- 004f72fc ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 004f72fc bytes c9edffd0
+ 004f72fc ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 004f72fc bytes c9edffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b2dfb0c14cff99cde7952184b2b1fd0"></a>

### [`004f73a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f73a8.md) → [`004f73a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f73a8.md) _ZN5Botan14Cert_Extension16Name_Constraints12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 18件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004f7afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f7afc.md) [`004f7cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f7cc4.md) [`004f7dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f7dec.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md) · 呼出先 18件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004f7afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7afc.md) [`004f7cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7cc4.md) [`004f7dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7dec.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.51% / 新版 94.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f7500",
      "incomplete_value": true,
      "site": "004f7500",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
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
      "definition_site": "004f7500",
      "incomplete_value": true,
      "site": "004f7500",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
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
    "ordinal": 12,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f752c",
      "incomplete_value": true,
      "site": "004f752c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
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
      "definition_site": "004f752c",
      "incomplete_value": true,
      "site": "004f752c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
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
    "ordinal": 14,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f7570",
      "incomplete_value": true,
      "site": "004f7570",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
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
      "definition_site": "004f7570",
      "incomplete_value": true,
      "site": "004f7570",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
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
    "ordinal": 17,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f74f0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004f751c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004f7560",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f74f0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004f751c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004f7560",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f74f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f73a8.md#insn-004f74f0) · [`004f751c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f73a8.md#insn-004f751c) · [`004f7560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f73a8.md#insn-004f7560)
- 新版 `004f74f0`（命令位置の公開資料なし） · `004f751c`（命令位置の公開資料なし） · `004f7560`（命令位置の公開資料なし）

~~~diff
- 004f74f0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 004f74f0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f74f0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 004f74f0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f74f0 bytes a99643f9
+ 004f74f0 bytes a9be43f9
- 004f751c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 004f751c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f751c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 004f751c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f751c bytes a99643f9
+ 004f751c bytes a9be43f9
- 004f7560 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 004f7560 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f7560 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 004f7560 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f7560 bytes a99643f9
+ 004f7560 bytes a9be43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca1c03ddf6b4d24913779de76b9bbad8"></a>

### [`004f7f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f7f54.md) → [`004f7f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7f54.md) _ZNK5Botan14Cert_Extension16Name_Constraints11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md) [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`004e6520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6520.md) [`00525380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/00525380.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0042e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md) [`004dc2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md) [`004e6520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6520.md) [`00525380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f8138",
      "incomplete_value": true,
      "site": "004f8140",
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
      "definition_site": "004f8138",
      "incomplete_value": true,
      "site": "004f8140",
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004f8148",
      "incomplete_value": true,
      "site": "004f8148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:50:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
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
      "definition_site": "004f8148",
      "incomplete_value": true,
      "site": "004f8148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:50:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f8148",
      "incomplete_value": true,
      "site": "004f8148",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f8148",
      "incomplete_value": true,
      "site": "004f8148",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f7fe4",
      "READ",
      [
        "storage",
        "00298ed0",
        null,
        "string"
      ]
    ],
    [
      "004f7fe4",
      "READ",
      [
        "storage",
        "00298ee0",
        null,
        "string"
      ]
    ],
    [
      "004f80a4",
      "READ",
      [
        "storage",
        "002939e6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f7fe4",
      "READ",
      [
        "storage",
        "00298e43",
        null,
        "string"
      ]
    ],
    [
      "004f7fe4",
      "READ",
      [
        "storage",
        "00298e53",
        null,
        "string"
      ]
    ],
    [
      "004f80a4",
      "READ",
      [
        "storage",
        "00293959",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f7fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f7f54.md#insn-004f7fa4) · [`004f8070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f7f54.md#insn-004f8070) · [`004f8134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f7f54.md#insn-004f8134)
- 新版 `004f7fa4`（命令位置の公開資料なし） · `004f8070`（命令位置の公開資料なし） · `004f8134`（命令位置の公開資料なし）

~~~diff
- 004f7fa4 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 004f7fa4 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 004f7fa4 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 004f7fa4 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 004f7fa4 ["COPY", "tmp:0:8", ["const:e43:8"]]
+ 004f7fa4 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 004f7fa4 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 004f7fa4 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 004f7fa4 bytes 39433b91
+ 004f7fa4 bytes 390f3991
- 004f8070 ["COPY", "tmp:0:8", ["const:9e6:8"]]
- 004f8070 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 004f8070 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 004f8070 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 004f8070 ["COPY", "tmp:0:8", ["const:959:8"]]
+ 004f8070 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 004f8070 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 004f8070 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 004f8070 bytes 189b2791
+ 004f8070 bytes 18672591
- 004f8134 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dd0:8"]]
- 004f8134 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f8134 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 004f8134 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 004f8134 bytes 73ea46f9
+ 004f8134 bytes 731247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a622447e5461c7bdb5591df81895abd9"></a>

### [`004f8244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f8/004f8244.md) → [`004f8244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f8/004f8244.md) _ZN5Botan14Cert_Extension16Name_Constraints8validateERKNS_16X509_CertificateES4_RKNSt6__ndk16vectorINS5_10shared_ptrIS3_EENS5_9allocatorIS8_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0051d9e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d9e4.md) [`00529cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00529/00529cc4.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0051d9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d9e4.md) [`00529cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529cc4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.95% / 新版 97.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f842c",
      "incomplete_value": true,
      "site": "004f842c",
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
      "definition_site": "004f842c",
      "incomplete_value": true,
      "site": "004f842c",
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
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f842c",
      "incomplete_value": true,
      "site": "004f842c",
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
      "definition_site": "004f842c",
      "incomplete_value": true,
      "site": "004f842c",
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
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f84b4",
      "incomplete_value": true,
      "site": "004f84b4",
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
      "definition_site": "004f84b4",
      "incomplete_value": true,
      "site": "004f84b4",
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
    "ordinal": 39,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f82bc",
      "READ",
      [
        "storage",
        "00295a07",
        null,
        "string"
      ]
    ],
    [
      "004f82c0",
      "READ",
      [
        "storage",
        "00295a15",
        null,
        "string"
      ]
    ],
    [
      "004f83b8",
      "READ",
      [
        "storage",
        "00295a07",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f82bc",
      "READ",
      [
        "storage",
        "0029597a",
        null,
        "string"
      ]
    ],
    [
      "004f82c0",
      "READ",
      [
        "storage",
        "00295988",
        null,
        "string"
      ]
    ],
    [
      "004f83b8",
      "READ",
      [
        "storage",
        "0029597a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f82b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f8/004f8244.md#insn-004f82b4) · [`004f8414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f8/004f8244.md#insn-004f8414) · [`004f8418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f8/004f8244.md#insn-004f8418)
- 新版 `004f82b4`（命令位置の公開資料なし） · `004f8414`（命令位置の公開資料なし） · `004f8418`（命令位置の公開資料なし）

~~~diff
- 004f82b4 ["COPY", "tmp:0:8", ["const:a07:8"]]
- 004f82b4 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 004f82b4 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 004f82b4 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 004f82b4 ["COPY", "tmp:0:8", ["const:97a:8"]]
+ 004f82b4 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 004f82b4 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 004f82b4 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 004f82b4 bytes 941e2891
+ 004f82b4 bytes 94ea2591
- 004f8414 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:310:8"]]
- 004f8414 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f8414 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:360:8"]]
+ 004f8414 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f8414 bytes 298941f9
+ 004f8414 bytes 29b141f9
- 004f8418 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2e8:8"]]
- 004f8418 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f8418 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:338:8"]]
+ 004f8418 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 004f8418 bytes 947641f9
+ 004f8418 bytes 949e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b70b317f13f52a67c55c9253fde9fd9e"></a>

### [`004f8c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f8/004f8c10.md) → [`004f8c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f8/004f8c10.md) _ZNK5Botan14Cert_Extension20Certificate_Policies12encode_innerEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`00529d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00529/00529d48.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`00529d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529d48.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.17% / 新版 97.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f8c7c",
      "incomplete_value": true,
      "site": "004f8c84",
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
      "definition_site": "004f8c7c",
      "incomplete_value": true,
      "site": "004f8c84",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f8ca0",
      "incomplete_value": true,
      "site": "004f8ca0",
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
      "definition_site": "004f8ca0",
      "incomplete_value": true,
      "site": "004f8ca0",
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f8dd4",
      "incomplete_value": true,
      "site": "004f8dd4",
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
      "definition_site": "004f8dd4",
      "incomplete_value": true,
      "site": "004f8dd4",
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
      "004f8c60",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "004f8c84",
      "DATA",
      [
        "storage",
        "00be9278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004f8c90",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f8c60",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "004f8c84",
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004f8c90",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f8c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f8/004f8c10.md#insn-004f8c60) · [`004f8c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f8/004f8c10.md#insn-004f8c78) · [`004f8c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f8/004f8c10.md#insn-004f8c90)
- 新版 `004f8c60`（命令位置の公開資料なし） · `004f8c78`（命令位置の公開資料なし） · `004f8c90`（命令位置の公開資料なし）

~~~diff
- 004f8c60 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f00:8"]]
- 004f8c60 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f8c60 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f50:8"]]
+ 004f8c60 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f8c60 bytes 298147f9
+ 004f8c60 bytes 29a947f9
- 004f8c78 ["COPY", "tmp:0:8", ["const:478:8"]]
- 004f8c78 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 004f8c78 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 004f8c78 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 004f8c78 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 004f8c78 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 004f8c78 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 004f8c78 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 004f8c78 bytes 73e21191
+ 004f8c78 bytes 73221391
- 004f8c90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
- 004f8c90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f8c90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
+ 004f8c90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f8c90 bytes 088147f9
+ 004f8c90 bytes 08a947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5bfb6511e0cbf980571179ce261ecef"></a>

### [`004f9190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9190.md) → [`004f9190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9190.md) _ZN5Botan14Cert_Extension20Certificate_Policies12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`0051ab34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051a/0051ab34.md) [`00528a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00528/00528a6c.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`0051ab34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051ab34.md) [`00528a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528a6c.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.69% / 新版 97.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f9218",
      "incomplete_value": true,
      "site": "004f9218",
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
      "definition_site": "004f9218",
      "incomplete_value": true,
      "site": "004f9218",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f94ac",
      "incomplete_value": true,
      "site": "004f94ac",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
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
      "definition_site": "004f94ac",
      "incomplete_value": true,
      "site": "004f94ac",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
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
    "ordinal": 16,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f94f0",
      "incomplete_value": true,
      "site": "004f94f0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
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
      "definition_site": "004f94f0",
      "incomplete_value": true,
      "site": "004f94f0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
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
    "ordinal": 19,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f91f8",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "004f9218",
      "DATA",
      [
        "storage",
        "00be9278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004f9244",
      "DATA",
      [
        "storage",
        "00bed478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f91f8",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "004f9218",
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004f9244",
      "DATA",
      [
        "storage",
        "00bed4c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f91f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9190.md#insn-004f91f8) · [`004f9208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9190.md#insn-004f9208) · [`004f949c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9190.md#insn-004f949c)
- 新版 `004f91f8`（命令位置の公開資料なし） · `004f9208`（命令位置の公開資料なし） · `004f949c`（命令位置の公開資料なし）

~~~diff
- 004f91f8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:f00:8"]]
- 004f91f8 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f91f8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:f50:8"]]
+ 004f91f8 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 004f91f8 bytes 188347f9
+ 004f91f8 bytes 18ab47f9
- 004f9208 ["COPY", "tmp:0:8", ["const:478:8"]]
- 004f9208 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
- 004f9208 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
- 004f9208 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
+ 004f9208 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 004f9208 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
+ 004f9208 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
+ 004f9208 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
- 004f9208 bytes 9ce31191
+ 004f9208 bytes 9c231391
- 004f949c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 004f949c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f949c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
+ 004f949c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f949c bytes 699643f9
+ 004f949c bytes 69be43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca1e8c222b93e5fdc22b6f8839023754"></a>

### [`004f97e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f97e4.md) → [`004f97e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f97e4.md) _ZNK5Botan14Cert_Extension20Certificate_Policies11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb960.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004dc2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.54% / 新版 92.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f9824",
      "incomplete_value": true,
      "site": "004f9838",
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
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:422:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f9824",
      "incomplete_value": true,
      "site": "004f9838",
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
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:397:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "004f983c",
      "incomplete_value": true,
      "site": "004f9840",
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
              "INT_ADD",
              [
                "leaf",
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f983c",
      "incomplete_value": true,
      "site": "004f9840",
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
              "INT_ADD",
              [
                "leaf",
                "const:a:8"
              ]
            ]
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
      "004f9824",
      "READ",
      [
        "storage",
        "0029e397",
        null,
        "string"
      ]
    ],
    [
      "004f983c",
      "READ",
      [
        "storage",
        "0029e3a1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f9824",
      "READ",
      [
        "storage",
        "0029e422",
        null,
        "string"
      ]
    ],
    [
      "004f983c",
      "READ",
      [
        "storage",
        "0029e42c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f981c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f97e4.md#insn-004f981c)
- 新版 `004f981c`（命令位置の公開資料なし）

~~~diff
- 004f981c ["COPY", "tmp:0:8", ["const:397:8"]]
- 004f981c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f981c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f981c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f981c ["COPY", "tmp:0:8", ["const:422:8"]]
+ 004f981c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f981c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f981c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f981c bytes 295d0e91
+ 004f981c bytes 29891091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5706f064a457aec2a225162aa13885c0"></a>

### [`004f9bd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9bd8.md) → [`004f9bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9bd8.md) _ZNK5Botan14Cert_Extension28Authority_Information_Access12encode_innerEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f9c58",
      "incomplete_value": true,
      "site": "004f9c58",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:4ee:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f9c58",
      "incomplete_value": true,
      "site": "004f9c58",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:463:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "004f9d4c",
      "incomplete_value": true,
      "site": "004f9d4c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
      "definition_site": "004f9d4c",
      "incomplete_value": true,
      "site": "004f9d4c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
    "ordinal": 13,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f9c48",
      "READ",
      [
        "storage",
        "002a5463",
        null,
        "string"
      ]
    ],
    [
      "004f9d3c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f9c48",
      "READ",
      [
        "storage",
        "002a54ee",
        null,
        "string"
      ]
    ],
    [
      "004f9d3c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f9c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9bd8.md#insn-004f9c40) · [`004f9d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9bd8.md#insn-004f9d3c)
- 新版 `004f9c40`（命令位置の公開資料なし） · `004f9d3c`（命令位置の公開資料なし）

~~~diff
- 004f9c40 ["COPY", "tmp:0:8", ["const:463:8"]]
- 004f9c40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f9c40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f9c40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f9c40 ["COPY", "tmp:0:8", ["const:4ee:8"]]
+ 004f9c40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f9c40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f9c40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f9c40 bytes 298d1191
+ 004f9c40 bytes 29b91391
- 004f9d3c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004f9d3c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f9d3c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004f9d3c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f9d3c bytes 299543f9
+ 004f9d3c bytes 29bd43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dafcea45f73fe3896c561f021fc74a33"></a>

### [`004f9e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9e04.md) → [`004f9e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9e04.md) _ZN5Botan14Cert_Extension28Authority_Information_Access12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.33% / 新版 96.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f9e90",
      "incomplete_value": true,
      "site": "004f9e90",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f9e90",
      "incomplete_value": true,
      "site": "004f9e90",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004fa130",
      "incomplete_value": true,
      "site": "004fa130",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fa130",
      "incomplete_value": true,
      "site": "004fa130",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004fa3f4",
      "incomplete_value": true,
      "site": "004fa3f4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fa3f4",
      "incomplete_value": true,
      "site": "004fa3f4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f9e80",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004f9f40",
      "READ",
      [
        "storage",
        "002a5463",
        null,
        "string"
      ]
    ],
    [
      "004fa120",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f9e80",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004f9f40",
      "READ",
      [
        "storage",
        "002a54ee",
        null,
        "string"
      ]
    ],
    [
      "004fa120",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f9e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9e04.md#insn-004f9e80) · [`004f9ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9e04.md#insn-004f9ec4) · [`004f9ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9e04.md#insn-004f9ec8)
- 新版 `004f9e80`（命令位置の公開資料なし） · `004f9ec4`（命令位置の公開資料なし）

~~~diff
- 004f9e80 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
- 004f9e80 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f9e80 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:778:8"]]
+ 004f9e80 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f9e80 bytes 099743f9
+ 004f9e80 bytes 09bf43f9
- 004f9ec4 ["COPY", "tmp:0:8", ["const:463:8"]]
- 004f9ec4 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
- 004f9ec4 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
- 004f9ec4 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
+ 004f9ec4 ["COPY", "tmp:0:8", ["const:4ee:8"]]
+ 004f9ec4 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
+ 004f9ec4 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
+ 004f9ec4 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
- 004f9ec4 bytes 9c8f1191
+ 004f9ec4 bytes 9cbb1391
- 004f9ec8 ["COPY", "register:40d8:8", ["const:2a1000:8"]]
- 004f9ec8 bytes 5bedff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5afcd39301682c905d57da29540aa76"></a>

### [`004fa630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa630.md) → [`004fa630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fa/004fa630.md) _ZNK5Botan14Cert_Extension28Authority_Information_Access11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004dc2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.49% / 新版 86.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa690",
      "incomplete_value": true,
      "site": "004fa690",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:b3c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fa690",
      "incomplete_value": true,
      "site": "004fa690",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa694",
      "incomplete_value": true,
      "site": "004fa694",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004fa694",
      "incomplete_value": true,
      "site": "004fa694",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa6cc",
      "incomplete_value": true,
      "site": "004fa6d4",
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
                "const:2a1000:8"
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
      "definition_site": "004fa6cc",
      "incomplete_value": true,
      "site": "004fa6d4",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:3c5:8"
              ]
            ]
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
      "004fa680",
      "READ",
      [
        "storage",
        "002afbd0",
        null,
        "string"
      ]
    ],
    [
      "004fa684",
      "READ",
      [
        "storage",
        "002afbd6",
        null,
        "string"
      ]
    ],
    [
      "004fa6cc",
      "READ",
      [
        "storage",
        "002a13c5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fa680",
      "READ",
      [
        "storage",
        "002afb3c",
        null,
        "string"
      ]
    ],
    [
      "004fa684",
      "READ",
      [
        "storage",
        "002afb42",
        null,
        "string"
      ]
    ],
    [
      "004fa6cc",
      "READ",
      [
        "storage",
        "002a1450",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fa678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa630.md#insn-004fa678) · [`004fa6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa630.md#insn-004fa6c4) · [`004fa6c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa630.md#insn-004fa6c8)
- 新版 `004fa678`（命令位置の公開資料なし） · `004fa6c4`（命令位置の公開資料なし）

~~~diff
- 004fa678 ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 004fa678 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004fa678 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004fa678 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004fa678 ["COPY", "tmp:0:8", ["const:b3c:8"]]
+ 004fa678 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004fa678 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004fa678 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004fa678 bytes 29412f91
+ 004fa678 bytes 29f12c91
- 004fa6c4 ["COPY", "tmp:0:8", ["const:3c5:8"]]
- 004fa6c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004fa6c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004fa6c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004fa6c4 ["COPY", "tmp:0:8", ["const:450:8"]]
+ 004fa6c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004fa6c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004fa6c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004fa6c4 bytes 29150f91
+ 004fa6c4 bytes 29411191
- 004fa6c8 ["COPY", "register:4040:8", ["const:2b1000:8"]]
- 004fa6c8 bytes a8edfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84a6eb35e619fdaba186e376566f4909"></a>

### [`004fa788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa788.md) → [`004fa788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fa/004fa788.md) _ZNK5Botan14Cert_Extension10CRL_Number14get_crl_numberEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf10.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdcf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf60.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fa7ec",
      "incomplete_value": false,
      "site": "004fa7f4",
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
            "const:639:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fa7ec",
      "incomplete_value": false,
      "site": "004fa7f4",
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
            "const:5ae:8"
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
      "definition_site": "004fa828",
      "incomplete_value": true,
      "site": "004fa834",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fa828",
      "incomplete_value": true,
      "site": "004fa834",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
              ]
            ]
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
      "004fa7ec",
      "PARAM",
      [
        "storage",
        "0029f5ae",
        null,
        "string"
      ]
    ],
    [
      "004fa828",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "004fa828",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004fa7ec",
      "PARAM",
      [
        "storage",
        "0029f639",
        null,
        "string"
      ]
    ],
    [
      "004fa828",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "004fa828",
      "PARAM",
      [
        "storage",
        "00be93d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fa7ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa788.md#insn-004fa7ec) · [`004fa828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa788.md#insn-004fa828)
- 新版 `004fa7ec`（命令位置の公開資料なし） · `004fa828`（命令位置の公開資料なし）

~~~diff
- 004fa7ec ["COPY", "tmp:0:8", ["const:5ae:8"]]
- 004fa7ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004fa7ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004fa7ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004fa7ec ["COPY", "tmp:0:8", ["const:639:8"]]
+ 004fa7ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004fa7ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004fa7ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004fa7ec bytes 21b81691
+ 004fa7ec bytes 21e41891
- 004fa828 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 004fa828 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fa828 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 004fa828 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004fa828 bytes 218447f9
+ 004fa828 bytes 21ac47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

