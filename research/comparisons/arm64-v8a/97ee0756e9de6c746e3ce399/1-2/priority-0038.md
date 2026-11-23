# v15.7.3 → v15.7.4 · 最優先の変更候補 (38)

[一覧の目次](README.md)

<a id="compare-90c3346a490954f57d18909ddefbed37"></a>

### [`007d8370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d8/007d8370.md) → [`007d8370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d8/007d8370.md) FUN_007d8370

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 17件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465394.md)
- 新版 呼出元 1件 [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 17件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465394.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.91% / 新版 95.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007d83bc",
      "incomplete_value": false,
      "site": "007d83c0",
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
      "definition_site": "007d83bc",
      "incomplete_value": false,
      "site": "007d83c0",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007d86c8",
      "incomplete_value": true,
      "site": "007d86cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "007d86c8",
      "incomplete_value": true,
      "site": "007d86cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 45,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007d86c4",
      "incomplete_value": true,
      "site": "007d86d0",
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
      "definition_site": "007d86c4",
      "incomplete_value": true,
      "site": "007d86d0",
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
    "ordinal": 46,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007d83c0",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "007d86b8",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      "007d86bc",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007d83c0",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "007d86b8",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      "007d86bc",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007d83bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d8/007d8370.md#insn-007d83bc) · [`007d86b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d8/007d8370.md#insn-007d86b8) · [`007d86bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d8/007d8370.md#insn-007d86bc)
- 新版 `007d83bc`（命令位置の公開資料なし） · `007d86b8`（命令位置の公開資料なし） · `007d86bc`（命令位置の公開資料なし）

~~~diff
- 007d83bc ["COPY", "tmp:0:8", ["const:d28:8"]]
- 007d83bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007d83bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007d83bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007d83bc ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 007d83bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007d83bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007d83bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007d83bc bytes 08a13491
+ 007d83bc bytes 08e13591
- 007d86b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 007d86b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007d86b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 007d86b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007d86b8 bytes 08b946f9
+ 007d86b8 bytes 08e146f9
- 007d86bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d78:8"]]
- 007d86bc ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 007d86bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dc8:8"]]
+ 007d86bc ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 007d86bc bytes b5be46f9
+ 007d86bc bytes b5e646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a48922447f45acbc5fe6bc1740a4351b"></a>

### [`007d99a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d99a4.md) → [`007d99a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d9/007d99a4.md) FUN_007d99a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007d9798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d9798.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`007d9798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d9/007d9798.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "007d99b0",
      "incomplete_value": false,
      "site": "007d99b4",
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
      "definition_site": "007d99b0",
      "incomplete_value": false,
      "site": "007d99b4",
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
      "007d99b0",
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
      "007d99b0",
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

- 旧版 [`007d99b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d99a4.md#insn-007d99b0)
- 新版 `007d99b0`（命令位置の公開資料なし）

~~~diff
- 007d99b0 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007d99b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007d99b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007d99b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007d99b0 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007d99b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007d99b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007d99b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007d99b0 bytes 000c0c91
+ 007d99b0 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5832d72c4a3bb69fde950c1cbe418747"></a>

### [`007d9de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d9de8.md) → [`007d9de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d9/007d9de8.md) FUN_007d9de8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007d99b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d99b8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`007d99b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d9/007d99b8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "007d9df4",
      "incomplete_value": false,
      "site": "007d9df8",
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
      "definition_site": "007d9df4",
      "incomplete_value": false,
      "site": "007d9df8",
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
      "007d9df4",
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
      "007d9df4",
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

- 旧版 [`007d9df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d9de8.md#insn-007d9df4)
- 新版 `007d9df4`（命令位置の公開資料なし）

~~~diff
- 007d9df4 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007d9df4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007d9df4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007d9df4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007d9df4 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007d9df4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007d9df4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007d9df4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007d9df4 bytes 000c0c91
+ 007d9df4 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e87432e3add810777065b8dd57868df"></a>

### [`007d9dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d9dfc.md) → [`007d9dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d9/007d9dfc.md) FUN_007d9dfc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007d8824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d8/007d8824.md) [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`007d8824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d8/007d8824.md) [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "007d9e08",
      "incomplete_value": false,
      "site": "007d9e0c",
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
      "definition_site": "007d9e08",
      "incomplete_value": false,
      "site": "007d9e0c",
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
      "007d9e08",
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
      "007d9e08",
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

- 旧版 [`007d9e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d9dfc.md#insn-007d9e08)
- 新版 `007d9e08`（命令位置の公開資料なし）

~~~diff
- 007d9e08 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007d9e08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007d9e08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007d9e08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007d9e08 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007d9e08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007d9e08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007d9e08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007d9e08 bytes 000c0c91
+ 007d9e08 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f33ef71337143a25a3bad11c16dc46e1"></a>

### [`007d9f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d9f3c.md) → [`007d9f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d9/007d9f3c.md) FUN_007d9f3c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007d9e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d9e10.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`007d9e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d9/007d9e10.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "007d9f48",
      "incomplete_value": false,
      "site": "007d9f4c",
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
      "definition_site": "007d9f48",
      "incomplete_value": false,
      "site": "007d9f4c",
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
      "007d9f48",
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
      "007d9f48",
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

- 旧版 [`007d9f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d9f3c.md#insn-007d9f48)
- 新版 `007d9f48`（命令位置の公開資料なし）

~~~diff
- 007d9f48 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007d9f48 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007d9f48 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007d9f48 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007d9f48 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007d9f48 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007d9f48 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007d9f48 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007d9f48 bytes 000c0c91
+ 007d9f48 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-831d639ef031513e488e2e3715430aaa"></a>

### [`007da15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da15c.md) → [`007da15c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007da/007da15c.md) FUN_007da15c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007d9f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d9f50.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`007d9f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d9/007d9f50.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "007da168",
      "incomplete_value": true,
      "site": "007da16c",
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
            "const:39d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007da168",
      "incomplete_value": true,
      "site": "007da16c",
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
      "007da168",
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
      "007da168",
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

- 旧版 [`007da168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da15c.md#insn-007da168)
- 新版 `007da168`（命令位置の公開資料なし）

~~~diff
- 007da168 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007da168 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007da168 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007da168 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007da168 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007da168 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007da168 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007da168 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007da168 bytes 000c0c91
+ 007da168 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07aa85ca449d8952f3b1f683e78ddfe2"></a>

### [`007da290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da290.md) → [`007da290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007da/007da290.md) FUN_007da290

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`007da170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da170.md) [`00aa980c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa980c.md) [`00aaa8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa8f8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`007da170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007da/007da170.md) [`00aa9850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9850.md) [`00aaa93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaa93c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "007da29c",
      "incomplete_value": false,
      "site": "007da2a0",
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
      "definition_site": "007da29c",
      "incomplete_value": false,
      "site": "007da2a0",
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
      "007da29c",
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
      "007da29c",
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

- 旧版 [`007da29c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da290.md#insn-007da29c)
- 新版 `007da29c`（命令位置の公開資料なし）

~~~diff
- 007da29c ["COPY", "tmp:0:8", ["const:303:8"]]
- 007da29c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007da29c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007da29c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007da29c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007da29c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007da29c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007da29c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007da29c bytes 000c0c91
+ 007da29c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfe49c662d5688111998fd06a4c743b7"></a>

### [`007da2a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da2a4.md) → [`007da2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007da/007da2a4.md) _INIT_143

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007da2e0",
      "incomplete_value": true,
      "site": "007da2fc",
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
      "definition_site": "007da2e0",
      "incomplete_value": true,
      "site": "007da2fc",
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
      "definition_site": "007da304",
      "incomplete_value": true,
      "site": "007da320",
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
      "definition_site": "007da304",
      "incomplete_value": true,
      "site": "007da320",
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
      "definition_site": "007da324",
      "incomplete_value": true,
      "site": "007da340",
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
      "definition_site": "007da324",
      "incomplete_value": true,
      "site": "007da340",
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
      "007da2e0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "007da304",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "007da324",
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
      "007da2e0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "007da304",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "007da324",
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

- 旧版 [`007da2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da2a4.md#insn-007da2d0) · [`007da2d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da2a4.md#insn-007da2d8)
- 新版 `007da2d0`（命令位置の公開資料なし） · `007da2d8`（命令位置の公開資料なし）

~~~diff
- 007da2d0 ["COPY", "tmp:0:8", ["const:88:8"]]
- 007da2d0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 007da2d0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 007da2d0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 007da2d0 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 007da2d0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 007da2d0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 007da2d0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 007da2d0 bytes 73220291
+ 007da2d0 bytes 73220391
- 007da2d8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 007da2d8 bytes 69d6ffb0
+ 007da2d8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 007da2d8 bytes 69d6ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b68da004f38e3d0fb22d6d25857fe916"></a>

### [`007da86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da86c.md) → [`007da86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007da/007da86c.md) FUN_007da86c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`009a3648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a3/009a3648.md) · 呼出先 22件 [`0041e03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e03c.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045a6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a6dc.md) [`0045a7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a7e0.md)
- 新版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`009a3648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a3/009a3648.md) · 呼出先 22件 [`0041e03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e03c.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045a6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a6dc.md) [`0045a7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a7e0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 96.62% / 新版 96.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007da8b8",
      "incomplete_value": false,
      "site": "007da8c4",
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
      "definition_site": "007da8b8",
      "incomplete_value": false,
      "site": "007da8c4",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007da8bc",
      "incomplete_value": true,
      "site": "007da8d0",
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
                "const:d3b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007da8bc",
      "incomplete_value": true,
      "site": "007da8d0",
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
                "const:dc8:8"
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
      "definition_site": "007dadd4",
      "incomplete_value": true,
      "site": "007dadd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "007dadd4",
      "incomplete_value": true,
      "site": "007dadd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "007da8bc",
      "READ",
      [
        "storage",
        "00294dc8",
        null,
        "string"
      ]
    ],
    [
      "007da8c4",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "007dadc4",
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
      "007da8bc",
      "READ",
      [
        "storage",
        "00294d3b",
        null,
        "string"
      ]
    ],
    [
      "007da8c4",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "007dadc4",
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

- 旧版 [`007da8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da86c.md#insn-007da8b0) · [`007da8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da86c.md#insn-007da8b4)
- 新版 `007da8b0`（命令位置の公開資料なし） · `007da8b4`（命令位置の公開資料なし）

~~~diff
- 007da8b0 ["COPY", "tmp:0:8", ["const:dc8:8"]]
- 007da8b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007da8b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007da8b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007da8b0 ["COPY", "tmp:0:8", ["const:d3b:8"]]
+ 007da8b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007da8b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007da8b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007da8b0 bytes 29213791
+ 007da8b0 bytes 29ed3491
- 007da8b4 ["COPY", "register:4040:8", ["const:be7000:8"]]
- 007da8b4 bytes 682000b0
+ 007da8b4 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 007da8b4 bytes 682000b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48d551dff225423af13fc1fd5494f262"></a>

### [`007dafe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007dafe4.md) → [`007dafe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007da/007dafe4.md) FUN_007dafe4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 9件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md) [`00ab11f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab11f0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 9件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md) [`00ab1234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1234.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007db020",
      "incomplete_value": false,
      "site": "007db02c",
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
      "definition_site": "007db020",
      "incomplete_value": false,
      "site": "007db02c",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007db024",
      "incomplete_value": true,
      "site": "007db038",
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
                "const:d3b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007db024",
      "incomplete_value": true,
      "site": "007db038",
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
                "const:dc8:8"
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
      "definition_site": "007db0c0",
      "incomplete_value": true,
      "site": "007db0c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "007db0c0",
      "incomplete_value": true,
      "site": "007db0c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "007db024",
      "READ",
      [
        "storage",
        "00294dc8",
        null,
        "string"
      ]
    ],
    [
      "007db02c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "007db0b0",
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
      "007db024",
      "READ",
      [
        "storage",
        "00294d3b",
        null,
        "string"
      ]
    ],
    [
      "007db02c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "007db0b0",
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

- 旧版 [`007db018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007dafe4.md#insn-007db018) · [`007db01c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007dafe4.md#insn-007db01c)
- 新版 `007db018`（命令位置の公開資料なし） · `007db01c`（命令位置の公開資料なし）

~~~diff
- 007db018 ["COPY", "tmp:0:8", ["const:dc8:8"]]
- 007db018 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007db018 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007db018 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007db018 ["COPY", "tmp:0:8", ["const:d3b:8"]]
+ 007db018 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007db018 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007db018 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007db018 bytes 29213791
+ 007db018 bytes 29ed3491
- 007db01c ["COPY", "register:4040:8", ["const:be7000:8"]]
- 007db01c bytes 68200090
+ 007db01c ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 007db01c bytes 68200090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-463257664260ff4757835785391ea793"></a>

### [`007db34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007db34c.md) → [`007db34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007db/007db34c.md) FUN_007db34c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.39% / 新版 98.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007db3a0",
      "incomplete_value": false,
      "site": "007db3b0",
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
      "definition_site": "007db3a0",
      "incomplete_value": false,
      "site": "007db3b0",
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
    "kind": "store_value",
    "new": {
      "definition_site": "007dbabc",
      "incomplete_value": true,
      "site": "007dbac8",
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
      "definition_site": "007dbabc",
      "incomplete_value": true,
      "site": "007dbac8",
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
    "ordinal": 101,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007dbae4",
      "incomplete_value": true,
      "site": "007dbae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "007dbae4",
      "incomplete_value": true,
      "site": "007dbae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 103,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007db3b0",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "007db3c0",
      "PARAM",
      [
        "storage",
        "0029e876",
        null,
        "string"
      ]
    ],
    [
      "007dbab0",
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
      "007db3b0",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "007db3c0",
      "PARAM",
      [
        "storage",
        "0029e901",
        null,
        "string"
      ]
    ],
    [
      "007dbab0",
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

- 旧版 [`007db3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007db34c.md#insn-007db3a0) · [`007db3b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007db34c.md#insn-007db3b4)
- 新版 `007db3a0`（命令位置の公開資料なし） · `007db3b4`（命令位置の公開資料なし）

~~~diff
- 007db3a0 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 007db3a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007db3a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007db3a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007db3a0 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 007db3a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007db3a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007db3a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007db3a0 bytes 4aa13491
+ 007db3a0 bytes 4ae13591
- 007db3b4 ["COPY", "register:4050:8", ["const:29e000:8"]]
- 007db3b4 bytes 0ad6fff0
+ 007db3b4 ["COPY", "register:4050:8", ["const:29e000:8"]]
+ 007db3b4 bytes 0ad6fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de3b7faf681318e7e13049bb2715da84"></a>

### [`007dbf7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007dbf7c.md) → [`007dbf7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007db/007dbf7c.md) FUN_007dbf7c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007dbc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007dbc94.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`007dbc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007db/007dbc94.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "007dbf88",
      "incomplete_value": false,
      "site": "007dbf8c",
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
      "definition_site": "007dbf88",
      "incomplete_value": false,
      "site": "007dbf8c",
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
      "007dbf88",
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
      "007dbf88",
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

- 旧版 [`007dbf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007dbf7c.md#insn-007dbf88)
- 新版 `007dbf88`（命令位置の公開資料なし）

~~~diff
- 007dbf88 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007dbf88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007dbf88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007dbf88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007dbf88 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007dbf88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007dbf88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007dbf88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007dbf88 bytes 000c0c91
+ 007dbf88 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1db1cc34dd7f6ba4809b7a9f4e4aa31"></a>

### [`007dbf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007dbf90.md) → [`007dbf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007db/007dbf90.md) FUN_007dbf90

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007db210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007db210.md) [`007db258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007db258.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 2件 [`007db210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007db/007db210.md) [`007db258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007db/007db258.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "007dbf9c",
      "incomplete_value": false,
      "site": "007dbfa0",
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
      "definition_site": "007dbf9c",
      "incomplete_value": false,
      "site": "007dbfa0",
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
      "007dbf9c",
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
      "007dbf9c",
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

- 旧版 [`007dbf9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007dbf90.md#insn-007dbf9c)
- 新版 `007dbf9c`（命令位置の公開資料なし）

~~~diff
- 007dbf9c ["COPY", "tmp:0:8", ["const:303:8"]]
- 007dbf9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007dbf9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007dbf9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007dbf9c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007dbf9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007dbf9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007dbf9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007dbf9c bytes 000c0c91
+ 007dbf9c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fea8396ac617bed252e3f9ec2218bf5"></a>

### [`007dbfa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007dbfa4.md) → [`007dbfa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007db/007dbfa4.md) FUN_007dbfa4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007db258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007db258.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`007db258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007db/007db258.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "007dbfb0",
      "incomplete_value": false,
      "site": "007dbfb4",
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
      "definition_site": "007dbfb0",
      "incomplete_value": false,
      "site": "007dbfb4",
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
      "007dbfb0",
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
      "007dbfb0",
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

- 旧版 [`007dbfb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007dbfa4.md#insn-007dbfb0)
- 新版 `007dbfb0`（命令位置の公開資料なし）

~~~diff
- 007dbfb0 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007dbfb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007dbfb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007dbfb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007dbfb0 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007dbfb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007dbfb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007dbfb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007dbfb0 bytes 000c0c91
+ 007dbfb0 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40c21a0361146b5ef15d85f3baf959a2"></a>

### [`007dbfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007dbfb8.md) → [`007dbfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007db/007dbfb8.md) FUN_007dbfb8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007db2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007db2c4.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`007db2c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007db/007db2c4.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "007dbfc4",
      "incomplete_value": false,
      "site": "007dbfc8",
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
      "definition_site": "007dbfc4",
      "incomplete_value": false,
      "site": "007dbfc8",
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
      "007dbfc4",
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
      "007dbfc4",
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

- 旧版 [`007dbfc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007dbfb8.md#insn-007dbfc4)
- 新版 `007dbfc4`（命令位置の公開資料なし）

~~~diff
- 007dbfc4 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007dbfc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007dbfc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007dbfc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007dbfc4 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007dbfc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007dbfc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007dbfc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007dbfc4 bytes 000c0c91
+ 007dbfc4 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fc28e1a4bb346efff4defd6011eb946"></a>

### [`007dc468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dc/007dc468.md) → [`007dc468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dc/007dc468.md) FUN_007dc468

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007dc2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dc/007dc2c0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`007dc2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dc/007dc2c0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "007dc474",
      "incomplete_value": false,
      "site": "007dc478",
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
      "definition_site": "007dc474",
      "incomplete_value": false,
      "site": "007dc478",
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
      "007dc474",
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
      "007dc474",
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

- 旧版 [`007dc474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dc/007dc468.md#insn-007dc474)
- 新版 `007dc474`（命令位置の公開資料なし）

~~~diff
- 007dc474 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007dc474 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007dc474 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007dc474 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007dc474 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007dc474 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007dc474 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007dc474 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007dc474 bytes 000c0c91
+ 007dc474 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15a453dac7daa5cceee12290fcccc15f"></a>

### [`007dc47c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dc/007dc47c.md) → [`007dc47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dc/007dc47c.md) _INIT_144

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
      "definition_site": "007dc4b8",
      "incomplete_value": true,
      "site": "007dc4d4",
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
      "definition_site": "007dc4b8",
      "incomplete_value": true,
      "site": "007dc4d4",
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
      "definition_site": "007dc4dc",
      "incomplete_value": true,
      "site": "007dc4f8",
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
      "definition_site": "007dc4dc",
      "incomplete_value": true,
      "site": "007dc4f8",
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
      "definition_site": "007dc4fc",
      "incomplete_value": true,
      "site": "007dc518",
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
      "definition_site": "007dc4fc",
      "incomplete_value": true,
      "site": "007dc518",
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
      "007dc4b8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "007dc4dc",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "007dc4fc",
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
      "007dc4b8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "007dc4dc",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "007dc4fc",
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

- 旧版 [`007dc4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dc/007dc47c.md#insn-007dc4a8) · [`007dc4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dc/007dc47c.md#insn-007dc4b0)
- 新版 `007dc4a8`（命令位置の公開資料なし） · `007dc4b0`（命令位置の公開資料なし）

~~~diff
- 007dc4a8 ["COPY", "tmp:0:8", ["const:a0:8"]]
- 007dc4a8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 007dc4a8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 007dc4a8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 007dc4a8 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 007dc4a8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 007dc4a8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 007dc4a8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 007dc4a8 bytes 73820291
+ 007dc4a8 bytes 73820391
- 007dc4b0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 007dc4b0 bytes 49d6fff0
+ 007dc4b0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 007dc4b0 bytes 49d6fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b58961c554d05c429eb158b6a1be40f"></a>

### [`007dd540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dd/007dd540.md) → [`007dd540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dd/007dd540.md) _INIT_145

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.66% / 新版 92.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007dd768",
      "incomplete_value": false,
      "site": "007dd774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c28000:8"
          ],
          [
            "leaf",
            "const:f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007dd768",
      "incomplete_value": false,
      "site": "007dd774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c28000:8"
          ],
          [
            "leaf",
            "const:b8:8"
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
      "definition_site": "007dd770",
      "incomplete_value": false,
      "site": "007dd774",
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
      "definition_site": "007dd770",
      "incomplete_value": false,
      "site": "007dd774",
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
      "007dd57c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "007dd5a0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "007dd5c0",
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
      "007dd57c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "007dd5a0",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "007dd5c0",
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

- 旧版 [`007dd56c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dd/007dd540.md#insn-007dd56c) · [`007dd578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dd/007dd540.md#insn-007dd578) · [`007dd594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dd/007dd540.md#insn-007dd594)
- 新版 `007dd56c`（命令位置の公開資料なし） · `007dd578`（命令位置の公開資料なし） · `007dd594`（命令位置の公開資料なし）

~~~diff
- 007dd56c ["COPY", "tmp:0:8", ["const:b8:8"]]
- 007dd56c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 007dd56c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 007dd56c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 007dd56c ["COPY", "tmp:0:8", ["const:f8:8"]]
+ 007dd56c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 007dd56c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 007dd56c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 007dd56c bytes 73e20291
+ 007dd56c bytes 73e20391
- 007dd578 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 007dd578 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007dd578 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007dd578 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007dd578 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 007dd578 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007dd578 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007dd578 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007dd578 bytes 29750b91
+ 007dd578 bytes 29dd0d91
- 007dd594 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 007dd594 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007dd594 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007dd594 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007dd594 ["COPY", "tmp:0:8", ["const:38a:8"]]
+ 007dd594 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007dd594 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007dd594 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007dd594 bytes 4ac10b91
+ 007dd594 bytes 4a290e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1a1aa317e9d8b6e2c975e273da04a13"></a>

### [`007dd8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dd/007dd8d0.md) → [`007dd8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dd/007dd8d0.md) FUN_007dd8d0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) · 呼出先 29件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00447a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447a10.md)
- 新版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 29件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00447a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447a10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ddac8",
      "incomplete_value": true,
      "site": "007ddadc",
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
                "const:74f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ddac8",
      "incomplete_value": true,
      "site": "007ddadc",
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
                "const:6c4:8"
              ]
            ]
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
      "definition_site": "007ddae0",
      "incomplete_value": true,
      "site": "007ddae0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007ddae0",
      "incomplete_value": true,
      "site": "007ddae0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ddb10",
      "incomplete_value": true,
      "site": "007ddb24",
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
                "const:7d5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ddb10",
      "incomplete_value": true,
      "site": "007ddb24",
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
                "const:74a:8"
              ]
            ]
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
      "007ddab4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "007ddac8",
      "READ",
      [
        "storage",
        "0029e6c4",
        null,
        "string"
      ]
    ],
    [
      "007ddad0",
      "READ",
      [
        "storage",
        "0029e6d1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007ddab4",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "007ddac8",
      "READ",
      [
        "storage",
        "0029e74f",
        null,
        "string"
      ]
    ],
    [
      "007ddad0",
      "READ",
      [
        "storage",
        "0029e75c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ddaac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dd/007dd8d0.md#insn-007ddaac) · [`007ddabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dd/007dd8d0.md#insn-007ddabc)
- 新版 `007ddaac`（命令位置の公開資料なし） · `007ddabc`（命令位置の公開資料なし）

~~~diff
- 007ddaac ["COPY", "tmp:0:8", ["const:38:8"]]
- 007ddaac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ddaac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ddaac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ddaac ["COPY", "tmp:0:8", ["const:78:8"]]
+ 007ddaac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ddaac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ddaac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ddaac bytes 08e10091
+ 007ddaac bytes 08e10191
- 007ddabc ["COPY", "register:4048:8", ["const:29e000:8"]]
- 007ddabc bytes 09d6ffb0
+ 007ddabc ["COPY", "register:4048:8", ["const:29e000:8"]]
+ 007ddabc bytes 09d6ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b539317f47d6d5995536c6a8eaa60be2"></a>

### [`007de628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007de/007de628.md) → [`007de628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007de/007de628.md) FUN_007de628

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 17件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00449588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449588.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md)
- 新版 呼出元 1件 [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · 呼出先 17件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00449588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449588.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.82% / 新版 97.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007de670",
      "incomplete_value": false,
      "site": "007de67c",
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
      "definition_site": "007de670",
      "incomplete_value": false,
      "site": "007de67c",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007de6b4",
      "incomplete_value": true,
      "site": "007de6b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a7b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007de6b4",
      "incomplete_value": true,
      "site": "007de6b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a6c:8"
              ]
            ]
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
      "definition_site": "007deee8",
      "incomplete_value": true,
      "site": "007deeec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "007deee8",
      "incomplete_value": true,
      "site": "007deeec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 168,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007de67c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "007de698",
      "READ",
      [
        "storage",
        "002a9a6c",
        null,
        "string"
      ]
    ],
    [
      "007deed8",
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
      "007de67c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "007de698",
      "READ",
      [
        "storage",
        "002a9a7b",
        null,
        "string"
      ]
    ],
    [
      "007deed8",
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

- 旧版 [`007de670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007de/007de628.md#insn-007de670) · [`007de68c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007de/007de628.md#insn-007de68c) · [`007deed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007de/007de628.md#insn-007deed8)
- 新版 `007de670`（命令位置の公開資料なし） · `007de68c`（命令位置の公開資料なし） · `007deed8`（命令位置の公開資料なし）

~~~diff
- 007de670 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 007de670 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007de670 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007de670 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007de670 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 007de670 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007de670 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007de670 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007de670 bytes 08a13491
+ 007de670 bytes 08e13591
- 007de68c ["COPY", "tmp:0:8", ["const:a6c:8"]]
- 007de68c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007de68c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007de68c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007de68c ["COPY", "tmp:0:8", ["const:a7b:8"]]
+ 007de68c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007de68c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007de68c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007de68c bytes 29b12991
+ 007de68c bytes 29ed2991
- 007deed8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 007deed8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007deed8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 007deed8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007deed8 bytes 08b946f9
+ 007deed8 bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d02074110a2b39ea0c9c2e8257f233f"></a>

### [`007df8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007df/007df8d4.md) → [`007df8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df8d4.md) _INIT_146

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
      "definition_site": "007df910",
      "incomplete_value": true,
      "site": "007df92c",
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
      "definition_site": "007df910",
      "incomplete_value": true,
      "site": "007df92c",
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
      "definition_site": "007df934",
      "incomplete_value": true,
      "site": "007df950",
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
      "definition_site": "007df934",
      "incomplete_value": true,
      "site": "007df950",
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
      "definition_site": "007df954",
      "incomplete_value": true,
      "site": "007df970",
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
      "definition_site": "007df954",
      "incomplete_value": true,
      "site": "007df970",
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
      "007df910",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "007df934",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "007df954",
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
      "007df910",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "007df934",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "007df954",
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

- 旧版 [`007df900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007df/007df8d4.md#insn-007df900) · [`007df908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007df/007df8d4.md#insn-007df908)
- 新版 `007df900`（命令位置の公開資料なし） · `007df908`（命令位置の公開資料なし）

~~~diff
- 007df900 ["COPY", "tmp:0:8", ["const:d0:8"]]
- 007df900 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 007df900 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 007df900 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 007df900 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 007df900 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 007df900 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 007df900 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 007df900 bytes 73420391
+ 007df900 bytes 73420491
- 007df908 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 007df908 bytes 49d6ff90
+ 007df908 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 007df908 bytes 49d6ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad13a5235ec033b2352250c214af81b5"></a>

### [`007dfc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007df/007dfc70.md) → [`007dfc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007dfc70.md) FUN_007dfc70

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) · 呼出先 14件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`005f0320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f0320.md) [`0069aa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069aa8c.md)
- 新版 呼出元 1件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · 呼出先 14件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`005f0320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0320.md) [`0069aa8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069a/0069aa8c.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 99.53% / 新版 99.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "007e0030",
      "incomplete_value": true,
      "site": "007e0030",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e0030",
      "incomplete_value": true,
      "site": "007e0030",
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
            "const:ff0:8"
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
      "007e0030",
      "WRITE",
      [
        "storage",
        "00c23ff0",
        null,
        "undefined4"
      ]
    ],
    [
      "007e00d4",
      "DATA",
      [
        "storage",
        "00c23fe4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "007e0030",
      "WRITE",
      [
        "storage",
        "00c24040",
        null,
        "undefined4"
      ]
    ],
    [
      "007e00d4",
      "DATA",
      [
        "storage",
        "00c24034",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007e0030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007df/007dfc70.md#insn-007e0030) · [`007e0028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007df/007dfc70.md#insn-007e0028) · [`007e0054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007df/007dfc70.md#insn-007e0054)
- 新版 `007e0030`（命令位置の公開資料なし） · `007e0028`（命令位置の公開資料なし） · `007e0054`（命令位置の公開資料なし）

~~~diff
- 007e0030 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ff0:8"]]
- 007e0030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 007e0030 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:40:8"]]
+ 007e0030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 007e0030 bytes 28f10fb9
+ 007e0030 bytes 284100b9
- 007e0028 ["COPY", "register:4048:8", ["const:c23000:8"]]
+ 007e0028 ["COPY", "register:4048:8", ["const:c24000:8"]]
- 007e0028 bytes 092200f0
+ 007e0028 bytes 29220090
- 007e0054 ["COPY", "register:40d8:8", ["const:c23000:8"]]
+ 007e0054 ["COPY", "register:40d8:8", ["const:c24000:8"]]
- 007e0054 bytes 1b2200f0
+ 007e0054 bytes 3b220090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6827dcbe5599406a2db98507d27579dc"></a>

### [`007e0354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e0/007e0354.md) → [`007e0354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e0/007e0354.md) FUN_007e0354

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) · 呼出先 14件 [`004297e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004297e4.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ad74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046ad74.md)
- 新版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · 呼出先 14件 [`004297e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/004297e4.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ad74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046ad74.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.35% / 新版 98.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007e055c",
      "incomplete_value": true,
      "site": "007e056c",
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
                "const:2fd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e055c",
      "incomplete_value": true,
      "site": "007e056c",
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
                "const:272:8"
              ]
            ]
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
      "007e055c",
      "READ",
      [
        "storage",
        "002a4272",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007e055c",
      "READ",
      [
        "storage",
        "002a42fd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007e0558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e0/007e0354.md#insn-007e0558)
- 新版 `007e0558`（命令位置の公開資料なし）

~~~diff
- 007e0558 ["COPY", "tmp:0:8", ["const:272:8"]]
- 007e0558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007e0558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007e0558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007e0558 ["COPY", "tmp:0:8", ["const:2fd:8"]]
+ 007e0558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007e0558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007e0558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007e0558 bytes 08c90991
+ 007e0558 bytes 08f50b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b82fce0dcfd3d9f1d22e39cb79b8f4eb"></a>

### [`007e09d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e0/007e09d8.md) → [`007e09d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e0/007e09d8.md) _INIT_147

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007e0a14",
      "incomplete_value": true,
      "site": "007e0a30",
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
      "definition_site": "007e0a14",
      "incomplete_value": true,
      "site": "007e0a30",
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
      "definition_site": "007e0a58",
      "incomplete_value": true,
      "site": "007e0a74",
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
      "definition_site": "007e0a58",
      "incomplete_value": true,
      "site": "007e0a74",
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
      "definition_site": "007e0a94",
      "incomplete_value": true,
      "site": "007e0ab0",
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
      "definition_site": "007e0a94",
      "incomplete_value": true,
      "site": "007e0ab0",
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
      "007e0a14",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "007e0a38",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "007e0a58",
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
      "007e0a14",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "007e0a38",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "007e0a58",
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

- 旧版 [`007e0a04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e0/007e09d8.md#insn-007e0a04) · [`007e0a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e0/007e09d8.md#insn-007e0a0c)
- 新版 `007e0a04`（命令位置の公開資料なし） · `007e0a0c`（命令位置の公開資料なし）

~~~diff
- 007e0a04 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 007e0a04 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 007e0a04 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 007e0a04 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 007e0a04 ["COPY", "tmp:0:8", ["const:128:8"]]
+ 007e0a04 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 007e0a04 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 007e0a04 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 007e0a04 bytes 73a20391
+ 007e0a04 bytes 73a20491
- 007e0a0c ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 007e0a0c bytes 29d6fff0
+ 007e0a0c ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 007e0a0c bytes 29d6fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c63618813656334046202b5a8d2d68c"></a>

### [`007e0f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e0/007e0f00.md) → [`007e0f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e0/007e0f00.md) FUN_007e0f00

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007e5fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e5/007e5fa4.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0044dabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044dabc.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md)
- 新版 呼出元 1件 [`007e5fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e5fa4.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0044dabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044dabc.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.67% / 新版 94.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007e0f44",
      "incomplete_value": false,
      "site": "007e0f50",
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
      "definition_site": "007e0f44",
      "incomplete_value": false,
      "site": "007e0f50",
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
    "kind": "store_value",
    "new": {
      "definition_site": "007e0f6c",
      "incomplete_value": true,
      "site": "007e0f84",
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
                "const:29a000:8"
              ],
              [
                "leaf",
                "const:1fc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e0f6c",
      "incomplete_value": true,
      "site": "007e0f84",
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
                "const:29a000:8"
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007e10f0",
      "incomplete_value": true,
      "site": "007e1108",
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
                "const:23a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e10f0",
      "incomplete_value": true,
      "site": "007e1108",
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
                "const:2c7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007e0f50",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "007e0f6c",
      "READ",
      [
        "storage",
        "0029a1fe",
        null,
        "string"
      ]
    ],
    [
      "007e10f0",
      "READ",
      [
        "storage",
        "002992c7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007e0f50",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "007e0f6c",
      "READ",
      [
        "storage",
        "0029a1fc",
        null,
        "string"
      ]
    ],
    [
      "007e10f0",
      "READ",
      [
        "storage",
        "0029923a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007e0f44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e0/007e0f00.md#insn-007e0f44) · [`007e0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e0/007e0f00.md#insn-007e0f60) · [`007e10e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e0/007e0f00.md#insn-007e10e8)
- 新版 `007e0f44`（命令位置の公開資料なし） · `007e0f60`（命令位置の公開資料なし） · `007e10e8`（命令位置の公開資料なし）

~~~diff
- 007e0f44 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 007e0f44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007e0f44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007e0f44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007e0f44 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 007e0f44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007e0f44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007e0f44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007e0f44 bytes 08a13491
+ 007e0f44 bytes 08e13591
- 007e0f60 ["COPY", "tmp:0:8", ["const:1fe:8"]]
- 007e0f60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007e0f60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007e0f60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007e0f60 ["COPY", "tmp:0:8", ["const:1fc:8"]]
+ 007e0f60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007e0f60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007e0f60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007e0f60 bytes 29f90791
+ 007e0f60 bytes 29f10791
- 007e10e8 ["COPY", "tmp:0:8", ["const:2c7:8"]]
- 007e10e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007e10e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007e10e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007e10e8 ["COPY", "tmp:0:8", ["const:23a:8"]]
+ 007e10e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007e10e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007e10e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007e10e8 bytes 291d0b91
+ 007e10e8 bytes 29e90891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47857cf4ba0f21a0972bf6372e2fa0f8"></a>

### [`007e17f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e1/007e17f4.md) → [`007e17f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e1/007e17f4.md) FUN_007e17f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007eb290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007eb/007eb290.md) [`007f78c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f7/007f78c4.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0059d1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d1d4.md)
- 新版 呼出元 2件 [`007eb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007eb/007eb290.md) [`007f78c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f78c4.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0059d1d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d1d4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.51% / 新版 99.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007e1ba8",
      "incomplete_value": true,
      "site": "007e1bb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:13b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e1ba8",
      "incomplete_value": true,
      "site": "007e1bb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a1:8"
              ]
            ]
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
      "007e1ba8",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007e1ba8",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007e1ba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e1/007e17f4.md#insn-007e1ba4)
- 新版 `007e1ba4`（命令位置の公開資料なし）

~~~diff
- 007e1ba4 ["COPY", "tmp:0:8", ["const:a1:8"]]
- 007e1ba4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007e1ba4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007e1ba4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007e1ba4 ["COPY", "tmp:0:8", ["const:13b:8"]]
+ 007e1ba4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007e1ba4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007e1ba4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007e1ba4 bytes 08850291
+ 007e1ba4 bytes 08ed0491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26b9a6b0fd18e0b5e5b76083263c8fde"></a>

### [`007e3220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e3/007e3220.md) → [`007e3220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e3/007e3220.md) FUN_007e3220

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007e5fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e5/007e5fa4.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`007e5fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e5fa4.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007e3550",
      "incomplete_value": true,
      "site": "007e3550",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a03:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e3550",
      "incomplete_value": true,
      "site": "007e3550",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:978:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007e366c",
      "incomplete_value": true,
      "site": "007e366c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:24c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e366c",
      "incomplete_value": true,
      "site": "007e366c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2d9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 64,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007e38c0",
      "incomplete_value": true,
      "site": "007e38c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c93:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e38c0",
      "incomplete_value": true,
      "site": "007e38c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 84,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007e3540",
      "READ",
      [
        "storage",
        "002a0978",
        null,
        "string"
      ]
    ],
    [
      "007e365c",
      "READ",
      [
        "storage",
        "002992d9",
        null,
        "string"
      ]
    ],
    [
      "007e36d8",
      "READ",
      [
        "storage",
        "0029d7b4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007e3540",
      "READ",
      [
        "storage",
        "002a0a03",
        null,
        "string"
      ]
    ],
    [
      "007e365c",
      "READ",
      [
        "storage",
        "0029924c",
        null,
        "string"
      ]
    ],
    [
      "007e36d8",
      "READ",
      [
        "storage",
        "0029d83f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007e353c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e3/007e3220.md#insn-007e353c) · [`007e364c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e3/007e3220.md#insn-007e364c) · [`007e36c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e3/007e3220.md#insn-007e36c8)
- 新版 `007e353c`（命令位置の公開資料なし） · `007e364c`（命令位置の公開資料なし） · `007e36c8`（命令位置の公開資料なし）

~~~diff
- 007e353c ["COPY", "tmp:0:8", ["const:978:8"]]
- 007e353c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007e353c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007e353c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007e353c ["COPY", "tmp:0:8", ["const:a03:8"]]
+ 007e353c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007e353c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007e353c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007e353c bytes 4ae12591
+ 007e353c bytes 4a0d2891
- 007e364c ["COPY", "tmp:0:8", ["const:2d9:8"]]
- 007e364c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007e364c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007e364c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007e364c ["COPY", "tmp:0:8", ["const:24c:8"]]
+ 007e364c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007e364c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007e364c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007e364c bytes 4a650b91
+ 007e364c bytes 4a310991
- 007e36c8 ["COPY", "tmp:0:8", ["const:7b4:8"]]
- 007e36c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007e36c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007e36c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007e36c8 ["COPY", "tmp:0:8", ["const:83f:8"]]
+ 007e36c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007e36c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007e36c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007e36c8 bytes 4ad11e91
+ 007e36c8 bytes 4afd2091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-949970248603bf0fd5537ed4904e4bd9"></a>

### [`007e5734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e5/007e5734.md) → [`007e5734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e5734.md) FUN_007e5734

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`007eafa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ea/007eafa4.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`006f1e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f1e2c.md) [`006f23b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f2/006f23b4.md) [`006f48c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f4/006f48c4.md)
- 新版 呼出元 1件 [`007eafa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ea/007eafa4.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`006f1e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1e2c.md) [`006f23b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f23b4.md) [`006f48c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f48c4.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 98.98% / 新版 98.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007e58d0",
      "incomplete_value": false,
      "site": "007e58d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:fb4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e58d0",
      "incomplete_value": false,
      "site": "007e58d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:f64:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007e598c",
      "incomplete_value": false,
      "site": "007e5994",
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
            "const:f6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e598c",
      "incomplete_value": false,
      "site": "007e5994",
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
            "const:ff9:8"
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
      "007e58d0",
      "WRITE",
      [
        "storage",
        "00c23f64",
        null,
        "undefined1"
      ]
    ],
    [
      "007e5994",
      "DATA",
      [
        "storage",
        "00298ff9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007e58d0",
      "WRITE",
      [
        "storage",
        "00c23fb4",
        null,
        "undefined1"
      ]
    ],
    [
      "007e5994",
      "DATA",
      [
        "storage",
        "00298f6c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007e58d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e5/007e5734.md#insn-007e58d0) · [`007e598c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e5/007e5734.md#insn-007e598c)
- 新版 `007e58d0`（命令位置の公開資料なし） · `007e598c`（命令位置の公開資料なし）

~~~diff
- 007e58d0 ["COPY", "tmp:0:4", ["register:40a0:4"]]
- 007e58d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:f64:8"]]
- 007e58d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 007e58d0 ["COPY", "tmp:0:4", ["register:40a0:4"]]
+ 007e58d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:fb4:8"]]
+ 007e58d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 007e58d0 bytes 14913d39
+ 007e58d0 bytes 14d13e39
- 007e598c ["COPY", "tmp:0:8", ["const:ff9:8"]]
- 007e598c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007e598c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007e598c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007e598c ["COPY", "tmp:0:8", ["const:f6c:8"]]
+ 007e598c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007e598c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007e598c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007e598c bytes 08e53f91
+ 007e598c bytes 08b13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dfd3407cdbed2c2835c72b645a695b6"></a>

### [`007e5fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e5/007e5fa4.md) → [`007e5fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e5fa4.md) FUN_007e5fa4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 50件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e03c.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0042d828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d828.md) [`0044abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abe4.md)
- 新版 呼出元 1件 [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · 呼出先 50件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e03c.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0042d828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d828.md) [`0044abe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abe4.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 93.07% / 新版 93.07%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007e6354",
      "incomplete_value": true,
      "site": "007e6364",
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
                "const:c94:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e6354",
      "incomplete_value": true,
      "site": "007e6364",
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
                "const:bfa:8"
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
      "definition_site": "007e6358",
      "incomplete_value": true,
      "site": "007e6368",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007e6358",
      "incomplete_value": true,
      "site": "007e6368",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 53,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007e67ec",
      "incomplete_value": true,
      "site": "007e67fc",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:ad4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007e67ec",
      "incomplete_value": true,
      "site": "007e67fc",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:a49:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 100,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007e5ff4",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:007e611c",
      "READ",
      [
        "storage",
        "Stack[-0x280]",
        null,
        null
      ]
    ],
    [
      "unmatched:007e6120",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:007e612c"
      ]
    ]
  ],
  "added": [
    [
      "007e5ff4",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "007e611c",
      "READ",
      [
        "storage",
        "Stack[-0x280]",
        null,
        null
      ]
    ],
    [
      "007e6120",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007e612c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007e6118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e5/007e5fa4.md#insn-007e6118) · [`007e6120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e5/007e5fa4.md#insn-007e6120)
- 新版 `007e6118`（命令位置の公開資料なし）

~~~diff
- 007e6118 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 007e6118 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 007e6118 ["COPY", "tmp:0:8", ["const:0:8"]]
- 007e6118 ["COPY", "register:4098:8", ["tmp:0:8"]]
- 007e6118 bytes 13019f9a
+ 007e6118 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 007e6118 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 007e6118 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 007e6118 ["COPY", "register:4098:8", ["tmp:0:8"]]
+ 007e6118 bytes 13019f9a
- 007e6120 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 007e6120 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 007e6120 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 007e6120 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 007e6120 bytes 68000036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14a04d48b086b3241ba50ea9ecbd7062"></a>

### [`007eb474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007eb/007eb474.md) → [`007eb474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007eb/007eb474.md) FUN_007eb474

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007f4120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f4/007f4120.md) · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`004264e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/004264e8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007eb8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007eb/007eb8f8.md)
- 新版 呼出元 1件 [`007f4120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f4/007f4120.md) · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`004264e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/004264e8.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`007eb8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007eb/007eb8f8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.76% / 新版 98.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007eb5a4",
      "incomplete_value": true,
      "site": "007eb5b4",
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
                "const:912:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007eb5a4",
      "incomplete_value": true,
      "site": "007eb5b4",
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
                "const:887:8"
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
      "007eb5a4",
      "READ",
      [
        "storage",
        "0029e887",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007eb5a4",
      "READ",
      [
        "storage",
        "0029e912",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007eb59c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007eb/007eb474.md#insn-007eb59c)
- 新版 `007eb59c`（命令位置の公開資料なし）

~~~diff
- 007eb59c ["COPY", "tmp:0:8", ["const:887:8"]]
- 007eb59c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007eb59c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007eb59c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007eb59c ["COPY", "tmp:0:8", ["const:912:8"]]
+ 007eb59c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007eb59c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007eb59c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007eb59c bytes 291d2291
+ 007eb59c bytes 29492491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0792a0a8eb52714d947cb6a21d00cb5e"></a>

### [`007ebab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007eb/007ebab8.md) → [`007ebab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007eb/007ebab8.md) FUN_007ebab8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`007ec810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ec/007ec810.md) [`007f3c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f3/007f3c28.md) [`00800728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800728.md) · 呼出先 17件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050ae28.md) [`005a83e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a83e4.md)
- 新版 呼出元 3件 [`007ec810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ec/007ec810.md) [`007f3c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3c28.md) [`00800728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/00800728.md) · 呼出先 17件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ae28.md) [`005a83e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a83e4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ebb10",
      "incomplete_value": true,
      "site": "007ebb10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e8a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ebb10",
      "incomplete_value": true,
      "site": "007ebb10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f1e:8"
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
      "definition_site": "007ebb04",
      "incomplete_value": true,
      "site": "007ebb14",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007ebb04",
      "incomplete_value": true,
      "site": "007ebb14",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ebe00",
      "incomplete_value": true,
      "site": "007ebe10",
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
                "const:29a000:8"
              ],
              [
                "leaf",
                "const:226:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ebe00",
      "incomplete_value": true,
      "site": "007ebe10",
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
                "const:29a000:8"
              ],
              [
                "leaf",
                "const:228:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 49,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007ebb00",
      "READ",
      [
        "storage",
        "002aef1e",
        null,
        "string"
      ]
    ],
    [
      "007ebb04",
      "READ",
      [
        "storage",
        "002aef25",
        null,
        "string"
      ]
    ],
    [
      "007ebb24",
      "PARAM",
      [
        "storage",
        "00294de6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007ebb00",
      "READ",
      [
        "storage",
        "002aee8a",
        null,
        "string"
      ]
    ],
    [
      "007ebb04",
      "READ",
      [
        "storage",
        "002aee91",
        null,
        "string"
      ]
    ],
    [
      "007ebb24",
      "PARAM",
      [
        "storage",
        "00294d59",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ebae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007eb/007ebab8.md#insn-007ebae4) · [`007ebb24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007eb/007ebab8.md#insn-007ebb24) · [`007ebd74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007eb/007ebab8.md#insn-007ebd74)
- 新版 `007ebae4`（命令位置の公開資料なし） · `007ebb24`（命令位置の公開資料なし） · `007ebd74`（命令位置の公開資料なし）

~~~diff
- 007ebae4 ["COPY", "tmp:0:8", ["const:f1e:8"]]
- 007ebae4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ebae4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ebae4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ebae4 ["COPY", "tmp:0:8", ["const:e8a:8"]]
+ 007ebae4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ebae4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ebae4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ebae4 bytes 29793c91
+ 007ebae4 bytes 29293a91
- 007ebb24 ["COPY", "tmp:0:8", ["const:de6:8"]]
- 007ebb24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007ebb24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007ebb24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007ebb24 ["COPY", "tmp:0:8", ["const:d59:8"]]
+ 007ebb24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007ebb24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007ebb24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007ebb24 bytes 21983791
+ 007ebb24 bytes 21643591
- 007ebd74 ["COPY", "tmp:0:8", ["const:6d9:8"]]
- 007ebd74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007ebd74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007ebd74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007ebd74 ["COPY", "tmp:0:8", ["const:764:8"]]
+ 007ebd74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007ebd74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007ebd74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007ebd74 bytes 21641b91
+ 007ebd74 bytes 21901d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28f4c4528e5ecc49ad224a83a4a99797"></a>

### [`007f1d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f1/007f1d24.md) → [`007f1d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f1/007f1d24.md) FUN_007f1d24

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`007f4120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f4/007f4120.md) [`007f5814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f5/007f5814.md) · 呼出先 13件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`009e964c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e964c.md) [`009e9790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e9790.md)
- 新版 呼出元 2件 [`007f4120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f4/007f4120.md) [`007f5814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f5/007f5814.md) · 呼出先 13件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`009e9690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9690.md) [`009e97d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e97d4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.10% / 新版 97.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f1ea4",
      "incomplete_value": false,
      "site": "007f1ea8",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:d80:8"
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
      "definition_site": "007f1ea4",
      "incomplete_value": false,
      "site": "007f1ea8",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:d30:8"
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007f1d64",
      "incomplete_value": true,
      "site": "007f1d64",
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
      "definition_site": "007f1d64",
      "incomplete_value": true,
      "site": "007f1d64",
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
      "definition_site": "007f1d6c",
      "incomplete_value": false,
      "site": "007f1d7c",
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
      "definition_site": "007f1d6c",
      "incomplete_value": false,
      "site": "007f1d7c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007f1d60",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f1d6c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f1d74",
      "PARAM",
      [
        "storage",
        "00c00488",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f1d60",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f1d6c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f1d74",
      "PARAM",
      [
        "storage",
        "00c004d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f1d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f1/007f1d24.md#insn-007f1d60) · [`007f1d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f1/007f1d24.md#insn-007f1d6c) · [`007f1d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f1/007f1d24.md#insn-007f1d74)
- 新版 `007f1d60`（命令位置の公開資料なし） · `007f1d6c`（命令位置の公開資料なし） · `007f1d74`（命令位置の公開資料なし）

~~~diff
- 007f1d60 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
- 007f1d60 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f1d60 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ab8:8"]]
+ 007f1d60 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007f1d60 bytes 203d45f9
+ 007f1d60 bytes 205d45f9
- 007f1d6c ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007f1d6c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f1d6c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f1d6c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f1d6c ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007f1d6c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f1d6c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f1d6c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f1d6c bytes 21203991
+ 007f1d6c bytes 21603a91
- 007f1d74 ["COPY", "tmp:0:8", ["const:488:8"]]
- 007f1d74 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007f1d74 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007f1d74 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007f1d74 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 007f1d74 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007f1d74 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007f1d74 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007f1d74 bytes 42201291
+ 007f1d74 bytes 42601391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54825fcd2ee234d0a2ff9315baf1f0a3"></a>

### [`007f24c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f2/007f24c4.md) → [`007f24c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f2/007f24c4.md) FUN_007f24c4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007ffe48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ffe48.md) · 呼出先 34件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`007ffe48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ffe48.md) · 呼出先 34件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.43% / 新版 94.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 20件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f269c",
      "incomplete_value": false,
      "site": "007f269c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f269c",
      "incomplete_value": false,
      "site": "007f269c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
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
      "definition_site": "007f26ec",
      "incomplete_value": false,
      "site": "007f26ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f26ec",
      "incomplete_value": false,
      "site": "007f26ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:530:8"
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
      "definition_site": "007f2a58",
      "incomplete_value": true,
      "site": "007f2a68",
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
                "const:925:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f2a58",
      "incomplete_value": true,
      "site": "007f2a68",
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
                "const:89a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 78,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007f269c",
      "DATA",
      [
        "storage",
        "00c004b0",
        null,
        "undefined *"
      ]
    ],
    [
      "007f26ec",
      "DATA",
      [
        "storage",
        "00c00530",
        null,
        "undefined *"
      ]
    ],
    [
      "007f2a58",
      "READ",
      [
        "storage",
        "0029e89a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f269c",
      "DATA",
      [
        "storage",
        "00c00500",
        null,
        "undefined *"
      ]
    ],
    [
      "007f26ec",
      "DATA",
      [
        "storage",
        "00c00580",
        null,
        "undefined *"
      ]
    ],
    [
      "007f2a58",
      "READ",
      [
        "storage",
        "0029e925",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f2/007f24c4.md#insn-007f2688) · [`007f26dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f2/007f24c4.md#insn-007f26dc) · [`007f2a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f2/007f24c4.md#insn-007f2a50)
- 新版 `007f2688`（命令位置の公開資料なし） · `007f26dc`（命令位置の公開資料なし） · `007f2a50`（命令位置の公開資料なし）

~~~diff
- 007f2688 ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 007f2688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f2688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f2688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f2688 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 007f2688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f2688 bytes 08c11291
+ 007f2688 bytes 08011491
- 007f26dc ["COPY", "tmp:0:8", ["const:530:8"]]
- 007f26dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f26dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f26dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f26dc ["COPY", "tmp:0:8", ["const:580:8"]]
+ 007f26dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f26dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f26dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f26dc bytes 08c11491
+ 007f26dc bytes 08011691
- 007f2a50 ["COPY", "tmp:0:8", ["const:89a:8"]]
- 007f2a50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f2a50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f2a50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f2a50 ["COPY", "tmp:0:8", ["const:925:8"]]
+ 007f2a50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2a50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2a50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f2a50 bytes 08692291
+ 007f2a50 bytes 08952491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84ed21bfe01b5a3bc39bd6e15b82ac89"></a>

### [`007f3788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f3/007f3788.md) → [`007f3788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3788.md) FUN_007f3788

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007ffe48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ffe48.md) · 呼出先 22件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007eafa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ea/007eafa4.md) [`007f3c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f3/007f3c28.md)
- 新版 呼出元 1件 [`007ffe48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ffe48.md) · 呼出先 22件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`007eafa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ea/007eafa4.md) [`007f3c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3c28.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f380c",
      "incomplete_value": true,
      "site": "007f381c",
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
                "const:953:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f380c",
      "incomplete_value": true,
      "site": "007f381c",
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
                "const:8c8:8"
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
      "definition_site": "007f3820",
      "incomplete_value": true,
      "site": "007f3820",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007f3820",
      "incomplete_value": true,
      "site": "007f3820",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f3918",
      "incomplete_value": false,
      "site": "007f3918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f3918",
      "incomplete_value": false,
      "site": "007f3918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
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
      "007f380c",
      "READ",
      [
        "storage",
        "002a38c8",
        null,
        "string"
      ]
    ],
    [
      "007f3810",
      "READ",
      [
        "storage",
        "002a38d7",
        null,
        "string"
      ]
    ],
    [
      "007f3918",
      "DATA",
      [
        "storage",
        "00c006b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f380c",
      "READ",
      [
        "storage",
        "002a3953",
        null,
        "string"
      ]
    ],
    [
      "007f3810",
      "READ",
      [
        "storage",
        "002a3962",
        null,
        "string"
      ]
    ],
    [
      "007f3918",
      "DATA",
      [
        "storage",
        "00c00700",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f3/007f3788.md#insn-007f3804) · [`007f3808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f3/007f3788.md#insn-007f3808)
- 新版 `007f3804`（命令位置の公開資料なし） · `007f3808`（命令位置の公開資料なし）

~~~diff
- 007f3804 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 007f3804 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f3804 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f3804 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f3804 ["COPY", "tmp:0:8", ["const:953:8"]]
+ 007f3804 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3804 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3804 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f3804 bytes 08212391
+ 007f3804 bytes 084d2591
- 007f3808 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 007f3808 bytes e9d5ffb0
+ 007f3808 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 007f3808 bytes e9d5ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04adf3e919274557d43b33b1c05eccf5"></a>

### [`007f3c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f3/007f3c28.md) → [`007f3c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3c28.md) FUN_007f3c28

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007f3788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f3/007f3788.md) [`007ff948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff948.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007ebab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007eb/007ebab8.md) [`007fae20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fae20.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`007f3788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3788.md) [`007ff948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff948.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`007ebab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007eb/007ebab8.md) [`007fae20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fae20.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.59% / 新版 96.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f3c70",
      "incomplete_value": true,
      "site": "007f3c80",
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
                "const:258:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f3c70",
      "incomplete_value": true,
      "site": "007f3c80",
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
                "const:2e5:8"
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
      "definition_site": "007f3c74",
      "incomplete_value": true,
      "site": "007f3c84",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007f3c74",
      "incomplete_value": true,
      "site": "007f3c84",
      "value": [
        "LOAD",
        "8",
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
      "007f3c70",
      "READ",
      [
        "storage",
        "002992e5",
        null,
        "string"
      ]
    ],
    [
      "007f3c74",
      "READ",
      [
        "storage",
        "002992f5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f3c70",
      "READ",
      [
        "storage",
        "00299258",
        null,
        "string"
      ]
    ],
    [
      "007f3c74",
      "READ",
      [
        "storage",
        "00299268",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f3/007f3c28.md#insn-007f3c68) · [`007f3c6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f3/007f3c28.md#insn-007f3c6c)
- 新版 `007f3c68`（命令位置の公開資料なし） · `007f3c6c`（命令位置の公開資料なし）

~~~diff
- 007f3c68 ["COPY", "tmp:0:8", ["const:2e5:8"]]
- 007f3c68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f3c68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f3c68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f3c68 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 007f3c68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3c68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3c68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f3c68 bytes 08950b91
+ 007f3c68 bytes 08610991
- 007f3c6c ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 007f3c6c bytes e9d5ffb0
+ 007f3c6c ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 007f3c6c bytes e9d5ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec71186d47c7b2128ddecf691ac26f53"></a>

### [`007f4120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f4/007f4120.md) → [`007f4120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f4/007f4120.md) FUN_007f4120

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007f78c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f7/007f78c4.md) [`007f8950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8950.md) · 呼出先 31件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00459a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459a90.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 2件 [`007f78c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f78c4.md) [`007f8950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f8950.md) · 呼出先 31件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00459a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459a90.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.69% / 新版 91.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `store_destination` 20件, `store_value` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f44b4",
      "incomplete_value": true,
      "site": "007f44c4",
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
                "const:690:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f44b4",
      "incomplete_value": true,
      "site": "007f44c4",
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
                "const:605:8"
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
      "definition_site": "007f4690",
      "incomplete_value": true,
      "site": "007f46a8",
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
                "const:b13:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f4690",
      "incomplete_value": true,
      "site": "007f46a8",
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
                "const:ba7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 50,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f47a0",
      "incomplete_value": true,
      "site": "007f47b0",
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
                "const:690:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f47a0",
      "incomplete_value": true,
      "site": "007f47b0",
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
                "const:605:8"
              ]
            ]
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
      "007f44a0",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "007f44b4",
      "READ",
      [
        "storage",
        "002a2605",
        null,
        "string"
      ]
    ],
    [
      "007f4520",
      "READ",
      [
        "storage",
        "002aeba7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f44a0",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "007f44b4",
      "READ",
      [
        "storage",
        "002a2690",
        null,
        "string"
      ]
    ],
    [
      "007f4520",
      "READ",
      [
        "storage",
        "002aeb13",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f449c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f4/007f4120.md#insn-007f449c) · [`007f44ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f4/007f4120.md#insn-007f44ac) · [`007f4514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f4/007f4120.md#insn-007f4514)
- 新版 `007f449c`（命令位置の公開資料なし） · `007f44ac`（命令位置の公開資料なし） · `007f4514`（命令位置の公開資料なし）

~~~diff
- 007f449c ["COPY", "tmp:0:8", ["const:38:8"]]
- 007f449c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f449c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f449c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f449c ["COPY", "tmp:0:8", ["const:78:8"]]
+ 007f449c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f449c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f449c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f449c bytes 08e10091
+ 007f449c bytes 08e10191
- 007f44ac ["COPY", "tmp:0:8", ["const:605:8"]]
- 007f44ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f44ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f44ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f44ac ["COPY", "tmp:0:8", ["const:690:8"]]
+ 007f44ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f44ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f44ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f44ac bytes 29151891
+ 007f44ac bytes 29411a91
- 007f4514 ["COPY", "tmp:0:8", ["const:ba7:8"]]
- 007f4514 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f4514 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f4514 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f4514 ["COPY", "tmp:0:8", ["const:b13:8"]]
+ 007f4514 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f4514 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f4514 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f4514 bytes 299d2e91
+ 007f4514 bytes 294d2c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dcdb1d4e37ed1bc8816ef657cb5fd63"></a>

### [`007f5814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f5/007f5814.md) → [`007f5814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f5/007f5814.md) FUN_007f5814

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007f8354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8354.md) · 呼出先 26件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md)
- 新版 呼出元 1件 [`007f8354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f8354.md) · 呼出先 26件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.05% / 新版 99.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f5d28",
      "incomplete_value": true,
      "site": "007f5d28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "007f5d28",
      "incomplete_value": true,
      "site": "007f5d28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "007f5858",
      "incomplete_value": true,
      "site": "007f5858",
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
      "definition_site": "007f5858",
      "incomplete_value": true,
      "site": "007f5858",
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
      "definition_site": "007f5860",
      "incomplete_value": false,
      "site": "007f5874",
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
      "definition_site": "007f5860",
      "incomplete_value": false,
      "site": "007f5874",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007f5854",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f5860",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f5868",
      "PARAM",
      [
        "storage",
        "00c00488",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f5854",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f5860",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f5868",
      "PARAM",
      [
        "storage",
        "00c004d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f5/007f5814.md#insn-007f5854) · [`007f5860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f5/007f5814.md#insn-007f5860) · [`007f5868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f5/007f5814.md#insn-007f5868)
- 新版 `007f5854`（命令位置の公開資料なし） · `007f5860`（命令位置の公開資料なし） · `007f5868`（命令位置の公開資料なし）

~~~diff
- 007f5854 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007f5854 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f5854 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007f5854 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007f5854 bytes 083d45f9
+ 007f5854 bytes 085d45f9
- 007f5860 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007f5860 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f5860 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f5860 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f5860 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007f5860 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f5860 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f5860 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f5860 bytes 21203991
+ 007f5860 bytes 21603a91
- 007f5868 ["COPY", "tmp:0:8", ["const:488:8"]]
- 007f5868 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007f5868 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007f5868 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007f5868 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 007f5868 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007f5868 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007f5868 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007f5868 bytes 42201291
+ 007f5868 bytes 42601391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3f8db7162f0acfab9de191e8785e085"></a>

### [`007f61cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f61cc.md) → [`007f61cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f6/007f61cc.md) FUN_007f61cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007f7288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f7/007f7288.md) · 呼出先 13件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`0080038c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/0080038c.md) [`00800390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800390.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`007f7288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f7288.md) · 呼出先 13件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`0080038c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/0080038c.md) [`00800390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/00800390.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.99% / 新版 92.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f6328",
      "incomplete_value": false,
      "site": "007f6328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6328",
      "incomplete_value": false,
      "site": "007f6328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
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
      "definition_site": "007f63b0",
      "incomplete_value": true,
      "site": "007f63b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "007f63b0",
      "incomplete_value": true,
      "site": "007f63b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "007f620c",
      "incomplete_value": true,
      "site": "007f620c",
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
      "definition_site": "007f620c",
      "incomplete_value": true,
      "site": "007f620c",
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
      "007f6208",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f6214",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f621c",
      "PARAM",
      [
        "storage",
        "00c00488",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f6208",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f6214",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f621c",
      "PARAM",
      [
        "storage",
        "00c004d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f61cc.md#insn-007f6208) · [`007f6214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f61cc.md#insn-007f6214) · [`007f621c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f61cc.md#insn-007f621c)
- 新版 `007f6208`（命令位置の公開資料なし） · `007f6214`（命令位置の公開資料なし） · `007f621c`（命令位置の公開資料なし）

~~~diff
- 007f6208 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007f6208 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f6208 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007f6208 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007f6208 bytes 083d45f9
+ 007f6208 bytes 085d45f9
- 007f6214 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007f6214 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f6214 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f6214 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f6214 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007f6214 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f6214 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f6214 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f6214 bytes 21203991
+ 007f6214 bytes 21603a91
- 007f621c ["COPY", "tmp:0:8", ["const:488:8"]]
- 007f621c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007f621c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007f621c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007f621c ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 007f621c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007f621c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007f621c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007f621c bytes 42201291
+ 007f621c bytes 42601391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-595f7ebe8ca38f9de64162164fcafe15"></a>

### [`007f64ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f64ac.md) → [`007f64ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f6/007f64ac.md) FUN_007f64ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007f7288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f7/007f7288.md) · 呼出先 16件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`00800530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800530.md) [`00800534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800534.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`007f7288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f7288.md) · 呼出先 16件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`00800530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/00800530.md) [`00800534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/00800534.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.69% / 新版 96.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f6664",
      "incomplete_value": false,
      "site": "007f6664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6664",
      "incomplete_value": false,
      "site": "007f6664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007f64e0",
      "incomplete_value": true,
      "site": "007f64e0",
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
      "definition_site": "007f64e0",
      "incomplete_value": true,
      "site": "007f64e0",
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
      "definition_site": "007f64e8",
      "incomplete_value": false,
      "site": "007f64fc",
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
      "definition_site": "007f64e8",
      "incomplete_value": false,
      "site": "007f64fc",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007f64dc",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f64e8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f64f0",
      "PARAM",
      [
        "storage",
        "00c00488",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f64dc",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f64e8",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f64f0",
      "PARAM",
      [
        "storage",
        "00c004d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f64dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f64ac.md#insn-007f64dc) · [`007f64e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f64ac.md#insn-007f64e8) · [`007f64f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f64ac.md#insn-007f64f0)
- 新版 `007f64dc`（命令位置の公開資料なし） · `007f64e8`（命令位置の公開資料なし） · `007f64f0`（命令位置の公開資料なし）

~~~diff
- 007f64dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007f64dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f64dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007f64dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007f64dc bytes 083d45f9
+ 007f64dc bytes 085d45f9
- 007f64e8 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007f64e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f64e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f64e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f64e8 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007f64e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f64e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f64e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f64e8 bytes 21203991
+ 007f64e8 bytes 21603a91
- 007f64f0 ["COPY", "tmp:0:8", ["const:488:8"]]
- 007f64f0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007f64f0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007f64f0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007f64f0 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 007f64f0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007f64f0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007f64f0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007f64f0 bytes 42201291
+ 007f64f0 bytes 42601391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-137f13998dcb033f9df0fc812c55978e"></a>

### [`007f6804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f6804.md) → [`007f6804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f6/007f6804.md) FUN_007f6804

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007f7288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f7/007f7288.md) · 呼出先 12件 [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`00800640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800640.md) [`00800644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800644.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00883e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883e08.md)
- 新版 呼出元 1件 [`007f7288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f7288.md) · 呼出先 12件 [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`00800640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/00800640.md) [`00800644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/00800644.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00883e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883e08.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.52% / 新版 92.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f6898",
      "incomplete_value": false,
      "site": "007f6898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6898",
      "incomplete_value": false,
      "site": "007f6898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
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
      "definition_site": "007f693c",
      "incomplete_value": false,
      "site": "007f6940",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:d80:8"
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
      "definition_site": "007f693c",
      "incomplete_value": false,
      "site": "007f6940",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:d30:8"
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f6844",
      "incomplete_value": true,
      "site": "007f6848",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "007f6844",
      "incomplete_value": true,
      "site": "007f6848",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "007f6824",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f6830",
      "PARAM",
      [
        "storage",
        "00c00488",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f6840",
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
      "007f6824",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f6830",
      "PARAM",
      [
        "storage",
        "00c004d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f6840",
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

- 旧版 [`007f6824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f6804.md#insn-007f6824) · [`007f6830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f6804.md#insn-007f6830) · [`007f6840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f6804.md#insn-007f6840)
- 新版 `007f6824`（命令位置の公開資料なし） · `007f6830`（命令位置の公開資料なし） · `007f6840`（命令位置の公開資料なし）

~~~diff
- 007f6824 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007f6824 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f6824 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f6824 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f6824 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007f6824 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f6824 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f6824 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f6824 bytes 21203991
+ 007f6824 bytes 21603a91
- 007f6830 ["COPY", "tmp:0:8", ["const:488:8"]]
- 007f6830 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007f6830 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007f6830 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007f6830 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 007f6830 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007f6830 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007f6830 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007f6830 bytes 42201291
+ 007f6830 bytes 42601391
- 007f6840 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007f6840 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f6840 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007f6840 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007f6840 bytes 083d45f9
+ 007f6840 bytes 085d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c02b5cea88dedfaf6968944b0c822ff"></a>

### [`007f6a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f6a14.md) → [`007f6a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f6/007f6a14.md) FUN_007f6a14

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007f7288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f7/007f7288.md) · 呼出先 17件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`007f3f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f3/007f3f40.md) [`00800720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800720.md) [`00800724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800724.md)
- 新版 呼出元 1件 [`007f7288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f7288.md) · 呼出先 17件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`007f3f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3f40.md) [`00800720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/00800720.md) [`00800724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/00800724.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.94% / 新版 97.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f6d90",
      "incomplete_value": false,
      "site": "007f6d90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6d90",
      "incomplete_value": false,
      "site": "007f6d90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007f6a4c",
      "incomplete_value": true,
      "site": "007f6a4c",
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
      "definition_site": "007f6a4c",
      "incomplete_value": true,
      "site": "007f6a4c",
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
      "definition_site": "007f6a54",
      "incomplete_value": false,
      "site": "007f6a68",
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
      "definition_site": "007f6a54",
      "incomplete_value": false,
      "site": "007f6a68",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007f6a48",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f6a54",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f6a5c",
      "PARAM",
      [
        "storage",
        "00c00488",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f6a48",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f6a54",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f6a5c",
      "PARAM",
      [
        "storage",
        "00c004d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f6a14.md#insn-007f6a48) · [`007f6a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f6a14.md#insn-007f6a54) · [`007f6a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f6/007f6a14.md#insn-007f6a5c)
- 新版 `007f6a48`（命令位置の公開資料なし） · `007f6a54`（命令位置の公開資料なし） · `007f6a5c`（命令位置の公開資料なし）

~~~diff
- 007f6a48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007f6a48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f6a48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007f6a48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007f6a48 bytes 083d45f9
+ 007f6a48 bytes 085d45f9
- 007f6a54 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007f6a54 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f6a54 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f6a54 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f6a54 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007f6a54 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f6a54 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f6a54 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f6a54 bytes 21203991
+ 007f6a54 bytes 21603a91
- 007f6a5c ["COPY", "tmp:0:8", ["const:488:8"]]
- 007f6a5c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007f6a5c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007f6a5c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007f6a5c ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 007f6a5c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007f6a5c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007f6a5c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007f6a5c bytes 42201291
+ 007f6a5c bytes 42601391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fe0c19b18785da0ab7c15a65c9a6dec"></a>

### [`007f8354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8354.md) → [`007f8354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f8354.md) FUN_007f8354

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007fa718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fa718.md) · 呼出先 16件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00446190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446190.md) [`00447378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447378.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`007e7970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e7/007e7970.md)
- 新版 呼出元 1件 [`007fa718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fa718.md) · 呼出先 16件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00446190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446190.md) [`00447378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447378.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`007e7970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e7/007e7970.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.40% / 新版 99.40%

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
      "definition_site": "007f840c",
      "incomplete_value": true,
      "site": "007f840c",
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
      "definition_site": "007f840c",
      "incomplete_value": true,
      "site": "007f840c",
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f8414",
      "incomplete_value": false,
      "site": "007f8424",
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
      "definition_site": "007f8414",
      "incomplete_value": false,
      "site": "007f8424",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f841c",
      "incomplete_value": false,
      "site": "007f8424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f841c",
      "incomplete_value": false,
      "site": "007f8424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "007f8408",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f8414",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f841c",
      "PARAM",
      [
        "storage",
        "00c00488",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f8408",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f8414",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f841c",
      "PARAM",
      [
        "storage",
        "00c004d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8354.md#insn-007f8408) · [`007f8414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8354.md#insn-007f8414) · [`007f841c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8354.md#insn-007f841c)
- 新版 `007f8408`（命令位置の公開資料なし） · `007f8414`（命令位置の公開資料なし） · `007f841c`（命令位置の公開資料なし）

~~~diff
- 007f8408 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007f8408 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f8408 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007f8408 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007f8408 bytes 003d45f9
+ 007f8408 bytes 005d45f9
- 007f8414 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007f8414 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f8414 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f8414 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f8414 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007f8414 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f8414 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f8414 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f8414 bytes 21203991
+ 007f8414 bytes 21603a91
- 007f841c ["COPY", "tmp:0:8", ["const:488:8"]]
- 007f841c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007f841c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007f841c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007f841c ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 007f841c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007f841c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007f841c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007f841c bytes 42201291
+ 007f841c bytes 42601391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f7b9bd771f6c4df47af527d01198a3a"></a>

### [`007f8b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8b0c.md) → [`007f8b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f8b0c.md) FUN_007f8b0c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 20件 [`0044b898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b898.md) [`0044b8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8a0.md) [`0044b8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8b0.md) [`0044beb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044beb4.md) [`0044c1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c1dc.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 20件 [`0044b898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b898.md) [`0044b8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8a0.md) [`0044b8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8b0.md) [`0044beb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044beb4.md) [`0044c1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.82% / 新版 97.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f8c5c",
      "incomplete_value": true,
      "site": "007f8c70",
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
                "const:a8b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8c5c",
      "incomplete_value": true,
      "site": "007f8c70",
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
                "const:a00:8"
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
      "definition_site": "007f8c08",
      "incomplete_value": true,
      "site": "007f8c08",
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
      "definition_site": "007f8c08",
      "incomplete_value": true,
      "site": "007f8c08",
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
    "ordinal": 12,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f8c10",
      "incomplete_value": false,
      "site": "007f8c20",
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
      "definition_site": "007f8c10",
      "incomplete_value": false,
      "site": "007f8c20",
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
      "007f8c04",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f8c10",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f8c18",
      "PARAM",
      [
        "storage",
        "00be8e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f8c04",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f8c10",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f8c18",
      "PARAM",
      [
        "storage",
        "00be8ea8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8b0c.md#insn-007f8c04) · [`007f8c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8b0c.md#insn-007f8c10) · [`007f8c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8b0c.md#insn-007f8c18)
- 新版 `007f8c04`（命令位置の公開資料なし） · `007f8c10`（命令位置の公開資料なし） · `007f8c18`（命令位置の公開資料なし）

~~~diff
- 007f8c04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007f8c04 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f8c04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007f8c04 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007f8c04 bytes 003d45f9
+ 007f8c04 bytes 005d45f9
- 007f8c10 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007f8c10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f8c10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f8c10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f8c10 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007f8c10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f8c10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f8c10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f8c10 bytes 21203991
+ 007f8c10 bytes 21603a91
- 007f8c18 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 007f8c18 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007f8c18 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007f8c18 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007f8c18 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 007f8c18 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007f8c18 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007f8c18 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007f8c18 bytes 42603991
+ 007f8c18 bytes 42a03a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-386309b98e9a2e167375ee4626b04f39"></a>

### [`007f8ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8ecc.md) → [`007f8ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f8ecc.md) FUN_007f8ecc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007f8b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8b0c.md) [`00adcc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adcc94.md) · 呼出先 17件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md)
- 新版 呼出元 2件 [`007f8b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f8b0c.md) [`00adccd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adccd8.md) · 呼出先 17件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_destination` 7件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f8f28",
      "incomplete_value": true,
      "site": "007f8f40",
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
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:8d5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8f28",
      "incomplete_value": true,
      "site": "007f8f40",
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
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:8d7:8"
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
      "definition_site": "007f8f48",
      "incomplete_value": true,
      "site": "007f8f58",
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
                "const:84b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f8f48",
      "incomplete_value": true,
      "site": "007f8f58",
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
                "const:7c0:8"
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
      "definition_site": "007f9184",
      "incomplete_value": true,
      "site": "007f9184",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f9184",
      "incomplete_value": true,
      "site": "007f9184",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9aa:8"
              ]
            ]
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
      "007f8f0c",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "007f8f28",
      "READ",
      [
        "storage",
        "0029b8d7",
        null,
        "string"
      ]
    ],
    [
      "007f8f48",
      "READ",
      [
        "storage",
        "0029d7c0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f8f0c",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "007f8f28",
      "READ",
      [
        "storage",
        "0029b8d5",
        null,
        "string"
      ]
    ],
    [
      "007f8f48",
      "READ",
      [
        "storage",
        "0029d84b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f8f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8ecc.md#insn-007f8f04) · [`007f8f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8ecc.md#insn-007f8f20) · [`007f8f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8ecc.md#insn-007f8f38)
- 新版 `007f8f04`（命令位置の公開資料なし） · `007f8f20`（命令位置の公開資料なし） · `007f8f38`（命令位置の公開資料なし）

~~~diff
- 007f8f04 ["COPY", "tmp:0:8", ["const:38:8"]]
- 007f8f04 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 007f8f04 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 007f8f04 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 007f8f04 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 007f8f04 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 007f8f04 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 007f8f04 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 007f8f04 bytes 39e30091
+ 007f8f04 bytes 39e30191
- 007f8f20 ["COPY", "tmp:0:8", ["const:8d7:8"]]
- 007f8f20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f8f20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f8f20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f8f20 ["COPY", "tmp:0:8", ["const:8d5:8"]]
+ 007f8f20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8f20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f8f20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f8f20 bytes 085d2391
+ 007f8f20 bytes 08552391
- 007f8f38 ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 007f8f38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f8f38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f8f38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f8f38 ["COPY", "tmp:0:8", ["const:84b:8"]]
+ 007f8f38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f8f38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f8f38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f8f38 bytes 29011f91
+ 007f8f38 bytes 292d2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-641c962e9f63aee4d5a12b8c46a14bf7"></a>

### [`007f95f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f95f4.md) → [`007f95f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f95f4.md) FUN_007f95f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 9件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00448e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448e7c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044c80c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c80c.md) [`0044d1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d1dc.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 9件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00448e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448e7c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044c80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c80c.md) [`0044d1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d1dc.md)

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
      "definition_site": "007f9640",
      "incomplete_value": true,
      "site": "007f9644",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "007f9640",
      "incomplete_value": true,
      "site": "007f9644",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f962c",
      "incomplete_value": false,
      "site": "007f9644",
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
      "definition_site": "007f962c",
      "incomplete_value": false,
      "site": "007f9644",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f9638",
      "incomplete_value": false,
      "site": "007f9644",
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
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f9638",
      "incomplete_value": false,
      "site": "007f9644",
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
            "const:e58:8"
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
      "007f962c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f9630",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f9638",
      "PARAM",
      [
        "storage",
        "00be8e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f962c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f9630",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f9638",
      "PARAM",
      [
        "storage",
        "00be8ea8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f962c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f95f4.md#insn-007f962c) · [`007f9630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f95f4.md#insn-007f9630) · [`007f9638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f95f4.md#insn-007f9638)
- 新版 `007f962c`（命令位置の公開資料なし） · `007f9630`（命令位置の公開資料なし） · `007f9638`（命令位置の公開資料なし）

~~~diff
- 007f962c ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007f962c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f962c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f962c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f962c ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007f962c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f962c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f962c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f962c bytes 21203991
+ 007f962c bytes 21603a91
- 007f9630 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007f9630 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f9630 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007f9630 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007f9630 bytes 083d45f9
+ 007f9630 bytes 085d45f9
- 007f9638 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 007f9638 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007f9638 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007f9638 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007f9638 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 007f9638 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007f9638 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007f9638 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007f9638 bytes 42603991
+ 007f9638 bytes 42a03a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9deff51f35514fcc7205262e6ff1535e"></a>

### [`007f99cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f99cc.md) → [`007f99cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f99cc.md) FUN_007f99cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 23件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`007f7288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f7/007f7288.md) [`00805f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00805/00805f2c.md) [`008070c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/008070c0.md) [`008070c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/008070c4.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 23件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`007f7288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f7288.md) [`00805f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00805/00805f2c.md) [`008070c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/008070c0.md) [`008070c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/008070c4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 89.94% / 新版 89.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007f9a08",
      "incomplete_value": false,
      "site": "007f9a08",
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
      "definition_site": "007f9a08",
      "incomplete_value": false,
      "site": "007f9a08",
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
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f9a00",
      "incomplete_value": true,
      "site": "007f9a08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "007f9a00",
      "incomplete_value": true,
      "site": "007f9a08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007f9a0c",
      "incomplete_value": false,
      "site": "007f9a0c",
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
      "definition_site": "007f9a0c",
      "incomplete_value": false,
      "site": "007f9a0c",
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
      "007f9a00",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f9a04",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "007f9a08",
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
      "007f9a00",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f9a04",
      "READ",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "007f9a08",
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

- 旧版 [`007f9a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f99cc.md#insn-007f9a08) · [`007f9a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f99cc.md#insn-007f9a0c) · [`007f9a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f99cc.md#insn-007f9a24)
- 新版 `007f9a08`（命令位置の公開資料なし） · `007f9a0c`（命令位置の公開資料なし） · `007f9a24`（命令位置の公開資料なし）

~~~diff
- 007f9a08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 007f9a08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 007f9a08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa8:8"]]
+ 007f9a08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 007f9a08 bytes 093505f9
+ 007f9a08 bytes 095505f9
- 007f9a0c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
- 007f9a0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 007f9a0c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ab8:8"]]
+ 007f9a0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 007f9a0c bytes ca3e05f9
+ 007f9a0c bytes ca5e05f9
- 007f9a24 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
- 007f9a24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 007f9a24 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ab8:8"]]
+ 007f9a24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 007f9a24 bytes d43e05f9
+ 007f9a24 bytes d45e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1fbf60855495d1ec01fde1ef0c2a0ab"></a>

### [`007f9cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f9cd4.md) → [`007f9cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f9cd4.md) FUN_007f9cd4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004296cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004296cc.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ad74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046ad74.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004296cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/004296cc.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ad74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046ad74.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.06% / 新版 98.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f9d7c",
      "incomplete_value": true,
      "site": "007f9d7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:958:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f9d7c",
      "incomplete_value": true,
      "site": "007f9d7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8be:8"
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
      "definition_site": "007f9f64",
      "incomplete_value": true,
      "site": "007f9f64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:958:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f9f64",
      "incomplete_value": true,
      "site": "007f9f64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8be:8"
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
      "definition_site": "007f9fa8",
      "incomplete_value": true,
      "site": "007f9fa8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:958:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f9fa8",
      "incomplete_value": true,
      "site": "007f9fa8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8be:8"
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
      "007f9d68",
      "READ",
      [
        "storage",
        "002a78be",
        null,
        "string"
      ]
    ],
    [
      "007f9f50",
      "READ",
      [
        "storage",
        "002a78be",
        null,
        "string"
      ]
    ],
    [
      "007f9f58",
      "DATA",
      [
        "storage",
        "00298f20",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f9d68",
      "READ",
      [
        "storage",
        "002a7958",
        null,
        "string"
      ]
    ],
    [
      "007f9f50",
      "READ",
      [
        "storage",
        "002a7958",
        null,
        "string"
      ]
    ],
    [
      "007f9f58",
      "DATA",
      [
        "storage",
        "00298f20",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f9d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f9cd4.md#insn-007f9d60) · [`007f9f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f9cd4.md#insn-007f9f4c) · [`007f9f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f9cd4.md#insn-007f9f90)
- 新版 `007f9d60`（命令位置の公開資料なし） · `007f9f4c`（命令位置の公開資料なし） · `007f9f90`（命令位置の公開資料なし）

~~~diff
- 007f9d60 ["COPY", "tmp:0:8", ["const:8be:8"]]
- 007f9d60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f9d60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f9d60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f9d60 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 007f9d60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f9d60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f9d60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f9d60 bytes 08f92291
+ 007f9d60 bytes 08612591
- 007f9f4c ["COPY", "tmp:0:8", ["const:8be:8"]]
- 007f9f4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f9f4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f9f4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f9f4c ["COPY", "tmp:0:8", ["const:958:8"]]
+ 007f9f4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f9f4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f9f4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f9f4c bytes 29f92291
+ 007f9f4c bytes 29612591
- 007f9f90 ["COPY", "tmp:0:8", ["const:8be:8"]]
- 007f9f90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f9f90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f9f90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f9f90 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 007f9f90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f9f90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f9f90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f9f90 bytes 29f92291
+ 007f9f90 bytes 29612591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b71336e9793de0cd5951568da5c4355"></a>

### [`007fa718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fa718.md) → [`007fa718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fa718.md) FUN_007fa718

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 22件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00445044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445044.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 22件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00445044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445044.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.44% / 新版 98.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007fa734",
      "incomplete_value": true,
      "site": "007fa734",
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
      "definition_site": "007fa734",
      "incomplete_value": true,
      "site": "007fa734",
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
      "definition_site": "007fa74c",
      "incomplete_value": true,
      "site": "007fa758",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fa74c",
      "incomplete_value": true,
      "site": "007fa758",
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
            "const:488:8"
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
      "007fa730",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007fa744",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007fa74c",
      "PARAM",
      [
        "storage",
        "00c00488",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007fa730",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007fa744",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007fa74c",
      "PARAM",
      [
        "storage",
        "00c004d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fa730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fa718.md#insn-007fa730) · [`007fa744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fa718.md#insn-007fa744) · [`007fa74c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fa718.md#insn-007fa74c)
- 新版 `007fa730`（命令位置の公開資料なし） · `007fa744`（命令位置の公開資料なし） · `007fa74c`（命令位置の公開資料なし）

~~~diff
- 007fa730 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007fa730 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007fa730 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007fa730 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007fa730 bytes 083d45f9
+ 007fa730 bytes 085d45f9
- 007fa744 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007fa744 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007fa744 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007fa744 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007fa744 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007fa744 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007fa744 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007fa744 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007fa744 bytes 21203991
+ 007fa744 bytes 21603a91
- 007fa74c ["COPY", "tmp:0:8", ["const:488:8"]]
- 007fa74c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007fa74c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007fa74c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007fa74c ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 007fa74c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007fa74c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007fa74c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007fa74c bytes 42201291
+ 007fa74c bytes 42601391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ccd1566605b5a4d934c1b231606f726"></a>

### [`007fabf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fabf8.md) → [`007fabf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fabf8.md) FUN_007fabf8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`007e5fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e5/007e5fa4.md) [`007e7bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e7/007e7bcc.md) [`007eb8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007eb/007eb8f8.md) [`007fa918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fa918.md) [`007fb248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fb/007fb248.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 5件 [`007e5fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e5fa4.md) [`007e7bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e7/007e7bcc.md) [`007eb8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007eb/007eb8f8.md) [`007fa918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fa918.md) [`007fb248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb248.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "007fac04",
      "incomplete_value": false,
      "site": "007fac08",
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
      "definition_site": "007fac04",
      "incomplete_value": false,
      "site": "007fac08",
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
      "007fac04",
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
      "007fac04",
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

- 旧版 [`007fac04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fabf8.md#insn-007fac04)
- 新版 `007fac04`（命令位置の公開資料なし）

~~~diff
- 007fac04 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007fac04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007fac04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007fac04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007fac04 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007fac04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007fac04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007fac04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007fac04 bytes 000c0c91
+ 007fac04 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf362fb3cfbd213dab2051f15fbf673e"></a>

### [`007fae20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fae20.md) → [`007fae20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fae20.md) FUN_007fae20

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`007e555c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e5/007e555c.md) [`007e7d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e7/007e7d84.md) [`007f3c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f3/007f3c28.md) [`007f4120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f4/007f4120.md) [`007fac0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fac0c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 5件 [`007e555c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e555c.md) [`007e7d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e7/007e7d84.md) [`007f3c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3c28.md) [`007f4120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f4/007f4120.md) [`007fac0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fac0c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "007fae2c",
      "incomplete_value": false,
      "site": "007fae30",
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
      "definition_site": "007fae2c",
      "incomplete_value": false,
      "site": "007fae30",
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
      "007fae2c",
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
      "007fae2c",
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

- 旧版 [`007fae2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fae20.md#insn-007fae2c)
- 新版 `007fae2c`（命令位置の公開資料なし）

~~~diff
- 007fae2c ["COPY", "tmp:0:8", ["const:303:8"]]
- 007fae2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007fae2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007fae2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007fae2c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007fae2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007fae2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007fae2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007fae2c bytes 000c0c91
+ 007fae2c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-154423512d8043488c2ae08fea7acdc5"></a>

### [`007faea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007faea4.md) → [`007faea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007faea4.md) FUN_007faea4

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
      "definition_site": "007faea8",
      "incomplete_value": false,
      "site": "007faeac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007faea8",
      "incomplete_value": false,
      "site": "007faeac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
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
      "007faeac",
      "DATA",
      [
        "storage",
        "00c003a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007faeac",
      "DATA",
      [
        "storage",
        "00c003f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007faea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007faea4.md#insn-007faea8)
- 新版 `007faea8`（命令位置の公開資料なし）

~~~diff
- 007faea8 ["COPY", "tmp:0:8", ["const:3a8:8"]]
- 007faea8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007faea8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007faea8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007faea8 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 007faea8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007faea8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007faea8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007faea8 bytes 08a10e91
+ 007faea8 bytes 08e10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3137b417a3dd9290daeb3c33a0dfc5c"></a>

### [`007faeb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007faeb4.md) → [`007faeb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007faeb4.md) FUN_007faeb4

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
      "definition_site": "007faec4",
      "incomplete_value": false,
      "site": "007faecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007faec4",
      "incomplete_value": false,
      "site": "007faecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
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
      "007faecc",
      "DATA",
      [
        "storage",
        "00c003a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007faecc",
      "DATA",
      [
        "storage",
        "00c003f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007faec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007faeb4.md#insn-007faec4)
- 新版 `007faec4`（命令位置の公開資料なし）

~~~diff
- 007faec4 ["COPY", "tmp:0:8", ["const:3a8:8"]]
- 007faec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007faec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007faec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007faec4 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 007faec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007faec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007faec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007faec4 bytes 08a10e91
+ 007faec4 bytes 08e10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58f642bbc99e85069b42c5a2c461dbbd"></a>

### [`007fafac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fafac.md) → [`007fafac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fafac.md) FUN_007fafac

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
      "definition_site": "007fafb0",
      "incomplete_value": false,
      "site": "007fafb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:448:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fafb0",
      "incomplete_value": false,
      "site": "007fafb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
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
      "007fafb4",
      "DATA",
      [
        "storage",
        "00c003f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007fafb4",
      "DATA",
      [
        "storage",
        "00c00448",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fafac.md#insn-007fafb0)
- 新版 `007fafb0`（命令位置の公開資料なし）

~~~diff
- 007fafb0 ["COPY", "tmp:0:8", ["const:3f8:8"]]
- 007fafb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fafb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fafb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fafb0 ["COPY", "tmp:0:8", ["const:448:8"]]
+ 007fafb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fafb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fafb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fafb0 bytes 08e10f91
+ 007fafb0 bytes 08211191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b7eace787ceb3d484c8d850c6592a7b"></a>

### [`007fb170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fb/007fb170.md) → [`007fb170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb170.md) FUN_007fb170

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
      "definition_site": "007fb174",
      "incomplete_value": false,
      "site": "007fb178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fb174",
      "incomplete_value": false,
      "site": "007fb178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:448:8"
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
      "007fb178",
      "DATA",
      [
        "storage",
        "00c00448",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fb178",
      "DATA",
      [
        "storage",
        "00c00498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fb174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fb/007fb170.md#insn-007fb174)
- 新版 `007fb174`（命令位置の公開資料なし）

~~~diff
- 007fb174 ["COPY", "tmp:0:8", ["const:448:8"]]
- 007fb174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fb174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fb174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fb174 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 007fb174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fb174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fb174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fb174 bytes 08211191
+ 007fb174 bytes 08611291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8a255880cf797b62d199a077ab2ca72"></a>

### [`007fb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fb/007fb180.md) → [`007fb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb180.md) FUN_007fb180

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
      "definition_site": "007fb190",
      "incomplete_value": false,
      "site": "007fb198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fb190",
      "incomplete_value": false,
      "site": "007fb198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:448:8"
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
      "007fb198",
      "DATA",
      [
        "storage",
        "00c00448",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fb198",
      "DATA",
      [
        "storage",
        "00c00498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fb190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fb/007fb180.md#insn-007fb190)
- 新版 `007fb190`（命令位置の公開資料なし）

~~~diff
- 007fb190 ["COPY", "tmp:0:8", ["const:448:8"]]
- 007fb190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fb190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fb190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fb190 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 007fb190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fb190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fb190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fb190 bytes 08211191
+ 007fb190 bytes 08611291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4486e47b5cee097e359265b4aafaf09"></a>

### [`007fb65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fb/007fb65c.md) → [`007fb65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb65c.md) FUN_007fb65c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007ef4ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ef/007ef4ec.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`007ef4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ef/007ef4ec.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "007fb668",
      "incomplete_value": false,
      "site": "007fb66c",
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
      "definition_site": "007fb668",
      "incomplete_value": false,
      "site": "007fb66c",
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
      "007fb668",
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
      "007fb668",
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

- 旧版 [`007fb668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fb/007fb65c.md#insn-007fb668)
- 新版 `007fb668`（命令位置の公開資料なし）

~~~diff
- 007fb668 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007fb668 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007fb668 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007fb668 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007fb668 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007fb668 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007fb668 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007fb668 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007fb668 bytes 000c0c91
+ 007fb668 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a5fd56b79a5bc70e759197eac4b388e"></a>

### [`007ff11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff11c.md) → [`007ff11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff11c.md) FUN_007ff11c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ff140",
      "incomplete_value": true,
      "site": "007ff144",
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
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff140",
      "incomplete_value": true,
      "site": "007ff144",
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
            "const:4b0:8"
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
      "007ff144",
      "DATA",
      [
        "storage",
        "00c004b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff144",
      "DATA",
      [
        "storage",
        "00c00500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff11c.md#insn-007ff140)
- 新版 `007ff140`（命令位置の公開資料なし）

~~~diff
- 007ff140 ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 007ff140 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ff140 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ff140 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ff140 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 007ff140 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff140 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff140 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ff140 bytes 08c11291
+ 007ff140 bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fc8e06a98b5b12b24761a42b6a21f0b"></a>

### [`007ff15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff15c.md) → [`007ff15c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff15c.md) FUN_007ff15c

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
      "definition_site": "007ff160",
      "incomplete_value": false,
      "site": "007ff164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff160",
      "incomplete_value": false,
      "site": "007ff164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
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
      "007ff164",
      "DATA",
      [
        "storage",
        "00c004b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff164",
      "DATA",
      [
        "storage",
        "00c00500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff15c.md#insn-007ff160)
- 新版 `007ff160`（命令位置の公開資料なし）

~~~diff
- 007ff160 ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 007ff160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ff160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ff160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ff160 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 007ff160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ff160 bytes 08c11291
+ 007ff160 bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc2c4c802eb11509e58e2e607fda967a"></a>

### [`007ff1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff1f0.md) → [`007ff1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff1f0.md) FUN_007ff1f0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ff214",
      "incomplete_value": true,
      "site": "007ff214",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff214",
      "incomplete_value": true,
      "site": "007ff214",
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
            "const:530:8"
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
      "007ff214",
      "DATA",
      [
        "storage",
        "00c00530",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff214",
      "DATA",
      [
        "storage",
        "00c00580",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff1f0.md#insn-007ff210)
- 新版 `007ff210`（命令位置の公開資料なし）

~~~diff
- 007ff210 ["COPY", "tmp:0:8", ["const:530:8"]]
- 007ff210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ff210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ff210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ff210 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 007ff210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ff210 bytes 08c11491
+ 007ff210 bytes 08011691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ee454d4c35fb8d1febd1f1ed5c0f62f"></a>

### [`007ff224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff224.md) → [`007ff224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff224.md) FUN_007ff224

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
      "definition_site": "007ff230",
      "incomplete_value": false,
      "site": "007ff230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff230",
      "incomplete_value": false,
      "site": "007ff230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:530:8"
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
      "007ff230",
      "DATA",
      [
        "storage",
        "00c00530",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff230",
      "DATA",
      [
        "storage",
        "00c00580",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff22c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff224.md#insn-007ff22c)
- 新版 `007ff22c`（命令位置の公開資料なし）

~~~diff
- 007ff22c ["COPY", "tmp:0:8", ["const:530:8"]]
- 007ff22c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ff22c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ff22c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ff22c ["COPY", "tmp:0:8", ["const:580:8"]]
+ 007ff22c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ff22c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ff22c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ff22c bytes 29c11491
+ 007ff22c bytes 29011691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9fe270c8a4f1bb8d6a8a4ac127f671b"></a>

### [`007ff2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff2cc.md) → [`007ff2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff2cc.md) FUN_007ff2cc

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
      "definition_site": "007ff2d8",
      "incomplete_value": false,
      "site": "007ff2e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff2d8",
      "incomplete_value": false,
      "site": "007ff2e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
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
      "007ff2e4",
      "DATA",
      [
        "storage",
        "00c005b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff2e4",
      "DATA",
      [
        "storage",
        "00c00600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff2d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff2cc.md#insn-007ff2d8)
- 新版 `007ff2d8`（命令位置の公開資料なし）

~~~diff
- 007ff2d8 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 007ff2d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007ff2d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007ff2d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007ff2d8 ["COPY", "tmp:0:8", ["const:600:8"]]
+ 007ff2d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007ff2d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007ff2d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007ff2d8 bytes 4ac11691
+ 007ff2d8 bytes 4a011891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0ab08a2a59be3fc746d236bb5857798"></a>

### [`007ff36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff36c.md) → [`007ff36c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff36c.md) FUN_007ff36c

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
      "definition_site": "007ff398",
      "incomplete_value": false,
      "site": "007ff398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff398",
      "incomplete_value": false,
      "site": "007ff398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
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
      "007ff398",
      "DATA",
      [
        "storage",
        "00c005b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff398",
      "DATA",
      [
        "storage",
        "00c00600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff36c.md#insn-007ff390)
- 新版 `007ff390`（命令位置の公開資料なし）

~~~diff
- 007ff390 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 007ff390 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ff390 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ff390 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ff390 ["COPY", "tmp:0:8", ["const:600:8"]]
+ 007ff390 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff390 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff390 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ff390 bytes 08c11691
+ 007ff390 bytes 08011891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d219cc13a07a40e302916c79654bb87"></a>

### [`007ff3f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff3f4.md) → [`007ff3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff3f4.md) FUN_007ff3f4

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
      "definition_site": "007ff410",
      "incomplete_value": false,
      "site": "007ff410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff410",
      "incomplete_value": false,
      "site": "007ff410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
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
      "007ff410",
      "DATA",
      [
        "storage",
        "00c005b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff410",
      "DATA",
      [
        "storage",
        "00c00600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff40c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff3f4.md#insn-007ff40c)
- 新版 `007ff40c`（命令位置の公開資料なし）

~~~diff
- 007ff40c ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 007ff40c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ff40c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ff40c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ff40c ["COPY", "tmp:0:8", ["const:600:8"]]
+ 007ff40c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ff40c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ff40c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ff40c bytes 29c11691
+ 007ff40c bytes 29011891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bde3fe0e6dc326f7d63e7709ff4abc74"></a>

### [`007ff598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff598.md) → [`007ff598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff598.md) FUN_007ff598

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
      "definition_site": "007ff5a4",
      "incomplete_value": false,
      "site": "007ff5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff5a4",
      "incomplete_value": false,
      "site": "007ff5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:630:8"
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
      "007ff5b0",
      "DATA",
      [
        "storage",
        "00c00630",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff5b0",
      "DATA",
      [
        "storage",
        "00c00680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff5a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff598.md#insn-007ff5a4)
- 新版 `007ff5a4`（命令位置の公開資料なし）

~~~diff
- 007ff5a4 ["COPY", "tmp:0:8", ["const:630:8"]]
- 007ff5a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007ff5a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007ff5a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007ff5a4 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 007ff5a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007ff5a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007ff5a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007ff5a4 bytes 4ac11891
+ 007ff5a4 bytes 4a011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd0d0375f333a40187d2e9da0bbc6968"></a>

### [`007ff5dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff5dc.md) → [`007ff5dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff5dc.md) FUN_007ff5dc

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
      "definition_site": "007ff5f4",
      "incomplete_value": false,
      "site": "007ff600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff5f4",
      "incomplete_value": false,
      "site": "007ff600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:630:8"
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
      "007ff600",
      "DATA",
      [
        "storage",
        "00c00630",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff600",
      "DATA",
      [
        "storage",
        "00c00680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff5f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff5dc.md#insn-007ff5f4)
- 新版 `007ff5f4`（命令位置の公開資料なし）

~~~diff
- 007ff5f4 ["COPY", "tmp:0:8", ["const:630:8"]]
- 007ff5f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ff5f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ff5f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ff5f4 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 007ff5f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff5f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff5f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ff5f4 bytes 08c11891
+ 007ff5f4 bytes 08011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc54c9d45ef1d9a40a11c972a00f21de"></a>

### [`007ff638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff638.md) → [`007ff638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff638.md) FUN_007ff638

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
      "definition_site": "007ff664",
      "incomplete_value": false,
      "site": "007ff664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff664",
      "incomplete_value": false,
      "site": "007ff664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:630:8"
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
      "007ff664",
      "DATA",
      [
        "storage",
        "00c00630",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff664",
      "DATA",
      [
        "storage",
        "00c00680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff638.md#insn-007ff65c)
- 新版 `007ff65c`（命令位置の公開資料なし）

~~~diff
- 007ff65c ["COPY", "tmp:0:8", ["const:630:8"]]
- 007ff65c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ff65c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ff65c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ff65c ["COPY", "tmp:0:8", ["const:680:8"]]
+ 007ff65c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff65c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff65c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ff65c bytes 08c11891
+ 007ff65c bytes 08011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b23ff9d3fd502c414358991b638a21be"></a>

### [`007ff6c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff6c0.md) → [`007ff6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff6c0.md) FUN_007ff6c0

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
      "definition_site": "007ff6dc",
      "incomplete_value": false,
      "site": "007ff6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff6dc",
      "incomplete_value": false,
      "site": "007ff6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:630:8"
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
      "007ff6dc",
      "DATA",
      [
        "storage",
        "00c00630",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff6dc",
      "DATA",
      [
        "storage",
        "00c00680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff6c0.md#insn-007ff6d8)
- 新版 `007ff6d8`（命令位置の公開資料なし）

~~~diff
- 007ff6d8 ["COPY", "tmp:0:8", ["const:630:8"]]
- 007ff6d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ff6d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ff6d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ff6d8 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 007ff6d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ff6d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ff6d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ff6d8 bytes 29c11891
+ 007ff6d8 bytes 29011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0baba31be6b8c0a08606d36e07eec97"></a>

### [`007ff834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff834.md) → [`007ff834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff834.md) FUN_007ff834

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
      "definition_site": "007ff858",
      "incomplete_value": false,
      "site": "007ff858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff858",
      "incomplete_value": false,
      "site": "007ff858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
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
      "007ff858",
      "DATA",
      [
        "storage",
        "00c006b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff858",
      "DATA",
      [
        "storage",
        "00c00700",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff834.md#insn-007ff854)
- 新版 `007ff854`（命令位置の公開資料なし）

~~~diff
- 007ff854 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 007ff854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ff854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ff854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ff854 ["COPY", "tmp:0:8", ["const:700:8"]]
+ 007ff854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ff854 bytes 08c11a91
+ 007ff854 bytes 08011c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c18c0ebe9ce9e3f3498213731804a9d"></a>

### [`007ff868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff868.md) → [`007ff868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff868.md) FUN_007ff868

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
      "definition_site": "007ff874",
      "incomplete_value": false,
      "site": "007ff874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff874",
      "incomplete_value": false,
      "site": "007ff874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
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
      "007ff874",
      "DATA",
      [
        "storage",
        "00c006b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff874",
      "DATA",
      [
        "storage",
        "00c00700",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff868.md#insn-007ff870)
- 新版 `007ff870`（命令位置の公開資料なし）

~~~diff
- 007ff870 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 007ff870 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ff870 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ff870 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ff870 ["COPY", "tmp:0:8", ["const:700:8"]]
+ 007ff870 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ff870 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ff870 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ff870 bytes 29c11a91
+ 007ff870 bytes 29011c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c2f21466b48d2f09a037b20cfb1e49f"></a>

### [`007ff92c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff92c.md) → [`007ff92c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff92c.md) FUN_007ff92c

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
      "definition_site": "007ff938",
      "incomplete_value": false,
      "site": "007ff938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff938",
      "incomplete_value": false,
      "site": "007ff938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:730:8"
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
      "007ff938",
      "DATA",
      [
        "storage",
        "00c00730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff938",
      "DATA",
      [
        "storage",
        "00c00780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff92c.md#insn-007ff934)
- 新版 `007ff934`（命令位置の公開資料なし）

~~~diff
- 007ff934 ["COPY", "tmp:0:8", ["const:730:8"]]
- 007ff934 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ff934 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ff934 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ff934 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 007ff934 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ff934 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ff934 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ff934 bytes 29c11c91
+ 007ff934 bytes 29011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-485d0da46502c3dab366d3f666fda183"></a>

### [`007ff948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff948.md) → [`007ff948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff948.md) FUN_007ff948

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 20件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007eafa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ea/007eafa4.md) [`007f3c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f3/007f3c28.md)
- 新版 呼出元 0件  · 呼出先 20件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`007eafa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ea/007eafa4.md) [`007f3c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3c28.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.38% / 新版 95.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ffa20",
      "incomplete_value": true,
      "site": "007ffa30",
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
                "const:953:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ffa20",
      "incomplete_value": true,
      "site": "007ffa30",
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
                "const:8c8:8"
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
      "definition_site": "007ffa34",
      "incomplete_value": true,
      "site": "007ffa34",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007ffa34",
      "incomplete_value": true,
      "site": "007ffa34",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ffb2c",
      "incomplete_value": false,
      "site": "007ffb2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ffb2c",
      "incomplete_value": false,
      "site": "007ffb2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
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
      "007ffa20",
      "READ",
      [
        "storage",
        "002a38c8",
        null,
        "string"
      ]
    ],
    [
      "007ffa24",
      "READ",
      [
        "storage",
        "002a38d7",
        null,
        "string"
      ]
    ],
    [
      "007ffb2c",
      "DATA",
      [
        "storage",
        "00c007a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ffa20",
      "READ",
      [
        "storage",
        "002a3953",
        null,
        "string"
      ]
    ],
    [
      "007ffa24",
      "READ",
      [
        "storage",
        "002a3962",
        null,
        "string"
      ]
    ],
    [
      "007ffb2c",
      "DATA",
      [
        "storage",
        "00c007f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ffa18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff948.md#insn-007ffa18) · [`007ffa1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ff948.md#insn-007ffa1c)
- 新版 `007ffa18`（命令位置の公開資料なし） · `007ffa1c`（命令位置の公開資料なし）

~~~diff
- 007ffa18 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 007ffa18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ffa18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ffa18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ffa18 ["COPY", "tmp:0:8", ["const:953:8"]]
+ 007ffa18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ffa18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ffa18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ffa18 bytes 08212391
+ 007ffa18 bytes 084d2591
- 007ffa1c ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 007ffa1c bytes 89d5ffb0
+ 007ffa1c ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 007ffa1c bytes 89d5ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd0c304288837664dd74da022e2772af"></a>

### [`007ffd20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ffd20.md) → [`007ffd20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ffd20.md) FUN_007ffd20

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
      "definition_site": "007ffd44",
      "incomplete_value": false,
      "site": "007ffd44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ffd44",
      "incomplete_value": false,
      "site": "007ffd44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
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
      "007ffd44",
      "DATA",
      [
        "storage",
        "00c007a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ffd44",
      "DATA",
      [
        "storage",
        "00c007f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ffd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ffd20.md#insn-007ffd40)
- 新版 `007ffd40`（命令位置の公開資料なし）

~~~diff
- 007ffd40 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 007ffd40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ffd40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ffd40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ffd40 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 007ffd40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ffd40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ffd40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ffd40 bytes 08811e91
+ 007ffd40 bytes 08c11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99b3bc515a7cbce40656025550b36b6a"></a>

### [`007ffd54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ffd54.md) → [`007ffd54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ffd54.md) FUN_007ffd54

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
      "definition_site": "007ffd60",
      "incomplete_value": false,
      "site": "007ffd60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ffd60",
      "incomplete_value": false,
      "site": "007ffd60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
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
      "007ffd60",
      "DATA",
      [
        "storage",
        "00c007a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ffd60",
      "DATA",
      [
        "storage",
        "00c007f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ffd5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ffd54.md#insn-007ffd5c)
- 新版 `007ffd5c`（命令位置の公開資料なし）

~~~diff
- 007ffd5c ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 007ffd5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ffd5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ffd5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ffd5c ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 007ffd5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ffd5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ffd5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ffd5c bytes 29811e91
+ 007ffd5c bytes 29c11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e836bdbf57cd5af503fd3d2340df66ac"></a>

### [`007ffde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ffde0.md) → [`007ffde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ffde0.md) FUN_007ffde0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007f4120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f4/007f4120.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`007f4120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f4/007f4120.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "007ffdec",
      "incomplete_value": false,
      "site": "007ffdf0",
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
      "definition_site": "007ffdec",
      "incomplete_value": false,
      "site": "007ffdf0",
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
      "007ffdec",
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
      "007ffdec",
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

- 旧版 [`007ffdec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ffde0.md#insn-007ffdec)
- 新版 `007ffdec`（命令位置の公開資料なし）

~~~diff
- 007ffdec ["COPY", "tmp:0:8", ["const:303:8"]]
- 007ffdec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007ffdec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007ffdec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007ffdec ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007ffdec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007ffdec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007ffdec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007ffdec bytes 000c0c91
+ 007ffdec bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7c2b8d2eb7a2d0368bd3cd3dce8314e"></a>

### [`007ffdf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ffdf8.md) → [`007ffdf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ffdf8.md) FUN_007ffdf8

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
      "definition_site": "007ffe1c",
      "incomplete_value": false,
      "site": "007ffe1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ffe1c",
      "incomplete_value": false,
      "site": "007ffe1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:830:8"
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
      "007ffe1c",
      "DATA",
      [
        "storage",
        "00c00830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ffe1c",
      "DATA",
      [
        "storage",
        "00c00880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ffe18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ffdf8.md#insn-007ffe18)
- 新版 `007ffe18`（命令位置の公開資料なし）

~~~diff
- 007ffe18 ["COPY", "tmp:0:8", ["const:830:8"]]
- 007ffe18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ffe18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ffe18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ffe18 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 007ffe18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ffe18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ffe18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ffe18 bytes 08c12091
+ 007ffe18 bytes 08012291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71fd82e09bed7989bc952dd373dcfafd"></a>

### [`007ffe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ffe2c.md) → [`007ffe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ffe2c.md) FUN_007ffe2c

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
      "definition_site": "007ffe38",
      "incomplete_value": false,
      "site": "007ffe38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ffe38",
      "incomplete_value": false,
      "site": "007ffe38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:830:8"
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
      "007ffe38",
      "DATA",
      [
        "storage",
        "00c00830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ffe38",
      "DATA",
      [
        "storage",
        "00c00880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ffe34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ff/007ffe2c.md#insn-007ffe34)
- 新版 `007ffe34`（命令位置の公開資料なし）

~~~diff
- 007ffe34 ["COPY", "tmp:0:8", ["const:830:8"]]
- 007ffe34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ffe34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ffe34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ffe34 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 007ffe34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ffe34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ffe34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ffe34 bytes 29c12091
+ 007ffe34 bytes 29012291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98be09326afc24e064bdda4bdcab8006"></a>

### [`0080033c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/0080033c.md) → [`0080033c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/0080033c.md) FUN_0080033c

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
      "definition_site": "0080035c",
      "incomplete_value": false,
      "site": "00800360",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0080035c",
      "incomplete_value": false,
      "site": "00800360",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
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
      "00800360",
      "DATA",
      [
        "storage",
        "00c008b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00800360",
      "DATA",
      [
        "storage",
        "00c00900",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0080035c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/0080033c.md#insn-0080035c)
- 新版 `0080035c`（命令位置の公開資料なし）

~~~diff
- 0080035c ["COPY", "tmp:0:8", ["const:8b0:8"]]
- 0080035c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0080035c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0080035c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0080035c ["COPY", "tmp:0:8", ["const:900:8"]]
+ 0080035c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0080035c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0080035c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0080035c bytes 08c12291
+ 0080035c bytes 08012491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25c3e22e939811d6413f4435dd6ee8a8"></a>

### [`00800374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800374.md) → [`00800374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/00800374.md) FUN_00800374

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
      "definition_site": "00800378",
      "incomplete_value": false,
      "site": "0080037c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00800378",
      "incomplete_value": false,
      "site": "0080037c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
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
      "0080037c",
      "DATA",
      [
        "storage",
        "00c008b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0080037c",
      "DATA",
      [
        "storage",
        "00c00900",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00800378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800374.md#insn-00800378)
- 新版 `00800378`（命令位置の公開資料なし）

~~~diff
- 00800378 ["COPY", "tmp:0:8", ["const:8b0:8"]]
- 00800378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00800378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00800378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00800378 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 00800378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00800378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00800378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00800378 bytes 08c12291
+ 00800378 bytes 08012491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1632ae875d3ec0adad0e54a54a445e6d"></a>

### [`008004e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/008004e8.md) → [`008004e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/008004e8.md) FUN_008004e8

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
      "definition_site": "0080050c",
      "incomplete_value": false,
      "site": "0080050c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0080050c",
      "incomplete_value": false,
      "site": "0080050c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "0080050c",
      "DATA",
      [
        "storage",
        "00c00930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0080050c",
      "DATA",
      [
        "storage",
        "00c00980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00800508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/008004e8.md#insn-00800508)
- 新版 `00800508`（命令位置の公開資料なし）

~~~diff
- 00800508 ["COPY", "tmp:0:8", ["const:930:8"]]
- 00800508 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00800508 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00800508 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00800508 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 00800508 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00800508 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00800508 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00800508 bytes 08c12491
+ 00800508 bytes 08012691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62c385cb4aa23995262b10074dc9bce9"></a>

### [`0080051c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/0080051c.md) → [`0080051c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/0080051c.md) FUN_0080051c

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
      "definition_site": "00800528",
      "incomplete_value": false,
      "site": "00800528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00800528",
      "incomplete_value": false,
      "site": "00800528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "00800528",
      "DATA",
      [
        "storage",
        "00c00930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00800528",
      "DATA",
      [
        "storage",
        "00c00980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00800524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/0080051c.md#insn-00800524)
- 新版 `00800524`（命令位置の公開資料なし）

~~~diff
- 00800524 ["COPY", "tmp:0:8", ["const:930:8"]]
- 00800524 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00800524 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00800524 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00800524 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 00800524 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00800524 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00800524 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00800524 bytes 29c12491
+ 00800524 bytes 29012691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed67ffc19bb46ad9d81040665cd4d94d"></a>

### [`008005f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/008005f8.md) → [`008005f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/008005f8.md) FUN_008005f8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0080061c",
      "incomplete_value": true,
      "site": "0080061c",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0080061c",
      "incomplete_value": true,
      "site": "0080061c",
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
            "const:9b0:8"
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
      "0080061c",
      "DATA",
      [
        "storage",
        "00c009b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0080061c",
      "DATA",
      [
        "storage",
        "00c00a00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00800618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/008005f8.md#insn-00800618)
- 新版 `00800618`（命令位置の公開資料なし）

~~~diff
- 00800618 ["COPY", "tmp:0:8", ["const:9b0:8"]]
- 00800618 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00800618 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00800618 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00800618 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00800618 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00800618 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00800618 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00800618 bytes 08c12691
+ 00800618 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fee51ba0847f71079c0e44b57c5b3fd"></a>

### [`0080062c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/0080062c.md) → [`0080062c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/0080062c.md) FUN_0080062c

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
      "definition_site": "00800638",
      "incomplete_value": false,
      "site": "00800638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00800638",
      "incomplete_value": false,
      "site": "00800638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
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
      "00800638",
      "DATA",
      [
        "storage",
        "00c009b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00800638",
      "DATA",
      [
        "storage",
        "00c00a00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00800634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/0080062c.md#insn-00800634)
- 新版 `00800634`（命令位置の公開資料なし）

~~~diff
- 00800634 ["COPY", "tmp:0:8", ["const:9b0:8"]]
- 00800634 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00800634 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00800634 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00800634 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00800634 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00800634 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00800634 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00800634 bytes 29c12691
+ 00800634 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35fe0a2c00be4d9f6794e05e5b5b2fd5"></a>

### [`008006d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/008006d8.md) → [`008006d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/008006d8.md) FUN_008006d8

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
      "definition_site": "008006fc",
      "incomplete_value": false,
      "site": "008006fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008006fc",
      "incomplete_value": false,
      "site": "008006fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "008006fc",
      "DATA",
      [
        "storage",
        "00c00a30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008006fc",
      "DATA",
      [
        "storage",
        "00c00a80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008006f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/008006d8.md#insn-008006f8)
- 新版 `008006f8`（命令位置の公開資料なし）

~~~diff
- 008006f8 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 008006f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008006f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008006f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008006f8 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 008006f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008006f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008006f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008006f8 bytes 08c12891
+ 008006f8 bytes 08012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ae6c9ca7d5241869f99648f180ab6b5"></a>

### [`0080070c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/0080070c.md) → [`0080070c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/0080070c.md) FUN_0080070c

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
      "definition_site": "00800718",
      "incomplete_value": false,
      "site": "00800718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00800718",
      "incomplete_value": false,
      "site": "00800718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "00800718",
      "DATA",
      [
        "storage",
        "00c00a30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00800718",
      "DATA",
      [
        "storage",
        "00c00a80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00800714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/0080070c.md#insn-00800714)
- 新版 `00800714`（命令位置の公開資料なし）

~~~diff
- 00800714 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 00800714 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00800714 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00800714 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00800714 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 00800714 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00800714 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00800714 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00800714 bytes 29c12891
+ 00800714 bytes 29012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab8fd1cf21b4882fe475fe7cc1f487c1"></a>

### [`00800728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800728.md) → [`00800728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/00800728.md) FUN_00800728

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 41件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044ac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac1c.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md)
- 新版 呼出元 0件  · 呼出先 41件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac1c.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.28% / 新版 97.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00800d68",
      "incomplete_value": true,
      "site": "00800d78",
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
                "const:271:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00800d68",
      "incomplete_value": true,
      "site": "00800d78",
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
                "const:2fe:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00800d6c",
      "incomplete_value": true,
      "site": "00800d7c",
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
                "const:c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00800d6c",
      "incomplete_value": true,
      "site": "00800d7c",
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
                "const:c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 45,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00800da0",
      "incomplete_value": false,
      "site": "00800da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00800da0",
      "incomplete_value": false,
      "site": "00800da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:c20:8"
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008009f0",
      "READ",
      [
        "storage",
        "00c1b6d8",
        null,
        "pointer"
      ]
    ],
    [
      "00800d18",
      "READ",
      [
        "storage",
        "00c1b6d8",
        null,
        "pointer"
      ]
    ],
    [
      "00800d68",
      "READ",
      [
        "storage",
        "002992fe",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008009f0",
      "READ",
      [
        "storage",
        "00c1b728",
        null,
        "pointer"
      ]
    ],
    [
      "00800d18",
      "READ",
      [
        "storage",
        "00c1b728",
        null,
        "pointer"
      ]
    ],
    [
      "00800d68",
      "READ",
      [
        "storage",
        "00299271",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008009f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800728.md#insn-008009f0) · [`00800d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800728.md#insn-00800d18) · [`00800d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800728.md#insn-00800d60)
- 新版 `008009f0`（命令位置の公開資料なし） · `00800d18`（命令位置の公開資料なし） · `00800d60`（命令位置の公開資料なし）

~~~diff
- 008009f0 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:6d8:8"]]
- 008009f0 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 008009f0 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
+ 008009f0 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 008009f0 bytes 186f43f9
+ 008009f0 bytes 189743f9
- 00800d18 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:6d8:8"]]
- 00800d18 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00800d18 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
+ 00800d18 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 00800d18 bytes f76e43f9
+ 00800d18 bytes f79643f9
- 00800d60 ["COPY", "tmp:0:8", ["const:2fe:8"]]
- 00800d60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00800d60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00800d60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00800d60 ["COPY", "tmp:0:8", ["const:271:8"]]
+ 00800d60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00800d60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00800d60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00800d60 bytes 08f90b91
+ 00800d60 bytes 08c50991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-806c04ce14c749d83ad9f8c0fc13ed65"></a>

### [`00802788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00802/00802788.md) → [`00802788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00802/00802788.md) FUN_00802788

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`00800728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00800/00800728.md) [`008037bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/008037bc.md) [`008038c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/008038c0.md) [`00803b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/00803b54.md) [`00803c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/00803c58.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 7件 [`00800728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/00800728.md) [`008037bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/008037bc.md) [`008038c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/008038c0.md) [`00803b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/00803b54.md) [`00803c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/00803c58.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00802794",
      "incomplete_value": false,
      "site": "00802798",
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
      "definition_site": "00802794",
      "incomplete_value": false,
      "site": "00802798",
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
      "00802794",
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
      "00802794",
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

- 旧版 [`00802794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00802/00802788.md#insn-00802794)
- 新版 `00802794`（命令位置の公開資料なし）

~~~diff
- 00802794 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00802794 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00802794 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00802794 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00802794 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00802794 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00802794 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00802794 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00802794 bytes 000c0c91
+ 00802794 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dafbe5aca5ee952cda9d727db60ceaa"></a>

### [`0080377c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/0080377c.md) → [`0080377c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/0080377c.md) FUN_0080377c

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
      "definition_site": "00803784",
      "incomplete_value": false,
      "site": "00803788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00803784",
      "incomplete_value": false,
      "site": "00803788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
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
      "00803788",
      "DATA",
      [
        "storage",
        "00c00aa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00803788",
      "DATA",
      [
        "storage",
        "00c00af0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00803784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/0080377c.md#insn-00803784)
- 新版 `00803784`（命令位置の公開資料なし）

~~~diff
- 00803784 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 00803784 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00803784 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00803784 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00803784 ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 00803784 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00803784 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00803784 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00803784 bytes 29812a91
+ 00803784 bytes 29c12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11002c787bce5332f07cd25c0f5adaa9"></a>

### [`008037bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/008037bc.md) → [`008037bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/008037bc.md) FUN_008037bc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00802788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00802/00802788.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00802788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00802/00802788.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.38% / 新版 95.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008037f0",
      "incomplete_value": false,
      "site": "008037f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008037f0",
      "incomplete_value": false,
      "site": "008037f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
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
      "008037f0",
      "DATA",
      [
        "storage",
        "00c00aa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008037f0",
      "DATA",
      [
        "storage",
        "00c00af0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008037e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/008037bc.md#insn-008037e4) · [`008037e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/008037bc.md#insn-008037e8)
- 新版 `008037e4`（命令位置の公開資料なし） · `008037e8`（命令位置の公開資料なし）

~~~diff
- 008037e4 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 008037e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008037e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008037e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008037e4 ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 008037e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008037e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008037e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008037e4 bytes 08812a91
+ 008037e4 bytes 08c12b91
- 008037e8 ["COPY", "register:4098:8", ["register:4000:8"]]
- 008037e8 bytes f30300aa
+ 008037e8 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 008037e8 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04738d43dab46bebee5c377014fa4320"></a>

### [`008038c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/008038c0.md) → [`008038c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/008038c0.md) FUN_008038c0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00802788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00802/00802788.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00802788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00802/00802788.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

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
      "definition_site": "008038f0",
      "incomplete_value": false,
      "site": "008038f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008038f0",
      "incomplete_value": false,
      "site": "008038f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
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
      "008038f0",
      "DATA",
      [
        "storage",
        "00c00aa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008038f0",
      "DATA",
      [
        "storage",
        "00c00af0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008038e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/008038c0.md#insn-008038e8)
- 新版 `008038e8`（命令位置の公開資料なし）

~~~diff
- 008038e8 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 008038e8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008038e8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008038e8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008038e8 ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 008038e8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008038e8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008038e8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008038e8 bytes 4a812a91
+ 008038e8 bytes 4ac12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f713fff3e449685e11aa4b28b0bd6e3"></a>

### [`00803af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/00803af0.md) → [`00803af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/00803af0.md) FUN_00803af0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00803afc",
      "incomplete_value": false,
      "site": "00803b00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00803afc",
      "incomplete_value": false,
      "site": "00803b00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "00803b00",
      "DATA",
      [
        "storage",
        "00c00b20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00803b00",
      "DATA",
      [
        "storage",
        "00c00b70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00803afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/00803af0.md#insn-00803afc)
- 新版 `00803afc`（命令位置の公開資料なし）

~~~diff
- 00803afc ["COPY", "tmp:0:8", ["const:b20:8"]]
- 00803afc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00803afc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00803afc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00803afc ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 00803afc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00803afc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00803afc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00803afc bytes 29812c91
+ 00803afc bytes 29c12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e652713b3465c36b3763951045ac4b0"></a>

### [`00803b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/00803b14.md) → [`00803b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/00803b14.md) FUN_00803b14

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
      "definition_site": "00803b1c",
      "incomplete_value": false,
      "site": "00803b20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00803b1c",
      "incomplete_value": false,
      "site": "00803b20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "00803b20",
      "DATA",
      [
        "storage",
        "00c00b20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00803b20",
      "DATA",
      [
        "storage",
        "00c00b70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00803b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/00803b14.md#insn-00803b1c)
- 新版 `00803b1c`（命令位置の公開資料なし）

~~~diff
- 00803b1c ["COPY", "tmp:0:8", ["const:b20:8"]]
- 00803b1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00803b1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00803b1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00803b1c ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 00803b1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00803b1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00803b1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00803b1c bytes 29812c91
+ 00803b1c bytes 29c12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d788b2f2332981d8dfa53c69bc5d335"></a>

### [`00803b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/00803b54.md) → [`00803b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/00803b54.md) FUN_00803b54

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00802788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00802/00802788.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00802788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00802/00802788.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.38% / 新版 95.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00803b88",
      "incomplete_value": false,
      "site": "00803b88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00803b88",
      "incomplete_value": false,
      "site": "00803b88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "00803b88",
      "DATA",
      [
        "storage",
        "00c00b20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00803b88",
      "DATA",
      [
        "storage",
        "00c00b70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00803b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/00803b54.md#insn-00803b7c) · [`00803b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/00803b54.md#insn-00803b80)
- 新版 `00803b7c`（命令位置の公開資料なし） · `00803b80`（命令位置の公開資料なし）

~~~diff
- 00803b7c ["COPY", "tmp:0:8", ["const:b20:8"]]
- 00803b7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00803b7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00803b7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00803b7c ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 00803b7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00803b7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00803b7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00803b7c bytes 08812c91
+ 00803b7c bytes 08c12d91
- 00803b80 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00803b80 bytes f30300aa
+ 00803b80 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00803b80 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e9c901b567113ba2adc151fe8fe07fe"></a>

### [`00803c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/00803c58.md) → [`00803c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/00803c58.md) FUN_00803c58

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00802788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00802/00802788.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00802788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00802/00802788.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00803c88",
      "incomplete_value": true,
      "site": "00803c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4050:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00803c88",
      "incomplete_value": true,
      "site": "00803c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4050:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "00803c88",
      "DATA",
      [
        "storage",
        "00c00b20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00803c88",
      "DATA",
      [
        "storage",
        "00c00b70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00803c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/00803c58.md#insn-00803c80)
- 新版 `00803c80`（命令位置の公開資料なし）

~~~diff
- 00803c80 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 00803c80 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00803c80 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00803c80 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00803c80 ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 00803c80 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00803c80 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00803c80 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00803c80 bytes 4a812c91
+ 00803c80 bytes 4ac12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-058ce310202de80ebd5910cbb694f971"></a>

### [`00803f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/00803f6c.md) → [`00803f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/00803f6c.md) FUN_00803f6c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00803f78",
      "incomplete_value": false,
      "site": "00803f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00803f78",
      "incomplete_value": false,
      "site": "00803f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
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
      "00803f7c",
      "DATA",
      [
        "storage",
        "00c00ba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00803f7c",
      "DATA",
      [
        "storage",
        "00c00bf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00803f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/00803f6c.md#insn-00803f78)
- 新版 `00803f78`（命令位置の公開資料なし）

~~~diff
- 00803f78 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 00803f78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00803f78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00803f78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00803f78 ["COPY", "tmp:0:8", ["const:bf0:8"]]
+ 00803f78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00803f78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00803f78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00803f78 bytes 29812e91
+ 00803f78 bytes 29c12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51ce4b8e09c1086ca04a2e5c99af2fa1"></a>

### [`00803f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/00803f90.md) → [`00803f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/00803f90.md) FUN_00803f90

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
      "definition_site": "00803f98",
      "incomplete_value": false,
      "site": "00803f9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00803f98",
      "incomplete_value": false,
      "site": "00803f9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
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
      "00803f9c",
      "DATA",
      [
        "storage",
        "00c00ba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00803f9c",
      "DATA",
      [
        "storage",
        "00c00bf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00803f98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/00803f90.md#insn-00803f98)
- 新版 `00803f98`（命令位置の公開資料なし）

~~~diff
- 00803f98 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 00803f98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00803f98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00803f98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00803f98 ["COPY", "tmp:0:8", ["const:bf0:8"]]
+ 00803f98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00803f98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00803f98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00803f98 bytes 29812e91
+ 00803f98 bytes 29c12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99ac1851242d3de21ae7736a81beb3c1"></a>

### [`00803fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/00803fd0.md) → [`00803fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/00803fd0.md) FUN_00803fd0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00802788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00802/00802788.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00802788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00802/00802788.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.38% / 新版 95.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00804004",
      "incomplete_value": false,
      "site": "00804004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00804004",
      "incomplete_value": false,
      "site": "00804004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
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
      "00804004",
      "DATA",
      [
        "storage",
        "00c00ba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00804004",
      "DATA",
      [
        "storage",
        "00c00bf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00803ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/00803fd0.md#insn-00803ff8) · [`00803ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00803/00803fd0.md#insn-00803ffc)
- 新版 `00803ff8`（命令位置の公開資料なし） · `00803ffc`（命令位置の公開資料なし）

~~~diff
- 00803ff8 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 00803ff8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00803ff8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00803ff8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00803ff8 ["COPY", "tmp:0:8", ["const:bf0:8"]]
+ 00803ff8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00803ff8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00803ff8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00803ff8 bytes 08812e91
+ 00803ff8 bytes 08c12f91
- 00803ffc ["COPY", "register:4098:8", ["register:4000:8"]]
- 00803ffc bytes f30300aa
+ 00803ffc ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00803ffc bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c847f41d34fdb917dfc74c8c45488357"></a>

### [`008040d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00804/008040d4.md) → [`008040d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00804/008040d4.md) FUN_008040d4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00802788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00802/00802788.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00802788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00802/00802788.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

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
      "definition_site": "00804104",
      "incomplete_value": false,
      "site": "00804104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00804104",
      "incomplete_value": false,
      "site": "00804104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
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
      "00804104",
      "DATA",
      [
        "storage",
        "00c00ba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00804104",
      "DATA",
      [
        "storage",
        "00c00bf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008040fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00804/008040d4.md#insn-008040fc)
- 新版 `008040fc`（命令位置の公開資料なし）

~~~diff
- 008040fc ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 008040fc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008040fc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008040fc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008040fc ["COPY", "tmp:0:8", ["const:bf0:8"]]
+ 008040fc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008040fc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008040fc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008040fc bytes 4a812e91
+ 008040fc bytes 4ac12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a06d893b7087c20fa6664c91462521a2"></a>

### [`0080420c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00804/0080420c.md) → [`0080420c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00804/0080420c.md) FUN_0080420c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444edc.md) [`0053770c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/0053770c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`008308f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00830/008308f0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444edc.md) [`0053770c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053770c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`008308f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00830/008308f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008042a4",
      "incomplete_value": true,
      "site": "008042a8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008042a4",
      "incomplete_value": true,
      "site": "008042a8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:a78:8"
              ]
            ]
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
      "definition_site": "00804290",
      "incomplete_value": true,
      "site": "008042a8",
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
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00804290",
      "incomplete_value": true,
      "site": "008042a8",
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
            "const:e48:8"
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
      "definition_site": "0080429c",
      "incomplete_value": false,
      "site": "008042a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0080429c",
      "incomplete_value": false,
      "site": "008042a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "00804290",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00804294",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0080429c",
      "PARAM",
      [
        "storage",
        "00c00488",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00804290",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00804294",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0080429c",
      "PARAM",
      [
        "storage",
        "00c004d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00804290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00804/0080420c.md#insn-00804290) · [`00804294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00804/0080420c.md#insn-00804294) · [`0080429c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00804/0080420c.md#insn-0080429c)
- 新版 `00804290`（命令位置の公開資料なし） · `00804294`（命令位置の公開資料なし） · `0080429c`（命令位置の公開資料なし）

~~~diff
- 00804290 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00804290 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00804290 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00804290 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00804290 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00804290 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00804290 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00804290 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00804290 bytes 21203991
+ 00804290 bytes 21603a91
- 00804294 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00804294 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00804294 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00804294 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00804294 bytes 083d45f9
+ 00804294 bytes 085d45f9
- 0080429c ["COPY", "tmp:0:8", ["const:488:8"]]
- 0080429c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0080429c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0080429c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0080429c ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 0080429c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0080429c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0080429c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0080429c bytes 42201291
+ 0080429c bytes 42601391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4961c6c8f9c04bee27e6d55d44a1835c"></a>

### [`008043c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00804/008043c0.md) → [`008043c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00804/008043c0.md) FUN_008043c0

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
      "definition_site": "008043d4",
      "incomplete_value": false,
      "site": "008043d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008043d4",
      "incomplete_value": false,
      "site": "008043d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "008043d8",
      "DATA",
      [
        "storage",
        "00c00c20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008043d8",
      "DATA",
      [
        "storage",
        "00c00c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008043d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00804/008043c0.md#insn-008043d4)
- 新版 `008043d4`（命令位置の公開資料なし）

~~~diff
- 008043d4 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 008043d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008043d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008043d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008043d4 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 008043d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008043d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008043d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008043d4 bytes 08813091
+ 008043d4 bytes 08c13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06fa43a41442b7f993783b856d3c6174"></a>

### [`008043e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00804/008043e4.md) → [`008043e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00804/008043e4.md) FUN_008043e4

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
      "definition_site": "008043e8",
      "incomplete_value": false,
      "site": "008043ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008043e8",
      "incomplete_value": false,
      "site": "008043ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "008043ec",
      "DATA",
      [
        "storage",
        "00c00c20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008043ec",
      "DATA",
      [
        "storage",
        "00c00c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008043e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00804/008043e4.md#insn-008043e8)
- 新版 `008043e8`（命令位置の公開資料なし）

~~~diff
- 008043e8 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 008043e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008043e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008043e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008043e8 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 008043e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008043e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008043e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008043e8 bytes 08813091
+ 008043e8 bytes 08c13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

