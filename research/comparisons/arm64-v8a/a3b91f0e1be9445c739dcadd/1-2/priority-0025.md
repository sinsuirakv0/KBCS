# v15.7.3 → v15.7.4 · 最優先の変更候補 (25)

[一覧の目次](README.md)

<a id="compare-7ddab051a7d01a89ebaabb335b68bf26"></a>

### [`005f5668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f5/005f5668.md) → [`005f5668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f5/005f5668.md) FUN_005f5668

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005f4a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f4/005f4a84.md) [`005f5668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f5/005f5668.md) [`00702240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00702/00702240.md) [`007bebf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007bebf8.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041e778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e778.md)
- 新版 呼出元 4件 [`005f4a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f4/005f4a84.md) [`005f5668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f5/005f5668.md) [`00702240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/00702240.md) [`007bebf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007be/007bebf8.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041e778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005f57c4",
      "incomplete_value": false,
      "site": "005f57cc",
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
      "definition_site": "005f57c4",
      "incomplete_value": false,
      "site": "005f57cc",
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
      "definition_site": "005f57e8",
      "incomplete_value": false,
      "site": "005f57f4",
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
      "definition_site": "005f57e8",
      "incomplete_value": false,
      "site": "005f57f4",
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
      "definition_site": "005f591c",
      "incomplete_value": false,
      "site": "005f5924",
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
      "definition_site": "005f591c",
      "incomplete_value": false,
      "site": "005f5924",
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
      "005f57c4",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "005f57e8",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "005f591c",
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
      "005f57c4",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "005f57e8",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "005f591c",
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

- 旧版 [`005f57c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f5/005f5668.md#insn-005f57c4) · [`005f57e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f5/005f5668.md#insn-005f57e8) · [`005f591c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f5/005f5668.md#insn-005f591c)
- 新版 [`005f57c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f5/005f5668.md#insn-005f57c4) · [`005f57e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f5/005f5668.md#insn-005f57e8) · [`005f591c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f5/005f5668.md#insn-005f591c)

~~~diff
- 005f57c4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005f57c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005f57c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005f57c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005f57c4 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 005f57c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005f57c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005f57c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005f57c4 bytes 21280c91
+ 005f57c4 bytes 21900e91
- 005f57e8 ["COPY", "tmp:0:8", ["const:919:8"]]
- 005f57e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005f57e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005f57e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005f57e8 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 005f57e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005f57e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005f57e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005f57e8 bytes 21642491
+ 005f57e8 bytes 21142291
- 005f591c ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 005f591c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005f591c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005f591c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005f591c ["COPY", "tmp:0:8", ["const:379:8"]]
+ 005f591c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005f591c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005f591c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005f591c bytes 21b80b91
+ 005f591c bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-893e114f79aca69b918ce7abe4c3f089"></a>

### [`005f6340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f6/005f6340.md) → [`005f6340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f6/005f6340.md) FUN_005f6340

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005f610c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f6/005f610c.md) [`005f6340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f6/005f6340.md) [`00ad1c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad1c34.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`005f610c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f6/005f610c.md) [`005f6340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f6/005f6340.md) [`00ad1c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad1/00ad1c78.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.05% / 新版 99.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005f64b4",
      "incomplete_value": false,
      "site": "005f64bc",
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
      "definition_site": "005f64b4",
      "incomplete_value": false,
      "site": "005f64bc",
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
      "definition_site": "005f6568",
      "incomplete_value": false,
      "site": "005f6570",
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
      "definition_site": "005f6568",
      "incomplete_value": false,
      "site": "005f6570",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005f6634",
      "incomplete_value": false,
      "site": "005f6644",
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
      "definition_site": "005f6634",
      "incomplete_value": false,
      "site": "005f6644",
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
      "005f64b4",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "005f6568",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "005f6580",
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
      "005f64b4",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "005f6568",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "005f6580",
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

- 旧版 [`005f64b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f6/005f6340.md#insn-005f64b4) · [`005f6568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f6/005f6340.md#insn-005f6568) · [`005f6580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f6/005f6340.md#insn-005f6580)
- 新版 [`005f64b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f6/005f6340.md#insn-005f64b4) · [`005f6568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f6/005f6340.md#insn-005f6568) · [`005f6580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f6/005f6340.md#insn-005f6580)

~~~diff
- 005f64b4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005f64b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005f64b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005f64b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005f64b4 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 005f64b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005f64b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005f64b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005f64b4 bytes 21280c91
+ 005f64b4 bytes 21900e91
- 005f6568 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 005f6568 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005f6568 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005f6568 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005f6568 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 005f6568 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005f6568 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005f6568 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005f6568 bytes 21b80b91
+ 005f6568 bytes 21e40d91
- 005f6580 ["COPY", "tmp:0:8", ["const:919:8"]]
- 005f6580 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005f6580 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005f6580 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005f6580 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 005f6580 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005f6580 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005f6580 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005f6580 bytes 21642491
+ 005f6580 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39077c13c4ec97a69692b74c32553a70"></a>

### [`005f714c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f714c.md) → [`005f714c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f714c.md) FUN_005f714c

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
      "definition_site": "005f7160",
      "incomplete_value": false,
      "site": "005f7164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f7160",
      "incomplete_value": false,
      "site": "005f7164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:a50:8"
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
      "005f7164",
      "DATA",
      [
        "storage",
        "00bf4a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f7164",
      "DATA",
      [
        "storage",
        "00bf4aa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f7160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f714c.md#insn-005f7160)
- 新版 [`005f7160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f714c.md#insn-005f7160)

~~~diff
- 005f7160 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 005f7160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f7160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f7160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f7160 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 005f7160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f7160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f7160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f7160 bytes 08412991
+ 005f7160 bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af663450f5a6ed99c950ab9c8dcbd431"></a>

### [`005f7170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7170.md) → [`005f7170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7170.md) FUN_005f7170

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
      "definition_site": "005f7174",
      "incomplete_value": false,
      "site": "005f7178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f7174",
      "incomplete_value": false,
      "site": "005f7178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:a50:8"
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
      "005f7178",
      "DATA",
      [
        "storage",
        "00bf4a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f7178",
      "DATA",
      [
        "storage",
        "00bf4aa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f7174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7170.md#insn-005f7174)
- 新版 [`005f7174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7170.md#insn-005f7174)

~~~diff
- 005f7174 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 005f7174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f7174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f7174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f7174 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 005f7174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f7174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f7174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f7174 bytes 08412991
+ 005f7174 bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0313f590325f7209b729ba0f6626b4de"></a>

### [`005f71fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f71fc.md) → [`005f71fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f71fc.md) FUN_005f71fc

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
      "definition_site": "005f7220",
      "incomplete_value": false,
      "site": "005f7220",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f7220",
      "incomplete_value": false,
      "site": "005f7220",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
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
      "005f7220",
      "DATA",
      [
        "storage",
        "00bf4ad0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f7220",
      "DATA",
      [
        "storage",
        "00bf4b20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f721c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f71fc.md#insn-005f721c)
- 新版 [`005f721c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f71fc.md#insn-005f721c)

~~~diff
- 005f721c ["COPY", "tmp:0:8", ["const:ad0:8"]]
- 005f721c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f721c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f721c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f721c ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 005f721c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f721c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f721c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f721c bytes 08412b91
+ 005f721c bytes 08812c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40263a1ad56494c11a1a4b7d72a2b804"></a>

### [`005f7230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7230.md) → [`005f7230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7230.md) FUN_005f7230

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
      "definition_site": "005f723c",
      "incomplete_value": false,
      "site": "005f723c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f723c",
      "incomplete_value": false,
      "site": "005f723c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
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
      "005f723c",
      "DATA",
      [
        "storage",
        "00bf4ad0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f723c",
      "DATA",
      [
        "storage",
        "00bf4b20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f7238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7230.md#insn-005f7238)
- 新版 [`005f7238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7230.md#insn-005f7238)

~~~diff
- 005f7238 ["COPY", "tmp:0:8", ["const:ad0:8"]]
- 005f7238 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005f7238 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005f7238 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005f7238 ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 005f7238 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005f7238 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005f7238 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005f7238 bytes 29412b91
+ 005f7238 bytes 29812c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bec3f676c23652eb20ffa98306fedad4"></a>

### [`005f7290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7290.md) → [`005f7290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7290.md) FUN_005f7290

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
      "definition_site": "005f72a4",
      "incomplete_value": false,
      "site": "005f72a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f72a4",
      "incomplete_value": false,
      "site": "005f72a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:b60:8"
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
      "005f72a8",
      "DATA",
      [
        "storage",
        "00bf4b60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f72a8",
      "DATA",
      [
        "storage",
        "00bf4bb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f72a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7290.md#insn-005f72a4)
- 新版 [`005f72a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7290.md#insn-005f72a4)

~~~diff
- 005f72a4 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 005f72a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f72a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f72a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f72a4 ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 005f72a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f72a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f72a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f72a4 bytes 08812d91
+ 005f72a4 bytes 08c12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7200fe6605e02abe410192057d997d1"></a>

### [`005f72b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f72b4.md) → [`005f72b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f72b4.md) FUN_005f72b4

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
      "definition_site": "005f72b8",
      "incomplete_value": false,
      "site": "005f72bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f72b8",
      "incomplete_value": false,
      "site": "005f72bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:b60:8"
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
      "005f72bc",
      "DATA",
      [
        "storage",
        "00bf4b60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f72bc",
      "DATA",
      [
        "storage",
        "00bf4bb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f72b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f72b4.md#insn-005f72b8)
- 新版 [`005f72b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f72b4.md#insn-005f72b8)

~~~diff
- 005f72b8 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 005f72b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f72b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f72b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f72b8 ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 005f72b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f72b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f72b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f72b8 bytes 08812d91
+ 005f72b8 bytes 08c12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0498232dba314957d81c11c4ae0f437"></a>

### [`005f7428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7428.md) → [`005f7428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7428.md) FUN_005f7428

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
      "definition_site": "005f743c",
      "incomplete_value": false,
      "site": "005f7440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f743c",
      "incomplete_value": false,
      "site": "005f7440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:be0:8"
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
      "005f7440",
      "DATA",
      [
        "storage",
        "00bf4be0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f7440",
      "DATA",
      [
        "storage",
        "00bf4c30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f743c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7428.md#insn-005f743c)
- 新版 [`005f743c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7428.md#insn-005f743c)

~~~diff
- 005f743c ["COPY", "tmp:0:8", ["const:be0:8"]]
- 005f743c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f743c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f743c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f743c ["COPY", "tmp:0:8", ["const:c30:8"]]
+ 005f743c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f743c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f743c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f743c bytes 08812f91
+ 005f743c bytes 08c13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-639a1a6e336987f3dff01318a8e5bf6b"></a>

### [`005f75c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f75c0.md) → [`005f75c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f75c0.md) FUN_005f75c0

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
      "definition_site": "005f75d4",
      "incomplete_value": false,
      "site": "005f75d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f75d4",
      "incomplete_value": false,
      "site": "005f75d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "005f75d8",
      "DATA",
      [
        "storage",
        "00bf4c60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f75d8",
      "DATA",
      [
        "storage",
        "00bf4cb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f75d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f75c0.md#insn-005f75d4)
- 新版 [`005f75d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f75c0.md#insn-005f75d4)

~~~diff
- 005f75d4 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 005f75d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f75d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f75d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f75d4 ["COPY", "tmp:0:8", ["const:cb0:8"]]
+ 005f75d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f75d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f75d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f75d4 bytes 08813191
+ 005f75d4 bytes 08c13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5de12f1fe162c3b8a6e37938c7bcdcba"></a>

### [`005f75e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f75e4.md) → [`005f75e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f75e4.md) FUN_005f75e4

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
      "definition_site": "005f75e8",
      "incomplete_value": false,
      "site": "005f75ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f75e8",
      "incomplete_value": false,
      "site": "005f75ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "005f75ec",
      "DATA",
      [
        "storage",
        "00bf4c60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f75ec",
      "DATA",
      [
        "storage",
        "00bf4cb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f75e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f75e4.md#insn-005f75e8)
- 新版 [`005f75e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f75e4.md#insn-005f75e8)

~~~diff
- 005f75e8 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 005f75e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f75e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f75e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f75e8 ["COPY", "tmp:0:8", ["const:cb0:8"]]
+ 005f75e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f75e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f75e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f75e8 bytes 08813191
+ 005f75e8 bytes 08c13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b8f59d21a81d1d9feed505e147149a2"></a>

### [`005f777c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f777c.md) → [`005f777c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f777c.md) FUN_005f777c

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
      "definition_site": "005f7780",
      "incomplete_value": false,
      "site": "005f7784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f7780",
      "incomplete_value": false,
      "site": "005f7784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "005f7784",
      "DATA",
      [
        "storage",
        "00bf4ce0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f7784",
      "DATA",
      [
        "storage",
        "00bf4d30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f7780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f777c.md#insn-005f7780)
- 新版 [`005f7780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f777c.md#insn-005f7780)

~~~diff
- 005f7780 ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 005f7780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f7780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f7780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f7780 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 005f7780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f7780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f7780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f7780 bytes 08813391
+ 005f7780 bytes 08c13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90b9011724915a2ccd68e4afde7c3179"></a>

### [`005f78f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f78f0.md) → [`005f78f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f78f0.md) FUN_005f78f0

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
      "definition_site": "005f7904",
      "incomplete_value": false,
      "site": "005f7908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f7904",
      "incomplete_value": false,
      "site": "005f7908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:d60:8"
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
      "005f7908",
      "DATA",
      [
        "storage",
        "00bf4d60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f7908",
      "DATA",
      [
        "storage",
        "00bf4db0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f7904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f78f0.md#insn-005f7904)
- 新版 [`005f7904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f78f0.md#insn-005f7904)

~~~diff
- 005f7904 ["COPY", "tmp:0:8", ["const:d60:8"]]
- 005f7904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f7904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f7904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f7904 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 005f7904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f7904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f7904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f7904 bytes 08813591
+ 005f7904 bytes 08c13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2f11ae93f148ca00a1ef63e082ef721"></a>

### [`005f7a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7a88.md) → [`005f7a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7a88.md) FUN_005f7a88

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
      "definition_site": "005f7a9c",
      "incomplete_value": false,
      "site": "005f7aa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:e30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f7a9c",
      "incomplete_value": false,
      "site": "005f7aa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:de0:8"
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
      "005f7aa0",
      "DATA",
      [
        "storage",
        "00bf4de0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f7aa0",
      "DATA",
      [
        "storage",
        "00bf4e30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f7a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7a88.md#insn-005f7a9c)
- 新版 [`005f7a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7a88.md#insn-005f7a9c)

~~~diff
- 005f7a9c ["COPY", "tmp:0:8", ["const:de0:8"]]
- 005f7a9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f7a9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f7a9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f7a9c ["COPY", "tmp:0:8", ["const:e30:8"]]
+ 005f7a9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f7a9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f7a9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f7a9c bytes 08813791
+ 005f7a9c bytes 08c13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c08a13116a5b157f15f29c60e70527be"></a>

### [`005f7d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7d20.md) → [`005f7d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7d20.md) FUN_005f7d20

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
      "definition_site": "005f7d34",
      "incomplete_value": false,
      "site": "005f7d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f7d34",
      "incomplete_value": false,
      "site": "005f7d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:e60:8"
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
      "005f7d38",
      "DATA",
      [
        "storage",
        "00bf4e60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f7d38",
      "DATA",
      [
        "storage",
        "00bf4eb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f7d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7d20.md#insn-005f7d34)
- 新版 [`005f7d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7d20.md#insn-005f7d34)

~~~diff
- 005f7d34 ["COPY", "tmp:0:8", ["const:e60:8"]]
- 005f7d34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f7d34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f7d34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f7d34 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 005f7d34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f7d34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f7d34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f7d34 bytes 08813991
+ 005f7d34 bytes 08c13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1f7c72f00e76554738b9bb8f6d1a9dd"></a>

### [`005f7d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7d44.md) → [`005f7d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7d44.md) FUN_005f7d44

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
      "definition_site": "005f7d48",
      "incomplete_value": false,
      "site": "005f7d4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f7d48",
      "incomplete_value": false,
      "site": "005f7d4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
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
      "005f7d4c",
      "DATA",
      [
        "storage",
        "00bf4e60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f7d4c",
      "DATA",
      [
        "storage",
        "00bf4eb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f7d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7d44.md#insn-005f7d48)
- 新版 [`005f7d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7d44.md#insn-005f7d48)

~~~diff
- 005f7d48 ["COPY", "tmp:0:8", ["const:e60:8"]]
- 005f7d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f7d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f7d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f7d48 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 005f7d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f7d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f7d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f7d48 bytes 08813991
+ 005f7d48 bytes 08c13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0639077144b6bc8ccf8f24bd8d1a11a3"></a>

### [`005f7eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7eb8.md) → [`005f7eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7eb8.md) FUN_005f7eb8

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
      "definition_site": "005f7ecc",
      "incomplete_value": false,
      "site": "005f7ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f7ecc",
      "incomplete_value": false,
      "site": "005f7ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
      "005f7ed0",
      "DATA",
      [
        "storage",
        "00bf4ee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f7ed0",
      "DATA",
      [
        "storage",
        "00bf4f30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f7ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7eb8.md#insn-005f7ecc)
- 新版 [`005f7ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7eb8.md#insn-005f7ecc)

~~~diff
- 005f7ecc ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 005f7ecc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f7ecc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f7ecc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f7ecc ["COPY", "tmp:0:8", ["const:f30:8"]]
+ 005f7ecc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f7ecc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f7ecc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f7ecc bytes 08813b91
+ 005f7ecc bytes 08c13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a14644a486e85a965263d648bb71e27"></a>

### [`005f7edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7edc.md) → [`005f7edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7edc.md) FUN_005f7edc

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
      "definition_site": "005f7ee0",
      "incomplete_value": false,
      "site": "005f7ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f7ee0",
      "incomplete_value": false,
      "site": "005f7ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
      "005f7ee4",
      "DATA",
      [
        "storage",
        "00bf4ee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f7ee4",
      "DATA",
      [
        "storage",
        "00bf4f30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f7ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7edc.md#insn-005f7ee0)
- 新版 [`005f7ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7edc.md#insn-005f7ee0)

~~~diff
- 005f7ee0 ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 005f7ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f7ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f7ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f7ee0 ["COPY", "tmp:0:8", ["const:f30:8"]]
+ 005f7ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f7ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f7ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f7ee0 bytes 08813b91
+ 005f7ee0 bytes 08c13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-509fbc11d19e6a7017bdb19a9af2ca39"></a>

### [`005f8050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8050.md) → [`005f8050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8050.md) FUN_005f8050

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
      "definition_site": "005f8064",
      "incomplete_value": false,
      "site": "005f8068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f8064",
      "incomplete_value": false,
      "site": "005f8068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:f60:8"
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
      "005f8068",
      "DATA",
      [
        "storage",
        "00bf4f60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f8068",
      "DATA",
      [
        "storage",
        "00bf4fb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f8064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8050.md#insn-005f8064)
- 新版 [`005f8064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8050.md#insn-005f8064)

~~~diff
- 005f8064 ["COPY", "tmp:0:8", ["const:f60:8"]]
- 005f8064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f8064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f8064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f8064 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 005f8064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f8064 bytes 08813d91
+ 005f8064 bytes 08c13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0eb72ff2f5eec988f6ca08d5e1c25c85"></a>

### [`005f8074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8074.md) → [`005f8074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8074.md) FUN_005f8074

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
      "definition_site": "005f8078",
      "incomplete_value": false,
      "site": "005f807c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f8078",
      "incomplete_value": false,
      "site": "005f807c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:f60:8"
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
      "005f807c",
      "DATA",
      [
        "storage",
        "00bf4f60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f807c",
      "DATA",
      [
        "storage",
        "00bf4fb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f8078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8074.md#insn-005f8078)
- 新版 [`005f8078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8074.md#insn-005f8078)

~~~diff
- 005f8078 ["COPY", "tmp:0:8", ["const:f60:8"]]
- 005f8078 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f8078 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f8078 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f8078 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 005f8078 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8078 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8078 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f8078 bytes 08813d91
+ 005f8078 bytes 08c13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a107be67ff1e17408e2112dbc7c55a71"></a>

### [`005f81e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f81e8.md) → [`005f81e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81e8.md) FUN_005f81e8

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
      "definition_site": "005f81fc",
      "incomplete_value": false,
      "site": "005f8200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f81fc",
      "incomplete_value": false,
      "site": "005f8200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:fe0:8"
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
      "005f8200",
      "DATA",
      [
        "storage",
        "00bf4fe0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f8200",
      "DATA",
      [
        "storage",
        "00bf5030",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f81f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f81e8.md#insn-005f81f8) · [`005f81fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f81e8.md#insn-005f81fc)
- 新版 [`005f81f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81e8.md#insn-005f81f8) · [`005f81fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81e8.md#insn-005f81fc)

~~~diff
- 005f81f8 ["COPY", "register:4040:8", ["const:bf4000:8"]]
+ 005f81f8 ["COPY", "register:4040:8", ["const:bf5000:8"]]
- 005f81f8 bytes e82f0090
+ 005f81f8 bytes e82f00b0
- 005f81fc ["COPY", "tmp:0:8", ["const:fe0:8"]]
- 005f81fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f81fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f81fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f81fc ["COPY", "tmp:0:8", ["const:30:8"]]
+ 005f81fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f81fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f81fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f81fc bytes 08813f91
+ 005f81fc bytes 08c10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9252bec56d2297218a64e735424b8008"></a>

### [`005f820c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f820c.md) → [`005f820c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f820c.md) FUN_005f820c

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
      "definition_site": "005f8210",
      "incomplete_value": false,
      "site": "005f8214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f8210",
      "incomplete_value": false,
      "site": "005f8214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:fe0:8"
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
      "005f8214",
      "DATA",
      [
        "storage",
        "00bf4fe0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f8214",
      "DATA",
      [
        "storage",
        "00bf5030",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f820c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f820c.md#insn-005f820c) · [`005f8210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f820c.md#insn-005f8210)
- 新版 [`005f820c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f820c.md#insn-005f820c) · [`005f8210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f820c.md#insn-005f8210)

~~~diff
- 005f820c ["COPY", "register:4040:8", ["const:bf4000:8"]]
+ 005f820c ["COPY", "register:4040:8", ["const:bf5000:8"]]
- 005f820c bytes e82f0090
+ 005f820c bytes e82f00b0
- 005f8210 ["COPY", "tmp:0:8", ["const:fe0:8"]]
- 005f8210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f8210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f8210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f8210 ["COPY", "tmp:0:8", ["const:30:8"]]
+ 005f8210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f8210 bytes 08813f91
+ 005f8210 bytes 08c10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89b5135467cb68a00cad7e181ee89103"></a>

### [`005f8380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8380.md) → [`005f8380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8380.md) FUN_005f8380

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
      "definition_site": "005f8394",
      "incomplete_value": false,
      "site": "005f8398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f8394",
      "incomplete_value": false,
      "site": "005f8398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:60:8"
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
      "005f8398",
      "DATA",
      [
        "storage",
        "00bf5060",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f8398",
      "DATA",
      [
        "storage",
        "00bf50b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f8394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8380.md#insn-005f8394)
- 新版 [`005f8394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8380.md#insn-005f8394)

~~~diff
- 005f8394 ["COPY", "tmp:0:8", ["const:60:8"]]
- 005f8394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f8394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f8394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f8394 ["COPY", "tmp:0:8", ["const:b0:8"]]
+ 005f8394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f8394 bytes 08810191
+ 005f8394 bytes 08c10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d16e97bfa109075387e32e9883a4acef"></a>

### [`005f83a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f83a4.md) → [`005f83a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83a4.md) FUN_005f83a4

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
      "definition_site": "005f83a8",
      "incomplete_value": false,
      "site": "005f83ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f83a8",
      "incomplete_value": false,
      "site": "005f83ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:60:8"
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
      "005f83ac",
      "DATA",
      [
        "storage",
        "00bf5060",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f83ac",
      "DATA",
      [
        "storage",
        "00bf50b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f83a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f83a4.md#insn-005f83a8)
- 新版 [`005f83a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83a4.md#insn-005f83a8)

~~~diff
- 005f83a8 ["COPY", "tmp:0:8", ["const:60:8"]]
- 005f83a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f83a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f83a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f83a8 ["COPY", "tmp:0:8", ["const:b0:8"]]
+ 005f83a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f83a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f83a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f83a8 bytes 08810191
+ 005f83a8 bytes 08c10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11739458871c182b1d8a4ba232572dab"></a>

### [`005f8544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8544.md) → [`005f8544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8544.md) FUN_005f8544

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
      "definition_site": "005f8548",
      "incomplete_value": false,
      "site": "005f854c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f8548",
      "incomplete_value": false,
      "site": "005f854c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:e0:8"
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
      "005f854c",
      "DATA",
      [
        "storage",
        "00bf50e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f854c",
      "DATA",
      [
        "storage",
        "00bf5130",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f8548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8544.md#insn-005f8548)
- 新版 [`005f8548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8544.md#insn-005f8548)

~~~diff
- 005f8548 ["COPY", "tmp:0:8", ["const:e0:8"]]
- 005f8548 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f8548 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f8548 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f8548 ["COPY", "tmp:0:8", ["const:130:8"]]
+ 005f8548 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8548 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8548 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f8548 bytes 08810391
+ 005f8548 bytes 08c10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cf24930bc2702641b92d88005d46a0b"></a>

### [`005f86b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f86b8.md) → [`005f86b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86b8.md) FUN_005f86b8

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
      "definition_site": "005f86cc",
      "incomplete_value": false,
      "site": "005f86d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f86cc",
      "incomplete_value": false,
      "site": "005f86d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:160:8"
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
      "005f86d0",
      "DATA",
      [
        "storage",
        "00bf5160",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f86d0",
      "DATA",
      [
        "storage",
        "00bf51b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f86cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f86b8.md#insn-005f86cc)
- 新版 [`005f86cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86b8.md#insn-005f86cc)

~~~diff
- 005f86cc ["COPY", "tmp:0:8", ["const:160:8"]]
- 005f86cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f86cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f86cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f86cc ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 005f86cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f86cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f86cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f86cc bytes 08810591
+ 005f86cc bytes 08c10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7346e6c097290804dc6a53a23453c24"></a>

### [`005f86dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f86dc.md) → [`005f86dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86dc.md) FUN_005f86dc

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
      "definition_site": "005f86e0",
      "incomplete_value": false,
      "site": "005f86e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f86e0",
      "incomplete_value": false,
      "site": "005f86e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:160:8"
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
      "005f86e4",
      "DATA",
      [
        "storage",
        "00bf5160",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f86e4",
      "DATA",
      [
        "storage",
        "00bf51b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f86e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f86dc.md#insn-005f86e0)
- 新版 [`005f86e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86dc.md#insn-005f86e0)

~~~diff
- 005f86e0 ["COPY", "tmp:0:8", ["const:160:8"]]
- 005f86e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f86e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f86e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f86e0 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 005f86e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f86e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f86e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f86e0 bytes 08810591
+ 005f86e0 bytes 08c10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c4376c61678b3440852be8d76b42b4b"></a>

### [`005f8850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8850.md) → [`005f8850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8850.md) FUN_005f8850

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
      "definition_site": "005f8864",
      "incomplete_value": false,
      "site": "005f8868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f8864",
      "incomplete_value": false,
      "site": "005f8868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
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
      "005f8868",
      "DATA",
      [
        "storage",
        "00bf51e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f8868",
      "DATA",
      [
        "storage",
        "00bf5230",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f8864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8850.md#insn-005f8864)
- 新版 [`005f8864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8850.md#insn-005f8864)

~~~diff
- 005f8864 ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 005f8864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f8864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f8864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f8864 ["COPY", "tmp:0:8", ["const:230:8"]]
+ 005f8864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f8864 bytes 08810791
+ 005f8864 bytes 08c10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53c5908716edd83462b52cf38057d103"></a>

### [`005f8874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8874.md) → [`005f8874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8874.md) FUN_005f8874

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
      "definition_site": "005f8878",
      "incomplete_value": false,
      "site": "005f887c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f8878",
      "incomplete_value": false,
      "site": "005f887c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
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
      "005f887c",
      "DATA",
      [
        "storage",
        "00bf51e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f887c",
      "DATA",
      [
        "storage",
        "00bf5230",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f8878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8874.md#insn-005f8878)
- 新版 [`005f8878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8874.md#insn-005f8878)

~~~diff
- 005f8878 ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 005f8878 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f8878 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f8878 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f8878 ["COPY", "tmp:0:8", ["const:230:8"]]
+ 005f8878 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8878 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8878 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f8878 bytes 08810791
+ 005f8878 bytes 08c10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14c5ebe1ae0147dd1717d9d059f95ba9"></a>

### [`005f89e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f89e8.md) → [`005f89e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89e8.md) FUN_005f89e8

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
      "definition_site": "005f89fc",
      "incomplete_value": false,
      "site": "005f8a00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f89fc",
      "incomplete_value": false,
      "site": "005f8a00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:260:8"
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
      "005f8a00",
      "DATA",
      [
        "storage",
        "00bf5260",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f8a00",
      "DATA",
      [
        "storage",
        "00bf52b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f89fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f89e8.md#insn-005f89fc)
- 新版 [`005f89fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89e8.md#insn-005f89fc)

~~~diff
- 005f89fc ["COPY", "tmp:0:8", ["const:260:8"]]
- 005f89fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f89fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f89fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f89fc ["COPY", "tmp:0:8", ["const:2b0:8"]]
+ 005f89fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f89fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f89fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f89fc bytes 08810991
+ 005f89fc bytes 08c10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04c1cfcda314f5bbcc353a7119eaaa7a"></a>

### [`005f8a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8a0c.md) → [`005f8a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8a0c.md) FUN_005f8a0c

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
      "definition_site": "005f8a10",
      "incomplete_value": false,
      "site": "005f8a14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f8a10",
      "incomplete_value": false,
      "site": "005f8a14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:260:8"
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
      "005f8a14",
      "DATA",
      [
        "storage",
        "00bf5260",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f8a14",
      "DATA",
      [
        "storage",
        "00bf52b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f8a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8a0c.md#insn-005f8a10)
- 新版 [`005f8a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8a0c.md#insn-005f8a10)

~~~diff
- 005f8a10 ["COPY", "tmp:0:8", ["const:260:8"]]
- 005f8a10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f8a10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f8a10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f8a10 ["COPY", "tmp:0:8", ["const:2b0:8"]]
+ 005f8a10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8a10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8a10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f8a10 bytes 08810991
+ 005f8a10 bytes 08c10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f01e113602b78cc215d95695be73820d"></a>

### [`005f8b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8b04.md) → [`005f8b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b04.md) FUN_005f8b04

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
      "definition_site": "005f8b28",
      "incomplete_value": false,
      "site": "005f8b28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f8b28",
      "incomplete_value": false,
      "site": "005f8b28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
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
      "005f8b28",
      "DATA",
      [
        "storage",
        "00bf52e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f8b28",
      "DATA",
      [
        "storage",
        "00bf5330",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f8b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8b04.md#insn-005f8b24)
- 新版 [`005f8b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b04.md#insn-005f8b24)

~~~diff
- 005f8b24 ["COPY", "tmp:0:8", ["const:2e0:8"]]
- 005f8b24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f8b24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f8b24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f8b24 ["COPY", "tmp:0:8", ["const:330:8"]]
+ 005f8b24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8b24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8b24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f8b24 bytes 08810b91
+ 005f8b24 bytes 08c10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1d340b46d70e23004cfe8eb6048f474"></a>

### [`005f8b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8b38.md) → [`005f8b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b38.md) FUN_005f8b38

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
      "definition_site": "005f8b44",
      "incomplete_value": false,
      "site": "005f8b44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f8b44",
      "incomplete_value": false,
      "site": "005f8b44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
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
      "005f8b44",
      "DATA",
      [
        "storage",
        "00bf52e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f8b44",
      "DATA",
      [
        "storage",
        "00bf5330",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f8b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8b38.md#insn-005f8b40)
- 新版 [`005f8b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b38.md#insn-005f8b40)

~~~diff
- 005f8b40 ["COPY", "tmp:0:8", ["const:2e0:8"]]
- 005f8b40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005f8b40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005f8b40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005f8b40 ["COPY", "tmp:0:8", ["const:330:8"]]
+ 005f8b40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005f8b40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005f8b40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005f8b40 bytes 29810b91
+ 005f8b40 bytes 29c10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bfc1eaa3348185fc978cf9beeb69af5"></a>

### [`005f8c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8c28.md) → [`005f8c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c28.md) FUN_005f8c28

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
      "definition_site": "005f8c3c",
      "incomplete_value": false,
      "site": "005f8c40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f8c3c",
      "incomplete_value": false,
      "site": "005f8c40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:360:8"
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
      "005f8c40",
      "DATA",
      [
        "storage",
        "00bf5360",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f8c40",
      "DATA",
      [
        "storage",
        "00bf53b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f8c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8c28.md#insn-005f8c3c)
- 新版 [`005f8c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c28.md#insn-005f8c3c)

~~~diff
- 005f8c3c ["COPY", "tmp:0:8", ["const:360:8"]]
- 005f8c3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f8c3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f8c3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f8c3c ["COPY", "tmp:0:8", ["const:3b0:8"]]
+ 005f8c3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8c3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8c3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f8c3c bytes 08810d91
+ 005f8c3c bytes 08c10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e8b26967a568794ee64a6147ee851f6"></a>

### [`005f8c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8c4c.md) → [`005f8c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c4c.md) FUN_005f8c4c

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
      "definition_site": "005f8c50",
      "incomplete_value": false,
      "site": "005f8c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f8c50",
      "incomplete_value": false,
      "site": "005f8c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:360:8"
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
      "005f8c54",
      "DATA",
      [
        "storage",
        "00bf5360",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f8c54",
      "DATA",
      [
        "storage",
        "00bf53b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f8c50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8c4c.md#insn-005f8c50)
- 新版 [`005f8c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c4c.md#insn-005f8c50)

~~~diff
- 005f8c50 ["COPY", "tmp:0:8", ["const:360:8"]]
- 005f8c50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f8c50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f8c50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f8c50 ["COPY", "tmp:0:8", ["const:3b0:8"]]
+ 005f8c50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8c50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f8c50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f8c50 bytes 08810d91
+ 005f8c50 bytes 08c10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4038fae58ccc805c74524c42ac172627"></a>

### [`005f8c64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8c64.md) → [`005f8c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c64.md) FUN_005f8c64

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 24件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md)
- 新版 呼出元 0件  · 呼出先 24件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.19% / 新版 87.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 5件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005f8d48",
      "incomplete_value": false,
      "site": "005f8d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f8d48",
      "incomplete_value": false,
      "site": "005f8d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
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
      "definition_site": "005f8dfc",
      "incomplete_value": true,
      "site": "005f8e0c",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:a80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f8dfc",
      "incomplete_value": true,
      "site": "005f8e0c",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:9e6:8"
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
      "definition_site": "005f8e10",
      "incomplete_value": true,
      "site": "005f8e10",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005f8e10",
      "incomplete_value": true,
      "site": "005f8e10",
      "value": [
        "LOAD",
        "8",
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
      "005f8ce4",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "005f8cf0",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005f8cf8",
      "PARAM",
      [
        "storage",
        "00bf4500",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005f8ce4",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "005f8cf0",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005f8cf8",
      "PARAM",
      [
        "storage",
        "00bf4550",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f8ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8c64.md#insn-005f8ce4) · [`005f8cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8c64.md#insn-005f8cf0) · [`005f8cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8c64.md#insn-005f8cf8)
- 新版 [`005f8ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c64.md#insn-005f8ce4) · [`005f8cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c64.md#insn-005f8cf0) · [`005f8cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c64.md#insn-005f8cf8)

~~~diff
- 005f8ce4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 005f8ce4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005f8ce4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 005f8ce4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005f8ce4 bytes 003d45f9
+ 005f8ce4 bytes 005d45f9
- 005f8cf0 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 005f8cf0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005f8cf0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005f8cf0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005f8cf0 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 005f8cf0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005f8cf0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005f8cf0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005f8cf0 bytes 21203991
+ 005f8cf0 bytes 21603a91
- 005f8cf8 ["COPY", "tmp:0:8", ["const:500:8"]]
- 005f8cf8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 005f8cf8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 005f8cf8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 005f8cf8 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 005f8cf8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 005f8cf8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 005f8cf8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 005f8cf8 bytes 42001491
+ 005f8cf8 bytes 42401591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-817b52986b5343e29c2e8b2a01afd333"></a>

### [`005f90a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f90a4.md) → [`005f90a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90a4.md) FUN_005f90a4

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
      "definition_site": "005f90b8",
      "incomplete_value": false,
      "site": "005f90bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f90b8",
      "incomplete_value": false,
      "site": "005f90bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
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
      "005f90bc",
      "DATA",
      [
        "storage",
        "00bf53d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f90bc",
      "DATA",
      [
        "storage",
        "00bf5420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f90b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f90a4.md#insn-005f90b8)
- 新版 [`005f90b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90a4.md#insn-005f90b8)

~~~diff
- 005f90b8 ["COPY", "tmp:0:8", ["const:3d0:8"]]
- 005f90b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f90b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f90b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f90b8 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 005f90b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f90b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f90b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f90b8 bytes 08410f91
+ 005f90b8 bytes 08811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c095a2fde50f89010a480634978cd191"></a>

### [`005f90c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f90c8.md) → [`005f90c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90c8.md) FUN_005f90c8

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
      "definition_site": "005f90cc",
      "incomplete_value": false,
      "site": "005f90d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f90cc",
      "incomplete_value": false,
      "site": "005f90d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
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
      "005f90d0",
      "DATA",
      [
        "storage",
        "00bf53d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f90d0",
      "DATA",
      [
        "storage",
        "00bf5420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f90cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f90c8.md#insn-005f90cc)
- 新版 [`005f90cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90c8.md#insn-005f90cc)

~~~diff
- 005f90cc ["COPY", "tmp:0:8", ["const:3d0:8"]]
- 005f90cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f90cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f90cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f90cc ["COPY", "tmp:0:8", ["const:420:8"]]
+ 005f90cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f90cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f90cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f90cc bytes 08410f91
+ 005f90cc bytes 08811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dd00018492d3f8a0d3d512974fac7fa"></a>

### [`005f9164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f9164.md) → [`005f9164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9164.md) FUN_005f9164

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
      "definition_site": "005f9178",
      "incomplete_value": false,
      "site": "005f917c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f9178",
      "incomplete_value": false,
      "site": "005f917c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:460:8"
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
      "005f917c",
      "DATA",
      [
        "storage",
        "00bf5460",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f917c",
      "DATA",
      [
        "storage",
        "00bf54b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f9178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f9164.md#insn-005f9178)
- 新版 [`005f9178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9164.md#insn-005f9178)

~~~diff
- 005f9178 ["COPY", "tmp:0:8", ["const:460:8"]]
- 005f9178 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f9178 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f9178 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f9178 ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 005f9178 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f9178 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f9178 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f9178 bytes 08811191
+ 005f9178 bytes 08c11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f848bd1acfe70c18526e46fb2c0d5d8"></a>

### [`005f93b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f93b0.md) → [`005f93b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f93b0.md) FUN_005f93b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005f91cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f91cc.md) [`005f93b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f93b0.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`005f91cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f91cc.md) [`005f93b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f93b0.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.93% / 新版 98.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005f9528",
      "incomplete_value": false,
      "site": "005f9534",
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
      "definition_site": "005f9528",
      "incomplete_value": false,
      "site": "005f9534",
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
      "definition_site": "005f95e0",
      "incomplete_value": true,
      "site": "005f95e8",
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
            "const:379:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f95e0",
      "incomplete_value": true,
      "site": "005f95e8",
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
            "const:2ee:8"
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
      "definition_site": "005f95f8",
      "incomplete_value": false,
      "site": "005f9604",
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
      "definition_site": "005f95f8",
      "incomplete_value": false,
      "site": "005f9604",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005f9528",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "005f95e0",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "005f95f8",
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
      "005f9528",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "005f95e0",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "005f95f8",
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

- 旧版 [`005f9528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f93b0.md#insn-005f9528) · [`005f95e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f93b0.md#insn-005f95e0) · [`005f95f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f93b0.md#insn-005f95f8)
- 新版 [`005f9528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f93b0.md#insn-005f9528) · [`005f95e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f93b0.md#insn-005f95e0) · [`005f95f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f93b0.md#insn-005f95f8)

~~~diff
- 005f9528 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005f9528 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005f9528 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005f9528 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005f9528 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 005f9528 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005f9528 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005f9528 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005f9528 bytes 21280c91
+ 005f9528 bytes 21900e91
- 005f95e0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 005f95e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005f95e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005f95e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005f95e0 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 005f95e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005f95e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005f95e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005f95e0 bytes 21b80b91
+ 005f95e0 bytes 21e40d91
- 005f95f8 ["COPY", "tmp:0:8", ["const:919:8"]]
- 005f95f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005f95f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005f95f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005f95f8 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 005f95f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005f95f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005f95f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005f95f8 bytes 21642491
+ 005f95f8 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a26bf58915aa451aab232487d636fc0"></a>

### [`005f9f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f9f90.md) → [`005f9f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9f90.md) FUN_005f9f90

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005f93b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f93b0.md) [`005f9f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f9f90.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`005f93b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f93b0.md) [`005f9f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9f90.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005fa108",
      "incomplete_value": false,
      "site": "005fa110",
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
      "definition_site": "005fa108",
      "incomplete_value": false,
      "site": "005fa110",
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
      "definition_site": "005fa1bc",
      "incomplete_value": false,
      "site": "005fa1c4",
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
      "definition_site": "005fa1bc",
      "incomplete_value": false,
      "site": "005fa1c4",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005fa288",
      "incomplete_value": false,
      "site": "005fa298",
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
      "definition_site": "005fa288",
      "incomplete_value": false,
      "site": "005fa298",
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
      "005fa108",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "005fa1bc",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "005fa1d4",
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
      "005fa108",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "005fa1bc",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "005fa1d4",
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

- 旧版 [`005fa108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f9f90.md#insn-005fa108) · [`005fa1bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f9f90.md#insn-005fa1bc) · [`005fa1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f9f90.md#insn-005fa1d4)
- 新版 [`005fa108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9f90.md#insn-005fa108) · [`005fa1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9f90.md#insn-005fa1bc) · [`005fa1d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9f90.md#insn-005fa1d4)

~~~diff
- 005fa108 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005fa108 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fa108 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fa108 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fa108 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 005fa108 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fa108 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fa108 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fa108 bytes 21280c91
+ 005fa108 bytes 21900e91
- 005fa1bc ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 005fa1bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fa1bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fa1bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fa1bc ["COPY", "tmp:0:8", ["const:379:8"]]
+ 005fa1bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fa1bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fa1bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fa1bc bytes 21b80b91
+ 005fa1bc bytes 21e40d91
- 005fa1d4 ["COPY", "tmp:0:8", ["const:919:8"]]
- 005fa1d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fa1d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fa1d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fa1d4 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 005fa1d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fa1d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fa1d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fa1d4 bytes 21642491
+ 005fa1d4 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15cbb92c8679b42a8730787073830b00"></a>

### [`005fa9ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fa/005fa9ec.md) → [`005fa9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fa/005fa9ec.md) FUN_005fa9ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005f9f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f9f90.md) [`005fa9ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fa/005fa9ec.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`005f9f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9f90.md) [`005fa9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fa/005fa9ec.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.66% / 新版 98.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005fab5c",
      "incomplete_value": false,
      "site": "005fab64",
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
      "definition_site": "005fab5c",
      "incomplete_value": false,
      "site": "005fab64",
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
      "definition_site": "005fac10",
      "incomplete_value": false,
      "site": "005fac18",
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
      "definition_site": "005fac10",
      "incomplete_value": false,
      "site": "005fac18",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005fac28",
      "incomplete_value": false,
      "site": "005fac38",
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
      "definition_site": "005fac28",
      "incomplete_value": false,
      "site": "005fac38",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005fab5c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "005fac10",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "005fac28",
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
      "005fab5c",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "005fac10",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "005fac28",
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

- 旧版 [`005fab5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fa/005fa9ec.md#insn-005fab5c) · [`005fac10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fa/005fa9ec.md#insn-005fac10) · [`005fac28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fa/005fa9ec.md#insn-005fac28)
- 新版 [`005fab5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fa/005fa9ec.md#insn-005fab5c) · [`005fac10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fa/005fa9ec.md#insn-005fac10) · [`005fac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fa/005fa9ec.md#insn-005fac28)

~~~diff
- 005fab5c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005fab5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fab5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fab5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fab5c ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 005fab5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fab5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fab5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fab5c bytes 21280c91
+ 005fab5c bytes 21900e91
- 005fac10 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 005fac10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fac10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fac10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fac10 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 005fac10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fac10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fac10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fac10 bytes 21b80b91
+ 005fac10 bytes 21e40d91
- 005fac28 ["COPY", "tmp:0:8", ["const:919:8"]]
- 005fac28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fac28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fac28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fac28 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 005fac28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fac28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fac28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fac28 bytes 21642491
+ 005fac28 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22e06caddca04b0f037bca224bcb0c5a"></a>

### [`005fb4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fb/005fb4e0.md) → [`005fb4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fb/005fb4e0.md) FUN_005fb4e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005fb2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fb/005fb2ec.md) [`005fb4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fb/005fb4e0.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`005fb2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fb/005fb2ec.md) [`005fb4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fb/005fb4e0.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.94% / 新版 98.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005fb660",
      "incomplete_value": false,
      "site": "005fb66c",
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
      "definition_site": "005fb660",
      "incomplete_value": false,
      "site": "005fb66c",
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
      "definition_site": "005fb7e0",
      "incomplete_value": false,
      "site": "005fb7ec",
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
      "definition_site": "005fb7e0",
      "incomplete_value": false,
      "site": "005fb7ec",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005fbcf8",
      "incomplete_value": false,
      "site": "005fbd00",
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
      "definition_site": "005fbcf8",
      "incomplete_value": false,
      "site": "005fbd00",
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
      "005fb660",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "005fb718",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "005fb730",
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
      "005fb660",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "005fb718",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "005fb730",
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

- 旧版 [`005fb660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fb/005fb4e0.md#insn-005fb660) · [`005fb718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fb/005fb4e0.md#insn-005fb718) · [`005fb730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fb/005fb4e0.md#insn-005fb730)
- 新版 [`005fb660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fb/005fb4e0.md#insn-005fb660) · [`005fb718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fb/005fb4e0.md#insn-005fb718) · [`005fb730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fb/005fb4e0.md#insn-005fb730)

~~~diff
- 005fb660 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005fb660 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fb660 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fb660 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fb660 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 005fb660 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fb660 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fb660 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fb660 bytes 21280c91
+ 005fb660 bytes 21900e91
- 005fb718 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 005fb718 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fb718 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fb718 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fb718 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 005fb718 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fb718 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fb718 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fb718 bytes 21b80b91
+ 005fb718 bytes 21e40d91
- 005fb730 ["COPY", "tmp:0:8", ["const:919:8"]]
- 005fb730 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fb730 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fb730 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fb730 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 005fb730 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fb730 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fb730 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fb730 bytes 21642491
+ 005fb730 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e43390a175fe6656246bddae25c93db"></a>

### [`005fc0cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fc/005fc0cc.md) → [`005fc0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fc/005fc0cc.md) FUN_005fc0cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005fb4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fb/005fb4e0.md) [`005fc0cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fc/005fc0cc.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`005fb4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fb/005fb4e0.md) [`005fc0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fc/005fc0cc.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.81% / 新版 98.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005fc244",
      "incomplete_value": false,
      "site": "005fc24c",
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
      "definition_site": "005fc244",
      "incomplete_value": false,
      "site": "005fc24c",
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
      "definition_site": "005fc2fc",
      "incomplete_value": false,
      "site": "005fc304",
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
      "definition_site": "005fc2fc",
      "incomplete_value": false,
      "site": "005fc304",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005fc3cc",
      "incomplete_value": false,
      "site": "005fc3d8",
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
      "definition_site": "005fc3cc",
      "incomplete_value": false,
      "site": "005fc3d8",
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
      "005fc244",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "005fc2fc",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "005fc318",
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
      "005fc244",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "005fc2fc",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "005fc318",
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

- 旧版 [`005fc244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fc/005fc0cc.md#insn-005fc244) · [`005fc2fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fc/005fc0cc.md#insn-005fc2fc) · [`005fc318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fc/005fc0cc.md#insn-005fc318)
- 新版 [`005fc244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fc/005fc0cc.md#insn-005fc244) · [`005fc2fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fc/005fc0cc.md#insn-005fc2fc) · [`005fc318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fc/005fc0cc.md#insn-005fc318)

~~~diff
- 005fc244 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005fc244 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fc244 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fc244 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fc244 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 005fc244 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fc244 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fc244 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fc244 bytes 21280c91
+ 005fc244 bytes 21900e91
- 005fc2fc ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 005fc2fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fc2fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fc2fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fc2fc ["COPY", "tmp:0:8", ["const:379:8"]]
+ 005fc2fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fc2fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fc2fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fc2fc bytes 21b80b91
+ 005fc2fc bytes 21e40d91
- 005fc318 ["COPY", "tmp:0:8", ["const:919:8"]]
- 005fc318 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fc318 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fc318 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fc318 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 005fc318 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fc318 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fc318 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fc318 bytes 21642491
+ 005fc318 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca67fd5e1c77a9e5f136d0b41d9d883c"></a>

### [`005fcb1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fc/005fcb1c.md) → [`005fcb1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fc/005fcb1c.md) FUN_005fcb1c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005fc0cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fc/005fc0cc.md) [`005fcb1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fc/005fcb1c.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`005fc0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fc/005fc0cc.md) [`005fcb1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fc/005fcb1c.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.66% / 新版 98.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005fcc8c",
      "incomplete_value": false,
      "site": "005fcc94",
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
      "definition_site": "005fcc8c",
      "incomplete_value": false,
      "site": "005fcc94",
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
      "definition_site": "005fcd58",
      "incomplete_value": false,
      "site": "005fcd68",
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
      "definition_site": "005fcd58",
      "incomplete_value": false,
      "site": "005fcd68",
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
      "definition_site": "005fd160",
      "incomplete_value": false,
      "site": "005fd16c",
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
      "definition_site": "005fd160",
      "incomplete_value": false,
      "site": "005fd16c",
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
      "005fcc8c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "005fcd40",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "005fcd58",
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
      "005fcc8c",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "005fcd40",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "005fcd58",
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

- 旧版 [`005fcc8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fc/005fcb1c.md#insn-005fcc8c) · [`005fcd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fc/005fcb1c.md#insn-005fcd40) · [`005fcd58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fc/005fcb1c.md#insn-005fcd58)
- 新版 [`005fcc8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fc/005fcb1c.md#insn-005fcc8c) · [`005fcd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fc/005fcb1c.md#insn-005fcd40) · [`005fcd58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fc/005fcb1c.md#insn-005fcd58)

~~~diff
- 005fcc8c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005fcc8c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fcc8c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fcc8c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fcc8c ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 005fcc8c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fcc8c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fcc8c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fcc8c bytes 21280c91
+ 005fcc8c bytes 21900e91
- 005fcd40 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 005fcd40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fcd40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fcd40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fcd40 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 005fcd40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fcd40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fcd40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fcd40 bytes 21b80b91
+ 005fcd40 bytes 21e40d91
- 005fcd58 ["COPY", "tmp:0:8", ["const:919:8"]]
- 005fcd58 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fcd58 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fcd58 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fcd58 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 005fcd58 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fcd58 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fcd58 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fcd58 bytes 21642491
+ 005fcd58 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4452bf944a0d4593f658395089d22fa4"></a>

### [`005fd41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fd/005fd41c.md) → [`005fd41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fd/005fd41c.md) FUN_005fd41c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005fcb1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fc/005fcb1c.md) [`005fd41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fd/005fd41c.md) [`0060a74c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060a/0060a74c.md) [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 4件 [`005fcb1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fc/005fcb1c.md) [`005fd41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fd/005fd41c.md) [`0060a74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060a/0060a74c.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.50% / 新版 98.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005fd578",
      "incomplete_value": false,
      "site": "005fd580",
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
      "definition_site": "005fd578",
      "incomplete_value": false,
      "site": "005fd580",
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
      "definition_site": "005fd59c",
      "incomplete_value": false,
      "site": "005fd5a8",
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
      "definition_site": "005fd59c",
      "incomplete_value": false,
      "site": "005fd5a8",
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
      "definition_site": "005fd6d0",
      "incomplete_value": false,
      "site": "005fd6d8",
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
      "definition_site": "005fd6d0",
      "incomplete_value": false,
      "site": "005fd6d8",
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
      "005fd578",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "005fd59c",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "005fd6d0",
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
      "005fd578",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "005fd59c",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "005fd6d0",
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

- 旧版 [`005fd578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fd/005fd41c.md#insn-005fd578) · [`005fd59c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fd/005fd41c.md#insn-005fd59c) · [`005fd6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fd/005fd41c.md#insn-005fd6d0)
- 新版 [`005fd578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fd/005fd41c.md#insn-005fd578) · [`005fd59c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fd/005fd41c.md#insn-005fd59c) · [`005fd6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fd/005fd41c.md#insn-005fd6d0)

~~~diff
- 005fd578 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005fd578 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fd578 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fd578 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fd578 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 005fd578 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fd578 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fd578 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fd578 bytes 21280c91
+ 005fd578 bytes 21900e91
- 005fd59c ["COPY", "tmp:0:8", ["const:919:8"]]
- 005fd59c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fd59c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fd59c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fd59c ["COPY", "tmp:0:8", ["const:885:8"]]
+ 005fd59c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fd59c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fd59c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fd59c bytes 21642491
+ 005fd59c bytes 21142291
- 005fd6d0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 005fd6d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fd6d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fd6d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fd6d0 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 005fd6d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fd6d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fd6d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fd6d0 bytes 21b80b91
+ 005fd6d0 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a81f4fb3181ad9c5083b6da2bc842813"></a>

### [`005fdc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fd/005fdc34.md) → [`005fdc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fd/005fdc34.md) FUN_005fdc34

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005ec6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ec/005ec6e8.md) [`005fdc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fd/005fdc34.md) [`005ffcc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ff/005ffcc8.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`005ec6e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ec/005ec6e8.md) [`005fdc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fd/005fdc34.md) [`005ffcc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ff/005ffcc8.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

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
      "definition_site": "005fdda4",
      "incomplete_value": false,
      "site": "005fddac",
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
      "definition_site": "005fdda4",
      "incomplete_value": false,
      "site": "005fddac",
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
      "definition_site": "005fde64",
      "incomplete_value": true,
      "site": "005fde6c",
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
            "const:379:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005fde64",
      "incomplete_value": true,
      "site": "005fde6c",
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
            "const:2ee:8"
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
      "definition_site": "005fde80",
      "incomplete_value": false,
      "site": "005fde8c",
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
      "definition_site": "005fde80",
      "incomplete_value": false,
      "site": "005fde8c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005fdda4",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "005fde64",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "005fde80",
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
      "005fdda4",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "005fde64",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "005fde80",
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

- 旧版 [`005fdda4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fd/005fdc34.md#insn-005fdda4) · [`005fde64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fd/005fdc34.md#insn-005fde64) · [`005fde80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fd/005fdc34.md#insn-005fde80)
- 新版 [`005fdda4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fd/005fdc34.md#insn-005fdda4) · [`005fde64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fd/005fdc34.md#insn-005fde64) · [`005fde80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fd/005fdc34.md#insn-005fde80)

~~~diff
- 005fdda4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005fdda4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fdda4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fdda4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fdda4 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 005fdda4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fdda4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fdda4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fdda4 bytes 21280c91
+ 005fdda4 bytes 21900e91
- 005fde64 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 005fde64 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fde64 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fde64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fde64 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 005fde64 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fde64 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fde64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fde64 bytes 21b80b91
+ 005fde64 bytes 21e40d91
- 005fde80 ["COPY", "tmp:0:8", ["const:919:8"]]
- 005fde80 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fde80 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fde80 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fde80 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 005fde80 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fde80 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fde80 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fde80 bytes 21642491
+ 005fde80 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2fb8aa31dfe08647fc5f7ceb0c73998"></a>

### [`005fe524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fe/005fe524.md) → [`005fe524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fe/005fe524.md) FUN_005fe524

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005fdc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fd/005fdc34.md) [`005fe524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fe/005fe524.md) [`00906b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md) [`009a7208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a7/009a7208.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 4件 [`005fdc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fd/005fdc34.md) [`005fe524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fe/005fe524.md) [`00906b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906b9c.md) [`009a7208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a7/009a7208.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005fe678",
      "incomplete_value": true,
      "site": "005fe680",
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
            "const:3a4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005fe678",
      "incomplete_value": true,
      "site": "005fe680",
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
      "definition_site": "005fe7d0",
      "incomplete_value": false,
      "site": "005fe7d8",
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
      "definition_site": "005fe7d0",
      "incomplete_value": false,
      "site": "005fe7d8",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005fe7e8",
      "incomplete_value": false,
      "site": "005fe7f4",
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
      "definition_site": "005fe7e8",
      "incomplete_value": false,
      "site": "005fe7f4",
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
      "005fe678",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "005fe69c",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "005fe7d0",
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
      "005fe678",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "005fe69c",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "005fe7d0",
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

- 旧版 [`005fe678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fe/005fe524.md#insn-005fe678) · [`005fe69c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fe/005fe524.md#insn-005fe69c) · [`005fe7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fe/005fe524.md#insn-005fe7d0)
- 新版 [`005fe678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fe/005fe524.md#insn-005fe678) · [`005fe69c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fe/005fe524.md#insn-005fe69c) · [`005fe7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fe/005fe524.md#insn-005fe7d0)

~~~diff
- 005fe678 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005fe678 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fe678 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fe678 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fe678 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 005fe678 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fe678 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fe678 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fe678 bytes 21280c91
+ 005fe678 bytes 21900e91
- 005fe69c ["COPY", "tmp:0:8", ["const:919:8"]]
- 005fe69c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fe69c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fe69c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fe69c ["COPY", "tmp:0:8", ["const:885:8"]]
+ 005fe69c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fe69c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fe69c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fe69c bytes 21642491
+ 005fe69c bytes 21142291
- 005fe7d0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 005fe7d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005fe7d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005fe7d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005fe7d0 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 005fe7d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005fe7d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005fe7d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005fe7d0 bytes 21b80b91
+ 005fe7d0 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db7e68654bb4755084d32a240637535d"></a>

### [`005fed28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fe/005fed28.md) → [`005fed28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fe/005fed28.md) FUN_005fed28

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
      "definition_site": "005fed3c",
      "incomplete_value": false,
      "site": "005fed40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005fed3c",
      "incomplete_value": false,
      "site": "005fed40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
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
      "005fed40",
      "DATA",
      [
        "storage",
        "00bf54e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005fed40",
      "DATA",
      [
        "storage",
        "00bf5530",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005fed3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fe/005fed28.md#insn-005fed3c)
- 新版 [`005fed3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fe/005fed28.md#insn-005fed3c)

~~~diff
- 005fed3c ["COPY", "tmp:0:8", ["const:4e0:8"]]
- 005fed3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005fed3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005fed3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005fed3c ["COPY", "tmp:0:8", ["const:530:8"]]
+ 005fed3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005fed3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005fed3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005fed3c bytes 08811391
+ 005fed3c bytes 08c11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e0947314e7b599269509f456ed0f295"></a>

### [`005fed4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fe/005fed4c.md) → [`005fed4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fe/005fed4c.md) FUN_005fed4c

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
      "definition_site": "005fed50",
      "incomplete_value": false,
      "site": "005fed54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005fed50",
      "incomplete_value": false,
      "site": "005fed54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
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
      "005fed54",
      "DATA",
      [
        "storage",
        "00bf54e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005fed54",
      "DATA",
      [
        "storage",
        "00bf5530",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005fed50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fe/005fed4c.md#insn-005fed50)
- 新版 [`005fed50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fe/005fed4c.md#insn-005fed50)

~~~diff
- 005fed50 ["COPY", "tmp:0:8", ["const:4e0:8"]]
- 005fed50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005fed50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005fed50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005fed50 ["COPY", "tmp:0:8", ["const:530:8"]]
+ 005fed50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005fed50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005fed50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005fed50 bytes 08811391
+ 005fed50 bytes 08c11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a666f3665759d669090405a3fa2cc98d"></a>

### [`005fed64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fe/005fed64.md) → [`005fed64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fe/005fed64.md) FUN_005fed64

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00701b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00701/00701b78.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00701b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00701/00701b78.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005ff044",
      "incomplete_value": false,
      "site": "005ff054",
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
      "definition_site": "005ff044",
      "incomplete_value": false,
      "site": "005ff054",
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
    "ordinal": 25,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005feed8",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "005fef50",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "005fef6c",
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
      "005feed8",
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "005fef50",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "005fef6c",
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

- 旧版 [`005feed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fe/005fed64.md#insn-005feed8) · [`005feee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fe/005fed64.md#insn-005feee0)
- 新版 [`005feed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fe/005fed64.md#insn-005feed8) · [`005feee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fe/005fed64.md#insn-005feee0)

~~~diff
- 005feed8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:e60:8"]]
- 005feed8 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 005feed8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:eb0:8"]]
+ 005feed8 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 005feed8 bytes f73247f9
+ 005feed8 bytes f75a47f9
- 005feee0 ["COPY", "register:4098:8", ["const:c25000:8"]]
- 005feee0 bytes 333100f0
+ 005feee0 ["COPY", "register:4098:8", ["const:c25000:8"]]
+ 005feee0 bytes 333100f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18ff5a2a0ac287ada12bb64c822935a5"></a>

### [`005ff26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ff/005ff26c.md) → [`005ff26c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ff/005ff26c.md) FUN_005ff26c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005ff11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ff/005ff11c.md) [`005ff26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ff/005ff26c.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`005ff11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ff/005ff11c.md) [`005ff26c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ff/005ff26c.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005ff498",
      "incomplete_value": false,
      "site": "005ff4a0",
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
      "definition_site": "005ff498",
      "incomplete_value": false,
      "site": "005ff4a0",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005ff7c8",
      "incomplete_value": false,
      "site": "005ff7d4",
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
            "const:5e5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ff7c8",
      "incomplete_value": false,
      "site": "005ff7d4",
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
            "const:672:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005ff93c",
      "incomplete_value": false,
      "site": "005ff948",
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
      "definition_site": "005ff93c",
      "incomplete_value": false,
      "site": "005ff948",
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
      "005ff3e4",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "005ff498",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "005ff4b0",
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
      "005ff3e4",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "005ff498",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "005ff4b0",
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

- 旧版 [`005ff3e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ff/005ff26c.md#insn-005ff3e4) · [`005ff498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ff/005ff26c.md#insn-005ff498) · [`005ff4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ff/005ff26c.md#insn-005ff4b0)
- 新版 [`005ff3e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ff/005ff26c.md#insn-005ff3e4) · [`005ff498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ff/005ff26c.md#insn-005ff498) · [`005ff4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ff/005ff26c.md#insn-005ff4b0)

~~~diff
- 005ff3e4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005ff3e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005ff3e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005ff3e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005ff3e4 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 005ff3e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005ff3e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005ff3e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005ff3e4 bytes 21280c91
+ 005ff3e4 bytes 21900e91
- 005ff498 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 005ff498 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005ff498 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005ff498 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005ff498 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 005ff498 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005ff498 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005ff498 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005ff498 bytes 21b80b91
+ 005ff498 bytes 21e40d91
- 005ff4b0 ["COPY", "tmp:0:8", ["const:919:8"]]
- 005ff4b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005ff4b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005ff4b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005ff4b0 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 005ff4b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005ff4b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005ff4b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005ff4b0 bytes 21642491
+ 005ff4b0 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43ee69c7ffe92a748887acca0a13bc3d"></a>

### [`005ffcc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ff/005ffcc8.md) → [`005ffcc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ff/005ffcc8.md) FUN_005ffcc8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005ff26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ff/005ff26c.md) [`005ffcc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ff/005ffcc8.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`005ff26c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ff/005ff26c.md) [`005ffcc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ff/005ffcc8.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

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
      "definition_site": "005ffe28",
      "incomplete_value": false,
      "site": "005ffe30",
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
      "definition_site": "005ffe28",
      "incomplete_value": false,
      "site": "005ffe30",
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
      "definition_site": "005ffee4",
      "incomplete_value": false,
      "site": "005ffeec",
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
      "definition_site": "005ffee4",
      "incomplete_value": false,
      "site": "005ffeec",
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
      "definition_site": "005ffefc",
      "incomplete_value": false,
      "site": "005fff08",
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
      "definition_site": "005ffefc",
      "incomplete_value": false,
      "site": "005fff08",
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
      "005ffe28",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "005ffee4",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "005ffefc",
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
      "005ffe28",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "005ffee4",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "005ffefc",
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

- 旧版 [`005ffe28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ff/005ffcc8.md#insn-005ffe28) · [`005ffee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ff/005ffcc8.md#insn-005ffee4) · [`005ffefc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ff/005ffcc8.md#insn-005ffefc)
- 新版 [`005ffe28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ff/005ffcc8.md#insn-005ffe28) · [`005ffee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ff/005ffcc8.md#insn-005ffee4) · [`005ffefc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ff/005ffcc8.md#insn-005ffefc)

~~~diff
- 005ffe28 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005ffe28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005ffe28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005ffe28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005ffe28 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 005ffe28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005ffe28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005ffe28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005ffe28 bytes 21280c91
+ 005ffe28 bytes 21900e91
- 005ffee4 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 005ffee4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005ffee4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005ffee4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005ffee4 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 005ffee4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005ffee4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005ffee4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005ffee4 bytes 21b80b91
+ 005ffee4 bytes 21e40d91
- 005ffefc ["COPY", "tmp:0:8", ["const:919:8"]]
- 005ffefc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005ffefc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005ffefc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005ffefc ["COPY", "tmp:0:8", ["const:885:8"]]
+ 005ffefc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005ffefc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005ffefc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005ffefc bytes 21642491
+ 005ffefc bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9373b51bde5b8379b1879ad0f64605cc"></a>

### [`006007cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/006007cc.md) → [`006007cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/006007cc.md) FUN_006007cc

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
      "definition_site": "006007f0",
      "incomplete_value": false,
      "site": "006007f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006007f0",
      "incomplete_value": false,
      "site": "006007f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:560:8"
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
      "006007f0",
      "DATA",
      [
        "storage",
        "00bf5560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006007f0",
      "DATA",
      [
        "storage",
        "00bf55b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006007ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/006007cc.md#insn-006007ec)
- 新版 [`006007ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/006007cc.md#insn-006007ec)

~~~diff
- 006007ec ["COPY", "tmp:0:8", ["const:560:8"]]
- 006007ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006007ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006007ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006007ec ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 006007ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006007ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006007ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006007ec bytes 08811591
+ 006007ec bytes 08c11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c8e9bc54ddf5d62de5c0c65feff160f"></a>

### [`00600800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600800.md) → [`00600800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600800.md) FUN_00600800

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
      "definition_site": "0060080c",
      "incomplete_value": false,
      "site": "0060080c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060080c",
      "incomplete_value": false,
      "site": "0060080c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:560:8"
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
      "0060080c",
      "DATA",
      [
        "storage",
        "00bf5560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0060080c",
      "DATA",
      [
        "storage",
        "00bf55b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00600808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600800.md#insn-00600808)
- 新版 [`00600808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600800.md#insn-00600808)

~~~diff
- 00600808 ["COPY", "tmp:0:8", ["const:560:8"]]
- 00600808 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00600808 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00600808 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00600808 ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 00600808 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00600808 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00600808 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00600808 bytes 29811591
+ 00600808 bytes 29c11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-754f31ced8587f00807edbaaed403c2b"></a>

### [`00600a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600a24.md) → [`00600a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600a24.md) FUN_00600a24

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
      "definition_site": "00600a48",
      "incomplete_value": false,
      "site": "00600a48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00600a48",
      "incomplete_value": false,
      "site": "00600a48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:5d0:8"
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
      "00600a48",
      "DATA",
      [
        "storage",
        "00bf55d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00600a48",
      "DATA",
      [
        "storage",
        "00bf5620",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00600a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600a24.md#insn-00600a44)
- 新版 [`00600a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600a24.md#insn-00600a44)

~~~diff
- 00600a44 ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 00600a44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00600a44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00600a44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00600a44 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00600a44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00600a44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00600a44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00600a44 bytes 08411791
+ 00600a44 bytes 08811891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59e2ab3117ded3fe8f4842626196e373"></a>

### [`00600a58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600a58.md) → [`00600a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600a58.md) FUN_00600a58

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
      "definition_site": "00600a64",
      "incomplete_value": false,
      "site": "00600a64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00600a64",
      "incomplete_value": false,
      "site": "00600a64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:5d0:8"
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
      "00600a64",
      "DATA",
      [
        "storage",
        "00bf55d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00600a64",
      "DATA",
      [
        "storage",
        "00bf5620",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00600a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600a58.md#insn-00600a60)
- 新版 [`00600a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600a58.md#insn-00600a60)

~~~diff
- 00600a60 ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 00600a60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00600a60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00600a60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00600a60 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00600a60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00600a60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00600a60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00600a60 bytes 29411791
+ 00600a60 bytes 29811891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-942afbacd81bb548505177c7ae2a73ab"></a>

### [`00600a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600a74.md) → [`00600a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600a74.md) FUN_00600a74

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 15件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`005ec96c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ec/005ec96c.md) [`00600d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600d64.md) [`00600d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600d68.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`005ec96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ec/005ec96c.md) [`00600d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600d64.md) [`00600d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600d68.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.98% / 新版 88.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00600adc",
      "incomplete_value": true,
      "site": "00600adc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00600adc",
      "incomplete_value": true,
      "site": "00600adc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:76a:8"
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
      "definition_site": "00600ae0",
      "incomplete_value": true,
      "site": "00600ae0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00600ae0",
      "incomplete_value": true,
      "site": "00600ae0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00600afc",
      "incomplete_value": false,
      "site": "00600afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00600afc",
      "incomplete_value": false,
      "site": "00600afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "00600acc",
      "READ",
      [
        "storage",
        "002a176a",
        null,
        "string"
      ]
    ],
    [
      "00600ad0",
      "READ",
      [
        "storage",
        "002a176f",
        null,
        "string"
      ]
    ],
    [
      "00600afc",
      "DATA",
      [
        "storage",
        "00bf5640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00600acc",
      "READ",
      [
        "storage",
        "002a17f5",
        null,
        "string"
      ]
    ],
    [
      "00600ad0",
      "READ",
      [
        "storage",
        "002a17fa",
        null,
        "string"
      ]
    ],
    [
      "00600afc",
      "DATA",
      [
        "storage",
        "00bf5690",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00600ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600a74.md#insn-00600ac4) · [`00600af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600a74.md#insn-00600af4) · [`00600af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600a74.md#insn-00600af8)
- 新版 [`00600ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600a74.md#insn-00600ac4) · [`00600af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600a74.md#insn-00600af4)

~~~diff
- 00600ac4 ["COPY", "tmp:0:8", ["const:76a:8"]]
- 00600ac4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00600ac4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00600ac4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00600ac4 ["COPY", "tmp:0:8", ["const:7f5:8"]]
+ 00600ac4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00600ac4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00600ac4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00600ac4 bytes 29a91d91
+ 00600ac4 bytes 29d51f91
- 00600af4 ["COPY", "tmp:0:8", ["const:640:8"]]
- 00600af4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00600af4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00600af4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00600af4 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 00600af4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00600af4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00600af4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00600af4 bytes 08011991
+ 00600af4 bytes 08411a91
- 00600af8 ["COPY", "tmp:0:8", ["const:30:8"]]
- 00600af8 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 00600af8 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 00600af8 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 00600af8 bytes f5c30091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2efac0f616604508921c420f9fde29f0"></a>

### [`00600d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600d1c.md) → [`00600d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600d1c.md) FUN_00600d1c

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
      "definition_site": "00600d40",
      "incomplete_value": false,
      "site": "00600d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00600d40",
      "incomplete_value": false,
      "site": "00600d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "00600d40",
      "DATA",
      [
        "storage",
        "00bf5640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00600d40",
      "DATA",
      [
        "storage",
        "00bf5690",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00600d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600d1c.md#insn-00600d3c)
- 新版 [`00600d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600d1c.md#insn-00600d3c)

~~~diff
- 00600d3c ["COPY", "tmp:0:8", ["const:640:8"]]
- 00600d3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00600d3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00600d3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00600d3c ["COPY", "tmp:0:8", ["const:690:8"]]
+ 00600d3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00600d3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00600d3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00600d3c bytes 08011991
+ 00600d3c bytes 08411a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-339864e1d02471abb52f77ca63834709"></a>

### [`00600d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600d50.md) → [`00600d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600d50.md) FUN_00600d50

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
      "definition_site": "00600d5c",
      "incomplete_value": false,
      "site": "00600d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00600d5c",
      "incomplete_value": false,
      "site": "00600d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "00600d5c",
      "DATA",
      [
        "storage",
        "00bf5640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00600d5c",
      "DATA",
      [
        "storage",
        "00bf5690",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00600d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600d50.md#insn-00600d58)
- 新版 [`00600d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600d50.md#insn-00600d58)

~~~diff
- 00600d58 ["COPY", "tmp:0:8", ["const:640:8"]]
- 00600d58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00600d58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00600d58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00600d58 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 00600d58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00600d58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00600d58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00600d58 bytes 29011991
+ 00600d58 bytes 29411a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38519d9cbb96f4968449557a83c8eedd"></a>

### [`00600e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600e0c.md) → [`00600e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600e0c.md) FUN_00600e0c

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
      "definition_site": "00600e20",
      "incomplete_value": false,
      "site": "00600e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00600e20",
      "incomplete_value": false,
      "site": "00600e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      "00600e24",
      "DATA",
      [
        "storage",
        "00bf56c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00600e24",
      "DATA",
      [
        "storage",
        "00bf5710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00600e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600e0c.md#insn-00600e20)
- 新版 [`00600e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600e0c.md#insn-00600e20)

~~~diff
- 00600e20 ["COPY", "tmp:0:8", ["const:6c0:8"]]
- 00600e20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00600e20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00600e20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00600e20 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00600e20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00600e20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00600e20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00600e20 bytes 08011b91
+ 00600e20 bytes 08411c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-597d3c84b469b150e72e032d90364384"></a>

### [`00600e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600e30.md) → [`00600e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600e30.md) FUN_00600e30

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00600e34",
      "incomplete_value": true,
      "site": "00600e38",
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
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00600e34",
      "incomplete_value": true,
      "site": "00600e38",
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
            "const:6c0:8"
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
      "00600e38",
      "DATA",
      [
        "storage",
        "00bf56c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00600e38",
      "DATA",
      [
        "storage",
        "00bf5710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00600e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600e30.md#insn-00600e34)
- 新版 [`00600e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600e30.md#insn-00600e34)

~~~diff
- 00600e34 ["COPY", "tmp:0:8", ["const:6c0:8"]]
- 00600e34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00600e34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00600e34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00600e34 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00600e34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00600e34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00600e34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00600e34 bytes 08011b91
+ 00600e34 bytes 08411c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76dddc9c63964ee77ff27b9ba9471d57"></a>

### [`00600ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600ec0.md) → [`00600ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600ec0.md) FUN_00600ec0

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
      "definition_site": "00600ed4",
      "incomplete_value": false,
      "site": "00600ed8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:7b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00600ed4",
      "incomplete_value": false,
      "site": "00600ed8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:760:8"
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
      "00600ed8",
      "DATA",
      [
        "storage",
        "00bf5760",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00600ed8",
      "DATA",
      [
        "storage",
        "00bf57b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00600ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600ec0.md#insn-00600ed4)
- 新版 [`00600ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600ec0.md#insn-00600ed4)

~~~diff
- 00600ed4 ["COPY", "tmp:0:8", ["const:760:8"]]
- 00600ed4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00600ed4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00600ed4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00600ed4 ["COPY", "tmp:0:8", ["const:7b0:8"]]
+ 00600ed4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00600ed4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00600ed4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00600ed4 bytes 08811d91
+ 00600ed4 bytes 08c11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fd4d7886acb13f0e7bfb634dd82482b"></a>

### [`0060115c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/0060115c.md) → [`0060115c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/0060115c.md) FUN_0060115c

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
      "definition_site": "00601160",
      "incomplete_value": false,
      "site": "00601164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00601160",
      "incomplete_value": false,
      "site": "00601164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
      "00601164",
      "DATA",
      [
        "storage",
        "00bf57e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00601164",
      "DATA",
      [
        "storage",
        "00bf5830",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00601160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/0060115c.md#insn-00601160)
- 新版 [`00601160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/0060115c.md#insn-00601160)

~~~diff
- 00601160 ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 00601160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00601160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00601160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00601160 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 00601160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00601160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00601160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00601160 bytes 08811f91
+ 00601160 bytes 08c12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-162f84d7449f35e86522a70f9277c3ca"></a>

### [`006011f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/006011f8.md) → [`006011f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006011f8.md) FUN_006011f8

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
      "definition_site": "0060120c",
      "incomplete_value": false,
      "site": "00601210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060120c",
      "incomplete_value": false,
      "site": "00601210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "00601210",
      "DATA",
      [
        "storage",
        "00bf5870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00601210",
      "DATA",
      [
        "storage",
        "00bf58c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0060120c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/006011f8.md#insn-0060120c)
- 新版 [`0060120c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006011f8.md#insn-0060120c)

~~~diff
- 0060120c ["COPY", "tmp:0:8", ["const:870:8"]]
- 0060120c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0060120c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0060120c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0060120c ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 0060120c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0060120c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0060120c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0060120c bytes 08c12191
+ 0060120c bytes 08012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37c6c0b39629bea9c07e607a2236af8c"></a>

### [`0060121c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/0060121c.md) → [`0060121c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/0060121c.md) FUN_0060121c

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
      "definition_site": "00601220",
      "incomplete_value": false,
      "site": "00601224",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00601220",
      "incomplete_value": false,
      "site": "00601224",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "00601224",
      "DATA",
      [
        "storage",
        "00bf5870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00601224",
      "DATA",
      [
        "storage",
        "00bf58c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00601220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/0060121c.md#insn-00601220)
- 新版 [`00601220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/0060121c.md#insn-00601220)

~~~diff
- 00601220 ["COPY", "tmp:0:8", ["const:870:8"]]
- 00601220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00601220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00601220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00601220 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00601220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00601220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00601220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00601220 bytes 08c12191
+ 00601220 bytes 08012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-478f5c4e1164dea7a1a306b66bca27e1"></a>

### [`0060128c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/0060128c.md) → [`0060128c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/0060128c.md) FUN_0060128c

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
      "definition_site": "006012a0",
      "incomplete_value": false,
      "site": "006012a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006012a0",
      "incomplete_value": false,
      "site": "006012a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "006012a4",
      "DATA",
      [
        "storage",
        "00bf58f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006012a4",
      "DATA",
      [
        "storage",
        "00bf5940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006012a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/0060128c.md#insn-006012a0)
- 新版 [`006012a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/0060128c.md#insn-006012a0)

~~~diff
- 006012a0 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 006012a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006012a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006012a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006012a0 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 006012a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006012a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006012a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006012a0 bytes 08c12391
+ 006012a0 bytes 08012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-486662f2ca3da15d6b85ad62f4ad11d1"></a>

### [`006012b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/006012b0.md) → [`006012b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006012b0.md) FUN_006012b0

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
      "definition_site": "006012b4",
      "incomplete_value": false,
      "site": "006012b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006012b4",
      "incomplete_value": false,
      "site": "006012b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "006012b8",
      "DATA",
      [
        "storage",
        "00bf58f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006012b8",
      "DATA",
      [
        "storage",
        "00bf5940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006012b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/006012b0.md#insn-006012b4)
- 新版 [`006012b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006012b0.md#insn-006012b4)

~~~diff
- 006012b4 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 006012b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006012b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006012b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006012b4 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 006012b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006012b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006012b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006012b4 bytes 08c12391
+ 006012b4 bytes 08012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c438b240962d4f2b4585276b4e940bd"></a>

### [`00601374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/00601374.md) → [`00601374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601374.md) FUN_00601374

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
      "definition_site": "00601380",
      "incomplete_value": false,
      "site": "00601380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00601380",
      "incomplete_value": false,
      "site": "00601380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
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
      "00601380",
      "DATA",
      [
        "storage",
        "00bf5970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00601380",
      "DATA",
      [
        "storage",
        "00bf59c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0060137c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/00601374.md#insn-0060137c)
- 新版 [`0060137c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601374.md#insn-0060137c)

~~~diff
- 0060137c ["COPY", "tmp:0:8", ["const:970:8"]]
- 0060137c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0060137c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0060137c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0060137c ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 0060137c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0060137c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0060137c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0060137c bytes 29c12591
+ 0060137c bytes 29012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0fe1a42cb0e3abb8ae449fe4ad1129f"></a>

### [`006013d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/006013d4.md) → [`006013d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006013d4.md) FUN_006013d4

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
      "definition_site": "006013e8",
      "incomplete_value": false,
      "site": "006013ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006013e8",
      "incomplete_value": false,
      "site": "006013ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "006013ec",
      "DATA",
      [
        "storage",
        "00bf59f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006013ec",
      "DATA",
      [
        "storage",
        "00bf5a40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006013e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/006013d4.md#insn-006013e8)
- 新版 [`006013e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006013d4.md#insn-006013e8)

~~~diff
- 006013e8 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 006013e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006013e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006013e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006013e8 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 006013e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006013e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006013e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006013e8 bytes 08c12791
+ 006013e8 bytes 08012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f274c665d35a98f960f5b3bac03a402e"></a>

### [`006013f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/006013f8.md) → [`006013f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006013f8.md) FUN_006013f8

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
      "definition_site": "006013fc",
      "incomplete_value": false,
      "site": "00601400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006013fc",
      "incomplete_value": false,
      "site": "00601400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
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
      "00601400",
      "DATA",
      [
        "storage",
        "00bf59f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00601400",
      "DATA",
      [
        "storage",
        "00bf5a40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006013fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/006013f8.md#insn-006013fc)
- 新版 [`006013fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006013f8.md#insn-006013fc)

~~~diff
- 006013fc ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 006013fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006013fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006013fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006013fc ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 006013fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006013fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006013fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006013fc bytes 08c12791
+ 006013fc bytes 08012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f413ed311c5cf4fdf90fbd0deda9fbe8"></a>

### [`0060156c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/0060156c.md) → [`0060156c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/0060156c.md) FUN_0060156c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00601590",
      "incomplete_value": false,
      "site": "00601594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00601590",
      "incomplete_value": false,
      "site": "00601594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:a70:8"
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
      "00601594",
      "DATA",
      [
        "storage",
        "00bf5a70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00601594",
      "DATA",
      [
        "storage",
        "00bf5ac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00601590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/0060156c.md#insn-00601590)
- 新版 [`00601590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/0060156c.md#insn-00601590)

~~~diff
- 00601590 ["COPY", "tmp:0:8", ["const:a70:8"]]
- 00601590 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00601590 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00601590 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00601590 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 00601590 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00601590 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00601590 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00601590 bytes 08c12991
+ 00601590 bytes 08012b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df906cd8887e30c9a740e34b854a5d72"></a>

### [`006015ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/006015ac.md) → [`006015ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006015ac.md) FUN_006015ac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "006015b0",
      "incomplete_value": false,
      "site": "006015b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006015b0",
      "incomplete_value": false,
      "site": "006015b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:a70:8"
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
      "006015b4",
      "DATA",
      [
        "storage",
        "00bf5a70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006015b4",
      "DATA",
      [
        "storage",
        "00bf5ac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006015b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/006015ac.md#insn-006015b0)
- 新版 [`006015b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006015ac.md#insn-006015b0)

~~~diff
- 006015b0 ["COPY", "tmp:0:8", ["const:a70:8"]]
- 006015b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006015b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006015b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006015b0 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 006015b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006015b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006015b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006015b0 bytes 08c12991
+ 006015b0 bytes 08012b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d414f39e1e982fbbb2b17de90825b661"></a>

### [`006015d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/006015d4.md) → [`006015d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006015d4.md) FUN_006015d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 20件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 20件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006018d4",
      "incomplete_value": true,
      "site": "006018d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a84:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006018d4",
      "incomplete_value": true,
      "site": "006018d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b11:8"
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
      "definition_site": "00601910",
      "incomplete_value": true,
      "site": "00601910",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:687:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00601910",
      "incomplete_value": true,
      "site": "00601910",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:689:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00601960",
      "incomplete_value": true,
      "site": "00601960",
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
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00601960",
      "incomplete_value": true,
      "site": "00601960",
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
            "const:ae0:8"
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
      "006018c0",
      "READ",
      [
        "storage",
        "00293b11",
        null,
        "string"
      ]
    ],
    [
      "00601900",
      "READ",
      [
        "storage",
        "0029b689",
        null,
        "string"
      ]
    ],
    [
      "00601960",
      "DATA",
      [
        "storage",
        "00bf5ae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006018c0",
      "READ",
      [
        "storage",
        "00293a84",
        null,
        "string"
      ]
    ],
    [
      "00601900",
      "READ",
      [
        "storage",
        "0029b687",
        null,
        "string"
      ]
    ],
    [
      "00601960",
      "DATA",
      [
        "storage",
        "00bf5b30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006018b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/006015d4.md#insn-006018b8) · [`006018fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/006015d4.md#insn-006018fc) · [`00601958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/006015d4.md#insn-00601958)
- 新版 [`006018b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006015d4.md#insn-006018b8) · [`006018fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006015d4.md#insn-006018fc) · [`00601958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006015d4.md#insn-00601958)

~~~diff
- 006018b8 ["COPY", "tmp:0:8", ["const:b11:8"]]
- 006018b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006018b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006018b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006018b8 ["COPY", "tmp:0:8", ["const:a84:8"]]
+ 006018b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006018b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006018b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006018b8 bytes 29452c91
+ 006018b8 bytes 29112a91
- 006018fc ["COPY", "tmp:0:8", ["const:689:8"]]
- 006018fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006018fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006018fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006018fc ["COPY", "tmp:0:8", ["const:687:8"]]
+ 006018fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006018fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006018fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006018fc bytes 08251a91
+ 006018fc bytes 081d1a91
- 00601958 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00601958 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00601958 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00601958 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00601958 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 00601958 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00601958 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00601958 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00601958 bytes 29812b91
+ 00601958 bytes 29c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b69d4b6e1a2629a6da4b8f615ec7c8d2"></a>

### [`00601ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/00601ca4.md) → [`00601ca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601ca4.md) FUN_00601ca4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00601cc4",
      "incomplete_value": false,
      "site": "00601cc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00601cc4",
      "incomplete_value": false,
      "site": "00601cc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "00601cc8",
      "DATA",
      [
        "storage",
        "00bf5ae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00601cc8",
      "DATA",
      [
        "storage",
        "00bf5b30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00601cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/00601ca4.md#insn-00601cc4)
- 新版 [`00601cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601ca4.md#insn-00601cc4)

~~~diff
- 00601cc4 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00601cc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00601cc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00601cc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00601cc4 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 00601cc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00601cc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00601cc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00601cc4 bytes 08812b91
+ 00601cc4 bytes 08c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a64045a469ac8eee658ac53ed018b396"></a>

### [`00601cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/00601cdc.md) → [`00601cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601cdc.md) FUN_00601cdc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00601ce0",
      "incomplete_value": false,
      "site": "00601ce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00601ce0",
      "incomplete_value": false,
      "site": "00601ce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "00601ce4",
      "DATA",
      [
        "storage",
        "00bf5ae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00601ce4",
      "DATA",
      [
        "storage",
        "00bf5b30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00601ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/00601cdc.md#insn-00601ce0)
- 新版 [`00601ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601cdc.md#insn-00601ce0)

~~~diff
- 00601ce0 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00601ce0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00601ce0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00601ce0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00601ce0 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 00601ce0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00601ce0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00601ce0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00601ce0 bytes 08812b91
+ 00601ce0 bytes 08c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f754ab564d36f7369f1804ca61e4ff6"></a>

### [`00602140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/00602140.md) → [`00602140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/00602140.md) FUN_00602140

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
      "definition_site": "00602154",
      "incomplete_value": false,
      "site": "00602158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00602154",
      "incomplete_value": false,
      "site": "00602158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
      "00602158",
      "DATA",
      [
        "storage",
        "00bf5b70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00602158",
      "DATA",
      [
        "storage",
        "00bf5bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00602154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/00602140.md#insn-00602154)
- 新版 [`00602154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/00602140.md#insn-00602154)

~~~diff
- 00602154 ["COPY", "tmp:0:8", ["const:b70:8"]]
- 00602154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00602154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00602154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00602154 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 00602154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00602154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00602154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00602154 bytes 08c12d91
+ 00602154 bytes 08012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78b7362d741a4ec6369b75fd68713694"></a>

### [`00602164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/00602164.md) → [`00602164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/00602164.md) FUN_00602164

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
      "definition_site": "00602168",
      "incomplete_value": false,
      "site": "0060216c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00602168",
      "incomplete_value": false,
      "site": "0060216c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
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
      "0060216c",
      "DATA",
      [
        "storage",
        "00bf5b70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0060216c",
      "DATA",
      [
        "storage",
        "00bf5bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00602168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/00602164.md#insn-00602168)
- 新版 [`00602168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/00602164.md#insn-00602168)

~~~diff
- 00602168 ["COPY", "tmp:0:8", ["const:b70:8"]]
- 00602168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00602168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00602168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00602168 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 00602168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00602168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00602168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00602168 bytes 08c12d91
+ 00602168 bytes 08012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0c9d1ea878a1392835e42ef2885a304"></a>

### [`0060217c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/0060217c.md) → [`0060217c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/0060217c.md) FUN_0060217c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`006f1e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f1e2c.md) [`0088600c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/0088600c.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448034.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`006f1e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1e2c.md) [`0088600c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/0088600c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.31% / 新版 98.31%

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
      "definition_site": "006021c4",
      "incomplete_value": true,
      "site": "006021c4",
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
      "definition_site": "006021c4",
      "incomplete_value": true,
      "site": "006021c4",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006021cc",
      "incomplete_value": false,
      "site": "006021dc",
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
      "definition_site": "006021cc",
      "incomplete_value": false,
      "site": "006021dc",
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006021d4",
      "incomplete_value": false,
      "site": "006021dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006021d4",
      "incomplete_value": false,
      "site": "006021dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "006021c0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006021cc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006021d4",
      "PARAM",
      [
        "storage",
        "00bf4500",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006021c0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006021cc",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006021d4",
      "PARAM",
      [
        "storage",
        "00bf4550",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006021c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/0060217c.md#insn-006021c0) · [`006021cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/0060217c.md#insn-006021cc) · [`006021d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/0060217c.md#insn-006021d4)
- 新版 [`006021c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/0060217c.md#insn-006021c0) · [`006021cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/0060217c.md#insn-006021cc) · [`006021d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/0060217c.md#insn-006021d4)

~~~diff
- 006021c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006021c0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006021c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 006021c0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 006021c0 bytes 003d45f9
+ 006021c0 bytes 005d45f9
- 006021cc ["COPY", "tmp:0:8", ["const:e48:8"]]
- 006021cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006021cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006021cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006021cc ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 006021cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006021cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006021cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006021cc bytes 21203991
+ 006021cc bytes 21603a91
- 006021d4 ["COPY", "tmp:0:8", ["const:500:8"]]
- 006021d4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006021d4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006021d4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006021d4 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 006021d4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006021d4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006021d4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006021d4 bytes 42001491
+ 006021d4 bytes 42401591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e0810f9bf59d56aa5f6d7807b97d7c0"></a>

### [`00602380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/00602380.md) → [`00602380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/00602380.md) FUN_00602380

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
      "definition_site": "006023a4",
      "incomplete_value": false,
      "site": "006023a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006023a4",
      "incomplete_value": false,
      "site": "006023a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:c00:8"
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
      "006023a4",
      "DATA",
      [
        "storage",
        "00bf5c00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006023a4",
      "DATA",
      [
        "storage",
        "00bf5c50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006023a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/00602380.md#insn-006023a0)
- 新版 [`006023a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/00602380.md#insn-006023a0)

~~~diff
- 006023a0 ["COPY", "tmp:0:8", ["const:c00:8"]]
- 006023a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006023a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006023a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006023a0 ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 006023a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006023a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006023a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006023a0 bytes 08013091
+ 006023a0 bytes 08413191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-976fbfa85ed98b7e8dd2dec3aedf0ec9"></a>

### [`006023b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/006023b4.md) → [`006023b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/006023b4.md) FUN_006023b4

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
      "definition_site": "006023c0",
      "incomplete_value": false,
      "site": "006023c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006023c0",
      "incomplete_value": false,
      "site": "006023c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:c00:8"
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
      "006023c0",
      "DATA",
      [
        "storage",
        "00bf5c00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006023c0",
      "DATA",
      [
        "storage",
        "00bf5c50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006023bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/006023b4.md#insn-006023bc)
- 新版 [`006023bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/006023b4.md#insn-006023bc)

~~~diff
- 006023bc ["COPY", "tmp:0:8", ["const:c00:8"]]
- 006023bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006023bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006023bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006023bc ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 006023bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006023bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006023bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006023bc bytes 29013091
+ 006023bc bytes 29413191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14e75aa5d9456c7dd0b91d88eac63a4c"></a>

### [`00602628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/00602628.md) → [`00602628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/00602628.md) FUN_00602628

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0060245c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/0060245c.md) [`00602628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/00602628.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0060245c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/0060245c.md) [`00602628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/00602628.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.93% / 新版 98.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0060279c",
      "incomplete_value": false,
      "site": "006027a8",
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
      "definition_site": "0060279c",
      "incomplete_value": false,
      "site": "006027a8",
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
      "definition_site": "00602854",
      "incomplete_value": false,
      "site": "0060285c",
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
      "definition_site": "00602854",
      "incomplete_value": false,
      "site": "0060285c",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00602920",
      "incomplete_value": false,
      "site": "00602930",
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
      "definition_site": "00602920",
      "incomplete_value": false,
      "site": "00602930",
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
      "0060279c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00602854",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0060286c",
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
      "0060279c",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00602854",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "0060286c",
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

- 旧版 [`0060279c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/00602628.md#insn-0060279c) · [`00602854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/00602628.md#insn-00602854) · [`0060286c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/00602628.md#insn-0060286c)
- 新版 [`0060279c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/00602628.md#insn-0060279c) · [`00602854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/00602628.md#insn-00602854) · [`0060286c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/00602628.md#insn-0060286c)

~~~diff
- 0060279c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0060279c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0060279c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0060279c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0060279c ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0060279c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0060279c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0060279c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0060279c bytes 21280c91
+ 0060279c bytes 21900e91
- 00602854 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00602854 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00602854 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00602854 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00602854 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00602854 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00602854 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00602854 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00602854 bytes 21b80b91
+ 00602854 bytes 21e40d91
- 0060286c ["COPY", "tmp:0:8", ["const:919:8"]]
- 0060286c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0060286c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0060286c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0060286c ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0060286c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0060286c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0060286c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0060286c bytes 21642491
+ 0060286c bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d56e1a67b72ada28d244d24fb5ea33ba"></a>

### [`0060320c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00603/0060320c.md) → [`0060320c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00603/0060320c.md) FUN_0060320c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00602628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/00602628.md) [`0060320c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00603/0060320c.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00602628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/00602628.md) [`0060320c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00603/0060320c.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.81% / 新版 98.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00603380",
      "incomplete_value": false,
      "site": "00603388",
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
      "definition_site": "00603380",
      "incomplete_value": false,
      "site": "00603388",
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
      "definition_site": "00603440",
      "incomplete_value": false,
      "site": "00603448",
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
      "definition_site": "00603440",
      "incomplete_value": false,
      "site": "00603448",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0060350c",
      "incomplete_value": false,
      "site": "00603518",
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
      "definition_site": "0060350c",
      "incomplete_value": false,
      "site": "00603518",
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
      "00603380",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00603440",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0060345c",
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
      "00603380",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00603440",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "0060345c",
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

- 旧版 [`00603380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00603/0060320c.md#insn-00603380) · [`00603440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00603/0060320c.md#insn-00603440) · [`0060345c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00603/0060320c.md#insn-0060345c)
- 新版 [`00603380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00603/0060320c.md#insn-00603380) · [`00603440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00603/0060320c.md#insn-00603440) · [`0060345c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00603/0060320c.md#insn-0060345c)

~~~diff
- 00603380 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00603380 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00603380 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00603380 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00603380 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00603380 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00603380 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00603380 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00603380 bytes 21280c91
+ 00603380 bytes 21900e91
- 00603440 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00603440 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00603440 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00603440 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00603440 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00603440 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00603440 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00603440 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00603440 bytes 21b80b91
+ 00603440 bytes 21e40d91
- 0060345c ["COPY", "tmp:0:8", ["const:919:8"]]
- 0060345c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0060345c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0060345c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0060345c ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0060345c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0060345c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0060345c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0060345c bytes 21642491
+ 0060345c bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7323b7642a23a6da6ad1d76a2870d4f0"></a>

### [`00603c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00603/00603c60.md) → [`00603c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00603/00603c60.md) _INIT_74

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
      "definition_site": "00603c9c",
      "incomplete_value": true,
      "site": "00603cb8",
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
      "definition_site": "00603c9c",
      "incomplete_value": true,
      "site": "00603cb8",
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
      "definition_site": "00603cc0",
      "incomplete_value": true,
      "site": "00603cdc",
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
      "definition_site": "00603cc0",
      "incomplete_value": true,
      "site": "00603cdc",
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
      "definition_site": "00603d00",
      "incomplete_value": true,
      "site": "00603d18",
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
      "definition_site": "00603d00",
      "incomplete_value": true,
      "site": "00603d18",
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
      "00603c9c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00603cc0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00603ce0",
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
      "00603c9c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00603cc0",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00603ce0",
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

- 旧版 [`00603c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00603/00603c60.md#insn-00603c8c) · [`00603c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00603/00603c60.md#insn-00603c94)
- 新版 [`00603c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00603/00603c60.md#insn-00603c8c) · [`00603c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00603/00603c60.md#insn-00603c94)

~~~diff
- 00603c8c ["COPY", "tmp:0:8", ["const:a98:8"]]
- 00603c8c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00603c8c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00603c8c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00603c8c ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 00603c8c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00603c8c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00603c8c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00603c8c bytes 73622a91
+ 00603c8c bytes 73622b91
- 00603c94 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00603c94 bytes 29e5ff90
+ 00603c94 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00603c94 bytes 29e5ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4cd900783b2cb76b926fb2c3e13e2a7"></a>

### [`00604288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/00604288.md) → [`00604288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604288.md) FUN_00604288

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00996eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00996/00996eec.md) · 呼出先 6件 [`004662bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00466/004662bc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00996eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996eec.md) · 呼出先 6件 [`004662bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004662bc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.35% / 新版 94.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00604318",
      "incomplete_value": true,
      "site": "00604328",
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
                "const:298000:8"
              ],
              [
                "leaf",
                "const:fc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00604318",
      "incomplete_value": true,
      "site": "00604328",
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
                "const:55:8"
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
      "definition_site": "006043f8",
      "incomplete_value": true,
      "site": "006043f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:f46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006043f8",
      "incomplete_value": true,
      "site": "006043f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:f48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006043fc",
      "incomplete_value": true,
      "site": "006043fc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006043fc",
      "incomplete_value": true,
      "site": "006043fc",
      "value": [
        "LOAD",
        "8",
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
      "00604318",
      "READ",
      [
        "storage",
        "00299055",
        null,
        "string"
      ]
    ],
    [
      "006043cc",
      "READ",
      [
        "storage",
        "002aeb9c",
        null,
        "string"
      ]
    ],
    [
      "006043ec",
      "READ",
      [
        "storage",
        "00299f48",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00604318",
      "READ",
      [
        "storage",
        "00298fc8",
        null,
        "string"
      ]
    ],
    [
      "006043cc",
      "READ",
      [
        "storage",
        "002aeb08",
        null,
        "string"
      ]
    ],
    [
      "006043ec",
      "READ",
      [
        "storage",
        "00299f46",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0060430c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/00604288.md#insn-0060430c) · [`00604310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/00604288.md#insn-00604310) · [`006043c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/00604288.md#insn-006043c8)
- 新版 [`0060430c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604288.md#insn-0060430c) · [`00604310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604288.md#insn-00604310) · [`006043c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604288.md#insn-006043c8)

~~~diff
- 0060430c ["COPY", "register:4040:8", ["const:299000:8"]]
+ 0060430c ["COPY", "register:4040:8", ["const:298000:8"]]
- 0060430c bytes a8e4ffb0
+ 0060430c bytes a8e4ff90
- 00604310 ["COPY", "tmp:0:8", ["const:55:8"]]
- 00604310 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00604310 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00604310 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00604310 ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 00604310 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00604310 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00604310 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00604310 bytes 08550191
+ 00604310 bytes 08213f91
- 006043c8 ["COPY", "tmp:0:8", ["const:b9c:8"]]
- 006043c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006043c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006043c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006043c8 ["COPY", "tmp:0:8", ["const:b08:8"]]
+ 006043c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006043c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006043c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006043c8 bytes 08712e91
+ 006043c8 bytes 08212c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4429a13de177f55fae2cf37714c1f5d8"></a>

### [`0060496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/0060496c.md) → [`0060496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/0060496c.md) _INIT_75

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
      "definition_site": "006049a8",
      "incomplete_value": true,
      "site": "006049c4",
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
      "definition_site": "006049a8",
      "incomplete_value": true,
      "site": "006049c4",
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
      "definition_site": "006049cc",
      "incomplete_value": true,
      "site": "006049e8",
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
      "definition_site": "006049cc",
      "incomplete_value": true,
      "site": "006049e8",
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
      "definition_site": "006049ec",
      "incomplete_value": true,
      "site": "00604a08",
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
      "definition_site": "006049ec",
      "incomplete_value": true,
      "site": "00604a08",
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
      "006049a8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "006049cc",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "006049ec",
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
      "006049a8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "006049cc",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "006049ec",
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

- 旧版 [`00604998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/0060496c.md#insn-00604998) · [`006049a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/0060496c.md#insn-006049a0)
- 新版 [`00604998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/0060496c.md#insn-00604998) · [`006049a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/0060496c.md#insn-006049a0)

~~~diff
- 00604998 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 00604998 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00604998 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00604998 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00604998 ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 00604998 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00604998 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00604998 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00604998 bytes 73c22a91
+ 00604998 bytes 73c22b91
- 006049a0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 006049a0 bytes 09e5fff0
+ 006049a0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 006049a0 bytes 09e5fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ca2eefc0e0d8a093afae63d41f790da"></a>

### [`00604cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/00604cfc.md) → [`00604cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604cfc.md) FUN_00604cfc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0060553c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00605/0060553c.md) · 呼出先 19件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00609f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00609/00609f20.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`0060553c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/0060553c.md) · 呼出先 19件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00609f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00609/00609f20.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.19% / 新版 90.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00604f14",
      "incomplete_value": true,
      "site": "00604f24",
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00604f14",
      "incomplete_value": true,
      "site": "00604f24",
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
                "const:74d:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00605024",
      "incomplete_value": false,
      "site": "00605024",
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
      "definition_site": "00605024",
      "incomplete_value": false,
      "site": "00605024",
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
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00605028",
      "incomplete_value": false,
      "site": "00605028",
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
      "definition_site": "00605028",
      "incomplete_value": false,
      "site": "00605028",
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
    "ordinal": 21,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00604dd4",
      "READ",
      [
        "storage",
        "00299f56",
        null,
        "string"
      ]
    ],
    [
      "00604f00",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00604f14",
      "READ",
      [
        "storage",
        "002a474d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00604dd4",
      "READ",
      [
        "storage",
        "00299f54",
        null,
        "string"
      ]
    ],
    [
      "00604f00",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00604f14",
      "READ",
      [
        "storage",
        "002a47d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00604dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/00604cfc.md#insn-00604dcc) · [`00604efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/00604cfc.md#insn-00604efc) · [`00604f0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/00604cfc.md#insn-00604f0c)
- 新版 [`00604dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604cfc.md#insn-00604dcc) · [`00604efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604cfc.md#insn-00604efc) · [`00604f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604cfc.md#insn-00604f0c)

~~~diff
- 00604dcc ["COPY", "tmp:0:8", ["const:f56:8"]]
- 00604dcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00604dcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00604dcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00604dcc ["COPY", "tmp:0:8", ["const:f54:8"]]
+ 00604dcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00604dcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00604dcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00604dcc bytes 29593d91
+ 00604dcc bytes 29513d91
- 00604efc ["COPY", "tmp:0:8", ["const:38:8"]]
- 00604efc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00604efc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00604efc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00604efc ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00604efc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00604efc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00604efc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00604efc bytes 08e10091
+ 00604efc bytes 08e10191
- 00604f0c ["COPY", "tmp:0:8", ["const:74d:8"]]
- 00604f0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00604f0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00604f0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00604f0c ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 00604f0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00604f0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00604f0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00604f0c bytes 29351d91
+ 00604f0c bytes 29611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5540a5227cb005a213e49aa726c97d5"></a>

### [`0060553c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00605/0060553c.md) → [`0060553c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/0060553c.md) FUN_0060553c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00608668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00608/00608668.md) · 呼出先 20件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`00604cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/00604cfc.md) [`006050b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00605/006050b4.md)
- 新版 呼出元 1件 [`00608668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608668.md) · 呼出先 20件 [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`00604cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604cfc.md) [`006050b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/006050b4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.04% / 新版 95.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00605774",
      "incomplete_value": false,
      "site": "00605788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00605774",
      "incomplete_value": false,
      "site": "00605788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:c80:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006058ac",
      "incomplete_value": false,
      "site": "006058b0",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006058ac",
      "incomplete_value": false,
      "site": "006058b0",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006058d0",
      "incomplete_value": false,
      "site": "006058ec",
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
      "definition_site": "006058d0",
      "incomplete_value": false,
      "site": "006058ec",
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
    "ordinal": 38,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00605574",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00605588",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "0060558c",
      "READ",
      [
        "storage",
        "00c1ae50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00605574",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00605588",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ],
    [
      "0060558c",
      "READ",
      [
        "storage",
        "00c1aea0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00605568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00605/0060553c.md#insn-00605568) · [`00605588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00605/0060553c.md#insn-00605588) · [`0060558c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00605/0060553c.md#insn-0060558c)
- 新版 [`00605568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/0060553c.md#insn-00605568) · [`00605588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/0060553c.md#insn-00605588) · [`0060558c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/0060553c.md#insn-0060558c)

~~~diff
- 00605568 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00605568 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00605568 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00605568 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00605568 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00605568 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00605568 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00605568 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00605568 bytes 08e10091
+ 00605568 bytes 08e10191
- 00605588 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00605588 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00605588 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00605588 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00605588 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 00605588 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00605588 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00605588 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00605588 bytes 00000091
+ 00605588 bytes 00000191
- 0060558c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:e50:8"]]
- 0060558c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 0060558c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:ea0:8"]]
+ 0060558c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 0060558c bytes 422847f9
+ 0060558c bytes 425047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61ae53bd2a3f6041190adb164fb43702"></a>

### [`00605bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00605/00605bdc.md) → [`00605bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/00605bdc.md) FUN_00605bdc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`006091c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00609/006091c4.md) [`0060afa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060a/0060afa4.md) · 呼出先 10件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00428648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428648.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046ede4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046e/0046ede4.md) [`00605f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00605/00605f28.md)
- 新版 呼出元 2件 [`006091c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00609/006091c4.md) [`0060afa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060a/0060afa4.md) · 呼出先 10件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00428648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428648.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046ede4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046e/0046ede4.md) [`00605f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/00605f28.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00605cb4",
      "incomplete_value": false,
      "site": "00605cbc",
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
            "const:803:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00605cb4",
      "incomplete_value": false,
      "site": "00605cbc",
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
            "const:778:8"
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
      "definition_site": "00605d28",
      "incomplete_value": false,
      "site": "00605d30",
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
            "const:1a1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00605d28",
      "incomplete_value": false,
      "site": "00605d30",
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
            "const:116:8"
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
      "00605cb4",
      "PARAM",
      [
        "storage",
        "002a1778",
        null,
        "string"
      ]
    ],
    [
      "00605d28",
      "PARAM",
      [
        "storage",
        "002a3116",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00605cb4",
      "PARAM",
      [
        "storage",
        "002a1803",
        null,
        "string"
      ]
    ],
    [
      "00605d28",
      "PARAM",
      [
        "storage",
        "002a31a1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00605cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00605/00605bdc.md#insn-00605cb4) · [`00605d28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00605/00605bdc.md#insn-00605d28)
- 新版 [`00605cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/00605bdc.md#insn-00605cb4) · [`00605d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/00605bdc.md#insn-00605d28)

~~~diff
- 00605cb4 ["COPY", "tmp:0:8", ["const:778:8"]]
- 00605cb4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00605cb4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00605cb4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00605cb4 ["COPY", "tmp:0:8", ["const:803:8"]]
+ 00605cb4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00605cb4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00605cb4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00605cb4 bytes 21e01d91
+ 00605cb4 bytes 210c2091
- 00605d28 ["COPY", "tmp:0:8", ["const:116:8"]]
- 00605d28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00605d28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00605d28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00605d28 ["COPY", "tmp:0:8", ["const:1a1:8"]]
+ 00605d28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00605d28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00605d28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00605d28 bytes 21580491
+ 00605d28 bytes 21840691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f92d3736cf42abdb3615805ad008ba55"></a>

### [`006062a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00606/006062a4.md) → [`006062a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00606/006062a4.md) FUN_006062a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00608668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00608/00608668.md) · 呼出先 7件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a25194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a25194.md) [`00a25380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a25380.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00608668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608668.md) · 呼出先 7件 [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a251d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a25/00a251d8.md) [`00a253c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a25/00a253c4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.09% / 新版 97.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00606300",
      "incomplete_value": false,
      "site": "00606308",
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
            "const:7ea:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00606300",
      "incomplete_value": false,
      "site": "00606308",
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
            "const:75f:8"
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
      "definition_site": "006063c4",
      "incomplete_value": false,
      "site": "006063cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:84f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006063c4",
      "incomplete_value": false,
      "site": "006063cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:7c4:8"
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
      "00606300",
      "PARAM",
      [
        "storage",
        "002a475f",
        null,
        "string"
      ]
    ],
    [
      "0060637c",
      "PARAM",
      [
        "storage",
        "002a25f0",
        null,
        "string"
      ]
    ],
    [
      "006063c4",
      "PARAM",
      [
        "storage",
        "0029c7c4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00606300",
      "PARAM",
      [
        "storage",
        "002a47ea",
        null,
        "string"
      ]
    ],
    [
      "0060637c",
      "PARAM",
      [
        "storage",
        "002a267b",
        null,
        "string"
      ]
    ],
    [
      "006063c4",
      "PARAM",
      [
        "storage",
        "0029c84f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00606300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00606/006062a4.md#insn-00606300) · [`00606338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00606/006062a4.md#insn-00606338) · [`006063c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00606/006062a4.md#insn-006063c4)
- 新版 [`00606300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00606/006062a4.md#insn-00606300) · [`00606338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00606/006062a4.md#insn-00606338) · [`006063c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00606/006062a4.md#insn-006063c4)

~~~diff
- 00606300 ["COPY", "tmp:0:8", ["const:75f:8"]]
- 00606300 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00606300 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00606300 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00606300 ["COPY", "tmp:0:8", ["const:7ea:8"]]
+ 00606300 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00606300 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00606300 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00606300 bytes 217c1d91
+ 00606300 bytes 21a81f91
- 00606338 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 00606338 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 00606338 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 00606338 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 00606338 ["COPY", "tmp:0:8", ["const:67b:8"]]
+ 00606338 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 00606338 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 00606338 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 00606338 bytes f7c21791
+ 00606338 bytes f7ee1991
- 006063c4 ["COPY", "tmp:0:8", ["const:7c4:8"]]
- 006063c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006063c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006063c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006063c4 ["COPY", "tmp:0:8", ["const:84f:8"]]
+ 006063c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006063c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006063c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006063c4 bytes 21101f91
+ 006063c4 bytes 213c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57302d2744d3661a57469041affb1b1c"></a>

### [`00607ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00607/00607ac8.md) → [`00607ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00607/00607ac8.md) FUN_00607ac8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00608668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00608/00608668.md) · 呼出先 24件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md)
- 新版 呼出元 1件 [`00608668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608668.md) · 呼出先 24件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md)

変更の種類 comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00607b0c",
      "incomplete_value": false,
      "site": "00607b18",
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
      "definition_site": "00607b0c",
      "incomplete_value": false,
      "site": "00607b18",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00608270"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00608274"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00607b18",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "0060804c",
      "PARAM",
      [
        "storage",
        "0029c7d8",
        null,
        null
      ]
    ],
    [
      "unmatched:00608260",
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
      "00607b18",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "0060804c",
      "PARAM",
      [
        "storage",
        "0029c863",
        null,
        null
      ]
    ],
    [
      "00608260",
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

- 旧版 [`00608270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00607/00607ac8.md#insn-00608270) · [`00608274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00607/00607ac8.md#insn-00608274)
- 新版 [`00608270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00607/00607ac8.md#insn-00608270)

~~~diff
- 00608270 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00608270 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00608270 bytes e81700f9
+ 00608270 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
+ 00608270 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00608270 bytes e81700f9
- 00608274 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:70:8"]]
- 00608274 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00608274 bytes e93b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98aad8ef8e2b0712c14c807f78225c48"></a>

### [`00608668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00608/00608668.md) → [`00608668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608668.md) FUN_00608668

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00604050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/00604050.md) [`006041b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/006041b0.md) · 呼出先 25件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`0060553c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00605/0060553c.md)
- 新版 呼出元 2件 [`00604050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604050.md) [`006041b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/006041b0.md) · 呼出先 25件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`0060553c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/0060553c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.12% / 新版 99.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00608e8c",
      "incomplete_value": false,
      "site": "00608e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00608e8c",
      "incomplete_value": false,
      "site": "00608e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "ordinal": 98,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00608fb8",
      "incomplete_value": false,
      "site": "00608fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00608fb8",
      "incomplete_value": false,
      "site": "00608fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "ordinal": 107,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00608d14",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "00608d28",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ],
    [
      "00608d40",
      "READ",
      [
        "storage",
        "00c1b528",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00608d14",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ],
    [
      "00608d28",
      "DATA",
      [
        "storage",
        "00c0bd38",
        null,
        "undefined *"
      ]
    ],
    [
      "00608d40",
      "READ",
      [
        "storage",
        "00c1b578",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00608d14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00608/00608668.md#insn-00608d14) · [`00608d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00608/00608668.md#insn-00608d40) · [`00608e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00608/00608668.md#insn-00608e84)
- 新版 [`00608d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608668.md#insn-00608d14) · [`00608d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608668.md#insn-00608d40) · [`00608e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608668.md#insn-00608e84)

~~~diff
- 00608d14 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:520:8"]]
- 00608d14 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00608d14 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:570:8"]]
+ 00608d14 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00608d14 bytes b59242f9
+ 00608d14 bytes b5ba42f9
- 00608d40 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:528:8"]]
- 00608d40 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00608d40 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:578:8"]]
+ 00608d40 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 00608d40 bytes d69642f9
+ 00608d40 bytes d6be42f9
- 00608e84 ["COPY", "tmp:0:8", ["const:d00:8"]]
- 00608e84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00608e84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00608e84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00608e84 ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 00608e84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00608e84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00608e84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00608e84 bytes 29013491
+ 00608e84 bytes 29413591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53ce9a6c631b468a54ff32e6d0318fd5"></a>

### [`006091c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00609/006091c4.md) → [`006091c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00609/006091c4.md) FUN_006091c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006041b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/006041b0.md) · 呼出先 23件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00428648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428648.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`006041b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/006041b0.md) · 呼出先 23件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00428648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428648.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.74% / 新版 98.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00609270",
      "incomplete_value": true,
      "site": "00609278",
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
            "const:a96:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00609270",
      "incomplete_value": true,
      "site": "00609278",
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
            "const:9fc:8"
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
      "definition_site": "00609590",
      "incomplete_value": false,
      "site": "006095a8",
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
            "const:7ea:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00609590",
      "incomplete_value": false,
      "site": "006095a8",
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
            "const:75f:8"
          ]
        ]
      ]
    },
    "ordinal": 45,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00609654",
      "incomplete_value": false,
      "site": "0060965c",
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
            "const:7ea:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00609654",
      "incomplete_value": false,
      "site": "0060965c",
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
            "const:75f:8"
          ]
        ]
      ]
    },
    "ordinal": 57,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00609270",
      "PARAM",
      [
        "storage",
        "002a69fc",
        null,
        "string"
      ]
    ],
    [
      "00609590",
      "PARAM",
      [
        "storage",
        "002a475f",
        null,
        "string"
      ]
    ],
    [
      "006095d0",
      "PARAM",
      [
        "storage",
        "00299f68",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00609270",
      "PARAM",
      [
        "storage",
        "002a6a96",
        null,
        "string"
      ]
    ],
    [
      "00609590",
      "PARAM",
      [
        "storage",
        "002a47ea",
        null,
        "string"
      ]
    ],
    [
      "006095d0",
      "PARAM",
      [
        "storage",
        "00299f66",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00609270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00609/006091c4.md#insn-00609270) · [`00609590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00609/006091c4.md#insn-00609590) · [`006095d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00609/006091c4.md#insn-006095d0)
- 新版 [`00609270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00609/006091c4.md#insn-00609270) · [`00609590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00609/006091c4.md#insn-00609590) · [`006095d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00609/006091c4.md#insn-006095d0)

~~~diff
- 00609270 ["COPY", "tmp:0:8", ["const:9fc:8"]]
- 00609270 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00609270 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00609270 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00609270 ["COPY", "tmp:0:8", ["const:a96:8"]]
+ 00609270 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00609270 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00609270 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00609270 bytes 21f02791
+ 00609270 bytes 21582a91
- 00609590 ["COPY", "tmp:0:8", ["const:75f:8"]]
- 00609590 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00609590 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00609590 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00609590 ["COPY", "tmp:0:8", ["const:7ea:8"]]
+ 00609590 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00609590 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00609590 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00609590 bytes 217c1d91
+ 00609590 bytes 21a81f91
- 006095d0 ["COPY", "tmp:0:8", ["const:f68:8"]]
- 006095d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006095d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006095d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006095d0 ["COPY", "tmp:0:8", ["const:f66:8"]]
+ 006095d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006095d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006095d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006095d0 bytes 21a03d91
+ 006095d0 bytes 21983d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8710170e8cefe3d684e913e9005923f"></a>

### [`00609f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00609/00609f20.md) → [`00609f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00609/00609f20.md) FUN_00609f20

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00604cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/00604cfc.md) [`00609f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00609/00609f20.md) [`008648a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md) [`0087cfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087c/0087cfbc.md) [`00979104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00979/00979104.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 5件 [`00604cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604cfc.md) [`00609f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00609/00609f20.md) [`008648a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008648a8.md) [`0087cfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087c/0087cfbc.md) [`00979104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979104.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.52% / 新版 98.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0060a080",
      "incomplete_value": false,
      "site": "0060a088",
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
      "definition_site": "0060a080",
      "incomplete_value": false,
      "site": "0060a088",
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
      "definition_site": "0060a0a4",
      "incomplete_value": false,
      "site": "0060a0b0",
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
      "definition_site": "0060a0a4",
      "incomplete_value": false,
      "site": "0060a0b0",
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
      "definition_site": "0060a280",
      "incomplete_value": false,
      "site": "0060a28c",
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
      "definition_site": "0060a280",
      "incomplete_value": false,
      "site": "0060a28c",
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
      "0060a080",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0060a0a4",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "0060a1d8",
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
      "0060a080",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0060a0a4",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0060a1d8",
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

- 旧版 [`0060a080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00609/00609f20.md#insn-0060a080) · [`0060a0a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00609/00609f20.md#insn-0060a0a4) · [`0060a1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00609/00609f20.md#insn-0060a1d8)
- 新版 [`0060a080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00609/00609f20.md#insn-0060a080) · [`0060a0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00609/00609f20.md#insn-0060a0a4) · [`0060a1d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00609/00609f20.md#insn-0060a1d8)

~~~diff
- 0060a080 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0060a080 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0060a080 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0060a080 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0060a080 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0060a080 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0060a080 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0060a080 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0060a080 bytes 21280c91
+ 0060a080 bytes 21900e91
- 0060a0a4 ["COPY", "tmp:0:8", ["const:919:8"]]
- 0060a0a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0060a0a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0060a0a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0060a0a4 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0060a0a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0060a0a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0060a0a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0060a0a4 bytes 21642491
+ 0060a0a4 bytes 21142291
- 0060a1d8 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0060a1d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0060a1d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0060a1d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0060a1d8 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0060a1d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0060a1d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0060a1d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0060a1d8 bytes 21b80b91
+ 0060a1d8 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e4165c3d0dc29d8585a09705370db4e"></a>

### [`0060a74c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060a/0060a74c.md) → [`0060a74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060a/0060a74c.md) FUN_0060a74c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`00609f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00609/00609f20.md) [`0060a74c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060a/0060a74c.md) [`0076e98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076e/0076e98c.md) [`008648a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md) [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 7件 [`00609f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00609/00609f20.md) [`0060a74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060a/0060a74c.md) [`0076e98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e98c.md) [`008648a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008648a8.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.50% / 新版 98.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0060a8a8",
      "incomplete_value": false,
      "site": "0060a8b0",
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
      "definition_site": "0060a8a8",
      "incomplete_value": false,
      "site": "0060a8b0",
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
      "definition_site": "0060a8cc",
      "incomplete_value": false,
      "site": "0060a8d8",
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
      "definition_site": "0060a8cc",
      "incomplete_value": false,
      "site": "0060a8d8",
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
      "definition_site": "0060aa00",
      "incomplete_value": false,
      "site": "0060aa08",
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
      "definition_site": "0060aa00",
      "incomplete_value": false,
      "site": "0060aa08",
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
      "0060a8a8",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0060a8cc",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "0060aa00",
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
      "0060a8a8",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0060a8cc",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0060aa00",
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

- 旧版 [`0060a8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060a/0060a74c.md#insn-0060a8a8) · [`0060a8cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060a/0060a74c.md#insn-0060a8cc) · [`0060aa00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060a/0060a74c.md#insn-0060aa00)
- 新版 [`0060a8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060a/0060a74c.md#insn-0060a8a8) · [`0060a8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060a/0060a74c.md#insn-0060a8cc) · [`0060aa00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060a/0060a74c.md#insn-0060aa00)

~~~diff
- 0060a8a8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0060a8a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0060a8a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0060a8a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0060a8a8 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0060a8a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0060a8a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0060a8a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0060a8a8 bytes 21280c91
+ 0060a8a8 bytes 21900e91
- 0060a8cc ["COPY", "tmp:0:8", ["const:919:8"]]
- 0060a8cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0060a8cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0060a8cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0060a8cc ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0060a8cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0060a8cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0060a8cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0060a8cc bytes 21642491
+ 0060a8cc bytes 21142291
- 0060aa00 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0060aa00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0060aa00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0060aa00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0060aa00 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0060aa00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0060aa00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0060aa00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0060aa00 bytes 21b80b91
+ 0060aa00 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bd65aea0e1aca873d9ee02300124509"></a>

### [`0060af68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060a/0060af68.md) → [`0060af68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060a/0060af68.md) FUN_0060af68

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
      "definition_site": "0060af7c",
      "incomplete_value": false,
      "site": "0060af80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060af7c",
      "incomplete_value": false,
      "site": "0060af80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:c80:8"
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
      "0060af80",
      "DATA",
      [
        "storage",
        "00bf5c80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0060af80",
      "DATA",
      [
        "storage",
        "00bf5cd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0060af7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060a/0060af68.md#insn-0060af7c)
- 新版 [`0060af7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060a/0060af68.md#insn-0060af7c)

~~~diff
- 0060af7c ["COPY", "tmp:0:8", ["const:c80:8"]]
- 0060af7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0060af7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0060af7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0060af7c ["COPY", "tmp:0:8", ["const:cd0:8"]]
+ 0060af7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0060af7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0060af7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0060af7c bytes 08013291
+ 0060af7c bytes 08413391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7612819ef4192dd544e0a8531dadba92"></a>

### [`0060af8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060a/0060af8c.md) → [`0060af8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060a/0060af8c.md) FUN_0060af8c

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
      "definition_site": "0060af90",
      "incomplete_value": false,
      "site": "0060af94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060af90",
      "incomplete_value": false,
      "site": "0060af94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:c80:8"
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
      "0060af94",
      "DATA",
      [
        "storage",
        "00bf5c80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0060af94",
      "DATA",
      [
        "storage",
        "00bf5cd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0060af90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060a/0060af8c.md#insn-0060af90)
- 新版 [`0060af90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060a/0060af8c.md#insn-0060af90)

~~~diff
- 0060af90 ["COPY", "tmp:0:8", ["const:c80:8"]]
- 0060af90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0060af90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0060af90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0060af90 ["COPY", "tmp:0:8", ["const:cd0:8"]]
+ 0060af90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0060af90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0060af90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0060af90 bytes 08013291
+ 0060af90 bytes 08413391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be47ed058f33740b94f354fdc5ca1ac6"></a>

### [`0060b0e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060b/0060b0e8.md) → [`0060b0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b0e8.md) FUN_0060b0e8

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
      "definition_site": "0060b0fc",
      "incomplete_value": false,
      "site": "0060b100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060b0fc",
      "incomplete_value": false,
      "site": "0060b100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:d00:8"
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
      "0060b100",
      "DATA",
      [
        "storage",
        "00bf5d00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0060b100",
      "DATA",
      [
        "storage",
        "00bf5d50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0060b0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060b/0060b0e8.md#insn-0060b0fc)
- 新版 [`0060b0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b0e8.md#insn-0060b0fc)

~~~diff
- 0060b0fc ["COPY", "tmp:0:8", ["const:d00:8"]]
- 0060b0fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0060b0fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0060b0fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0060b0fc ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 0060b0fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0060b0fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0060b0fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0060b0fc bytes 08013491
+ 0060b0fc bytes 08413591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fc0de68e8e9d39ac246341c4e5cf84d"></a>

### [`0060b10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060b/0060b10c.md) → [`0060b10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b10c.md) FUN_0060b10c

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
      "definition_site": "0060b110",
      "incomplete_value": false,
      "site": "0060b114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060b110",
      "incomplete_value": false,
      "site": "0060b114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:d00:8"
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
      "0060b114",
      "DATA",
      [
        "storage",
        "00bf5d00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0060b114",
      "DATA",
      [
        "storage",
        "00bf5d50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0060b110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060b/0060b10c.md#insn-0060b110)
- 新版 [`0060b110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b10c.md#insn-0060b110)

~~~diff
- 0060b110 ["COPY", "tmp:0:8", ["const:d00:8"]]
- 0060b110 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0060b110 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0060b110 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0060b110 ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 0060b110 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0060b110 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0060b110 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0060b110 bytes 08013491
+ 0060b110 bytes 08413591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6838954cc226dbd61328975ee259ad14"></a>

### [`0060b280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060b/0060b280.md) → [`0060b280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b280.md) FUN_0060b280

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
      "definition_site": "0060b294",
      "incomplete_value": false,
      "site": "0060b298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060b294",
      "incomplete_value": false,
      "site": "0060b298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:d80:8"
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
      "0060b298",
      "DATA",
      [
        "storage",
        "00bf5d80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0060b298",
      "DATA",
      [
        "storage",
        "00bf5dd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0060b294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060b/0060b280.md#insn-0060b294)
- 新版 [`0060b294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b280.md#insn-0060b294)

~~~diff
- 0060b294 ["COPY", "tmp:0:8", ["const:d80:8"]]
- 0060b294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0060b294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0060b294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0060b294 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 0060b294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0060b294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0060b294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0060b294 bytes 08013691
+ 0060b294 bytes 08413791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

