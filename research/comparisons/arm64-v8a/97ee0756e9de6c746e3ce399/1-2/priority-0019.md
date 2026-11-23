# v15.7.3 → v15.7.4 · 最優先の変更候補 (19)

[一覧の目次](README.md)

<a id="compare-6b4c5c286e6ae330a341981d5f8161ab"></a>

### [`0056fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056f/0056fddc.md) → [`0056fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fddc.md) FUN_0056fddc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "0056fdf4",
      "incomplete_value": false,
      "site": "0056fdf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056fdf4",
      "incomplete_value": false,
      "site": "0056fdf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:418:8"
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
      "0056fdf8",
      "DATA",
      [
        "storage",
        "00bf0418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056fdf8",
      "DATA",
      [
        "storage",
        "00bf0468",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056fdf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056f/0056fddc.md#insn-0056fdf4)
- 新版 `0056fdf4`（命令位置の公開資料なし）

~~~diff
- 0056fdf4 ["COPY", "tmp:0:8", ["const:418:8"]]
- 0056fdf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056fdf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056fdf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056fdf4 ["COPY", "tmp:0:8", ["const:468:8"]]
+ 0056fdf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056fdf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056fdf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056fdf4 bytes 08611091
+ 0056fdf4 bytes 08a11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c9224c72967c1713299f51dde4574a5"></a>

### [`0056fea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056f/0056fea8.md) → [`0056fea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fea8.md) FUN_0056fea8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0056fec0",
      "incomplete_value": false,
      "site": "0056fec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056fec0",
      "incomplete_value": false,
      "site": "0056fec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:418:8"
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
      "0056fec4",
      "DATA",
      [
        "storage",
        "00bf0418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056fec4",
      "DATA",
      [
        "storage",
        "00bf0468",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056fec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056f/0056fea8.md#insn-0056fec0)
- 新版 `0056fec0`（命令位置の公開資料なし）

~~~diff
- 0056fec0 ["COPY", "tmp:0:8", ["const:418:8"]]
- 0056fec0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056fec0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056fec0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056fec0 ["COPY", "tmp:0:8", ["const:468:8"]]
+ 0056fec0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056fec0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056fec0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056fec0 bytes 08611091
+ 0056fec0 bytes 08a11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78a11ac4bf2266070f94de5d04d75c2b"></a>

### [`005700e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00570/005700e0.md) → [`005700e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/005700e0.md) FUN_005700e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb080.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00570118",
      "incomplete_value": false,
      "site": "0057012c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:160:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570118",
      "incomplete_value": false,
      "site": "0057012c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:110:8"
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
      "definition_site": "00570120",
      "incomplete_value": false,
      "site": "0057012c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570120",
      "incomplete_value": false,
      "site": "0057012c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:120:8"
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
      "00570118",
      "PARAM",
      [
        "storage",
        "00bf0110",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00570120",
      "PARAM",
      [
        "storage",
        "00bf0120",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00570118",
      "PARAM",
      [
        "storage",
        "00bf0160",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00570120",
      "PARAM",
      [
        "storage",
        "00bf0170",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00570118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00570/005700e0.md#insn-00570118) · [`00570120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00570/005700e0.md#insn-00570120)
- 新版 `00570118`（命令位置の公開資料なし） · `00570120`（命令位置の公開資料なし）

~~~diff
- 00570118 ["COPY", "tmp:0:8", ["const:110:8"]]
- 00570118 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00570118 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00570118 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00570118 ["COPY", "tmp:0:8", ["const:160:8"]]
+ 00570118 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00570118 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00570118 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00570118 bytes 21400491
+ 00570118 bytes 21800591
- 00570120 ["COPY", "tmp:0:8", ["const:120:8"]]
- 00570120 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00570120 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00570120 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00570120 ["COPY", "tmp:0:8", ["const:170:8"]]
+ 00570120 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00570120 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00570120 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00570120 bytes 42800491
+ 00570120 bytes 42c00591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7e6e8de6c6761fb00af31b4f4bc82f7"></a>

### [`0057029c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00570/0057029c.md) → [`0057029c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/0057029c.md) FUN_0057029c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb080.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "005702dc",
      "incomplete_value": true,
      "site": "005702e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
          ],
          [
            "leaf",
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005702dc",
      "incomplete_value": true,
      "site": "005702e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
          ],
          [
            "leaf",
            "const:120:8"
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
      "005702d4",
      "PARAM",
      [
        "storage",
        "00bf0110",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005702dc",
      "PARAM",
      [
        "storage",
        "00bf0120",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005702d4",
      "PARAM",
      [
        "storage",
        "00bf0160",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005702dc",
      "PARAM",
      [
        "storage",
        "00bf0170",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005702d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00570/0057029c.md#insn-005702d4) · [`005702dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00570/0057029c.md#insn-005702dc)
- 新版 `005702d4`（命令位置の公開資料なし） · `005702dc`（命令位置の公開資料なし）

~~~diff
- 005702d4 ["COPY", "tmp:0:8", ["const:110:8"]]
- 005702d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005702d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005702d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005702d4 ["COPY", "tmp:0:8", ["const:160:8"]]
+ 005702d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005702d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005702d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005702d4 bytes 21400491
+ 005702d4 bytes 21800591
- 005702dc ["COPY", "tmp:0:8", ["const:120:8"]]
- 005702dc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 005702dc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 005702dc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 005702dc ["COPY", "tmp:0:8", ["const:170:8"]]
+ 005702dc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 005702dc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 005702dc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 005702dc bytes 42800491
+ 005702dc bytes 42c00591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e84eccd159a795c9e472bbdb1a5e7e9"></a>

### [`00570458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00570/00570458.md) → [`00570458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/00570458.md) FUN_00570458

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057045c",
      "incomplete_value": false,
      "site": "00570460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057045c",
      "incomplete_value": false,
      "site": "00570460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:450:8"
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
      "00570460",
      "DATA",
      [
        "storage",
        "00bf0450",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00570460",
      "DATA",
      [
        "storage",
        "00bf04a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057045c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00570/00570458.md#insn-0057045c)
- 新版 `0057045c`（命令位置の公開資料なし）

~~~diff
- 0057045c ["COPY", "tmp:0:8", ["const:450:8"]]
- 0057045c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057045c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057045c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057045c ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 0057045c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057045c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057045c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057045c bytes 08411191
+ 0057045c bytes 08811291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8338da41da8592bdaa9b46eb26299cd"></a>

### [`00570468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00570/00570468.md) → [`00570468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/00570468.md) FUN_00570468

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00570478",
      "incomplete_value": false,
      "site": "00570480",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570478",
      "incomplete_value": false,
      "site": "00570480",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:450:8"
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
      "00570480",
      "DATA",
      [
        "storage",
        "00bf0450",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00570480",
      "DATA",
      [
        "storage",
        "00bf04a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00570478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00570/00570468.md#insn-00570478)
- 新版 `00570478`（命令位置の公開資料なし）

~~~diff
- 00570478 ["COPY", "tmp:0:8", ["const:450:8"]]
- 00570478 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00570478 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00570478 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00570478 ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 00570478 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00570478 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00570478 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00570478 bytes 08411191
+ 00570478 bytes 08811291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-361883d4306653e58156bfe08d12c023"></a>

### [`005704a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00570/005704a8.md) → [`005704a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/005704a8.md) FUN_005704a8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00570dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00570/00570dcc.md) · 呼出先 14件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00424230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424230.md) [`005323b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005323b0.md) [`005708ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00570/005708ec.md)
- 新版 呼出元 1件 [`00570dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/00570dcc.md) · 呼出先 14件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00424230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424230.md) [`005323b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323b0.md) [`005708ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/005708ec.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.09% / 新版 99.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005704e8",
      "incomplete_value": false,
      "site": "005704ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005704e8",
      "incomplete_value": false,
      "site": "005704ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
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
      "005704ec",
      "DATA",
      [
        "storage",
        "00bf04a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005704ec",
      "DATA",
      [
        "storage",
        "00bf04f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005704e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00570/005704a8.md#insn-005704e8)
- 新版 `005704e8`（命令位置の公開資料なし）

~~~diff
- 005704e8 ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 005704e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005704e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005704e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005704e8 ["COPY", "tmp:0:8", ["const:4f0:8"]]
+ 005704e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005704e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005704e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005704e8 bytes 08811291
+ 005704e8 bytes 08c11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5410fa8ecc84db7143c323153c48ddf2"></a>

### [`00570dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00570/00570dcc.md) → [`00570dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/00570dcc.md) FUN_00570dcc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0056e384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e384.md) · 呼出先 21件 [`005704a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00570/005704a8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`0056e384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e384.md) · 呼出先 21件 [`005704a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/005704a8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.20% / 新版 97.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005712b8",
      "incomplete_value": false,
      "site": "005712c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005712b8",
      "incomplete_value": false,
      "site": "005712c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "ordinal": 63,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00570eb8",
      "incomplete_value": false,
      "site": "00570ec4",
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
            "const:7ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570eb8",
      "incomplete_value": false,
      "site": "00570ec4",
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
            "const:72f:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00570ee4",
      "incomplete_value": false,
      "site": "00570eec",
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
            "const:333:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570ee4",
      "incomplete_value": false,
      "site": "00570eec",
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
            "const:2a8:8"
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
      "00570eb8",
      "PARAM",
      [
        "storage",
        "002a572f",
        null,
        "string"
      ]
    ],
    [
      "00570ee4",
      "PARAM",
      [
        "storage",
        "002a42a8",
        null,
        null
      ]
    ],
    [
      "00571028",
      "PARAM",
      [
        "storage",
        "002a42a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00570eb8",
      "PARAM",
      [
        "storage",
        "002a57ba",
        null,
        "string"
      ]
    ],
    [
      "00570ee4",
      "PARAM",
      [
        "storage",
        "002a4333",
        null,
        null
      ]
    ],
    [
      "00571028",
      "PARAM",
      [
        "storage",
        "002a4333",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00570eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00570/00570dcc.md#insn-00570eb8) · [`00570ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00570/00570dcc.md#insn-00570ee4) · [`00571028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00570/00570dcc.md#insn-00571028)
- 新版 `00570eb8`（命令位置の公開資料なし） · `00570ee4`（命令位置の公開資料なし） · `00571028`（命令位置の公開資料なし）

~~~diff
- 00570eb8 ["COPY", "tmp:0:8", ["const:72f:8"]]
- 00570eb8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00570eb8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00570eb8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00570eb8 ["COPY", "tmp:0:8", ["const:7ba:8"]]
+ 00570eb8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00570eb8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00570eb8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00570eb8 bytes 42bc1c91
+ 00570eb8 bytes 42e81e91
- 00570ee4 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 00570ee4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00570ee4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00570ee4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00570ee4 ["COPY", "tmp:0:8", ["const:333:8"]]
+ 00570ee4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00570ee4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00570ee4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00570ee4 bytes 21a00a91
+ 00570ee4 bytes 21cc0c91
- 00571028 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 00571028 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00571028 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00571028 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00571028 ["COPY", "tmp:0:8", ["const:333:8"]]
+ 00571028 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00571028 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00571028 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00571028 bytes 21a00a91
+ 00571028 bytes 21cc0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b04291e1120acc83b78c8a31daff3bb7"></a>

### [`005719c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00571/005719c8.md) → [`005719c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/005719c8.md) FUN_005719c8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005719cc",
      "incomplete_value": false,
      "site": "005719d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005719cc",
      "incomplete_value": false,
      "site": "005719d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
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
      "005719d0",
      "DATA",
      [
        "storage",
        "00bf04f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005719d0",
      "DATA",
      [
        "storage",
        "00bf0548",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005719cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00571/005719c8.md#insn-005719cc)
- 新版 `005719cc`（命令位置の公開資料なし）

~~~diff
- 005719cc ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 005719cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005719cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005719cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005719cc ["COPY", "tmp:0:8", ["const:548:8"]]
+ 005719cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005719cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005719cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005719cc bytes 08e11391
+ 005719cc bytes 08211591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27bf80d4fdaf8de81bfa4c79293fc836"></a>

### [`005719d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00571/005719d8.md) → [`005719d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/005719d8.md) FUN_005719d8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005719e8",
      "incomplete_value": false,
      "site": "005719f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005719e8",
      "incomplete_value": false,
      "site": "005719f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
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
      "005719f0",
      "DATA",
      [
        "storage",
        "00bf04f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005719f0",
      "DATA",
      [
        "storage",
        "00bf0548",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005719e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00571/005719d8.md#insn-005719e8)
- 新版 `005719e8`（命令位置の公開資料なし）

~~~diff
- 005719e8 ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 005719e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005719e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005719e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005719e8 ["COPY", "tmp:0:8", ["const:548:8"]]
+ 005719e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005719e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005719e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005719e8 bytes 08e11391
+ 005719e8 bytes 08211591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd00235871a590e8a6c3adec7b91d72b"></a>

### [`00571a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00571/00571a08.md) → [`00571a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571a08.md) FUN_00571a08

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`005323b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005323b0.md) [`00571468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00571/00571468.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdd7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd7a0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`005323b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323b0.md) [`00571468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571468.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd7f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00571a1c",
      "incomplete_value": false,
      "site": "00571a20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571a1c",
      "incomplete_value": false,
      "site": "00571a20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00571a20",
      "DATA",
      [
        "storage",
        "00bf04a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00571a20",
      "DATA",
      [
        "storage",
        "00bf04f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00571/00571a08.md#insn-00571a1c)
- 新版 `00571a1c`（命令位置の公開資料なし）

~~~diff
- 00571a1c ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 00571a1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00571a1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00571a1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00571a1c ["COPY", "tmp:0:8", ["const:4f0:8"]]
+ 00571a1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00571a1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00571a1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00571a1c bytes 08811291
+ 00571a1c bytes 08c11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ca79d9b496e8a2e0d6f5bdf61ca7504"></a>

### [`00571a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00571/00571a60.md) → [`00571a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571a60.md) FUN_00571a60

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005655f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/005655f0.md) · 呼出先 7件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00571c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00571/00571c94.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`005655f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/005655f0.md) · 呼出先 7件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00571c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571c94.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.35% / 新版 98.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00571a94",
      "incomplete_value": false,
      "site": "00571aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571a94",
      "incomplete_value": false,
      "site": "00571aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:548:8"
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
      "00571aa4",
      "DATA",
      [
        "storage",
        "00bf0548",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00571aa4",
      "DATA",
      [
        "storage",
        "00bf0598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00571/00571a60.md#insn-00571a94)
- 新版 `00571a94`（命令位置の公開資料なし）

~~~diff
- 00571a94 ["COPY", "tmp:0:8", ["const:548:8"]]
- 00571a94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00571a94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00571a94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00571a94 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 00571a94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00571a94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00571a94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00571a94 bytes 29211591
+ 00571a94 bytes 29611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1fafd1aeaa13e7accfffda0aafc37a3"></a>

### [`00571c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00571/00571c94.md) → [`00571c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571c94.md) FUN_00571c94

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00571a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00571/00571a60.md) · 呼出先 12件 [`0053c5ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5ec.md) [`0053c654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c654.md) [`0053c668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c668.md) [`0053c688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c688.md) [`005722b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/005722b8.md)
- 新版 呼出元 1件 [`00571a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571a60.md) · 呼出先 12件 [`0053c5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5ec.md) [`0053c654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c654.md) [`0053c668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c668.md) [`0053c688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c688.md) [`005722b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005722b8.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.63% / 新版 97.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00571e1c",
      "incomplete_value": true,
      "site": "00571e2c",
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
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:70c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571e1c",
      "incomplete_value": true,
      "site": "00571e2c",
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
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:681:8"
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
      "00571e1c",
      "READ",
      [
        "storage",
        "0029f681",
        null,
        "string"
      ]
    ],
    [
      "00571e20",
      "READ",
      [
        "storage",
        "0029f68c",
        null,
        "string"
      ]
    ],
    [
      "00571f9c",
      "PARAM",
      [
        "storage",
        "002a46aa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00571e1c",
      "READ",
      [
        "storage",
        "0029f70c",
        null,
        "string"
      ]
    ],
    [
      "00571e20",
      "READ",
      [
        "storage",
        "0029f717",
        null,
        "string"
      ]
    ],
    [
      "00571f9c",
      "PARAM",
      [
        "storage",
        "002a4735",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00571/00571c94.md#insn-00571e14) · [`00571e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00571/00571c94.md#insn-00571e18)
- 新版 `00571e14`（命令位置の公開資料なし） · `00571e18`（命令位置の公開資料なし）

~~~diff
- 00571e14 ["COPY", "tmp:0:8", ["const:681:8"]]
- 00571e14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00571e14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00571e14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00571e14 ["COPY", "tmp:0:8", ["const:70c:8"]]
+ 00571e14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00571e14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00571e14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00571e14 bytes 08051a91
+ 00571e14 bytes 08311c91
- 00571e18 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00571e18 bytes 09eaff90
+ 00571e18 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 00571e18 bytes 09eaff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37399d1620bc2f922f3bcd2eb22409c3"></a>

### [`005720e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/005720e0.md) → [`005720e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005720e0.md) FUN_005720e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005656c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/005656c4.md) · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`005656c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/005656c4.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005720f8",
      "incomplete_value": false,
      "site": "005720fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005720f8",
      "incomplete_value": false,
      "site": "005720fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:548:8"
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
      "005720fc",
      "DATA",
      [
        "storage",
        "00bf0548",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005720fc",
      "DATA",
      [
        "storage",
        "00bf0598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005720f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/005720e0.md#insn-005720f8)
- 新版 `005720f8`（命令位置の公開資料なし）

~~~diff
- 005720f8 ["COPY", "tmp:0:8", ["const:548:8"]]
- 005720f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005720f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005720f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005720f8 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 005720f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005720f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005720f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005720f8 bytes 08211591
+ 005720f8 bytes 08611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19df642adb4f7538a3d1f1c8ac42476c"></a>

### [`00572494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572494.md) → [`00572494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572494.md) FUN_00572494

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.49% / 新版 95.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0057256c",
      "incomplete_value": false,
      "site": "00572570",
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
            "const:949:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057256c",
      "incomplete_value": false,
      "site": "00572570",
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
            "const:9d6:8"
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
      "definition_site": "0057259c",
      "incomplete_value": false,
      "site": "005725a0",
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
      "definition_site": "0057259c",
      "incomplete_value": false,
      "site": "005725a0",
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
      "0057250c",
      "PARAM",
      [
        "storage",
        "0029e2aa",
        null,
        null
      ]
    ],
    [
      "0057256c",
      "PARAM",
      [
        "storage",
        "002979d6",
        null,
        null
      ]
    ],
    [
      "0057259c",
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
      "0057250c",
      "PARAM",
      [
        "storage",
        "0029e335",
        null,
        null
      ]
    ],
    [
      "0057256c",
      "PARAM",
      [
        "storage",
        "00297949",
        null,
        null
      ]
    ],
    [
      "0057259c",
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

- 旧版 [`005724f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572494.md#insn-005724f8) · [`0057256c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572494.md#insn-0057256c) · [`0057259c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572494.md#insn-0057259c)
- 新版 `005724f8`（命令位置の公開資料なし） · `0057256c`（命令位置の公開資料なし） · `0057259c`（命令位置の公開資料なし）

~~~diff
- 005724f8 ["COPY", "tmp:0:8", ["const:2aa:8"]]
- 005724f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005724f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005724f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005724f8 ["COPY", "tmp:0:8", ["const:335:8"]]
+ 005724f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005724f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005724f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005724f8 bytes 29a90a91
+ 005724f8 bytes 29d50c91
- 0057256c ["COPY", "tmp:0:8", ["const:9d6:8"]]
- 0057256c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0057256c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0057256c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0057256c ["COPY", "tmp:0:8", ["const:949:8"]]
+ 0057256c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0057256c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0057256c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0057256c bytes 00582791
+ 0057256c bytes 00242591
- 0057259c ["COPY", "tmp:0:8", ["const:866:8"]]
- 0057259c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0057259c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0057259c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0057259c ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 0057259c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0057259c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0057259c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0057259c bytes 00982191
+ 0057259c bytes 00641f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44944d23fddb76213c28199b17667668"></a>

### [`005726a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/005726a8.md) → [`005726a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005726a8.md) FUN_005726a8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00573e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/00573e38.md) · 呼出先 2件 [`005727b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/005727b4.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 1件 [`00573e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573e38.md) · 呼出先 2件 [`005727b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005727b4.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005726bc",
      "incomplete_value": false,
      "site": "005726c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005726bc",
      "incomplete_value": false,
      "site": "005726c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "005726c4",
      "DATA",
      [
        "storage",
        "00bf05d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005726c4",
      "DATA",
      [
        "storage",
        "00bf0628",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005726bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/005726a8.md#insn-005726bc)
- 新版 `005726bc`（命令位置の公開資料なし）

~~~diff
- 005726bc ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 005726bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005726bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005726bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005726bc ["COPY", "tmp:0:8", ["const:628:8"]]
+ 005726bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005726bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005726bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005726bc bytes 08611791
+ 005726bc bytes 08a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bfa4342aed47e8b183414e125ceccf1"></a>

### [`005727b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/005727b4.md) → [`005727b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005727b4.md) FUN_005727b4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005726a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/005726a8.md) · 呼出先 4件 [`00572998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572998.md) [`00572b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572e44.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`005726a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005726a8.md) · 呼出先 4件 [`00572998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572998.md) [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00572808",
      "incomplete_value": false,
      "site": "0057280c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572808",
      "incomplete_value": false,
      "site": "0057280c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057285c",
      "incomplete_value": false,
      "site": "00572860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057285c",
      "incomplete_value": false,
      "site": "00572860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
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
      "0057280c",
      "DATA",
      [
        "storage",
        "00bf0668",
        null,
        "pointer"
      ]
    ],
    [
      "00572860",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057280c",
      "DATA",
      [
        "storage",
        "00bf06b8",
        null,
        "pointer"
      ]
    ],
    [
      "00572860",
      "DATA",
      [
        "storage",
        "00be6b20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00572808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/005727b4.md#insn-00572808) · [`0057285c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/005727b4.md#insn-0057285c)
- 新版 `00572808`（命令位置の公開資料なし） · `0057285c`（命令位置の公開資料なし）

~~~diff
- 00572808 ["COPY", "tmp:0:8", ["const:668:8"]]
- 00572808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00572808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00572808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00572808 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 00572808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00572808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00572808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00572808 bytes 08a11991
+ 00572808 bytes 08e11a91
- 0057285c ["COPY", "tmp:0:8", ["const:ad0:8"]]
- 0057285c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057285c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057285c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057285c ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 0057285c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057285c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057285c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057285c bytes 08412b91
+ 0057285c bytes 08812c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-914a3f5cce946aa79c239ae158019f66"></a>

### [`005728ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/005728ac.md) → [`005728ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005728ac.md) FUN_005728ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005728c4",
      "incomplete_value": false,
      "site": "005728cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005728c4",
      "incomplete_value": false,
      "site": "005728cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "005728cc",
      "DATA",
      [
        "storage",
        "00bf05d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005728cc",
      "DATA",
      [
        "storage",
        "00bf0628",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005728c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/005728ac.md#insn-005728c4)
- 新版 `005728c4`（命令位置の公開資料なし）

~~~diff
- 005728c4 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 005728c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005728c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005728c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005728c4 ["COPY", "tmp:0:8", ["const:628:8"]]
+ 005728c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005728c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005728c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005728c4 bytes 08611791
+ 005728c4 bytes 08a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-720e199140efbd8c004632a2221f5c95"></a>

### [`00572924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572924.md) → [`00572924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572924.md) FUN_00572924

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057293c",
      "incomplete_value": false,
      "site": "00572944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057293c",
      "incomplete_value": false,
      "site": "00572944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "00572944",
      "DATA",
      [
        "storage",
        "00bf05d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00572944",
      "DATA",
      [
        "storage",
        "00bf0628",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057293c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572924.md#insn-0057293c)
- 新版 `0057293c`（命令位置の公開資料なし）

~~~diff
- 0057293c ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 0057293c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057293c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057293c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057293c ["COPY", "tmp:0:8", ["const:628:8"]]
+ 0057293c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057293c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057293c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057293c bytes 08611791
+ 0057293c bytes 08a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29fd468281dd31a6a9e712d0c505f5f3"></a>

### [`00572b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572b04.md) → [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md) FUN_00572b04

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005727b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/005727b4.md) [`00572b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572e44.md) · 呼出先 13件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`00438f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438f20.md) [`00572998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572998.md) [`00572b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572b04.md)
- 新版 呼出元 3件 [`005727b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005727b4.md) [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md) · 呼出先 13件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00438f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438f20.md) [`00572998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572998.md) [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.39% / 新版 96.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00572b9c",
      "incomplete_value": false,
      "site": "00572ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572b9c",
      "incomplete_value": false,
      "site": "00572ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "definition_site": "00572c30",
      "incomplete_value": false,
      "site": "00572c34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572c30",
      "incomplete_value": false,
      "site": "00572c34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00572dc0",
      "incomplete_value": true,
      "site": "00572dc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572dc0",
      "incomplete_value": true,
      "site": "00572dc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00572ba0",
      "DATA",
      [
        "storage",
        "00bf0668",
        null,
        "pointer"
      ]
    ],
    [
      "00572c34",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ],
    [
      "00572d84",
      "READ",
      [
        "storage",
        "00be6ad8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00572ba0",
      "DATA",
      [
        "storage",
        "00bf06b8",
        null,
        "pointer"
      ]
    ],
    [
      "00572c34",
      "DATA",
      [
        "storage",
        "00be6b20",
        null,
        "pointer"
      ]
    ],
    [
      "00572d84",
      "READ",
      [
        "storage",
        "00be6b28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00572b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572b04.md#insn-00572b9c) · [`00572c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572b04.md#insn-00572c30) · [`00572d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572b04.md#insn-00572d74)
- 新版 `00572b9c`（命令位置の公開資料なし） · `00572c30`（命令位置の公開資料なし） · `00572d74`（命令位置の公開資料なし）

~~~diff
- 00572b9c ["COPY", "tmp:0:8", ["const:668:8"]]
- 00572b9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00572b9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00572b9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00572b9c ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 00572b9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00572b9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00572b9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00572b9c bytes 08a11991
+ 00572b9c bytes 08e11a91
- 00572c30 ["COPY", "tmp:0:8", ["const:ad0:8"]]
- 00572c30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00572c30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00572c30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00572c30 ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 00572c30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00572c30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00572c30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00572c30 bytes 08412b91
+ 00572c30 bytes 08812c91
- 00572d74 ["COPY", "tmp:0:8", ["const:90d:8"]]
- 00572d74 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00572d74 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00572d74 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00572d74 ["COPY", "tmp:0:8", ["const:9a7:8"]]
+ 00572d74 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00572d74 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00572d74 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00572d74 bytes 73362491
+ 00572d74 bytes 739e2691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edeb2e476eb63f2ad15de0da11ac16e3"></a>

### [`00572e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572e44.md) → [`00572e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md) FUN_00572e44

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`005727b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/005727b4.md) [`00572b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572e44.md) · 呼出先 15件 [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`00436bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436bf8.md) [`00438f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438f20.md) [`00572998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572998.md) [`00572b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572b04.md)
- 新版 呼出元 3件 [`005727b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005727b4.md) [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md) · 呼出先 15件 [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00436bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436bf8.md) [`00438f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438f20.md) [`00572998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572998.md) [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.39% / 新版 94.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0057310c",
      "incomplete_value": true,
      "site": "00573110",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057310c",
      "incomplete_value": true,
      "site": "00573110",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00573164",
      "incomplete_value": false,
      "site": "00573168",
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
            "const:be1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00573164",
      "incomplete_value": false,
      "site": "00573168",
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
            "const:c6e:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00573178",
      "incomplete_value": true,
      "site": "0057317c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00573178",
      "incomplete_value": true,
      "site": "0057317c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00572f24",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ],
    [
      "00572fa8",
      "DATA",
      [
        "storage",
        "00bf0668",
        null,
        "pointer"
      ]
    ],
    [
      "0057306c",
      "READ",
      [
        "storage",
        "00be6ad8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00572f24",
      "DATA",
      [
        "storage",
        "00be6b20",
        null,
        "pointer"
      ]
    ],
    [
      "00572fa8",
      "DATA",
      [
        "storage",
        "00bf06b8",
        null,
        "pointer"
      ]
    ],
    [
      "0057306c",
      "READ",
      [
        "storage",
        "00be6b28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00572e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572e44.md#insn-00572e8c) · [`00572e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572e44.md#insn-00572e94)
- 新版 `00572e8c`（命令位置の公開資料なし） · `00572e94`（命令位置の公開資料なし）

~~~diff
- 00572e8c ["COPY", "tmp:0:8", ["const:aa8:8"]]
- 00572e8c ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 00572e8c ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 00572e8c ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 00572e8c ["COPY", "tmp:0:8", ["const:a1b:8"]]
+ 00572e8c ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 00572e8c ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 00572e8c ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 00572e8c bytes 18a32a91
+ 00572e8c bytes 186f2891
- 00572e94 ["COPY", "register:40d8:8", ["const:be6000:8"]]
- 00572e94 bytes bb330090
+ 00572e94 ["COPY", "register:40d8:8", ["const:be6000:8"]]
+ 00572e94 bytes bb330090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a61dc23d0d7ec1d72e1d68a6c1953ada"></a>

### [`0057321c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/0057321c.md) → [`0057321c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/0057321c.md) FUN_0057321c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00572b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572e44.md) · 呼出先 3件 [`005735cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/005735cc.md) [`00573960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/00573960.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 2件 [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md) · 呼出先 3件 [`005735cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/005735cc.md) [`00573960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573960.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00573280",
      "incomplete_value": false,
      "site": "00573288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00573280",
      "incomplete_value": false,
      "site": "00573288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005732a8",
      "incomplete_value": false,
      "site": "005732b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005732a8",
      "incomplete_value": false,
      "site": "005732b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
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
      "00573288",
      "DATA",
      [
        "storage",
        "00bf05f8",
        null,
        "pointer"
      ]
    ],
    [
      "005732b0",
      "DATA",
      [
        "storage",
        "00bf05f8",
        null,
        "pointer"
      ]
    ],
    [
      "005732dc",
      "DATA",
      [
        "storage",
        "00bf05f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00573288",
      "DATA",
      [
        "storage",
        "00bf0648",
        null,
        "pointer"
      ]
    ],
    [
      "005732b0",
      "DATA",
      [
        "storage",
        "00bf0648",
        null,
        "pointer"
      ]
    ],
    [
      "005732dc",
      "DATA",
      [
        "storage",
        "00bf0648",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00573280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/0057321c.md#insn-00573280) · [`005732a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/0057321c.md#insn-005732a8) · [`005732d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/0057321c.md#insn-005732d4)
- 新版 `00573280`（命令位置の公開資料なし） · `005732a8`（命令位置の公開資料なし） · `005732d4`（命令位置の公開資料なし）

~~~diff
- 00573280 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 00573280 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00573280 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00573280 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00573280 ["COPY", "tmp:0:8", ["const:648:8"]]
+ 00573280 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00573280 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00573280 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00573280 bytes 08e11791
+ 00573280 bytes 08211991
- 005732a8 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 005732a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005732a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005732a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005732a8 ["COPY", "tmp:0:8", ["const:648:8"]]
+ 005732a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005732a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005732a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005732a8 bytes 29e11791
+ 005732a8 bytes 29211991
- 005732d4 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 005732d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005732d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005732d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005732d4 ["COPY", "tmp:0:8", ["const:648:8"]]
+ 005732d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005732d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005732d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005732d4 bytes 29e11791
+ 005732d4 bytes 29211991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-242fe469970e06f50050b1d707b3af0d"></a>

### [`005735cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/005735cc.md) → [`005735cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/005735cc.md) FUN_005735cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0057321c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/0057321c.md) · 呼出先 12件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0057321c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/0057321c.md) · 呼出先 12件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.73% / 新版 95.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057371c",
      "incomplete_value": false,
      "site": "00573720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057371c",
      "incomplete_value": false,
      "site": "00573720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005737bc",
      "incomplete_value": false,
      "site": "005737c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005737bc",
      "incomplete_value": false,
      "site": "005737c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005738bc",
      "incomplete_value": false,
      "site": "005738c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005738bc",
      "incomplete_value": false,
      "site": "005738c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005736b0",
      "PARAM",
      [
        "storage",
        "002a81e3",
        null,
        null
      ]
    ],
    [
      "005736dc",
      "PARAM",
      [
        "storage",
        "002a81e3",
        null,
        null
      ]
    ],
    [
      "00573720",
      "DATA",
      [
        "storage",
        "00bf05f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005736b0",
      "PARAM",
      [
        "storage",
        "002a827d",
        null,
        null
      ]
    ],
    [
      "005736dc",
      "PARAM",
      [
        "storage",
        "002a827d",
        null,
        null
      ]
    ],
    [
      "00573720",
      "DATA",
      [
        "storage",
        "00bf0648",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005736b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/005735cc.md#insn-005736b0) · [`005736dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/005735cc.md#insn-005736dc) · [`0057371c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/005735cc.md#insn-0057371c)
- 新版 `005736b0`（命令位置の公開資料なし） · `005736dc`（命令位置の公開資料なし） · `0057371c`（命令位置の公開資料なし）

~~~diff
- 005736b0 ["COPY", "tmp:0:8", ["const:1e3:8"]]
- 005736b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005736b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005736b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005736b0 ["COPY", "tmp:0:8", ["const:27d:8"]]
+ 005736b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005736b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005736b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005736b0 bytes 008c0791
+ 005736b0 bytes 00f40991
- 005736dc ["COPY", "tmp:0:8", ["const:1e3:8"]]
- 005736dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005736dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005736dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005736dc ["COPY", "tmp:0:8", ["const:27d:8"]]
+ 005736dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005736dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005736dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005736dc bytes 218c0791
+ 005736dc bytes 21f40991
- 0057371c ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 0057371c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057371c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057371c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057371c ["COPY", "tmp:0:8", ["const:648:8"]]
+ 0057371c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057371c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057371c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057371c bytes 08e11791
+ 0057371c bytes 08211991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68af5d3ce5320423208ef2e27d038ef8"></a>

### [`00573960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/00573960.md) → [`00573960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573960.md) FUN_00573960

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0057321c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/0057321c.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`0057321c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/0057321c.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.15% / 新版 97.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00573d1c",
      "incomplete_value": false,
      "site": "00573d20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00573d1c",
      "incomplete_value": false,
      "site": "00573d20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:750:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00573ad4",
      "incomplete_value": false,
      "site": "00573ae0",
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
            "const:6ec:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00573ad4",
      "incomplete_value": false,
      "site": "00573ae0",
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
            "const:661:8"
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
      "005739b4",
      "READ",
      [
        "storage",
        "00c1b4a8",
        null,
        "pointer"
      ]
    ],
    [
      "00573a30",
      "PARAM",
      [
        "storage",
        "0029e661",
        null,
        null
      ]
    ],
    [
      "00573aa0",
      "PARAM",
      [
        "storage",
        "00293ab2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005739b4",
      "READ",
      [
        "storage",
        "00c1b4f8",
        null,
        "pointer"
      ]
    ],
    [
      "00573a30",
      "PARAM",
      [
        "storage",
        "0029e6ec",
        null,
        null
      ]
    ],
    [
      "00573aa0",
      "PARAM",
      [
        "storage",
        "00293a25",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005739b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/00573960.md#insn-005739b0) · [`005739b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/00573960.md#insn-005739b4) · [`005739b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/00573960.md#insn-005739b8)
- 新版 `005739b0`（命令位置の公開資料なし） · `005739b4`（命令位置の公開資料なし）

~~~diff
- 005739b0 ["COPY", "tmp:0:8", ["const:ab2:8"]]
- 005739b0 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 005739b0 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 005739b0 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 005739b0 ["COPY", "tmp:0:8", ["const:a25:8"]]
+ 005739b0 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 005739b0 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 005739b0 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 005739b0 bytes 94ca2a91
+ 005739b0 bytes 94962891
- 005739b4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4a8:8"]]
- 005739b4 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 005739b4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4f8:8"]]
+ 005739b4 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 005739b4 bytes b55642f9
+ 005739b4 bytes b57e42f9
- 005739b8 ["COPY", "register:40b0:8", ["const:29e000:8"]]
- 005739b8 bytes 56e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97df168a06962be759fbb8741550d9ff"></a>

### [`00573e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/00573e38.md) → [`00573e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573e38.md) FUN_00573e38

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 14件 [`00419718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) [`0041cddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cddc.md) [`00437118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437118.md) [`00437898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437898.md) [`0043d234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d234.md) · 呼出先 5件 [`005726a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/005726a8.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 14件 [`00419718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`0041cddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md) [`00437118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437118.md) [`00437898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437898.md) [`0043d234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d234.md) · 呼出先 5件 [`005726a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005726a8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00573e90",
      "incomplete_value": false,
      "site": "00573e90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00573e90",
      "incomplete_value": false,
      "site": "00573e90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
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
      "definition_site": "00573ec0",
      "incomplete_value": false,
      "site": "00573ec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00573ec0",
      "incomplete_value": false,
      "site": "00573ec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "00573e90",
      "DATA",
      [
        "storage",
        "00bf06c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00573ec8",
      "DATA",
      [
        "storage",
        "00bf05d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00573e90",
      "DATA",
      [
        "storage",
        "00bf0718",
        null,
        "undefined *"
      ]
    ],
    [
      "00573ec8",
      "DATA",
      [
        "storage",
        "00bf0628",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00573e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/00573e38.md#insn-00573e88) · [`00573ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/00573e38.md#insn-00573ec0)
- 新版 `00573e88`（命令位置の公開資料なし） · `00573ec0`（命令位置の公開資料なし）

~~~diff
- 00573e88 ["COPY", "tmp:0:8", ["const:6c8:8"]]
- 00573e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00573e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00573e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00573e88 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 00573e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00573e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00573e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00573e88 bytes 08211b91
+ 00573e88 bytes 08611c91
- 00573ec0 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00573ec0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00573ec0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00573ec0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00573ec0 ["COPY", "tmp:0:8", ["const:628:8"]]
+ 00573ec0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00573ec0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00573ec0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00573ec0 bytes 08611791
+ 00573ec0 bytes 08a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc5dcfb0fb58ace7aa4f9266a732c7f0"></a>

### [`00574054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574054.md) → [`00574054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574054.md) FUN_00574054

採用 · 移動量 `+0x0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 34件 [`0042d484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d484.md) [`00453c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00453/00453c78.md) [`0054e408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e408.md) [`0054fd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054f/0054fd90.md) [`005627f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005627f4.md) · 呼出先 6件 [`00573e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/00573e38.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 34件 [`0042d484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d484.md) [`00453c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/00453c78.md) [`0054e408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e408.md) [`0054fd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fd90.md) [`005627f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005627f4.md) · 呼出先 6件 [`00573e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573e38.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "00574094",
      "incomplete_value": false,
      "site": "005740a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574094",
      "incomplete_value": false,
      "site": "005740a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:788:8"
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
      "definition_site": "0057409c",
      "incomplete_value": false,
      "site": "005740a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057409c",
      "incomplete_value": false,
      "site": "005740a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b08:8"
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
      "00574094",
      "PARAM",
      [
        "storage",
        "00be6788",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0057409c",
      "PARAM",
      [
        "storage",
        "00be6b08",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00574094",
      "PARAM",
      [
        "storage",
        "00be67d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0057409c",
      "PARAM",
      [
        "storage",
        "00be6b58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574054.md#insn-00574094) · [`0057409c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574054.md#insn-0057409c)
- 新版 `00574094`（命令位置の公開資料なし） · `0057409c`（命令位置の公開資料なし）

~~~diff
- 00574094 ["COPY", "tmp:0:8", ["const:788:8"]]
- 00574094 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00574094 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00574094 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00574094 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 00574094 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00574094 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00574094 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00574094 bytes 21201e91
+ 00574094 bytes 21601f91
- 0057409c ["COPY", "tmp:0:8", ["const:b08:8"]]
- 0057409c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0057409c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0057409c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0057409c ["COPY", "tmp:0:8", ["const:b58:8"]]
+ 0057409c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0057409c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0057409c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0057409c bytes 42202c91
+ 0057409c bytes 42602d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8abc668ea92bc2282f2236ffd37b629"></a>

### [`00574144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574144.md) → [`00574144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574144.md) FUN_00574144

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00473b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00473/00473b84.md) [`0073bad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bad0.md) · 呼出先 6件 [`00573f44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/00573f44.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`00473b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473b84.md) [`0073bad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bad0.md) · 呼出先 6件 [`00573f44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573f44.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "00574184",
      "incomplete_value": false,
      "site": "00574194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574184",
      "incomplete_value": false,
      "site": "00574194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:788:8"
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
      "definition_site": "0057418c",
      "incomplete_value": false,
      "site": "00574194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057418c",
      "incomplete_value": false,
      "site": "00574194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b08:8"
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
      "00574184",
      "PARAM",
      [
        "storage",
        "00be6788",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0057418c",
      "PARAM",
      [
        "storage",
        "00be6b08",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00574184",
      "PARAM",
      [
        "storage",
        "00be67d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0057418c",
      "PARAM",
      [
        "storage",
        "00be6b58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574144.md#insn-00574184) · [`0057418c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574144.md#insn-0057418c)
- 新版 `00574184`（命令位置の公開資料なし） · `0057418c`（命令位置の公開資料なし）

~~~diff
- 00574184 ["COPY", "tmp:0:8", ["const:788:8"]]
- 00574184 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00574184 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00574184 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00574184 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 00574184 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00574184 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00574184 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00574184 bytes 21201e91
+ 00574184 bytes 21601f91
- 0057418c ["COPY", "tmp:0:8", ["const:b08:8"]]
- 0057418c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0057418c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0057418c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0057418c ["COPY", "tmp:0:8", ["const:b58:8"]]
+ 0057418c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0057418c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0057418c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0057418c bytes 42202c91
+ 0057418c bytes 42602d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2256158416110b15035201f61a4394b9"></a>

### [`0057423c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/0057423c.md) → [`0057423c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057423c.md) FUN_0057423c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00574254",
      "incomplete_value": false,
      "site": "00574258",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574254",
      "incomplete_value": false,
      "site": "00574258",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "00574258",
      "DATA",
      [
        "storage",
        "00bf0668",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00574258",
      "DATA",
      [
        "storage",
        "00bf06b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/0057423c.md#insn-00574254)
- 新版 `00574254`（命令位置の公開資料なし）

~~~diff
- 00574254 ["COPY", "tmp:0:8", ["const:668:8"]]
- 00574254 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00574254 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00574254 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574254 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 00574254 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574254 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574254 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00574254 bytes 08a11991
+ 00574254 bytes 08e11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b39ecb6a472b86ff6d52d6c365bf560f"></a>

### [`005742c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/005742c4.md) → [`005742c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/005742c4.md) FUN_005742c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00572b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572e44.md) [`00575024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00575/00575024.md) [`0073bad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bad0.md) [`0076e98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076e/0076e98c.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 6件 [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md) [`00575024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00575/00575024.md) [`0073bad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bad0.md) [`0076e98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e98c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005742e0",
      "incomplete_value": false,
      "site": "005742e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005742e0",
      "incomplete_value": false,
      "site": "005742e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "005742e4",
      "DATA",
      [
        "storage",
        "00bf0668",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005742e4",
      "DATA",
      [
        "storage",
        "00bf06b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005742e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/005742c4.md#insn-005742e0)
- 新版 `005742e0`（命令位置の公開資料なし）

~~~diff
- 005742e0 ["COPY", "tmp:0:8", ["const:668:8"]]
- 005742e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005742e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005742e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005742e0 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 005742e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005742e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005742e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005742e0 bytes 08a11991
+ 005742e0 bytes 08e11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34f38252fa1313d6c79295b20e4d0c10"></a>

### [`00574344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574344.md) → [`00574344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574344.md) FUN_00574344

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00572b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572b04.md) [`0057462c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/0057462c.md) [`0073ccd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073ccd0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md) [`0057462c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057462c.md) [`0073ccd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073ccd0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00574350",
      "incomplete_value": false,
      "site": "00574354",
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
      "definition_site": "00574350",
      "incomplete_value": false,
      "site": "00574354",
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
      "00574350",
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
      "00574350",
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

- 旧版 [`00574350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574344.md#insn-00574350)
- 新版 `00574350`（命令位置の公開資料なし）

~~~diff
- 00574350 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00574350 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00574350 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00574350 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00574350 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00574350 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00574350 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00574350 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00574350 bytes 000c0c91
+ 00574350 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e8dcd3368b4c690ad216b5019609f93"></a>

### [`00574a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574a08.md) → [`00574a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574a08.md) FUN_00574a08

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005748e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/005748e4.md) · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 1件 [`005748e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/005748e4.md) · 呼出先 8件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00574a70",
      "incomplete_value": true,
      "site": "00574a74",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:500:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574a70",
      "incomplete_value": true,
      "site": "00574a74",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:4b0:8"
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
      "00574a70",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ],
    [
      "00574a70",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00574a70",
      "READ",
      [
        "storage",
        "00c1b500",
        null,
        "pointer"
      ]
    ],
    [
      "00574a70",
      "PARAM",
      [
        "storage",
        "010a28b0",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574a08.md#insn-00574a70)
- 新版 `00574a70`（命令位置の公開資料なし）

~~~diff
- 00574a70 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b0:8"]]
- 00574a70 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00574a70 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:500:8"]]
+ 00574a70 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00574a70 bytes 215842f9
+ 00574a70 bytes 218042f9
~~~


<a id="compare-a2d4e1290bbf85c709f0a24d7dea5a37"></a>

### [`00574bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574bbc.md) → [`00574bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574bbc.md) FUN_00574bbc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0055664c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00556/0055664c.md) [`00985084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00985/00985084.md) · 呼出先 9件 [`00574d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574d68.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md) [`00bdb110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb110.md)
- 新版 呼出元 2件 [`0055664c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00556/0055664c.md) [`00985084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00985/00985084.md) · 呼出先 9件 [`00574d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574d68.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00574c74",
      "incomplete_value": true,
      "site": "00574c78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00574c74",
      "incomplete_value": true,
      "site": "00574c78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00574bf0",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "00574bf4",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "00574c0c",
      "READ",
      [
        "storage",
        "00c13410",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00574bf0",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "00574bf4",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "00574c0c",
      "READ",
      [
        "storage",
        "00c13460",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574bbc.md#insn-00574bf0) · [`00574bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574bbc.md#insn-00574bf4) · [`00574c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574bbc.md#insn-00574c68)
- 新版 `00574bf0`（命令位置の公開資料なし） · `00574bf4`（命令位置の公開資料なし） · `00574c68`（命令位置の公開資料なし）

~~~diff
- 00574bf0 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:e48:8"]]
- 00574bf0 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00574bf0 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:e98:8"]]
+ 00574bf0 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00574bf0 bytes 5a2747f9
+ 00574bf0 bytes 5a4f47f9
- 00574bf4 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:d78:8"]]
- 00574bf4 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00574bf4 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:dc8:8"]]
+ 00574bf4 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 00574bf4 bytes 39bf46f9
+ 00574bf4 bytes 39e746f9
- 00574c68 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d80:8"]]
- 00574c68 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00574c68 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:dd0:8"]]
+ 00574c68 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 00574c68 bytes d6c246f9
+ 00574c68 bytes d6ea46f9
~~~


<a id="compare-516d54e782bdf7a0481866f9dd9198b6"></a>

### [`00574d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574d68.md) → [`00574d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574d68.md) FUN_00574d68

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00574bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574bbc.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md)
- 新版 呼出元 1件 [`00574bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574bbc.md) · 呼出先 9件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md)

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
      "definition_site": "00574dc8",
      "incomplete_value": true,
      "site": "00574dcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:508:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574dc8",
      "incomplete_value": true,
      "site": "00574dcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
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
      "definition_site": "00574e0c",
      "incomplete_value": true,
      "site": "00574e10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00574e0c",
      "incomplete_value": true,
      "site": "00574e10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00574dc8",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "00574dc8",
      "PARAM",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00574e0c",
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
      "00574dc8",
      "READ",
      [
        "storage",
        "00c1b508",
        null,
        "pointer"
      ]
    ],
    [
      "00574dc8",
      "PARAM",
      [
        "storage",
        "010a28d0",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00574e0c",
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

- 旧版 [`00574dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574d68.md#insn-00574dc8) · [`00574e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574d68.md#insn-00574e0c)
- 新版 `00574dc8`（命令位置の公開資料なし） · `00574e0c`（命令位置の公開資料なし）

~~~diff
- 00574dc8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
- 00574dc8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00574dc8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:508:8"]]
+ 00574dc8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00574dc8 bytes 215c42f9
+ 00574dc8 bytes 218442f9
- 00574e0c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 00574e0c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00574e0c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
+ 00574e0c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00574e0c bytes 21f846f9
+ 00574e0c bytes 212047f9
~~~


<a id="compare-55f142b81c407de31419a12a9e65f87b"></a>

### [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) → [`00574ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff8.md) FUN_00574ff8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 15件 [`00588310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00588/00588310.md) [`00592b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592b14.md) [`0059313c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/0059313c.md) [`00593688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593688.md) [`00593a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593a6c.md) · 呼出先 0件 
- 新版 呼出元 15件 [`00588310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588310.md) [`00592b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592b14.md) [`0059313c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/0059313c.md) [`00593688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593688.md) [`00593a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593a6c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00575000",
      "incomplete_value": false,
      "site": "00575004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00575000",
      "incomplete_value": false,
      "site": "00575004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "00575004",
      "DATA",
      [
        "storage",
        "00bf0718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00575004",
      "DATA",
      [
        "storage",
        "00bf0768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00575000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md#insn-00575000)
- 新版 `00575000`（命令位置の公開資料なし）

~~~diff
- 00575000 ["COPY", "tmp:0:8", ["const:718:8"]]
- 00575000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00575000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00575000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00575000 ["COPY", "tmp:0:8", ["const:768:8"]]
+ 00575000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00575000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00575000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00575000 bytes 08611c91
+ 00575000 bytes 08a11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-368e4482035bec270a575c1cd79ecadc"></a>

### [`00575024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00575/00575024.md) → [`00575024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00575/00575024.md) FUN_00575024

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00576334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576334.md) [`00576890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576890.md) [`00588344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00588/00588344.md) [`00588848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00588/00588848.md) · 呼出先 39件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0042d084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d084.md) [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md)
- 新版 呼出元 4件 [`00576334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576334.md) [`00576890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576890.md) [`00588344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588344.md) [`00588848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588848.md) · 呼出先 39件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0042d084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d084.md) [`0042e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 95.23% / 新版 95.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057523c",
      "incomplete_value": false,
      "site": "00575244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057523c",
      "incomplete_value": false,
      "site": "00575244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00575250",
      "incomplete_value": true,
      "site": "00575250",
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
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00575250",
      "incomplete_value": true,
      "site": "00575250",
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
            "const:ad0:8"
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
      "definition_site": "005752a0",
      "incomplete_value": true,
      "site": "005752a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005752a0",
      "incomplete_value": true,
      "site": "005752a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005750d0",
      "READ",
      [
        "storage",
        "00c266d0",
        null,
        "undefined1"
      ]
    ],
    [
      "005750dc",
      "READ",
      [
        "storage",
        "00c266d8",
        null,
        "undefined8"
      ]
    ],
    [
      "005750fc",
      "READ",
      [
        "storage",
        "00c266e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005750d0",
      "READ",
      [
        "storage",
        "00c26710",
        null,
        "undefined1"
      ]
    ],
    [
      "005750dc",
      "READ",
      [
        "storage",
        "00c26718",
        null,
        "undefined8"
      ]
    ],
    [
      "005750fc",
      "READ",
      [
        "storage",
        "00c26720",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005750c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00575/00575024.md#insn-005750c0) · [`0057514c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00575/00575024.md#insn-0057514c) · [`00575154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00575/00575024.md#insn-00575154)
- 新版 `005750c0`（命令位置の公開資料なし） · `0057514c`（命令位置の公開資料なし） · `00575154`（命令位置の公開資料なし）

~~~diff
- 005750c0 ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 005750c0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005750c0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005750c0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005750c0 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 005750c0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005750c0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005750c0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005750c0 bytes 4a411b91
+ 005750c0 bytes 4a411c91
- 0057514c ["COPY", "tmp:0:8", ["const:688:8"]]
- 0057514c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 0057514c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 0057514c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 0057514c ["COPY", "tmp:0:8", ["const:6c8:8"]]
+ 0057514c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 0057514c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 0057514c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 0057514c bytes b5221a91
+ 0057514c bytes b5221b91
- 00575154 ["COPY", "tmp:0:8", ["const:97d:8"]]
- 00575154 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00575154 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00575154 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00575154 ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 00575154 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00575154 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00575154 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00575154 bytes 00f42591
+ 00575154 bytes 00c02391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-660365ba93e844e70f821881537e8763"></a>

### [`005760b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760b0.md) → [`005760b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/005760b0.md) FUN_005760b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005760a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760a8.md) · 呼出先 3件 [`005778b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/005778b0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`005760a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/005760a8.md) · 呼出先 3件 [`005778b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/005778b0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.85% / 新版 97.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00576150",
      "incomplete_value": false,
      "site": "00576154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576150",
      "incomplete_value": false,
      "site": "00576154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "00576154",
      "DATA",
      [
        "storage",
        "00bf0780",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00576154",
      "DATA",
      [
        "storage",
        "00bf07d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760b0.md#insn-00576150)
- 新版 `00576150`（命令位置の公開資料なし）

~~~diff
- 00576150 ["COPY", "tmp:0:8", ["const:780:8"]]
- 00576150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00576150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00576150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00576150 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 00576150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00576150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00576150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00576150 bytes 08011e91
+ 00576150 bytes 08411f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c42644ddacb15ca7269025978ea731a"></a>

### [`00576334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576334.md) → [`00576334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576334.md) FUN_00576334

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00575024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00575/00575024.md) [`00576850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576850.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00575024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00575/00575024.md) [`00576850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576850.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.08% / 新版 97.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005765ec",
      "incomplete_value": false,
      "site": "005765f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005765ec",
      "incomplete_value": false,
      "site": "005765f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:870:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00576450",
      "READ",
      [
        "storage",
        "00c26688",
        null,
        "undefined1"
      ]
    ],
    [
      "00576454",
      "READ",
      [
        "storage",
        "00c26690",
        null,
        "undefined8"
      ]
    ],
    [
      "00576454",
      "READ",
      [
        "storage",
        "00c26698",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00576450",
      "READ",
      [
        "storage",
        "00c266c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00576454",
      "READ",
      [
        "storage",
        "00c266d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00576454",
      "READ",
      [
        "storage",
        "00c266d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576334.md#insn-00576448) · [`005765ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576334.md#insn-005765ec)
- 新版 `00576448`（命令位置の公開資料なし） · `005765ec`（命令位置の公開資料なし）

~~~diff
- 00576448 ["COPY", "tmp:0:8", ["const:688:8"]]
- 00576448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00576448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00576448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00576448 ["COPY", "tmp:0:8", ["const:6c8:8"]]
+ 00576448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00576448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00576448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00576448 bytes 08211a91
+ 00576448 bytes 08211b91
- 005765ec ["COPY", "tmp:0:8", ["const:870:8"]]
- 005765ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005765ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005765ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005765ec ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 005765ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005765ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005765ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005765ec bytes 08c12191
+ 005765ec bytes 08012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-713c6298ee9dc2328371a7616a0d0741"></a>

### [`00576890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576890.md) → [`00576890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576890.md) FUN_00576890

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00575024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00575/00575024.md) [`005784a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/005784a0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00575024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00575/00575024.md) [`005784a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005784a0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.40% / 新版 96.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00576b00",
      "incomplete_value": false,
      "site": "00576b08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576b00",
      "incomplete_value": false,
      "site": "00576b08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "00576960",
      "READ",
      [
        "storage",
        "00c26688",
        null,
        "undefined1"
      ]
    ],
    [
      "00576964",
      "READ",
      [
        "storage",
        "00c26690",
        null,
        "undefined8"
      ]
    ],
    [
      "00576964",
      "READ",
      [
        "storage",
        "00c26698",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00576960",
      "READ",
      [
        "storage",
        "00c266c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00576964",
      "READ",
      [
        "storage",
        "00c266d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00576964",
      "READ",
      [
        "storage",
        "00c266d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576890.md#insn-00576958) · [`00576b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576890.md#insn-00576b00) · [`00576b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576890.md#insn-00576b04)
- 新版 `00576958`（命令位置の公開資料なし） · `00576b00`（命令位置の公開資料なし）

~~~diff
- 00576958 ["COPY", "tmp:0:8", ["const:688:8"]]
- 00576958 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00576958 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00576958 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00576958 ["COPY", "tmp:0:8", ["const:6c8:8"]]
+ 00576958 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00576958 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00576958 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00576958 bytes 08211a91
+ 00576958 bytes 08211b91
- 00576b00 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 00576b00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00576b00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00576b00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00576b00 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 00576b00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00576b00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00576b00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00576b00 bytes 08c12391
+ 00576b00 bytes 08012591
- 00576b04 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00576b04 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35dcefc29a24897584c8c4f29981222a"></a>

### [`00576d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576d9c.md) → [`00576d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576d9c.md) FUN_00576d9c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00577df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577df0.md) [`00578500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578500.md) · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00576eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576eec.md) [`0073ed78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073ed78.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`009bd60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009bd/009bd60c.md)
- 新版 呼出元 2件 [`00577df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577df0.md) [`00578500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578500.md) · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00576eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576eec.md) [`0073ed78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073ed78.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`009bd618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd618.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.81% / 新版 98.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00576dc4",
      "incomplete_value": false,
      "site": "00576dd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576dc4",
      "incomplete_value": false,
      "site": "00576dd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
      "00576dc4",
      "PARAM",
      [
        "storage",
        "00c26670",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00576dc4",
      "PARAM",
      [
        "storage",
        "00c266b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576d9c.md#insn-00576dc4)
- 新版 `00576dc4`（命令位置の公開資料なし）

~~~diff
- 00576dc4 ["COPY", "tmp:0:8", ["const:670:8"]]
- 00576dc4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00576dc4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00576dc4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00576dc4 ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 00576dc4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00576dc4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00576dc4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00576dc4 bytes 21c01991
+ 00576dc4 bytes 21c01a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-167bad4864bebc6e0e3342a6121d1e2c"></a>

### [`00576eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576eec.md) → [`00576eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576eec.md) FUN_00576eec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00576d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576d9c.md) · 呼出先 12件 [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) [`0042fd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fd7c.md) [`00578a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578a28.md) [`00578a78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578a78.md) [`0073a038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a038.md)
- 新版 呼出元 1件 [`00576d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576d9c.md) · 呼出先 12件 [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`0042fd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md) [`00578a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578a28.md) [`00578a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578a78.md) [`0073a038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a038.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00576f8c",
      "incomplete_value": false,
      "site": "00576f8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576f8c",
      "incomplete_value": false,
      "site": "00576f8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "00576f8c",
      "DATA",
      [
        "storage",
        "00bf0970",
        null,
        "undefined *"
      ]
    ],
    [
      "00576fc8",
      "READ",
      [
        "storage",
        "00bf0990",
        null,
        "pointer"
      ]
    ],
    [
      "00576fc8",
      "READ",
      [
        "storage",
        "00bf0998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00576f8c",
      "DATA",
      [
        "storage",
        "00bf09c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00576fc8",
      "READ",
      [
        "storage",
        "00bf09e0",
        null,
        "pointer"
      ]
    ],
    [
      "00576fc8",
      "READ",
      [
        "storage",
        "00bf09e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576eec.md#insn-00576f84)
- 新版 `00576f84`（命令位置の公開資料なし）

~~~diff
- 00576f84 ["COPY", "tmp:0:8", ["const:970:8"]]
- 00576f84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00576f84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00576f84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00576f84 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00576f84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00576f84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00576f84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00576f84 bytes 08c12591
+ 00576f84 bytes 08012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e8b005c89f594a1764c438c4965524c"></a>

### [`0057715c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/0057715c.md) → [`0057715c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057715c.md) FUN_0057715c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00577df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577df0.md) [`00578500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578500.md) · 呼出先 4件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 2件 [`00577df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577df0.md) [`00578500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578500.md) · 呼出先 4件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.28% / 新版 98.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00577190",
      "incomplete_value": false,
      "site": "005771a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577190",
      "incomplete_value": false,
      "site": "005771a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:688:8"
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
      "definition_site": "00577204",
      "incomplete_value": false,
      "site": "0057720c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577204",
      "incomplete_value": false,
      "site": "0057720c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
      "00577190",
      "PARAM",
      [
        "storage",
        "00c26688",
        null,
        "undefined1"
      ]
    ],
    [
      "00577204",
      "PARAM",
      [
        "storage",
        "00c26670",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00577190",
      "PARAM",
      [
        "storage",
        "00c266c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00577204",
      "PARAM",
      [
        "storage",
        "00c266b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/0057715c.md#insn-00577190) · [`00577204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/0057715c.md#insn-00577204)
- 新版 `00577190`（命令位置の公開資料なし） · `00577204`（命令位置の公開資料なし）

~~~diff
- 00577190 ["COPY", "tmp:0:8", ["const:688:8"]]
- 00577190 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00577190 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00577190 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00577190 ["COPY", "tmp:0:8", ["const:6c8:8"]]
+ 00577190 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00577190 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00577190 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00577190 bytes 21201a91
+ 00577190 bytes 21201b91
- 00577204 ["COPY", "tmp:0:8", ["const:670:8"]]
- 00577204 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00577204 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00577204 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00577204 ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 00577204 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00577204 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00577204 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00577204 bytes 21c01991
+ 00577204 bytes 21c01a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d3e556e4a2646f2ca691c7c9b01ddcc"></a>

### [`0057753c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/0057753c.md) → [`0057753c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057753c.md) FUN_0057753c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00577620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577620.md) [`00588e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00588/00588e80.md) [`00588f0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00588/00588f0c.md) · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 3件 [`00577620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577620.md) [`00588e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588e80.md) [`00588f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588f0c.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.49% / 新版 96.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00577554",
      "incomplete_value": false,
      "site": "00577558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577554",
      "incomplete_value": false,
      "site": "00577558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "00577558",
      "DATA",
      [
        "storage",
        "00bf0718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00577558",
      "DATA",
      [
        "storage",
        "00bf0768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/0057753c.md#insn-00577554)
- 新版 `00577554`（命令位置の公開資料なし）

~~~diff
- 00577554 ["COPY", "tmp:0:8", ["const:718:8"]]
- 00577554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00577554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00577554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00577554 ["COPY", "tmp:0:8", ["const:768:8"]]
+ 00577554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00577554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00577554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00577554 bytes 08611c91
+ 00577554 bytes 08a11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d9a0f9016c45eea47662827b6a303e3"></a>

### [`00577644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577644.md) → [`00577644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577644.md) FUN_00577644

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00577650",
      "incomplete_value": false,
      "site": "0057765c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577650",
      "incomplete_value": false,
      "site": "0057765c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "0057765c",
      "DATA",
      [
        "storage",
        "00bf0780",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057765c",
      "DATA",
      [
        "storage",
        "00bf07d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577644.md#insn-00577650)
- 新版 `00577650`（命令位置の公開資料なし）

~~~diff
- 00577650 ["COPY", "tmp:0:8", ["const:780:8"]]
- 00577650 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00577650 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00577650 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00577650 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 00577650 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00577650 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00577650 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00577650 bytes 4a011e91
+ 00577650 bytes 4a411f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04b89e901b5bb92436c80f2b88ae1595"></a>

### [`00577688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577688.md) → [`00577688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577688.md) FUN_00577688

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005776a0",
      "incomplete_value": false,
      "site": "005776ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005776a0",
      "incomplete_value": false,
      "site": "005776ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "005776ac",
      "DATA",
      [
        "storage",
        "00bf0780",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005776ac",
      "DATA",
      [
        "storage",
        "00bf07d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005776a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577688.md#insn-005776a0)
- 新版 `005776a0`（命令位置の公開資料なし）

~~~diff
- 005776a0 ["COPY", "tmp:0:8", ["const:780:8"]]
- 005776a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005776a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005776a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005776a0 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 005776a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005776a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005776a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005776a0 bytes 08011e91
+ 005776a0 bytes 08411f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51d8559d01b9355274b94dd028faafa6"></a>

### [`005776e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/005776e4.md) → [`005776e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/005776e4.md) FUN_005776e4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00577710",
      "incomplete_value": false,
      "site": "00577710",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577710",
      "incomplete_value": false,
      "site": "00577710",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "00577710",
      "DATA",
      [
        "storage",
        "00bf0780",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00577710",
      "DATA",
      [
        "storage",
        "00bf07d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/005776e4.md#insn-00577708)
- 新版 `00577708`（命令位置の公開資料なし）

~~~diff
- 00577708 ["COPY", "tmp:0:8", ["const:780:8"]]
- 00577708 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00577708 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00577708 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00577708 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 00577708 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00577708 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00577708 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00577708 bytes 08011e91
+ 00577708 bytes 08411f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-405d75e253ca554d73a7584c8f332a36"></a>

### [`0057776c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/0057776c.md) → [`0057776c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057776c.md) FUN_0057776c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00577788",
      "incomplete_value": false,
      "site": "00577788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577788",
      "incomplete_value": false,
      "site": "00577788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "00577788",
      "DATA",
      [
        "storage",
        "00bf0780",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00577788",
      "DATA",
      [
        "storage",
        "00bf07d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/0057776c.md#insn-00577784)
- 新版 `00577784`（命令位置の公開資料なし）

~~~diff
- 00577784 ["COPY", "tmp:0:8", ["const:780:8"]]
- 00577784 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00577784 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00577784 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00577784 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 00577784 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00577784 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00577784 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00577784 bytes 29011e91
+ 00577784 bytes 29411f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-086976d95fa7d38dcffc4dd6c24220e6"></a>

### [`00577b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577b80.md) → [`00577b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577b80.md) FUN_00577b80

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00576334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576334.md) [`00588344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00588/00588344.md) · 呼出先 3件 [`00b73360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73360.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 2件 [`00576334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576334.md) [`00588344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588344.md) · 呼出先 3件 [`00b733a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b733a4.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00577ba0",
      "incomplete_value": true,
      "site": "00577ba4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00577ba0",
      "incomplete_value": true,
      "site": "00577ba4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "definition_site": "00577ba8",
      "incomplete_value": true,
      "site": "00577bb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:520:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577ba8",
      "incomplete_value": true,
      "site": "00577bb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4d0:8"
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
      "definition_site": "00577bac",
      "incomplete_value": true,
      "site": "00577bb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:528:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577bac",
      "incomplete_value": true,
      "site": "00577bb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4d8:8"
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
      "00577b9c",
      "READ",
      [
        "storage",
        "00c1b4c8",
        null,
        "pointer"
      ]
    ],
    [
      "00577ba4",
      "DATA",
      [
        "storage",
        "00c12c10",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00577ba8",
      "READ",
      [
        "storage",
        "00c1b4d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00577b9c",
      "READ",
      [
        "storage",
        "00c1b518",
        null,
        "pointer"
      ]
    ],
    [
      "00577ba4",
      "DATA",
      [
        "storage",
        "00c12c60",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00577ba8",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577b80.md#insn-00577b9c) · [`00577ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577b80.md#insn-00577ba8) · [`00577bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577b80.md#insn-00577bac)
- 新版 `00577b9c`（命令位置の公開資料なし） · `00577ba8`（命令位置の公開資料なし） · `00577bac`（命令位置の公開資料なし）

~~~diff
- 00577b9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4c8:8"]]
- 00577b9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00577b9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:518:8"]]
+ 00577b9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00577b9c bytes 086542f9
+ 00577b9c bytes 088d42f9
- 00577ba8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4d0:8"]]
- 00577ba8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00577ba8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:520:8"]]
+ 00577ba8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00577ba8 bytes 216842f9
+ 00577ba8 bytes 219042f9
- 00577bac ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:4d8:8"]]
- 00577bac ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00577bac ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:528:8"]]
+ 00577bac ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00577bac bytes 426c42f9
+ 00577bac bytes 429442f9
~~~


<a id="compare-a32c4468948641f6a3c76bfc7de53310"></a>

### [`00577bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577bb4.md) → [`00577bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577bb4.md) FUN_00577bb4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00577bcc",
      "incomplete_value": false,
      "site": "00577bd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577bcc",
      "incomplete_value": false,
      "site": "00577bd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "00577bd0",
      "DATA",
      [
        "storage",
        "00bf0870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00577bd0",
      "DATA",
      [
        "storage",
        "00bf08c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577bb4.md#insn-00577bcc)
- 新版 `00577bcc`（命令位置の公開資料なし）

~~~diff
- 00577bcc ["COPY", "tmp:0:8", ["const:870:8"]]
- 00577bcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00577bcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00577bcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00577bcc ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00577bcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00577bcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00577bcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00577bcc bytes 29c12191
+ 00577bcc bytes 29012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-606118c83e8261898d028f4809b6c17d"></a>

### [`00577c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577c00.md) → [`00577c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577c00.md) FUN_00577c00

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00577c18",
      "incomplete_value": false,
      "site": "00577c1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577c18",
      "incomplete_value": false,
      "site": "00577c1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "00577c1c",
      "DATA",
      [
        "storage",
        "00bf0870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00577c1c",
      "DATA",
      [
        "storage",
        "00bf08c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577c00.md#insn-00577c18)
- 新版 `00577c18`（命令位置の公開資料なし）

~~~diff
- 00577c18 ["COPY", "tmp:0:8", ["const:870:8"]]
- 00577c18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00577c18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00577c18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00577c18 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00577c18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00577c18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00577c18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00577c18 bytes 29c12191
+ 00577c18 bytes 29012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af033e3a9279f48ea866d48954a6ea41"></a>

### [`00577c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577c48.md) → [`00577c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577c48.md) FUN_00577c48

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00577c70",
      "incomplete_value": false,
      "site": "00577c70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577c70",
      "incomplete_value": false,
      "site": "00577c70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "00577c70",
      "DATA",
      [
        "storage",
        "00bf0870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00577c70",
      "DATA",
      [
        "storage",
        "00bf08c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577c6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577c48.md#insn-00577c6c)
- 新版 `00577c6c`（命令位置の公開資料なし）

~~~diff
- 00577c6c ["COPY", "tmp:0:8", ["const:870:8"]]
- 00577c6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00577c6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00577c6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00577c6c ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00577c6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00577c6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00577c6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00577c6c bytes 29c12191
+ 00577c6c bytes 29012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3572e86b3fc954008c9ff91516832614"></a>

### [`00577ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577ce8.md) → [`00577ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577ce8.md) FUN_00577ce8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00577d08",
      "incomplete_value": false,
      "site": "00577d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577d08",
      "incomplete_value": false,
      "site": "00577d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "00577d08",
      "DATA",
      [
        "storage",
        "00bf0870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00577d08",
      "DATA",
      [
        "storage",
        "00bf08c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577ce8.md#insn-00577d04)
- 新版 `00577d04`（命令位置の公開資料なし）

~~~diff
- 00577d04 ["COPY", "tmp:0:8", ["const:870:8"]]
- 00577d04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00577d04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00577d04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00577d04 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00577d04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00577d04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00577d04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00577d04 bytes 29c12191
+ 00577d04 bytes 29012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9821421098204d6cd157535666c4a7f6"></a>

### [`00578220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578220.md) → [`00578220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578220.md) FUN_00578220

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00578238",
      "incomplete_value": false,
      "site": "0057823c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578238",
      "incomplete_value": false,
      "site": "0057823c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "0057823c",
      "DATA",
      [
        "storage",
        "00bf08f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057823c",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578220.md#insn-00578238)
- 新版 `00578238`（命令位置の公開資料なし）

~~~diff
- 00578238 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 00578238 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00578238 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00578238 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00578238 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 00578238 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00578238 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00578238 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00578238 bytes 29c12391
+ 00578238 bytes 29012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92560f75735fca22a5bd818213b8a8fb"></a>

### [`00578290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578290.md) → [`00578290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578290.md) FUN_00578290

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005782a8",
      "incomplete_value": false,
      "site": "005782ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005782a8",
      "incomplete_value": false,
      "site": "005782ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "005782ac",
      "DATA",
      [
        "storage",
        "00bf08f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005782ac",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005782a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578290.md#insn-005782a8)
- 新版 `005782a8`（命令位置の公開資料なし）

~~~diff
- 005782a8 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 005782a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005782a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005782a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005782a8 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 005782a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005782a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005782a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005782a8 bytes 29c12391
+ 005782a8 bytes 29012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c040875e6fa324367502398218a3ce97"></a>

### [`005782fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/005782fc.md) → [`005782fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005782fc.md) FUN_005782fc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057831c",
      "incomplete_value": false,
      "site": "00578324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057831c",
      "incomplete_value": false,
      "site": "00578324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "00578324",
      "DATA",
      [
        "storage",
        "00bf08f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00578324",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057831c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/005782fc.md#insn-0057831c) · [`00578320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/005782fc.md#insn-00578320)
- 新版 `0057831c`（命令位置の公開資料なし） · `00578320`（命令位置の公開資料なし）

~~~diff
- 0057831c ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 0057831c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057831c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057831c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057831c ["COPY", "tmp:0:8", ["const:940:8"]]
+ 0057831c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057831c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057831c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057831c bytes 08c12391
+ 0057831c bytes 08012591
- 00578320 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00578320 bytes f30300aa
+ 00578320 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00578320 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fef463d8370762462ee4956445e8cfdd"></a>

### [`005783a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/005783a4.md) → [`005783a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005783a4.md) FUN_005783a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005783b8",
      "incomplete_value": true,
      "site": "005783c0",
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
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005783b8",
      "incomplete_value": true,
      "site": "005783c0",
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
            "const:8f0:8"
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
      "005783c0",
      "DATA",
      [
        "storage",
        "00bf08f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005783c0",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005783b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/005783a4.md#insn-005783b8)
- 新版 `005783b8`（命令位置の公開資料なし）

~~~diff
- 005783b8 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 005783b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005783b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005783b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005783b8 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 005783b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005783b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005783b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005783b8 bytes 08c12391
+ 005783b8 bytes 08012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7d73eefd84e64ea280ce2e050410eff"></a>

### [`005788ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/005788ec.md) → [`005788ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005788ec.md) FUN_005788ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00578900",
      "incomplete_value": false,
      "site": "00578904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578900",
      "incomplete_value": false,
      "site": "00578904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "00578904",
      "DATA",
      [
        "storage",
        "00bf0970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00578904",
      "DATA",
      [
        "storage",
        "00bf09c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/005788ec.md#insn-00578900)
- 新版 `00578900`（命令位置の公開資料なし）

~~~diff
- 00578900 ["COPY", "tmp:0:8", ["const:970:8"]]
- 00578900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00578900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00578900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00578900 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00578900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00578900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00578900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00578900 bytes 08c12591
+ 00578900 bytes 08012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a58d189ef8d8af8e0d7b9bd1b7193b25"></a>

### [`00578948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578948.md) → [`00578948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578948.md) FUN_00578948

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00578960",
      "incomplete_value": false,
      "site": "00578964",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578960",
      "incomplete_value": false,
      "site": "00578964",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "00578964",
      "DATA",
      [
        "storage",
        "00bf0970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00578964",
      "DATA",
      [
        "storage",
        "00bf09c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578948.md#insn-00578960)
- 新版 `00578960`（命令位置の公開資料なし）

~~~diff
- 00578960 ["COPY", "tmp:0:8", ["const:970:8"]]
- 00578960 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00578960 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00578960 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00578960 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00578960 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00578960 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00578960 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00578960 bytes 08c12591
+ 00578960 bytes 08012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56caeba2e0105a6d24886e7849d2b683"></a>

### [`005789a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/005789a4.md) → [`005789a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005789a4.md) FUN_005789a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005789c8",
      "incomplete_value": false,
      "site": "005789c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005789c8",
      "incomplete_value": false,
      "site": "005789c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "005789c8",
      "DATA",
      [
        "storage",
        "00bf0970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005789c8",
      "DATA",
      [
        "storage",
        "00bf09c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005789c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/005789a4.md#insn-005789c4)
- 新版 `005789c4`（命令位置の公開資料なし）

~~~diff
- 005789c4 ["COPY", "tmp:0:8", ["const:970:8"]]
- 005789c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005789c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005789c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005789c4 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 005789c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005789c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005789c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005789c4 bytes 29c12591
+ 005789c4 bytes 29012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d20850cab89a593945808bf144f19826"></a>

### [`005789f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/005789f4.md) → [`005789f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005789f4.md) FUN_005789f4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00578a00",
      "incomplete_value": false,
      "site": "00578a00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578a00",
      "incomplete_value": false,
      "site": "00578a00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "00578a00",
      "DATA",
      [
        "storage",
        "00bf0970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00578a00",
      "DATA",
      [
        "storage",
        "00bf09c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005789fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/005789f4.md#insn-005789fc)
- 新版 `005789fc`（命令位置の公開資料なし）

~~~diff
- 005789fc ["COPY", "tmp:0:8", ["const:970:8"]]
- 005789fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005789fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005789fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005789fc ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 005789fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005789fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005789fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005789fc bytes 29c12591
+ 005789fc bytes 29012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5d4be719587456bb0fa6d2e88b0b4bf"></a>

### [`00578bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578bc0.md) → [`00578bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578bc0.md) _INIT_36

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 79.61% / 新版 79.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 7件, `store_value` 5件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00578bfc",
      "incomplete_value": true,
      "site": "00578c18",
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
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578bfc",
      "incomplete_value": true,
      "site": "00578c18",
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
                "const:2dd:8"
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
      "definition_site": "00578c20",
      "incomplete_value": true,
      "site": "00578c3c",
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
                "const:38a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578c20",
      "incomplete_value": true,
      "site": "00578c3c",
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
                "const:2f0:8"
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
      "definition_site": "00578c40",
      "incomplete_value": true,
      "site": "00578c5c",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578c40",
      "incomplete_value": true,
      "site": "00578c5c",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:46:8"
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
      "00578bfc",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00578c20",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00578c40",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00578bfc",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00578c20",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00578c40",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578bc0.md#insn-00578df8) · [`00578e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578bc0.md#insn-00578e38)
- 新版 `00578df8`（命令位置の公開資料なし）

~~~diff
- 00578df8 ["INT_ADD", "register:40f0:8", ["const:578df8:8", "const:4:8"]]
- 00578df8 ["CALL", null, ["callee:00bdafe0:8"]]
- 00578df8 bytes 66881994
+ 00578df8 ["INT_ADD", "register:40f0:8", ["const:578df8:8", "const:4:8"]]
+ 00578df8 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00578df8 bytes 7a881994
- 00578e38 ["INT_ADD", "register:40f0:8", ["const:578e38:8", "const:4:8"]]
- 00578e38 ["CALL", null, ["callee:00bdafe0:8"]]
- 00578e38 bytes 56881994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-233472a4b1f141cda4a509e7c3a0dbeb"></a>

### [`00578ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578ff0.md) → [`00578ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md) FUN_00578ff0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 15件 [`00579e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/00579e0c.md) [`0057a9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a9e0.md) [`0057c274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c274.md) [`0057cc9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057cc9c.md) [`0057de8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057de8c.md) · 呼出先 1件 [`00579074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/00579074.md)
- 新版 呼出元 15件 [`00579e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/00579e0c.md) [`0057a9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057a9e0.md) [`0057c274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057c274.md) [`0057cc9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057cc9c.md) [`0057de8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057de8c.md) · 呼出先 1件 [`00579074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/00579074.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057900c",
      "incomplete_value": false,
      "site": "00579014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057900c",
      "incomplete_value": false,
      "site": "00579014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
      "00579014",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00579014",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057900c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578ff0.md#insn-0057900c) · [`00579010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578ff0.md#insn-00579010)
- 新版 `0057900c`（命令位置の公開資料なし） · `00579010`（命令位置の公開資料なし）

~~~diff
- 0057900c ["COPY", "tmp:0:8", ["const:a10:8"]]
- 0057900c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057900c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057900c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057900c ["COPY", "tmp:0:8", ["const:a60:8"]]
+ 0057900c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057900c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057900c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057900c bytes 08412891
+ 0057900c bytes 08812991
- 00579010 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00579010 bytes f50300aa
+ 00579010 ["COPY", "register:40a8:8", ["register:4000:8"]]
+ 00579010 bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9178dab7254e13cda113be1bd89ecad0"></a>

### [`005791cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/005791cc.md) → [`005791cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/005791cc.md) FUN_005791cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057922c",
      "incomplete_value": true,
      "site": "0057922c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:1f4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057922c",
      "incomplete_value": true,
      "site": "0057922c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:169:8"
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
      "definition_site": "00579300",
      "incomplete_value": true,
      "site": "00579300",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:571:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579300",
      "incomplete_value": true,
      "site": "00579300",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5fe:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00579304",
      "incomplete_value": true,
      "site": "00579304",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00579304",
      "incomplete_value": true,
      "site": "00579304",
      "value": [
        "LOAD",
        "8",
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
      "00579224",
      "READ",
      [
        "storage",
        "002a3169",
        null,
        "string"
      ]
    ],
    [
      "005792b4",
      "PARAM",
      [
        "storage",
        "0029e299",
        null,
        "string"
      ]
    ],
    [
      "005792d4",
      "PARAM",
      [
        "storage",
        "002a65e5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00579224",
      "READ",
      [
        "storage",
        "002a31f4",
        null,
        "string"
      ]
    ],
    [
      "005792b4",
      "PARAM",
      [
        "storage",
        "0029e324",
        null,
        "string"
      ]
    ],
    [
      "005792d4",
      "PARAM",
      [
        "storage",
        "002a667f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00579220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/005791cc.md#insn-00579220) · [`005792b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/005791cc.md#insn-005792b4) · [`005792d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/005791cc.md#insn-005792d4)
- 新版 `00579220`（命令位置の公開資料なし） · `005792b4`（命令位置の公開資料なし） · `005792d4`（命令位置の公開資料なし）

~~~diff
- 00579220 ["COPY", "tmp:0:8", ["const:169:8"]]
- 00579220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00579220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00579220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00579220 ["COPY", "tmp:0:8", ["const:1f4:8"]]
+ 00579220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00579220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00579220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00579220 bytes 08a50591
+ 00579220 bytes 08d10791
- 005792b4 ["COPY", "tmp:0:8", ["const:299:8"]]
- 005792b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005792b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005792b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005792b4 ["COPY", "tmp:0:8", ["const:324:8"]]
+ 005792b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005792b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005792b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005792b4 bytes 21640a91
+ 005792b4 bytes 21900c91
- 005792d4 ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 005792d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005792d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005792d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005792d4 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 005792d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005792d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005792d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005792d4 bytes 00941791
+ 005792d4 bytes 00fc1991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dbed46cce2c372d2a15670b7bff0137"></a>

### [`005795b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/005795b4.md) → [`005795b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/005795b4.md) FUN_005795b4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005795cc",
      "incomplete_value": false,
      "site": "005795d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005795cc",
      "incomplete_value": false,
      "site": "005795d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
      "005795d0",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005795d0",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005795cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/005795b4.md#insn-005795cc)
- 新版 `005795cc`（命令位置の公開資料なし）

~~~diff
- 005795cc ["COPY", "tmp:0:8", ["const:a10:8"]]
- 005795cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005795cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005795cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005795cc ["COPY", "tmp:0:8", ["const:a60:8"]]
+ 005795cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005795cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005795cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005795cc bytes 29412891
+ 005795cc bytes 29812991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1084ff31751af14acb3cdf722deb9332"></a>

### [`00579608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/00579608.md) → [`00579608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/00579608.md) FUN_00579608

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00579610",
      "incomplete_value": false,
      "site": "00579614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579610",
      "incomplete_value": false,
      "site": "00579614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "00579614",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00579614",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00579610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/00579608.md#insn-00579610)
- 新版 `00579610`（命令位置の公開資料なし）

~~~diff
- 00579610 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 00579610 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00579610 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00579610 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00579610 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 00579610 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00579610 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00579610 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00579610 bytes 29c12791
+ 00579610 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b48d3a162687ceb8c9f55156caaf1a22"></a>

### [`00579628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/00579628.md) → [`00579628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/00579628.md) FUN_00579628

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00579630",
      "incomplete_value": false,
      "site": "00579634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579630",
      "incomplete_value": false,
      "site": "00579634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "00579634",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00579634",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00579630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/00579628.md#insn-00579630)
- 新版 `00579630`（命令位置の公開資料なし）

~~~diff
- 00579630 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 00579630 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00579630 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00579630 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00579630 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 00579630 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00579630 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00579630 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00579630 bytes 29c12791
+ 00579630 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05ba9c3a671419863c32a351df402154"></a>

### [`00579668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/00579668.md) → [`00579668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/00579668.md) _INIT_37

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 8件, `store_value` 3件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005796a8",
      "incomplete_value": true,
      "site": "005796c4",
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
                "live",
                "register:4048:8"
              ],
              [
                "leaf",
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005796a8",
      "incomplete_value": true,
      "site": "005796c4",
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
                "live",
                "register:4048:8"
              ],
              [
                "leaf",
                "const:2dd:8"
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
      "definition_site": "005796ec",
      "incomplete_value": true,
      "site": "00579708",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005796ec",
      "incomplete_value": true,
      "site": "00579708",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:46:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0057970c",
      "incomplete_value": true,
      "site": "00579724",
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
                "const:6ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057970c",
      "incomplete_value": true,
      "site": "00579724",
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
                "const:73b:8"
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
      "005796a8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "005796cc",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "005796ec",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005796a8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "005796cc",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "005796ec",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00579900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/00579668.md#insn-00579900) · [`00579698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/00579668.md#insn-00579698)
- 新版 `00579900`（命令位置の公開資料なし） · `00579698`（命令位置の公開資料なし）

~~~diff
- 00579900 ["INT_ADD", "register:40f0:8", ["const:579900:8", "const:4:8"]]
- 00579900 ["CALL", null, ["callee:00bdafe0:8"]]
- 00579900 bytes a4851994
+ 00579900 ["INT_ADD", "register:40f0:8", ["const:579900:8", "const:4:8"]]
+ 00579900 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00579900 bytes b8851994
- 00579698 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 00579698 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00579698 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00579698 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00579698 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 00579698 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00579698 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00579698 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00579698 bytes 73821a91
+ 00579698 bytes 73821b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1c5c494c136afcae085d6a8bcd78b6a"></a>

### [`00579ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/00579ab8.md) → [`00579ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/00579ab8.md) FUN_00579ab8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578fc4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.25% / 新版 94.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00579b08",
      "incomplete_value": true,
      "site": "00579b08",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:674:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579b08",
      "incomplete_value": true,
      "site": "00579b08",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:5da:8"
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
      "definition_site": "00579c18",
      "incomplete_value": true,
      "site": "00579c28",
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
                "const:bed:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579c18",
      "incomplete_value": true,
      "site": "00579c28",
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
                "const:c7a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00579ce8",
      "incomplete_value": false,
      "site": "00579cf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579ce8",
      "incomplete_value": false,
      "site": "00579cf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
      "00579aec",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "00579c18",
      "READ",
      [
        "storage",
        "00295c7a",
        null,
        "string"
      ]
    ],
    [
      "00579cf4",
      "DATA",
      [
        "storage",
        "00bf0b70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00579aec",
      "READ",
      [
        "storage",
        "002a6674",
        null,
        "string"
      ]
    ],
    [
      "00579c18",
      "READ",
      [
        "storage",
        "00295bed",
        null,
        "string"
      ]
    ],
    [
      "00579cf4",
      "DATA",
      [
        "storage",
        "00bf0bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00579ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/00579ab8.md#insn-00579ae0) · [`00579c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/00579ab8.md#insn-00579c10) · [`00579ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/00579ab8.md#insn-00579ce8)
- 新版 `00579ae0`（命令位置の公開資料なし） · `00579c10`（命令位置の公開資料なし） · `00579ce8`（命令位置の公開資料なし）

~~~diff
- 00579ae0 ["COPY", "tmp:0:8", ["const:5da:8"]]
- 00579ae0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00579ae0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00579ae0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00579ae0 ["COPY", "tmp:0:8", ["const:674:8"]]
+ 00579ae0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00579ae0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00579ae0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00579ae0 bytes 4a691791
+ 00579ae0 bytes 4ad11991
- 00579c10 ["COPY", "tmp:0:8", ["const:c7a:8"]]
- 00579c10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00579c10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00579c10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00579c10 ["COPY", "tmp:0:8", ["const:bed:8"]]
+ 00579c10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00579c10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00579c10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00579c10 bytes 29e93191
+ 00579c10 bytes 29b52f91
- 00579ce8 ["COPY", "tmp:0:8", ["const:b70:8"]]
- 00579ce8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00579ce8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00579ce8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00579ce8 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 00579ce8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00579ce8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00579ce8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00579ce8 bytes 08c12d91
+ 00579ce8 bytes 08012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cfb9cc083678a52340bc40ce09f34a1"></a>

### [`00579e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/00579e0c.md) → [`00579e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/00579e0c.md) FUN_00579e0c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005907e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/005907e4.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578ff0.md)
- 新版 呼出元 1件 [`005907e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/005907e4.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00579e34",
      "incomplete_value": false,
      "site": "00579e38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579e34",
      "incomplete_value": false,
      "site": "00579e38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
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
      "00579e38",
      "DATA",
      [
        "storage",
        "00bf0aa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00579e38",
      "DATA",
      [
        "storage",
        "00bf0af8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00579e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/00579e0c.md#insn-00579e34)
- 新版 `00579e34`（命令位置の公開資料なし）

~~~diff
- 00579e34 ["COPY", "tmp:0:8", ["const:aa8:8"]]
- 00579e34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00579e34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00579e34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00579e34 ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 00579e34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00579e34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00579e34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00579e34 bytes 08a12a91
+ 00579e34 bytes 08e12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d609903c045106f89d9136cb882ae95"></a>

### [`00579ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/00579ea8.md) → [`00579ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/00579ea8.md) FUN_00579ea8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`0057945c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/0057945c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`0057945c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/0057945c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.24% / 新版 97.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a0ac",
      "incomplete_value": true,
      "site": "0057a0ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:60e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a0ac",
      "incomplete_value": true,
      "site": "0057a0ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:583:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057a05c",
      "PARAM",
      [
        "storage",
        "0029e2aa",
        null,
        null
      ]
    ],
    [
      "0057a098",
      "READ",
      [
        "storage",
        "002a3583",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057a05c",
      "PARAM",
      [
        "storage",
        "0029e335",
        null,
        null
      ]
    ],
    [
      "0057a098",
      "READ",
      [
        "storage",
        "002a360e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00579fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/00579ea8.md#insn-00579fa8) · [`0057a090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/00579ea8.md#insn-0057a090)
- 新版 `00579fa8`（命令位置の公開資料なし） · `0057a090`（命令位置の公開資料なし）

~~~diff
- 00579fa8 ["COPY", "tmp:0:8", ["const:2aa:8"]]
- 00579fa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00579fa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00579fa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00579fa8 ["COPY", "tmp:0:8", ["const:335:8"]]
+ 00579fa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00579fa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00579fa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00579fa8 bytes 08a90a91
+ 00579fa8 bytes 08d50c91
- 0057a090 ["COPY", "tmp:0:8", ["const:583:8"]]
- 0057a090 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057a090 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057a090 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057a090 ["COPY", "tmp:0:8", ["const:60e:8"]]
+ 0057a090 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057a090 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057a090 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057a090 bytes 290d1691
+ 0057a090 bytes 29391891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc250ee0dffb4c4bbcfb17c1ff55670a"></a>

### [`0057a1bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a1bc.md) → [`0057a1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057a1bc.md) FUN_0057a1bc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a1d8",
      "incomplete_value": false,
      "site": "0057a1e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a1d8",
      "incomplete_value": false,
      "site": "0057a1e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a1f0",
      "incomplete_value": false,
      "site": "0057a1f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a1f0",
      "incomplete_value": false,
      "site": "0057a1f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:b00:8"
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
      "0057a1e0",
      "DATA",
      [
        "storage",
        "00bf0bc0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057a1f0",
      "DATA",
      [
        "storage",
        "00bf0b00",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057a1e0",
      "DATA",
      [
        "storage",
        "00bf0c10",
        null,
        "undefined *"
      ]
    ],
    [
      "0057a1f0",
      "DATA",
      [
        "storage",
        "00bf0b50",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a1bc.md#insn-0057a1d8) · [`0057a1e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a1bc.md#insn-0057a1e4)
- 新版 `0057a1d8`（命令位置の公開資料なし） · `0057a1e4`（命令位置の公開資料なし）

~~~diff
- 0057a1d8 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 0057a1d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057a1d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057a1d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057a1d8 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 0057a1d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a1d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a1d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057a1d8 bytes 08012f91
+ 0057a1d8 bytes 08413091
- 0057a1e4 ["COPY", "register:4040:8", ["const:bf0000:8"]]
- 0057a1e4 bytes a83300d0
+ 0057a1e4 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 0057a1e4 bytes a83300d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-553fb661e23ac1c95c108ca57c4533f0"></a>

### [`0057a204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a204.md) → [`0057a204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057a204.md) FUN_0057a204

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a240",
      "incomplete_value": false,
      "site": "0057a244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a50:8"
              ]
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
      "definition_site": "0057a240",
      "incomplete_value": false,
      "site": "0057a244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
              ]
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
      "0057a244",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057a244",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a204.md#insn-0057a238)
- 新版 `0057a238`（命令位置の公開資料なし）

~~~diff
- 0057a238 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0057a238 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057a238 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057a238 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057a238 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0057a238 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a238 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a238 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057a238 bytes 08012891
+ 0057a238 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-242a1be95b224e1fe1c742180c930800"></a>

### [`0057a278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a278.md) → [`0057a278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057a278.md) FUN_0057a278

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a2b4",
      "incomplete_value": false,
      "site": "0057a2b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a50:8"
              ]
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
      "definition_site": "0057a2b4",
      "incomplete_value": false,
      "site": "0057a2b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
              ]
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
      "0057a2b8",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057a2b8",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a278.md#insn-0057a2ac)
- 新版 `0057a2ac`（命令位置の公開資料なし）

~~~diff
- 0057a2ac ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0057a2ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057a2ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057a2ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057a2ac ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0057a2ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a2ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a2ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057a2ac bytes 08012891
+ 0057a2ac bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43e8f407a27f01a2421bdf6b4f7d2b2f"></a>

### [`0057a2e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a2e8.md) → [`0057a2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057a2e8.md) FUN_0057a2e8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a310",
      "incomplete_value": false,
      "site": "0057a314",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a310",
      "incomplete_value": false,
      "site": "0057a314",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057a314",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057a314",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a2e8.md#insn-0057a310)
- 新版 `0057a310`（命令位置の公開資料なし）

~~~diff
- 0057a310 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057a310 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057a310 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057a310 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057a310 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057a310 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057a310 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057a310 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057a310 bytes 29c12791
+ 0057a310 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e352147223aa9951abd219c43876fed"></a>

### [`0057a338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a338.md) → [`0057a338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057a338.md) FUN_0057a338

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a360",
      "incomplete_value": false,
      "site": "0057a364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a360",
      "incomplete_value": false,
      "site": "0057a364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057a364",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057a364",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a338.md#insn-0057a360)
- 新版 `0057a360`（命令位置の公開資料なし）

~~~diff
- 0057a360 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057a360 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057a360 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057a360 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057a360 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057a360 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057a360 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057a360 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057a360 bytes 29c12791
+ 0057a360 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec2a92ccb121ea0ab49b636e81aa089c"></a>

### [`0057a384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a384.md) → [`0057a384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057a384.md) FUN_0057a384

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a388",
      "incomplete_value": false,
      "site": "0057a38c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a388",
      "incomplete_value": false,
      "site": "0057a38c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
      "0057a38c",
      "DATA",
      [
        "storage",
        "00bf0b70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057a38c",
      "DATA",
      [
        "storage",
        "00bf0bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a384.md#insn-0057a388)
- 新版 `0057a388`（命令位置の公開資料なし）

~~~diff
- 0057a388 ["COPY", "tmp:0:8", ["const:b70:8"]]
- 0057a388 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057a388 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057a388 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057a388 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 0057a388 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a388 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a388 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057a388 bytes 08c12d91
+ 0057a388 bytes 08012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac53649cc02eec3ce53840c248ebd4c7"></a>

### [`0057a394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a394.md) → [`0057a394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057a394.md) FUN_0057a394

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a3a4",
      "incomplete_value": false,
      "site": "0057a3ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a3a4",
      "incomplete_value": false,
      "site": "0057a3ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
      "0057a3ac",
      "DATA",
      [
        "storage",
        "00bf0b70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057a3ac",
      "DATA",
      [
        "storage",
        "00bf0bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a394.md#insn-0057a3a4)
- 新版 `0057a3a4`（命令位置の公開資料なし）

~~~diff
- 0057a3a4 ["COPY", "tmp:0:8", ["const:b70:8"]]
- 0057a3a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057a3a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057a3a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057a3a4 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 0057a3a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a3a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a3a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057a3a4 bytes 08c12d91
+ 0057a3a4 bytes 08012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-930f3436810385db2c0950eb77fba434"></a>

### [`0057a3c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a3c4.md) → [`0057a3c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057a3c4.md) FUN_0057a3c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a3ec",
      "incomplete_value": false,
      "site": "0057a3f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a3ec",
      "incomplete_value": false,
      "site": "0057a3f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057a3f0",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057a3f0",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a3ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a3c4.md#insn-0057a3ec)
- 新版 `0057a3ec`（命令位置の公開資料なし）

~~~diff
- 0057a3ec ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057a3ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057a3ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057a3ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057a3ec ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057a3ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057a3ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057a3ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057a3ec bytes 29c12791
+ 0057a3ec bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcf908d7a88270e295975516c6821a5d"></a>

### [`0057a418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a418.md) → [`0057a418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057a418.md) FUN_0057a418

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a41c",
      "incomplete_value": false,
      "site": "0057a420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a41c",
      "incomplete_value": false,
      "site": "0057a420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "0057a420",
      "DATA",
      [
        "storage",
        "00bf0bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057a420",
      "DATA",
      [
        "storage",
        "00bf0c10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a418.md#insn-0057a41c)
- 新版 `0057a41c`（命令位置の公開資料なし）

~~~diff
- 0057a41c ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 0057a41c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057a41c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057a41c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057a41c ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 0057a41c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a41c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a41c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057a41c bytes 08012f91
+ 0057a41c bytes 08413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-680f91186a8d0c5cdf478f12437088ae"></a>

### [`0057a428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a428.md) → [`0057a428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057a428.md) FUN_0057a428

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a438",
      "incomplete_value": false,
      "site": "0057a440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a438",
      "incomplete_value": false,
      "site": "0057a440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "0057a440",
      "DATA",
      [
        "storage",
        "00bf0bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057a440",
      "DATA",
      [
        "storage",
        "00bf0c10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a428.md#insn-0057a438)
- 新版 `0057a438`（命令位置の公開資料なし）

~~~diff
- 0057a438 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 0057a438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057a438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057a438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057a438 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 0057a438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057a438 bytes 08012f91
+ 0057a438 bytes 08413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-822e773a3cc97c935fc6f0458bb47b67"></a>

### [`0057a460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a460.md) → [`0057a460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057a460.md) _INIT_38

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a49c",
      "incomplete_value": true,
      "site": "0057a4b8",
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
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a49c",
      "incomplete_value": true,
      "site": "0057a4b8",
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
                "const:2dd:8"
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
      "definition_site": "0057a4c0",
      "incomplete_value": true,
      "site": "0057a4dc",
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
                "const:38a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a4c0",
      "incomplete_value": true,
      "site": "0057a4dc",
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
                "const:2f0:8"
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
      "definition_site": "0057a500",
      "incomplete_value": true,
      "site": "0057a518",
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
                "const:6ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a500",
      "incomplete_value": true,
      "site": "0057a518",
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
                "const:73b:8"
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
      "0057a49c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0057a4c0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0057a4e0",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057a49c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0057a4c0",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0057a4e0",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a460.md#insn-0057a48c) · [`0057a494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a460.md#insn-0057a494)
- 新版 `0057a48c`（命令位置の公開資料なし） · `0057a494`（命令位置の公開資料なし）

~~~diff
- 0057a48c ["COPY", "tmp:0:8", ["const:718:8"]]
- 0057a48c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0057a48c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0057a48c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0057a48c ["COPY", "tmp:0:8", ["const:758:8"]]
+ 0057a48c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0057a48c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0057a48c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0057a48c bytes 73621c91
+ 0057a48c bytes 73621d91
- 0057a494 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0057a494 bytes 69e9ffb0
+ 0057a494 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0057a494 bytes 69e9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ed2533afbe6ad54e88643f2bd24db23"></a>

### [`0057a7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a7f0.md) → [`0057a7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057a7f0.md) FUN_0057a7f0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578fc4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a83c",
      "incomplete_value": true,
      "site": "0057a83c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:674:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a83c",
      "incomplete_value": true,
      "site": "0057a83c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:5da:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a8ec",
      "incomplete_value": false,
      "site": "0057a8f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a8ec",
      "incomplete_value": false,
      "site": "0057a8f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
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
      "definition_site": "0057a910",
      "incomplete_value": false,
      "site": "0057a918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a910",
      "incomplete_value": false,
      "site": "0057a918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "0057a820",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "0057a8f8",
      "DATA",
      [
        "storage",
        "00bf0ce8",
        null,
        "undefined *"
      ]
    ],
    [
      "0057a918",
      "DATA",
      [
        "storage",
        "00bf0c10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057a820",
      "READ",
      [
        "storage",
        "002a6674",
        null,
        "string"
      ]
    ],
    [
      "0057a8f8",
      "DATA",
      [
        "storage",
        "00bf0d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0057a918",
      "DATA",
      [
        "storage",
        "00bf0c60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a7f0.md#insn-0057a814) · [`0057a8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a7f0.md#insn-0057a8ec) · [`0057a910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a7f0.md#insn-0057a910)
- 新版 `0057a814`（命令位置の公開資料なし） · `0057a8ec`（命令位置の公開資料なし） · `0057a910`（命令位置の公開資料なし）

~~~diff
- 0057a814 ["COPY", "tmp:0:8", ["const:5da:8"]]
- 0057a814 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057a814 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057a814 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057a814 ["COPY", "tmp:0:8", ["const:674:8"]]
+ 0057a814 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057a814 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057a814 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057a814 bytes 4a691791
+ 0057a814 bytes 4ad11991
- 0057a8ec ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 0057a8ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057a8ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057a8ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057a8ec ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 0057a8ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a8ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a8ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057a8ec bytes 08a13391
+ 0057a8ec bytes 08e13491
- 0057a910 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 0057a910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057a910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057a910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057a910 ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 0057a910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057a910 bytes 08413091
+ 0057a910 bytes 08813191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab33e68fbc8c29eba993ad9f5eeb0899"></a>

### [`0057a9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a9e0.md) → [`0057a9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057a9e0.md) FUN_0057a9e0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0058ef88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058ef88.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578ff0.md)
- 新版 呼出元 1件 [`0058ef88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058ef88.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a9fc",
      "incomplete_value": false,
      "site": "0057aa00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:c80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a9fc",
      "incomplete_value": false,
      "site": "0057aa00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:c30:8"
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
      "0057aa00",
      "DATA",
      [
        "storage",
        "00bf0c30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057aa00",
      "DATA",
      [
        "storage",
        "00bf0c80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a9e0.md#insn-0057a9fc)
- 新版 `0057a9fc`（命令位置の公開資料なし）

~~~diff
- 0057a9fc ["COPY", "tmp:0:8", ["const:c30:8"]]
- 0057a9fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057a9fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057a9fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057a9fc ["COPY", "tmp:0:8", ["const:c80:8"]]
+ 0057a9fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a9fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a9fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057a9fc bytes 08c13091
+ 0057a9fc bytes 08013291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62893cbbbb31b306ea90ae99ed9735cb"></a>

### [`0057abd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057abd4.md) → [`0057abd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057abd4.md) FUN_0057abd4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057abf0",
      "incomplete_value": false,
      "site": "0057abf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057abf0",
      "incomplete_value": false,
      "site": "0057abf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ac08",
      "incomplete_value": false,
      "site": "0057ac08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ac08",
      "incomplete_value": false,
      "site": "0057ac08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "0057abf8",
      "DATA",
      [
        "storage",
        "00bf0d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0057ac08",
      "DATA",
      [
        "storage",
        "00bf0c88",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057abf8",
      "DATA",
      [
        "storage",
        "00bf0d88",
        null,
        "undefined *"
      ]
    ],
    [
      "0057ac08",
      "DATA",
      [
        "storage",
        "00bf0cd8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057abf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057abd4.md#insn-0057abf0) · [`0057abfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057abd4.md#insn-0057abfc)
- 新版 `0057abf0`（命令位置の公開資料なし） · `0057abfc`（命令位置の公開資料なし）

~~~diff
- 0057abf0 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 0057abf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057abf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057abf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057abf0 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 0057abf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057abf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057abf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057abf0 bytes 08e13491
+ 0057abf0 bytes 08213691
- 0057abfc ["COPY", "register:4040:8", ["const:bf0000:8"]]
- 0057abfc bytes a83300d0
+ 0057abfc ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 0057abfc bytes a83300d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a239b9a9ab3fcb042b9c77825f564f2"></a>

### [`0057ac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ac1c.md) → [`0057ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057ac1c.md) FUN_0057ac1c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ac48",
      "incomplete_value": false,
      "site": "0057ac4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a50:8"
              ]
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
      "definition_site": "0057ac48",
      "incomplete_value": false,
      "site": "0057ac4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
              ]
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
      "0057ac4c",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057ac4c",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ac40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ac1c.md#insn-0057ac40)
- 新版 `0057ac40`（命令位置の公開資料なし）

~~~diff
- 0057ac40 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0057ac40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ac40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ac40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ac40 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0057ac40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ac40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ac40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ac40 bytes 08012891
+ 0057ac40 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c808626907e2720fc081711353a7927"></a>

### [`0057ac80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ac80.md) → [`0057ac80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057ac80.md) FUN_0057ac80

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057acac",
      "incomplete_value": false,
      "site": "0057acb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a50:8"
              ]
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
      "definition_site": "0057acac",
      "incomplete_value": false,
      "site": "0057acb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
              ]
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
      "0057acb0",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057acb0",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057aca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ac80.md#insn-0057aca4)
- 新版 `0057aca4`（命令位置の公開資料なし）

~~~diff
- 0057aca4 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0057aca4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057aca4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057aca4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057aca4 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0057aca4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057aca4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057aca4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057aca4 bytes 08012891
+ 0057aca4 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24d5b754a173fdeb1c73b913cf83d774"></a>

### [`0057ace0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ace0.md) → [`0057ace0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057ace0.md) FUN_0057ace0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ace8",
      "incomplete_value": false,
      "site": "0057acec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ace8",
      "incomplete_value": false,
      "site": "0057acec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057acec",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057acec",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ace8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ace0.md#insn-0057ace8)
- 新版 `0057ace8`（命令位置の公開資料なし）

~~~diff
- 0057ace8 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057ace8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057ace8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057ace8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057ace8 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057ace8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057ace8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057ace8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057ace8 bytes 29c12791
+ 0057ace8 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1defad3f68fa872791adb9cc005c9724"></a>

### [`0057ad20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ad20.md) → [`0057ad20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057ad20.md) FUN_0057ad20

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ad24",
      "incomplete_value": false,
      "site": "0057ad28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ad24",
      "incomplete_value": false,
      "site": "0057ad28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
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
      "0057ad28",
      "DATA",
      [
        "storage",
        "00bf0ce8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057ad28",
      "DATA",
      [
        "storage",
        "00bf0d38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ad24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ad20.md#insn-0057ad24)
- 新版 `0057ad24`（命令位置の公開資料なし）

~~~diff
- 0057ad24 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 0057ad24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ad24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ad24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ad24 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 0057ad24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ad24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ad24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ad24 bytes 08a13391
+ 0057ad24 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc1b0273266d1e0dad92f72906c8b1fb"></a>

### [`0057ad60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ad60.md) → [`0057ad60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057ad60.md) FUN_0057ad60

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ad68",
      "incomplete_value": false,
      "site": "0057ad6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ad68",
      "incomplete_value": false,
      "site": "0057ad6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057ad6c",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057ad6c",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ad68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ad60.md#insn-0057ad68)
- 新版 `0057ad68`（命令位置の公開資料なし）

~~~diff
- 0057ad68 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057ad68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057ad68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057ad68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057ad68 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057ad68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057ad68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057ad68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057ad68 bytes 29c12791
+ 0057ad68 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67f891d0c13a1f2efda1686303ec3349"></a>

### [`0057ad84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ad84.md) → [`0057ad84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057ad84.md) FUN_0057ad84

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ad88",
      "incomplete_value": false,
      "site": "0057ad8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ad88",
      "incomplete_value": false,
      "site": "0057ad8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "0057ad8c",
      "DATA",
      [
        "storage",
        "00bf0d38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057ad8c",
      "DATA",
      [
        "storage",
        "00bf0d88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ad88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ad84.md#insn-0057ad88)
- 新版 `0057ad88`（命令位置の公開資料なし）

~~~diff
- 0057ad88 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 0057ad88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ad88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ad88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ad88 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 0057ad88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ad88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ad88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ad88 bytes 08e13491
+ 0057ad88 bytes 08213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9070209991d3be945b7ebf4b5a899b32"></a>

### [`0057ad94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ad94.md) → [`0057ad94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057ad94.md) FUN_0057ad94

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ada4",
      "incomplete_value": false,
      "site": "0057adac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ada4",
      "incomplete_value": false,
      "site": "0057adac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "0057adac",
      "DATA",
      [
        "storage",
        "00bf0d38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057adac",
      "DATA",
      [
        "storage",
        "00bf0d88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ada4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057ad94.md#insn-0057ada4)
- 新版 `0057ada4`（命令位置の公開資料なし）

~~~diff
- 0057ada4 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 0057ada4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ada4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ada4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ada4 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 0057ada4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ada4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ada4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ada4 bytes 08e13491
+ 0057ada4 bytes 08213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c388dae3fb6d565f2faf5ebb61b0777"></a>

### [`0057adcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057adcc.md) → [`0057adcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057adcc.md) _INIT_39

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ae08",
      "incomplete_value": true,
      "site": "0057ae24",
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
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ae08",
      "incomplete_value": true,
      "site": "0057ae24",
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
                "const:2dd:8"
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
      "definition_site": "0057ae2c",
      "incomplete_value": true,
      "site": "0057ae48",
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
                "const:38a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ae2c",
      "incomplete_value": true,
      "site": "0057ae48",
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
                "const:2f0:8"
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
      "definition_site": "0057ae4c",
      "incomplete_value": true,
      "site": "0057ae68",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ae4c",
      "incomplete_value": true,
      "site": "0057ae68",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:46:8"
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
      "0057ae08",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0057ae2c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0057ae4c",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057ae08",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0057ae2c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0057ae4c",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057adf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057adcc.md#insn-0057adf8) · [`0057ae00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057adcc.md#insn-0057ae00)
- 新版 `0057adf8`（命令位置の公開資料なし） · `0057ae00`（命令位置の公開資料なし）

~~~diff
- 0057adf8 ["COPY", "tmp:0:8", ["const:730:8"]]
- 0057adf8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0057adf8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0057adf8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0057adf8 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 0057adf8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0057adf8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0057adf8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0057adf8 bytes 73c21c91
+ 0057adf8 bytes 73c21d91
- 0057ae00 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0057ae00 bytes 69e9ffb0
+ 0057ae00 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0057ae00 bytes 69e9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cce65912e9188d803a7718e9cb6d84b"></a>

### [`0057b184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b184.md) → [`0057b184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057b184.md) FUN_0057b184

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0057b864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b864.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0057b864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057b864.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.88% / 新版 98.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b1dc",
      "incomplete_value": true,
      "site": "0057b1dc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:674:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b1dc",
      "incomplete_value": true,
      "site": "0057b1dc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:5da:8"
              ]
            ]
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
      "0057b1c0",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057b1c0",
      "READ",
      [
        "storage",
        "002a6674",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b184.md#insn-0057b1b0)
- 新版 `0057b1b0`（命令位置の公開資料なし）

~~~diff
- 0057b1b0 ["COPY", "tmp:0:8", ["const:5da:8"]]
- 0057b1b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057b1b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057b1b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057b1b0 ["COPY", "tmp:0:8", ["const:674:8"]]
+ 0057b1b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057b1b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057b1b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057b1b0 bytes 4a691791
+ 0057b1b0 bytes 4ad11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e5395d16fe6c5ed1cbcfd08011678b3"></a>

### [`0057b6a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b6a4.md) → [`0057b6a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057b6a4.md) FUN_0057b6a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b6c0",
      "incomplete_value": false,
      "site": "0057b6c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b6c0",
      "incomplete_value": false,
      "site": "0057b6c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b6d8",
      "incomplete_value": false,
      "site": "0057b6d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b6d8",
      "incomplete_value": false,
      "site": "0057b6d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:da8:8"
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
      "0057b6c8",
      "DATA",
      [
        "storage",
        "00bf0eb0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057b6d8",
      "DATA",
      [
        "storage",
        "00bf0da8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057b6c8",
      "DATA",
      [
        "storage",
        "00bf0f00",
        null,
        "undefined *"
      ]
    ],
    [
      "0057b6d8",
      "DATA",
      [
        "storage",
        "00bf0df8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b6c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b6a4.md#insn-0057b6c0) · [`0057b6cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b6a4.md#insn-0057b6cc)
- 新版 `0057b6c0`（命令位置の公開資料なし） · `0057b6cc`（命令位置の公開資料なし）

~~~diff
- 0057b6c0 ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 0057b6c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b6c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b6c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b6c0 ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 0057b6c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b6c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b6c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b6c0 bytes 08c13a91
+ 0057b6c0 bytes 08013c91
- 0057b6cc ["COPY", "register:4040:8", ["const:bf0000:8"]]
- 0057b6cc bytes a83300b0
+ 0057b6cc ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 0057b6cc bytes a83300b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3214b3053f1f89ebec4f67ba36704e70"></a>

### [`0057b6ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b6ec.md) → [`0057b6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057b6ec.md) FUN_0057b6ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0057b708",
      "incomplete_value": true,
      "site": "0057b70c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0057b708",
      "incomplete_value": true,
      "site": "0057b70c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0057b700",
      "READ",
      [
        "storage",
        "00c1b4e0",
        null,
        "pointer"
      ]
    ],
    [
      "0057b70c",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057b700",
      "READ",
      [
        "storage",
        "00c1b530",
        null,
        "pointer"
      ]
    ],
    [
      "0057b70c",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b6ec.md#insn-0057b700)
- 新版 `0057b700`（命令位置の公開資料なし）

~~~diff
- 0057b700 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e0:8"]]
- 0057b700 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0057b700 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:530:8"]]
+ 0057b700 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0057b700 bytes 087142f9
+ 0057b700 bytes 089942f9
~~~


<a id="compare-006a19d146878f1f24316002cfd654e5"></a>

### [`0057b73c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b73c.md) → [`0057b73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057b73c.md) FUN_0057b73c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b7a4",
      "incomplete_value": false,
      "site": "0057b7a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b7a4",
      "incomplete_value": false,
      "site": "0057b7a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057b7a8",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057b7a8",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b7a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b73c.md#insn-0057b7a4)
- 新版 `0057b7a4`（命令位置の公開資料なし）

~~~diff
- 0057b7a4 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057b7a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057b7a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057b7a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057b7a4 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057b7a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b7a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b7a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057b7a4 bytes 29c12791
+ 0057b7a4 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a277fd2e0d090f776f8345b82d60432"></a>

### [`0057b7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b7d4.md) → [`0057b7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057b7d4.md) FUN_0057b7d4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b83c",
      "incomplete_value": false,
      "site": "0057b840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b83c",
      "incomplete_value": false,
      "site": "0057b840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057b840",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057b840",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b7d4.md#insn-0057b83c)
- 新版 `0057b83c`（命令位置の公開資料なし）

~~~diff
- 0057b83c ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057b83c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057b83c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057b83c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057b83c ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057b83c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b83c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b83c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057b83c bytes 29c12791
+ 0057b83c bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d894de61d3a91ed87622f2717cebeba4"></a>

### [`0057b864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b864.md) → [`0057b864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057b864.md) FUN_0057b864

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0057b184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b184.md) · 呼出先 4件 [`0051d884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d884.md) [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0057b184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057b184.md) · 呼出先 4件 [`0051d884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d884.md) [`00578fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578fc4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.73% / 新版 92.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b8d0",
      "incomplete_value": false,
      "site": "0057b8d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b8d0",
      "incomplete_value": false,
      "site": "0057b8d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:e60:8"
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
      "definition_site": "0057b8f8",
      "incomplete_value": true,
      "site": "0057b900",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b8f8",
      "incomplete_value": true,
      "site": "0057b900",
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
            "const:d88:8"
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
      "0057b8d4",
      "DATA",
      [
        "storage",
        "00bf0e60",
        null,
        "undefined *"
      ]
    ],
    [
      "0057b900",
      "DATA",
      [
        "storage",
        "00bf0d88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057b8d4",
      "DATA",
      [
        "storage",
        "00bf0eb0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057b900",
      "DATA",
      [
        "storage",
        "00bf0dd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b864.md#insn-0057b8d0) · [`0057b8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b864.md#insn-0057b8f8)
- 新版 `0057b8d0`（命令位置の公開資料なし） · `0057b8f8`（命令位置の公開資料なし）

~~~diff
- 0057b8d0 ["COPY", "tmp:0:8", ["const:e60:8"]]
- 0057b8d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b8d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b8d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b8d0 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 0057b8d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b8d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b8d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b8d0 bytes 08813991
+ 0057b8d0 bytes 08c13a91
- 0057b8f8 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 0057b8f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b8f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b8f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b8f8 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 0057b8f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b8f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b8f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b8f8 bytes 08213691
+ 0057b8f8 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74999c64e8ab5de55ab7b373aeb11601"></a>

### [`0057b97c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b97c.md) → [`0057b97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057b97c.md) FUN_0057b97c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b980",
      "incomplete_value": false,
      "site": "0057b984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b980",
      "incomplete_value": false,
      "site": "0057b984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:e60:8"
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
      "0057b984",
      "DATA",
      [
        "storage",
        "00bf0e60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057b984",
      "DATA",
      [
        "storage",
        "00bf0eb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b97c.md#insn-0057b980)
- 新版 `0057b980`（命令位置の公開資料なし）

~~~diff
- 0057b980 ["COPY", "tmp:0:8", ["const:e60:8"]]
- 0057b980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b980 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 0057b980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b980 bytes 08813991
+ 0057b980 bytes 08c13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d223bda2d68265cf3d0f41568cc7321"></a>

### [`0057b98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b98c.md) → [`0057b98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057b98c.md) FUN_0057b98c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b99c",
      "incomplete_value": false,
      "site": "0057b9a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b99c",
      "incomplete_value": false,
      "site": "0057b9a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:e60:8"
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
      "0057b9a4",
      "DATA",
      [
        "storage",
        "00bf0e60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057b9a4",
      "DATA",
      [
        "storage",
        "00bf0eb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b99c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b98c.md#insn-0057b99c)
- 新版 `0057b99c`（命令位置の公開資料なし）

~~~diff
- 0057b99c ["COPY", "tmp:0:8", ["const:e60:8"]]
- 0057b99c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b99c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b99c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b99c ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 0057b99c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b99c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b99c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b99c bytes 08813991
+ 0057b99c bytes 08c13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6de11b0bafb82a6f8c83119db0a9d115"></a>

### [`0057b9bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b9bc.md) → [`0057b9bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057b9bc.md) FUN_0057b9bc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ba24",
      "incomplete_value": false,
      "site": "0057ba28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ba24",
      "incomplete_value": false,
      "site": "0057ba28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057ba28",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057ba28",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ba24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057b9bc.md#insn-0057ba24)
- 新版 `0057ba24`（命令位置の公開資料なし）

~~~diff
- 0057ba24 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057ba24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057ba24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057ba24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057ba24 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057ba24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057ba24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057ba24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057ba24 bytes 29c12791
+ 0057ba24 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

