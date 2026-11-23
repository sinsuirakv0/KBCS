# v15.7.3 → v15.7.4 · 最優先の変更候補 (32)

[一覧の目次](README.md)

<a id="compare-86f8d477fc76bdce104df5ebd005650a"></a>

### [`0070f0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070f/0070f0b0.md) → [`0070f0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070f/0070f0b0.md) FUN_0070f0b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00748560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00748/00748560.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 7件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`007112e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00711/007112e8.md) [`00711360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00711/00711360.md) [`007113f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00711/007113f4.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md)
- 新版 呼出元 2件 [`00748560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00748/00748560.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 7件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`007112e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00711/007112e8.md) [`00711360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00711/00711360.md) [`007113f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00711/007113f4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)

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
      "definition_site": "0070f1b0",
      "incomplete_value": false,
      "site": "0070f1b4",
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
            "const:65a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070f1b0",
      "incomplete_value": false,
      "site": "0070f1b4",
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
            "const:5cf:8"
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
      "0070f1b0",
      "PARAM",
      [
        "storage",
        "002a35cf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0070f1b0",
      "PARAM",
      [
        "storage",
        "002a365a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070f1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070f/0070f0b0.md#insn-0070f1b0)
- 新版 `0070f1b0`（命令位置の公開資料なし）

~~~diff
- 0070f1b0 ["COPY", "tmp:0:8", ["const:5cf:8"]]
- 0070f1b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0070f1b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0070f1b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0070f1b0 ["COPY", "tmp:0:8", ["const:65a:8"]]
+ 0070f1b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0070f1b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0070f1b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0070f1b0 bytes 003c1791
+ 0070f1b0 bytes 00681991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b133136b0740586e142ddb8002d8810"></a>

### [`0070f204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070f/0070f204.md) → [`0070f204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070f/0070f204.md) FUN_0070f204

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00748560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00748/00748560.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0070f230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070f/0070f230.md)
- 新版 呼出元 2件 [`00748560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00748/00748560.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0070f230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070f/0070f230.md)

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
      "definition_site": "0070f228",
      "incomplete_value": false,
      "site": "0070f22c",
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
            "const:65a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070f228",
      "incomplete_value": false,
      "site": "0070f22c",
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
            "const:5cf:8"
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
      "0070f228",
      "PARAM",
      [
        "storage",
        "002a35cf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0070f228",
      "PARAM",
      [
        "storage",
        "002a365a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070f228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070f/0070f204.md#insn-0070f228)
- 新版 `0070f228`（命令位置の公開資料なし）

~~~diff
- 0070f228 ["COPY", "tmp:0:8", ["const:5cf:8"]]
- 0070f228 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0070f228 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0070f228 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0070f228 ["COPY", "tmp:0:8", ["const:65a:8"]]
+ 0070f228 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0070f228 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0070f228 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0070f228 bytes 003c1791
+ 0070f228 bytes 00681991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-116fa6b9e3884796dc01434ff8bcdcc3"></a>

### [`00710214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00710/00710214.md) → [`00710214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710214.md) FUN_00710214

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0070a03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070a/0070a03c.md) [`00710214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00710/00710214.md) [`0087acb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087acb4.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`0070a03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070a/0070a03c.md) [`00710214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710214.md) [`0087acb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087acb4.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.85% / 新版 98.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00710370",
      "incomplete_value": false,
      "site": "00710378",
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
            "const:3a4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00710370",
      "incomplete_value": false,
      "site": "00710378",
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
            "const:30a:8"
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
      "definition_site": "0071042c",
      "incomplete_value": false,
      "site": "00710434",
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
            "const:379:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071042c",
      "incomplete_value": false,
      "site": "00710434",
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
            "const:2ee:8"
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
      "definition_site": "00710540",
      "incomplete_value": true,
      "site": "0071054c",
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
            "const:885:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00710540",
      "incomplete_value": true,
      "site": "0071054c",
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
            "const:919:8"
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
      "00710370",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0071042c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00710444",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00710370",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0071042c",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "00710444",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00710370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00710/00710214.md#insn-00710370) · [`0071042c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00710/00710214.md#insn-0071042c) · [`00710444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00710/00710214.md#insn-00710444)
- 新版 `00710370`（命令位置の公開資料なし） · `0071042c`（命令位置の公開資料なし） · `00710444`（命令位置の公開資料なし）

~~~diff
- 00710370 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00710370 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00710370 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00710370 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00710370 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00710370 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00710370 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00710370 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00710370 bytes 21280c91
+ 00710370 bytes 21900e91
- 0071042c ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0071042c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0071042c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0071042c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0071042c ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0071042c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0071042c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0071042c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0071042c bytes 21b80b91
+ 0071042c bytes 21e40d91
- 00710444 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00710444 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00710444 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00710444 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00710444 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00710444 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00710444 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00710444 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00710444 bytes 21642491
+ 00710444 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe5d5a56699131399825116bcce477eb"></a>

### [`00710de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00710/00710de0.md) → [`00710de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710de0.md) FUN_00710de0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0070afb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070a/0070afb4.md) [`0070db34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070d/0070db34.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`0070afb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070a/0070afb4.md) [`0070db34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070d/0070db34.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00710dec",
      "incomplete_value": false,
      "site": "00710df0",
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
      "definition_site": "00710dec",
      "incomplete_value": false,
      "site": "00710df0",
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
      "00710dec",
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
      "00710dec",
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

- 旧版 [`00710dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00710/00710de0.md#insn-00710dec)
- 新版 `00710dec`（命令位置の公開資料なし）

~~~diff
- 00710dec ["COPY", "tmp:0:8", ["const:303:8"]]
- 00710dec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00710dec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00710dec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00710dec ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00710dec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00710dec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00710dec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00710dec bytes 000c0c91
+ 00710dec bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b5d49b56010ba233c96eb7d53ecdf8c"></a>

### [`00710df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00710/00710df4.md) → [`00710df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710df4.md) FUN_00710df4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 9件 [`0070a288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070a/0070a288.md) [`0070b824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070b/0070b824.md) [`0070bb9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070b/0070bb9c.md) [`0070bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070b/0070bedc.md) [`0070d20c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070d/0070d20c.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 9件 [`0070a288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070a/0070a288.md) [`0070b824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070b/0070b824.md) [`0070bb9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070b/0070bb9c.md) [`0070bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070b/0070bedc.md) [`0070d20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070d/0070d20c.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "00710e00",
      "incomplete_value": false,
      "site": "00710e04",
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
      "definition_site": "00710e00",
      "incomplete_value": false,
      "site": "00710e04",
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
      "00710e00",
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
      "00710e00",
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

- 旧版 [`00710e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00710/00710df4.md#insn-00710e00)
- 新版 `00710e00`（命令位置の公開資料なし）

~~~diff
- 00710e00 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00710e00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00710e00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00710e00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00710e00 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00710e00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00710e00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00710e00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00710e00 bytes 000c0c91
+ 00710e00 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9887aef6c63dcc30cc275d1d68f95a8d"></a>

### [`00710e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00710/00710e08.md) → [`00710e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710e08.md) FUN_00710e08

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0070b604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070b/0070b604.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0070b604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070b/0070b604.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00710e14",
      "incomplete_value": false,
      "site": "00710e18",
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
      "definition_site": "00710e14",
      "incomplete_value": false,
      "site": "00710e18",
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
      "00710e14",
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
      "00710e14",
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

- 旧版 [`00710e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00710/00710e08.md#insn-00710e14)
- 新版 `00710e14`（命令位置の公開資料なし）

~~~diff
- 00710e14 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00710e14 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00710e14 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00710e14 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00710e14 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00710e14 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00710e14 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00710e14 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00710e14 bytes 000c0c91
+ 00710e14 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53285e7c9fcb703d9fb78dca57f2de6c"></a>

### [`007112e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00711/007112e8.md) → [`007112e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00711/007112e8.md) FUN_007112e8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0070f0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070f/0070f0b0.md) [`00710ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00710/00710ef4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`0070f0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070f/0070f0b0.md) [`00710ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710ef4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "007112f4",
      "incomplete_value": false,
      "site": "007112f8",
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
      "definition_site": "007112f4",
      "incomplete_value": false,
      "site": "007112f8",
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
      "007112f4",
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
      "007112f4",
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

- 旧版 [`007112f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00711/007112e8.md#insn-007112f4)
- 新版 `007112f4`（命令位置の公開資料なし）

~~~diff
- 007112f4 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007112f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007112f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007112f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007112f4 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007112f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007112f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007112f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007112f4 bytes 000c0c91
+ 007112f4 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a3a22ff04aa4c39a8f57151cdbdef0e"></a>

### [`0071152c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00711/0071152c.md) → [`0071152c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00711/0071152c.md) _INIT_124

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00711568",
      "incomplete_value": true,
      "site": "00711584",
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
      "definition_site": "00711568",
      "incomplete_value": true,
      "site": "00711584",
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
      "definition_site": "0071158c",
      "incomplete_value": true,
      "site": "007115a8",
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
      "definition_site": "0071158c",
      "incomplete_value": true,
      "site": "007115a8",
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
      "definition_site": "007115ac",
      "incomplete_value": true,
      "site": "007115c8",
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
      "definition_site": "007115ac",
      "incomplete_value": true,
      "site": "007115c8",
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
      "00711568",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0071158c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "007115ac",
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
      "00711568",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0071158c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "007115ac",
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

- 旧版 [`00711558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00711/0071152c.md#insn-00711558) · [`00711560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00711/0071152c.md#insn-00711560)
- 新版 `00711558`（命令位置の公開資料なし） · `00711560`（命令位置の公開資料なし）

~~~diff
- 00711558 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 00711558 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00711558 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00711558 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00711558 ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 00711558 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00711558 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00711558 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00711558 bytes 73823891
+ 00711558 bytes 73823991
- 00711560 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00711560 bytes a9dcffd0
+ 00711560 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00711560 bytes a9dcffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f5bf2cc0c84629e3ddd6a5650f3fb91"></a>

### [`007118bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00711/007118bc.md) → [`007118bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00711/007118bc.md) FUN_007118bc

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007127f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00712/007127f8.md) · 呼出先 12件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d83c.md) [`00657e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00657/00657e7c.md) [`00831724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00831/00831724.md) [`00832580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00832/00832580.md)
- 新版 呼出元 1件 [`007127f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00712/007127f8.md) · 呼出先 12件 [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d83c.md) [`00657e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/00657e7c.md) [`00831724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00831/00831724.md) [`00832580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00832/00832580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.79% / 新版 88.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 29件, `store_destination` 7件, `store_value` 18件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007118f8",
      "incomplete_value": false,
      "site": "007118fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007118f8",
      "incomplete_value": false,
      "site": "007118fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "definition_site": "00711948",
      "incomplete_value": true,
      "site": "00711948",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00711948",
      "incomplete_value": true,
      "site": "00711948",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:895:8"
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
      "definition_site": "00711960",
      "incomplete_value": true,
      "site": "00711960",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:88a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00711960",
      "incomplete_value": true,
      "site": "00711960",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7ff:8"
              ]
            ]
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
      "007118fc",
      "DATA",
      [
        "storage",
        "00bfa500",
        null,
        "pointer"
      ]
    ],
    [
      "00711918",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00711938",
      "READ",
      [
        "storage",
        "002a5895",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007118fc",
      "DATA",
      [
        "storage",
        "00bfa550",
        null,
        "pointer"
      ]
    ],
    [
      "00711918",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00711938",
      "READ",
      [
        "storage",
        "002a5920",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007118f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00711/007118bc.md#insn-007118f8) · [`00711900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00711/007118bc.md#insn-00711900)
- 新版 `007118f8`（命令位置の公開資料なし） · `00711900`（命令位置の公開資料なし）

~~~diff
- 007118f8 ["COPY", "tmp:0:8", ["const:500:8"]]
- 007118f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007118f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007118f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007118f8 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 007118f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007118f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007118f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007118f8 bytes 08011491
+ 007118f8 bytes 08411591
- 00711900 ["COPY", "register:40c0:8", ["const:c25000:8"]]
- 00711900 bytes b8280090
+ 00711900 ["COPY", "register:40c0:8", ["const:c25000:8"]]
+ 00711900 bytes b8280090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a9b08d1cca3299ad2a60069a18ab4fb"></a>

### [`007127f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00712/007127f8.md) → [`007127f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00712/007127f8.md) FUN_007127f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0071748c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/0071748c.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 47件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md)
- 新版 呼出元 2件 [`0071748c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/0071748c.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 47件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.48% / 新版 97.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 3件, `store_destination` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00712848",
      "incomplete_value": false,
      "site": "00712848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00712848",
      "incomplete_value": false,
      "site": "00712848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00712840",
      "incomplete_value": true,
      "site": "00712848",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
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
      "definition_site": "00712840",
      "incomplete_value": true,
      "site": "00712848",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:a78:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0071284c",
      "incomplete_value": false,
      "site": "0071284c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071284c",
      "incomplete_value": false,
      "site": "0071284c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00712840",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00712844",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00712848",
      "WRITE",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00712840",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00712844",
      "READ",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00712848",
      "WRITE",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00712848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00712/007127f8.md#insn-00712848) · [`0071284c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00712/007127f8.md#insn-0071284c) · [`00712868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00712/007127f8.md#insn-00712868)
- 新版 `00712848`（命令位置の公開資料なし） · `0071284c`（命令位置の公開資料なし） · `00712868`（命令位置の公開資料なし）

~~~diff
- 00712848 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 00712848 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00712848 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa8:8"]]
+ 00712848 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00712848 bytes 093505f9
+ 00712848 bytes 095505f9
- 0071284c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
- 0071284c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 0071284c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ab8:8"]]
+ 0071284c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 0071284c bytes ca3e05f9
+ 0071284c bytes ca5e05f9
- 00712868 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
- 00712868 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 00712868 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ab8:8"]]
+ 00712868 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00712868 bytes d43e05f9
+ 00712868 bytes d45e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da9248301a02c618b502cdfe971cd8d2"></a>

### [`00713660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00713/00713660.md) → [`00713660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00713/00713660.md) FUN_00713660

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 46件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 46件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 95.20% / 新版 95.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `store_destination` 21件, `store_value` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00713b10",
      "incomplete_value": false,
      "site": "00713b10",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00713b10",
      "incomplete_value": false,
      "site": "00713b10",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00713b14",
      "incomplete_value": false,
      "site": "00713b14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00713b14",
      "incomplete_value": false,
      "site": "00713b14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00713b10",
      "incomplete_value": false,
      "site": "00713b14",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00713b10",
      "incomplete_value": false,
      "site": "00713b14",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007136a0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007136b4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007136bc",
      "PARAM",
      [
        "storage",
        "00bfa510",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007136a0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007136b4",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007136bc",
      "PARAM",
      [
        "storage",
        "00bfa560",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007136a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00713/00713660.md#insn-007136a0) · [`007136b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00713/00713660.md#insn-007136b4) · [`007136bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00713/00713660.md#insn-007136bc)
- 新版 `007136a0`（命令位置の公開資料なし） · `007136b4`（命令位置の公開資料なし） · `007136bc`（命令位置の公開資料なし）

~~~diff
- 007136a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007136a0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007136a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007136a0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007136a0 bytes 003d45f9
+ 007136a0 bytes 005d45f9
- 007136b4 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007136b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007136b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007136b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007136b4 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007136b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007136b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007136b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007136b4 bytes 21203991
+ 007136b4 bytes 21603a91
- 007136bc ["COPY", "tmp:0:8", ["const:510:8"]]
- 007136bc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007136bc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007136bc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007136bc ["COPY", "tmp:0:8", ["const:560:8"]]
+ 007136bc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007136bc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007136bc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007136bc bytes 42401491
+ 007136bc bytes 42801591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59a01c9750e5d3c3cfc5ce82639c474d"></a>

### [`00714cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00714/00714cf0.md) → [`00714cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00714/00714cf0.md) FUN_00714cf0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 41件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00445044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445044.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 41件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00445044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445044.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.31% / 新版 97.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 10件, `store_destination` 14件, `store_value` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00716c68",
      "incomplete_value": false,
      "site": "00716c68",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00716c68",
      "incomplete_value": false,
      "site": "00716c68",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 91,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00716c6c",
      "incomplete_value": false,
      "site": "00716c6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00716c6c",
      "incomplete_value": false,
      "site": "00716c6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 92,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00716c68",
      "incomplete_value": false,
      "site": "00716c6c",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00716c68",
      "incomplete_value": false,
      "site": "00716c6c",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 92,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00714d3c",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00714d48",
      "READ",
      [
        "storage",
        "00c25030",
        null,
        "undefined8"
      ]
    ],
    [
      "00714d58",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00714d3c",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00714d48",
      "READ",
      [
        "storage",
        "00c25070",
        null,
        "undefined8"
      ]
    ],
    [
      "00714d58",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00714d28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00714/00714cf0.md#insn-00714d28) · [`00714d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00714/00714cf0.md#insn-00714d48) · [`00714d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00714/00714cf0.md#insn-00714d58)
- 新版 `00714d28`（命令位置の公開資料なし） · `00714d48`（命令位置の公開資料なし） · `00714d58`（命令位置の公開資料なし）

~~~diff
- 00714d28 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00714d28 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00714d28 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00714d28 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00714d28 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00714d28 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00714d28 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00714d28 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00714d28 bytes 94e20091
+ 00714d28 bytes 94e20191
- 00714d48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:30:8"]]
- 00714d48 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00714d48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:70:8"]]
+ 00714d48 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00714d48 bytes 601a40f9
+ 00714d48 bytes 603a40f9
- 00714d58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00714d58 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00714d58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00714d58 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00714d58 bytes 003d45f9
+ 00714d58 bytes 005d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ec1cdb8afbbf86e0d51201d3f20971a"></a>

### [`00716d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00716/00716d24.md) → [`00716d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00716/00716d24.md) FUN_00716d24

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00716ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00716/00716ebc.md) · 呼出先 4件 [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00716ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00716/00716ebc.md) · 呼出先 4件 [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00716d40",
      "incomplete_value": false,
      "site": "00716d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00716d40",
      "incomplete_value": false,
      "site": "00716d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "definition_site": "00716e74",
      "incomplete_value": false,
      "site": "00716e78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00716e74",
      "incomplete_value": false,
      "site": "00716e78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "00716d44",
      "DATA",
      [
        "storage",
        "00bfa500",
        null,
        "pointer"
      ]
    ],
    [
      "00716e78",
      "DATA",
      [
        "storage",
        "00bf7298",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00716d44",
      "DATA",
      [
        "storage",
        "00bfa550",
        null,
        "pointer"
      ]
    ],
    [
      "00716e78",
      "DATA",
      [
        "storage",
        "00bf72e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00716d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00716/00716d24.md#insn-00716d40) · [`00716e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00716/00716d24.md#insn-00716e74)
- 新版 `00716d40`（命令位置の公開資料なし） · `00716e74`（命令位置の公開資料なし）

~~~diff
- 00716d40 ["COPY", "tmp:0:8", ["const:500:8"]]
- 00716d40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00716d40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00716d40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00716d40 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00716d40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00716d40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00716d40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00716d40 bytes 08011491
+ 00716d40 bytes 08411591
- 00716e74 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00716e74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00716e74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00716e74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00716e74 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 00716e74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00716e74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00716e74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00716e74 bytes 08610a91
+ 00716e74 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-581df4800cc2d9c2b4e32cb292b6001a"></a>

### [`007170a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/007170a0.md) → [`007170a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/007170a0.md) FUN_007170a0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "007170c4",
      "incomplete_value": false,
      "site": "007170c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007170c4",
      "incomplete_value": false,
      "site": "007170c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:538:8"
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
      "007170c4",
      "DATA",
      [
        "storage",
        "00bfa538",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007170c4",
      "DATA",
      [
        "storage",
        "00bfa588",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007170c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/007170a0.md#insn-007170c0)
- 新版 `007170c0`（命令位置の公開資料なし）

~~~diff
- 007170c0 ["COPY", "tmp:0:8", ["const:538:8"]]
- 007170c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007170c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007170c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007170c0 ["COPY", "tmp:0:8", ["const:588:8"]]
+ 007170c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007170c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007170c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007170c0 bytes 08e11491
+ 007170c0 bytes 08211691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-715542c62329c7e3d7e79592677e0c2f"></a>

### [`007170d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/007170d4.md) → [`007170d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/007170d4.md) FUN_007170d4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007170e0",
      "incomplete_value": false,
      "site": "007170e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007170e0",
      "incomplete_value": false,
      "site": "007170e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:538:8"
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
      "007170e0",
      "DATA",
      [
        "storage",
        "00bfa538",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007170e0",
      "DATA",
      [
        "storage",
        "00bfa588",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007170dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/007170d4.md#insn-007170dc)
- 新版 `007170dc`（命令位置の公開資料なし）

~~~diff
- 007170dc ["COPY", "tmp:0:8", ["const:538:8"]]
- 007170dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007170dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007170dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007170dc ["COPY", "tmp:0:8", ["const:588:8"]]
+ 007170dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007170dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007170dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007170dc bytes 29e11491
+ 007170dc bytes 29211691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce3843061549865c4261ffc49eb09e84"></a>

### [`00717278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/00717278.md) → [`00717278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/00717278.md) FUN_00717278

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0071729c",
      "incomplete_value": false,
      "site": "0071729c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071729c",
      "incomplete_value": false,
      "site": "0071729c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
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
      "0071729c",
      "DATA",
      [
        "storage",
        "00bfa5b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071729c",
      "DATA",
      [
        "storage",
        "00bfa608",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00717298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/00717278.md#insn-00717298)
- 新版 `00717298`（命令位置の公開資料なし）

~~~diff
- 00717298 ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 00717298 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00717298 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00717298 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00717298 ["COPY", "tmp:0:8", ["const:608:8"]]
+ 00717298 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00717298 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00717298 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00717298 bytes 08e11691
+ 00717298 bytes 08211891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-073fb28f331838dc03c218b8e2bce9d6"></a>

### [`007172ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/007172ac.md) → [`007172ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/007172ac.md) FUN_007172ac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007172b8",
      "incomplete_value": false,
      "site": "007172b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007172b8",
      "incomplete_value": false,
      "site": "007172b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
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
      "007172b8",
      "DATA",
      [
        "storage",
        "00bfa5b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007172b8",
      "DATA",
      [
        "storage",
        "00bfa608",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007172b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/007172ac.md#insn-007172b4)
- 新版 `007172b4`（命令位置の公開資料なし）

~~~diff
- 007172b4 ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 007172b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007172b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007172b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007172b4 ["COPY", "tmp:0:8", ["const:608:8"]]
+ 007172b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007172b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007172b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007172b4 bytes 29e11691
+ 007172b4 bytes 29211891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa2fd91f220b8b852779f6e689113475"></a>

### [`007172c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/007172c8.md) → [`007172c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/007172c8.md) FUN_007172c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459bb4.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00717484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/00717484.md) [`00717488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/00717488.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459bb4.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00717484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/00717484.md) [`00717488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/00717488.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.83% / 新版 96.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0071735c",
      "incomplete_value": false,
      "site": "0071735c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071735c",
      "incomplete_value": false,
      "site": "0071735c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:628:8"
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
      "0071735c",
      "DATA",
      [
        "storage",
        "00bfa628",
        null,
        "undefined *"
      ]
    ],
    [
      "00717398",
      "READ",
      [
        "storage",
        "00bfa648",
        null,
        "pointer"
      ]
    ],
    [
      "00717398",
      "READ",
      [
        "storage",
        "00bfa650",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071735c",
      "DATA",
      [
        "storage",
        "00bfa678",
        null,
        "undefined *"
      ]
    ],
    [
      "00717398",
      "READ",
      [
        "storage",
        "00bfa698",
        null,
        "pointer"
      ]
    ],
    [
      "00717398",
      "READ",
      [
        "storage",
        "00bfa6a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00717354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/007172c8.md#insn-00717354)
- 新版 `00717354`（命令位置の公開資料なし）

~~~diff
- 00717354 ["COPY", "tmp:0:8", ["const:628:8"]]
- 00717354 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00717354 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00717354 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00717354 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 00717354 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00717354 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00717354 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00717354 bytes 08a11891
+ 00717354 bytes 08e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11b5c7316784c2588b79ab721483f126"></a>

### [`0071743c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/0071743c.md) → [`0071743c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/0071743c.md) FUN_0071743c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00717460",
      "incomplete_value": false,
      "site": "00717460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00717460",
      "incomplete_value": false,
      "site": "00717460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:628:8"
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
      "00717460",
      "DATA",
      [
        "storage",
        "00bfa628",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00717460",
      "DATA",
      [
        "storage",
        "00bfa678",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071745c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/0071743c.md#insn-0071745c)
- 新版 `0071745c`（命令位置の公開資料なし）

~~~diff
- 0071745c ["COPY", "tmp:0:8", ["const:628:8"]]
- 0071745c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071745c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071745c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071745c ["COPY", "tmp:0:8", ["const:678:8"]]
+ 0071745c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071745c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071745c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071745c bytes 08a11891
+ 0071745c bytes 08e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdef79f6f3edb694ffcb7baec2e3c47c"></a>

### [`00717470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/00717470.md) → [`00717470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/00717470.md) FUN_00717470

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0071747c",
      "incomplete_value": false,
      "site": "0071747c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071747c",
      "incomplete_value": false,
      "site": "0071747c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:628:8"
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
      "0071747c",
      "DATA",
      [
        "storage",
        "00bfa628",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071747c",
      "DATA",
      [
        "storage",
        "00bfa678",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00717478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/00717470.md#insn-00717478)
- 新版 `00717478`（命令位置の公開資料なし）

~~~diff
- 00717478 ["COPY", "tmp:0:8", ["const:628:8"]]
- 00717478 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00717478 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00717478 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00717478 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 00717478 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00717478 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00717478 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00717478 bytes 29a11891
+ 00717478 bytes 29e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-793d58222e813bd95fcf4e3955570ad8"></a>

### [`0071748c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/0071748c.md) → [`0071748c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/0071748c.md) FUN_0071748c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 24件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 24件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.31% / 新版 97.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007176b4",
      "incomplete_value": false,
      "site": "007176b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007176b4",
      "incomplete_value": false,
      "site": "007176b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00717744",
      "incomplete_value": false,
      "site": "00717744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00717744",
      "incomplete_value": false,
      "site": "00717744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007176b4",
      "DATA",
      [
        "storage",
        "00bfa698",
        null,
        "undefined *"
      ]
    ],
    [
      "00717710",
      "READ",
      [
        "storage",
        "002a8394",
        null,
        "string"
      ]
    ],
    [
      "00717744",
      "DATA",
      [
        "storage",
        "00bfa718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007176b4",
      "DATA",
      [
        "storage",
        "00bfa6e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00717710",
      "READ",
      [
        "storage",
        "002a842e",
        null,
        "string"
      ]
    ],
    [
      "00717744",
      "DATA",
      [
        "storage",
        "00bfa768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007176ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/0071748c.md#insn-007176ac) · [`007176b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/0071748c.md#insn-007176b0)
- 新版 `007176ac`（命令位置の公開資料なし） · `007176b0`（命令位置の公開資料なし）

~~~diff
- 007176ac ["COPY", "tmp:0:8", ["const:698:8"]]
- 007176ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007176ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007176ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007176ac ["COPY", "tmp:0:8", ["const:6e8:8"]]
+ 007176ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007176ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007176ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007176ac bytes 08611a91
+ 007176ac bytes 08a11b91
- 007176b0 ["INT_SUB", "register:40a0:8", ["register:40e8:8", "const:70:8"]]
- 007176b0 bytes b4c301d1
+ 007176b0 ["INT_SUB", "register:40a0:8", ["register:40e8:8", "const:70:8"]]
+ 007176b0 bytes b4c301d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6aa601739270a195be64d332fd9b6de"></a>

### [`00717a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/00717a24.md) → [`00717a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/00717a24.md) FUN_00717a24

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00717a48",
      "incomplete_value": false,
      "site": "00717a48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00717a48",
      "incomplete_value": false,
      "site": "00717a48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "00717a48",
      "DATA",
      [
        "storage",
        "00bfa698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00717a48",
      "DATA",
      [
        "storage",
        "00bfa6e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00717a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/00717a24.md#insn-00717a44)
- 新版 `00717a44`（命令位置の公開資料なし）

~~~diff
- 00717a44 ["COPY", "tmp:0:8", ["const:698:8"]]
- 00717a44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00717a44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00717a44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00717a44 ["COPY", "tmp:0:8", ["const:6e8:8"]]
+ 00717a44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00717a44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00717a44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00717a44 bytes 08611a91
+ 00717a44 bytes 08a11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a0a194d79df95a36dc9e2b797e6ea39"></a>

### [`00717a58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/00717a58.md) → [`00717a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/00717a58.md) FUN_00717a58

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00717a64",
      "incomplete_value": false,
      "site": "00717a64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00717a64",
      "incomplete_value": false,
      "site": "00717a64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "00717a64",
      "DATA",
      [
        "storage",
        "00bfa698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00717a64",
      "DATA",
      [
        "storage",
        "00bfa6e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00717a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/00717a58.md#insn-00717a60)
- 新版 `00717a60`（命令位置の公開資料なし）

~~~diff
- 00717a60 ["COPY", "tmp:0:8", ["const:698:8"]]
- 00717a60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00717a60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00717a60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00717a60 ["COPY", "tmp:0:8", ["const:6e8:8"]]
+ 00717a60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00717a60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00717a60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00717a60 bytes 29611a91
+ 00717a60 bytes 29a11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d320e765b2a8d6ed1f637ab048dfa5f"></a>

### [`00717ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/00717ab8.md) → [`00717ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/00717ab8.md) FUN_00717ab8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00717acc",
      "incomplete_value": false,
      "site": "00717ad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00717acc",
      "incomplete_value": false,
      "site": "00717ad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
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
      "00717ad0",
      "DATA",
      [
        "storage",
        "00bfa718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00717ad0",
      "DATA",
      [
        "storage",
        "00bfa768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00717acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/00717ab8.md#insn-00717acc)
- 新版 `00717acc`（命令位置の公開資料なし）

~~~diff
- 00717acc ["COPY", "tmp:0:8", ["const:718:8"]]
- 00717acc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00717acc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00717acc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00717acc ["COPY", "tmp:0:8", ["const:768:8"]]
+ 00717acc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00717acc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00717acc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00717acc bytes 08611c91
+ 00717acc bytes 08a11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56248821890b2a7a4b85ea659b750fd8"></a>

### [`00717adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/00717adc.md) → [`00717adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/00717adc.md) FUN_00717adc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00717ae0",
      "incomplete_value": false,
      "site": "00717ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00717ae0",
      "incomplete_value": false,
      "site": "00717ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "00717ae4",
      "DATA",
      [
        "storage",
        "00bfa718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00717ae4",
      "DATA",
      [
        "storage",
        "00bfa768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00717ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/00717adc.md#insn-00717ae0)
- 新版 `00717ae0`（命令位置の公開資料なし）

~~~diff
- 00717ae0 ["COPY", "tmp:0:8", ["const:718:8"]]
- 00717ae0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00717ae0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00717ae0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00717ae0 ["COPY", "tmp:0:8", ["const:768:8"]]
+ 00717ae0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00717ae0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00717ae0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00717ae0 bytes 08611c91
+ 00717ae0 bytes 08a11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4adba8e31ad782ca2b4e8540163697d6"></a>

### [`00717b64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/00717b64.md) → [`00717b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/00717b64.md) _INIT_125

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
      "definition_site": "00717ba0",
      "incomplete_value": true,
      "site": "00717bbc",
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
      "definition_site": "00717ba0",
      "incomplete_value": true,
      "site": "00717bbc",
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
      "definition_site": "00717bc4",
      "incomplete_value": true,
      "site": "00717be0",
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
      "definition_site": "00717bc4",
      "incomplete_value": true,
      "site": "00717be0",
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
      "definition_site": "00717be4",
      "incomplete_value": true,
      "site": "00717c00",
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
      "definition_site": "00717be4",
      "incomplete_value": true,
      "site": "00717c00",
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
      "00717ba0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00717bc4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00717be4",
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
      "00717ba0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00717bc4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00717be4",
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

- 旧版 [`00717b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/00717b64.md#insn-00717b90) · [`00717b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/00717b64.md#insn-00717b98)
- 新版 `00717b90`（命令位置の公開資料なし） · `00717b98`（命令位置の公開資料なし）

~~~diff
- 00717b90 ["COPY", "tmp:0:8", ["const:e38:8"]]
- 00717b90 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00717b90 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00717b90 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00717b90 ["COPY", "tmp:0:8", ["const:e78:8"]]
+ 00717b90 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00717b90 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00717b90 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00717b90 bytes 73e23891
+ 00717b90 bytes 73e23991
- 00717b98 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00717b98 bytes 89dcff90
+ 00717b98 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00717b98 bytes 89dcff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35d914cc56d8ac4fd449e3a8ee9ab492"></a>

### [`007180bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00718/007180bc.md) → [`007180bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00718/007180bc.md) FUN_007180bc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`007127f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00712/007127f8.md) [`00713660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00713/00713660.md) · 呼出先 13件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00716ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00716/00716ee0.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`007127f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00712/007127f8.md) [`00713660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00713/00713660.md) · 呼出先 13件 [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00716ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00716/00716ee0.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.20% / 新版 91.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007180e8",
      "incomplete_value": true,
      "site": "007180e8",
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
      "definition_site": "007180e8",
      "incomplete_value": true,
      "site": "007180e8",
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
      "definition_site": "007180f0",
      "incomplete_value": false,
      "site": "00718100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007180f0",
      "incomplete_value": false,
      "site": "00718100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "definition_site": "007180f8",
      "incomplete_value": false,
      "site": "00718100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007180f8",
      "incomplete_value": false,
      "site": "00718100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:510:8"
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
      "007180e4",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007180f0",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007180f8",
      "PARAM",
      [
        "storage",
        "00bfa510",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007180e4",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007180f0",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007180f8",
      "PARAM",
      [
        "storage",
        "00bfa560",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007180e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00718/007180bc.md#insn-007180e4) · [`007180f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00718/007180bc.md#insn-007180f0) · [`007180f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00718/007180bc.md#insn-007180f8)
- 新版 `007180e4`（命令位置の公開資料なし） · `007180f0`（命令位置の公開資料なし） · `007180f8`（命令位置の公開資料なし）

~~~diff
- 007180e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007180e4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007180e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007180e4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007180e4 bytes 003d45f9
+ 007180e4 bytes 005d45f9
- 007180f0 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007180f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007180f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007180f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007180f0 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007180f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007180f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007180f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007180f0 bytes 21203991
+ 007180f0 bytes 21603a91
- 007180f8 ["COPY", "tmp:0:8", ["const:510:8"]]
- 007180f8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007180f8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007180f8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007180f8 ["COPY", "tmp:0:8", ["const:560:8"]]
+ 007180f8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007180f8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007180f8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007180f8 bytes 42401491
+ 007180f8 bytes 42801591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd6033de3535f0f5fd08de37262c393a"></a>

### [`007182dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00718/007182dc.md) → [`007182dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00718/007182dc.md) _INIT_126

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00718318",
      "incomplete_value": true,
      "site": "00718334",
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
      "definition_site": "00718318",
      "incomplete_value": true,
      "site": "00718334",
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
      "definition_site": "0071835c",
      "incomplete_value": true,
      "site": "00718378",
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
                "register:4050:8"
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
      "definition_site": "0071835c",
      "incomplete_value": true,
      "site": "00718378",
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
                "register:4050:8"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00718398",
      "incomplete_value": true,
      "site": "007183b4",
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
                "const:36c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00718398",
      "incomplete_value": true,
      "site": "007183b4",
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
                "const:36e:8"
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
      "00718318",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0071833c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0071835c",
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
      "00718318",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0071833c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0071835c",
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

- 旧版 [`00718308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00718/007182dc.md#insn-00718308) · [`00718310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00718/007182dc.md#insn-00718310)
- 新版 `00718308`（命令位置の公開資料なし） · `00718310`（命令位置の公開資料なし）

~~~diff
- 00718308 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 00718308 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00718308 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00718308 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00718308 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00718308 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00718308 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00718308 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00718308 bytes 73423991
+ 00718308 bytes 73423a91
- 00718310 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00718310 bytes 69dcfff0
+ 00718310 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00718310 bytes 69dcfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-235c75a0b7858ba7d5845c3e21c17a3b"></a>

### [`00718a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00718/00718a74.md) → [`00718a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00718/00718a74.md) FUN_00718a74

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 18件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 18件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.94% / 新版 96.94%

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
      "definition_site": "00718ad8",
      "incomplete_value": true,
      "site": "00718af4",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:d71:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00718ad8",
      "incomplete_value": true,
      "site": "00718af4",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:e05:8"
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
      "definition_site": "00718af8",
      "incomplete_value": true,
      "site": "00718af8",
      "value": [
        "LOAD",
        "8",
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
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00718af8",
      "incomplete_value": true,
      "site": "00718af8",
      "value": [
        "LOAD",
        "8",
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
                "const:d:8"
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
      "definition_site": "00719108",
      "incomplete_value": true,
      "site": "0071910c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00719108",
      "incomplete_value": true,
      "site": "0071910c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 106,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00718ac4",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00718ad8",
      "READ",
      [
        "storage",
        "002aee05",
        null,
        "string"
      ]
    ],
    [
      "00718ae0",
      "READ",
      [
        "storage",
        "002aee12",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00718ac4",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00718ad8",
      "READ",
      [
        "storage",
        "002aed71",
        null,
        "string"
      ]
    ],
    [
      "00718ae0",
      "READ",
      [
        "storage",
        "002aed7e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00718ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00718/00718a74.md#insn-00718ab8) · [`00718ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00718/00718a74.md#insn-00718ad4) · [`007190f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00718/00718a74.md#insn-007190f8)
- 新版 `00718ab8`（命令位置の公開資料なし） · `00718ad4`（命令位置の公開資料なし） · `007190f8`（命令位置の公開資料なし）

~~~diff
- 00718ab8 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00718ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00718ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00718ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00718ab8 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00718ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00718ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00718ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00718ab8 bytes 08a13491
+ 00718ab8 bytes 08e13591
- 00718ad4 ["COPY", "tmp:0:8", ["const:e05:8"]]
- 00718ad4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00718ad4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00718ad4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00718ad4 ["COPY", "tmp:0:8", ["const:d71:8"]]
+ 00718ad4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00718ad4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00718ad4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00718ad4 bytes 29153891
+ 00718ad4 bytes 29c53591
- 007190f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 007190f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007190f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 007190f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007190f8 bytes 08b946f9
+ 007190f8 bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-992aefb7b47ca2a369690e842c4ab1b1"></a>

### [`00719278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00719/00719278.md) → [`00719278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00719/00719278.md) FUN_00719278

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0071a28c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071a/0071a28c.md) · 呼出先 13件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`0071a28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071a/0071a28c.md) · 呼出先 13件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007192ac",
      "incomplete_value": false,
      "site": "007192b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007192ac",
      "incomplete_value": false,
      "site": "007192b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "definition_site": "007192c0",
      "incomplete_value": true,
      "site": "007192d4",
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
                "const:9a7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007192c0",
      "incomplete_value": true,
      "site": "007192d4",
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
                "const:91c:8"
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
      "definition_site": "007192d8",
      "incomplete_value": true,
      "site": "007192d8",
      "value": [
        "LOAD",
        "8",
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
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007192d8",
      "incomplete_value": true,
      "site": "007192d8",
      "value": [
        "LOAD",
        "8",
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
                "const:d:8"
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
      "007192b8",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "007192c0",
      "READ",
      [
        "storage",
        "002a191c",
        null,
        "string"
      ]
    ],
    [
      "007192c8",
      "READ",
      [
        "storage",
        "002a1929",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007192b8",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "007192c0",
      "READ",
      [
        "storage",
        "002a19a7",
        null,
        "string"
      ]
    ],
    [
      "007192c8",
      "READ",
      [
        "storage",
        "002a19b4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007192ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00719/00719278.md#insn-007192ac) · [`007192b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00719/00719278.md#insn-007192b0)
- 新版 `007192ac`（命令位置の公開資料なし） · `007192b0`（命令位置の公開資料なし）

~~~diff
- 007192ac ["COPY", "tmp:0:8", ["const:d28:8"]]
- 007192ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007192ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007192ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007192ac ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 007192ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007192ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007192ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007192ac bytes 08a13491
+ 007192ac bytes 08e13591
- 007192b0 ["COPY", "register:4048:8", ["const:2a1000:8"]]
- 007192b0 bytes 49dcff90
+ 007192b0 ["COPY", "register:4048:8", ["const:2a1000:8"]]
+ 007192b0 bytes 49dcff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9652e22fa7cb2996b5c8f15ce5d274b2"></a>

### [`007194ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00719/007194ac.md) → [`007194ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00719/007194ac.md) FUN_007194ac

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0071b5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071b/0071b5e0.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`0071b5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071b/0071b5e0.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.58% / 新版 96.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007194f8",
      "incomplete_value": true,
      "site": "00719500",
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
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007194f8",
      "incomplete_value": true,
      "site": "00719500",
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
            "const:d28:8"
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
      "definition_site": "00719518",
      "incomplete_value": true,
      "site": "00719524",
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
                "const:294000:8"
              ],
              [
                "leaf",
                "const:c6f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00719518",
      "incomplete_value": true,
      "site": "00719524",
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
                "const:294000:8"
              ],
              [
                "leaf",
                "const:cfc:8"
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
      "definition_site": "0071969c",
      "incomplete_value": true,
      "site": "007196a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0071969c",
      "incomplete_value": true,
      "site": "007196a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00719500",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00719518",
      "READ",
      [
        "storage",
        "00294cfc",
        null,
        "string"
      ]
    ],
    [
      "0071968c",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00719500",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00719518",
      "READ",
      [
        "storage",
        "00294c6f",
        null,
        "string"
      ]
    ],
    [
      "0071968c",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007194f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00719/007194ac.md#insn-007194f8) · [`00719514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00719/007194ac.md#insn-00719514) · [`0071968c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00719/007194ac.md#insn-0071968c)
- 新版 `007194f8`（命令位置の公開資料なし） · `00719514`（命令位置の公開資料なし） · `0071968c`（命令位置の公開資料なし）

~~~diff
- 007194f8 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 007194f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007194f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007194f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007194f8 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 007194f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007194f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007194f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007194f8 bytes 08a13491
+ 007194f8 bytes 08e13591
- 00719514 ["COPY", "tmp:0:8", ["const:cfc:8"]]
- 00719514 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00719514 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00719514 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00719514 ["COPY", "tmp:0:8", ["const:c6f:8"]]
+ 00719514 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00719514 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00719514 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00719514 bytes 08f13391
+ 00719514 bytes 08bd3191
- 0071968c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 0071968c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0071968c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 0071968c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0071968c bytes 08b946f9
+ 0071968c bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f507ecca3637e41bcfd3ad6dda8db0e"></a>

### [`0071b838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071b/0071b838.md) → [`0071b838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071b/0071b838.md) FUN_0071b838

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00761ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00761/00761ab0.md) [`00a33510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a33510.md) · 呼出先 8件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0071d874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071d874.md) [`0071dcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071dcf0.md) [`00728090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/00728090.md) [`0097ec84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097ec84.md)
- 新版 呼出元 2件 [`00761ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761ab0.md) [`00a33554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a33554.md) · 呼出先 8件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0071d874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071d874.md) [`0071dcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071dcf0.md) [`00728090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/00728090.md) [`0097ec84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097e/0097ec84.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.42% / 新版 98.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0071b994",
      "incomplete_value": false,
      "site": "0071b998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:808:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071b994",
      "incomplete_value": false,
      "site": "0071b998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0071ba40",
      "incomplete_value": false,
      "site": "0071ba40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071ba40",
      "incomplete_value": false,
      "site": "0071ba40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "0071b998",
      "DATA",
      [
        "storage",
        "00bfa7b8",
        null,
        "undefined *"
      ]
    ],
    [
      "0071ba40",
      "DATA",
      [
        "storage",
        "00bfa848",
        null,
        "undefined *"
      ]
    ],
    [
      "0071bac0",
      "READ",
      [
        "storage",
        "00bfa870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071b998",
      "DATA",
      [
        "storage",
        "00bfa808",
        null,
        "undefined *"
      ]
    ],
    [
      "0071ba40",
      "DATA",
      [
        "storage",
        "00bfa898",
        null,
        "undefined *"
      ]
    ],
    [
      "0071bac0",
      "READ",
      [
        "storage",
        "00bfa8c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071b994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071b/0071b838.md#insn-0071b994) · [`0071ba38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071b/0071b838.md#insn-0071ba38)
- 新版 `0071b994`（命令位置の公開資料なし） · `0071ba38`（命令位置の公開資料なし）

~~~diff
- 0071b994 ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 0071b994 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0071b994 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0071b994 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0071b994 ["COPY", "tmp:0:8", ["const:808:8"]]
+ 0071b994 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0071b994 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0071b994 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0071b994 bytes 29e11e91
+ 0071b994 bytes 29212091
- 0071ba38 ["COPY", "tmp:0:8", ["const:848:8"]]
- 0071ba38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071ba38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071ba38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071ba38 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 0071ba38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071ba38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071ba38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071ba38 bytes 08212191
+ 0071ba38 bytes 08612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c25e75e1dac9f3feb097178dadab06de"></a>

### [`0071bdc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071b/0071bdc8.md) → [`0071bdc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071b/0071bdc8.md) FUN_0071bdc8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e1a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md) [`0071c3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071c/0071c3d0.md) [`0071c4c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071c/0071c4c8.md) · 呼出先 10件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0071dfd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071dfd0.md) [`0071e48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e48c.md) [`00728090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/00728090.md) [`0073ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073ab94.md)
- 新版 呼出元 4件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`0071c3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071c/0071c3d0.md) [`0071c4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071c/0071c4c8.md) · 呼出先 10件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0071dfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071dfd0.md) [`0071e48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e48c.md) [`00728090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/00728090.md) [`0073ab94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073ab94.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0071bf84",
      "incomplete_value": false,
      "site": "0071bf88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071bf84",
      "incomplete_value": false,
      "site": "0071bf88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0071c03c",
      "incomplete_value": false,
      "site": "0071c040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071c03c",
      "incomplete_value": false,
      "site": "0071c040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "0071bf88",
      "DATA",
      [
        "storage",
        "00bfa8c8",
        null,
        "undefined *"
      ]
    ],
    [
      "0071c040",
      "DATA",
      [
        "storage",
        "00bfa948",
        null,
        "undefined *"
      ]
    ],
    [
      "0071c0c8",
      "READ",
      [
        "storage",
        "00bfa970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071bf88",
      "DATA",
      [
        "storage",
        "00bfa918",
        null,
        "undefined *"
      ]
    ],
    [
      "0071c040",
      "DATA",
      [
        "storage",
        "00bfa998",
        null,
        "undefined *"
      ]
    ],
    [
      "0071c0c8",
      "READ",
      [
        "storage",
        "00bfa9c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071bf84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071b/0071bdc8.md#insn-0071bf84) · [`0071c03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071b/0071bdc8.md#insn-0071c03c)
- 新版 `0071bf84`（命令位置の公開資料なし） · `0071c03c`（命令位置の公開資料なし）

~~~diff
- 0071bf84 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 0071bf84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0071bf84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0071bf84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0071bf84 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 0071bf84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0071bf84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0071bf84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0071bf84 bytes 29212391
+ 0071bf84 bytes 29612491
- 0071c03c ["COPY", "tmp:0:8", ["const:948:8"]]
- 0071c03c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0071c03c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0071c03c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0071c03c ["COPY", "tmp:0:8", ["const:998:8"]]
+ 0071c03c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0071c03c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0071c03c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0071c03c bytes 29212591
+ 0071c03c bytes 29612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3592a1ec053ebaed710a385cdc8f6d8"></a>

### [`0071c3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071c/0071c3d0.md) → [`0071c3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071c/0071c3d0.md) FUN_0071c3d0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00a2c36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2c/00a2c36c.md) · 呼出先 4件 [`0071bdc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071b/0071bdc8.md) [`0071e5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e5b8.md) [`0071e5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e5bc.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00a2c3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2c/00a2c3b0.md) · 呼出先 4件 [`0071bdc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071b/0071bdc8.md) [`0071e5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e5b8.md) [`0071e5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e5bc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "0071c410",
      "incomplete_value": false,
      "site": "0071c41c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071c410",
      "incomplete_value": false,
      "site": "0071c41c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
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
      "0071c41c",
      "DATA",
      [
        "storage",
        "00bfa9c8",
        null,
        "undefined *"
      ]
    ],
    [
      "0071c450",
      "READ",
      [
        "storage",
        "00bfa9e8",
        null,
        "pointer"
      ]
    ],
    [
      "0071c450",
      "READ",
      [
        "storage",
        "00bfa9f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071c41c",
      "DATA",
      [
        "storage",
        "00bfaa18",
        null,
        "undefined *"
      ]
    ],
    [
      "0071c450",
      "READ",
      [
        "storage",
        "00bfaa38",
        null,
        "pointer"
      ]
    ],
    [
      "0071c450",
      "READ",
      [
        "storage",
        "00bfaa40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071c410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071c/0071c3d0.md#insn-0071c410)
- 新版 `0071c410`（命令位置の公開資料なし）

~~~diff
- 0071c410 ["COPY", "tmp:0:8", ["const:9c8:8"]]
- 0071c410 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071c410 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071c410 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071c410 ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 0071c410 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071c410 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071c410 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071c410 bytes 08212791
+ 0071c410 bytes 08612891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d4ade0e13b00e08500ac0b157e1d89a"></a>

### [`0071c4c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071c/0071c4c8.md) → [`0071c4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071c/0071c4c8.md) FUN_0071c4c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00419718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) [`00989a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00989/00989a48.md) · 呼出先 11件 [`0071bdc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071b/0071bdc8.md) [`0071e624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e624.md) [`0071e628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e628.md) [`0071e6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e6a8.md) [`0071e6ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e6ac.md)
- 新版 呼出元 2件 [`00419718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`00989a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/00989a48.md) · 呼出先 11件 [`0071bdc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071b/0071bdc8.md) [`0071e624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e624.md) [`0071e628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e628.md) [`0071e6a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e6a8.md) [`0071e6ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e6ac.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0071c518",
      "incomplete_value": false,
      "site": "0071c518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071c518",
      "incomplete_value": false,
      "site": "0071c518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
      "definition_site": "0071c55c",
      "incomplete_value": false,
      "site": "0071c55c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071c55c",
      "incomplete_value": false,
      "site": "0071c55c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0071c570",
      "incomplete_value": false,
      "site": "0071c574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071c570",
      "incomplete_value": false,
      "site": "0071c574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:b48:8"
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
      "0071c518",
      "DATA",
      [
        "storage",
        "00bfaa48",
        null,
        "undefined *"
      ]
    ],
    [
      "0071c55c",
      "DATA",
      [
        "storage",
        "00bfaac8",
        null,
        "undefined *"
      ]
    ],
    [
      "0071c574",
      "DATA",
      [
        "storage",
        "00bfab48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071c518",
      "DATA",
      [
        "storage",
        "00bfaa98",
        null,
        "undefined *"
      ]
    ],
    [
      "0071c55c",
      "DATA",
      [
        "storage",
        "00bfab18",
        null,
        "undefined *"
      ]
    ],
    [
      "0071c574",
      "DATA",
      [
        "storage",
        "00bfab98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071c50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071c/0071c4c8.md#insn-0071c50c) · [`0071c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071c/0071c4c8.md#insn-0071c554) · [`0071c570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071c/0071c4c8.md#insn-0071c570)
- 新版 `0071c50c`（命令位置の公開資料なし） · `0071c554`（命令位置の公開資料なし） · `0071c570`（命令位置の公開資料なし）

~~~diff
- 0071c50c ["COPY", "tmp:0:8", ["const:a48:8"]]
- 0071c50c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071c50c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071c50c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071c50c ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 0071c50c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071c50c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071c50c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071c50c bytes 08212991
+ 0071c50c bytes 08612a91
- 0071c554 ["COPY", "tmp:0:8", ["const:ac8:8"]]
- 0071c554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071c554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071c554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071c554 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 0071c554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071c554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071c554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071c554 bytes 08212b91
+ 0071c554 bytes 08612c91
- 0071c570 ["COPY", "tmp:0:8", ["const:b48:8"]]
- 0071c570 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071c570 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071c570 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071c570 ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 0071c570 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071c570 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071c570 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071c570 bytes 08212d91
+ 0071c570 bytes 08612e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee0d160cd9a3f680a6f2fcfde69c00f7"></a>

### [`0071cb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071c/0071cb00.md) → [`0071cb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071c/0071cb00.md) FUN_0071cb00

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) · 呼出先 8件 [`0071e944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e944.md) [`0071f798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071f/0071f798.md) [`00720390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00720/00720390.md) [`00728090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/00728090.md) [`0097f740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097f740.md)
- 新版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · 呼出先 8件 [`0071e944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e944.md) [`0071f798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f798.md) [`00720390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/00720390.md) [`00728090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/00728090.md) [`0097f740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097f740.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.41% / 新版 98.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0071cc48",
      "incomplete_value": false,
      "site": "0071cc48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071cc48",
      "incomplete_value": false,
      "site": "0071cc48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
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
      "definition_site": "0071cd08",
      "incomplete_value": false,
      "site": "0071cd08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071cd08",
      "incomplete_value": false,
      "site": "0071cd08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:c48:8"
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
      "0071cc48",
      "DATA",
      [
        "storage",
        "00bfabc8",
        null,
        "undefined *"
      ]
    ],
    [
      "0071cd08",
      "DATA",
      [
        "storage",
        "00bfac48",
        null,
        "undefined *"
      ]
    ],
    [
      "0071cd94",
      "READ",
      [
        "storage",
        "00bfac70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071cc48",
      "DATA",
      [
        "storage",
        "00bfac18",
        null,
        "undefined *"
      ]
    ],
    [
      "0071cd08",
      "DATA",
      [
        "storage",
        "00bfac98",
        null,
        "undefined *"
      ]
    ],
    [
      "0071cd94",
      "READ",
      [
        "storage",
        "00bfacc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071cc40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071c/0071cb00.md#insn-0071cc40) · [`0071cd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071c/0071cb00.md#insn-0071cd00)
- 新版 `0071cc40`（命令位置の公開資料なし） · `0071cd00`（命令位置の公開資料なし）

~~~diff
- 0071cc40 ["COPY", "tmp:0:8", ["const:bc8:8"]]
- 0071cc40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0071cc40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0071cc40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0071cc40 ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 0071cc40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0071cc40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0071cc40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0071cc40 bytes 29212f91
+ 0071cc40 bytes 29613091
- 0071cd00 ["COPY", "tmp:0:8", ["const:c48:8"]]
- 0071cd00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0071cd00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0071cd00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0071cd00 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 0071cd00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0071cd00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0071cd00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0071cd00 bytes 29213191
+ 0071cd00 bytes 29613291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1639bf6decb2d95970843d87d36acea8"></a>

### [`0071d678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071d678.md) → [`0071d678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071d678.md) FUN_0071d678

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007194ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00719/007194ac.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`007194ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00719/007194ac.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0071d684",
      "incomplete_value": false,
      "site": "0071d688",
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
      "definition_site": "0071d684",
      "incomplete_value": false,
      "site": "0071d688",
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
      "0071d684",
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
      "0071d684",
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

- 旧版 [`0071d684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071d678.md#insn-0071d684)
- 新版 `0071d684`（命令位置の公開資料なし）

~~~diff
- 0071d684 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0071d684 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0071d684 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0071d684 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0071d684 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0071d684 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0071d684 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0071d684 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0071d684 bytes 000c0c91
+ 0071d684 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-701bea9773add9eace2a8515deb01001"></a>

### [`0071d68c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071d68c.md) → [`0071d68c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071d68c.md) FUN_0071d68c

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
      "definition_site": "0071d698",
      "incomplete_value": false,
      "site": "0071d6a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:808:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071d698",
      "incomplete_value": false,
      "site": "0071d6a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
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
      "0071d6a4",
      "DATA",
      [
        "storage",
        "00bfa7b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071d6a4",
      "DATA",
      [
        "storage",
        "00bfa808",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071d698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071d68c.md#insn-0071d698)
- 新版 `0071d698`（命令位置の公開資料なし）

~~~diff
- 0071d698 ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 0071d698 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0071d698 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0071d698 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0071d698 ["COPY", "tmp:0:8", ["const:808:8"]]
+ 0071d698 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0071d698 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0071d698 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0071d698 bytes 4ae11e91
+ 0071d698 bytes 4a212091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddf44e344691e418569f9bfc7c25e6c8"></a>

### [`0071d6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071d6d0.md) → [`0071d6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071d6d0.md) FUN_0071d6d0

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
      "definition_site": "0071d6e8",
      "incomplete_value": false,
      "site": "0071d6f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:808:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071d6e8",
      "incomplete_value": false,
      "site": "0071d6f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
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
      "0071d6f4",
      "DATA",
      [
        "storage",
        "00bfa7b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071d6f4",
      "DATA",
      [
        "storage",
        "00bfa808",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071d6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071d6d0.md#insn-0071d6e8)
- 新版 `0071d6e8`（命令位置の公開資料なし）

~~~diff
- 0071d6e8 ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 0071d6e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071d6e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071d6e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071d6e8 ["COPY", "tmp:0:8", ["const:808:8"]]
+ 0071d6e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071d6e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071d6e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071d6e8 bytes 08e11e91
+ 0071d6e8 bytes 08212091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4b7fd64e69282b018c83695845d82a4"></a>

### [`0071d72c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071d72c.md) → [`0071d72c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071d72c.md) FUN_0071d72c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0071d754",
      "incomplete_value": false,
      "site": "0071d758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:808:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071d754",
      "incomplete_value": false,
      "site": "0071d758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
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
      "0071d758",
      "DATA",
      [
        "storage",
        "00bfa7b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071d758",
      "DATA",
      [
        "storage",
        "00bfa808",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071d754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071d72c.md#insn-0071d754)
- 新版 `0071d754`（命令位置の公開資料なし）

~~~diff
- 0071d754 ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 0071d754 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0071d754 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0071d754 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0071d754 ["COPY", "tmp:0:8", ["const:808:8"]]
+ 0071d754 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0071d754 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0071d754 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0071d754 bytes 29e11e91
+ 0071d754 bytes 29212091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61b56407b58abdee89899607c5056f68"></a>

### [`0071d7bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071d7bc.md) → [`0071d7bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071d7bc.md) FUN_0071d7bc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0071d7d8",
      "incomplete_value": false,
      "site": "0071d7dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:808:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071d7d8",
      "incomplete_value": false,
      "site": "0071d7dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
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
      "0071d7dc",
      "DATA",
      [
        "storage",
        "00bfa7b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071d7dc",
      "DATA",
      [
        "storage",
        "00bfa808",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071d7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071d7bc.md#insn-0071d7d8)
- 新版 `0071d7d8`（命令位置の公開資料なし）

~~~diff
- 0071d7d8 ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 0071d7d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0071d7d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0071d7d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0071d7d8 ["COPY", "tmp:0:8", ["const:808:8"]]
+ 0071d7d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0071d7d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0071d7d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0071d7d8 bytes 4ae11e91
+ 0071d7d8 bytes 4a212091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6318e32625d11120bce55b2883409648"></a>

### [`0071db1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071db1c.md) → [`0071db1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071db1c.md) FUN_0071db1c

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
      "definition_site": "0071db28",
      "incomplete_value": false,
      "site": "0071db34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071db28",
      "incomplete_value": false,
      "site": "0071db34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "0071db34",
      "DATA",
      [
        "storage",
        "00bfa848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071db34",
      "DATA",
      [
        "storage",
        "00bfa898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071db28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071db1c.md#insn-0071db28)
- 新版 `0071db28`（命令位置の公開資料なし）

~~~diff
- 0071db28 ["COPY", "tmp:0:8", ["const:848:8"]]
- 0071db28 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0071db28 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0071db28 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0071db28 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 0071db28 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0071db28 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0071db28 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0071db28 bytes 4a212191
+ 0071db28 bytes 4a612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-223d1ab598d095fa9bb56e9cd7f97a4e"></a>

### [`0071dbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071dbbc.md) → [`0071dbbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071dbbc.md) FUN_0071dbbc

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
      "definition_site": "0071dbe8",
      "incomplete_value": false,
      "site": "0071dbe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071dbe8",
      "incomplete_value": false,
      "site": "0071dbe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "0071dbe8",
      "DATA",
      [
        "storage",
        "00bfa848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071dbe8",
      "DATA",
      [
        "storage",
        "00bfa898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071dbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071dbbc.md#insn-0071dbe0)
- 新版 `0071dbe0`（命令位置の公開資料なし）

~~~diff
- 0071dbe0 ["COPY", "tmp:0:8", ["const:848:8"]]
- 0071dbe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071dbe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071dbe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071dbe0 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 0071dbe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071dbe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071dbe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071dbe0 bytes 08212191
+ 0071dbe0 bytes 08612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ed6bfdb043fd8d6c5b319edc06b2d56"></a>

### [`0071dc44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071dc44.md) → [`0071dc44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071dc44.md) FUN_0071dc44

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0071dc60",
      "incomplete_value": true,
      "site": "0071dc60",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071dc60",
      "incomplete_value": true,
      "site": "0071dc60",
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
            "const:848:8"
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
      "0071dc60",
      "DATA",
      [
        "storage",
        "00bfa848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071dc60",
      "DATA",
      [
        "storage",
        "00bfa898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071dc5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071dc44.md#insn-0071dc5c)
- 新版 `0071dc5c`（命令位置の公開資料なし）

~~~diff
- 0071dc5c ["COPY", "tmp:0:8", ["const:848:8"]]
- 0071dc5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0071dc5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0071dc5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0071dc5c ["COPY", "tmp:0:8", ["const:898:8"]]
+ 0071dc5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0071dc5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0071dc5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0071dc5c bytes 29212191
+ 0071dc5c bytes 29612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbf9bef7660a2ba6d376c107969480f9"></a>

### [`0071dddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071dddc.md) → [`0071dddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071dddc.md) FUN_0071dddc

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
      "definition_site": "0071dde8",
      "incomplete_value": false,
      "site": "0071ddf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071dde8",
      "incomplete_value": false,
      "site": "0071ddf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "0071ddf4",
      "DATA",
      [
        "storage",
        "00bfa8c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071ddf4",
      "DATA",
      [
        "storage",
        "00bfa918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071dde8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071dddc.md#insn-0071dde8)
- 新版 `0071dde8`（命令位置の公開資料なし）

~~~diff
- 0071dde8 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 0071dde8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0071dde8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0071dde8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0071dde8 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 0071dde8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0071dde8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0071dde8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0071dde8 bytes 4a212391
+ 0071dde8 bytes 4a612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-711093a2d4b2cb374c545b50e9f3c691"></a>

### [`0071de20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071de20.md) → [`0071de20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071de20.md) FUN_0071de20

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
      "definition_site": "0071de38",
      "incomplete_value": false,
      "site": "0071de44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071de38",
      "incomplete_value": false,
      "site": "0071de44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "0071de44",
      "DATA",
      [
        "storage",
        "00bfa8c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071de44",
      "DATA",
      [
        "storage",
        "00bfa918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071de38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071de20.md#insn-0071de38)
- 新版 `0071de38`（命令位置の公開資料なし）

~~~diff
- 0071de38 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 0071de38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071de38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071de38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071de38 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 0071de38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071de38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071de38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071de38 bytes 08212391
+ 0071de38 bytes 08612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47d897fca83e21e5c16e084410ad4899"></a>

### [`0071de7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071de7c.md) → [`0071de7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071de7c.md) FUN_0071de7c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0071dea4",
      "incomplete_value": false,
      "site": "0071dea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071dea4",
      "incomplete_value": false,
      "site": "0071dea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "0071dea8",
      "DATA",
      [
        "storage",
        "00bfa8c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071dea8",
      "DATA",
      [
        "storage",
        "00bfa918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071dea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071de7c.md#insn-0071dea4)
- 新版 `0071dea4`（命令位置の公開資料なし）

~~~diff
- 0071dea4 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 0071dea4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0071dea4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0071dea4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0071dea4 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 0071dea4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0071dea4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0071dea4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0071dea4 bytes 29212391
+ 0071dea4 bytes 29612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58061552bb3e6832d7bcd2b883fe3f07"></a>

### [`0071df14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071df14.md) → [`0071df14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071df14.md) FUN_0071df14

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0071df34",
      "incomplete_value": false,
      "site": "0071df38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071df34",
      "incomplete_value": false,
      "site": "0071df38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "0071df38",
      "DATA",
      [
        "storage",
        "00bfa8c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071df38",
      "DATA",
      [
        "storage",
        "00bfa918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071df34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071df14.md#insn-0071df34)
- 新版 `0071df34`（命令位置の公開資料なし）

~~~diff
- 0071df34 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 0071df34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0071df34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0071df34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0071df34 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 0071df34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0071df34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0071df34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0071df34 bytes 29212391
+ 0071df34 bytes 29612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cf6974953b5fc7dedf141b2d7511985"></a>

### [`0071e2a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e2a4.md) → [`0071e2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e2a4.md) FUN_0071e2a4

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
      "definition_site": "0071e2b0",
      "incomplete_value": false,
      "site": "0071e2bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e2b0",
      "incomplete_value": false,
      "site": "0071e2bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "0071e2bc",
      "DATA",
      [
        "storage",
        "00bfa948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071e2bc",
      "DATA",
      [
        "storage",
        "00bfa998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e2a4.md#insn-0071e2b0)
- 新版 `0071e2b0`（命令位置の公開資料なし）

~~~diff
- 0071e2b0 ["COPY", "tmp:0:8", ["const:948:8"]]
- 0071e2b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0071e2b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0071e2b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0071e2b0 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 0071e2b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0071e2b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0071e2b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0071e2b0 bytes 4a212591
+ 0071e2b0 bytes 4a612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae3529b418547ebdab7fb1babe2a0a0e"></a>

### [`0071e2e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e2e8.md) → [`0071e2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e2e8.md) FUN_0071e2e8

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
      "definition_site": "0071e300",
      "incomplete_value": false,
      "site": "0071e30c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e300",
      "incomplete_value": false,
      "site": "0071e30c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "0071e30c",
      "DATA",
      [
        "storage",
        "00bfa948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071e30c",
      "DATA",
      [
        "storage",
        "00bfa998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e2e8.md#insn-0071e300)
- 新版 `0071e300`（命令位置の公開資料なし）

~~~diff
- 0071e300 ["COPY", "tmp:0:8", ["const:948:8"]]
- 0071e300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071e300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071e300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071e300 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 0071e300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071e300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071e300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071e300 bytes 08212591
+ 0071e300 bytes 08612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a11198ee2a0646a8d1076ef62b64280d"></a>

### [`0071e344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e344.md) → [`0071e344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e344.md) FUN_0071e344

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0071e36c",
      "incomplete_value": false,
      "site": "0071e370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e36c",
      "incomplete_value": false,
      "site": "0071e370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "0071e370",
      "DATA",
      [
        "storage",
        "00bfa948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071e370",
      "DATA",
      [
        "storage",
        "00bfa998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e344.md#insn-0071e36c)
- 新版 `0071e36c`（命令位置の公開資料なし）

~~~diff
- 0071e36c ["COPY", "tmp:0:8", ["const:948:8"]]
- 0071e36c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0071e36c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0071e36c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0071e36c ["COPY", "tmp:0:8", ["const:998:8"]]
+ 0071e36c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0071e36c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0071e36c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0071e36c bytes 29212591
+ 0071e36c bytes 29612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d503bb644ca6456c1038778516f166f5"></a>

### [`0071e3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e3d4.md) → [`0071e3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e3d4.md) FUN_0071e3d4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0071e3f0",
      "incomplete_value": false,
      "site": "0071e3f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e3f0",
      "incomplete_value": false,
      "site": "0071e3f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "0071e3f4",
      "DATA",
      [
        "storage",
        "00bfa948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071e3f4",
      "DATA",
      [
        "storage",
        "00bfa998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e3d4.md#insn-0071e3f0)
- 新版 `0071e3f0`（命令位置の公開資料なし）

~~~diff
- 0071e3f0 ["COPY", "tmp:0:8", ["const:948:8"]]
- 0071e3f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0071e3f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0071e3f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0071e3f0 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 0071e3f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0071e3f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0071e3f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0071e3f0 bytes 4a212591
+ 0071e3f0 bytes 4a612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79d0512176f6cad5991b8b73d2253727"></a>

### [`0071e584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e584.md) → [`0071e584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e584.md) FUN_0071e584

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0071e598",
      "incomplete_value": false,
      "site": "0071e59c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e598",
      "incomplete_value": false,
      "site": "0071e59c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
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
      "0071e59c",
      "DATA",
      [
        "storage",
        "00bfa9c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071e59c",
      "DATA",
      [
        "storage",
        "00bfaa18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e584.md#insn-0071e598)
- 新版 `0071e598`（命令位置の公開資料なし）

~~~diff
- 0071e598 ["COPY", "tmp:0:8", ["const:9c8:8"]]
- 0071e598 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071e598 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071e598 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071e598 ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 0071e598 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071e598 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071e598 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071e598 bytes 08212791
+ 0071e598 bytes 08612891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed0e48cb9e799095085cb2ce4acbefa6"></a>

### [`0071e5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e5a8.md) → [`0071e5a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e5a8.md) FUN_0071e5a8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0071e5ac",
      "incomplete_value": false,
      "site": "0071e5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e5ac",
      "incomplete_value": false,
      "site": "0071e5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
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
      "0071e5b0",
      "DATA",
      [
        "storage",
        "00bfa9c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071e5b0",
      "DATA",
      [
        "storage",
        "00bfaa18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e5a8.md#insn-0071e5ac)
- 新版 `0071e5ac`（命令位置の公開資料なし）

~~~diff
- 0071e5ac ["COPY", "tmp:0:8", ["const:9c8:8"]]
- 0071e5ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071e5ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071e5ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071e5ac ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 0071e5ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071e5ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071e5ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071e5ac bytes 08212791
+ 0071e5ac bytes 08612891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a49e771cb3144968c3aa9aea4899b1f6"></a>

### [`0071e5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e5f0.md) → [`0071e5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e5f0.md) FUN_0071e5f0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0071e604",
      "incomplete_value": false,
      "site": "0071e608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e604",
      "incomplete_value": false,
      "site": "0071e608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
      "0071e608",
      "DATA",
      [
        "storage",
        "00bfaa48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071e608",
      "DATA",
      [
        "storage",
        "00bfaa98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e5f0.md#insn-0071e604)
- 新版 `0071e604`（命令位置の公開資料なし）

~~~diff
- 0071e604 ["COPY", "tmp:0:8", ["const:a48:8"]]
- 0071e604 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071e604 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071e604 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071e604 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 0071e604 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071e604 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071e604 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071e604 bytes 08212991
+ 0071e604 bytes 08612a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa99495ef697b391b648d03a21d32cad"></a>

### [`0071e614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e614.md) → [`0071e614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e614.md) FUN_0071e614

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0071e618",
      "incomplete_value": false,
      "site": "0071e61c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e618",
      "incomplete_value": false,
      "site": "0071e61c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
      "0071e61c",
      "DATA",
      [
        "storage",
        "00bfaa48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071e61c",
      "DATA",
      [
        "storage",
        "00bfaa98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e614.md#insn-0071e618)
- 新版 `0071e618`（命令位置の公開資料なし）

~~~diff
- 0071e618 ["COPY", "tmp:0:8", ["const:a48:8"]]
- 0071e618 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071e618 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071e618 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071e618 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 0071e618 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071e618 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071e618 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071e618 bytes 08212991
+ 0071e618 bytes 08612a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d283ce54dd7c0e571ac8e423e1dce68"></a>

### [`0071e660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e660.md) → [`0071e660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e660.md) FUN_0071e660

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0071e684",
      "incomplete_value": false,
      "site": "0071e684",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e684",
      "incomplete_value": false,
      "site": "0071e684",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
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
      "0071e684",
      "DATA",
      [
        "storage",
        "00bfaac8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071e684",
      "DATA",
      [
        "storage",
        "00bfab18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e660.md#insn-0071e680)
- 新版 `0071e680`（命令位置の公開資料なし）

~~~diff
- 0071e680 ["COPY", "tmp:0:8", ["const:ac8:8"]]
- 0071e680 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071e680 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071e680 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071e680 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 0071e680 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071e680 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071e680 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071e680 bytes 08212b91
+ 0071e680 bytes 08612c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97c5c92c2b902dacfbaac97b0db309d7"></a>

### [`0071e694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e694.md) → [`0071e694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e694.md) FUN_0071e694

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0071e6a0",
      "incomplete_value": false,
      "site": "0071e6a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e6a0",
      "incomplete_value": false,
      "site": "0071e6a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
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
      "0071e6a0",
      "DATA",
      [
        "storage",
        "00bfaac8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071e6a0",
      "DATA",
      [
        "storage",
        "00bfab18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e69c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e694.md#insn-0071e69c)
- 新版 `0071e69c`（命令位置の公開資料なし）

~~~diff
- 0071e69c ["COPY", "tmp:0:8", ["const:ac8:8"]]
- 0071e69c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0071e69c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0071e69c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0071e69c ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 0071e69c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0071e69c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0071e69c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0071e69c bytes 29212b91
+ 0071e69c bytes 29612c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0aa0545f9a5b521826196bf33a719c57"></a>

### [`0071e8dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e8dc.md) → [`0071e8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e8dc.md) FUN_0071e8dc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0071e8f0",
      "incomplete_value": false,
      "site": "0071e8f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e8f0",
      "incomplete_value": false,
      "site": "0071e8f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:b48:8"
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
      "0071e8f4",
      "DATA",
      [
        "storage",
        "00bfab48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071e8f4",
      "DATA",
      [
        "storage",
        "00bfab98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e8dc.md#insn-0071e8f0)
- 新版 `0071e8f0`（命令位置の公開資料なし）

~~~diff
- 0071e8f0 ["COPY", "tmp:0:8", ["const:b48:8"]]
- 0071e8f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071e8f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071e8f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071e8f0 ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 0071e8f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071e8f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071e8f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071e8f0 bytes 08212d91
+ 0071e8f0 bytes 08612e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c22d4fbe32cbc696e9d5a8e912db64fe"></a>

### [`0071e900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e900.md) → [`0071e900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e900.md) FUN_0071e900

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0071e904",
      "incomplete_value": false,
      "site": "0071e908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e904",
      "incomplete_value": false,
      "site": "0071e908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:b48:8"
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
      "0071e908",
      "DATA",
      [
        "storage",
        "00bfab48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071e908",
      "DATA",
      [
        "storage",
        "00bfab98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071e900.md#insn-0071e904)
- 新版 `0071e904`（命令位置の公開資料なし）

~~~diff
- 0071e904 ["COPY", "tmp:0:8", ["const:b48:8"]]
- 0071e904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071e904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071e904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071e904 ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 0071e904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071e904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071e904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071e904 bytes 08212d91
+ 0071e904 bytes 08612e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e31815ae298fa69d58e23bc80a48daf"></a>

### [`0071ed5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071ed5c.md) → [`0071ed5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071ed5c.md) FUN_0071ed5c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0071d070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071d070.md) [`0071eb38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071eb38.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`0071d070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071d070.md) [`0071eb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071eb38.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0071ed68",
      "incomplete_value": false,
      "site": "0071ed6c",
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
      "definition_site": "0071ed68",
      "incomplete_value": false,
      "site": "0071ed6c",
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
      "0071ed68",
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
      "0071ed68",
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

- 旧版 [`0071ed68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071ed5c.md#insn-0071ed68)
- 新版 `0071ed68`（命令位置の公開資料なし）

~~~diff
- 0071ed68 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0071ed68 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0071ed68 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0071ed68 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0071ed68 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0071ed68 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0071ed68 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0071ed68 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0071ed68 bytes 000c0c91
+ 0071ed68 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d90f4c1480e7514e7b04cdbc0c6fc443"></a>

### [`0071edcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071edcc.md) → [`0071edcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071edcc.md) FUN_0071edcc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0071edcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071edcc.md) [`0096ff84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096ff84.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0071edcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071edcc.md) [`0096ff84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096ff84.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0071ef1c",
      "incomplete_value": false,
      "site": "0071ef24",
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
            "const:3a4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071ef1c",
      "incomplete_value": false,
      "site": "0071ef24",
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
            "const:30a:8"
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
      "definition_site": "0071ef40",
      "incomplete_value": false,
      "site": "0071ef4c",
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
            "const:885:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071ef40",
      "incomplete_value": false,
      "site": "0071ef4c",
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
            "const:919:8"
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
      "definition_site": "0071f074",
      "incomplete_value": false,
      "site": "0071f07c",
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
            "const:379:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071f074",
      "incomplete_value": false,
      "site": "0071f07c",
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
            "const:2ee:8"
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
      "0071ef1c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0071ef40",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "0071f074",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0071ef1c",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0071ef40",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0071f074",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071ef1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071edcc.md#insn-0071ef1c) · [`0071ef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071edcc.md#insn-0071ef40) · [`0071f074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071edcc.md#insn-0071f074)
- 新版 `0071ef1c`（命令位置の公開資料なし） · `0071ef40`（命令位置の公開資料なし） · `0071f074`（命令位置の公開資料なし）

~~~diff
- 0071ef1c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0071ef1c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0071ef1c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0071ef1c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0071ef1c ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0071ef1c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0071ef1c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0071ef1c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0071ef1c bytes 21280c91
+ 0071ef1c bytes 21900e91
- 0071ef40 ["COPY", "tmp:0:8", ["const:919:8"]]
- 0071ef40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0071ef40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0071ef40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0071ef40 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0071ef40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0071ef40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0071ef40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0071ef40 bytes 21642491
+ 0071ef40 bytes 21142291
- 0071f074 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0071f074 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0071f074 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0071f074 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0071f074 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0071f074 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0071f074 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0071f074 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0071f074 bytes 21b80b91
+ 0071f074 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5739a9de41110921fe8441231682c01"></a>

### [`0071f5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071f/0071f5b8.md) → [`0071f5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f5b8.md) FUN_0071f5b8

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
      "definition_site": "0071f5c4",
      "incomplete_value": false,
      "site": "0071f5d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071f5c4",
      "incomplete_value": false,
      "site": "0071f5d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
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
      "0071f5d0",
      "DATA",
      [
        "storage",
        "00bfabc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071f5d0",
      "DATA",
      [
        "storage",
        "00bfac18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071f5c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071f/0071f5b8.md#insn-0071f5c4)
- 新版 `0071f5c4`（命令位置の公開資料なし）

~~~diff
- 0071f5c4 ["COPY", "tmp:0:8", ["const:bc8:8"]]
- 0071f5c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0071f5c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0071f5c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0071f5c4 ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 0071f5c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0071f5c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0071f5c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0071f5c4 bytes 4a212f91
+ 0071f5c4 bytes 4a613091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fd1a0a03c194f56f11c51c885bd24c0"></a>

### [`0071f5fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071f/0071f5fc.md) → [`0071f5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f5fc.md) FUN_0071f5fc

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
      "definition_site": "0071f614",
      "incomplete_value": false,
      "site": "0071f620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071f614",
      "incomplete_value": false,
      "site": "0071f620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
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
      "0071f620",
      "DATA",
      [
        "storage",
        "00bfabc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071f620",
      "DATA",
      [
        "storage",
        "00bfac18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071f614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071f/0071f5fc.md#insn-0071f614)
- 新版 `0071f614`（命令位置の公開資料なし）

~~~diff
- 0071f614 ["COPY", "tmp:0:8", ["const:bc8:8"]]
- 0071f614 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071f614 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071f614 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071f614 ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 0071f614 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071f614 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071f614 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071f614 bytes 08212f91
+ 0071f614 bytes 08613091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a982164821e6a5fa1f6472d049223dd"></a>

### [`0071f658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071f/0071f658.md) → [`0071f658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f658.md) FUN_0071f658

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0071f684",
      "incomplete_value": false,
      "site": "0071f684",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071f684",
      "incomplete_value": false,
      "site": "0071f684",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
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
      "0071f684",
      "DATA",
      [
        "storage",
        "00bfabc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071f684",
      "DATA",
      [
        "storage",
        "00bfac18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071f67c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071f/0071f658.md#insn-0071f67c)
- 新版 `0071f67c`（命令位置の公開資料なし）

~~~diff
- 0071f67c ["COPY", "tmp:0:8", ["const:bc8:8"]]
- 0071f67c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071f67c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071f67c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071f67c ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 0071f67c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071f67c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071f67c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071f67c bytes 08212f91
+ 0071f67c bytes 08613091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b63ea62dadb336e5bc2ddbe366852d3"></a>

### [`0071f6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071f/0071f6e8.md) → [`0071f6e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f6e8.md) FUN_0071f6e8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0071f708",
      "incomplete_value": false,
      "site": "0071f708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071f708",
      "incomplete_value": false,
      "site": "0071f708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
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
      "0071f708",
      "DATA",
      [
        "storage",
        "00bfabc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0071f708",
      "DATA",
      [
        "storage",
        "00bfac18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071f704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071f/0071f6e8.md#insn-0071f704)
- 新版 `0071f704`（命令位置の公開資料なし）

~~~diff
- 0071f704 ["COPY", "tmp:0:8", ["const:bc8:8"]]
- 0071f704 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071f704 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071f704 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0071f704 ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 0071f704 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0071f704 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0071f704 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071f704 bytes 08212f91
+ 0071f704 bytes 08613091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8755aaf58b7c72d2eb95f9cb6219855"></a>

### [`007201bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00720/007201bc.md) → [`007201bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007201bc.md) FUN_007201bc

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
      "definition_site": "007201c8",
      "incomplete_value": false,
      "site": "007201d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007201c8",
      "incomplete_value": false,
      "site": "007201d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:c48:8"
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
      "007201d4",
      "DATA",
      [
        "storage",
        "00bfac48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007201d4",
      "DATA",
      [
        "storage",
        "00bfac98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007201c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00720/007201bc.md#insn-007201c8)
- 新版 `007201c8`（命令位置の公開資料なし）

~~~diff
- 007201c8 ["COPY", "tmp:0:8", ["const:c48:8"]]
- 007201c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007201c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007201c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007201c8 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 007201c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007201c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007201c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007201c8 bytes 4a213191
+ 007201c8 bytes 4a613291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b0917b7d8d6451a22b962d5656f0270"></a>

### [`00720200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00720/00720200.md) → [`00720200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/00720200.md) FUN_00720200

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
      "definition_site": "00720218",
      "incomplete_value": false,
      "site": "00720224",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00720218",
      "incomplete_value": false,
      "site": "00720224",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:c48:8"
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
      "00720224",
      "DATA",
      [
        "storage",
        "00bfac48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00720224",
      "DATA",
      [
        "storage",
        "00bfac98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00720218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00720/00720200.md#insn-00720218)
- 新版 `00720218`（命令位置の公開資料なし）

~~~diff
- 00720218 ["COPY", "tmp:0:8", ["const:c48:8"]]
- 00720218 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00720218 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00720218 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00720218 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 00720218 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00720218 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00720218 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00720218 bytes 08213191
+ 00720218 bytes 08613291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8bac5e8e74a1699ef7cd5c30184e1bd"></a>

### [`0072025c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00720/0072025c.md) → [`0072025c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/0072025c.md) FUN_0072025c

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
      "definition_site": "00720288",
      "incomplete_value": false,
      "site": "00720288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00720288",
      "incomplete_value": false,
      "site": "00720288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:c48:8"
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
      "00720288",
      "DATA",
      [
        "storage",
        "00bfac48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00720288",
      "DATA",
      [
        "storage",
        "00bfac98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00720280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00720/0072025c.md#insn-00720280)
- 新版 `00720280`（命令位置の公開資料なし）

~~~diff
- 00720280 ["COPY", "tmp:0:8", ["const:c48:8"]]
- 00720280 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00720280 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00720280 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00720280 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 00720280 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00720280 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00720280 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00720280 bytes 08213191
+ 00720280 bytes 08613291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b1535cad4e568ab642a1e2e9bc8e1e9"></a>

### [`007202e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00720/007202e4.md) → [`007202e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007202e4.md) FUN_007202e4

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
      "definition_site": "00720300",
      "incomplete_value": false,
      "site": "00720300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00720300",
      "incomplete_value": false,
      "site": "00720300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:c48:8"
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
      "00720300",
      "DATA",
      [
        "storage",
        "00bfac48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00720300",
      "DATA",
      [
        "storage",
        "00bfac98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007202fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00720/007202e4.md#insn-007202fc)
- 新版 `007202fc`（命令位置の公開資料なし）

~~~diff
- 007202fc ["COPY", "tmp:0:8", ["const:c48:8"]]
- 007202fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007202fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007202fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007202fc ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 007202fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007202fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007202fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007202fc bytes 29213191
+ 007202fc bytes 29613291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8303cca3be03e2a899c69d045a630570"></a>

### [`00720714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00720/00720714.md) → [`00720714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/00720714.md) _INIT_127

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
      "definition_site": "00720750",
      "incomplete_value": true,
      "site": "0072076c",
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
      "definition_site": "00720750",
      "incomplete_value": true,
      "site": "0072076c",
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
      "definition_site": "00720774",
      "incomplete_value": true,
      "site": "00720790",
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
      "definition_site": "00720774",
      "incomplete_value": true,
      "site": "00720790",
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
      "definition_site": "00720794",
      "incomplete_value": true,
      "site": "007207b0",
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
      "definition_site": "00720794",
      "incomplete_value": true,
      "site": "007207b0",
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
      "00720750",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00720774",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00720794",
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
      "00720750",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00720774",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00720794",
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

- 旧版 [`00720740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00720/00720714.md#insn-00720740) · [`00720748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00720/00720714.md#insn-00720748)
- 新版 `00720740`（命令位置の公開資料なし） · `00720748`（命令位置の公開資料なし）

~~~diff
- 00720740 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 00720740 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00720740 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00720740 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00720740 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 00720740 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00720740 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00720740 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00720740 bytes 73a23991
+ 00720740 bytes 73a23a91
- 00720748 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00720748 bytes 29dcfff0
+ 00720748 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00720748 bytes 29dcfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea95f58f7f0e7a720025f29f2df64765"></a>

### [`00721018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00721/00721018.md) → [`00721018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00721/00721018.md) FUN_00721018

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006c0784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0784.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md)
- 新版 呼出元 1件 [`006c0784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0784.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.21% / 新版 97.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00721388",
      "incomplete_value": false,
      "site": "00721390",
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
      "definition_site": "00721388",
      "incomplete_value": false,
      "site": "00721390",
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
      "007210a8",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "00721118",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "00721168",
      "READ",
      [
        "storage",
        "00c1b718",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007210a8",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "00721118",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "00721168",
      "READ",
      [
        "storage",
        "00c1b768",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00721084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00721/00721018.md#insn-00721084) · [`00721168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00721/00721018.md#insn-00721168) · [`007211fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00721/00721018.md#insn-007211fc)
- 新版 `00721084`（命令位置の公開資料なし） · `00721168`（命令位置の公開資料なし） · `007211fc`（命令位置の公開資料なし）

~~~diff
- 00721084 ["COPY", "tmp:0:8", ["const:866:8"]]
- 00721084 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 00721084 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 00721084 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 00721084 ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 00721084 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 00721084 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 00721084 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 00721084 bytes 399b2191
+ 00721084 bytes 39671f91
- 00721168 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:718:8"]]
- 00721168 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00721168 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:768:8"]]
+ 00721168 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 00721168 bytes 7b8f43f9
+ 00721168 bytes 7bb743f9
- 007211fc ["COPY", "register:4040:8", ["const:c23000:8"]]
+ 007211fc ["COPY", "register:4040:8", ["const:c24000:8"]]
- 007211fc bytes 082800d0
+ 007211fc bytes 082800f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75fbb2fb47c2a113bc85243a7026ad56"></a>

### [`00723a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00723/00723a20.md) → [`00723a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00723/00723a20.md) FUN_00723a20

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007e5fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e5/007e5fa4.md) · 呼出先 9件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md) [`00ab11f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab11f0.md)
- 新版 呼出元 1件 [`007e5fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e5fa4.md) · 呼出先 9件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md) [`00ab1234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1234.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.18% / 新版 98.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00723a50",
      "incomplete_value": true,
      "site": "00723a68",
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
                "const:95a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00723a50",
      "incomplete_value": true,
      "site": "00723a68",
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
                "const:8cf:8"
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
      "00723a50",
      "READ",
      [
        "storage",
        "0029f8cf",
        null,
        "string"
      ]
    ],
    [
      "00723d34",
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
      "00723a50",
      "READ",
      [
        "storage",
        "0029f95a",
        null,
        "string"
      ]
    ],
    [
      "00723d34",
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

- 旧版 [`00723a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00723/00723a20.md#insn-00723a48) · [`00723ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00723/00723a20.md#insn-00723ab4)
- 新版 `00723a48`（命令位置の公開資料なし） · `00723ab4`（命令位置の公開資料なし）

~~~diff
- 00723a48 ["COPY", "tmp:0:8", ["const:8cf:8"]]
- 00723a48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00723a48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00723a48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00723a48 ["COPY", "tmp:0:8", ["const:95a:8"]]
+ 00723a48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00723a48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00723a48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00723a48 bytes 293d2391
+ 00723a48 bytes 29692591
- 00723ab4 ["COPY", "tmp:0:8", ["const:866:8"]]
- 00723ab4 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00723ab4 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00723ab4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00723ab4 ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 00723ab4 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00723ab4 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00723ab4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00723ab4 bytes b59a2191
+ 00723ab4 bytes b5661f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c56290761cbbce1560c181d0b6632bf"></a>

### [`007240f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00724/007240f8.md) → [`007240f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00724/007240f8.md) FUN_007240f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008fdd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fdd40.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`008fdd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fd/008fdd40.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00724128",
      "incomplete_value": true,
      "site": "00724134",
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
                "const:9a3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00724128",
      "incomplete_value": true,
      "site": "00724134",
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
                "const:994:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00724128",
      "incomplete_value": true,
      "site": "00724134",
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
      "definition_site": "00724128",
      "incomplete_value": true,
      "site": "00724134",
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
      "00724128",
      "READ",
      [
        "storage",
        "002a9994",
        null,
        "string"
      ]
    ],
    [
      "00724128",
      "READ",
      [
        "storage",
        "002a99a4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00724128",
      "READ",
      [
        "storage",
        "002a99a3",
        null,
        "string"
      ]
    ],
    [
      "00724128",
      "READ",
      [
        "storage",
        "002a99b3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00724124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00724/007240f8.md#insn-00724124)
- 新版 `00724124`（命令位置の公開資料なし）

~~~diff
- 00724124 ["COPY", "tmp:0:8", ["const:994:8"]]
- 00724124 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00724124 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00724124 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00724124 ["COPY", "tmp:0:8", ["const:9a3:8"]]
+ 00724124 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00724124 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00724124 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00724124 bytes 08512691
+ 00724124 bytes 088d2691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5202652620f03492e22a12b298985de8"></a>

### [`00724148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00724/00724148.md) → [`00724148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00724/00724148.md) FUN_00724148

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008fe34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe34c.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`008fe34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fe/008fe34c.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0072416c",
      "incomplete_value": true,
      "site": "0072417c",
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
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:77e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072416c",
      "incomplete_value": true,
      "site": "0072417c",
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
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:6f3:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00724170",
      "incomplete_value": true,
      "site": "00724180",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00724170",
      "incomplete_value": true,
      "site": "00724180",
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
                "const:e:8"
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
      "0072416c",
      "READ",
      [
        "storage",
        "0029d6f3",
        null,
        "string"
      ]
    ],
    [
      "00724170",
      "READ",
      [
        "storage",
        "0029d701",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0072416c",
      "READ",
      [
        "storage",
        "0029d77e",
        null,
        "string"
      ]
    ],
    [
      "00724170",
      "READ",
      [
        "storage",
        "0029d78c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00724164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00724/00724148.md#insn-00724164) · [`00724168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00724/00724148.md#insn-00724168)
- 新版 `00724164`（命令位置の公開資料なし） · `00724168`（命令位置の公開資料なし）

~~~diff
- 00724164 ["COPY", "tmp:0:8", ["const:6f3:8"]]
- 00724164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00724164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00724164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00724164 ["COPY", "tmp:0:8", ["const:77e:8"]]
+ 00724164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00724164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00724164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00724164 bytes 08cd1b91
+ 00724164 bytes 08f91d91
- 00724168 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00724168 bytes 69dcff90
+ 00724168 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 00724168 bytes 69dcff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08ad98322f9796f76cf76d04a283b9c5"></a>

### [`00724198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00724/00724198.md) → [`00724198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00724/00724198.md) FUN_00724198

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008fdba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fdba8.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00469fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fe0.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md)
- 新版 呼出元 1件 [`008fdba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fd/008fdba8.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00469fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fe0.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.24% / 新版 93.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00724230",
      "incomplete_value": true,
      "site": "00724230",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f2f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00724230",
      "incomplete_value": true,
      "site": "00724230",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f31:8"
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
      "definition_site": "007242c4",
      "incomplete_value": true,
      "site": "007242dc",
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
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:939:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007242c4",
      "incomplete_value": true,
      "site": "007242dc",
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
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:8ae:8"
              ]
            ]
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
      "definition_site": "007243b8",
      "incomplete_value": true,
      "site": "007243c8",
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
                "const:299000:8"
              ],
              [
                "leaf",
                "const:171:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007243b8",
      "incomplete_value": true,
      "site": "007243c8",
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
                "const:299000:8"
              ],
              [
                "leaf",
                "const:1fe:8"
              ]
            ]
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
      "007241f8",
      "READ",
      [
        "storage",
        "002991f1",
        null,
        "string"
      ]
    ],
    [
      "00724220",
      "READ",
      [
        "storage",
        "00299f31",
        null,
        "string"
      ]
    ],
    [
      "007242c4",
      "READ",
      [
        "storage",
        "0029c8ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007241f8",
      "READ",
      [
        "storage",
        "00299164",
        null,
        "string"
      ]
    ],
    [
      "00724220",
      "READ",
      [
        "storage",
        "00299f2f",
        null,
        "string"
      ]
    ],
    [
      "007242c4",
      "READ",
      [
        "storage",
        "0029c939",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007241f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00724/00724198.md#insn-007241f4) · [`00724218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00724/00724198.md#insn-00724218) · [`007242c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00724/00724198.md#insn-007242c0)
- 新版 `007241f4`（命令位置の公開資料なし） · `00724218`（命令位置の公開資料なし） · `007242c0`（命令位置の公開資料なし）

~~~diff
- 007241f4 ["COPY", "tmp:0:8", ["const:1f1:8"]]
- 007241f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007241f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007241f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007241f4 ["COPY", "tmp:0:8", ["const:164:8"]]
+ 007241f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007241f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007241f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007241f4 bytes 08c50791
+ 007241f4 bytes 08910591
- 00724218 ["COPY", "tmp:0:8", ["const:f31:8"]]
- 00724218 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00724218 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00724218 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00724218 ["COPY", "tmp:0:8", ["const:f2f:8"]]
+ 00724218 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00724218 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00724218 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00724218 bytes 29c53c91
+ 00724218 bytes 29bd3c91
- 007242c0 ["COPY", "tmp:0:8", ["const:8ae:8"]]
- 007242c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007242c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007242c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007242c0 ["COPY", "tmp:0:8", ["const:939:8"]]
+ 007242c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007242c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007242c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007242c0 bytes 29b92291
+ 007242c0 bytes 29e52491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73a177314c4bc86ea287f4f6cd3ba6aa"></a>

### [`00725698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00725/00725698.md) → [`00725698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00725/00725698.md) FUN_00725698

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009121c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00912/009121c4.md) · 呼出先 13件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`005b5878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b5/005b5878.md) [`006f302c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f3/006f302c.md) [`006f4c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f4/006f4c58.md)
- 新版 呼出元 1件 [`009121c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00912/009121c4.md) · 呼出先 13件 [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`005b5878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5878.md) [`006f302c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f302c.md) [`006f4c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f4c58.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.94% / 新版 96.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00725904",
      "incomplete_value": false,
      "site": "00725914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00725904",
      "incomplete_value": false,
      "site": "00725914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00725950",
      "incomplete_value": false,
      "site": "00725960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00725950",
      "incomplete_value": false,
      "site": "00725960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007256e0",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "00725720",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00725730",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "007256e0",
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "00725720",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00725730",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007256e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00725/00725698.md#insn-007256e0) · [`007256f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00725/00725698.md#insn-007256f0) · [`007256f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00725/00725698.md#insn-007256f4)
- 新版 `007256e0`（命令位置の公開資料なし） · `007256f0`（命令位置の公開資料なし）

~~~diff
- 007256e0 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:e60:8"]]
- 007256e0 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 007256e0 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:eb0:8"]]
+ 007256e0 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 007256e0 bytes 393347f9
+ 007256e0 bytes 395b47f9
- 007256f0 ["COPY", "tmp:0:8", ["const:38:8"]]
- 007256f0 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 007256f0 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 007256f0 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 007256f0 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 007256f0 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 007256f0 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 007256f0 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 007256f0 bytes 94e20091
+ 007256f0 bytes 94e20191
- 007256f4 ["COPY", "register:40a8:8", ["const:c25000:8"]]
- 007256f4 bytes 15280090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9871ba8fa3eb628d55470de2f335ffcb"></a>

### [`007280a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/007280a8.md) → [`007280a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/007280a8.md) FUN_007280a8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00989a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00989/00989a48.md) · 呼出先 10件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md) [`00589fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00589/00589fe4.md) [`005b5878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b5/005b5878.md)
- 新版 呼出元 1件 [`00989a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/00989a48.md) · 呼出先 10件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md) [`00589fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00589/00589fe4.md) [`005b5878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5878.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0072811c",
      "incomplete_value": true,
      "site": "0072812c",
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
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:94c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072811c",
      "incomplete_value": true,
      "site": "0072812c",
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
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:8c1:8"
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
      "definition_site": "00728130",
      "incomplete_value": true,
      "site": "00728130",
      "value": [
        "LOAD",
        "8",
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
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00728130",
      "incomplete_value": true,
      "site": "00728130",
      "value": [
        "LOAD",
        "8",
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
                "const:d:8"
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
      "definition_site": "007282b8",
      "incomplete_value": false,
      "site": "007282c0",
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
            "const:834:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007282b8",
      "incomplete_value": false,
      "site": "007282c0",
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
            "const:7a9:8"
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
      "0072811c",
      "READ",
      [
        "storage",
        "0029c8c1",
        null,
        "string"
      ]
    ],
    [
      "00728120",
      "READ",
      [
        "storage",
        "0029c8ce",
        null,
        "string"
      ]
    ],
    [
      "007282b8",
      "PARAM",
      [
        "storage",
        "002a37a9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0072811c",
      "READ",
      [
        "storage",
        "0029c94c",
        null,
        "string"
      ]
    ],
    [
      "00728120",
      "READ",
      [
        "storage",
        "0029c959",
        null,
        "string"
      ]
    ],
    [
      "007282b8",
      "PARAM",
      [
        "storage",
        "002a3834",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00728114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/007280a8.md#insn-00728114) · [`007282b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/007280a8.md#insn-007282b8)
- 新版 `00728114`（命令位置の公開資料なし） · `007282b8`（命令位置の公開資料なし）

~~~diff
- 00728114 ["COPY", "tmp:0:8", ["const:8c1:8"]]
- 00728114 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00728114 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00728114 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00728114 ["COPY", "tmp:0:8", ["const:94c:8"]]
+ 00728114 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00728114 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00728114 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00728114 bytes 29052391
+ 00728114 bytes 29312591
- 007282b8 ["COPY", "tmp:0:8", ["const:7a9:8"]]
- 007282b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007282b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007282b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007282b8 ["COPY", "tmp:0:8", ["const:834:8"]]
+ 007282b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007282b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007282b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007282b8 bytes 21a41e91
+ 007282b8 bytes 21d02091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dad2faf00e36c5da69f0ddc3efc03f1f"></a>

### [`007283fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/007283fc.md) → [`007283fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/007283fc.md) FUN_007283fc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00989a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00989/00989a48.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md) [`005b5878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b5/005b5878.md) [`0063e6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e6d4.md)
- 新版 呼出元 1件 [`00989a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/00989a48.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md) [`005b5878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5878.md) [`0063e6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e6d4.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.03% / 新版 98.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007287f4",
      "incomplete_value": true,
      "site": "00728800",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:834:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007287f4",
      "incomplete_value": true,
      "site": "00728800",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:7a9:8"
              ]
            ]
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
      "00728528",
      "READ",
      [
        "storage",
        "0029c8c1",
        null,
        "string"
      ]
    ],
    [
      "00728534",
      "READ",
      [
        "storage",
        "0029c8ce",
        null,
        "string"
      ]
    ],
    [
      "007286c8",
      "READ",
      [
        "storage",
        "002a1932",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00728528",
      "READ",
      [
        "storage",
        "0029c94c",
        null,
        "string"
      ]
    ],
    [
      "00728534",
      "READ",
      [
        "storage",
        "0029c959",
        null,
        "string"
      ]
    ],
    [
      "007286c8",
      "READ",
      [
        "storage",
        "002a19bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00728474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/007283fc.md#insn-00728474) · [`0072847c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/007283fc.md#insn-0072847c)
- 新版 `00728474`（命令位置の公開資料なし） · `0072847c`（命令位置の公開資料なし）

~~~diff
- 00728474 ["COPY", "tmp:0:8", ["const:932:8"]]
- 00728474 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00728474 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00728474 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00728474 ["COPY", "tmp:0:8", ["const:9bd:8"]]
+ 00728474 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00728474 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00728474 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00728474 bytes d6ca2491
+ 00728474 bytes d6f62691
- 0072847c ["COPY", "register:40e0:8", ["const:29c000:8"]]
- 0072847c bytes bcdbff90
+ 0072847c ["COPY", "register:40e0:8", ["const:29c000:8"]]
+ 0072847c bytes bcdbff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-204a02a87c52f27c07f6ef1425ad3a63"></a>

### [`007289e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/007289e0.md) → [`007289e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/007289e0.md) FUN_007289e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a0fc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0f/00a0fc20.md) · 呼出先 13件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00a0fc64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0f/00a0fc64.md) · 呼出先 13件 [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.10% / 新版 89.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00728ca8",
      "incomplete_value": false,
      "site": "00728ca8",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00728ca8",
      "incomplete_value": false,
      "site": "00728ca8",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00728cac",
      "incomplete_value": false,
      "site": "00728cac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00728cac",
      "incomplete_value": false,
      "site": "00728cac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00728ca8",
      "incomplete_value": false,
      "site": "00728cac",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00728ca8",
      "incomplete_value": false,
      "site": "00728cac",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
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
      "00728a18",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00728a2c",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "00728a2c",
      "PARAM",
      [
        "storage",
        "00c250d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00728a18",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00728a2c",
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "00728a2c",
      "PARAM",
      [
        "storage",
        "00c25118",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00728a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/007289e0.md#insn-00728a10) · [`00728a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/007289e0.md#insn-00728a28) · [`00728a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/007289e0.md#insn-00728a2c)
- 新版 `00728a10`（命令位置の公開資料なし） · `00728a28`（命令位置の公開資料なし） · `00728a2c`（命令位置の公開資料なし）

~~~diff
- 00728a10 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00728a10 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 00728a10 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 00728a10 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 00728a10 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00728a10 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 00728a10 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 00728a10 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 00728a10 bytes f7e20091
+ 00728a10 bytes f7e20191
- 00728a28 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00728a28 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00728a28 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00728a28 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00728a28 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 00728a28 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00728a28 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00728a28 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00728a28 bytes 94020091
+ 00728a28 bytes 94020191
- 00728a2c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:e60:8"]]
- 00728a2c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00728a2c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:eb0:8"]]
+ 00728a2c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00728a2c bytes 423047f9
+ 00728a2c bytes 425847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5db8bfefadc2aef13c92d6580d16de24"></a>

### [`00729130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/00729130.md) → [`00729130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/00729130.md) FUN_00729130

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00729144",
      "incomplete_value": false,
      "site": "00729148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00729144",
      "incomplete_value": false,
      "site": "00729148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
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
      "00729148",
      "DATA",
      [
        "storage",
        "00bfacc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00729148",
      "DATA",
      [
        "storage",
        "00bfad18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00729144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/00729130.md#insn-00729144)
- 新版 `00729144`（命令位置の公開資料なし）

~~~diff
- 00729144 ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 00729144 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00729144 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00729144 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00729144 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 00729144 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00729144 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00729144 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00729144 bytes 08213391
+ 00729144 bytes 08613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae93ffa08272f2a024c09c0516debbc4"></a>

### [`00729154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/00729154.md) → [`00729154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/00729154.md) FUN_00729154

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00729158",
      "incomplete_value": false,
      "site": "0072915c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00729158",
      "incomplete_value": false,
      "site": "0072915c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
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
      "0072915c",
      "DATA",
      [
        "storage",
        "00bfacc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0072915c",
      "DATA",
      [
        "storage",
        "00bfad18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00729158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/00729154.md#insn-00729158)
- 新版 `00729158`（命令位置の公開資料なし）

~~~diff
- 00729158 ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 00729158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00729158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00729158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00729158 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 00729158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00729158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00729158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00729158 bytes 08213391
+ 00729158 bytes 08613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-100bf1e9ff8f4d4f3a1d8e72fcbbf8bd"></a>

### [`0072916c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/0072916c.md) → [`0072916c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/0072916c.md) FUN_0072916c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ad88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046ad88.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ad88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046ad88.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.19% / 新版 92.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007291f4",
      "incomplete_value": true,
      "site": "00729208",
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
                "const:9d6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007291f4",
      "incomplete_value": true,
      "site": "00729208",
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
                "const:94b:8"
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
      "definition_site": "0072920c",
      "incomplete_value": true,
      "site": "0072920c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0072920c",
      "incomplete_value": true,
      "site": "0072920c",
      "value": [
        "LOAD",
        "8",
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
      "007291f4",
      "READ",
      [
        "storage",
        "002a194b",
        null,
        "string"
      ]
    ],
    [
      "007291fc",
      "READ",
      [
        "storage",
        "002a1959",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007291f4",
      "READ",
      [
        "storage",
        "002a19d6",
        null,
        "string"
      ]
    ],
    [
      "007291fc",
      "READ",
      [
        "storage",
        "002a19e4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007291f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/0072916c.md#insn-007291f0)
- 新版 `007291f0`（命令位置の公開資料なし）

~~~diff
- 007291f0 ["COPY", "tmp:0:8", ["const:94b:8"]]
- 007291f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007291f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007291f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007291f0 ["COPY", "tmp:0:8", ["const:9d6:8"]]
+ 007291f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007291f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007291f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007291f0 bytes 292d2591
+ 007291f0 bytes 29592791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-108e500fbcf36d93e067bd0f16c740e6"></a>

### [`007292d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/007292d8.md) → [`007292d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/007292d8.md) FUN_007292d8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`007259f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00725/007259f0.md) [`00726b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00726/00726b58.md) [`00750e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00750/00750e68.md) [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) [`007bd244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bd244.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 7件 [`007259f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00725/007259f0.md) [`00726b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00726/00726b58.md) [`00750e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00750/00750e68.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) [`007bd244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bd/007bd244.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "007292e4",
      "incomplete_value": false,
      "site": "007292e8",
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
      "definition_site": "007292e4",
      "incomplete_value": false,
      "site": "007292e8",
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
      "007292e4",
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
      "007292e4",
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

- 旧版 [`007292e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/007292d8.md#insn-007292e4)
- 新版 `007292e4`（命令位置の公開資料なし）

~~~diff
- 007292e4 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007292e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007292e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007292e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007292e4 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007292e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007292e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007292e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007292e4 bytes 000c0c91
+ 007292e4 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33a96a10b808b3c7ae90d3d5539a864e"></a>

### [`007292ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/007292ec.md) → [`007292ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/007292ec.md) _INIT_128

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00729328",
      "incomplete_value": true,
      "site": "00729344",
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
      "definition_site": "00729328",
      "incomplete_value": true,
      "site": "00729344",
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
      "definition_site": "0072936c",
      "incomplete_value": true,
      "site": "00729388",
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
      "definition_site": "0072936c",
      "incomplete_value": true,
      "site": "00729388",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0072938c",
      "incomplete_value": true,
      "site": "007293a4",
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
      "definition_site": "0072938c",
      "incomplete_value": true,
      "site": "007293a4",
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
      "00729328",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0072934c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0072936c",
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
      "00729328",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0072934c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0072936c",
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

- 旧版 [`00729318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/007292ec.md#insn-00729318) · [`00729320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/007292ec.md#insn-00729320)
- 新版 `00729318`（命令位置の公開資料なし） · `00729320`（命令位置の公開資料なし）

~~~diff
- 00729318 ["COPY", "tmp:0:8", ["const:e80:8"]]
- 00729318 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00729318 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00729318 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00729318 ["COPY", "tmp:0:8", ["const:ec0:8"]]
+ 00729318 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00729318 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00729318 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00729318 bytes 73023a91
+ 00729318 bytes 73023b91
- 00729320 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00729320 bytes e9dbffd0
+ 00729320 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00729320 bytes e9dbffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf689dd6e606fbe57f8dc6f6829a8608"></a>

### [`0072967c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/0072967c.md) → [`0072967c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/0072967c.md) FUN_0072967c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 16件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00467864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467864.md) [`0072a6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072a/0072a6fc.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 16件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00467864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467864.md) [`0072a6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072a/0072a6fc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.14% / 新版 86.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 14件, `store_destination` 22件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007296c0",
      "incomplete_value": false,
      "site": "007296c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007296c0",
      "incomplete_value": false,
      "site": "007296c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007296b8",
      "incomplete_value": true,
      "site": "007296c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
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
      "definition_site": "007296b8",
      "incomplete_value": true,
      "site": "007296c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:a78:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "007296c4",
      "incomplete_value": true,
      "site": "007296c4",
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
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007296c4",
      "incomplete_value": true,
      "site": "007296c4",
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
            "const:a78:8"
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
      "007296b8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007296bc",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "007296c0",
      "WRITE",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "007296b8",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007296bc",
      "READ",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "007296c0",
      "WRITE",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007296c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/0072967c.md#insn-007296c0) · [`007296c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/0072967c.md#insn-007296c4) · [`007296f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/0072967c.md#insn-007296f4)
- 新版 `007296c0`（命令位置の公開資料なし） · `007296c4`（命令位置の公開資料なし） · `007296f4`（命令位置の公開資料なし）

~~~diff
- 007296c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 007296c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 007296c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa8:8"]]
+ 007296c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 007296c0 bytes 093505f9
+ 007296c0 bytes 095505f9
- 007296c4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
- 007296c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 007296c4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab8:8"]]
+ 007296c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 007296c4 bytes aa3e05f9
+ 007296c4 bytes aa5e05f9
- 007296f4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
- 007296f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 007296f4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab8:8"]]
+ 007296f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 007296f4 bytes b43e05f9
+ 007296f4 bytes b45e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86c494807d3a24fa1b532c05d23badc6"></a>

### [`00729ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/00729ff0.md) → [`00729ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/00729ff0.md) FUN_00729ff0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 17件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`00445d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d88.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 17件 [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`0044592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044592c.md) [`00445d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d88.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.11% / 新版 99.11%

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
      "definition_site": "0072a028",
      "incomplete_value": true,
      "site": "0072a028",
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
      "definition_site": "0072a028",
      "incomplete_value": true,
      "site": "0072a028",
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
      "definition_site": "0072a038",
      "incomplete_value": false,
      "site": "0072a04c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072a038",
      "incomplete_value": false,
      "site": "0072a04c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "definition_site": "0072a040",
      "incomplete_value": false,
      "site": "0072a04c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072a040",
      "incomplete_value": false,
      "site": "0072a04c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:d50:8"
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
      "0072a024",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0072a038",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0072a040",
      "PARAM",
      [
        "storage",
        "00bfad50",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0072a024",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0072a038",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0072a040",
      "PARAM",
      [
        "storage",
        "00bfada0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0072a024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/00729ff0.md#insn-0072a024) · [`0072a038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/00729ff0.md#insn-0072a038) · [`0072a040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/00729ff0.md#insn-0072a040)
- 新版 `0072a024`（命令位置の公開資料なし） · `0072a038`（命令位置の公開資料なし） · `0072a040`（命令位置の公開資料なし）

~~~diff
- 0072a024 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0072a024 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0072a024 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 0072a024 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0072a024 bytes 083d45f9
+ 0072a024 bytes 085d45f9
- 0072a038 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0072a038 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0072a038 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0072a038 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0072a038 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0072a038 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0072a038 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0072a038 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0072a038 bytes 21203991
+ 0072a038 bytes 21603a91
- 0072a040 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 0072a040 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0072a040 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0072a040 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0072a040 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 0072a040 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0072a040 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0072a040 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0072a040 bytes 42403591
+ 0072a040 bytes 42803691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56b328e8673225175e0f66aff807cc47"></a>

### [`0072a6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072a/0072a6fc.md) → [`0072a6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072a/0072a6fc.md) FUN_0072a6fc

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0072967c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/0072967c.md) · 呼出先 16件 [`00459a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459a90.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md)
- 新版 呼出元 1件 [`0072967c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/0072967c.md) · 呼出先 16件 [`00459a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459a90.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.98% / 新版 90.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 22件, `store_destination` 7件, `store_value` 13件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0072a740",
      "incomplete_value": false,
      "site": "0072a744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072a740",
      "incomplete_value": false,
      "site": "0072a744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:d78:8"
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
      "definition_site": "0072a7c4",
      "incomplete_value": true,
      "site": "0072a7d4",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:688:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072a7c4",
      "incomplete_value": true,
      "site": "0072a7d4",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:5fd:8"
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
      "definition_site": "0072a9a4",
      "incomplete_value": true,
      "site": "0072a9b0",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:464:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072a9a4",
      "incomplete_value": true,
      "site": "0072a9b0",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:3ca:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0072a744",
      "DATA",
      [
        "storage",
        "00bfad78",
        null,
        "pointer"
      ]
    ],
    [
      "0072a758",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "0072a7c4",
      "READ",
      [
        "storage",
        "002a35fd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0072a744",
      "DATA",
      [
        "storage",
        "00bfadc8",
        null,
        "pointer"
      ]
    ],
    [
      "0072a758",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "0072a7c4",
      "READ",
      [
        "storage",
        "002a3688",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0072a740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072a/0072a6fc.md#insn-0072a740) · [`0072a748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072a/0072a6fc.md#insn-0072a748)
- 新版 `0072a740`（命令位置の公開資料なし） · `0072a748`（命令位置の公開資料なし）

~~~diff
- 0072a740 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 0072a740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0072a740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0072a740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0072a740 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 0072a740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0072a740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0072a740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0072a740 bytes 08e13591
+ 0072a740 bytes 08213791
- 0072a748 ["COPY", "register:40c8:8", ["const:c25000:8"]]
- 0072a748 bytes d92700f0
+ 0072a748 ["COPY", "register:40c8:8", ["const:c25000:8"]]
+ 0072a748 bytes d92700f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a347622cae385f9d287f1370ed333312"></a>

### [`0072b854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072b/0072b854.md) → [`0072b854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072b/0072b854.md) FUN_0072b854

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0072b94c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072b/0072b94c.md) · 呼出先 3件 [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`0072b94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072b/0072b94c.md) · 呼出先 3件 [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "0072b86c",
      "incomplete_value": false,
      "site": "0072b870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072b86c",
      "incomplete_value": false,
      "site": "0072b870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:d78:8"
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
      "definition_site": "0072b908",
      "incomplete_value": false,
      "site": "0072b90c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072b908",
      "incomplete_value": false,
      "site": "0072b90c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "0072b870",
      "DATA",
      [
        "storage",
        "00bfad78",
        null,
        "pointer"
      ]
    ],
    [
      "0072b90c",
      "DATA",
      [
        "storage",
        "00bf7298",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0072b870",
      "DATA",
      [
        "storage",
        "00bfadc8",
        null,
        "pointer"
      ]
    ],
    [
      "0072b90c",
      "DATA",
      [
        "storage",
        "00bf72e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0072b86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072b/0072b854.md#insn-0072b86c) · [`0072b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072b/0072b854.md#insn-0072b908)
- 新版 `0072b86c`（命令位置の公開資料なし） · `0072b908`（命令位置の公開資料なし）

~~~diff
- 0072b86c ["COPY", "tmp:0:8", ["const:d78:8"]]
- 0072b86c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0072b86c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0072b86c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0072b86c ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 0072b86c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0072b86c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0072b86c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0072b86c bytes 08e13591
+ 0072b86c bytes 08213791
- 0072b908 ["COPY", "tmp:0:8", ["const:298:8"]]
- 0072b908 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0072b908 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0072b908 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0072b908 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 0072b908 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0072b908 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0072b908 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0072b908 bytes 08610a91
+ 0072b908 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ccb4da5d109666da2d59439f12d038e"></a>

### [`0072b970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072b/0072b970.md) → [`0072b970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072b/0072b970.md) _INIT_129

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0072b9ac",
      "incomplete_value": true,
      "site": "0072b9c8",
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
      "definition_site": "0072b9ac",
      "incomplete_value": true,
      "site": "0072b9c8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0072b9f0",
      "incomplete_value": true,
      "site": "0072ba0c",
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
      "definition_site": "0072b9f0",
      "incomplete_value": true,
      "site": "0072ba0c",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0072ba2c",
      "incomplete_value": true,
      "site": "0072ba48",
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
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:36c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072ba2c",
      "incomplete_value": true,
      "site": "0072ba48",
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
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:36e:8"
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
      "0072b9ac",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0072b9d0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0072b9f0",
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
      "0072b9ac",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0072b9d0",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0072b9f0",
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

- 旧版 [`0072b99c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072b/0072b970.md#insn-0072b99c) · [`0072b9a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072b/0072b970.md#insn-0072b9a4)
- 新版 `0072b99c`（命令位置の公開資料なし） · `0072b9a4`（命令位置の公開資料なし）

~~~diff
- 0072b99c ["COPY", "tmp:0:8", ["const:e98:8"]]
- 0072b99c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0072b99c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0072b99c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0072b99c ["COPY", "tmp:0:8", ["const:ed8:8"]]
+ 0072b99c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0072b99c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0072b99c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0072b99c bytes 73623a91
+ 0072b99c bytes 73623b91
- 0072b9a4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0072b9a4 bytes e9dbff90
+ 0072b9a4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0072b9a4 bytes e9dbff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dd5de1484900b9bacce1ef6b26d54ba"></a>

### [`0072bd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072b/0072bd00.md) → [`0072bd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072b/0072bd00.md) _INIT_130

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
      "definition_site": "0072bd3c",
      "incomplete_value": true,
      "site": "0072bd58",
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
      "definition_site": "0072bd3c",
      "incomplete_value": true,
      "site": "0072bd58",
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
      "definition_site": "0072bd60",
      "incomplete_value": true,
      "site": "0072bd7c",
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
      "definition_site": "0072bd60",
      "incomplete_value": true,
      "site": "0072bd7c",
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
      "definition_site": "0072bd80",
      "incomplete_value": true,
      "site": "0072bd9c",
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
      "definition_site": "0072bd80",
      "incomplete_value": true,
      "site": "0072bd9c",
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
      "0072bd3c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0072bd60",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0072bd80",
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
      "0072bd3c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0072bd60",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0072bd80",
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

- 旧版 [`0072bd2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072b/0072bd00.md#insn-0072bd2c) · [`0072bd34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072b/0072bd00.md#insn-0072bd34)
- 新版 `0072bd2c`（命令位置の公開資料なし） · `0072bd34`（命令位置の公開資料なし）

~~~diff
- 0072bd2c ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 0072bd2c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0072bd2c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0072bd2c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0072bd2c ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 0072bd2c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0072bd2c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0072bd2c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0072bd2c bytes 73c23a91
+ 0072bd2c bytes 73c23b91
- 0072bd34 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0072bd34 bytes e9dbff90
+ 0072bd34 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0072bd34 bytes e9dbff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7f03681724eef0da1be05418a13822c"></a>

### [`0072c090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072c/0072c090.md) → [`0072c090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072c/0072c090.md) FUN_0072c090

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 10件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`0080735c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/0080735c.md) [`008a4544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a4/008a4544.md) [`008cb758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb758.md) [`008cd6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd6e0.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 10件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`0080735c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/0080735c.md) [`008a4544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4544.md) [`008cb758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cb/008cb758.md) [`008cd6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cd/008cd6e0.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.75% / 新版 90.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 61件, `store_destination` 7件, `store_value` 36件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0072c0d0",
      "incomplete_value": false,
      "site": "0072c0d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072c0d0",
      "incomplete_value": false,
      "site": "0072c0d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:d98:8"
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
      "definition_site": "0072c1a8",
      "incomplete_value": true,
      "site": "0072c1a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:937:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072c1a8",
      "incomplete_value": true,
      "site": "0072c1a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8ac:8"
              ]
            ]
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
      "definition_site": "0072c1c0",
      "incomplete_value": true,
      "site": "0072c1c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:73a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072c1c0",
      "incomplete_value": true,
      "site": "0072c1c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:73c:8"
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
      "0072c0d8",
      "DATA",
      [
        "storage",
        "00bfad98",
        null,
        "pointer"
      ]
    ],
    [
      "0072c178",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "0072c198",
      "READ",
      [
        "storage",
        "002a08ac",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0072c0d8",
      "DATA",
      [
        "storage",
        "00bfade8",
        null,
        "pointer"
      ]
    ],
    [
      "0072c178",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "0072c198",
      "READ",
      [
        "storage",
        "002a0937",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0072c0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072c/0072c090.md#insn-0072c0d0) · [`0072c170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072c/0072c090.md#insn-0072c170) · [`0072c194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072c/0072c090.md#insn-0072c194)
- 新版 `0072c0d0`（命令位置の公開資料なし） · `0072c170`（命令位置の公開資料なし） · `0072c194`（命令位置の公開資料なし）

~~~diff
- 0072c0d0 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 0072c0d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0072c0d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0072c0d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0072c0d0 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 0072c0d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0072c0d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0072c0d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0072c0d0 bytes 08613691
+ 0072c0d0 bytes 08a13791
- 0072c170 ["COPY", "tmp:0:8", ["const:38:8"]]
- 0072c170 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 0072c170 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 0072c170 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 0072c170 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0072c170 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 0072c170 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 0072c170 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 0072c170 bytes 39e30091
+ 0072c170 bytes 39e30191
- 0072c194 ["COPY", "tmp:0:8", ["const:8ac:8"]]
- 0072c194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0072c194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0072c194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0072c194 ["COPY", "tmp:0:8", ["const:937:8"]]
+ 0072c194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0072c194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0072c194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0072c194 bytes 08b12291
+ 0072c194 bytes 08dd2491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9edea011f08efa2f1001ddb0aa676c0"></a>

### [`0072dfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072d/0072dfbc.md) → [`0072dfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072d/0072dfbc.md) FUN_0072dfbc

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 7件 [`0072c090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072c/0072c090.md) [`007802c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00780/007802c0.md) [`008895f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00889/008895f4.md) [`008acbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ac/008acbf0.md) [`008c6e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6e18.md) · 呼出先 10件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00657e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00657/00657e7c.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)
- 新版 呼出元 7件 [`0072c090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072c/0072c090.md) [`007802c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00780/007802c0.md) [`008895f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/008895f4.md) [`008acbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008acbf0.md) [`008c6e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c6/008c6e18.md) · 呼出先 10件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00657e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/00657e7c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 75.44% / 新版 75.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0072dfec",
      "incomplete_value": false,
      "site": "0072dff0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072dfec",
      "incomplete_value": false,
      "site": "0072dff0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "definition_site": "0072e030",
      "incomplete_value": true,
      "site": "0072e030",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:291000:8"
              ],
              [
                "leaf",
                "const:d9c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072e030",
      "incomplete_value": true,
      "site": "0072e030",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:291000:8"
              ],
              [
                "leaf",
                "const:e29:8"
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
      "definition_site": "0072e048",
      "incomplete_value": true,
      "site": "0072e048",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ae000:8"
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
      "definition_site": "0072e048",
      "incomplete_value": true,
      "site": "0072e048",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:e44:8"
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
      "0072dff0",
      "DATA",
      [
        "storage",
        "00bfadb8",
        null,
        "pointer"
      ]
    ],
    [
      "0072e000",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "0072e020",
      "READ",
      [
        "storage",
        "00291e29",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0072dff0",
      "DATA",
      [
        "storage",
        "00bfae08",
        null,
        "pointer"
      ]
    ],
    [
      "0072e000",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "0072e020",
      "READ",
      [
        "storage",
        "00291d9c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0072dfec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072d/0072dfbc.md#insn-0072dfec) · [`0072dff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072d/0072dfbc.md#insn-0072dff4)
- 新版 `0072dfec`（命令位置の公開資料なし） · `0072dff4`（命令位置の公開資料なし）

~~~diff
- 0072dfec ["COPY", "tmp:0:8", ["const:db8:8"]]
- 0072dfec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0072dfec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0072dfec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0072dfec ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 0072dfec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0072dfec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0072dfec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0072dfec bytes 08e13691
+ 0072dfec bytes 08213891
- 0072dff4 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 0072dff4 bytes c8270090
+ 0072dff4 ["COPY", "register:4040:8", ["const:c25000:8"]]
+ 0072dff4 bytes c8270090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8abc9808bf957793513c773d2e7bdd6"></a>

### [`0072e62c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072e/0072e62c.md) → [`0072e62c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072e/0072e62c.md) FUN_0072e62c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 7件 [`00608668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00608/00608668.md) [`00651720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00651/00651720.md) [`00654084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00654/00654084.md) [`008f06a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f0/008f06a0.md) [`00988788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00988/00988788.md) · 呼出先 21件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c1dc.md) [`0044c80c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c80c.md)
- 新版 呼出元 7件 [`00608668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608668.md) [`00651720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00651/00651720.md) [`00654084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00654/00654084.md) [`008f06a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f0/008f06a0.md) [`00988788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00988/00988788.md) · 呼出先 21件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md) [`0044c80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c80c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.88% / 新版 93.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0072e8ec",
      "incomplete_value": true,
      "site": "0072e8fc",
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
                "const:db7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072e8ec",
      "incomplete_value": true,
      "site": "0072e8fc",
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
                "const:e44:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 56,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0072e9e8",
      "incomplete_value": true,
      "site": "0072e9f8",
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
                "const:c84:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072e9e8",
      "incomplete_value": true,
      "site": "0072e9f8",
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
                "const:d11:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 63,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0072ece0",
      "incomplete_value": false,
      "site": "0072ece0",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072ece0",
      "incomplete_value": false,
      "site": "0072ece0",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 80,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0072e68c",
      "PARAM",
      [
        "storage",
        "002a5957",
        null,
        "string"
      ]
    ],
    [
      "0072e69c",
      "PARAM",
      [
        "storage",
        "002a37d2",
        null,
        null
      ]
    ],
    [
      "0072e7d0",
      "READ",
      [
        "storage",
        "0029f8f4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0072e68c",
      "PARAM",
      [
        "storage",
        "002a59e2",
        null,
        "string"
      ]
    ],
    [
      "0072e69c",
      "PARAM",
      [
        "storage",
        "002a385d",
        null,
        null
      ]
    ],
    [
      "0072e7d0",
      "READ",
      [
        "storage",
        "0029f97f",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0072e68c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072e/0072e62c.md#insn-0072e68c) · [`0072e69c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072e/0072e62c.md#insn-0072e69c) · [`0072e7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072e/0072e62c.md#insn-0072e7c4)
- 新版 `0072e68c`（命令位置の公開資料なし） · `0072e69c`（命令位置の公開資料なし） · `0072e7c4`（命令位置の公開資料なし）

~~~diff
- 0072e68c ["COPY", "tmp:0:8", ["const:957:8"]]
- 0072e68c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0072e68c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0072e68c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0072e68c ["COPY", "tmp:0:8", ["const:9e2:8"]]
+ 0072e68c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0072e68c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0072e68c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0072e68c bytes 215c2591
+ 0072e68c bytes 21882791
- 0072e69c ["COPY", "tmp:0:8", ["const:7d2:8"]]
- 0072e69c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0072e69c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0072e69c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0072e69c ["COPY", "tmp:0:8", ["const:85d:8"]]
+ 0072e69c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0072e69c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0072e69c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0072e69c bytes 21481f91
+ 0072e69c bytes 21742191
- 0072e7c4 ["COPY", "tmp:0:8", ["const:8f4:8"]]
- 0072e7c4 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 0072e7c4 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 0072e7c4 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 0072e7c4 ["COPY", "tmp:0:8", ["const:97f:8"]]
+ 0072e7c4 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 0072e7c4 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 0072e7c4 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 0072e7c4 bytes 18d32391
+ 0072e7c4 bytes 18ff2591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17c9bb4a8f0c48f0e66c7d3919d6540d"></a>

### [`007317b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00731/007317b0.md) → [`007317b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00731/007317b0.md) FUN_007317b0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00733548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00733/00733548.md) · 呼出先 32件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`005dfdec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005df/005dfdec.md) [`006f1e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f1e2c.md) [`006f23b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f2/006f23b4.md)
- 新版 呼出元 1件 [`00733548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00733/00733548.md) · 呼出先 32件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`005dfdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005df/005dfdec.md) [`006f1e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1e2c.md) [`006f23b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f23b4.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 98.03% / 新版 98.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件, `store_value` 12件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007318c8",
      "incomplete_value": false,
      "site": "007318d0",
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
            "const:72f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007318c8",
      "incomplete_value": false,
      "site": "007318d0",
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
            "const:6a4:8"
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
      "definition_site": "007318f0",
      "incomplete_value": false,
      "site": "007318fc",
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
            "const:7ec:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007318f0",
      "incomplete_value": false,
      "site": "007318fc",
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
            "const:761:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00732464",
      "incomplete_value": true,
      "site": "00732464",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00732464",
      "incomplete_value": true,
      "site": "00732464",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:758:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 140,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007318d0",
      "DATA",
      [
        "storage",
        "0029e6a4",
        null,
        "string"
      ]
    ],
    [
      "007318fc",
      "DATA",
      [
        "storage",
        "002a2761",
        null,
        "string"
      ]
    ],
    [
      "00731928",
      "DATA",
      [
        "storage",
        "002a1731",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007318d0",
      "DATA",
      [
        "storage",
        "0029e72f",
        null,
        "string"
      ]
    ],
    [
      "007318fc",
      "DATA",
      [
        "storage",
        "002a27ec",
        null,
        "string"
      ]
    ],
    [
      "00731928",
      "DATA",
      [
        "storage",
        "002a17bc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007318c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00731/007317b0.md#insn-007318c8) · [`007318cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00731/007317b0.md#insn-007318cc)
- 新版 `007318c8`（命令位置の公開資料なし） · `007318cc`（命令位置の公開資料なし）

~~~diff
- 007318c8 ["COPY", "tmp:0:8", ["const:6a4:8"]]
- 007318c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007318c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007318c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007318c8 ["COPY", "tmp:0:8", ["const:72f:8"]]
+ 007318c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007318c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007318c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007318c8 bytes 08911a91
+ 007318c8 bytes 08bd1c91
- 007318cc ["COPY", "tmp:0:8", ["const:80:8"]]
- 007318cc ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 007318cc ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 007318cc ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 007318cc bytes f4030291
+ 007318cc ["COPY", "tmp:0:8", ["const:80:8"]]
+ 007318cc ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
+ 007318cc ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
+ 007318cc ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
+ 007318cc bytes f4030291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc681af3ae3a929478e1f7458955c6f1"></a>

### [`00733548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00733/00733548.md) → [`00733548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00733/00733548.md) FUN_00733548

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 4件 [`005e8d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e8/005e8d4c.md) [`00695904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md) [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`007bdafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bdafc.md) · 呼出先 42件 [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`005188a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/005188a4.md) [`00574784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574784.md) [`00574810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574810.md) [`005748a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/005748a0.md)
- 新版 呼出元 4件 [`005e8d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e8/005e8d4c.md) [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`007bdafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bd/007bdafc.md) · 呼出先 42件 [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`005188a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005188a4.md) [`00574784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574784.md) [`00574810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574810.md) [`005748a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/005748a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.08% / 新版 99.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0073371c",
      "incomplete_value": false,
      "site": "0073371c",
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
            "const:79d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073371c",
      "incomplete_value": false,
      "site": "0073371c",
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
            "const:712:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00733780",
      "incomplete_value": false,
      "site": "00733780",
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
            "const:d5d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00733780",
      "incomplete_value": false,
      "site": "00733780",
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
            "const:dea:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007338c8",
      "incomplete_value": false,
      "site": "007338c8",
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
            "const:79d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007338c8",
      "incomplete_value": false,
      "site": "007338c8",
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
            "const:712:8"
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
      "0073371c",
      "DATA",
      [
        "storage",
        "0029d712",
        null,
        null
      ]
    ],
    [
      "00733780",
      "DATA",
      [
        "storage",
        "00291dea",
        null,
        null
      ]
    ],
    [
      "007338c8",
      "DATA",
      [
        "storage",
        "0029d712",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0073371c",
      "DATA",
      [
        "storage",
        "0029d79d",
        null,
        null
      ]
    ],
    [
      "00733780",
      "DATA",
      [
        "storage",
        "00291d5d",
        null,
        null
      ]
    ],
    [
      "007338c8",
      "DATA",
      [
        "storage",
        "0029d79d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00733714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00733/00733548.md#insn-00733714) · [`0073377c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00733/00733548.md#insn-0073377c) · [`007338c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00733/00733548.md#insn-007338c0)
- 新版 `00733714`（命令位置の公開資料なし） · `0073377c`（命令位置の公開資料なし） · `007338c0`（命令位置の公開資料なし）

~~~diff
- 00733714 ["COPY", "tmp:0:8", ["const:712:8"]]
- 00733714 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00733714 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00733714 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00733714 ["COPY", "tmp:0:8", ["const:79d:8"]]
+ 00733714 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00733714 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00733714 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00733714 bytes 08491c91
+ 00733714 bytes 08751e91
- 0073377c ["COPY", "tmp:0:8", ["const:dea:8"]]
- 0073377c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0073377c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0073377c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0073377c ["COPY", "tmp:0:8", ["const:d5d:8"]]
+ 0073377c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0073377c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0073377c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0073377c bytes 08a93791
+ 0073377c bytes 08753591
- 007338c0 ["COPY", "tmp:0:8", ["const:712:8"]]
- 007338c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007338c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007338c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007338c0 ["COPY", "tmp:0:8", ["const:79d:8"]]
+ 007338c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007338c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007338c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007338c0 bytes 08491c91
+ 007338c0 bytes 08751e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e2849a22baf0ce764d62d039bec3d7c"></a>

### [`00734374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/00734374.md) → [`00734374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/00734374.md) FUN_00734374

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00733548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00733/00733548.md) [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) · 呼出先 14件 [`0042bbc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bbc8.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`00574784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574784.md)
- 新版 呼出元 2件 [`00733548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00733/00733548.md) [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · 呼出先 14件 [`0042bbc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bbc8.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`00574784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574784.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.90% / 新版 97.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007344e8",
      "incomplete_value": false,
      "site": "00734518",
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
            "const:915:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007344e8",
      "incomplete_value": false,
      "site": "00734518",
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
            "const:88a:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007343bc",
      "READ",
      [
        "storage",
        "002a3856",
        null,
        "string"
      ]
    ],
    [
      "007343bc",
      "READ",
      [
        "storage",
        "002a3866",
        null,
        "string"
      ]
    ],
    [
      "007343d0",
      "READ",
      [
        "storage",
        "002a3873",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007343bc",
      "READ",
      [
        "storage",
        "002a38e1",
        null,
        "string"
      ]
    ],
    [
      "007343bc",
      "READ",
      [
        "storage",
        "002a38f1",
        null,
        "string"
      ]
    ],
    [
      "007343d0",
      "READ",
      [
        "storage",
        "002a38fe",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007343b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/00734374.md#insn-007343b4) · [`007344e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/00734374.md#insn-007344e0) · [`007344e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/00734374.md#insn-007344e8)
- 新版 `007343b4`（命令位置の公開資料なし） · `007344e0`（命令位置の公開資料なし） · `007344e8`（命令位置の公開資料なし）

~~~diff
- 007343b4 ["COPY", "tmp:0:8", ["const:7d6:8"]]
- 007343b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007343b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007343b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007343b4 ["COPY", "tmp:0:8", ["const:861:8"]]
+ 007343b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007343b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007343b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007343b4 bytes 08591f91
+ 007343b4 bytes 08852191
- 007344e0 ["COPY", "register:4018:8", ["const:4caf:8"]]
+ 007344e0 ["COPY", "register:4018:8", ["const:4cb0:8"]]
- 007344e0 bytes e3958952
+ 007344e0 bytes 03968952
- 007344e8 ["COPY", "tmp:0:8", ["const:88a:8"]]
- 007344e8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007344e8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007344e8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007344e8 ["COPY", "tmp:0:8", ["const:915:8"]]
+ 007344e8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007344e8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007344e8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007344e8 bytes 42282291
+ 007344e8 bytes 42542491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8c3ac95e0e82d67e4b73cb11c92e8d4"></a>

### [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) → [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) FUN_0073496c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 174件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md)
- 新版 呼出元 2件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 174件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.66% / 新版 95.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 62件, `call_target` 2件, `store_destination` 28件, `store_value` 29件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00734a40",
      "incomplete_value": true,
      "site": "00734a40",
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
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00734a40",
      "incomplete_value": true,
      "site": "00734a40",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00734a44",
      "incomplete_value": true,
      "site": "00734a44",
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
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00734a44",
      "incomplete_value": true,
      "site": "00734a44",
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
            "const:a78:8"
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
      "definition_site": "00734a74",
      "incomplete_value": true,
      "site": "00734a74",
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
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00734a74",
      "incomplete_value": true,
      "site": "00734a74",
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
            "const:a78:8"
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
      "00734a34",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00734a38",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00734a40",
      "WRITE",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00734a34",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00734a38",
      "READ",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00734a40",
      "WRITE",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00734a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md#insn-00734a40) · [`00734a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md#insn-00734a44) · [`00734a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md#insn-00734a74)
- 新版 `00734a40`（命令位置の公開資料なし） · `00734a44`（命令位置の公開資料なし） · `00734a74`（命令位置の公開資料なし）

~~~diff
- 00734a40 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 00734a40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00734a40 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa8:8"]]
+ 00734a40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00734a40 bytes 093505f9
+ 00734a40 bytes 095505f9
- 00734a44 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
- 00734a44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00734a44 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab8:8"]]
+ 00734a44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00734a44 bytes aa3e05f9
+ 00734a44 bytes aa5e05f9
- 00734a74 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
- 00734a74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 00734a74 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab8:8"]]
+ 00734a74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00734a74 bytes b43e05f9
+ 00734a74 bytes b45e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3f03b94d99a0862723ff0cb560ed7ee"></a>

### [`00739a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00739/00739a10.md) → [`00739a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00739/00739a10.md) FUN_00739a10

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) · 呼出先 19件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0053f81c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053f81c.md) [`0062d23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d23c.md) [`006fdbdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fdbdc.md)
- 新版 呼出元 1件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · 呼出先 19件 [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0053f81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f81c.md) [`0062d23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d23c.md) [`006fdbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdbdc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.62% / 新版 96.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00739af8",
      "incomplete_value": true,
      "site": "00739b00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00739af8",
      "incomplete_value": true,
      "site": "00739b00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:770:8"
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
      "00739af8",
      "READ",
      [
        "storage",
        "00c1b770",
        null,
        "pointer"
      ]
    ],
    [
      "00739af8",
      "PARAM",
      [
        "storage",
        "0109e4b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00739b78",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00739af8",
      "READ",
      [
        "storage",
        "00c1b7c0",
        null,
        "pointer"
      ]
    ],
    [
      "00739af8",
      "PARAM",
      [
        "storage",
        "0109e4f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00739b78",
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00739af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00739/00739a10.md#insn-00739af8) · [`00739b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00739/00739a10.md#insn-00739b78) · [`00739b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00739/00739a10.md#insn-00739b88)
- 新版 `00739af8`（命令位置の公開資料なし） · `00739b78`（命令位置の公開資料なし） · `00739b88`（命令位置の公開資料なし）

~~~diff
- 00739af8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:770:8"]]
- 00739af8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00739af8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:7c0:8"]]
+ 00739af8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00739af8 bytes 21b843f9
+ 00739af8 bytes 21e043f9
- 00739b78 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:e60:8"]]
- 00739b78 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00739b78 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:eb0:8"]]
+ 00739b78 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 00739b78 bytes f73247f9
+ 00739b78 bytes f75a47f9
- 00739b88 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00739b88 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00739b88 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00739b88 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00739b88 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00739b88 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00739b88 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00739b88 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00739b88 bytes 94e20091
+ 00739b88 bytes 94e20191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ceddc9882d1395a1fa11ac51e63bb624"></a>

### [`00739da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00739/00739da8.md) → [`00739da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00739/00739da8.md) FUN_00739da8

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`007693f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00769/007693f4.md) · 呼出先 9件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00700be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00700/00700be0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)
- 新版 呼出元 2件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`007693f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00769/007693f4.md) · 呼出先 9件 [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00700be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00700/00700be0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.63% / 新版 89.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00739fd4",
      "incomplete_value": false,
      "site": "00739fd4",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00739fd4",
      "incomplete_value": false,
      "site": "00739fd4",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00739fd8",
      "incomplete_value": false,
      "site": "00739fd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00739fd8",
      "incomplete_value": false,
      "site": "00739fd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00739fd4",
      "incomplete_value": false,
      "site": "00739fd8",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00739fd4",
      "incomplete_value": false,
      "site": "00739fd8",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
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
      "00739e98",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "00739eec",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00739f00",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00739e98",
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "00739eec",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00739f00",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00739e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00739/00739da8.md#insn-00739e98) · [`00739ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00739/00739da8.md#insn-00739ee8) · [`00739f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00739/00739da8.md#insn-00739f00)
- 新版 `00739e98`（命令位置の公開資料なし） · `00739ee8`（命令位置の公開資料なし） · `00739f00`（命令位置の公開資料なし）

~~~diff
- 00739e98 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:e60:8"]]
- 00739e98 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00739e98 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:eb0:8"]]
+ 00739e98 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00739e98 bytes 183347f9
+ 00739e98 bytes 185b47f9
- 00739ee8 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00739ee8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00739ee8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00739ee8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00739ee8 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00739ee8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00739ee8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00739ee8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00739ee8 bytes 08e10091
+ 00739ee8 bytes 08e10191
- 00739f00 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00739f00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00739f00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00739f00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00739f00 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 00739f00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00739f00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00739f00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00739f00 bytes 00000091
+ 00739f00 bytes 00000191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

