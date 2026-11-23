# v15.7.3 → v15.7.4 · 最優先の変更候補 (8)

[一覧の目次](README.md)

<a id="compare-f352c1031f70c4353cedbcad4abc2dce"></a>

### [`00499b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499b28.md) → [`00499b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499b28.md) FUN_00499b28

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`00499b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499b20.md) [`0049c56c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c56c.md) [`004a1190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1190.md) [`004a15d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a15d0.md) [`004a1e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1e34.md) · 呼出先 5件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdbee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbee0.md)
- 新版 呼出元 10件 [`00499b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499b20.md) [`0049c56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c56c.md) [`004a1190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1190.md) [`004a15d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a15d0.md) [`004a1e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1e34.md) · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbf30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf30.md)

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
      "definition_site": "00499c20",
      "incomplete_value": true,
      "site": "00499c2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00499c20",
      "incomplete_value": true,
      "site": "00499c2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00499c20",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "00499c20",
      "PARAM",
      [
        "storage",
        "00be9e18",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00499c20",
      "READ",
      [
        "storage",
        "00c1b048",
        null,
        "pointer"
      ]
    ],
    [
      "00499c20",
      "PARAM",
      [
        "storage",
        "00be9e68",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00499c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499b28.md#insn-00499c14) · [`00499c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499b28.md#insn-00499c20)
- 新版 `00499c14`（命令位置の公開資料なし） · `00499c20`（命令位置の公開資料なし）

~~~diff
- 00499c14 ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 00499c14 ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 00499c14 bytes 013c00b0
+ 00499c14 bytes 013c00d0
- 00499c20 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ff8:8"]]
- 00499c20 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00499c20 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:48:8"]]
+ 00499c20 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00499c20 bytes 21fc47f9
+ 00499c20 bytes 212440f9
~~~


<a id="compare-92b1f806060cc1677861140fd2e6a9fd"></a>

### [`00499c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499c7c.md) → [`00499c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499c7c.md) _ZN5Botan8CBC_Mode9start_msgEPKhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`005204e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/005204e8.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`005204e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/005204e8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00499d6c",
      "incomplete_value": true,
      "site": "00499d78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00499d6c",
      "incomplete_value": true,
      "site": "00499d78",
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
      "00499d6c",
      "READ",
      [
        "storage",
        "00c1b000",
        null,
        "pointer"
      ]
    ],
    [
      "00499d6c",
      "PARAM",
      [
        "storage",
        "00be94a0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00499d6c",
      "READ",
      [
        "storage",
        "00c1b050",
        null,
        "pointer"
      ]
    ],
    [
      "00499d6c",
      "PARAM",
      [
        "storage",
        "00be94f0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00499d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499c7c.md#insn-00499d6c)
- 新版 `00499d6c`（命令位置の公開資料なし）

~~~diff
- 00499d6c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00499d6c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00499d6c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:50:8"]]
+ 00499d6c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00499d6c bytes 210040f9
+ 00499d6c bytes 212840f9
~~~


<a id="compare-5395a68e947dd9e9df73e58642fd7fb8"></a>

### [`00499dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499dd0.md) → [`00499dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499dd0.md) _ZNK5Botan14CBC_Encryption13output_lengthEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00499e10",
      "incomplete_value": false,
      "site": "00499e30",
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
            "const:8e2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00499e10",
      "incomplete_value": false,
      "site": "00499e30",
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
            "const:96f:8"
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
      "definition_site": "00499e18",
      "incomplete_value": false,
      "site": "00499e30",
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
            "const:50f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00499e18",
      "incomplete_value": false,
      "site": "00499e30",
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
            "const:511:8"
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
      "definition_site": "00499e20",
      "incomplete_value": false,
      "site": "00499e30",
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
            "const:6f6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00499e20",
      "incomplete_value": false,
      "site": "00499e30",
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
            "const:65c:8"
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
      "00499e10",
      "PARAM",
      [
        "storage",
        "0029296f",
        null,
        "string"
      ]
    ],
    [
      "00499e18",
      "PARAM",
      [
        "storage",
        "0029b511",
        null,
        "string"
      ]
    ],
    [
      "00499e20",
      "PARAM",
      [
        "storage",
        "002a765c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00499e10",
      "PARAM",
      [
        "storage",
        "002928e2",
        null,
        "string"
      ]
    ],
    [
      "00499e18",
      "PARAM",
      [
        "storage",
        "0029b50f",
        null,
        "string"
      ]
    ],
    [
      "00499e20",
      "PARAM",
      [
        "storage",
        "002a76f6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00499e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499dd0.md#insn-00499e10) · [`00499e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499dd0.md#insn-00499e18) · [`00499e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499dd0.md#insn-00499e20)
- 新版 `00499e10`（命令位置の公開資料なし） · `00499e18`（命令位置の公開資料なし） · `00499e20`（命令位置の公開資料なし）

~~~diff
- 00499e10 ["COPY", "tmp:0:8", ["const:96f:8"]]
- 00499e10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00499e10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00499e10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00499e10 ["COPY", "tmp:0:8", ["const:8e2:8"]]
+ 00499e10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00499e10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00499e10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00499e10 bytes 00bc2591
+ 00499e10 bytes 00882391
- 00499e18 ["COPY", "tmp:0:8", ["const:511:8"]]
- 00499e18 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00499e18 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00499e18 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00499e18 ["COPY", "tmp:0:8", ["const:50f:8"]]
+ 00499e18 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00499e18 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00499e18 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00499e18 bytes 21441491
+ 00499e18 bytes 213c1491
- 00499e20 ["COPY", "tmp:0:8", ["const:65c:8"]]
- 00499e20 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00499e20 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00499e20 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00499e20 ["COPY", "tmp:0:8", ["const:6f6:8"]]
+ 00499e20 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00499e20 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00499e20 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00499e20 bytes 42701991
+ 00499e20 bytes 42d81b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-004d3533c0eb721855041f65a0584e14"></a>

### [`00499e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499e34.md) → [`00499e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499e34.md) _ZN5Botan14CBC_Encryption7processEPhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00520980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520980.md) [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00520980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520980.md) [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.06% / 新版 98.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049a07c",
      "incomplete_value": false,
      "site": "0049a09c",
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
            "const:d95:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049a07c",
      "incomplete_value": false,
      "site": "0049a09c",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049a08c",
      "incomplete_value": false,
      "site": "0049a09c",
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
            "const:73d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049a08c",
      "incomplete_value": false,
      "site": "0049a09c",
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
            "const:7ca:8"
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
      "definition_site": "0049a094",
      "incomplete_value": false,
      "site": "0049a09c",
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
            "const:3d2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049a094",
      "incomplete_value": false,
      "site": "0049a09c",
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
            "const:8e1:8"
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
      "0049a07c",
      "PARAM",
      [
        "storage",
        "00298e22",
        null,
        "string"
      ]
    ],
    [
      "0049a08c",
      "PARAM",
      [
        "storage",
        "002947ca",
        null,
        "string"
      ]
    ],
    [
      "0049a094",
      "PARAM",
      [
        "storage",
        "002918e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049a07c",
      "PARAM",
      [
        "storage",
        "00298d95",
        null,
        "string"
      ]
    ],
    [
      "0049a08c",
      "PARAM",
      [
        "storage",
        "0029473d",
        null,
        "string"
      ]
    ],
    [
      "0049a094",
      "PARAM",
      [
        "storage",
        "0029c3d2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049a07c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499e34.md#insn-0049a07c) · [`0049a08c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499e34.md#insn-0049a08c) · [`0049a090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499e34.md#insn-0049a090)
- 新版 `0049a07c`（命令位置の公開資料なし） · `0049a08c`（命令位置の公開資料なし） · `0049a090`（命令位置の公開資料なし）

~~~diff
- 0049a07c ["COPY", "tmp:0:8", ["const:e22:8"]]
- 0049a07c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049a07c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049a07c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049a07c ["COPY", "tmp:0:8", ["const:d95:8"]]
+ 0049a07c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049a07c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049a07c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049a07c bytes 00883891
+ 0049a07c bytes 00543691
- 0049a08c ["COPY", "tmp:0:8", ["const:7ca:8"]]
- 0049a08c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0049a08c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0049a08c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0049a08c ["COPY", "tmp:0:8", ["const:73d:8"]]
+ 0049a08c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0049a08c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0049a08c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0049a08c bytes 42281f91
+ 0049a08c bytes 42f41c91
- 0049a090 ["COPY", "register:4018:8", ["const:291000:8"]]
+ 0049a090 ["COPY", "register:4018:8", ["const:29c000:8"]]
- 0049a090 bytes a3effff0
+ 0049a090 bytes 03f0ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e4b68368076efbe9da0cdf60b13d1b5"></a>

### [`0049a0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049a0a0.md) → [`0049a0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049a0a0.md) _ZN5Botan14CBC_Encryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.34% / 新版 90.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049a1c4",
      "incomplete_value": false,
      "site": "0049a1e4",
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
            "const:49b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049a1c4",
      "incomplete_value": false,
      "site": "0049a1e4",
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
            "const:410:8"
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
      "definition_site": "0049a1cc",
      "incomplete_value": false,
      "site": "0049a1e4",
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
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049a1cc",
      "incomplete_value": false,
      "site": "0049a1e4",
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
            "const:3e5:8"
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
      "definition_site": "0049a1d4",
      "incomplete_value": false,
      "site": "0049a1e4",
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
            "const:56a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049a1d4",
      "incomplete_value": false,
      "site": "0049a1e4",
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
            "const:4d0:8"
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
      "0049a1c4",
      "PARAM",
      [
        "storage",
        "0029d410",
        null,
        "string"
      ]
    ],
    [
      "0049a1cc",
      "PARAM",
      [
        "storage",
        "002a43e5",
        null,
        "string"
      ]
    ],
    [
      "0049a1d4",
      "PARAM",
      [
        "storage",
        "002a94d0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049a1c4",
      "PARAM",
      [
        "storage",
        "0029d49b",
        null,
        "string"
      ]
    ],
    [
      "0049a1cc",
      "PARAM",
      [
        "storage",
        "002a4470",
        null,
        "string"
      ]
    ],
    [
      "0049a1d4",
      "PARAM",
      [
        "storage",
        "002a956a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049a1c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049a0a0.md#insn-0049a1c4) · [`0049a1cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049a0a0.md#insn-0049a1cc) · [`0049a1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049a0a0.md#insn-0049a1d4)
- 新版 `0049a1c4`（命令位置の公開資料なし） · `0049a1cc`（命令位置の公開資料なし） · `0049a1d4`（命令位置の公開資料なし）

~~~diff
- 0049a1c4 ["COPY", "tmp:0:8", ["const:410:8"]]
- 0049a1c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049a1c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049a1c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049a1c4 ["COPY", "tmp:0:8", ["const:49b:8"]]
+ 0049a1c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049a1c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049a1c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049a1c4 bytes 00401091
+ 0049a1c4 bytes 006c1291
- 0049a1cc ["COPY", "tmp:0:8", ["const:3e5:8"]]
- 0049a1cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049a1cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049a1cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049a1cc ["COPY", "tmp:0:8", ["const:470:8"]]
+ 0049a1cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049a1cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049a1cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049a1cc bytes 21940f91
+ 0049a1cc bytes 21c01191
- 0049a1d4 ["COPY", "tmp:0:8", ["const:4d0:8"]]
- 0049a1d4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0049a1d4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0049a1d4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0049a1d4 ["COPY", "tmp:0:8", ["const:56a:8"]]
+ 0049a1d4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0049a1d4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0049a1d4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0049a1d4 bytes 42401391
+ 0049a1d4 bytes 42a81591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b14550a9210df102113f6f8725d0891d"></a>

### [`0049a380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049a380.md) → [`0049a380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049a380.md) _ZN5Botan14CTS_Encryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051d3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d3cc.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.19% / 新版 95.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0049a638",
      "incomplete_value": true,
      "site": "0049a638",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049a638",
      "incomplete_value": true,
      "site": "0049a638",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049a6f8",
      "incomplete_value": false,
      "site": "0049a718",
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
            "const:49b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049a6f8",
      "incomplete_value": false,
      "site": "0049a718",
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
            "const:410:8"
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
      "definition_site": "0049a700",
      "incomplete_value": false,
      "site": "0049a718",
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
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049a700",
      "incomplete_value": false,
      "site": "0049a718",
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
            "const:3e5:8"
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
      "0049a628",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0049a6f8",
      "PARAM",
      [
        "storage",
        "0029d410",
        null,
        "string"
      ]
    ],
    [
      "0049a700",
      "PARAM",
      [
        "storage",
        "002a43e5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049a628",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0049a6f8",
      "PARAM",
      [
        "storage",
        "0029d49b",
        null,
        "string"
      ]
    ],
    [
      "0049a700",
      "PARAM",
      [
        "storage",
        "002a4470",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049a628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049a380.md#insn-0049a628) · [`0049a6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049a380.md#insn-0049a6f8) · [`0049a700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049a380.md#insn-0049a700)
- 新版 `0049a628`（命令位置の公開資料なし） · `0049a6f8`（命令位置の公開資料なし） · `0049a700`（命令位置の公開資料なし）

~~~diff
- 0049a628 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 0049a628 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049a628 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 0049a628 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0049a628 bytes 299543f9
+ 0049a628 bytes 29bd43f9
- 0049a6f8 ["COPY", "tmp:0:8", ["const:410:8"]]
- 0049a6f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049a6f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049a6f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049a6f8 ["COPY", "tmp:0:8", ["const:49b:8"]]
+ 0049a6f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049a6f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049a6f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049a6f8 bytes 00401091
+ 0049a6f8 bytes 006c1291
- 0049a700 ["COPY", "tmp:0:8", ["const:3e5:8"]]
- 0049a700 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049a700 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049a700 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049a700 ["COPY", "tmp:0:8", ["const:470:8"]]
+ 0049a700 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049a700 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049a700 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049a700 bytes 21940f91
+ 0049a700 bytes 21c01191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82a3b8b9a2f79360ee1304dc4e0629bb"></a>

### [`0049a8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049a8a4.md) → [`0049a8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049a8a4.md) _ZN5Botan14CBC_Decryption7processEPhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.32% / 新版 97.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049aad4",
      "incomplete_value": false,
      "site": "0049aaf4",
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
            "const:d95:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049aad4",
      "incomplete_value": false,
      "site": "0049aaf4",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049aadc",
      "incomplete_value": false,
      "site": "0049aaf4",
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
            "const:52d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049aadc",
      "incomplete_value": false,
      "site": "0049aaf4",
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
            "const:4a2:8"
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
      "definition_site": "0049aae4",
      "incomplete_value": false,
      "site": "0049aaf4",
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
            "const:73d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049aae4",
      "incomplete_value": false,
      "site": "0049aaf4",
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
            "const:7ca:8"
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
      "0049aad4",
      "PARAM",
      [
        "storage",
        "00298e22",
        null,
        "string"
      ]
    ],
    [
      "0049aadc",
      "PARAM",
      [
        "storage",
        "002a04a2",
        null,
        "string"
      ]
    ],
    [
      "0049aae4",
      "PARAM",
      [
        "storage",
        "002947ca",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049aad4",
      "PARAM",
      [
        "storage",
        "00298d95",
        null,
        "string"
      ]
    ],
    [
      "0049aadc",
      "PARAM",
      [
        "storage",
        "002a052d",
        null,
        "string"
      ]
    ],
    [
      "0049aae4",
      "PARAM",
      [
        "storage",
        "0029473d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049aad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049a8a4.md#insn-0049aad4) · [`0049aadc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049a8a4.md#insn-0049aadc) · [`0049aae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049a8a4.md#insn-0049aae4)
- 新版 `0049aad4`（命令位置の公開資料なし） · `0049aadc`（命令位置の公開資料なし） · `0049aae4`（命令位置の公開資料なし）

~~~diff
- 0049aad4 ["COPY", "tmp:0:8", ["const:e22:8"]]
- 0049aad4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049aad4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049aad4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049aad4 ["COPY", "tmp:0:8", ["const:d95:8"]]
+ 0049aad4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049aad4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049aad4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049aad4 bytes 00883891
+ 0049aad4 bytes 00543691
- 0049aadc ["COPY", "tmp:0:8", ["const:4a2:8"]]
- 0049aadc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049aadc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049aadc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049aadc ["COPY", "tmp:0:8", ["const:52d:8"]]
+ 0049aadc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049aadc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049aadc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049aadc bytes 21881291
+ 0049aadc bytes 21b41491
- 0049aae4 ["COPY", "tmp:0:8", ["const:7ca:8"]]
- 0049aae4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0049aae4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0049aae4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0049aae4 ["COPY", "tmp:0:8", ["const:73d:8"]]
+ 0049aae4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0049aae4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0049aae4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0049aae4 bytes 42281f91
+ 0049aae4 bytes 42f41c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06b5a7cc94a9e0528154e97425d07ab6"></a>

### [`0049aaf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049aaf8.md) → [`0049aaf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049aaf8.md) _ZN5Botan14CBC_Decryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.30% / 新版 94.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049acc8",
      "incomplete_value": false,
      "site": "0049acd0",
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
            "const:9ef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049acc8",
      "incomplete_value": false,
      "site": "0049acd0",
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
            "const:a83:8"
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
      "definition_site": "0049ad18",
      "incomplete_value": true,
      "site": "0049ad24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049ad18",
      "incomplete_value": true,
      "site": "0049ad24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049ad40",
      "incomplete_value": false,
      "site": "0049ad60",
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
            "const:6c9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ad40",
      "incomplete_value": false,
      "site": "0049ad60",
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
            "const:63e:8"
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
      "0049acc8",
      "PARAM",
      [
        "storage",
        "002afa83",
        null,
        "string"
      ]
    ],
    [
      "0049ad18",
      "READ",
      [
        "storage",
        "00c1af10",
        null,
        "pointer"
      ]
    ],
    [
      "0049ad18",
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
      "0049acc8",
      "PARAM",
      [
        "storage",
        "002af9ef",
        null,
        "string"
      ]
    ],
    [
      "0049ad18",
      "READ",
      [
        "storage",
        "00c1af60",
        null,
        "pointer"
      ]
    ],
    [
      "0049ad18",
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

- 旧版 [`0049acc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049aaf8.md#insn-0049acc8) · [`0049ad18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049aaf8.md#insn-0049ad18) · [`0049ad40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049aaf8.md#insn-0049ad40)
- 新版 `0049acc8`（命令位置の公開資料なし） · `0049ad18`（命令位置の公開資料なし） · `0049ad40`（命令位置の公開資料なし）

~~~diff
- 0049acc8 ["COPY", "tmp:0:8", ["const:a83:8"]]
- 0049acc8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049acc8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049acc8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049acc8 ["COPY", "tmp:0:8", ["const:9ef:8"]]
+ 0049acc8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049acc8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049acc8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049acc8 bytes 210c2a91
+ 0049acc8 bytes 21bc2791
- 0049ad18 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
- 0049ad18 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049ad18 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f60:8"]]
+ 0049ad18 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0049ad18 bytes 218847f9
+ 0049ad18 bytes 21b047f9
- 0049ad40 ["COPY", "tmp:0:8", ["const:63e:8"]]
- 0049ad40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049ad40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049ad40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049ad40 ["COPY", "tmp:0:8", ["const:6c9:8"]]
+ 0049ad40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049ad40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049ad40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049ad40 bytes 00f81891
+ 0049ad40 bytes 00241b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95071695862277ea229522152c2ebb19"></a>

### [`0049af04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049af04.md) → [`0049af04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049af04.md) _ZN5Botan14CTS_Decryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051d3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d3cc.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.99% / 新版 94.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0049b288",
      "incomplete_value": true,
      "site": "0049b288",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049b288",
      "incomplete_value": true,
      "site": "0049b288",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049b354",
      "incomplete_value": false,
      "site": "0049b374",
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
            "const:49b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049b354",
      "incomplete_value": false,
      "site": "0049b374",
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
            "const:410:8"
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
      "definition_site": "0049b35c",
      "incomplete_value": false,
      "site": "0049b374",
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
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049b35c",
      "incomplete_value": false,
      "site": "0049b374",
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
            "const:3e5:8"
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
      "0049b278",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0049b354",
      "PARAM",
      [
        "storage",
        "0029d410",
        null,
        "string"
      ]
    ],
    [
      "0049b35c",
      "PARAM",
      [
        "storage",
        "002a43e5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049b278",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0049b354",
      "PARAM",
      [
        "storage",
        "0029d49b",
        null,
        "string"
      ]
    ],
    [
      "0049b35c",
      "PARAM",
      [
        "storage",
        "002a4470",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049b278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049af04.md#insn-0049b278) · [`0049b354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049af04.md#insn-0049b354) · [`0049b35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049af04.md#insn-0049b35c)
- 新版 `0049b278`（命令位置の公開資料なし） · `0049b354`（命令位置の公開資料なし） · `0049b35c`（命令位置の公開資料なし）

~~~diff
- 0049b278 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 0049b278 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049b278 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 0049b278 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0049b278 bytes 299543f9
+ 0049b278 bytes 29bd43f9
- 0049b354 ["COPY", "tmp:0:8", ["const:410:8"]]
- 0049b354 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049b354 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049b354 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049b354 ["COPY", "tmp:0:8", ["const:49b:8"]]
+ 0049b354 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049b354 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049b354 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049b354 bytes 00401091
+ 0049b354 bytes 006c1291
- 0049b35c ["COPY", "tmp:0:8", ["const:3e5:8"]]
- 0049b35c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049b35c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049b35c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049b35c ["COPY", "tmp:0:8", ["const:470:8"]]
+ 0049b35c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049b35c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049b35c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049b35c bytes 21940f91
+ 0049b35c bytes 21c01191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-339efab9a054ec13ba8f96a3d00736e2"></a>

### [`0049b54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049b/0049b54c.md) → [`0049b54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049b54c.md) _ZN5Botan5CPUID9to_stringEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbf00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf00.md) · 呼出先 8件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdbf50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf50.md) · 呼出先 8件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 99.27% / 新版 99.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0049b590",
      "incomplete_value": true,
      "site": "0049b590",
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
      "definition_site": "0049b590",
      "incomplete_value": true,
      "site": "0049b590",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0049b57c",
      "READ",
      [
        "storage",
        "00c1aed8",
        null,
        "pointer"
      ]
    ],
    [
      "0049b584",
      "READ",
      [
        "storage",
        "00c25338",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "0049b69c",
      "READ",
      [
        "storage",
        "00c25338",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0049b57c",
      "READ",
      [
        "storage",
        "00c1af28",
        null,
        "pointer"
      ]
    ],
    [
      "0049b584",
      "READ",
      [
        "storage",
        "00c25378",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "0049b69c",
      "READ",
      [
        "storage",
        "00c25378",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049b57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049b/0049b54c.md#insn-0049b57c)
- 新版 `0049b57c`（命令位置の公開資料なし）

~~~diff
- 0049b57c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:ed8:8"]]
- 0049b57c ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049b57c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:f28:8"]]
+ 0049b57c ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 0049b57c bytes 186f47f9
+ 0049b57c bytes 189747f9
~~~


<a id="compare-db909945237458dc51771053f2252101"></a>

### [`0049bcc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049b/0049bcc4.md) → [`0049bcc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bcc4.md) _ZN5Botan5CPUID5printERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdbf00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf00.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbf50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049bce0",
      "incomplete_value": false,
      "site": "0049bcf0",
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
            "const:9b7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049bce0",
      "incomplete_value": false,
      "site": "0049bcf0",
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
            "const:a44:8"
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
      "definition_site": "0049bd28",
      "incomplete_value": false,
      "site": "0049bd30",
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
      "definition_site": "0049bd28",
      "incomplete_value": false,
      "site": "0049bd30",
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
      "0049bce0",
      "PARAM",
      [
        "storage",
        "00296a44",
        null,
        "string"
      ]
    ],
    [
      "0049bd28",
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
      "0049bce0",
      "PARAM",
      [
        "storage",
        "002969b7",
        null,
        "string"
      ]
    ],
    [
      "0049bd28",
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

- 旧版 [`0049bce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049b/0049bcc4.md#insn-0049bce0) · [`0049bd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049b/0049bcc4.md#insn-0049bd28)
- 新版 `0049bce0`（命令位置の公開資料なし） · `0049bd28`（命令位置の公開資料なし）

~~~diff
- 0049bce0 ["COPY", "tmp:0:8", ["const:a44:8"]]
- 0049bce0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049bce0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049bce0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049bce0 ["COPY", "tmp:0:8", ["const:9b7:8"]]
+ 0049bce0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049bce0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049bce0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049bce0 bytes 21102991
+ 0049bce0 bytes 21dc2691
- 0049bd28 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 0049bd28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049bd28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049bd28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049bd28 ["COPY", "tmp:0:8", ["const:333:8"]]
+ 0049bd28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049bd28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049bd28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049bd28 bytes 21a00a91
+ 0049bd28 bytes 21cc0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86e542416541e14f10763b66590bb3d0"></a>

### [`0049bd98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049b/0049bd98.md) → [`0049bd98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bd98.md) _ZN5Botan5CPUID10initializeEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0049bda4",
      "incomplete_value": true,
      "site": "0049bda4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049bda4",
      "incomplete_value": true,
      "site": "0049bda4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed8:8"
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
      "0049bda0",
      "READ",
      [
        "storage",
        "00c1aed8",
        null,
        "pointer"
      ]
    ],
    [
      "0049bda4",
      "WRITE",
      [
        "storage",
        "00c25338",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0049bda0",
      "READ",
      [
        "storage",
        "00c1af28",
        null,
        "pointer"
      ]
    ],
    [
      "0049bda4",
      "WRITE",
      [
        "storage",
        "00c25378",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049bda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049b/0049bd98.md#insn-0049bda0)
- 新版 `0049bda0`（命令位置の公開資料なし）

~~~diff
- 0049bda0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ed8:8"]]
- 0049bda0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049bda0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f28:8"]]
+ 0049bda0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0049bda0 bytes 086d47f9
+ 0049bda0 bytes 089547f9
~~~


<a id="compare-3a019aa7410187446f149b6cb5772500"></a>

### [`0049c054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c054.md) → [`0049c054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c054.md) _ZN5Botan8ECB_ModeC2EPNS_11BlockCipherEPNS_28BlockCipherModePaddingMethodE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf10.md) · 呼出先 8件 [`00483974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdbf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf60.md) · 呼出先 8件 [`00483974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.10% / 新版 95.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049c090",
      "incomplete_value": true,
      "site": "0049c090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0049c090",
      "incomplete_value": true,
      "site": "0049c090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049c13c",
      "incomplete_value": false,
      "site": "0049c144",
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
            "const:be5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049c13c",
      "incomplete_value": false,
      "site": "0049c144",
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
            "const:c72:8"
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
      "definition_site": "0049c1d8",
      "incomplete_value": true,
      "site": "0049c1e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049c1d8",
      "incomplete_value": true,
      "site": "0049c1e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0049c07c",
      "READ",
      [
        "storage",
        "00c1b008",
        null,
        "pointer"
      ]
    ],
    [
      "0049c090",
      "DATA",
      [
        "storage",
        "00be94c8",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0049c13c",
      "PARAM",
      [
        "storage",
        "00299c72",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049c07c",
      "READ",
      [
        "storage",
        "00c1b058",
        null,
        "pointer"
      ]
    ],
    [
      "0049c090",
      "DATA",
      [
        "storage",
        "00be9518",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0049c13c",
      "PARAM",
      [
        "storage",
        "00299be5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049c07c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c054.md#insn-0049c07c) · [`0049c13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c054.md#insn-0049c13c) · [`0049c1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c054.md#insn-0049c1d8)
- 新版 `0049c07c`（命令位置の公開資料なし） · `0049c13c`（命令位置の公開資料なし） · `0049c1d8`（命令位置の公開資料なし）

~~~diff
- 0049c07c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:8:8"]]
- 0049c07c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049c07c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:58:8"]]
+ 0049c07c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0049c07c bytes 290540f9
+ 0049c07c bytes 292d40f9
- 0049c13c ["COPY", "tmp:0:8", ["const:c72:8"]]
- 0049c13c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049c13c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049c13c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049c13c ["COPY", "tmp:0:8", ["const:be5:8"]]
+ 0049c13c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049c13c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049c13c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049c13c bytes 21c83191
+ 0049c13c bytes 21942f91
- 0049c1d8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 0049c1d8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049c1d8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 0049c1d8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0049c1d8 bytes 217847f9
+ 0049c1d8 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1121c5e1c8f5e4cb718ff51862a0563c"></a>

### [`0049c360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c360.md) → [`0049c360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c360.md) _ZNK5Botan8ECB_Mode4nameEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf20.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)
- 新版 呼出元 1件 [`00bdbf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf70.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049c3a0",
      "incomplete_value": false,
      "site": "0049c3a8",
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
            "const:9c5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049c3a0",
      "incomplete_value": false,
      "site": "0049c3a8",
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
            "const:a52:8"
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
      "0049c3a0",
      "PARAM",
      [
        "storage",
        "00296a52",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049c3a0",
      "PARAM",
      [
        "storage",
        "002969c5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049c3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c360.md#insn-0049c3a0)
- 新版 `0049c3a0`（命令位置の公開資料なし）

~~~diff
- 0049c3a0 ["COPY", "tmp:0:8", ["const:a52:8"]]
- 0049c3a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049c3a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049c3a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049c3a0 ["COPY", "tmp:0:8", ["const:9c5:8"]]
+ 0049c3a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049c3a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049c3a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049c3a0 bytes 21482991
+ 0049c3a0 bytes 21142791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bdc3c8dde110996421fe876c7efc86b"></a>

### [`0049c574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c574.md) → [`0049c574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c574.md) _ZN5Botan8ECB_Mode9start_msgEPKhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdbef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbef0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbf40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

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
      "definition_site": "0049c61c",
      "incomplete_value": true,
      "site": "0049c628",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049c61c",
      "incomplete_value": true,
      "site": "0049c628",
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
      "0049c61c",
      "READ",
      [
        "storage",
        "00c1b000",
        null,
        "pointer"
      ]
    ],
    [
      "0049c61c",
      "PARAM",
      [
        "storage",
        "00be94a0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049c61c",
      "READ",
      [
        "storage",
        "00c1b050",
        null,
        "pointer"
      ]
    ],
    [
      "0049c61c",
      "PARAM",
      [
        "storage",
        "00be94f0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049c61c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c574.md#insn-0049c61c)
- 新版 `0049c61c`（命令位置の公開資料なし）

~~~diff
- 0049c61c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 0049c61c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049c61c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:50:8"]]
+ 0049c61c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0049c61c bytes 210040f9
+ 0049c61c bytes 212840f9
~~~


<a id="compare-971af1e5ab596662ed0ece38dce30e4a"></a>

### [`0049c684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c684.md) → [`0049c684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c684.md) _ZNK5Botan14ECB_Encryption13output_lengthEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.21% / 新版 86.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049c6d4",
      "incomplete_value": false,
      "site": "0049c6f4",
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
            "const:8e2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049c6d4",
      "incomplete_value": false,
      "site": "0049c6f4",
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
            "const:96f:8"
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
      "definition_site": "0049c6dc",
      "incomplete_value": false,
      "site": "0049c6f4",
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
            "const:50f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049c6dc",
      "incomplete_value": false,
      "site": "0049c6f4",
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
            "const:511:8"
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
      "definition_site": "0049c6e4",
      "incomplete_value": false,
      "site": "0049c6f4",
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
            "const:6f6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049c6e4",
      "incomplete_value": false,
      "site": "0049c6f4",
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
            "const:65c:8"
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
      "0049c6d4",
      "PARAM",
      [
        "storage",
        "0029296f",
        null,
        "string"
      ]
    ],
    [
      "0049c6dc",
      "PARAM",
      [
        "storage",
        "0029b511",
        null,
        "string"
      ]
    ],
    [
      "0049c6e4",
      "PARAM",
      [
        "storage",
        "002a765c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049c6d4",
      "PARAM",
      [
        "storage",
        "002928e2",
        null,
        "string"
      ]
    ],
    [
      "0049c6dc",
      "PARAM",
      [
        "storage",
        "0029b50f",
        null,
        "string"
      ]
    ],
    [
      "0049c6e4",
      "PARAM",
      [
        "storage",
        "002a76f6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049c6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c684.md#insn-0049c6d4) · [`0049c6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c684.md#insn-0049c6dc) · [`0049c6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c684.md#insn-0049c6e4)
- 新版 `0049c6d4`（命令位置の公開資料なし） · `0049c6dc`（命令位置の公開資料なし） · `0049c6e4`（命令位置の公開資料なし）

~~~diff
- 0049c6d4 ["COPY", "tmp:0:8", ["const:96f:8"]]
- 0049c6d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049c6d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049c6d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049c6d4 ["COPY", "tmp:0:8", ["const:8e2:8"]]
+ 0049c6d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049c6d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049c6d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049c6d4 bytes 00bc2591
+ 0049c6d4 bytes 00882391
- 0049c6dc ["COPY", "tmp:0:8", ["const:511:8"]]
- 0049c6dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049c6dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049c6dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049c6dc ["COPY", "tmp:0:8", ["const:50f:8"]]
+ 0049c6dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049c6dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049c6dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049c6dc bytes 21441491
+ 0049c6dc bytes 213c1491
- 0049c6e4 ["COPY", "tmp:0:8", ["const:65c:8"]]
- 0049c6e4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0049c6e4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0049c6e4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0049c6e4 ["COPY", "tmp:0:8", ["const:6f6:8"]]
+ 0049c6e4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0049c6e4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0049c6e4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0049c6e4 bytes 42701991
+ 0049c6e4 bytes 42d81b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae67afbd1b116cc10e6e3a9a0378e8ed"></a>

### [`0049c6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c6f8.md) → [`0049c6f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c6f8.md) _ZN5Botan14ECB_Encryption7processEPhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049c760",
      "incomplete_value": false,
      "site": "0049c780",
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
            "const:d95:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049c760",
      "incomplete_value": false,
      "site": "0049c780",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049c768",
      "incomplete_value": false,
      "site": "0049c780",
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
            "const:82f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049c768",
      "incomplete_value": false,
      "site": "0049c780",
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
            "const:8bc:8"
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
      "definition_site": "0049c770",
      "incomplete_value": false,
      "site": "0049c780",
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
            "const:73d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049c770",
      "incomplete_value": false,
      "site": "0049c780",
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
            "const:7ca:8"
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
      "0049c760",
      "PARAM",
      [
        "storage",
        "00298e22",
        null,
        "string"
      ]
    ],
    [
      "0049c768",
      "PARAM",
      [
        "storage",
        "002938bc",
        null,
        "string"
      ]
    ],
    [
      "0049c770",
      "PARAM",
      [
        "storage",
        "002947ca",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049c760",
      "PARAM",
      [
        "storage",
        "00298d95",
        null,
        "string"
      ]
    ],
    [
      "0049c768",
      "PARAM",
      [
        "storage",
        "0029382f",
        null,
        "string"
      ]
    ],
    [
      "0049c770",
      "PARAM",
      [
        "storage",
        "0029473d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049c760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c6f8.md#insn-0049c760) · [`0049c768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c6f8.md#insn-0049c768) · [`0049c770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c6f8.md#insn-0049c770)
- 新版 `0049c760`（命令位置の公開資料なし） · `0049c768`（命令位置の公開資料なし） · `0049c770`（命令位置の公開資料なし）

~~~diff
- 0049c760 ["COPY", "tmp:0:8", ["const:e22:8"]]
- 0049c760 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049c760 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049c760 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049c760 ["COPY", "tmp:0:8", ["const:d95:8"]]
+ 0049c760 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049c760 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049c760 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049c760 bytes 00883891
+ 0049c760 bytes 00543691
- 0049c768 ["COPY", "tmp:0:8", ["const:8bc:8"]]
- 0049c768 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049c768 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049c768 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049c768 ["COPY", "tmp:0:8", ["const:82f:8"]]
+ 0049c768 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049c768 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049c768 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049c768 bytes 21f02291
+ 0049c768 bytes 21bc2091
- 0049c770 ["COPY", "tmp:0:8", ["const:7ca:8"]]
- 0049c770 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0049c770 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0049c770 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0049c770 ["COPY", "tmp:0:8", ["const:73d:8"]]
+ 0049c770 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0049c770 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0049c770 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0049c770 bytes 42281f91
+ 0049c770 bytes 42f41c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c483ff59b81ddde5563f530e7bc23cb1"></a>

### [`0049c784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c784.md) → [`0049c784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c784.md) _ZN5Botan14ECB_Encryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.37% / 新版 92.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049c8b0",
      "incomplete_value": false,
      "site": "0049c8d0",
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
            "const:49b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049c8b0",
      "incomplete_value": false,
      "site": "0049c8d0",
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
            "const:410:8"
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
      "definition_site": "0049c8b8",
      "incomplete_value": false,
      "site": "0049c8d0",
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
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049c8b8",
      "incomplete_value": false,
      "site": "0049c8d0",
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
            "const:3e5:8"
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
      "definition_site": "0049c8c0",
      "incomplete_value": false,
      "site": "0049c8d0",
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
            "const:56a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049c8c0",
      "incomplete_value": false,
      "site": "0049c8d0",
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
            "const:4d0:8"
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
      "0049c8b0",
      "PARAM",
      [
        "storage",
        "0029d410",
        null,
        "string"
      ]
    ],
    [
      "0049c8b8",
      "PARAM",
      [
        "storage",
        "002a43e5",
        null,
        "string"
      ]
    ],
    [
      "0049c8c0",
      "PARAM",
      [
        "storage",
        "002a94d0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049c8b0",
      "PARAM",
      [
        "storage",
        "0029d49b",
        null,
        "string"
      ]
    ],
    [
      "0049c8b8",
      "PARAM",
      [
        "storage",
        "002a4470",
        null,
        "string"
      ]
    ],
    [
      "0049c8c0",
      "PARAM",
      [
        "storage",
        "002a956a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049c8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c784.md#insn-0049c8b0) · [`0049c8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c784.md#insn-0049c8b8) · [`0049c8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c784.md#insn-0049c8c0)
- 新版 `0049c8b0`（命令位置の公開資料なし） · `0049c8b8`（命令位置の公開資料なし） · `0049c8c0`（命令位置の公開資料なし）

~~~diff
- 0049c8b0 ["COPY", "tmp:0:8", ["const:410:8"]]
- 0049c8b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049c8b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049c8b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049c8b0 ["COPY", "tmp:0:8", ["const:49b:8"]]
+ 0049c8b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049c8b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049c8b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049c8b0 bytes 00401091
+ 0049c8b0 bytes 006c1291
- 0049c8b8 ["COPY", "tmp:0:8", ["const:3e5:8"]]
- 0049c8b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049c8b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049c8b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049c8b8 ["COPY", "tmp:0:8", ["const:470:8"]]
+ 0049c8b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049c8b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049c8b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049c8b8 bytes 21940f91
+ 0049c8b8 bytes 21c01191
- 0049c8c0 ["COPY", "tmp:0:8", ["const:4d0:8"]]
- 0049c8c0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0049c8c0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0049c8c0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0049c8c0 ["COPY", "tmp:0:8", ["const:56a:8"]]
+ 0049c8c0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0049c8c0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0049c8c0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0049c8c0 bytes 42401391
+ 0049c8c0 bytes 42a81591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcc0344bd61705fb65ab65844a99028b"></a>

### [`0049ca18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049ca18.md) → [`0049ca18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049ca18.md) _ZN5Botan14ECB_Decryption7processEPhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049ca80",
      "incomplete_value": false,
      "site": "0049caa0",
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
            "const:d95:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ca80",
      "incomplete_value": false,
      "site": "0049caa0",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049ca88",
      "incomplete_value": false,
      "site": "0049caa0",
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
            "const:52d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ca88",
      "incomplete_value": false,
      "site": "0049caa0",
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
            "const:4a2:8"
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
      "definition_site": "0049ca90",
      "incomplete_value": false,
      "site": "0049caa0",
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
            "const:73d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ca90",
      "incomplete_value": false,
      "site": "0049caa0",
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
            "const:7ca:8"
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
      "0049ca80",
      "PARAM",
      [
        "storage",
        "00298e22",
        null,
        "string"
      ]
    ],
    [
      "0049ca88",
      "PARAM",
      [
        "storage",
        "002a04a2",
        null,
        "string"
      ]
    ],
    [
      "0049ca90",
      "PARAM",
      [
        "storage",
        "002947ca",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049ca80",
      "PARAM",
      [
        "storage",
        "00298d95",
        null,
        "string"
      ]
    ],
    [
      "0049ca88",
      "PARAM",
      [
        "storage",
        "002a052d",
        null,
        "string"
      ]
    ],
    [
      "0049ca90",
      "PARAM",
      [
        "storage",
        "0029473d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049ca80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049ca18.md#insn-0049ca80) · [`0049ca88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049ca18.md#insn-0049ca88) · [`0049ca90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049ca18.md#insn-0049ca90)
- 新版 `0049ca80`（命令位置の公開資料なし） · `0049ca88`（命令位置の公開資料なし） · `0049ca90`（命令位置の公開資料なし）

~~~diff
- 0049ca80 ["COPY", "tmp:0:8", ["const:e22:8"]]
- 0049ca80 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049ca80 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049ca80 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049ca80 ["COPY", "tmp:0:8", ["const:d95:8"]]
+ 0049ca80 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049ca80 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049ca80 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049ca80 bytes 00883891
+ 0049ca80 bytes 00543691
- 0049ca88 ["COPY", "tmp:0:8", ["const:4a2:8"]]
- 0049ca88 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049ca88 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049ca88 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049ca88 ["COPY", "tmp:0:8", ["const:52d:8"]]
+ 0049ca88 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049ca88 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049ca88 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049ca88 bytes 21881291
+ 0049ca88 bytes 21b41491
- 0049ca90 ["COPY", "tmp:0:8", ["const:7ca:8"]]
- 0049ca90 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0049ca90 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0049ca90 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0049ca90 ["COPY", "tmp:0:8", ["const:73d:8"]]
+ 0049ca90 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0049ca90 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0049ca90 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0049ca90 bytes 42281f91
+ 0049ca90 bytes 42f41c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a20f45023e20cecd45d63f73ab0e2c16"></a>

### [`0049caa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049caa4.md) → [`0049caa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049caa4.md) _ZN5Botan14ECB_Decryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049cc14",
      "incomplete_value": false,
      "site": "0049cc1c",
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
            "const:9ef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049cc14",
      "incomplete_value": false,
      "site": "0049cc1c",
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
            "const:a83:8"
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
      "definition_site": "0049cc64",
      "incomplete_value": true,
      "site": "0049cc70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049cc64",
      "incomplete_value": true,
      "site": "0049cc70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049cc88",
      "incomplete_value": false,
      "site": "0049cca8",
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
            "const:49b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049cc88",
      "incomplete_value": false,
      "site": "0049cca8",
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
            "const:410:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0049cc14",
      "PARAM",
      [
        "storage",
        "002afa83",
        null,
        "string"
      ]
    ],
    [
      "0049cc64",
      "READ",
      [
        "storage",
        "00c1af10",
        null,
        "pointer"
      ]
    ],
    [
      "0049cc64",
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
      "0049cc14",
      "PARAM",
      [
        "storage",
        "002af9ef",
        null,
        "string"
      ]
    ],
    [
      "0049cc64",
      "READ",
      [
        "storage",
        "00c1af60",
        null,
        "pointer"
      ]
    ],
    [
      "0049cc64",
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

- 旧版 [`0049cc14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049caa4.md#insn-0049cc14) · [`0049cc64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049caa4.md#insn-0049cc64) · [`0049cc88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049caa4.md#insn-0049cc88)
- 新版 `0049cc14`（命令位置の公開資料なし） · `0049cc64`（命令位置の公開資料なし） · `0049cc88`（命令位置の公開資料なし）

~~~diff
- 0049cc14 ["COPY", "tmp:0:8", ["const:a83:8"]]
- 0049cc14 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049cc14 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049cc14 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049cc14 ["COPY", "tmp:0:8", ["const:9ef:8"]]
+ 0049cc14 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049cc14 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049cc14 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049cc14 bytes 210c2a91
+ 0049cc14 bytes 21bc2791
- 0049cc64 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
- 0049cc64 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049cc64 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f60:8"]]
+ 0049cc64 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0049cc64 bytes 218847f9
+ 0049cc64 bytes 21b047f9
- 0049cc88 ["COPY", "tmp:0:8", ["const:410:8"]]
- 0049cc88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049cc88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049cc88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049cc88 ["COPY", "tmp:0:8", ["const:49b:8"]]
+ 0049cc88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049cc88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049cc88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049cc88 bytes 00401091
+ 0049cc88 bytes 006c1291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d2da3279fe2cf910914237b2fa51a90"></a>

### [`0049ce2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049ce2c.md) → [`0049ce2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049ce2c.md) _ZN5Botan13EMSA_PKCS1v1511encoding_ofERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmRNS_21RandomNumberGeneratorE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0049cf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049cf60.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0049cf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cf60.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049cecc",
      "incomplete_value": false,
      "site": "0049ced4",
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
            "const:47f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049cecc",
      "incomplete_value": false,
      "site": "0049ced4",
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
            "const:3f4:8"
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
      "definition_site": "0049cf04",
      "incomplete_value": true,
      "site": "0049cf10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049cf04",
      "incomplete_value": true,
      "site": "0049cf10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0049cecc",
      "PARAM",
      [
        "storage",
        "002a43f4",
        null,
        "string"
      ]
    ],
    [
      "0049cf04",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "0049cf04",
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
      "0049cecc",
      "PARAM",
      [
        "storage",
        "002a447f",
        null,
        "string"
      ]
    ],
    [
      "0049cf04",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "0049cf04",
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

- 旧版 [`0049cecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049ce2c.md#insn-0049cecc) · [`0049cf04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049ce2c.md#insn-0049cf04)
- 新版 `0049cecc`（命令位置の公開資料なし） · `0049cf04`（命令位置の公開資料なし）

~~~diff
- 0049cecc ["COPY", "tmp:0:8", ["const:3f4:8"]]
- 0049cecc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049cecc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049cecc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049cecc ["COPY", "tmp:0:8", ["const:47f:8"]]
+ 0049cecc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049cecc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049cecc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049cecc bytes 21d00f91
+ 0049cecc bytes 21fc1191
- 0049cf04 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
- 0049cf04 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049cf04 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
+ 0049cf04 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0049cf04 bytes 21ac47f9
+ 0049cf04 bytes 21d447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7ee27ca36aa652066796efe6d305ee0"></a>

### [`0049cf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049cf60.md) → [`0049cf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cf60.md) FUN_0049cf60

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0049ce2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049ce2c.md) [`0049d19c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049d19c.md) [`0049e834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049e834.md) [`0049e84c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049e84c.md) · 呼出先 10件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 4件 [`0049ce2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049ce2c.md) [`0049d19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d19c.md) [`0049e834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e834.md) [`0049e84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e84c.md) · 呼出先 10件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.04% / 新版 95.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049d0c0",
      "incomplete_value": false,
      "site": "0049d0c8",
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
            "const:e93:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d0c0",
      "incomplete_value": false,
      "site": "0049d0c8",
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
            "const:f20:8"
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
      "definition_site": "0049d0f8",
      "incomplete_value": true,
      "site": "0049d104",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049d0f8",
      "incomplete_value": true,
      "site": "0049d104",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049d11c",
      "incomplete_value": false,
      "site": "0049d13c",
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
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d11c",
      "incomplete_value": false,
      "site": "0049d13c",
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
            "const:c05:8"
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
      "0049d0c0",
      "PARAM",
      [
        "storage",
        "00298f20",
        null,
        "string"
      ]
    ],
    [
      "0049d0f8",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "0049d0f8",
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
      "0049d0c0",
      "PARAM",
      [
        "storage",
        "00298e93",
        null,
        "string"
      ]
    ],
    [
      "0049d0f8",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "0049d0f8",
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

- 旧版 [`0049d0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049cf60.md#insn-0049d0c0) · [`0049d0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049cf60.md#insn-0049d0f8) · [`0049d11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049cf60.md#insn-0049d11c)
- 新版 `0049d0c0`（命令位置の公開資料なし） · `0049d0f8`（命令位置の公開資料なし） · `0049d11c`（命令位置の公開資料なし）

~~~diff
- 0049d0c0 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 0049d0c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049d0c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049d0c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049d0c0 ["COPY", "tmp:0:8", ["const:e93:8"]]
+ 0049d0c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049d0c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049d0c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049d0c0 bytes 21803c91
+ 0049d0c0 bytes 214c3a91
- 0049d0f8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
- 0049d0f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049d0f8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
+ 0049d0f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0049d0f8 bytes 21ac47f9
+ 0049d0f8 bytes 21d447f9
- 0049d11c ["COPY", "tmp:0:8", ["const:c05:8"]]
- 0049d11c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049d11c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049d11c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049d11c ["COPY", "tmp:0:8", ["const:b78:8"]]
+ 0049d11c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049d11c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049d11c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049d11c bytes 00143091
+ 0049d11c bytes 00e02d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91021c8d84de636271def660d5a3394d"></a>

### [`0049d19c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049d19c.md) → [`0049d19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d19c.md) _ZN5Botan13EMSA_PKCS1v156verifyERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEES7_m

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0049cf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049cf60.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0049cf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cf60.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0049d260",
      "incomplete_value": true,
      "site": "0049d260",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049d260",
      "incomplete_value": true,
      "site": "0049d260",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0049d250",
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
      "0049d250",
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

- 旧版 [`0049d250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049d19c.md#insn-0049d250)
- 新版 `0049d250`（命令位置の公開資料なし）

~~~diff
- 0049d250 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 0049d250 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049d250 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 0049d250 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0049d250 bytes 299543f9
+ 0049d250 bytes 29bd43f9
~~~


<a id="compare-c1665be48ab98d498701980a037393a2"></a>

### [`0049d2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049d2b0.md) → [`0049d2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d2b0.md) _ZNK5Botan13EMSA_PKCS1v1515config_for_x509ERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0049d8dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049d8dc.md) [`0049da90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049da90.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0049d8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d8dc.md) [`0049da90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049da90.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.96% / 新版 96.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049d3ec",
      "incomplete_value": true,
      "site": "0049d3ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0049d3ec",
      "incomplete_value": true,
      "site": "0049d3ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0049d434",
      "incomplete_value": false,
      "site": "0049d43c",
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
            "const:83d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d434",
      "incomplete_value": false,
      "site": "0049d43c",
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
            "const:8ca:8"
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
      "definition_site": "0049d5f0",
      "incomplete_value": false,
      "site": "0049d5f8",
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
            "const:745:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d5f0",
      "incomplete_value": false,
      "site": "0049d5f8",
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
            "const:7d2:8"
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
      "0049d3e0",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "0049d3ec",
      "DATA",
      [
        "storage",
        "00be9198",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0049d434",
      "PARAM",
      [
        "storage",
        "002958ca",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0049d3e0",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "0049d3ec",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0049d434",
      "PARAM",
      [
        "storage",
        "0029583d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049d3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049d2b0.md#insn-0049d3e0) · [`0049d434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049d2b0.md#insn-0049d434) · [`0049d5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049d2b0.md#insn-0049d5f0)
- 新版 `0049d3e0`（命令位置の公開資料なし） · `0049d434`（命令位置の公開資料なし） · `0049d5f0`（命令位置の公開資料なし）

~~~diff
- 0049d3e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef8:8"]]
- 0049d3e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049d3e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
+ 0049d3e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0049d3e0 bytes 087d47f9
+ 0049d3e0 bytes 08a547f9
- 0049d434 ["COPY", "tmp:0:8", ["const:8ca:8"]]
- 0049d434 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049d434 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049d434 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049d434 ["COPY", "tmp:0:8", ["const:83d:8"]]
+ 0049d434 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049d434 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049d434 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049d434 bytes 21282391
+ 0049d434 bytes 21f42091
- 0049d5f0 ["COPY", "tmp:0:8", ["const:7d2:8"]]
- 0049d5f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049d5f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049d5f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049d5f0 ["COPY", "tmp:0:8", ["const:745:8"]]
+ 0049d5f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049d5f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049d5f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049d5f0 bytes 21481f91
+ 0049d5f0 bytes 21141d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcae2cc622127a3b547c1dcf7b4f3e6b"></a>

### [`0049da90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049da90.md) → [`0049da90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049da90.md) FUN_0049da90

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0049d2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049d2b0.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)
- 新版 呼出元 1件 [`0049d2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d2b0.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049daf4",
      "incomplete_value": false,
      "site": "0049dafc",
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
      "definition_site": "0049daf4",
      "incomplete_value": false,
      "site": "0049dafc",
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
      "0049daf4",
      "PARAM",
      [
        "storage",
        "0029b286",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0049daf4",
      "PARAM",
      [
        "storage",
        "0029b284",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049daf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049da90.md#insn-0049daf4)
- 新版 `0049daf4`（命令位置の公開資料なし）

~~~diff
- 0049daf4 ["COPY", "tmp:0:8", ["const:286:8"]]
- 0049daf4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049daf4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049daf4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049daf4 ["COPY", "tmp:0:8", ["const:284:8"]]
+ 0049daf4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049daf4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049daf4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049daf4 bytes 21180a91
+ 0049daf4 bytes 21100a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9f5a7c74eccf10df1b92e2f173efd94"></a>

### [`0049dbe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049dbe4.md) → [`0049dbe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049dbe4.md) _ZN5Botan13EMSA_PKCS1v15C1EPNS_12HashFunctionE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc670.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdbf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf40.md)
- 新版 呼出元 1件 [`00bdc6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6c0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049dc14",
      "incomplete_value": true,
      "site": "0049dc20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0049dc14",
      "incomplete_value": true,
      "site": "0049dc20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0049dc08",
      "READ",
      [
        "storage",
        "00c1b010",
        null,
        "pointer"
      ]
    ],
    [
      "0049dc20",
      "DATA",
      [
        "storage",
        "00be9568",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "0049dc08",
      "READ",
      [
        "storage",
        "00c1b060",
        null,
        "pointer"
      ]
    ],
    [
      "0049dc20",
      "DATA",
      [
        "storage",
        "00be95b8",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049dc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049dbe4.md#insn-0049dc08) · [`0049dc0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049dbe4.md#insn-0049dc0c)
- 新版 `0049dc08`（命令位置の公開資料なし） · `0049dc0c`（命令位置の公開資料なし）

~~~diff
- 0049dc08 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:10:8"]]
- 0049dc08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049dc08 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:60:8"]]
+ 0049dc08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0049dc08 bytes 290940f9
+ 0049dc08 bytes 293140f9
- 0049dc0c ["COPY", "register:4098:8", ["register:4000:8"]]
- 0049dc0c bytes f30300aa
+ 0049dc0c ["COPY", "register:4098:8", ["register:4000:8"]]
+ 0049dc0c bytes f30300aa
~~~


<a id="compare-d82d9fad3d7361b4b1e8c3ac84724c85"></a>

### [`0049dd0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049dd0c.md) → [`0049dd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049dd0c.md) _ZN5Botan12pkcs_hash_idERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf40.md) · 呼出先 9件 [`0041f354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f354.md) [`004a92b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a9/004a92b4.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdbf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf90.md) · 呼出先 9件 [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md) [`004a92b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a92b4.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.54% / 新版 96.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049df24",
      "incomplete_value": false,
      "site": "0049df2c",
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
            "const:3f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049df24",
      "incomplete_value": false,
      "site": "0049df2c",
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
            "const:36e:8"
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
      "definition_site": "0049df54",
      "incomplete_value": false,
      "site": "0049df5c",
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
            "const:b7d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049df54",
      "incomplete_value": false,
      "site": "0049df5c",
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
            "const:c0a:8"
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
      "definition_site": "0049df84",
      "incomplete_value": false,
      "site": "0049df8c",
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
            "const:d14:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049df84",
      "incomplete_value": false,
      "site": "0049df8c",
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
            "const:da1:8"
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
      "0049df24",
      "PARAM",
      [
        "storage",
        "0029e36e",
        null,
        "string"
      ]
    ],
    [
      "0049df54",
      "PARAM",
      [
        "storage",
        "00299c0a",
        null,
        "string"
      ]
    ],
    [
      "0049df84",
      "PARAM",
      [
        "storage",
        "00298da1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049df24",
      "PARAM",
      [
        "storage",
        "0029e3f9",
        null,
        "string"
      ]
    ],
    [
      "0049df54",
      "PARAM",
      [
        "storage",
        "00299b7d",
        null,
        "string"
      ]
    ],
    [
      "0049df84",
      "PARAM",
      [
        "storage",
        "00298d14",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049df24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049dd0c.md#insn-0049df24) · [`0049df54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049dd0c.md#insn-0049df54) · [`0049df84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049dd0c.md#insn-0049df84)
- 新版 `0049df24`（命令位置の公開資料なし） · `0049df54`（命令位置の公開資料なし） · `0049df84`（命令位置の公開資料なし）

~~~diff
- 0049df24 ["COPY", "tmp:0:8", ["const:36e:8"]]
- 0049df24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049df24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049df24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049df24 ["COPY", "tmp:0:8", ["const:3f9:8"]]
+ 0049df24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049df24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049df24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049df24 bytes 21b80d91
+ 0049df24 bytes 21e40f91
- 0049df54 ["COPY", "tmp:0:8", ["const:c0a:8"]]
- 0049df54 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049df54 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049df54 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049df54 ["COPY", "tmp:0:8", ["const:b7d:8"]]
+ 0049df54 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049df54 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049df54 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049df54 bytes 21283091
+ 0049df54 bytes 21f42d91
- 0049df84 ["COPY", "tmp:0:8", ["const:da1:8"]]
- 0049df84 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049df84 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049df84 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049df84 ["COPY", "tmp:0:8", ["const:d14:8"]]
+ 0049df84 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049df84 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049df84 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049df84 bytes 21843691
+ 0049df84 bytes 21503491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-254f00fde3600ea34f67640c7afeb9fb"></a>

### [`0049e24c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049e24c.md) → [`0049e24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e24c.md) _ZN5Botan17EMSA_PKCS1v15_RawC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc660.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdbf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf40.md) [`00bdbf50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf50.md)
- 新版 呼出元 1件 [`00bdc6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6b0.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf90.md) [`00bdbfa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbfa0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049e280",
      "incomplete_value": true,
      "site": "0049e288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0049e280",
      "incomplete_value": true,
      "site": "0049e288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0049e270",
      "READ",
      [
        "storage",
        "00c1b018",
        null,
        "pointer"
      ]
    ],
    [
      "0049e288",
      "DATA",
      [
        "storage",
        "00be95c0",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "0049e270",
      "READ",
      [
        "storage",
        "00c1b068",
        null,
        "pointer"
      ]
    ],
    [
      "0049e288",
      "DATA",
      [
        "storage",
        "00be9610",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049e270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049e24c.md#insn-0049e270)
- 新版 `0049e270`（命令位置の公開資料なし）

~~~diff
- 0049e270 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:18:8"]]
- 0049e270 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049e270 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:68:8"]]
+ 0049e270 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0049e270 bytes 080d40f9
+ 0049e270 bytes 083540f9
~~~


<a id="compare-1c02e7be73f11def9224e3e23a091315"></a>

### [`0049e708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049e708.md) → [`0049e708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e708.md) _ZN5Botan17EMSA_PKCS1v15_Raw8raw_dataEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049e790",
      "incomplete_value": false,
      "site": "0049e798",
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
            "const:556:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049e790",
      "incomplete_value": false,
      "site": "0049e798",
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
            "const:4cb:8"
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
      "definition_site": "0049e7cc",
      "incomplete_value": true,
      "site": "0049e7d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049e7cc",
      "incomplete_value": true,
      "site": "0049e7d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0049e790",
      "PARAM",
      [
        "storage",
        "002a54cb",
        null,
        "string"
      ]
    ],
    [
      "0049e7cc",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "0049e7cc",
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
      "0049e790",
      "PARAM",
      [
        "storage",
        "002a5556",
        null,
        "string"
      ]
    ],
    [
      "0049e7cc",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "0049e7cc",
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

- 旧版 [`0049e790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049e708.md#insn-0049e790) · [`0049e7cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049e708.md#insn-0049e7cc)
- 新版 `0049e790`（命令位置の公開資料なし） · `0049e7cc`（命令位置の公開資料なし）

~~~diff
- 0049e790 ["COPY", "tmp:0:8", ["const:4cb:8"]]
- 0049e790 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049e790 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049e790 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049e790 ["COPY", "tmp:0:8", ["const:556:8"]]
+ 0049e790 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049e790 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049e790 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049e790 bytes 212c1391
+ 0049e790 bytes 21581591
- 0049e7cc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
- 0049e7cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049e7cc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
+ 0049e7cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0049e7cc bytes 21ac47f9
+ 0049e7cc bytes 21d447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be879016eba818f93e9b7d09249f3ac9"></a>

### [`0049e948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049e948.md) → [`0049e948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e948.md) _ZN5Botan4PSSRC1EPNS_12HashFunctionE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049e968",
      "incomplete_value": true,
      "site": "0049e96c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0049e968",
      "incomplete_value": true,
      "site": "0049e96c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0049e960",
      "READ",
      [
        "storage",
        "00c1b020",
        null,
        "pointer"
      ]
    ],
    [
      "0049e96c",
      "DATA",
      [
        "storage",
        "00be9618",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "0049e960",
      "READ",
      [
        "storage",
        "00c1b070",
        null,
        "pointer"
      ]
    ],
    [
      "0049e96c",
      "DATA",
      [
        "storage",
        "00be9668",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049e960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049e948.md#insn-0049e960)
- 新版 `0049e960`（命令位置の公開資料なし）

~~~diff
- 0049e960 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:20:8"]]
- 0049e960 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049e960 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:70:8"]]
+ 0049e960 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0049e960 bytes 081140f9
+ 0049e960 bytes 083940f9
~~~


<a id="compare-deb7b841bae66b7a4714e4810b3cb02f"></a>

### [`0049eb38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049eb38.md) → [`0049eb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049eb38.md) FUN_0049eb38

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0049ea3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049ea3c.md) [`0049ffc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049f/0049ffc4.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 2件 [`0049ea3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049ea3c.md) [`0049ffc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049ffc4.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.15% / 新版 99.15%

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
      "definition_site": "0049ede8",
      "incomplete_value": true,
      "site": "0049ede8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049ede8",
      "incomplete_value": true,
      "site": "0049ede8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 18,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049ee74",
      "incomplete_value": true,
      "site": "0049ee80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049ee74",
      "incomplete_value": true,
      "site": "0049ee80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049eed4",
      "incomplete_value": true,
      "site": "0049eee0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049eed4",
      "incomplete_value": true,
      "site": "0049eee0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0049edd8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0049ee74",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "0049ee74",
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
      "0049edd8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0049ee74",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "0049ee74",
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

- 旧版 [`0049edd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049eb38.md#insn-0049edd8) · [`0049ee74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049eb38.md#insn-0049ee74) · [`0049eed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049eb38.md#insn-0049eed4)
- 新版 `0049edd8`（命令位置の公開資料なし） · `0049ee74`（命令位置の公開資料なし） · `0049eed4`（命令位置の公開資料なし）

~~~diff
- 0049edd8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 0049edd8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049edd8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 0049edd8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0049edd8 bytes 299543f9
+ 0049edd8 bytes 29bd43f9
- 0049ee74 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
- 0049ee74 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049ee74 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
+ 0049ee74 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0049ee74 bytes 21ac47f9
+ 0049ee74 bytes 21d447f9
- 0049eed4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
- 0049eed4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049eed4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
+ 0049eed4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0049eed4 bytes 21ac47f9
+ 0049eed4 bytes 21d447f9
~~~


<a id="compare-6238146b3d8ecc77c195e6e1436e58f1"></a>

### [`0049ef6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049ef6c.md) → [`0049ef6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049ef6c.md) FUN_0049ef6c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0049ef64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049ef64.md) [`004a00c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a0/004a00c0.md) · 呼出先 10件 [`0048e51c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048e/0048e51c.md) [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`0049cdcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049cdcc.md) [`0051d3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d3cc.md) [`00520980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520980.md)
- 新版 呼出元 2件 [`0049ef64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049ef64.md) [`004a00c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a00c0.md) · 呼出先 10件 [`0048e51c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048e/0048e51c.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`0049cdcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cdcc.md) [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`00520980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520980.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.22% / 新版 99.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0049f358",
      "incomplete_value": true,
      "site": "0049f358",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049f358",
      "incomplete_value": true,
      "site": "0049f358",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0049f348",
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
      "0049f348",
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

- 旧版 [`0049f348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049ef6c.md#insn-0049f348)
- 新版 `0049f348`（命令位置の公開資料なし）

~~~diff
- 0049f348 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 0049f348 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049f348 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 0049f348 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0049f348 bytes 299543f9
+ 0049f348 bytes 29bd43f9
~~~


<a id="compare-e2320a5ccd2f9ffc183d9f8902305ba3"></a>

### [`0049f3b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049f/0049f3b8.md) → [`0049f3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049f3b8.md) _ZNK5Botan4PSSR4nameEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.09% / 新版 97.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049f3f8",
      "incomplete_value": false,
      "site": "0049f404",
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
            "const:27f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049f3f8",
      "incomplete_value": false,
      "site": "0049f404",
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
            "const:1e5:8"
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
      "definition_site": "0049f424",
      "incomplete_value": false,
      "site": "0049f42c",
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
            "const:4d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049f424",
      "incomplete_value": false,
      "site": "0049f42c",
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
            "const:449:8"
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
      "definition_site": "0049f494",
      "incomplete_value": false,
      "site": "0049f49c",
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
      "definition_site": "0049f494",
      "incomplete_value": false,
      "site": "0049f49c",
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
      "0049f3f8",
      "PARAM",
      [
        "storage",
        "002a81e5",
        null,
        "string"
      ]
    ],
    [
      "0049f424",
      "PARAM",
      [
        "storage",
        "0029d449",
        null,
        "string"
      ]
    ],
    [
      "0049f494",
      "PARAM",
      [
        "storage",
        "0029b286",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0049f3f8",
      "PARAM",
      [
        "storage",
        "002a827f",
        null,
        "string"
      ]
    ],
    [
      "0049f424",
      "PARAM",
      [
        "storage",
        "0029d4d4",
        null,
        "string"
      ]
    ],
    [
      "0049f494",
      "PARAM",
      [
        "storage",
        "0029b284",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049f3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049f/0049f3b8.md#insn-0049f3f8) · [`0049f424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049f/0049f3b8.md#insn-0049f424) · [`0049f494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049f/0049f3b8.md#insn-0049f494)
- 新版 `0049f3f8`（命令位置の公開資料なし） · `0049f424`（命令位置の公開資料なし） · `0049f494`（命令位置の公開資料なし）

~~~diff
- 0049f3f8 ["COPY", "tmp:0:8", ["const:1e5:8"]]
- 0049f3f8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0049f3f8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0049f3f8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0049f3f8 ["COPY", "tmp:0:8", ["const:27f:8"]]
+ 0049f3f8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0049f3f8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0049f3f8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0049f3f8 bytes 42940791
+ 0049f3f8 bytes 42fc0991
- 0049f424 ["COPY", "tmp:0:8", ["const:449:8"]]
- 0049f424 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049f424 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049f424 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049f424 ["COPY", "tmp:0:8", ["const:4d4:8"]]
+ 0049f424 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049f424 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049f424 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049f424 bytes 21241191
+ 0049f424 bytes 21501391
- 0049f494 ["COPY", "tmp:0:8", ["const:286:8"]]
- 0049f494 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049f494 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049f494 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049f494 ["COPY", "tmp:0:8", ["const:284:8"]]
+ 0049f494 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049f494 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049f494 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049f494 bytes 21180a91
+ 0049f494 bytes 21100a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-055f7a269c519d54a8427036b177035a"></a>

### [`0049f624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049f/0049f624.md) → [`0049f624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049f624.md) _ZNK5Botan4PSSR15config_for_x509ERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 22件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`0049d8dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049d8dc.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md)
- 新版 呼出元 0件  · 呼出先 22件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`0049d8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d8dc.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.99% / 新版 94.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049f760",
      "incomplete_value": true,
      "site": "0049f760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0049f760",
      "incomplete_value": true,
      "site": "0049f760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0049f7a0",
      "incomplete_value": true,
      "site": "0049f7a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049f7a0",
      "incomplete_value": true,
      "site": "0049f7a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:327:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0049f91c",
      "incomplete_value": true,
      "site": "0049f91c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0049f91c",
      "incomplete_value": true,
      "site": "0049f91c",
      "value": [
        "LOAD",
        "8",
        [
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
      "0049f754",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "0049f760",
      "DATA",
      [
        "storage",
        "00be9198",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0049f788",
      "READ",
      [
        "storage",
        "002a1327",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049f754",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "0049f760",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0049f788",
      "READ",
      [
        "storage",
        "002a13b2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049f754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049f/0049f624.md#insn-0049f754) · [`0049f780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049f/0049f624.md#insn-0049f780) · [`0049f90c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049f/0049f624.md#insn-0049f90c)
- 新版 `0049f754`（命令位置の公開資料なし） · `0049f780`（命令位置の公開資料なし） · `0049f90c`（命令位置の公開資料なし）

~~~diff
- 0049f754 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef8:8"]]
- 0049f754 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049f754 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
+ 0049f754 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0049f754 bytes 087d47f9
+ 0049f754 bytes 08a547f9
- 0049f780 ["COPY", "tmp:0:8", ["const:327:8"]]
- 0049f780 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0049f780 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0049f780 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0049f780 ["COPY", "tmp:0:8", ["const:3b2:8"]]
+ 0049f780 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0049f780 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0049f780 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0049f780 bytes 299d0c91
+ 0049f780 bytes 29c90e91
- 0049f90c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0049f90c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049f90c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0049f90c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0049f90c bytes a99643f9
+ 0049f90c bytes a9be43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2614db3c9834ec50d0892d18f6fa3d2"></a>

### [`0049fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049f/0049fddc.md) → [`0049fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049fddc.md) _ZN5Botan8PSSR_RawC1EPNS_12HashFunctionE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0049fdfc",
      "incomplete_value": true,
      "site": "0049fe00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0049fdfc",
      "incomplete_value": true,
      "site": "0049fe00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0049fdf4",
      "READ",
      [
        "storage",
        "00c1b028",
        null,
        "pointer"
      ]
    ],
    [
      "0049fe00",
      "DATA",
      [
        "storage",
        "00be9670",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "0049fdf4",
      "READ",
      [
        "storage",
        "00c1b078",
        null,
        "pointer"
      ]
    ],
    [
      "0049fe00",
      "DATA",
      [
        "storage",
        "00be96c0",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049fdf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049f/0049fddc.md#insn-0049fdf4)
- 新版 `0049fdf4`（命令位置の公開資料なし）

~~~diff
- 0049fdf4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:28:8"]]
- 0049fdf4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049fdf4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:78:8"]]
+ 0049fdf4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0049fdf4 bytes 081540f9
+ 0049fdf4 bytes 083d40f9
~~~


<a id="compare-6133946a49a0bbce61f0f75fdaff9c1f"></a>

### [`0049fe7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049f/0049fe7c.md) → [`0049fe7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049fe7c.md) _ZN5Botan8PSSR_Raw8raw_dataEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

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
      "definition_site": "0049ff20",
      "incomplete_value": false,
      "site": "0049ff28",
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
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ff20",
      "incomplete_value": false,
      "site": "0049ff28",
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
            "const:8d5:8"
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
      "definition_site": "0049ff58",
      "incomplete_value": true,
      "site": "0049ff64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049ff58",
      "incomplete_value": true,
      "site": "0049ff64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0049ff20",
      "PARAM",
      [
        "storage",
        "002938d5",
        null,
        "string"
      ]
    ],
    [
      "0049ff58",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "0049ff58",
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
      "0049ff20",
      "PARAM",
      [
        "storage",
        "00293848",
        null,
        "string"
      ]
    ],
    [
      "0049ff58",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "0049ff58",
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

- 旧版 [`0049ff20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049f/0049fe7c.md#insn-0049ff20) · [`0049ff58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049f/0049fe7c.md#insn-0049ff58)
- 新版 `0049ff20`（命令位置の公開資料なし） · `0049ff58`（命令位置の公開資料なし）

~~~diff
- 0049ff20 ["COPY", "tmp:0:8", ["const:8d5:8"]]
- 0049ff20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049ff20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049ff20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049ff20 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 0049ff20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049ff20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049ff20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049ff20 bytes 21542391
+ 0049ff20 bytes 21202191
- 0049ff58 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
- 0049ff58 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049ff58 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
+ 0049ff58 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0049ff58 bytes 21ac47f9
+ 0049ff58 bytes 21d447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-287f585995dd47582e8d0f99d2010524"></a>

### [`004a00c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a0/004a00c8.md) → [`004a00c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a00c8.md) _ZNK5Botan8PSSR_Raw4nameEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.09% / 新版 97.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a0108",
      "incomplete_value": false,
      "site": "004a0114",
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
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0108",
      "incomplete_value": false,
      "site": "004a0114",
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
            "const:a15:8"
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
      "definition_site": "004a0134",
      "incomplete_value": false,
      "site": "004a013c",
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
            "const:4d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0134",
      "incomplete_value": false,
      "site": "004a013c",
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
            "const:449:8"
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
      "definition_site": "004a01a4",
      "incomplete_value": false,
      "site": "004a01ac",
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
      "definition_site": "004a01a4",
      "incomplete_value": false,
      "site": "004a01ac",
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
      "004a0108",
      "PARAM",
      [
        "storage",
        "00291a15",
        null,
        "string"
      ]
    ],
    [
      "004a0134",
      "PARAM",
      [
        "storage",
        "0029d449",
        null,
        "string"
      ]
    ],
    [
      "004a01a4",
      "PARAM",
      [
        "storage",
        "0029b286",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004a0108",
      "PARAM",
      [
        "storage",
        "00291988",
        null,
        "string"
      ]
    ],
    [
      "004a0134",
      "PARAM",
      [
        "storage",
        "0029d4d4",
        null,
        "string"
      ]
    ],
    [
      "004a01a4",
      "PARAM",
      [
        "storage",
        "0029b284",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a0108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a0/004a00c8.md#insn-004a0108) · [`004a0134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a0/004a00c8.md#insn-004a0134) · [`004a01a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a0/004a00c8.md#insn-004a01a4)
- 新版 `004a0108`（命令位置の公開資料なし） · `004a0134`（命令位置の公開資料なし） · `004a01a4`（命令位置の公開資料なし）

~~~diff
- 004a0108 ["COPY", "tmp:0:8", ["const:a15:8"]]
- 004a0108 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004a0108 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004a0108 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004a0108 ["COPY", "tmp:0:8", ["const:988:8"]]
+ 004a0108 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004a0108 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004a0108 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004a0108 bytes 42542891
+ 004a0108 bytes 42202691
- 004a0134 ["COPY", "tmp:0:8", ["const:449:8"]]
- 004a0134 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a0134 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a0134 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a0134 ["COPY", "tmp:0:8", ["const:4d4:8"]]
+ 004a0134 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a0134 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a0134 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a0134 bytes 21241191
+ 004a0134 bytes 21501391
- 004a01a4 ["COPY", "tmp:0:8", ["const:286:8"]]
- 004a01a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a01a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a01a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a01a4 ["COPY", "tmp:0:8", ["const:284:8"]]
+ 004a01a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a01a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a01a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a01a4 bytes 21180a91
+ 004a01a4 bytes 21100a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc81d6472563a3842fb61134af5dd026"></a>

### [`004a0334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a0/004a0334.md) → [`004a0334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0334.md) _ZN5Botan14Entropy_Source6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "004a03f8",
      "incomplete_value": false,
      "site": "004a0400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bec000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a03f8",
      "incomplete_value": false,
      "site": "004a0400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bec000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "004a0400",
      "DATA",
      [
        "storage",
        "00becc78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004a0400",
      "DATA",
      [
        "storage",
        "00beccc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a03f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a0/004a0334.md#insn-004a03f8)
- 新版 `004a03f8`（命令位置の公開資料なし）

~~~diff
- 004a03f8 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 004a03f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004a03f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004a03f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004a03f8 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 004a03f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004a03f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004a03f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004a03f8 bytes 29e13191
+ 004a03f8 bytes 29213391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-339ad585795ef62d4be2ae069f6c673c"></a>

### [`004a0c64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a0/004a0c64.md) → [`004a0c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0c64.md) _ZN5Botan15Entropy_Sources14global_sourcesEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md) [`00450668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450668.md) [`004a0fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a0/004a0fc4.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md) [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`004a0fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0fc4.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 90.07% / 新版 90.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a0ccc",
      "incomplete_value": false,
      "site": "004a0cd0",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0ccc",
      "incomplete_value": false,
      "site": "004a0cd0",
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
            "const:360:8"
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
      "definition_site": "004a0cdc",
      "incomplete_value": false,
      "site": "004a0ce8",
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
            "const:4ac:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0cdc",
      "incomplete_value": false,
      "site": "004a0ce8",
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
            "const:421:8"
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
      "definition_site": "004a0cf4",
      "incomplete_value": false,
      "site": "004a0cfc",
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
            "const:bfb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0cf4",
      "incomplete_value": false,
      "site": "004a0cfc",
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
            "const:c88:8"
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
      "004a0c90",
      "READ",
      [
        "storage",
        "00c25360",
        null,
        "undefined1"
      ]
    ],
    [
      "004a0cac",
      "DATA",
      [
        "storage",
        "00c25348",
        null,
        null
      ]
    ],
    [
      "004a0ccc",
      "PARAM",
      [
        "storage",
        "00c25360",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004a0c90",
      "READ",
      [
        "storage",
        "00c253a0",
        null,
        "undefined1"
      ]
    ],
    [
      "004a0cac",
      "DATA",
      [
        "storage",
        "00c25388",
        null,
        null
      ]
    ],
    [
      "004a0ccc",
      "PARAM",
      [
        "storage",
        "00c253a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a0c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a0/004a0c64.md#insn-004a0c8c) · [`004a0cac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a0/004a0c64.md#insn-004a0cac) · [`004a0ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a0/004a0c64.md#insn-004a0ccc)
- 新版 `004a0c8c`（命令位置の公開資料なし） · `004a0cac`（命令位置の公開資料なし） · `004a0ccc`（命令位置の公開資料なし）

~~~diff
- 004a0c8c ["COPY", "tmp:0:8", ["const:360:8"]]
- 004a0c8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004a0c8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004a0c8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004a0c8c ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 004a0c8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004a0c8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004a0c8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004a0c8c bytes 08810d91
+ 004a0c8c bytes 08810e91
- 004a0cac ["COPY", "tmp:0:8", ["const:348:8"]]
- 004a0cac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004a0cac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004a0cac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004a0cac ["COPY", "tmp:0:8", ["const:388:8"]]
+ 004a0cac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004a0cac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004a0cac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004a0cac bytes 00200d91
+ 004a0cac bytes 00200e91
- 004a0ccc ["COPY", "tmp:0:8", ["const:360:8"]]
- 004a0ccc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004a0ccc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004a0ccc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004a0ccc ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 004a0ccc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004a0ccc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004a0ccc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004a0ccc bytes 00800d91
+ 004a0ccc bytes 00800e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-636964f1a09e8d6e094dae02248a8f4c"></a>

### [`004a1040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1040.md) → [`004a1040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1040.md) _ZN5Botan19StreamCipher_FilterC1EPNS_12StreamCipherE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md) [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a1074",
      "incomplete_value": true,
      "site": "004a107c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a1074",
      "incomplete_value": true,
      "site": "004a107c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a10b0",
      "incomplete_value": true,
      "site": "004a10b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a10b0",
      "incomplete_value": true,
      "site": "004a10b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a1130",
      "incomplete_value": true,
      "site": "004a1138",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a1130",
      "incomplete_value": true,
      "site": "004a1138",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a1060",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a107c",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a10a4",
      "READ",
      [
        "storage",
        "00c1b038",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a1060",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a107c",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a10a4",
      "READ",
      [
        "storage",
        "00c1b088",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1040.md#insn-004a1060) · [`004a10a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1040.md#insn-004a10a4) · [`004a1128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1040.md#insn-004a1128)
- 新版 `004a1060`（命令位置の公開資料なし） · `004a10a4`（命令位置の公開資料なし） · `004a1128`（命令位置の公開資料なし）

~~~diff
- 004a1060 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 004a1060 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a1060 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 004a1060 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a1060 bytes 081940f9
+ 004a1060 bytes 084140f9
- 004a10a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:38:8"]]
- 004a10a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a10a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:88:8"]]
+ 004a10a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a10a4 bytes 081d40f9
+ 004a10a4 bytes 084540f9
- 004a1128 ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 004a1128 ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 004a1128 bytes c23b00b0
+ 004a1128 bytes c23b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-268bc30d7d7d0a0b316d2f43a1bd7449"></a>

### [`004a1190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1190.md) → [`004a1190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1190.md) _ZN5Botan19StreamCipher_FilterC2EPNS_12StreamCipherERKNS_11OctetStringE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00499b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499b28.md) [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md) [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00499b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499b28.md) [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a11cc",
      "incomplete_value": true,
      "site": "004a11d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a11cc",
      "incomplete_value": true,
      "site": "004a11d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a120c",
      "incomplete_value": true,
      "site": "004a1214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a120c",
      "incomplete_value": true,
      "site": "004a1214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a12a0",
      "incomplete_value": true,
      "site": "004a12a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a12a0",
      "incomplete_value": true,
      "site": "004a12a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a11b8",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a11d4",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a11fc",
      "READ",
      [
        "storage",
        "00c1b038",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a11b8",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a11d4",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a11fc",
      "READ",
      [
        "storage",
        "00c1b088",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a11b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1190.md#insn-004a11b8) · [`004a11fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1190.md#insn-004a11fc) · [`004a1298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1190.md#insn-004a1298)
- 新版 `004a11b8`（命令位置の公開資料なし） · `004a11fc`（命令位置の公開資料なし） · `004a1298`（命令位置の公開資料なし）

~~~diff
- 004a11b8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:30:8"]]
- 004a11b8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a11b8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:80:8"]]
+ 004a11b8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a11b8 bytes 291940f9
+ 004a11b8 bytes 294140f9
- 004a11fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:38:8"]]
- 004a11fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a11fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:88:8"]]
+ 004a11fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a11fc bytes 081d40f9
+ 004a11fc bytes 084540f9
- 004a1298 ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 004a1298 ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 004a1298 bytes c23b00b0
+ 004a1298 bytes c23b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ad5f54307af0b7b5acebafb9e502b13"></a>

### [`004a1328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1328.md) → [`004a1328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1328.md) _ZN5Botan19StreamCipher_FilterC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md) [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.04% / 新版 89.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a135c",
      "incomplete_value": true,
      "site": "004a1364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a135c",
      "incomplete_value": true,
      "site": "004a1364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a139c",
      "incomplete_value": true,
      "site": "004a13a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a139c",
      "incomplete_value": true,
      "site": "004a13a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a143c",
      "incomplete_value": true,
      "site": "004a1444",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a143c",
      "incomplete_value": true,
      "site": "004a1444",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a1348",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a1364",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a138c",
      "READ",
      [
        "storage",
        "00c1b038",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a1348",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a1364",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a138c",
      "READ",
      [
        "storage",
        "00c1b088",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1328.md#insn-004a1348) · [`004a138c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1328.md#insn-004a138c) · [`004a1434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1328.md#insn-004a1434)
- 新版 `004a1348`（命令位置の公開資料なし） · `004a138c`（命令位置の公開資料なし） · `004a1434`（命令位置の公開資料なし）

~~~diff
- 004a1348 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 004a1348 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a1348 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 004a1348 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a1348 bytes 081940f9
+ 004a1348 bytes 084140f9
- 004a138c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:38:8"]]
- 004a138c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a138c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:88:8"]]
+ 004a138c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a138c bytes 081d40f9
+ 004a138c bytes 084540f9
- 004a1434 ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 004a1434 ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 004a1434 bytes c23b00b0
+ 004a1434 bytes c23b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22fa5ba27b0f5f070721f0d8794918aa"></a>

### [`004a14bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a14bc.md) → [`004a14bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a14bc.md) _ZN5Botan12StreamCipher15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbfb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbfb0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdc000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc000.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a1534",
      "incomplete_value": false,
      "site": "004a153c",
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
            "const:5d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a1534",
      "incomplete_value": false,
      "site": "004a153c",
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
            "const:537:8"
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
      "definition_site": "004a1574",
      "incomplete_value": true,
      "site": "004a1580",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a1574",
      "incomplete_value": true,
      "site": "004a1580",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe8:8"
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
      "004a1534",
      "PARAM",
      [
        "storage",
        "002a9537",
        null,
        "string"
      ]
    ],
    [
      "004a1574",
      "READ",
      [
        "storage",
        "00c1afe8",
        null,
        "pointer"
      ]
    ],
    [
      "004a1574",
      "PARAM",
      [
        "storage",
        "00be93e8",
        "_ZTIN5Botan12Lookup_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a1534",
      "PARAM",
      [
        "storage",
        "002a95d1",
        null,
        "string"
      ]
    ],
    [
      "004a1574",
      "READ",
      [
        "storage",
        "00c1b038",
        null,
        "pointer"
      ]
    ],
    [
      "004a1574",
      "PARAM",
      [
        "storage",
        "00be9438",
        "_ZTIN5Botan12Lookup_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a14bc.md#insn-004a1534) · [`004a1568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a14bc.md#insn-004a1568) · [`004a1574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a14bc.md#insn-004a1574)
- 新版 `004a1534`（命令位置の公開資料なし） · `004a1568`（命令位置の公開資料なし） · `004a1574`（命令位置の公開資料なし）

~~~diff
- 004a1534 ["COPY", "tmp:0:8", ["const:537:8"]]
- 004a1534 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a1534 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a1534 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a1534 ["COPY", "tmp:0:8", ["const:5d1:8"]]
+ 004a1534 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a1534 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a1534 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a1534 bytes 21dc1491
+ 004a1534 bytes 21441791
- 004a1568 ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 004a1568 ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 004a1568 bytes c13b00b0
+ 004a1568 bytes c13b00d0
- 004a1574 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fe8:8"]]
- 004a1574 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a1574 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:38:8"]]
+ 004a1574 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a1574 bytes 21f447f9
+ 004a1574 bytes 211c40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-695e60d9803c4d62003cac7898f88977"></a>

### [`004a15d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a15d0.md) → [`004a15d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a15d0.md) _ZN5Botan19StreamCipher_FilterC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS_11OctetStringE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00499b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499b28.md) [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md) [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00499b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499b28.md) [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a160c",
      "incomplete_value": true,
      "site": "004a1614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a160c",
      "incomplete_value": true,
      "site": "004a1614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a164c",
      "incomplete_value": true,
      "site": "004a1654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a164c",
      "incomplete_value": true,
      "site": "004a1654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a1700",
      "incomplete_value": true,
      "site": "004a1708",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a1700",
      "incomplete_value": true,
      "site": "004a1708",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a15f8",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a1614",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a163c",
      "READ",
      [
        "storage",
        "00c1b038",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a15f8",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a1614",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a163c",
      "READ",
      [
        "storage",
        "00c1b088",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a15f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a15d0.md#insn-004a15f8) · [`004a163c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a15d0.md#insn-004a163c) · [`004a16f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a15d0.md#insn-004a16f8)
- 新版 `004a15f8`（命令位置の公開資料なし） · `004a163c`（命令位置の公開資料なし） · `004a16f8`（命令位置の公開資料なし）

~~~diff
- 004a15f8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:30:8"]]
- 004a15f8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a15f8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:80:8"]]
+ 004a15f8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a15f8 bytes 291940f9
+ 004a15f8 bytes 294140f9
- 004a163c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:38:8"]]
- 004a163c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a163c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:88:8"]]
+ 004a163c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a163c bytes 081d40f9
+ 004a163c bytes 084540f9
- 004a16f8 ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 004a16f8 ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 004a16f8 bytes c23b00b0
+ 004a16f8 bytes c23b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a561df2ff524c8f3d076ad436ecb1ec"></a>

### [`004a181c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a181c.md) → [`004a181c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a181c.md) _ZN5Botan11Hash_FilterC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdbfd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbfd0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

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
      "definition_site": "004a1858",
      "incomplete_value": true,
      "site": "004a1860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a1858",
      "incomplete_value": true,
      "site": "004a1860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a188c",
      "incomplete_value": true,
      "site": "004a1894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a188c",
      "incomplete_value": true,
      "site": "004a1894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004a1844",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a1860",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a1880",
      "READ",
      [
        "storage",
        "00c1b040",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a1844",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a1860",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a1880",
      "READ",
      [
        "storage",
        "00c1b090",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a181c.md#insn-004a1844) · [`004a1880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a181c.md#insn-004a1880)
- 新版 `004a1844`（命令位置の公開資料なし） · `004a1880`（命令位置の公開資料なし）

~~~diff
- 004a1844 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:30:8"]]
- 004a1844 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a1844 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:80:8"]]
+ 004a1844 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a1844 bytes 291940f9
+ 004a1844 bytes 294140f9
- 004a1880 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:40:8"]]
- 004a1880 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a1880 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:90:8"]]
+ 004a1880 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a1880 bytes 082140f9
+ 004a1880 bytes 084940f9
~~~


<a id="compare-4e3e0ef3357016e284f6ff4382aca426"></a>

### [`004a1940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1940.md) → [`004a1940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1940.md) _ZN5Botan6FilterC2Ev

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.61% / 新版 82.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a1964",
      "incomplete_value": true,
      "site": "004a1968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a1964",
      "incomplete_value": true,
      "site": "004a1968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004a195c",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a1968",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004a195c",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a1968",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a195c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1940.md#insn-004a195c) · [`004a1960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1940.md#insn-004a1960)
- 新版 `004a195c`（命令位置の公開資料なし） · `004a1960`（命令位置の公開資料なし）

~~~diff
- 004a195c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 004a195c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a195c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 004a195c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a195c bytes 081940f9
+ 004a195c bytes 084140f9
- 004a1960 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 004a1960 bytes f40300aa
+ 004a1960 ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 004a1960 bytes f40300aa
~~~


<a id="compare-16c852241b0d73cf342e955bbd15447f"></a>

### [`004a19c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a19c4.md) → [`004a19c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a19c4.md) _ZN5Botan12HashFunction15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbfd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbfd0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdc020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc020.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a1a3c",
      "incomplete_value": false,
      "site": "004a1a44",
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
            "const:7bf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a1a3c",
      "incomplete_value": false,
      "site": "004a1a44",
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
            "const:84c:8"
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
      "definition_site": "004a1a7c",
      "incomplete_value": true,
      "site": "004a1a88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a1a7c",
      "incomplete_value": true,
      "site": "004a1a88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe8:8"
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
      "004a1a3c",
      "PARAM",
      [
        "storage",
        "0029284c",
        null,
        null
      ]
    ],
    [
      "004a1a7c",
      "READ",
      [
        "storage",
        "00c1afe8",
        null,
        "pointer"
      ]
    ],
    [
      "004a1a7c",
      "PARAM",
      [
        "storage",
        "00be93e8",
        "_ZTIN5Botan12Lookup_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a1a3c",
      "PARAM",
      [
        "storage",
        "002927bf",
        null,
        null
      ]
    ],
    [
      "004a1a7c",
      "READ",
      [
        "storage",
        "00c1b038",
        null,
        "pointer"
      ]
    ],
    [
      "004a1a7c",
      "PARAM",
      [
        "storage",
        "00be9438",
        "_ZTIN5Botan12Lookup_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a19c4.md#insn-004a1a3c) · [`004a1a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a19c4.md#insn-004a1a70) · [`004a1a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a19c4.md#insn-004a1a7c)
- 新版 `004a1a3c`（命令位置の公開資料なし） · `004a1a70`（命令位置の公開資料なし） · `004a1a7c`（命令位置の公開資料なし）

~~~diff
- 004a1a3c ["COPY", "tmp:0:8", ["const:84c:8"]]
- 004a1a3c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a1a3c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a1a3c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a1a3c ["COPY", "tmp:0:8", ["const:7bf:8"]]
+ 004a1a3c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a1a3c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a1a3c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a1a3c bytes 21302191
+ 004a1a3c bytes 21fc1e91
- 004a1a70 ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 004a1a70 ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 004a1a70 bytes c13b00b0
+ 004a1a70 bytes c13b00d0
- 004a1a7c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fe8:8"]]
- 004a1a7c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a1a7c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:38:8"]]
+ 004a1a7c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a1a7c bytes 21f447f9
+ 004a1a7c bytes 211c40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5eecdcda3b38a198bd26562b17d03fd5"></a>

### [`004a1bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1bfc.md) → [`004a1bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1bfc.md) _ZN5Botan10MAC_FilterC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdbfe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbfe0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc030.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

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
      "definition_site": "004a1c38",
      "incomplete_value": true,
      "site": "004a1c40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a1c38",
      "incomplete_value": true,
      "site": "004a1c40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a1c6c",
      "incomplete_value": true,
      "site": "004a1c74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a1c6c",
      "incomplete_value": true,
      "site": "004a1c74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004a1c24",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a1c40",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a1c60",
      "READ",
      [
        "storage",
        "00c1b048",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a1c24",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a1c40",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a1c60",
      "READ",
      [
        "storage",
        "00c1b098",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1bfc.md#insn-004a1c24) · [`004a1c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1bfc.md#insn-004a1c60)
- 新版 `004a1c24`（命令位置の公開資料なし） · `004a1c60`（命令位置の公開資料なし）

~~~diff
- 004a1c24 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:30:8"]]
- 004a1c24 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a1c24 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:80:8"]]
+ 004a1c24 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a1c24 bytes 291940f9
+ 004a1c24 bytes 294140f9
- 004a1c60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
- 004a1c60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a1c60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:98:8"]]
+ 004a1c60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a1c60 bytes 082540f9
+ 004a1c60 bytes 084d40f9
~~~


<a id="compare-e5aebf2b6d6b403a5246f887dd414a07"></a>

### [`004a1d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1d20.md) → [`004a1d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1d20.md) _ZN5Botan25MessageAuthenticationCode15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbfe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbfe0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdc030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc030.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a1d98",
      "incomplete_value": false,
      "site": "004a1da0",
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
            "const:58a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a1d98",
      "incomplete_value": false,
      "site": "004a1da0",
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
            "const:4ff:8"
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
      "definition_site": "004a1dd8",
      "incomplete_value": true,
      "site": "004a1de4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a1dd8",
      "incomplete_value": true,
      "site": "004a1de4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe8:8"
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
      "004a1d98",
      "PARAM",
      [
        "storage",
        "0029c4ff",
        null,
        null
      ]
    ],
    [
      "004a1dd8",
      "READ",
      [
        "storage",
        "00c1afe8",
        null,
        "pointer"
      ]
    ],
    [
      "004a1dd8",
      "PARAM",
      [
        "storage",
        "00be93e8",
        "_ZTIN5Botan12Lookup_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a1d98",
      "PARAM",
      [
        "storage",
        "0029c58a",
        null,
        null
      ]
    ],
    [
      "004a1dd8",
      "READ",
      [
        "storage",
        "00c1b038",
        null,
        "pointer"
      ]
    ],
    [
      "004a1dd8",
      "PARAM",
      [
        "storage",
        "00be9438",
        "_ZTIN5Botan12Lookup_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1d20.md#insn-004a1d98) · [`004a1dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1d20.md#insn-004a1dcc) · [`004a1dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1d20.md#insn-004a1dd8)
- 新版 `004a1d98`（命令位置の公開資料なし） · `004a1dcc`（命令位置の公開資料なし） · `004a1dd8`（命令位置の公開資料なし）

~~~diff
- 004a1d98 ["COPY", "tmp:0:8", ["const:4ff:8"]]
- 004a1d98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a1d98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a1d98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a1d98 ["COPY", "tmp:0:8", ["const:58a:8"]]
+ 004a1d98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a1d98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a1d98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a1d98 bytes 21fc1391
+ 004a1d98 bytes 21281691
- 004a1dcc ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 004a1dcc ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 004a1dcc bytes c13b00b0
+ 004a1dcc bytes c13b00d0
- 004a1dd8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fe8:8"]]
- 004a1dd8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a1dd8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:38:8"]]
+ 004a1dd8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a1dd8 bytes 21f447f9
+ 004a1dd8 bytes 211c40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-339234e5b7062ae4062bdcfac61dc729"></a>

### [`004a1e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1e34.md) → [`004a1e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1e34.md) _ZN5Botan10MAC_FilterC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS_11OctetStringEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00499b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499b28.md) [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdbfe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbfe0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00499b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499b28.md) [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc030.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.98% / 新版 92.98%

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
      "definition_site": "004a1e74",
      "incomplete_value": true,
      "site": "004a1e7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a1e74",
      "incomplete_value": true,
      "site": "004a1e7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "004a1ea8",
      "incomplete_value": true,
      "site": "004a1eb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a1ea8",
      "incomplete_value": true,
      "site": "004a1eb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004a1e5c",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a1e7c",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a1e9c",
      "READ",
      [
        "storage",
        "00c1b048",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a1e5c",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a1e7c",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a1e9c",
      "READ",
      [
        "storage",
        "00c1b098",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1e34.md#insn-004a1e5c) · [`004a1e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a1/004a1e34.md#insn-004a1e78)
- 新版 `004a1e5c`（命令位置の公開資料なし） · `004a1e78`（命令位置の公開資料なし）

~~~diff
- 004a1e5c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:30:8"]]
- 004a1e5c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a1e5c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:80:8"]]
+ 004a1e5c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a1e5c bytes 291940f9
+ 004a1e5c bytes 294140f9
- 004a1e78 ["COPY", "register:40b8:8", ["register:4000:8"]]
- 004a1e78 bytes f70300aa
+ 004a1e78 ["COPY", "register:40b8:8", ["register:4000:8"]]
+ 004a1e78 bytes f70300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a21706777806da86b5fdee76f864512f"></a>

### [`004a20b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a20b4.md) → [`004a20b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a20b4.md) _ZN5Botan12Keyed_Filter6set_ivERKNS_11OctetStringE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdbef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbef0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbf40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a2168",
      "incomplete_value": true,
      "site": "004a2174",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a2168",
      "incomplete_value": true,
      "site": "004a2174",
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
      "004a2168",
      "READ",
      [
        "storage",
        "00c1b000",
        null,
        "pointer"
      ]
    ],
    [
      "004a2168",
      "PARAM",
      [
        "storage",
        "00be94a0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a2168",
      "READ",
      [
        "storage",
        "00c1b050",
        null,
        "pointer"
      ]
    ],
    [
      "004a2168",
      "PARAM",
      [
        "storage",
        "00be94f0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a2168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a20b4.md#insn-004a2168)
- 新版 `004a2168`（命令位置の公開資料なし）

~~~diff
- 004a2168 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 004a2168 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a2168 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:50:8"]]
+ 004a2168 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a2168 bytes 210040f9
+ 004a2168 bytes 212840f9
~~~


<a id="compare-1f47f013c9b707fc2953e6c0f15ae1b7"></a>

### [`004a21c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a21c8.md) → [`004a21c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a21c8.md) _ZN5Botan5ChainC2EPNS_6FilterES2_S2_S2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.12% / 新版 97.12%

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
      "definition_site": "004a2200",
      "incomplete_value": true,
      "site": "004a2204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2200",
      "incomplete_value": true,
      "site": "004a2204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2230",
      "incomplete_value": true,
      "site": "004a2234",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2230",
      "incomplete_value": true,
      "site": "004a2234",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004a21e8",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a2204",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a2224",
      "READ",
      [
        "storage",
        "00c1b050",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a21e8",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a2204",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a2224",
      "READ",
      [
        "storage",
        "00c1b0a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a21e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a21c8.md#insn-004a21e8) · [`004a2224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a21c8.md#insn-004a2224)
- 新版 `004a21e8`（命令位置の公開資料なし） · `004a2224`（命令位置の公開資料なし）

~~~diff
- 004a21e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 004a21e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a21e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 004a21e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a21e8 bytes 081940f9
+ 004a21e8 bytes 084140f9
- 004a2224 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:50:8"]]
- 004a2224 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a2224 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a0:8"]]
+ 004a2224 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a2224 bytes 082940f9
+ 004a2224 bytes 085140f9
~~~


<a id="compare-82e784cbcbf669268cec4f227a9b7470"></a>

### [`004a2390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a2390.md) → [`004a2390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2390.md) _ZN5Botan5ChainC1EPPNS_6FilterEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

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
      "definition_site": "004a23bc",
      "incomplete_value": true,
      "site": "004a23c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a23bc",
      "incomplete_value": true,
      "site": "004a23c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a23ec",
      "incomplete_value": true,
      "site": "004a23f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a23ec",
      "incomplete_value": true,
      "site": "004a23f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004a23ac",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a23c0",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a23e0",
      "READ",
      [
        "storage",
        "00c1b050",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a23ac",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a23c0",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a23e0",
      "READ",
      [
        "storage",
        "00c1b0a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a23ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a2390.md#insn-004a23ac) · [`004a23e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a2390.md#insn-004a23e0)
- 新版 `004a23ac`（命令位置の公開資料なし） · `004a23e0`（命令位置の公開資料なし）

~~~diff
- 004a23ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 004a23ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a23ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 004a23ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a23ac bytes 081940f9
+ 004a23ac bytes 084140f9
- 004a23e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:50:8"]]
- 004a23e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a23e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a0:8"]]
+ 004a23e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a23e0 bytes 082940f9
+ 004a23e0 bytes 085140f9
~~~


<a id="compare-eeebeecef20344600d111f9c127f1b9f"></a>

### [`004a24b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a24b0.md) → [`004a24b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a24b0.md) _ZN5Botan4ForkC1EPNS_6FilterES2_S2_S2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md) [`00520ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520ec4.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00520ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520ec4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

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
      "definition_site": "004a24f8",
      "incomplete_value": true,
      "site": "004a2500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a24f8",
      "incomplete_value": true,
      "site": "004a2500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2530",
      "incomplete_value": true,
      "site": "004a2538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2530",
      "incomplete_value": true,
      "site": "004a2538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004a24dc",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a2500",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a2524",
      "READ",
      [
        "storage",
        "00c1b058",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a24dc",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a2500",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a2524",
      "READ",
      [
        "storage",
        "00c1b0a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a24dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a24b0.md#insn-004a24dc) · [`004a24fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a24b0.md#insn-004a24fc)
- 新版 `004a24dc`（命令位置の公開資料なし） · `004a24fc`（命令位置の公開資料なし）

~~~diff
- 004a24dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:30:8"]]
- 004a24dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a24dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:80:8"]]
+ 004a24dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a24dc bytes 291940f9
+ 004a24dc bytes 294140f9
- 004a24fc ["COPY", "register:40c0:8", ["register:4000:8"]]
- 004a24fc bytes f80300aa
+ 004a24fc ["COPY", "register:40c0:8", ["register:4000:8"]]
+ 004a24fc bytes f80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9569ea7d65e200ebfe3e8f0a7f1714ef"></a>

### [`004a2608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a2608.md) → [`004a2608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2608.md) _ZN5Botan4ForkC2EPPNS_6FilterEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md) [`00520ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520ec4.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00520ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520ec4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

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
      "definition_site": "004a2634",
      "incomplete_value": true,
      "site": "004a2638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2634",
      "incomplete_value": true,
      "site": "004a2638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2668",
      "incomplete_value": true,
      "site": "004a2670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2668",
      "incomplete_value": true,
      "site": "004a2670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004a2624",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a2638",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a2658",
      "READ",
      [
        "storage",
        "00c1b058",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a2624",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a2638",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a2658",
      "READ",
      [
        "storage",
        "00c1b0a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a2624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a2608.md#insn-004a2624) · [`004a2658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a2608.md#insn-004a2658)
- 新版 `004a2624`（命令位置の公開資料なし） · `004a2658`（命令位置の公開資料なし）

~~~diff
- 004a2624 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 004a2624 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a2624 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 004a2624 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a2624 bytes 081940f9
+ 004a2624 bytes 084140f9
- 004a2658 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:58:8"]]
- 004a2658 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a2658 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a8:8"]]
+ 004a2658 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a2658 bytes 082d40f9
+ 004a2658 bytes 085540f9
~~~


<a id="compare-862d7308b8f80afc34881545033a18d9"></a>

### [`004a2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a2710.md) → [`004a2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2710.md) _ZN5Botan15Buffered_FilterC2Emm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc000.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdc050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc050.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.36% / 新版 91.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a2744",
      "incomplete_value": true,
      "site": "004a2744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2744",
      "incomplete_value": true,
      "site": "004a2744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a27b0",
      "incomplete_value": false,
      "site": "004a27b8",
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
            "const:787:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a27b0",
      "incomplete_value": false,
      "site": "004a27b8",
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
            "const:814:8"
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
      "definition_site": "004a27e8",
      "incomplete_value": true,
      "site": "004a27f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a27e8",
      "incomplete_value": true,
      "site": "004a27f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a2738",
      "READ",
      [
        "storage",
        "00c1b060",
        null,
        "pointer"
      ]
    ],
    [
      "004a2744",
      "DATA",
      [
        "storage",
        "00be9898",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004a27b0",
      "PARAM",
      [
        "storage",
        "00294814",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004a2738",
      "READ",
      [
        "storage",
        "00c1b0b0",
        null,
        "pointer"
      ]
    ],
    [
      "004a2744",
      "DATA",
      [
        "storage",
        "00be98e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004a27b0",
      "PARAM",
      [
        "storage",
        "00294787",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a2738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a2710.md#insn-004a2738) · [`004a27b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a2710.md#insn-004a27b0) · [`004a27e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a2710.md#insn-004a27e8)
- 新版 `004a2738`（命令位置の公開資料なし） · `004a27b0`（命令位置の公開資料なし） · `004a27e8`（命令位置の公開資料なし）

~~~diff
- 004a2738 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:60:8"]]
- 004a2738 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a2738 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b0:8"]]
+ 004a2738 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a2738 bytes 293140f9
+ 004a2738 bytes 295940f9
- 004a27b0 ["COPY", "tmp:0:8", ["const:814:8"]]
- 004a27b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a27b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a27b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a27b0 ["COPY", "tmp:0:8", ["const:787:8"]]
+ 004a27b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a27b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a27b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a27b0 bytes 21502091
+ 004a27b0 bytes 211c1e91
- 004a27e8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 004a27e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a27e8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004a27e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a27e8 bytes 217847f9
+ 004a27e8 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cdf76f14eccb1be7ac2afd2b4738d3d"></a>

### [`004a29fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a29fc.md) → [`004a29fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a29fc.md) _ZN5Botan15Buffered_Filter7end_msgEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc020.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdc070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc070.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.10% / 新版 97.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a2ac4",
      "incomplete_value": false,
      "site": "004a2acc",
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
            "const:876:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a2ac4",
      "incomplete_value": false,
      "site": "004a2acc",
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
            "const:903:8"
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
      "definition_site": "004a2afc",
      "incomplete_value": true,
      "site": "004a2b08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a2afc",
      "incomplete_value": true,
      "site": "004a2b08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a2ac4",
      "PARAM",
      [
        "storage",
        "00293903",
        null,
        "string"
      ]
    ],
    [
      "004a2afc",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004a2afc",
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
      "004a2ac4",
      "PARAM",
      [
        "storage",
        "00293876",
        null,
        "string"
      ]
    ],
    [
      "004a2afc",
      "READ",
      [
        "storage",
        "00c1af98",
        null,
        "pointer"
      ]
    ],
    [
      "004a2afc",
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

- 旧版 [`004a2ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a29fc.md#insn-004a2ac4) · [`004a2afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a29fc.md#insn-004a2afc)
- 新版 `004a2ac4`（命令位置の公開資料なし） · `004a2afc`（命令位置の公開資料なし）

~~~diff
- 004a2ac4 ["COPY", "tmp:0:8", ["const:903:8"]]
- 004a2ac4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a2ac4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a2ac4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a2ac4 ["COPY", "tmp:0:8", ["const:876:8"]]
+ 004a2ac4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a2ac4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a2ac4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a2ac4 bytes 210c2491
+ 004a2ac4 bytes 21d82191
- 004a2afc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f48:8"]]
- 004a2afc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a2afc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f98:8"]]
+ 004a2afc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a2afc bytes 21a447f9
+ 004a2afc bytes 21cc47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdd9436144da8aa1ae52e74efe5a3b58"></a>

### [`004a2b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a2b58.md) → [`004a2b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2b58.md) _ZN5Botan18Cipher_Mode_FilterC1EPNS_11Cipher_ModeE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc0f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc0f0.md) · 呼出先 7件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)
- 新版 呼出元 1件 [`00bdc140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc140.md) · 呼出先 7件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a2b80",
      "incomplete_value": true,
      "site": "004a2b84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2b80",
      "incomplete_value": true,
      "site": "004a2b84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2bb0",
      "incomplete_value": true,
      "site": "004a2bb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2bb0",
      "incomplete_value": true,
      "site": "004a2bb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "004a2c24",
      "incomplete_value": true,
      "site": "004a2c2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2c24",
      "incomplete_value": true,
      "site": "004a2c2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004a2b74",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a2b84",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a2ba4",
      "READ",
      [
        "storage",
        "00c1b068",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a2b74",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a2b84",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a2ba4",
      "READ",
      [
        "storage",
        "00c1b0b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a2b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a2b58.md#insn-004a2b74) · [`004a2b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a2b58.md#insn-004a2b78)
- 新版 `004a2b74`（命令位置の公開資料なし） · `004a2b78`（命令位置の公開資料なし）

~~~diff
- 004a2b74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 004a2b74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a2b74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 004a2b74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a2b74 bytes 081940f9
+ 004a2b74 bytes 084140f9
- 004a2b78 ["COPY", "register:4098:8", ["register:4000:8"]]
- 004a2b78 bytes f30300aa
+ 004a2b78 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 004a2b78 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1113b5866b003f15568fd91654249c72"></a>

### [`004a2f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a2f20.md) → [`004a2f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2f20.md) _ZN5Botan18Cipher_Mode_Filter9start_msgEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.39% / 新版 96.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a2fd8",
      "incomplete_value": false,
      "site": "004a2fe4",
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
            "const:79f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a2fd8",
      "incomplete_value": false,
      "site": "004a2fe4",
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
            "const:705:8"
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
      "definition_site": "004a3004",
      "incomplete_value": false,
      "site": "004a300c",
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
            "const:553:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a3004",
      "incomplete_value": false,
      "site": "004a300c",
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
            "const:4c8:8"
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
      "definition_site": "004a3058",
      "incomplete_value": true,
      "site": "004a3064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a3058",
      "incomplete_value": true,
      "site": "004a3064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a2fd8",
      "PARAM",
      [
        "storage",
        "002a6705",
        null,
        "string"
      ]
    ],
    [
      "004a3004",
      "PARAM",
      [
        "storage",
        "0029c4c8",
        null,
        "string"
      ]
    ],
    [
      "004a3058",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a2fd8",
      "PARAM",
      [
        "storage",
        "002a679f",
        null,
        "string"
      ]
    ],
    [
      "004a3004",
      "PARAM",
      [
        "storage",
        "0029c553",
        null,
        "string"
      ]
    ],
    [
      "004a3058",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a2fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a2f20.md#insn-004a2fd8) · [`004a3004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a2f20.md#insn-004a3004) · [`004a3058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a2f20.md#insn-004a3058)
- 新版 `004a2fd8`（命令位置の公開資料なし） · `004a3004`（命令位置の公開資料なし） · `004a3058`（命令位置の公開資料なし）

~~~diff
- 004a2fd8 ["COPY", "tmp:0:8", ["const:705:8"]]
- 004a2fd8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004a2fd8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004a2fd8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004a2fd8 ["COPY", "tmp:0:8", ["const:79f:8"]]
+ 004a2fd8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004a2fd8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004a2fd8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004a2fd8 bytes 42141c91
+ 004a2fd8 bytes 427c1e91
- 004a3004 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 004a3004 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a3004 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a3004 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a3004 ["COPY", "tmp:0:8", ["const:553:8"]]
+ 004a3004 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a3004 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a3004 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a3004 bytes 21201391
+ 004a3004 bytes 214c1591
- 004a3058 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 004a3058 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a3058 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 004a3058 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a3058 bytes 218447f9
+ 004a3058 bytes 21ac47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29e2cd7d857dfa6ff7d815dfa982f0a9"></a>

### [`004a32dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a32dc.md) → [`004a32dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a32dc.md) _ZN5Botan15DataSink_Stream5writeEPKhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a3358",
      "incomplete_value": false,
      "site": "004a3364",
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
            "const:7a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a3358",
      "incomplete_value": false,
      "site": "004a3364",
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
            "const:70d:8"
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
      "definition_site": "004a3398",
      "incomplete_value": true,
      "site": "004a33a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a3398",
      "incomplete_value": true,
      "site": "004a33a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a3358",
      "PARAM",
      [
        "storage",
        "002a670d",
        null,
        "string"
      ]
    ],
    [
      "004a3398",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "004a3398",
      "PARAM",
      [
        "storage",
        "00be9250",
        "_ZTIN5Botan15Stream_IO_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a3358",
      "PARAM",
      [
        "storage",
        "002a67a7",
        null,
        "string"
      ]
    ],
    [
      "004a3398",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "004a3398",
      "PARAM",
      [
        "storage",
        "00be92a0",
        "_ZTIN5Botan15Stream_IO_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a3358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a32dc.md#insn-004a3358) · [`004a3398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a32dc.md#insn-004a3398)
- 新版 `004a3358`（命令位置の公開資料なし） · `004a3398`（命令位置の公開資料なし）

~~~diff
- 004a3358 ["COPY", "tmp:0:8", ["const:70d:8"]]
- 004a3358 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004a3358 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004a3358 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004a3358 ["COPY", "tmp:0:8", ["const:7a7:8"]]
+ 004a3358 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004a3358 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004a3358 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004a3358 bytes 00341c91
+ 004a3358 bytes 009c1e91
- 004a3398 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
- 004a3398 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a3398 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f90:8"]]
+ 004a3398 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a3398 bytes 21a047f9
+ 004a3398 bytes 21c847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-098528c8f3c1ca63758c7becf0991231"></a>

### [`004a3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a3400.md) → [`004a3400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3400.md) _ZN5Botan15DataSink_StreamC2ERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEERKNS1_12basic_stringIcS4_NS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "004a342c",
      "incomplete_value": true,
      "site": "004a3430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a342c",
      "incomplete_value": true,
      "site": "004a3430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a345c",
      "incomplete_value": true,
      "site": "004a3460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a345c",
      "incomplete_value": true,
      "site": "004a3460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004a341c",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a3430",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a3450",
      "READ",
      [
        "storage",
        "00c1b078",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a341c",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a3430",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a3450",
      "READ",
      [
        "storage",
        "00c1b0c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a341c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a3400.md#insn-004a341c) · [`004a3450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a3400.md#insn-004a3450)
- 新版 `004a341c`（命令位置の公開資料なし） · `004a3450`（命令位置の公開資料なし）

~~~diff
- 004a341c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 004a341c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a341c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 004a341c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a341c bytes 081940f9
+ 004a341c bytes 084140f9
- 004a3450 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:78:8"]]
- 004a3450 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a3450 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c8:8"]]
+ 004a3450 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a3450 bytes 083d40f9
+ 004a3450 bytes 086540f9
~~~


<a id="compare-a33c29d9fb2e69facc85327a943e9a51"></a>

### [`004a34dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a34dc.md) → [`004a34dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a34dc.md) _ZN5Botan15DataSink_StreamC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004a36fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a36fc.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004a36fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a36fc.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.38% / 新版 94.38%

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
      "definition_site": "004a3518",
      "incomplete_value": true,
      "site": "004a3520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a3518",
      "incomplete_value": true,
      "site": "004a3520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a354c",
      "incomplete_value": true,
      "site": "004a3550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a354c",
      "incomplete_value": true,
      "site": "004a3550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a35f0",
      "incomplete_value": false,
      "site": "004a35fc",
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
            "const:542:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a35f0",
      "incomplete_value": false,
      "site": "004a35fc",
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
            "const:4b7:8"
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
      "004a3504",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a3520",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a3540",
      "READ",
      [
        "storage",
        "00c1b078",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a3504",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a3520",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a3540",
      "READ",
      [
        "storage",
        "00c1b0c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a3504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a34dc.md#insn-004a3504) · [`004a3540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a34dc.md#insn-004a3540) · [`004a35f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a34dc.md#insn-004a35f0)
- 新版 `004a3504`（命令位置の公開資料なし） · `004a3540`（命令位置の公開資料なし） · `004a35f0`（命令位置の公開資料なし）

~~~diff
- 004a3504 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:30:8"]]
- 004a3504 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a3504 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:80:8"]]
+ 004a3504 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a3504 bytes 291940f9
+ 004a3504 bytes 294140f9
- 004a3540 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:78:8"]]
- 004a3540 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a3540 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c8:8"]]
+ 004a3540 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a3540 bytes 083d40f9
+ 004a3540 bytes 086540f9
- 004a35f0 ["COPY", "tmp:0:8", ["const:4b7:8"]]
- 004a35f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004a35f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004a35f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004a35f0 ["COPY", "tmp:0:8", ["const:542:8"]]
+ 004a35f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004a35f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004a35f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004a35f0 bytes 00dc1291
+ 004a35f0 bytes 00081591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3af21456ce1daaa86cab28b90e115ad"></a>

### [`004a36fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a36fc.md) → [`004a36fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a36fc.md) FUN_004a36fc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004a34dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a34dc.md) · 呼出先 4件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdc060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc060.md) [`00bdc070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc070.md)
- 新版 呼出元 1件 [`004a34dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a34dc.md) · 呼出先 4件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdc0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0b0.md) [`00bdc0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0c0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 85.45% / 新版 85.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a3740",
      "incomplete_value": true,
      "site": "004a3740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004a3740",
      "incomplete_value": true,
      "site": "004a3740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a3738",
      "incomplete_value": true,
      "site": "004a3744",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a3738",
      "incomplete_value": true,
      "site": "004a3744",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
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
      "definition_site": "004a374c",
      "incomplete_value": true,
      "site": "004a374c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
      "definition_site": "004a374c",
      "incomplete_value": true,
      "site": "004a374c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
      "004a3720",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a3724",
      "READ",
      [
        "storage",
        "00c1b088",
        null,
        "pointer"
      ]
    ],
    [
      "004a3738",
      "READ",
      [
        "storage",
        "00c132d8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004a3720",
      "READ",
      [
        "storage",
        "00c1b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "004a3724",
      "READ",
      [
        "storage",
        "00c1b0d8",
        null,
        "pointer"
      ]
    ],
    [
      "004a3738",
      "READ",
      [
        "storage",
        "00c13328",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a3720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a36fc.md#insn-004a3720) · [`004a3724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a36fc.md#insn-004a3724)
- 新版 `004a3720`（命令位置の公開資料なし） · `004a3724`（命令位置の公開資料なし）

~~~diff
- 004a3720 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:80:8"]]
- 004a3720 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a3720 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:d0:8"]]
+ 004a3720 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 004a3720 bytes 394340f9
+ 004a3720 bytes 396b40f9
- 004a3724 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:88:8"]]
- 004a3724 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a3724 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:d8:8"]]
+ 004a3724 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 004a3724 bytes 184740f9
+ 004a3724 bytes 186f40f9
~~~


<a id="compare-9b23ad65bb37dcabac8c2e756101b2eb"></a>

### [`004a3b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a3b2c.md) → [`004a3b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3b2c.md) _ZN5Botan6Filter8set_portEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a3b98",
      "incomplete_value": false,
      "site": "004a3ba0",
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
            "const:a19:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a3b98",
      "incomplete_value": false,
      "site": "004a3ba0",
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
            "const:aad:8"
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
      "definition_site": "004a3bd4",
      "incomplete_value": true,
      "site": "004a3be0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a3bd4",
      "incomplete_value": true,
      "site": "004a3be0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a3b98",
      "PARAM",
      [
        "storage",
        "002afaad",
        null,
        "string"
      ]
    ],
    [
      "004a3bd4",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004a3bd4",
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
      "004a3b98",
      "PARAM",
      [
        "storage",
        "002afa19",
        null,
        "string"
      ]
    ],
    [
      "004a3bd4",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "004a3bd4",
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

- 旧版 [`004a3b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a3b2c.md#insn-004a3b98) · [`004a3bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a3b2c.md#insn-004a3bd4)
- 新版 `004a3b98`（命令位置の公開資料なし） · `004a3bd4`（命令位置の公開資料なし）

~~~diff
- 004a3b98 ["COPY", "tmp:0:8", ["const:aad:8"]]
- 004a3b98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a3b98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a3b98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a3b98 ["COPY", "tmp:0:8", ["const:a19:8"]]
+ 004a3b98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a3b98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a3b98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a3b98 bytes 21b42a91
+ 004a3b98 bytes 21642891
- 004a3bd4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 004a3bd4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a3bd4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004a3bd4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a3bd4 bytes 217847f9
+ 004a3bd4 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a78e141b78ab492cf547e959e6146d7c"></a>

### [`004a3c6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a3c6c.md) → [`004a3c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3c6c.md) _ZN5Botan10get_cipherERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS_10Cipher_DirE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc0d0.md) · 呼出先 8件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdc120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc120.md) · 呼出先 8件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.78% / 新版 97.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a3d10",
      "incomplete_value": true,
      "site": "004a3d18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a3d10",
      "incomplete_value": true,
      "site": "004a3d18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:90:8"
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
      "004a3d10",
      "READ",
      [
        "storage",
        "00c1b090",
        null,
        "pointer"
      ]
    ],
    [
      "004a3d10",
      "PARAM",
      [
        "storage",
        "00be9a08",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a3d10",
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ],
    [
      "004a3d10",
      "PARAM",
      [
        "storage",
        "00be9a58",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a3d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a3c6c.md#insn-004a3d10)
- 新版 `004a3d10`（命令位置の公開資料なし）

~~~diff
- 004a3d10 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:90:8"]]
- 004a3d10 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a3d10 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e0:8"]]
+ 004a3d10 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a3d10 bytes 214840f9
+ 004a3d10 bytes 217040f9
~~~


<a id="compare-330e9a70abe124670a9a4f989afaaf48"></a>

### [`004a3d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a3d70.md) → [`004a3d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3d70.md) _ZN5Botan15get_cipher_modeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS_10Cipher_DirES8_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc0e0.md) · 呼出先 27件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`004aec4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ae/004aec4c.md) [`004aece4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ae/004aece4.md) [`00524c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c94.md)
- 新版 呼出元 1件 [`00bdc130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc130.md) · 呼出先 27件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`004aec4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004aec4c.md) [`004aece4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004aece4.md) [`00524c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c94.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.00% / 新版 97.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a3dd0",
      "incomplete_value": true,
      "site": "004a3dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a3dd0",
      "incomplete_value": true,
      "site": "004a3dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004a3e2c",
      "incomplete_value": false,
      "site": "004a3e38",
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
      "definition_site": "004a3e2c",
      "incomplete_value": false,
      "site": "004a3e38",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a3efc",
      "incomplete_value": true,
      "site": "004a3f00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004a3efc",
      "incomplete_value": true,
      "site": "004a3f00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "004a3dc8",
      "READ",
      [
        "storage",
        "00c1b098",
        null,
        "pointer"
      ]
    ],
    [
      "004a3dd0",
      "DATA",
      [
        "storage",
        "00becd50",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004a3e38",
      "DATA",
      [
        "storage",
        "00bed6a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004a3dc8",
      "READ",
      [
        "storage",
        "00c1b0e8",
        null,
        "pointer"
      ]
    ],
    [
      "004a3dd0",
      "DATA",
      [
        "storage",
        "00becda0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004a3e38",
      "DATA",
      [
        "storage",
        "00bed6f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a3dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a3d70.md#insn-004a3dc8) · [`004a3e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a3d70.md#insn-004a3e2c) · [`004a3eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a3d70.md#insn-004a3eec)
- 新版 `004a3dc8`（命令位置の公開資料なし） · `004a3e2c`（命令位置の公開資料なし） · `004a3eec`（命令位置の公開資料なし）

~~~diff
- 004a3dc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:98:8"]]
- 004a3dc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a3dc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e8:8"]]
+ 004a3dc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a3dc8 bytes 084d40f9
+ 004a3dc8 bytes 087540f9
- 004a3e2c ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 004a3e2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004a3e2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004a3e2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004a3e2c ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 004a3e2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004a3e2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004a3e2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004a3e2c bytes 08811a91
+ 004a3e2c bytes 08c11b91
- 004a3eec ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:e48:8"]]
- 004a3eec ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a3eec ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:e98:8"]]
+ 004a3eec ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 004a3eec bytes 5a2747f9
+ 004a3eec bytes 5a4f47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc51d8dd3a3d89af84f6a25ed1eaa3ae"></a>

### [`004a4974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a4/004a4974.md) → [`004a4974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4974.md) _ZN5Botan11SecureQueue4readEPhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc150.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00bdc1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1a0.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a4a48",
      "incomplete_value": true,
      "site": "004a4a48",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004a4a48",
      "incomplete_value": true,
      "site": "004a4a48",
      "value": [
        "LOAD",
        "8",
        [
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
      "004a4a38",
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
      "004a4a38",
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

- 旧版 [`004a4a38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a4/004a4974.md#insn-004a4a38)
- 新版 `004a4a38`（命令位置の公開資料なし）

~~~diff
- 004a4a38 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:728:8"]]
- 004a4a38 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a4a38 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:778:8"]]
+ 004a4a38 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a4a38 bytes 499743f9
+ 004a4a38 bytes 49bf43f9
~~~


<a id="compare-8771470b7346e313f075a12231dc0200"></a>

### [`004a4bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a4/004a4bf0.md) → [`004a4bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4bf0.md) FUN_004a4bf0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004a5d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5d40.md) · 呼出先 3件 [`00520ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520ff4.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 1件 [`004a5d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5d40.md) · 呼出先 3件 [`00520ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520ff4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.03% / 新版 91.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a4cc8",
      "incomplete_value": false,
      "site": "004a4ce8",
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
            "const:c02:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a4cc8",
      "incomplete_value": false,
      "site": "004a4ce8",
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
            "const:c8f:8"
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
      "definition_site": "004a4cd0",
      "incomplete_value": false,
      "site": "004a4ce8",
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
            "const:c08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a4cd0",
      "incomplete_value": false,
      "site": "004a4ce8",
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
            "const:c95:8"
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
      "definition_site": "004a4cd8",
      "incomplete_value": false,
      "site": "004a4ce8",
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
            "const:9cb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a4cd8",
      "incomplete_value": false,
      "site": "004a4ce8",
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
            "const:a58:8"
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
      "004a4cc8",
      "PARAM",
      [
        "storage",
        "00299c8f",
        null,
        "string"
      ]
    ],
    [
      "004a4cd0",
      "PARAM",
      [
        "storage",
        "00299c95",
        null,
        "string"
      ]
    ],
    [
      "004a4cd8",
      "PARAM",
      [
        "storage",
        "00296a58",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004a4cc8",
      "PARAM",
      [
        "storage",
        "00299c02",
        null,
        "string"
      ]
    ],
    [
      "004a4cd0",
      "PARAM",
      [
        "storage",
        "00299c08",
        null,
        "string"
      ]
    ],
    [
      "004a4cd8",
      "PARAM",
      [
        "storage",
        "002969cb",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a4cc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a4/004a4bf0.md#insn-004a4cc8) · [`004a4cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a4/004a4bf0.md#insn-004a4cd0) · [`004a4cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a4/004a4bf0.md#insn-004a4cd8)
- 新版 `004a4cc8`（命令位置の公開資料なし） · `004a4cd0`（命令位置の公開資料なし） · `004a4cd8`（命令位置の公開資料なし）

~~~diff
- 004a4cc8 ["COPY", "tmp:0:8", ["const:c8f:8"]]
- 004a4cc8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004a4cc8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004a4cc8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004a4cc8 ["COPY", "tmp:0:8", ["const:c02:8"]]
+ 004a4cc8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004a4cc8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004a4cc8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004a4cc8 bytes 003c3291
+ 004a4cc8 bytes 00083091
- 004a4cd0 ["COPY", "tmp:0:8", ["const:c95:8"]]
- 004a4cd0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a4cd0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a4cd0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a4cd0 ["COPY", "tmp:0:8", ["const:c08:8"]]
+ 004a4cd0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a4cd0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a4cd0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a4cd0 bytes 21543291
+ 004a4cd0 bytes 21203091
- 004a4cd8 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 004a4cd8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004a4cd8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004a4cd8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004a4cd8 ["COPY", "tmp:0:8", ["const:9cb:8"]]
+ 004a4cd8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004a4cd8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004a4cd8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004a4cd8 bytes 42602991
+ 004a4cd8 bytes 422c2791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33da469d1e7dbe00073c0aa4add3a261"></a>

### [`004a4ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a4/004a4ea0.md) → [`004a4ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4ea0.md) _ZN5Botan4PipeC2EPNS_6FilterES2_S2_S2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdc170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc170.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdc1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a4ed4",
      "incomplete_value": true,
      "site": "004a4edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a4ed4",
      "incomplete_value": true,
      "site": "004a4edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004a4ec0",
      "READ",
      [
        "storage",
        "00c1b0c0",
        null,
        "pointer"
      ]
    ],
    [
      "004a4edc",
      "DATA",
      [
        "storage",
        "00be9a30",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004a4ec0",
      "READ",
      [
        "storage",
        "00c1b110",
        null,
        "pointer"
      ]
    ],
    [
      "004a4edc",
      "DATA",
      [
        "storage",
        "00be9a80",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a4ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a4/004a4ea0.md#insn-004a4ec0)
- 新版 `004a4ec0`（命令位置の公開資料なし）

~~~diff
- 004a4ec0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c0:8"]]
- 004a4ec0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a4ec0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:110:8"]]
+ 004a4ec0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a4ec0 bytes 086140f9
+ 004a4ec0 bytes 088940f9
~~~


<a id="compare-e48ad16b88388a31f999404213e2b968"></a>

### [`004a4f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a4/004a4f60.md) → [`004a4f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4f60.md) _ZN5Botan4PipeC2ESt16initializer_listIPNS_6FilterEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdc170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc170.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdc1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a4f8c",
      "incomplete_value": true,
      "site": "004a4f90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a4f8c",
      "incomplete_value": true,
      "site": "004a4f90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004a4f7c",
      "READ",
      [
        "storage",
        "00c1b0c0",
        null,
        "pointer"
      ]
    ],
    [
      "004a4f90",
      "DATA",
      [
        "storage",
        "00be9a30",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004a4f7c",
      "READ",
      [
        "storage",
        "00c1b110",
        null,
        "pointer"
      ]
    ],
    [
      "004a4f90",
      "DATA",
      [
        "storage",
        "00be9a80",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a4f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a4/004a4f60.md#insn-004a4f7c)
- 新版 `004a4f7c`（命令位置の公開資料なし）

~~~diff
- 004a4f7c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c0:8"]]
- 004a4f7c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a4f7c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:110:8"]]
+ 004a4f7c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a4f7c bytes 086140f9
+ 004a4f7c bytes 088940f9
~~~


<a id="compare-020e9f40175de3359ce1d1e787204378"></a>

### [`004a5000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5000.md) → [`004a5000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5000.md) _ZN5Botan4Pipe9do_appendEPNS_6FilterE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc170.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdc1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1c0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 94.96% / 新版 94.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004a5034",
      "incomplete_value": true,
      "site": "004a5038",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "004a5034",
      "incomplete_value": true,
      "site": "004a5038",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "004a50cc",
      "incomplete_value": false,
      "site": "004a50d4",
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
            "const:39f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a50cc",
      "incomplete_value": false,
      "site": "004a50d4",
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
            "const:314:8"
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
      "definition_site": "004a5108",
      "incomplete_value": true,
      "site": "004a5114",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a5108",
      "incomplete_value": true,
      "site": "004a5114",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a5028",
      "READ",
      [
        "storage",
        "00c1b0c8",
        null,
        "pointer"
      ]
    ],
    [
      "004a50cc",
      "PARAM",
      [
        "storage",
        "002a2314",
        null,
        "string"
      ]
    ],
    [
      "004a5108",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a5028",
      "READ",
      [
        "storage",
        "00c1b118",
        null,
        "pointer"
      ]
    ],
    [
      "004a50cc",
      "PARAM",
      [
        "storage",
        "002a239f",
        null,
        "string"
      ]
    ],
    [
      "004a5108",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a5028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5000.md#insn-004a5028) · [`004a50cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5000.md#insn-004a50cc) · [`004a5108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5000.md#insn-004a5108)
- 新版 `004a5028`（命令位置の公開資料なし） · `004a50cc`（命令位置の公開資料なし） · `004a5108`（命令位置の公開資料なし）

~~~diff
- 004a5028 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c8:8"]]
- 004a5028 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5028 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:118:8"]]
+ 004a5028 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a5028 bytes 296540f9
+ 004a5028 bytes 298d40f9
- 004a50cc ["COPY", "tmp:0:8", ["const:314:8"]]
- 004a50cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a50cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a50cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a50cc ["COPY", "tmp:0:8", ["const:39f:8"]]
+ 004a50cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a50cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a50cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a50cc bytes 21500c91
+ 004a50cc bytes 217c0e91
- 004a5108 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 004a5108 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5108 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004a5108 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a5108 bytes 217847f9
+ 004a5108 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab17a5dec60bc34a24d1755e2719bee9"></a>

### [`004a52c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a52c0.md) → [`004a52c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a52c0.md) _ZN5Botan4Pipe8destructEPNS_6FilterE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc180.md) · 呼出先 1件 [`00bdc180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc180.md)
- 新版 呼出元 1件 [`00bdc1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1d0.md) · 呼出先 1件 [`00bdc1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1d0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004a52e8",
      "incomplete_value": true,
      "site": "004a52ec",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "004a52e8",
      "incomplete_value": true,
      "site": "004a52ec",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004a52dc",
      "READ",
      [
        "storage",
        "00c1b0c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a52dc",
      "READ",
      [
        "storage",
        "00c1b118",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a52dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a52c0.md#insn-004a52dc)
- 新版 `004a52dc`（命令位置の公開資料なし）

~~~diff
- 004a52dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c8:8"]]
- 004a52dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a52dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:118:8"]]
+ 004a52dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a52dc bytes 086540f9
+ 004a52dc bytes 088d40f9
~~~


<a id="compare-7c57ee47541836790174591a4c6f9294"></a>

### [`004a53c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a53c0.md) → [`004a53c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a53c0.md) _ZNK5Botan4Pipe9remainingEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc1a0.md) · 呼出先 5件 [`004a6834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6834.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdc1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1f0.md) · 呼出先 5件 [`004a6834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6834.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a53f4",
      "incomplete_value": true,
      "site": "004a53f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a53f4",
      "incomplete_value": true,
      "site": "004a53f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:428:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a54e8",
      "incomplete_value": true,
      "site": "004a54f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:120:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a54e8",
      "incomplete_value": true,
      "site": "004a54f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d0:8"
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
      "004a53e0",
      "READ",
      [
        "storage",
        "002a4428",
        null,
        "string"
      ]
    ],
    [
      "004a54e8",
      "READ",
      [
        "storage",
        "00c1b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "004a54e8",
      "PARAM",
      [
        "storage",
        "00be9b88",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a53e0",
      "READ",
      [
        "storage",
        "002a44b3",
        null,
        "string"
      ]
    ],
    [
      "004a54e8",
      "READ",
      [
        "storage",
        "00c1b120",
        null,
        "pointer"
      ]
    ],
    [
      "004a54e8",
      "PARAM",
      [
        "storage",
        "00be9bd8",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a53d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a53c0.md#insn-004a53d8) · [`004a54e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a53c0.md#insn-004a54e8)
- 新版 `004a53d8`（命令位置の公開資料なし） · `004a54e8`（命令位置の公開資料なし）

~~~diff
- 004a53d8 ["COPY", "tmp:0:8", ["const:428:8"]]
- 004a53d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004a53d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004a53d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004a53d8 ["COPY", "tmp:0:8", ["const:4b3:8"]]
+ 004a53d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004a53d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004a53d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004a53d8 bytes 4aa11091
+ 004a53d8 bytes 4acd1291
- 004a54e8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d0:8"]]
- 004a54e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a54e8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:120:8"]]
+ 004a54e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a54e8 bytes 216840f9
+ 004a54e8 bytes 219040f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1f4934854e7bfeb8674815609776577"></a>

### [`004a5538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5538.md) → [`004a5538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5538.md) _ZN5Botan4Pipe15set_default_msgEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a55a8",
      "incomplete_value": false,
      "site": "004a55b0",
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
            "const:546:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a55a8",
      "incomplete_value": false,
      "site": "004a55b0",
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
            "const:4bb:8"
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
      "definition_site": "004a55e4",
      "incomplete_value": true,
      "site": "004a55f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a55e4",
      "incomplete_value": true,
      "site": "004a55f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a55a8",
      "PARAM",
      [
        "storage",
        "002a14bb",
        null,
        "string"
      ]
    ],
    [
      "004a55e4",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004a55e4",
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
      "004a55a8",
      "PARAM",
      [
        "storage",
        "002a1546",
        null,
        "string"
      ]
    ],
    [
      "004a55e4",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "004a55e4",
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

- 旧版 [`004a55a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5538.md#insn-004a55a8) · [`004a55e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5538.md#insn-004a55e4)
- 新版 `004a55a8`（命令位置の公開資料なし） · `004a55e4`（命令位置の公開資料なし）

~~~diff
- 004a55a8 ["COPY", "tmp:0:8", ["const:4bb:8"]]
- 004a55a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a55a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a55a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a55a8 ["COPY", "tmp:0:8", ["const:546:8"]]
+ 004a55a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a55a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a55a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a55a8 bytes 21ec1291
+ 004a55a8 bytes 21181591
- 004a55e4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 004a55e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a55e4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004a55e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a55e4 bytes 217847f9
+ 004a55e4 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-637d2772ba0b14458b4cae574fa5b045"></a>

### [`004a5698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5698.md) → [`004a5698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5698.md) _ZN5Botan4Pipe9start_msgEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc1b0.md) · 呼出先 10件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00bdc200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc200.md) · 呼出先 10件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.33% / 新版 89.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a56ec",
      "incomplete_value": true,
      "site": "004a56f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a56ec",
      "incomplete_value": true,
      "site": "004a56f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004a5710",
      "incomplete_value": false,
      "site": "004a571c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a5710",
      "incomplete_value": false,
      "site": "004a571c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:b48:8"
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
      "definition_site": "004a5778",
      "incomplete_value": false,
      "site": "004a5780",
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
            "const:ab7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a5778",
      "incomplete_value": false,
      "site": "004a5780",
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
            "const:b44:8"
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
      "004a56e4",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a56f0",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a571c",
      "DATA",
      [
        "storage",
        "00be9b48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004a56e4",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a56f0",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a571c",
      "DATA",
      [
        "storage",
        "00be9b98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a56e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5698.md#insn-004a56e4) · [`004a56e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5698.md#insn-004a56e8)
- 新版 `004a56e4`（命令位置の公開資料なし） · `004a56e8`（命令位置の公開資料なし）

~~~diff
- 004a56e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 004a56e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a56e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 004a56e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a56e4 bytes 081940f9
+ 004a56e4 bytes 084140f9
- 004a56e8 ["COPY", "register:40b0:8", ["register:4000:8"]]
- 004a56e8 bytes f60300aa
+ 004a56e8 ["COPY", "register:40b0:8", ["register:4000:8"]]
+ 004a56e8 bytes f60300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dea23e2e733f6bdf0e5385f0d87aac9b"></a>

### [`004a5838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5838.md) → [`004a5838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5838.md) _ZN5Botan4Pipe5writeEPKhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc1c0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdc210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc210.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a58a4",
      "incomplete_value": false,
      "site": "004a58ac",
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
            "const:992:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a58a4",
      "incomplete_value": false,
      "site": "004a58ac",
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
            "const:a1f:8"
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
      "definition_site": "004a58e0",
      "incomplete_value": true,
      "site": "004a58ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a58e0",
      "incomplete_value": true,
      "site": "004a58ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a58a4",
      "PARAM",
      [
        "storage",
        "00291a1f",
        null,
        "string"
      ]
    ],
    [
      "004a58e0",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "004a58e0",
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
      "004a58a4",
      "PARAM",
      [
        "storage",
        "00291992",
        null,
        "string"
      ]
    ],
    [
      "004a58e0",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "004a58e0",
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

- 旧版 [`004a58a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5838.md#insn-004a58a4) · [`004a58e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5838.md#insn-004a58e0)
- 新版 `004a58a4`（命令位置の公開資料なし） · `004a58e0`（命令位置の公開資料なし）

~~~diff
- 004a58a4 ["COPY", "tmp:0:8", ["const:a1f:8"]]
- 004a58a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a58a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a58a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a58a4 ["COPY", "tmp:0:8", ["const:992:8"]]
+ 004a58a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a58a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a58a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a58a4 bytes 217c2891
+ 004a58a4 bytes 21482691
- 004a58e0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 004a58e0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a58e0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 004a58e0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a58e0 bytes 218447f9
+ 004a58e0 bytes 21ac47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32cdf32d12570df23991d197de5d2c94"></a>

### [`004a5940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5940.md) → [`004a5940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5940.md) _ZN5Botan4Pipe7end_msgEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc1d0.md) · 呼出先 12件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`004a4d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a4/004a4d88.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00bdc220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc220.md) · 呼出先 12件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`004a4d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4d88.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 1件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a59a8",
      "incomplete_value": true,
      "site": "004a59ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a59a8",
      "incomplete_value": true,
      "site": "004a59ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "004a5998",
      "incomplete_value": true,
      "site": "004a5998",
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
      "definition_site": "004a5998",
      "incomplete_value": true,
      "site": "004a5998",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a59e0",
      "incomplete_value": true,
      "site": "004a59e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a59e0",
      "incomplete_value": true,
      "site": "004a59e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a59a0",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a59ac",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a59d0",
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
      "004a59a0",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a59ac",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a59d0",
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

- 旧版 [`004a5990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5940.md#insn-004a5990) · [`004a59a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5940.md#insn-004a59a0) · [`004a59d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5940.md#insn-004a59d0)
- 新版 `004a5990`（命令位置の公開資料なし） · `004a59a0`（命令位置の公開資料なし） · `004a59d0`（命令位置の公開資料なし）

~~~diff
- 004a5990 ["COPY", "tmp:0:8", ["const:b48:8"]]
- 004a5990 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004a5990 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004a5990 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004a5990 ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 004a5990 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004a5990 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004a5990 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004a5990 bytes 29212d91
+ 004a5990 bytes 29612e91
- 004a59a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 004a59a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a59a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 004a59a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a59a0 bytes 081940f9
+ 004a59a0 bytes 084140f9
- 004a59d0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004a59d0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a59d0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004a59d0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a59d0 bytes 299543f9
+ 004a59d0 bytes 29bd43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-303e12b9e445dd1cee0cb8e2a19fbb7f"></a>

### [`004a5bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5bdc.md) → [`004a5bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5bdc.md) _ZN5Botan4Pipe5writeERNS_10DataSourceE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc200.md) · 呼出先 9件 [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 1件 [`00bdc250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc250.md) · 呼出先 9件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.30% / 新版 97.30%

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
      "definition_site": "004a5c98",
      "incomplete_value": true,
      "site": "004a5c98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a5c98",
      "incomplete_value": true,
      "site": "004a5c98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a5cf4",
      "incomplete_value": true,
      "site": "004a5cfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a5cf4",
      "incomplete_value": true,
      "site": "004a5cfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a5cf8",
      "incomplete_value": true,
      "site": "004a5cfc",
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
      "definition_site": "004a5cf8",
      "incomplete_value": true,
      "site": "004a5cfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a5c84",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004a5cf4",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "004a5cf4",
      "PARAM",
      [
        "storage",
        "00c168a0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a5c84",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004a5cf4",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "004a5cf4",
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a5c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5bdc.md#insn-004a5c84) · [`004a5cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5bdc.md#insn-004a5cec) · [`004a5cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5bdc.md#insn-004a5cf4)
- 新版 `004a5c84`（命令位置の公開資料なし） · `004a5cec`（命令位置の公開資料なし） · `004a5cf4`（命令位置の公開資料なし）

~~~diff
- 004a5c84 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004a5c84 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5c84 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004a5c84 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a5c84 bytes 299543f9
+ 004a5c84 bytes 29bd43f9
- 004a5cec ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 004a5cec ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 004a5cec bytes a23b00b0
+ 004a5cec bytes a23b00d0
- 004a5cf4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
- 004a5cf4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5cf4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ff8:8"]]
+ 004a5cf4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a5cf4 bytes 21d447f9
+ 004a5cf4 bytes 21fc47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb928d2e57dd4ec46b4c25ad18a5f373"></a>

### [`004a5e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5e90.md) → [`004a5e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5e90.md) _ZN5Botan4Pipe13append_filterEPNS_6FilterE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a5ef8",
      "incomplete_value": false,
      "site": "004a5f00",
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
            "const:9b2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a5ef8",
      "incomplete_value": false,
      "site": "004a5f00",
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
            "const:a3f:8"
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
      "definition_site": "004a5f34",
      "incomplete_value": true,
      "site": "004a5f40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a5f34",
      "incomplete_value": true,
      "site": "004a5f40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a5ef8",
      "PARAM",
      [
        "storage",
        "00295a3f",
        null,
        "string"
      ]
    ],
    [
      "004a5f34",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "004a5f34",
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
      "004a5ef8",
      "PARAM",
      [
        "storage",
        "002959b2",
        null,
        "string"
      ]
    ],
    [
      "004a5f34",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "004a5f34",
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

- 旧版 [`004a5ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5e90.md#insn-004a5ef8) · [`004a5f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5e90.md#insn-004a5f34)
- 新版 `004a5ef8`（命令位置の公開資料なし） · `004a5f34`（命令位置の公開資料なし）

~~~diff
- 004a5ef8 ["COPY", "tmp:0:8", ["const:a3f:8"]]
- 004a5ef8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a5ef8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a5ef8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a5ef8 ["COPY", "tmp:0:8", ["const:9b2:8"]]
+ 004a5ef8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a5ef8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a5ef8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a5ef8 bytes 21fc2891
+ 004a5ef8 bytes 21c82691
- 004a5f34 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 004a5f34 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5f34 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 004a5f34 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a5f34 bytes 218447f9
+ 004a5f34 bytes 21ac47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d03a2ae14e7763630f22dad3ad5b840"></a>

### [`004a5f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5f94.md) → [`004a5f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5f94.md) _ZN5Botan4Pipe7prependEPNS_6FilterE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 95.80% / 新版 95.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004a5fd0",
      "incomplete_value": true,
      "site": "004a5fd4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "004a5fd0",
      "incomplete_value": true,
      "site": "004a5fd4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a6060",
      "incomplete_value": false,
      "site": "004a6068",
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
            "const:5e5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6060",
      "incomplete_value": false,
      "site": "004a6068",
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
            "const:55a:8"
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
      "definition_site": "004a609c",
      "incomplete_value": true,
      "site": "004a60a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a609c",
      "incomplete_value": true,
      "site": "004a60a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a5fc4",
      "READ",
      [
        "storage",
        "00c1b0c8",
        null,
        "pointer"
      ]
    ],
    [
      "004a6060",
      "PARAM",
      [
        "storage",
        "002a555a",
        null,
        "string"
      ]
    ],
    [
      "004a609c",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a5fc4",
      "READ",
      [
        "storage",
        "00c1b118",
        null,
        "pointer"
      ]
    ],
    [
      "004a6060",
      "PARAM",
      [
        "storage",
        "002a55e5",
        null,
        "string"
      ]
    ],
    [
      "004a609c",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a5fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5f94.md#insn-004a5fc4) · [`004a6060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5f94.md#insn-004a6060) · [`004a609c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a5f94.md#insn-004a609c)
- 新版 `004a5fc4`（命令位置の公開資料なし） · `004a6060`（命令位置の公開資料なし） · `004a609c`（命令位置の公開資料なし）

~~~diff
- 004a5fc4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c8:8"]]
- 004a5fc4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5fc4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:118:8"]]
+ 004a5fc4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a5fc4 bytes 296540f9
+ 004a5fc4 bytes 298d40f9
- 004a6060 ["COPY", "tmp:0:8", ["const:55a:8"]]
- 004a6060 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a6060 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a6060 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a6060 ["COPY", "tmp:0:8", ["const:5e5:8"]]
+ 004a6060 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a6060 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a6060 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a6060 bytes 21681591
+ 004a6060 bytes 21941791
- 004a609c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 004a609c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a609c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 004a609c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a609c bytes 218447f9
+ 004a609c bytes 21ac47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b2359ecf5b73d7c7f45370a96a6519c"></a>

### [`004a61cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a61cc.md) → [`004a61cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a61cc.md) _ZN5Botan4Pipe3popEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a6278",
      "incomplete_value": false,
      "site": "004a6280",
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
            "const:a11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6278",
      "incomplete_value": false,
      "site": "004a6280",
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
            "const:a9e:8"
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
      "definition_site": "004a62b4",
      "incomplete_value": true,
      "site": "004a62c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a62b4",
      "incomplete_value": true,
      "site": "004a62c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a6318",
      "incomplete_value": true,
      "site": "004a6324",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a6318",
      "incomplete_value": true,
      "site": "004a6324",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a6278",
      "PARAM",
      [
        "storage",
        "00295a9e",
        null,
        "string"
      ]
    ],
    [
      "004a62b4",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "004a62b4",
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
      "004a6278",
      "PARAM",
      [
        "storage",
        "00295a11",
        null,
        "string"
      ]
    ],
    [
      "004a62b4",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "004a62b4",
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

- 旧版 [`004a6278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a61cc.md#insn-004a6278) · [`004a62b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a61cc.md#insn-004a62b4) · [`004a6318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a61cc.md#insn-004a6318)
- 新版 `004a6278`（命令位置の公開資料なし） · `004a62b4`（命令位置の公開資料なし） · `004a6318`（命令位置の公開資料なし）

~~~diff
- 004a6278 ["COPY", "tmp:0:8", ["const:a9e:8"]]
- 004a6278 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a6278 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a6278 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a6278 ["COPY", "tmp:0:8", ["const:a11:8"]]
+ 004a6278 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a6278 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a6278 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a6278 bytes 21782a91
+ 004a6278 bytes 21442891
- 004a62b4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 004a62b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a62b4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 004a62b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a62b4 bytes 218447f9
+ 004a62b4 bytes 21ac47f9
- 004a6318 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 004a6318 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a6318 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 004a6318 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a6318 bytes 218447f9
+ 004a6318 bytes 21ac47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb04c782786d26695b60197fd3edc4aa"></a>

### [`004a6378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6378.md) → [`004a6378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6378.md) _ZN5BotanlsERNSt6__ndk113basic_ostreamIcNS0_11char_traitsIcEEEERNS_4PipeE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a6450",
      "incomplete_value": true,
      "site": "004a6450",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a6450",
      "incomplete_value": true,
      "site": "004a6450",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a64b0",
      "incomplete_value": true,
      "site": "004a64b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a64b0",
      "incomplete_value": true,
      "site": "004a64b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a64b4",
      "incomplete_value": true,
      "site": "004a64b8",
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
      "definition_site": "004a64b4",
      "incomplete_value": true,
      "site": "004a64b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a6440",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004a64b0",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "004a64b0",
      "PARAM",
      [
        "storage",
        "00c168a0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a6440",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004a64b0",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "004a64b0",
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a6440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6378.md#insn-004a6440) · [`004a64a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6378.md#insn-004a64a8) · [`004a64b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6378.md#insn-004a64b0)
- 新版 `004a6440`（命令位置の公開資料なし） · `004a64a8`（命令位置の公開資料なし） · `004a64b0`（命令位置の公開資料なし）

~~~diff
- 004a6440 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004a6440 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a6440 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004a6440 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a6440 bytes 299543f9
+ 004a6440 bytes 29bd43f9
- 004a64a8 ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 004a64a8 ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 004a64a8 bytes a23b0090
+ 004a64a8 bytes a23b00b0
- 004a64b0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
- 004a64b0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a64b0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ff8:8"]]
+ 004a64b0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a64b0 bytes 21d447f9
+ 004a64b0 bytes 21fc47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-003e5845d94d48db867330467f288bcc"></a>

### [`004a6590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6590.md) → [`004a6590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6590.md) _ZN5BotanrsERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEERNS_4PipeE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a6650",
      "incomplete_value": true,
      "site": "004a6650",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a6650",
      "incomplete_value": true,
      "site": "004a6650",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a66b0",
      "incomplete_value": true,
      "site": "004a66b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a66b0",
      "incomplete_value": true,
      "site": "004a66b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a66b4",
      "incomplete_value": true,
      "site": "004a66b8",
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
      "definition_site": "004a66b4",
      "incomplete_value": true,
      "site": "004a66b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a6640",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004a66b0",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "004a66b0",
      "PARAM",
      [
        "storage",
        "00c168a0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a6640",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004a66b0",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "004a66b0",
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a6640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6590.md#insn-004a6640) · [`004a66a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6590.md#insn-004a66a8) · [`004a66b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6590.md#insn-004a66b0)
- 新版 `004a6640`（命令位置の公開資料なし） · `004a66a8`（命令位置の公開資料なし） · `004a66b0`（命令位置の公開資料なし）

~~~diff
- 004a6640 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004a6640 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a6640 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004a6640 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a6640 bytes 299543f9
+ 004a6640 bytes 29bd43f9
- 004a66a8 ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 004a66a8 ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 004a66a8 bytes a23b0090
+ 004a66a8 bytes a23b00b0
- 004a66b0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
- 004a66b0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a66b0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ff8:8"]]
+ 004a66b0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a66b0 bytes 21d447f9
+ 004a66b0 bytes 21fc47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ceb837c573fc483693f4f92a6547421"></a>

### [`004a6788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6788.md) → [`004a6788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6788.md) _ZNK5Botan4Pipe14get_message_noERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004a6834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6834.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004a6834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6834.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a6814",
      "incomplete_value": true,
      "site": "004a681c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:120:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6814",
      "incomplete_value": true,
      "site": "004a681c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d0:8"
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
      "004a6814",
      "READ",
      [
        "storage",
        "00c1b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "004a6814",
      "PARAM",
      [
        "storage",
        "00be9b88",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a6814",
      "READ",
      [
        "storage",
        "00c1b120",
        null,
        "pointer"
      ]
    ],
    [
      "004a6814",
      "PARAM",
      [
        "storage",
        "00be9bd8",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a6814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6788.md#insn-004a6814)
- 新版 `004a6814`（命令位置の公開資料なし）

~~~diff
- 004a6814 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d0:8"]]
- 004a6814 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a6814 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:120:8"]]
+ 004a6814 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a6814 bytes 216840f9
+ 004a6814 bytes 219040f9
~~~


<a id="compare-966c40641fa7edf95bc3204bbcda5dd6"></a>

### [`004a6834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6834.md) → [`004a6834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6834.md) FUN_004a6834

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004a53c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a5/004a53c0.md) [`004a6788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6788.md) [`004a6aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6aa8.md) [`004a6e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6e24.md) · 呼出先 7件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)
- 新版 呼出元 4件 [`004a53c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a53c0.md) [`004a6788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6788.md) [`004a6aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6aa8.md) [`004a6e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6e24.md) · 呼出先 7件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.86% / 新版 98.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a68fc",
      "incomplete_value": true,
      "site": "004a6900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a68fc",
      "incomplete_value": true,
      "site": "004a6900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a6930",
      "incomplete_value": true,
      "site": "004a6934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a6930",
      "incomplete_value": true,
      "site": "004a6934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a68e0",
      "incomplete_value": false,
      "site": "004a68ec",
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
            "const:83d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a68e0",
      "incomplete_value": false,
      "site": "004a68ec",
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
            "const:8ca:8"
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
      "004a68e0",
      "PARAM",
      [
        "storage",
        "002968ca",
        null,
        "string"
      ]
    ],
    [
      "004a68f4",
      "READ",
      [
        "storage",
        "00c1af20",
        null,
        "pointer"
      ]
    ],
    [
      "004a6900",
      "DATA",
      [
        "storage",
        "00bea440",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004a68e0",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ],
    [
      "004a68f4",
      "READ",
      [
        "storage",
        "00c1af70",
        null,
        "pointer"
      ]
    ],
    [
      "004a6900",
      "DATA",
      [
        "storage",
        "00bea490",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a68e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6834.md#insn-004a68e0) · [`004a68f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6834.md#insn-004a68f4) · [`004a692c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6834.md#insn-004a692c)
- 新版 `004a68e0`（命令位置の公開資料なし） · `004a68f4`（命令位置の公開資料なし） · `004a692c`（命令位置の公開資料なし）

~~~diff
- 004a68e0 ["COPY", "tmp:0:8", ["const:8ca:8"]]
- 004a68e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a68e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a68e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a68e0 ["COPY", "tmp:0:8", ["const:83d:8"]]
+ 004a68e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a68e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a68e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a68e0 bytes 21282391
+ 004a68e0 bytes 21f42091
- 004a68f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
- 004a68f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a68f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f70:8"]]
+ 004a68f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a68f4 bytes 089147f9
+ 004a68f4 bytes 08b947f9
- 004a692c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d8:8"]]
- 004a692c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a692c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:128:8"]]
+ 004a692c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a692c bytes 086d40f9
+ 004a692c bytes 089540f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c055cc0cc703d09b6d21af798ef01694"></a>

### [`004a6aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6aa8.md) → [`004a6aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6aa8.md) _ZN5Botan4Pipe4readEPhmm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc220.md) · 呼出先 6件 [`004a6834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6834.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdc270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc270.md) · 呼出先 6件 [`004a6834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6834.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

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
      "definition_site": "004a6bac",
      "incomplete_value": true,
      "site": "004a6bb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:120:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6bac",
      "incomplete_value": true,
      "site": "004a6bb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d0:8"
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
      "004a6bac",
      "READ",
      [
        "storage",
        "00c1b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "004a6bac",
      "PARAM",
      [
        "storage",
        "00be9b88",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a6bac",
      "READ",
      [
        "storage",
        "00c1b120",
        null,
        "pointer"
      ]
    ],
    [
      "004a6bac",
      "PARAM",
      [
        "storage",
        "00be9bd8",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a6bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6aa8.md#insn-004a6bac)
- 新版 `004a6bac`（命令位置の公開資料なし）

~~~diff
- 004a6bac ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d0:8"]]
- 004a6bac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a6bac ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:120:8"]]
+ 004a6bac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a6bac bytes 216840f9
+ 004a6bac bytes 219040f9
~~~


<a id="compare-7cf62211085e900e198a94db5635d2d5"></a>

### [`004a6c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6c9c.md) → [`004a6c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6c9c.md) _ZN5Botan4Pipe18read_all_as_stringEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.47% / 新版 97.47%

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
      "definition_site": "004a6d6c",
      "incomplete_value": true,
      "site": "004a6d6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a6d6c",
      "incomplete_value": true,
      "site": "004a6d6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a6dc8",
      "incomplete_value": true,
      "site": "004a6dd0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a6dc8",
      "incomplete_value": true,
      "site": "004a6dd0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a6dcc",
      "incomplete_value": true,
      "site": "004a6dd0",
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
      "definition_site": "004a6dcc",
      "incomplete_value": true,
      "site": "004a6dd0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004a6d58",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004a6dc8",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "004a6dc8",
      "PARAM",
      [
        "storage",
        "00c168a0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a6d58",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004a6dc8",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "004a6dc8",
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a6d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6c9c.md#insn-004a6d58) · [`004a6dc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6c9c.md#insn-004a6dc0) · [`004a6dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6c9c.md#insn-004a6dc8)
- 新版 `004a6d58`（命令位置の公開資料なし） · `004a6dc0`（命令位置の公開資料なし） · `004a6dc8`（命令位置の公開資料なし）

~~~diff
- 004a6d58 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004a6d58 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a6d58 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004a6d58 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a6d58 bytes 299543f9
+ 004a6d58 bytes 29bd43f9
- 004a6dc0 ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 004a6dc0 ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 004a6dc0 bytes a23b0090
+ 004a6dc0 bytes a23b00b0
- 004a6dc8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
- 004a6dc8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a6dc8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ff8:8"]]
+ 004a6dc8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a6dc8 bytes 21d447f9
+ 004a6dc8 bytes 21fc47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2c19de7302416135cc9315e3f42d654"></a>

### [`004a6e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6e24.md) → [`004a6e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6e24.md) _ZNK5Botan4Pipe4peekEPhmmm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc240.md) · 呼出先 6件 [`004a6834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6834.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdc290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc290.md) · 呼出先 6件 [`004a6834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6834.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

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
      "definition_site": "004a6f40",
      "incomplete_value": true,
      "site": "004a6f48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:120:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6f40",
      "incomplete_value": true,
      "site": "004a6f48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d0:8"
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
      "004a6f40",
      "READ",
      [
        "storage",
        "00c1b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "004a6f40",
      "PARAM",
      [
        "storage",
        "00be9b88",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a6f40",
      "READ",
      [
        "storage",
        "00c1b120",
        null,
        "pointer"
      ]
    ],
    [
      "004a6f40",
      "PARAM",
      [
        "storage",
        "00be9bd8",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a6f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6e24.md#insn-004a6f40)
- 新版 `004a6f40`（命令位置の公開資料なし）

~~~diff
- 004a6f40 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d0:8"]]
- 004a6f40 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a6f40 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:120:8"]]
+ 004a6f40 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a6f40 bytes 216840f9
+ 004a6f40 bytes 219040f9
~~~


<a id="compare-f7f1580ee029900e4ea592379a425f18"></a>

### [`004a6fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6fa8.md) → [`004a6fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6fa8.md) _ZNK5Botan4Pipe14get_bytes_readEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a7008",
      "incomplete_value": false,
      "site": "004a7028",
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
            "const:7cc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a7008",
      "incomplete_value": false,
      "site": "004a7028",
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
            "const:732:8"
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
      "definition_site": "004a7018",
      "incomplete_value": false,
      "site": "004a7028",
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
            "const:c1b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a7018",
      "incomplete_value": false,
      "site": "004a7028",
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
            "const:ca8:8"
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
      "definition_site": "004a7020",
      "incomplete_value": false,
      "site": "004a7028",
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
            "const:3d2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a7020",
      "incomplete_value": false,
      "site": "004a7028",
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
            "const:8e1:8"
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
      "004a7008",
      "PARAM",
      [
        "storage",
        "002a6732",
        null,
        "string"
      ]
    ],
    [
      "004a7018",
      "PARAM",
      [
        "storage",
        "00299ca8",
        null,
        null
      ]
    ],
    [
      "004a7020",
      "PARAM",
      [
        "storage",
        "002918e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004a7008",
      "PARAM",
      [
        "storage",
        "002a67cc",
        null,
        "string"
      ]
    ],
    [
      "004a7018",
      "PARAM",
      [
        "storage",
        "00299c1b",
        null,
        null
      ]
    ],
    [
      "004a7020",
      "PARAM",
      [
        "storage",
        "0029c3d2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a7008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6fa8.md#insn-004a7008) · [`004a7018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6fa8.md#insn-004a7018) · [`004a701c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6fa8.md#insn-004a701c)
- 新版 `004a7008`（命令位置の公開資料なし） · `004a7018`（命令位置の公開資料なし） · `004a701c`（命令位置の公開資料なし）

~~~diff
- 004a7008 ["COPY", "tmp:0:8", ["const:732:8"]]
- 004a7008 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004a7008 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004a7008 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004a7008 ["COPY", "tmp:0:8", ["const:7cc:8"]]
+ 004a7008 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004a7008 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004a7008 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004a7008 bytes 00c81c91
+ 004a7008 bytes 00301f91
- 004a7018 ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 004a7018 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004a7018 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004a7018 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004a7018 ["COPY", "tmp:0:8", ["const:c1b:8"]]
+ 004a7018 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004a7018 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004a7018 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004a7018 bytes 42a03291
+ 004a7018 bytes 426c3091
- 004a701c ["COPY", "register:4018:8", ["const:291000:8"]]
+ 004a701c ["COPY", "register:4018:8", ["const:29c000:8"]]
- 004a701c bytes 43efffd0
+ 004a701c bytes a3efffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4439553601260afb9b05a9397653499f"></a>

### [`004a702c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a702c.md) → [`004a702c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a702c.md) _ZNK5Botan4Pipe14get_bytes_readEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a708c",
      "incomplete_value": false,
      "site": "004a70ac",
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
            "const:7cc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a708c",
      "incomplete_value": false,
      "site": "004a70ac",
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
            "const:732:8"
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
      "definition_site": "004a709c",
      "incomplete_value": false,
      "site": "004a70ac",
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
            "const:c1b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a709c",
      "incomplete_value": false,
      "site": "004a70ac",
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
            "const:ca8:8"
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
      "definition_site": "004a70a4",
      "incomplete_value": false,
      "site": "004a70ac",
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
            "const:3d2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a70a4",
      "incomplete_value": false,
      "site": "004a70ac",
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
            "const:8e1:8"
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
      "004a708c",
      "PARAM",
      [
        "storage",
        "002a6732",
        null,
        "string"
      ]
    ],
    [
      "004a709c",
      "PARAM",
      [
        "storage",
        "00299ca8",
        null,
        null
      ]
    ],
    [
      "004a70a4",
      "PARAM",
      [
        "storage",
        "002918e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004a708c",
      "PARAM",
      [
        "storage",
        "002a67cc",
        null,
        "string"
      ]
    ],
    [
      "004a709c",
      "PARAM",
      [
        "storage",
        "00299c1b",
        null,
        null
      ]
    ],
    [
      "004a70a4",
      "PARAM",
      [
        "storage",
        "0029c3d2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a708c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a702c.md#insn-004a708c) · [`004a709c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a702c.md#insn-004a709c) · [`004a70a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a702c.md#insn-004a70a0)
- 新版 `004a708c`（命令位置の公開資料なし） · `004a709c`（命令位置の公開資料なし） · `004a70a0`（命令位置の公開資料なし）

~~~diff
- 004a708c ["COPY", "tmp:0:8", ["const:732:8"]]
- 004a708c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004a708c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004a708c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004a708c ["COPY", "tmp:0:8", ["const:7cc:8"]]
+ 004a708c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004a708c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004a708c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004a708c bytes 00c81c91
+ 004a708c bytes 00301f91
- 004a709c ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 004a709c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004a709c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004a709c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004a709c ["COPY", "tmp:0:8", ["const:c1b:8"]]
+ 004a709c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004a709c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004a709c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004a709c bytes 42a03291
+ 004a709c bytes 426c3091
- 004a70a0 ["COPY", "register:4018:8", ["const:291000:8"]]
+ 004a70a0 ["COPY", "register:4018:8", ["const:29c000:8"]]
- 004a70a0 bytes 43efffd0
+ 004a70a0 bytes a3efffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7506cbee34c7d492cdeea80bfaa58bd5"></a>

### [`004a710c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a710c.md) → [`004a710c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a710c.md) _ZN5Botan11SecureQueueC1Ev

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc210.md) · 呼出先 8件 [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md) [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdc260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc260.md) · 呼出先 8件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.06% / 新版 93.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a713c",
      "incomplete_value": true,
      "site": "004a7144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a713c",
      "incomplete_value": true,
      "site": "004a7144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a7170",
      "incomplete_value": true,
      "site": "004a7178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a7170",
      "incomplete_value": true,
      "site": "004a7178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a7180",
      "incomplete_value": true,
      "site": "004a7180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a7180",
      "incomplete_value": true,
      "site": "004a7180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:88:8"
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
      "004a712c",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a7144",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a7164",
      "READ",
      [
        "storage",
        "00c1b0c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a712c",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a7144",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a7164",
      "READ",
      [
        "storage",
        "00c1b118",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a712c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a710c.md#insn-004a712c) · [`004a7164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a710c.md#insn-004a7164) · [`004a7214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a710c.md#insn-004a7214)
- 新版 `004a712c`（命令位置の公開資料なし） · `004a7164`（命令位置の公開資料なし） · `004a7214`（命令位置の公開資料なし）

~~~diff
- 004a712c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 004a712c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a712c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 004a712c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a712c bytes 081940f9
+ 004a712c bytes 084140f9
- 004a7164 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c8:8"]]
- 004a7164 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a7164 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:118:8"]]
+ 004a7164 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a7164 bytes 086540f9
+ 004a7164 bytes 088d40f9
- 004a7214 ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 004a7214 ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 004a7214 bytes 823b00f0
+ 004a7214 bytes a23b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb4e2a60785ed280c64a031265c469c1"></a>

### [`004a728c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a728c.md) → [`004a728c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a728c.md) _ZN5Botan11SecureQueueC1ERKS0_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md) [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a72cc",
      "incomplete_value": true,
      "site": "004a72d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a72cc",
      "incomplete_value": true,
      "site": "004a72d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a72fc",
      "incomplete_value": true,
      "site": "004a7304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a72fc",
      "incomplete_value": true,
      "site": "004a7304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a730c",
      "incomplete_value": true,
      "site": "004a730c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a730c",
      "incomplete_value": true,
      "site": "004a730c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:88:8"
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
      "004a72c0",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a72d4",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a72f0",
      "READ",
      [
        "storage",
        "00c1b0c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a72c0",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a72d4",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a72f0",
      "READ",
      [
        "storage",
        "00c1b118",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a72c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a728c.md#insn-004a72c0) · [`004a72f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a728c.md#insn-004a72f0) · [`004a73c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a728c.md#insn-004a73c8)
- 新版 `004a72c0`（命令位置の公開資料なし） · `004a72f0`（命令位置の公開資料なし） · `004a73c8`（命令位置の公開資料なし）

~~~diff
- 004a72c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 004a72c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a72c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 004a72c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a72c0 bytes 081940f9
+ 004a72c0 bytes 084140f9
- 004a72f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c8:8"]]
- 004a72f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a72f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:118:8"]]
+ 004a72f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a72f0 bytes 086540f9
+ 004a72f0 bytes 088d40f9
- 004a73c8 ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 004a73c8 ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 004a73c8 bytes 823b00f0
+ 004a73c8 bytes a23b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ed50d7631d146e211b632d9fd29d308"></a>

### [`004a7444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a7444.md) → [`004a7444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7444.md) _ZN5Botan11SecureQueue5writeEPKhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc250.md) · 呼出先 8件 [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdc2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2a0.md) · 呼出先 8件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a75bc",
      "incomplete_value": true,
      "site": "004a75c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a75bc",
      "incomplete_value": true,
      "site": "004a75c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a75c0",
      "incomplete_value": true,
      "site": "004a75c4",
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
      "definition_site": "004a75c0",
      "incomplete_value": true,
      "site": "004a75c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 7,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a75f4",
      "incomplete_value": true,
      "site": "004a75fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a75f4",
      "incomplete_value": true,
      "site": "004a75fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a75bc",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "004a75bc",
      "PARAM",
      [
        "storage",
        "00c168a0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004a75c0",
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
      "004a75bc",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "004a75bc",
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004a75c0",
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

- 旧版 [`004a75b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a7444.md#insn-004a75b4) · [`004a75bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a7444.md#insn-004a75bc) · [`004a75c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a7444.md#insn-004a75c0)
- 新版 `004a75b4`（命令位置の公開資料なし） · `004a75bc`（命令位置の公開資料なし） · `004a75c0`（命令位置の公開資料なし）

~~~diff
- 004a75b4 ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 004a75b4 ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 004a75b4 bytes 823b00f0
+ 004a75b4 bytes a23b0090
- 004a75bc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
- 004a75bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a75bc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ff8:8"]]
+ 004a75bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a75bc bytes 21d447f9
+ 004a75bc bytes 21fc47f9
- 004a75c0 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:fb0:8"]]
- 004a75c0 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a75c0 ["COPY", "tmp:0:8", ["register:4010:8"]]
+ 004a75c0 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 004a75c0 bytes 42d847f9
+ 004a75c0 bytes 420040f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c735c064338b1b96bcc128816a6d7fe"></a>

### [`004a7634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a7634.md) → [`004a7634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7634.md) _ZN5Botan11SecureQueue7destroyEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a7694",
      "incomplete_value": true,
      "site": "004a7694",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004a7694",
      "incomplete_value": true,
      "site": "004a7694",
      "value": [
        "LOAD",
        "8",
        [
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
      "004a7684",
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
      "004a7684",
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

- 旧版 [`004a7684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a7634.md#insn-004a7684)
- 新版 `004a7684`（命令位置の公開資料なし）

~~~diff
- 004a7684 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 004a7684 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a7684 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 004a7684 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a7684 bytes c99643f9
+ 004a7684 bytes c9be43f9
~~~


<a id="compare-92f543d336476e7050484a1d9163cbee"></a>

### [`004a76c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a76c0.md) → [`004a76c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a76c0.md) _ZN5Botan11SecureQueueaSERKS0_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a7744",
      "incomplete_value": true,
      "site": "004a7744",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004a7744",
      "incomplete_value": true,
      "site": "004a7744",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a7828",
      "incomplete_value": true,
      "site": "004a7830",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a7828",
      "incomplete_value": true,
      "site": "004a7830",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a782c",
      "incomplete_value": true,
      "site": "004a7830",
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
      "definition_site": "004a782c",
      "incomplete_value": true,
      "site": "004a7830",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a7734",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004a7828",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "004a7828",
      "PARAM",
      [
        "storage",
        "00c168a0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a7734",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004a7828",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "004a7828",
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a7734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a76c0.md#insn-004a7734) · [`004a7820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a76c0.md#insn-004a7820) · [`004a7828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a76c0.md#insn-004a7828)
- 新版 `004a7734`（命令位置の公開資料なし） · `004a7820`（命令位置の公開資料なし） · `004a7828`（命令位置の公開資料なし）

~~~diff
- 004a7734 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
- 004a7734 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a7734 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:778:8"]]
+ 004a7734 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a7734 bytes 299743f9
+ 004a7734 bytes 29bf43f9
- 004a7820 ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 004a7820 ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 004a7820 bytes 823b00f0
+ 004a7820 bytes a23b0090
- 004a7828 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
- 004a7828 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a7828 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ff8:8"]]
+ 004a7828 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a7828 bytes 21d447f9
+ 004a7828 bytes 21fc47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc6bdf81e0b850dbc0b4cc7c03b0ba3a"></a>

### [`004a791c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a791c.md) → [`004a791c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a791c.md) _ZN5Botan13Threaded_ForkC2EPNS_6FilterES2_S2_S2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdc260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc260.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.14% / 新版 90.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a7964",
      "incomplete_value": true,
      "site": "004a796c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a7964",
      "incomplete_value": true,
      "site": "004a796c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a79a4",
      "incomplete_value": true,
      "site": "004a79ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a79a4",
      "incomplete_value": true,
      "site": "004a79ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004a7948",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a796c",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a7994",
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a7948",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a796c",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a7994",
      "READ",
      [
        "storage",
        "00c1b130",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a7948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a791c.md#insn-004a7948) · [`004a7968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a791c.md#insn-004a7968)
- 新版 `004a7948`（命令位置の公開資料なし） · `004a7968`（命令位置の公開資料なし）

~~~diff
- 004a7948 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:30:8"]]
- 004a7948 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a7948 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:80:8"]]
+ 004a7948 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a7948 bytes 291940f9
+ 004a7948 bytes 294140f9
- 004a7968 ["COPY", "register:40c0:8", ["register:4000:8"]]
- 004a7968 bytes f80300aa
+ 004a7968 ["COPY", "register:40c0:8", ["register:4000:8"]]
+ 004a7968 bytes f80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d335c380c0524a5da81b98726afc0a63"></a>

### [`004a7da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a7da8.md) → [`004a7da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7da8.md) _ZN5Botan13Threaded_ForkC1EPPNS_6FilterEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00520d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520d84.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdc260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc260.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdc2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.68% / 新版 88.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a7dd4",
      "incomplete_value": true,
      "site": "004a7dd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a7dd4",
      "incomplete_value": true,
      "site": "004a7dd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a7e10",
      "incomplete_value": true,
      "site": "004a7e18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a7e10",
      "incomplete_value": true,
      "site": "004a7e18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004a7dc4",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "004a7dd8",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a7e00",
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a7dc4",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004a7dd8",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004a7e00",
      "READ",
      [
        "storage",
        "00c1b130",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a7dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a7da8.md#insn-004a7dc4) · [`004a7e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a7da8.md#insn-004a7e00)
- 新版 `004a7dc4`（命令位置の公開資料なし） · `004a7e00`（命令位置の公開資料なし）

~~~diff
- 004a7dc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 004a7dc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a7dc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 004a7dc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a7dc4 bytes 081940f9
+ 004a7dc4 bytes 084140f9
- 004a7e00 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e0:8"]]
- 004a7e00 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a7e00 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:130:8"]]
+ 004a7e00 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a7e00 bytes 297140f9
+ 004a7e00 bytes 299940f9
~~~


<a id="compare-ee2b55d0fe762f4299c2b17b8ca32885"></a>

### [`004a80a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a80a0.md) → [`004a80a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a80a0.md) _ZNK5Botan13Threaded_Fork4nameEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a80bc",
      "incomplete_value": true,
      "site": "004a80bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:57c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a80bc",
      "incomplete_value": true,
      "site": "004a80bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4f1:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "004a80c0",
      "incomplete_value": true,
      "site": "004a80c0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004a80c0",
      "incomplete_value": true,
      "site": "004a80c0",
      "value": [
        "LOAD",
        "8",
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
      "004a80ac",
      "READ",
      [
        "storage",
        "0029c4f1",
        null,
        "string"
      ]
    ],
    [
      "004a80b4",
      "READ",
      [
        "storage",
        "0029c4f6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004a80ac",
      "READ",
      [
        "storage",
        "0029c57c",
        null,
        "string"
      ]
    ],
    [
      "004a80b4",
      "READ",
      [
        "storage",
        "0029c581",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a80a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a80a0.md#insn-004a80a8)
- 新版 `004a80a8`（命令位置の公開資料なし）

~~~diff
- 004a80a8 ["COPY", "tmp:0:8", ["const:4f1:8"]]
- 004a80a8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004a80a8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004a80a8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004a80a8 ["COPY", "tmp:0:8", ["const:57c:8"]]
+ 004a80a8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004a80a8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004a80a8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004a80a8 bytes 4ac51391
+ 004a80a8 bytes 4af11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2e2405bae37d0eccce37dfbd2577c31"></a>

### [`004a832c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a832c.md) → [`004a832c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a832c.md) FUN_004a832c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004a7a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a7a98.md) · 呼出先 6件 [`00521aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00521/00521aec.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb260.md) [`00bdb270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb270.md)
- 新版 呼出元 1件 [`004a7a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7a98.md) · 呼出先 6件 [`00521aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521aec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2b0.md) [`00bdb2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2c0.md)

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
      "definition_site": "004a83d8",
      "incomplete_value": false,
      "site": "004a83dc",
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
            "const:544:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a83d8",
      "incomplete_value": false,
      "site": "004a83dc",
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
            "const:5d1:8"
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
      "004a83d8",
      "PARAM",
      [
        "storage",
        "002945d1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004a83d8",
      "PARAM",
      [
        "storage",
        "00294544",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a83d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a832c.md#insn-004a83d8)
- 新版 `004a83d8`（命令位置の公開資料なし）

~~~diff
- 004a83d8 ["COPY", "tmp:0:8", ["const:5d1:8"]]
- 004a83d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a83d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a83d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a83d8 ["COPY", "tmp:0:8", ["const:544:8"]]
+ 004a83d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a83d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a83d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a83d8 bytes 21441791
+ 004a83d8 bytes 21101591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-656303b0d0e65d0a74bc23e48ddc3399"></a>

### [`004a8854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a8854.md) → [`004a8854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8854.md) FUN_004a8854

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0049e3f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049e3f4.md) [`0050db94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050db94.md) · 呼出先 6件 [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdbb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb90.md)
- 新版 呼出元 2件 [`0049e3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e3f4.md) [`0050db94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050db94.md) · 呼出先 6件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.63% / 新版 92.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a8880",
      "incomplete_value": true,
      "site": "004a8888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a8880",
      "incomplete_value": true,
      "site": "004a8888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a88e8",
      "incomplete_value": true,
      "site": "004a88e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a88e8",
      "incomplete_value": true,
      "site": "004a88e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a8984",
      "incomplete_value": true,
      "site": "004a898c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a8984",
      "incomplete_value": true,
      "site": "004a898c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a8874",
      "READ",
      [
        "storage",
        "00c1b0f8",
        null,
        "pointer"
      ]
    ],
    [
      "004a8888",
      "DATA",
      [
        "storage",
        "00be9cc8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004a88d4",
      "READ",
      [
        "storage",
        "00c1b100",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a8874",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "004a8888",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004a88d4",
      "READ",
      [
        "storage",
        "00c1b150",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a8874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a8854.md#insn-004a8874) · [`004a88d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a8854.md#insn-004a88d4) · [`004a897c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a8854.md#insn-004a897c)
- 新版 `004a8874`（命令位置の公開資料なし） · `004a88d4`（命令位置の公開資料なし） · `004a897c`（命令位置の公開資料なし）

~~~diff
- 004a8874 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
- 004a8874 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a8874 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
+ 004a8874 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a8874 bytes 087d40f9
+ 004a8874 bytes 08a540f9
- 004a88d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:100:8"]]
- 004a88d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a88d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:150:8"]]
+ 004a88d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a88d4 bytes 088140f9
+ 004a88d4 bytes 08a940f9
- 004a897c ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 004a897c ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 004a897c bytes 823b00d0
+ 004a897c bytes 823b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

