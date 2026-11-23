# v15.7.3 → v15.7.4 · 最優先の変更候補 (24)

[一覧の目次](README.md)

<a id="compare-17b59a82a9081d93770802ce9125fecc"></a>

### [`005b6bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6bb0.md) → [`005b6bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6bb0.md) FUN_005b6bb0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`005b7004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7004.md)
- 新版 呼出元 0件  · 呼出先 18件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`005b7004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7004.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b6ccc",
      "incomplete_value": true,
      "site": "005b6ccc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:76e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6ccc",
      "incomplete_value": true,
      "site": "005b6ccc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6e3:8"
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
      "definition_site": "005b6cd0",
      "incomplete_value": true,
      "site": "005b6cd0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005b6cd0",
      "incomplete_value": true,
      "site": "005b6cd0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b6d48",
      "incomplete_value": false,
      "site": "005b6d48",
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
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6d48",
      "incomplete_value": false,
      "site": "005b6d48",
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
            "const:280:8"
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
      "005b6cbc",
      "READ",
      [
        "storage",
        "002a46e3",
        null,
        "string"
      ]
    ],
    [
      "005b6cc0",
      "READ",
      [
        "storage",
        "002a46e8",
        null,
        "string"
      ]
    ],
    [
      "005b6d48",
      "DATA",
      [
        "storage",
        "00bf4280",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6cbc",
      "READ",
      [
        "storage",
        "002a476e",
        null,
        "string"
      ]
    ],
    [
      "005b6cc0",
      "READ",
      [
        "storage",
        "002a4773",
        null,
        "string"
      ]
    ],
    [
      "005b6d48",
      "DATA",
      [
        "storage",
        "00bf42d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6bb0.md#insn-005b6cb4) · [`005b6d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6bb0.md#insn-005b6d40) · [`005b6d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6bb0.md#insn-005b6d80)
- 新版 `005b6cb4`（命令位置の公開資料なし） · `005b6d40`（命令位置の公開資料なし） · `005b6d80`（命令位置の公開資料なし）

~~~diff
- 005b6cb4 ["COPY", "tmp:0:8", ["const:6e3:8"]]
- 005b6cb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6cb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6cb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6cb4 ["COPY", "tmp:0:8", ["const:76e:8"]]
+ 005b6cb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6cb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6cb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6cb4 bytes 298d1b91
+ 005b6cb4 bytes 29b91d91
- 005b6d40 ["COPY", "tmp:0:8", ["const:280:8"]]
- 005b6d40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6d40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6d40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6d40 ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 005b6d40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6d40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6d40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6d40 bytes 08010a91
+ 005b6d40 bytes 08410b91
- 005b6d80 ["COPY", "tmp:0:8", ["const:72f:8"]]
- 005b6d80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6d80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6d80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6d80 ["COPY", "tmp:0:8", ["const:7ba:8"]]
+ 005b6d80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6d80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6d80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6d80 bytes 29bd1c91
+ 005b6d80 bytes 29e91e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c22103087c82f6ea2422c6c64aa3c394"></a>

### [`005b7140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7140.md) → [`005b7140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7140.md) FUN_005b7140

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
      "definition_site": "005b7164",
      "incomplete_value": false,
      "site": "005b7164",
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
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7164",
      "incomplete_value": false,
      "site": "005b7164",
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
            "const:280:8"
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
      "005b7164",
      "DATA",
      [
        "storage",
        "00bf4280",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7164",
      "DATA",
      [
        "storage",
        "00bf42d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7140.md#insn-005b7160)
- 新版 `005b7160`（命令位置の公開資料なし）

~~~diff
- 005b7160 ["COPY", "tmp:0:8", ["const:280:8"]]
- 005b7160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b7160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b7160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7160 ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 005b7160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b7160 bytes 08010a91
+ 005b7160 bytes 08410b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c28ed1fe077befd39f457965d554f81c"></a>

### [`005b7174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7174.md) → [`005b7174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7174.md) FUN_005b7174

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
      "definition_site": "005b7180",
      "incomplete_value": false,
      "site": "005b7180",
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
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7180",
      "incomplete_value": false,
      "site": "005b7180",
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
            "const:280:8"
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
      "005b7180",
      "DATA",
      [
        "storage",
        "00bf4280",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7180",
      "DATA",
      [
        "storage",
        "00bf42d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b717c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7174.md#insn-005b717c)
- 新版 `005b717c`（命令位置の公開資料なし）

~~~diff
- 005b717c ["COPY", "tmp:0:8", ["const:280:8"]]
- 005b717c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b717c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b717c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b717c ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 005b717c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b717c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b717c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b717c bytes 29010a91
+ 005b717c bytes 29410b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c4395003dd74f9ba9dcf2150ed4f8c4"></a>

### [`005b7204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7204.md) → [`005b7204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7204.md) FUN_005b7204

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
      "definition_site": "005b7228",
      "incomplete_value": false,
      "site": "005b722c",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7228",
      "incomplete_value": false,
      "site": "005b722c",
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
            "const:300:8"
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
      "005b722c",
      "DATA",
      [
        "storage",
        "00bf4300",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b722c",
      "DATA",
      [
        "storage",
        "00bf4350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7204.md#insn-005b7228)
- 新版 `005b7228`（命令位置の公開資料なし）

~~~diff
- 005b7228 ["COPY", "tmp:0:8", ["const:300:8"]]
- 005b7228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b7228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b7228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7228 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 005b7228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b7228 bytes 08010c91
+ 005b7228 bytes 08410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d5656b9d13f12e9a8801784b88119db"></a>

### [`005b7244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7244.md) → [`005b7244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7244.md) FUN_005b7244

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
      "definition_site": "005b7248",
      "incomplete_value": false,
      "site": "005b724c",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7248",
      "incomplete_value": false,
      "site": "005b724c",
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
            "const:300:8"
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
      "005b724c",
      "DATA",
      [
        "storage",
        "00bf4300",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b724c",
      "DATA",
      [
        "storage",
        "00bf4350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7244.md#insn-005b7248)
- 新版 `005b7248`（命令位置の公開資料なし）

~~~diff
- 005b7248 ["COPY", "tmp:0:8", ["const:300:8"]]
- 005b7248 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b7248 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b7248 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7248 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 005b7248 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7248 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7248 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b7248 bytes 08010c91
+ 005b7248 bytes 08410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be6b0bfe9554aa80a02a378206ec0dde"></a>

### [`005b73b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b73b4.md) → [`005b73b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b73b4.md) FUN_005b73b4

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
      "definition_site": "005b73c0",
      "incomplete_value": false,
      "site": "005b73c0",
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
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b73c0",
      "incomplete_value": false,
      "site": "005b73c0",
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
            "const:390:8"
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
      "005b73c0",
      "DATA",
      [
        "storage",
        "00bf4390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b73c0",
      "DATA",
      [
        "storage",
        "00bf43e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b73bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b73b4.md#insn-005b73bc)
- 新版 `005b73bc`（命令位置の公開資料なし）

~~~diff
- 005b73bc ["COPY", "tmp:0:8", ["const:390:8"]]
- 005b73bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b73bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b73bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b73bc ["COPY", "tmp:0:8", ["const:3e0:8"]]
+ 005b73bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b73bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b73bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b73bc bytes 29410e91
+ 005b73bc bytes 29810f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff7b4d3ca9d660f27dfdb21694791027"></a>

### [`005b7480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7480.md) → [`005b7480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7480.md) FUN_005b7480

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
      "definition_site": "005b74a4",
      "incomplete_value": true,
      "site": "005b74a4",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b74a4",
      "incomplete_value": true,
      "site": "005b74a4",
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
            "const:410:8"
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
      "005b74a4",
      "DATA",
      [
        "storage",
        "00bf4410",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b74a4",
      "DATA",
      [
        "storage",
        "00bf4460",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b74a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7480.md#insn-005b74a0)
- 新版 `005b74a0`（命令位置の公開資料なし）

~~~diff
- 005b74a0 ["COPY", "tmp:0:8", ["const:410:8"]]
- 005b74a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b74a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b74a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b74a0 ["COPY", "tmp:0:8", ["const:460:8"]]
+ 005b74a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b74a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b74a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b74a0 bytes 08411091
+ 005b74a0 bytes 08811191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3aacf61e2e91ec8b0dd95b57c187a00"></a>

### [`005b74b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b74b4.md) → [`005b74b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b74b4.md) FUN_005b74b4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b74c0",
      "incomplete_value": true,
      "site": "005b74c0",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b74c0",
      "incomplete_value": true,
      "site": "005b74c0",
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
            "const:410:8"
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
      "005b74c0",
      "DATA",
      [
        "storage",
        "00bf4410",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b74c0",
      "DATA",
      [
        "storage",
        "00bf4460",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b74bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b74b4.md#insn-005b74bc)
- 新版 `005b74bc`（命令位置の公開資料なし）

~~~diff
- 005b74bc ["COPY", "tmp:0:8", ["const:410:8"]]
- 005b74bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b74bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b74bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b74bc ["COPY", "tmp:0:8", ["const:460:8"]]
+ 005b74bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b74bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b74bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b74bc bytes 29411091
+ 005b74bc bytes 29811191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-456391df5929f3bc449b67eda563ba36"></a>

### [`005b75f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b75f0.md) → [`005b75f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b75f0.md) FUN_005b75f0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`005a7dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a7dfc.md) [`0067417c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00674/0067417c.md) [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`0087d888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087d/0087d888.md) [`008a0d28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a0/008a0d28.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 8件 [`005a7dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a7dfc.md) [`0067417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067417c.md) [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`0087d888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087d/0087d888.md) [`008a0d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a0/008a0d28.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "005b75fc",
      "incomplete_value": true,
      "site": "005b7600",
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
      "definition_site": "005b75fc",
      "incomplete_value": true,
      "site": "005b7600",
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
      "005b75fc",
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
      "005b75fc",
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

- 旧版 [`005b75fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b75f0.md#insn-005b75fc)
- 新版 `005b75fc`（命令位置の公開資料なし）

~~~diff
- 005b75fc ["COPY", "tmp:0:8", ["const:303:8"]]
- 005b75fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005b75fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005b75fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005b75fc ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005b75fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005b75fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005b75fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005b75fc bytes 000c0c91
+ 005b75fc bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d6acdc5cd4aa6d82cfd4ed960ef57ab"></a>

### [`005b760c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b760c.md) → [`005b760c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b760c.md) FUN_005b760c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b762c",
      "incomplete_value": true,
      "site": "005b7630",
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
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b762c",
      "incomplete_value": true,
      "site": "005b7630",
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
            "const:490:8"
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
      "005b7630",
      "DATA",
      [
        "storage",
        "00bf4490",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7630",
      "DATA",
      [
        "storage",
        "00bf44e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b762c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b760c.md#insn-005b762c)
- 新版 `005b762c`（命令位置の公開資料なし）

~~~diff
- 005b762c ["COPY", "tmp:0:8", ["const:490:8"]]
- 005b762c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b762c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b762c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b762c ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 005b762c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b762c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b762c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b762c bytes 08411291
+ 005b762c bytes 08811391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f3cd28012e77b6a5b44c1a3e1042a2d"></a>

### [`005b77d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b77d8.md) → [`005b77d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b77d8.md) _INIT_62

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b7814",
      "incomplete_value": true,
      "site": "005b7830",
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
      "definition_site": "005b7814",
      "incomplete_value": true,
      "site": "005b7830",
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
      "definition_site": "005b7838",
      "incomplete_value": true,
      "site": "005b7854",
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
      "definition_site": "005b7838",
      "incomplete_value": true,
      "site": "005b7854",
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
      "definition_site": "005b7858",
      "incomplete_value": true,
      "site": "005b7874",
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
      "definition_site": "005b7858",
      "incomplete_value": true,
      "site": "005b7874",
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
      "005b7814",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "005b7838",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "005b7858",
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
      "005b7814",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "005b7838",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "005b7858",
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

- 旧版 [`005b7804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b77d8.md#insn-005b7804) · [`005b780c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b77d8.md#insn-005b780c)
- 新版 `005b7804`（命令位置の公開資料なし） · `005b780c`（命令位置の公開資料なし）

~~~diff
- 005b7804 ["COPY", "tmp:0:8", ["const:978:8"]]
- 005b7804 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005b7804 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005b7804 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005b7804 ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 005b7804 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005b7804 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005b7804 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005b7804 bytes 73e22591
+ 005b7804 bytes 73e22691
- 005b780c ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 005b780c bytes 89e7ff90
+ 005b780c ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 005b780c bytes 89e7ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddaae593cb965f9db43a1aa2403ec2a1"></a>

### [`005b7d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7d98.md) → [`005b7d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7d98.md) FUN_005b7d98

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`005b7b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7b78.md) [`005b9118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b9/005b9118.md) [`005b97a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b9/005b97a0.md) [`005b9970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b9/005b9970.md) [`005ba170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005ba170.md) · 呼出先 1件 [`0041f354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f354.md)
- 新版 呼出元 5件 [`005b7b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7b78.md) [`005b9118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b9118.md) [`005b97a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b97a0.md) [`005b9970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b9970.md) [`005ba170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba170.md) · 呼出先 1件 [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005b7f1c",
      "incomplete_value": false,
      "site": "005b7f24",
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
            "const:62e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7f1c",
      "incomplete_value": false,
      "site": "005b7f24",
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
            "const:5a3:8"
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
      "definition_site": "005b7f38",
      "incomplete_value": false,
      "site": "005b7f40",
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
            "const:6a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7f38",
      "incomplete_value": false,
      "site": "005b7f40",
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
            "const:61c:8"
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
      "definition_site": "005b7f54",
      "incomplete_value": false,
      "site": "005b7f5c",
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
            "const:c36:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7f54",
      "incomplete_value": false,
      "site": "005b7f5c",
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
            "const:cc3:8"
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
      "005b7f1c",
      "PARAM",
      [
        "storage",
        "002a35a3",
        null,
        "string"
      ]
    ],
    [
      "005b7f38",
      "PARAM",
      [
        "storage",
        "0029d61c",
        null,
        "string"
      ]
    ],
    [
      "005b7f54",
      "PARAM",
      [
        "storage",
        "00296cc3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005b7f1c",
      "PARAM",
      [
        "storage",
        "002a362e",
        null,
        "string"
      ]
    ],
    [
      "005b7f38",
      "PARAM",
      [
        "storage",
        "0029d6a7",
        null,
        "string"
      ]
    ],
    [
      "005b7f54",
      "PARAM",
      [
        "storage",
        "00296c36",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7f1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7d98.md#insn-005b7f1c) · [`005b7f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7d98.md#insn-005b7f38) · [`005b7f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7d98.md#insn-005b7f54)
- 新版 `005b7f1c`（命令位置の公開資料なし） · `005b7f38`（命令位置の公開資料なし） · `005b7f54`（命令位置の公開資料なし）

~~~diff
- 005b7f1c ["COPY", "tmp:0:8", ["const:5a3:8"]]
- 005b7f1c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005b7f1c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005b7f1c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005b7f1c ["COPY", "tmp:0:8", ["const:62e:8"]]
+ 005b7f1c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005b7f1c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005b7f1c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005b7f1c bytes 218c1691
+ 005b7f1c bytes 21b81891
- 005b7f38 ["COPY", "tmp:0:8", ["const:61c:8"]]
- 005b7f38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005b7f38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005b7f38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005b7f38 ["COPY", "tmp:0:8", ["const:6a7:8"]]
+ 005b7f38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005b7f38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005b7f38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005b7f38 bytes 21701891
+ 005b7f38 bytes 219c1a91
- 005b7f54 ["COPY", "tmp:0:8", ["const:cc3:8"]]
- 005b7f54 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005b7f54 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005b7f54 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005b7f54 ["COPY", "tmp:0:8", ["const:c36:8"]]
+ 005b7f54 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005b7f54 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005b7f54 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005b7f54 bytes 210c3391
+ 005b7f54 bytes 21d83091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f6b12c08e3802aeb26ba9b192f194c9"></a>

### [`005b8a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b8/005b8a40.md) → [`005b8a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b8a40.md) FUN_005b8a40

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005b807c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b8/005b807c.md) [`005c43a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c4/005c43a4.md) · 呼出先 9件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`0044abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abe4.md) [`0044abfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abfc.md)
- 新版 呼出元 2件 [`005b807c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b807c.md) [`005c43a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c4/005c43a4.md) · 呼出先 9件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044abe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abe4.md) [`0044abfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abfc.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005b8d14",
      "incomplete_value": true,
      "site": "005b8d18",
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
      "definition_site": "005b8d14",
      "incomplete_value": true,
      "site": "005b8d18",
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
    "ordinal": 21,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005b8d04",
      "READ",
      [
        "storage",
        "00c1b610",
        null,
        "pointer"
      ]
    ],
    [
      "005b8d08",
      "READ",
      [
        "storage",
        "00c1b618",
        null,
        "pointer"
      ]
    ],
    [
      "005b8d0c",
      "READ",
      [
        "storage",
        "00c16fb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b8d04",
      "READ",
      [
        "storage",
        "00c1b660",
        null,
        "pointer"
      ]
    ],
    [
      "005b8d08",
      "READ",
      [
        "storage",
        "00c1b668",
        null,
        "pointer"
      ]
    ],
    [
      "005b8d0c",
      "READ",
      [
        "storage",
        "00c17000",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b8/005b8a40.md#insn-005b8d04) · [`005b8d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b8/005b8a40.md#insn-005b8d08)
- 新版 `005b8d04`（命令位置の公開資料なし） · `005b8d08`（命令位置の公開資料なし）

~~~diff
- 005b8d04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:610:8"]]
- 005b8d04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b8d04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:660:8"]]
+ 005b8d04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b8d04 bytes 080943f9
+ 005b8d04 bytes 083143f9
- 005b8d08 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:618:8"]]
- 005b8d08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b8d08 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:668:8"]]
+ 005b8d08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005b8d08 bytes 290d43f9
+ 005b8d08 bytes 293543f9
~~~


<a id="compare-a2a2a046d4211b0033531887b4f52aa0"></a>

### [`005b9970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b9/005b9970.md) → [`005b9970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b9970.md) FUN_005b9970

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005c47c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c4/005c47c4.md) · 呼出先 10件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00449588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449588.md) [`005b7d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7d98.md) [`005ba170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005ba170.md)
- 新版 呼出元 1件 [`005c47c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c4/005c47c4.md) · 呼出先 10件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00449588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449588.md) [`005b7d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7d98.md) [`005ba170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba170.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 97.11% / 新版 97.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 14件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b9ffc",
      "incomplete_value": true,
      "site": "005b9ffc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ad3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b9ffc",
      "incomplete_value": true,
      "site": "005b9ffc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 74,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005b9a58",
      "incomplete_value": true,
      "site": "005b9a5c",
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
      "definition_site": "005b9a58",
      "incomplete_value": true,
      "site": "005b9a5c",
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005b9b9c",
      "incomplete_value": true,
      "site": "005b9ba0",
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
      "definition_site": "005b9b9c",
      "incomplete_value": true,
      "site": "005b9ba0",
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
      "005b9a48",
      "READ",
      [
        "storage",
        "00c1b618",
        null,
        "pointer"
      ]
    ],
    [
      "005b9a4c",
      "READ",
      [
        "storage",
        "00c1b610",
        null,
        "pointer"
      ]
    ],
    [
      "005b9a50",
      "READ",
      [
        "storage",
        "00c17280",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b9a48",
      "READ",
      [
        "storage",
        "00c1b668",
        null,
        "pointer"
      ]
    ],
    [
      "005b9a4c",
      "READ",
      [
        "storage",
        "00c1b660",
        null,
        "pointer"
      ]
    ],
    [
      "005b9a50",
      "READ",
      [
        "storage",
        "00c172d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b9a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b9/005b9970.md#insn-005b9a48) · [`005b9a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b9/005b9970.md#insn-005b9a4c) · [`005b9b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b9/005b9970.md#insn-005b9b8c)
- 新版 `005b9a48`（命令位置の公開資料なし） · `005b9a4c`（命令位置の公開資料なし） · `005b9b8c`（命令位置の公開資料なし）

~~~diff
- 005b9a48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:618:8"]]
- 005b9a48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b9a48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:668:8"]]
+ 005b9a48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b9a48 bytes 080d43f9
+ 005b9a48 bytes 083543f9
- 005b9a4c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:610:8"]]
- 005b9a4c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b9a4c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:660:8"]]
+ 005b9a4c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005b9a4c bytes 290943f9
+ 005b9a4c bytes 293143f9
- 005b9b8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:618:8"]]
- 005b9b8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b9b8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:668:8"]]
+ 005b9b8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b9b8c bytes 080d43f9
+ 005b9b8c bytes 083543f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-204f7f43bf6a6e3ae18b1809e4628460"></a>

### [`005ba170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005ba170.md) → [`005ba170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba170.md) FUN_005ba170

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b9970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b9/005b9970.md) · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`005b7d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7d98.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`005b9970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b9970.md) · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`005b7d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7d98.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 95.42% / 新版 95.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005ba20c",
      "incomplete_value": true,
      "site": "005ba210",
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
      "definition_site": "005ba20c",
      "incomplete_value": true,
      "site": "005ba210",
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "005ba210"
      ],
      [
        "FALL_THROUGH",
        "005ba210"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "005ba20c",
      "incomplete_value": true,
      "site": "005ba220",
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
      "definition_site": "005ba20c",
      "incomplete_value": true,
      "site": "005ba220",
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
    "ordinal": 13,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "005ba210"
      ],
      [
        "FALL_THROUGH",
        "005ba210"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "005ba20c",
      "incomplete_value": true,
      "site": "005ba228",
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
      "definition_site": "005ba20c",
      "incomplete_value": true,
      "site": "005ba228",
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
    "ordinal": 14,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005ba1fc",
      "READ",
      [
        "storage",
        "00c1b618",
        null,
        "pointer"
      ]
    ],
    [
      "005ba200",
      "READ",
      [
        "storage",
        "00c1b610",
        null,
        "pointer"
      ]
    ],
    [
      "005ba204",
      "READ",
      [
        "storage",
        "00c17280",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ba1fc",
      "READ",
      [
        "storage",
        "00c1b668",
        null,
        "pointer"
      ]
    ],
    [
      "005ba200",
      "READ",
      [
        "storage",
        "00c1b660",
        null,
        "pointer"
      ]
    ],
    [
      "005ba204",
      "READ",
      [
        "storage",
        "00c172d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ba1fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005ba170.md#insn-005ba1fc) · [`005ba200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005ba170.md#insn-005ba200)
- 新版 `005ba1fc`（命令位置の公開資料なし） · `005ba200`（命令位置の公開資料なし）

~~~diff
- 005ba1fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:618:8"]]
- 005ba1fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ba1fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:668:8"]]
+ 005ba1fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ba1fc bytes 080d43f9
+ 005ba1fc bytes 083543f9
- 005ba200 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:610:8"]]
- 005ba200 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ba200 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:660:8"]]
+ 005ba200 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005ba200 bytes 290943f9
+ 005ba200 bytes 293143f9
~~~


<a id="compare-c1706b619dfccdbecffd91f9260ba9ed"></a>

### [`005ba3c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005ba3c4.md) → [`005ba3c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba3c4.md) FUN_005ba3c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005b8a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b8/005b8a40.md) [`005c8d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c8/005c8d50.md) [`005c98a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c9/005c98a4.md) [`005ca880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ca/005ca880.md) · 呼出先 10件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md) [`0044bf2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044bf2c.md) [`005ba8bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005ba8bc.md)
- 新版 呼出元 4件 [`005b8a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b8a40.md) [`005c8d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c8/005c8d50.md) [`005c98a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c9/005c98a4.md) [`005ca880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ca/005ca880.md) · 呼出先 10件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md) [`0044bf2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044bf2c.md) [`005ba8bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba8bc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005ba42c",
      "incomplete_value": true,
      "site": "005ba42c",
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
      "definition_site": "005ba42c",
      "incomplete_value": true,
      "site": "005ba42c",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "005ba4c8",
      "incomplete_value": true,
      "site": "005ba4c8",
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
      "definition_site": "005ba4c8",
      "incomplete_value": true,
      "site": "005ba4c8",
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005ba44c",
      "incomplete_value": false,
      "site": "005ba454",
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
      "definition_site": "005ba44c",
      "incomplete_value": false,
      "site": "005ba454",
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
      "005ba428",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "005ba43c",
      "PARAM",
      [
        "storage",
        "00bf4500",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005ba44c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005ba428",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "005ba43c",
      "PARAM",
      [
        "storage",
        "00bf4550",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005ba44c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ba428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005ba3c4.md#insn-005ba428) · [`005ba434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005ba3c4.md#insn-005ba434) · [`005ba43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005ba3c4.md#insn-005ba43c)
- 新版 `005ba428`（命令位置の公開資料なし） · `005ba434`（命令位置の公開資料なし） · `005ba43c`（命令位置の公開資料なし）

~~~diff
- 005ba428 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 005ba428 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ba428 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 005ba428 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ba428 bytes 083d45f9
+ 005ba428 bytes 085d45f9
- 005ba434 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 005ba434 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005ba434 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005ba434 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005ba434 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 005ba434 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005ba434 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005ba434 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005ba434 bytes 29213991
+ 005ba434 bytes 29613a91
- 005ba43c ["COPY", "tmp:0:8", ["const:500:8"]]
- 005ba43c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 005ba43c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 005ba43c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 005ba43c ["COPY", "tmp:0:8", ["const:550:8"]]
+ 005ba43c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 005ba43c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 005ba43c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 005ba43c bytes 42001491
+ 005ba43c bytes 42401591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dad42cb6a6ae3f9394e088082689b004"></a>

### [`005baabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005baabc.md) → [`005baabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005baabc.md) FUN_005baabc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005b8d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b8/005b8d90.md) · 呼出先 10件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md) [`0044bf2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044bf2c.md) [`005ba8bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005ba8bc.md)
- 新版 呼出元 1件 [`005b8d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b8d90.md) · 呼出先 10件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md) [`0044bf2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044bf2c.md) [`005ba8bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba8bc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.12% / 新版 98.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005bab28",
      "incomplete_value": true,
      "site": "005bab28",
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
      "definition_site": "005bab28",
      "incomplete_value": true,
      "site": "005bab28",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "005babc0",
      "incomplete_value": true,
      "site": "005babc0",
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
      "definition_site": "005babc0",
      "incomplete_value": true,
      "site": "005babc0",
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005bab48",
      "incomplete_value": false,
      "site": "005bab50",
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
      "definition_site": "005bab48",
      "incomplete_value": false,
      "site": "005bab50",
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
      "005bab24",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "005bab38",
      "PARAM",
      [
        "storage",
        "00bf4500",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005bab48",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005bab24",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "005bab38",
      "PARAM",
      [
        "storage",
        "00bf4550",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005bab48",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bab24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005baabc.md#insn-005bab24) · [`005bab30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005baabc.md#insn-005bab30) · [`005bab38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005baabc.md#insn-005bab38)
- 新版 `005bab24`（命令位置の公開資料なし） · `005bab30`（命令位置の公開資料なし） · `005bab38`（命令位置の公開資料なし）

~~~diff
- 005bab24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 005bab24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005bab24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 005bab24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005bab24 bytes 083d45f9
+ 005bab24 bytes 085d45f9
- 005bab30 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 005bab30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005bab30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005bab30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005bab30 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 005bab30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005bab30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005bab30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005bab30 bytes 29213991
+ 005bab30 bytes 29613a91
- 005bab38 ["COPY", "tmp:0:8", ["const:500:8"]]
- 005bab38 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 005bab38 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 005bab38 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 005bab38 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 005bab38 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 005bab38 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 005bab38 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 005bab38 bytes 42001491
+ 005bab38 bytes 42401591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0632fae6b7beb00d278be1b7659ee4d8"></a>

### [`005bafb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005bafb8.md) → [`005bafb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005bafb8.md) FUN_005bafb8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005b8d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b8/005b8d90.md) [`0075f8cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075f/0075f8cc.md) [`00a09be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a09/00a09be4.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 3件 [`005b8d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b8d90.md) [`0075f8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md) [`00a09c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09c28.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "005bafc4",
      "incomplete_value": false,
      "site": "005bafc8",
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
      "definition_site": "005bafc4",
      "incomplete_value": false,
      "site": "005bafc8",
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
      "005bafc4",
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
      "005bafc4",
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

- 旧版 [`005bafc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005bafb8.md#insn-005bafc4)
- 新版 `005bafc4`（命令位置の公開資料なし）

~~~diff
- 005bafc4 ["COPY", "tmp:0:8", ["const:303:8"]]
- 005bafc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005bafc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005bafc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005bafc4 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005bafc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005bafc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005bafc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005bafc4 bytes 000c0c91
+ 005bafc4 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-642007b7be857fc5eee5cf49abba2aad"></a>

### [`005bafcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005bafcc.md) → [`005bafcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005bafcc.md) _INIT_63

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
      "definition_site": "005bb008",
      "incomplete_value": true,
      "site": "005bb024",
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
      "definition_site": "005bb008",
      "incomplete_value": true,
      "site": "005bb024",
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
      "definition_site": "005bb04c",
      "incomplete_value": true,
      "site": "005bb068",
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
      "definition_site": "005bb04c",
      "incomplete_value": true,
      "site": "005bb068",
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
      "definition_site": "005bb06c",
      "incomplete_value": true,
      "site": "005bb084",
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
      "definition_site": "005bb06c",
      "incomplete_value": true,
      "site": "005bb084",
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
      "005bb008",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "005bb02c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "005bb04c",
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
      "005bb008",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "005bb02c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "005bb04c",
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

- 旧版 [`005baff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005bafcc.md#insn-005baff8) · [`005bb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005bafcc.md#insn-005bb000)
- 新版 `005baff8`（命令位置の公開資料なし） · `005bb000`（命令位置の公開資料なし）

~~~diff
- 005baff8 ["COPY", "tmp:0:8", ["const:990:8"]]
- 005baff8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005baff8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005baff8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005baff8 ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 005baff8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005baff8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005baff8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005baff8 bytes 73422691
+ 005baff8 bytes 73422791
- 005bb000 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 005bb000 bytes 69e7ff90
+ 005bb000 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 005bb000 bytes 69e7ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4be3bfe29cfce7173ef93e1d24115b4"></a>

### [`005bb810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bb/005bb810.md) → [`005bb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb810.md) _INIT_64

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.53% / 新版 91.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005bb84c",
      "incomplete_value": true,
      "site": "005bb868",
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
      "definition_site": "005bb84c",
      "incomplete_value": true,
      "site": "005bb868",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005bba38",
      "incomplete_value": false,
      "site": "005bba44",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bba38",
      "incomplete_value": false,
      "site": "005bba44",
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
            "const:9a8:8"
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
      "definition_site": "005bba40",
      "incomplete_value": false,
      "site": "005bba44",
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
      "definition_site": "005bba40",
      "incomplete_value": false,
      "site": "005bba44",
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
      "005bb84c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "005bb870",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "005bb890",
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
      "005bb84c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "005bb870",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "005bb890",
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

- 旧版 [`005bb83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bb/005bb810.md#insn-005bb83c) · [`005bb844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bb/005bb810.md#insn-005bb844)
- 新版 `005bb83c`（命令位置の公開資料なし） · `005bb844`（命令位置の公開資料なし）

~~~diff
- 005bb83c ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 005bb83c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005bb83c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005bb83c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005bb83c ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 005bb83c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005bb83c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005bb83c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005bb83c bytes 73a22691
+ 005bb83c bytes 73a22791
- 005bb844 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 005bb844 bytes 69e7ff90
+ 005bb844 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 005bb844 bytes 69e7ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e60ec49a7a6646c83f2a2f92eb736241"></a>

### [`005bcea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bcea8.md) → [`005bcea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bcea8.md) FUN_005bcea8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00996eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00996/00996eec.md) · 呼出先 29件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c1dc.md) [`0044c80c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c80c.md) [`0044c86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c86c.md)
- 新版 呼出元 1件 [`00996eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996eec.md) · 呼出先 29件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md) [`0044c80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c80c.md) [`0044c86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c86c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 98.10% / 新版 98.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005bd0bc",
      "incomplete_value": true,
      "site": "005bd0cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a15:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bd0bc",
      "incomplete_value": true,
      "site": "005bd0cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aa2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005bd9c8",
      "incomplete_value": false,
      "site": "005bd9c8",
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
      "definition_site": "005bd9c8",
      "incomplete_value": false,
      "site": "005bd9c8",
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
    "ordinal": 81,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005bd120",
      "incomplete_value": false,
      "site": "005bd128",
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
      "definition_site": "005bd120",
      "incomplete_value": false,
      "site": "005bd128",
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
      "005bd038",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "005bd0bc",
      "READ",
      [
        "storage",
        "00292aa2",
        null,
        "string"
      ]
    ],
    [
      "005bd120",
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
      "005bd038",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "005bd0bc",
      "READ",
      [
        "storage",
        "00292a15",
        null,
        "string"
      ]
    ],
    [
      "005bd120",
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

- 旧版 [`005bd034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bcea8.md#insn-005bd034) · [`005bd0b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bcea8.md#insn-005bd0b8) · [`005bd120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bcea8.md#insn-005bd120)
- 新版 `005bd034`（命令位置の公開資料なし） · `005bd0b8`（命令位置の公開資料なし） · `005bd120`（命令位置の公開資料なし）

~~~diff
- 005bd034 ["COPY", "tmp:0:8", ["const:38:8"]]
- 005bd034 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005bd034 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005bd034 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005bd034 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 005bd034 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005bd034 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005bd034 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005bd034 bytes 08e10091
+ 005bd034 bytes 08e10191
- 005bd0b8 ["COPY", "tmp:0:8", ["const:aa2:8"]]
- 005bd0b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005bd0b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005bd0b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005bd0b8 ["COPY", "tmp:0:8", ["const:a15:8"]]
+ 005bd0b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005bd0b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005bd0b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005bd0b8 bytes 08892a91
+ 005bd0b8 bytes 08552891
- 005bd120 ["COPY", "tmp:0:8", ["const:0:8"]]
- 005bd120 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005bd120 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005bd120 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005bd120 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 005bd120 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005bd120 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005bd120 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005bd120 bytes 00000091
+ 005bd120 bytes 00000191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52109ae8f494ae5db8d3d338030e2484"></a>

### [`005bdd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bd/005bdd1c.md) → [`005bdd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bd/005bdd1c.md) FUN_005bdd1c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 24件 [`005be404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005be/005be404.md) [`005e1a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md) [`00629194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00629/00629194.md) [`0068d810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d810.md) [`006c0784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0784.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 24件 [`005be404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005be/005be404.md) [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`00629194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00629/00629194.md) [`0068d810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d810.md) [`006c0784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0784.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate, store_destination, store_value

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005bdd70",
      "incomplete_value": false,
      "site": "005bdd70",
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
      "definition_site": "005bdd70",
      "incomplete_value": false,
      "site": "005bdd70",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005bdd74",
      "incomplete_value": false,
      "site": "005bdd74",
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
      "definition_site": "005bdd74",
      "incomplete_value": false,
      "site": "005bdd74",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005bdd70",
      "incomplete_value": false,
      "site": "005bdd74",
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
      "definition_site": "005bdd70",
      "incomplete_value": false,
      "site": "005bdd74",
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
      "005bdd2c",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "005bdd38",
      "DATA",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "005bdd48",
      "PARAM",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "005bdd2c",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "005bdd38",
      "DATA",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ],
    [
      "005bdd48",
      "PARAM",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bdd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bd/005bdd1c.md#insn-005bdd28) · [`005bdd38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bd/005bdd1c.md#insn-005bdd38) · [`005bdd48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bd/005bdd1c.md#insn-005bdd48)
- 新版 `005bdd28`（命令位置の公開資料なし） · `005bdd38`（命令位置の公開資料なし） · `005bdd48`（命令位置の公開資料なし）

~~~diff
- 005bdd28 ["COPY", "tmp:0:8", ["const:38:8"]]
- 005bdd28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005bdd28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005bdd28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005bdd28 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 005bdd28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005bdd28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005bdd28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005bdd28 bytes 08e10091
+ 005bdd28 bytes 08e10191
- 005bdd38 ["COPY", "tmp:0:8", ["const:0:8"]]
- 005bdd38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005bdd38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005bdd38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005bdd38 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 005bdd38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005bdd38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005bdd38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005bdd38 bytes 00000091
+ 005bdd38 bytes 00000191
- 005bdd48 ["COPY", "tmp:0:8", ["const:38:8"]]
- 005bdd48 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005bdd48 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005bdd48 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005bdd48 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 005bdd48 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005bdd48 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005bdd48 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005bdd48 bytes 00e00091
+ 005bdd48 bytes 00e00191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71f6dd2186786f170c03459eff27eba3"></a>

### [`005be404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005be/005be404.md) → [`005be404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005be/005be404.md) FUN_005be404

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`0062fecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062fecc.md) [`00632020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00632/00632020.md) [`0068d484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d484.md) [`009eadc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009ea/009eadc8.md) · 呼出先 32件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00424bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`004264e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/004264e8.md) [`0044b660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b660.md)
- 新版 呼出元 4件 [`0062fecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062fecc.md) [`00632020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00632/00632020.md) [`0068d484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d484.md) [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) · 呼出先 32件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00424bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`004264e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/004264e8.md) [`0044b660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b660.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.27% / 新版 91.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_destination` 4件, `store_value` 10件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005be4d0",
      "incomplete_value": true,
      "site": "005be4d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005be4d0",
      "incomplete_value": true,
      "site": "005be4d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef1:8"
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
      "definition_site": "005be618",
      "incomplete_value": true,
      "site": "005be62c",
      "value": [
        "LOAD",
        "8",
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
                "const:18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005be618",
      "incomplete_value": true,
      "site": "005be62c",
      "value": [
        "LOAD",
        "8",
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
                "const:18:8"
              ]
            ]
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
      "definition_site": "005be664",
      "incomplete_value": true,
      "site": "005be66c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005be664",
      "incomplete_value": true,
      "site": "005be66c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005be4ac",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "005be4c0",
      "READ",
      [
        "storage",
        "00299ef1",
        null,
        "string"
      ]
    ],
    [
      "005be510",
      "READ",
      [
        "storage",
        "002a97ec",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005be4ac",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "005be4c0",
      "READ",
      [
        "storage",
        "00299eef",
        null,
        "string"
      ]
    ],
    [
      "005be510",
      "READ",
      [
        "storage",
        "002a97fb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005be4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005be/005be404.md#insn-005be4a8) · [`005be4b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005be/005be404.md#insn-005be4b4)
- 新版 `005be4a8`（命令位置の公開資料なし） · `005be4b4`（命令位置の公開資料なし）

~~~diff
- 005be4a8 ["COPY", "tmp:0:8", ["const:38:8"]]
- 005be4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005be4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005be4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005be4a8 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 005be4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005be4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005be4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005be4a8 bytes 08e10091
+ 005be4a8 bytes 08e10191
- 005be4b4 ["COPY", "register:4048:8", ["const:299000:8"]]
- 005be4b4 bytes c9e6fff0
+ 005be4b4 ["COPY", "register:4048:8", ["const:299000:8"]]
+ 005be4b4 bytes c9e6fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a25712440bec1f8d578f49e917842f00"></a>

### [`005bf364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bf/005bf364.md) → [`005bf364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bf/005bf364.md) FUN_005bf364

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0068f070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068f/0068f070.md) [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) · 呼出先 9件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00447a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447a10.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00467c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467c58.md) [`00467c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467c60.md)
- 新版 呼出元 2件 [`0068f070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068f/0068f070.md) [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 9件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00447a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447a10.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00467c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c58.md) [`00467c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.41% / 新版 98.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005bf52c",
      "incomplete_value": true,
      "site": "005bf540",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "005bf52c",
      "incomplete_value": true,
      "site": "005bf540",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 23,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005bf528",
      "incomplete_value": false,
      "site": "005bf540",
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
      "definition_site": "005bf528",
      "incomplete_value": false,
      "site": "005bf540",
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
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005bf534",
      "incomplete_value": false,
      "site": "005bf540",
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
      "definition_site": "005bf534",
      "incomplete_value": false,
      "site": "005bf540",
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
    "ordinal": 23,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005bf528",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005bf52c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "005bf534",
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
      "005bf528",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005bf52c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "005bf534",
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

- 旧版 [`005bf528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bf/005bf364.md#insn-005bf528) · [`005bf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bf/005bf364.md#insn-005bf52c) · [`005bf534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bf/005bf364.md#insn-005bf534)
- 新版 `005bf528`（命令位置の公開資料なし） · `005bf52c`（命令位置の公開資料なし） · `005bf534`（命令位置の公開資料なし）

~~~diff
- 005bf528 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 005bf528 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005bf528 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005bf528 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005bf528 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 005bf528 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005bf528 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005bf528 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005bf528 bytes 21203991
+ 005bf528 bytes 21603a91
- 005bf52c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 005bf52c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005bf52c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 005bf52c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005bf52c bytes 003d45f9
+ 005bf52c bytes 005d45f9
- 005bf534 ["COPY", "tmp:0:8", ["const:500:8"]]
- 005bf534 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 005bf534 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 005bf534 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 005bf534 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 005bf534 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 005bf534 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 005bf534 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 005bf534 bytes 42001491
+ 005bf534 bytes 42401591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d6f6f2843664de74d52aba826d48f87"></a>

### [`005c03ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c0/005c03ec.md) → [`005c03ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c0/005c03ec.md) _INIT_65

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005c0428",
      "incomplete_value": true,
      "site": "005c0444",
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
      "definition_site": "005c0428",
      "incomplete_value": true,
      "site": "005c0444",
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
      "definition_site": "005c044c",
      "incomplete_value": true,
      "site": "005c0468",
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
      "definition_site": "005c044c",
      "incomplete_value": true,
      "site": "005c0468",
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
      "definition_site": "005c048c",
      "incomplete_value": true,
      "site": "005c04a4",
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
      "definition_site": "005c048c",
      "incomplete_value": true,
      "site": "005c04a4",
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
      "005c0428",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "005c044c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "005c046c",
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
      "005c0428",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "005c044c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "005c046c",
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

- 旧版 [`005c0418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c0/005c03ec.md#insn-005c0418) · [`005c0424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c0/005c03ec.md#insn-005c0424) · [`005c0440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c0/005c03ec.md#insn-005c0440)
- 新版 `005c0418`（命令位置の公開資料なし） · `005c0424`（命令位置の公開資料なし） · `005c0440`（命令位置の公開資料なし）

~~~diff
- 005c0418 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 005c0418 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005c0418 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005c0418 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005c0418 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005c0418 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005c0418 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005c0418 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005c0418 bytes 73022791
+ 005c0418 bytes 73022891
- 005c0424 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 005c0424 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005c0424 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005c0424 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005c0424 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 005c0424 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005c0424 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005c0424 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005c0424 bytes 29750b91
+ 005c0424 bytes 29dd0d91
- 005c0440 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 005c0440 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005c0440 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005c0440 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005c0440 ["COPY", "tmp:0:8", ["const:38a:8"]]
+ 005c0440 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005c0440 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005c0440 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005c0440 bytes 4ac10b91
+ 005c0440 bytes 4a290e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79b22cc339992f44cbcbd156cf94444d"></a>

### [`005c077c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c0/005c077c.md) → [`005c077c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c0/005c077c.md) _INIT_66

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
      "definition_site": "005c07b8",
      "incomplete_value": true,
      "site": "005c07d4",
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
      "definition_site": "005c07b8",
      "incomplete_value": true,
      "site": "005c07d4",
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
      "definition_site": "005c07fc",
      "incomplete_value": true,
      "site": "005c0818",
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
      "definition_site": "005c07fc",
      "incomplete_value": true,
      "site": "005c0818",
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
      "definition_site": "005c081c",
      "incomplete_value": true,
      "site": "005c0834",
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
      "definition_site": "005c081c",
      "incomplete_value": true,
      "site": "005c0834",
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
      "005c07b8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "005c07dc",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "005c07fc",
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
      "005c07b8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "005c07dc",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "005c07fc",
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

- 旧版 [`005c07a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c0/005c077c.md#insn-005c07a8) · [`005c07b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c0/005c077c.md#insn-005c07b0)
- 新版 `005c07a8`（命令位置の公開資料なし） · `005c07b0`（命令位置の公開資料なし）

~~~diff
- 005c07a8 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 005c07a8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005c07a8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005c07a8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005c07a8 ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 005c07a8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005c07a8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005c07a8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005c07a8 bytes 73622791
+ 005c07a8 bytes 73622891
- 005c07b0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 005c07b0 bytes 29e7fff0
+ 005c07b0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 005c07b0 bytes 29e7fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f9ee47beb074ccb0e52b616031ce2a5"></a>

### [`005c0b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c0/005c0b0c.md) → [`005c0b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c0/005c0b0c.md) FUN_005c0b0c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.40% / 新版 98.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005c0b4c",
      "incomplete_value": true,
      "site": "005c0b58",
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
      "definition_site": "005c0b4c",
      "incomplete_value": true,
      "site": "005c0b58",
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
      "005c0b58",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "005c0b80",
      "READ",
      [
        "storage",
        "002a9816",
        null,
        "string"
      ]
    ],
    [
      "005c0b84",
      "READ",
      [
        "storage",
        "002a9825",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005c0b58",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "005c0b80",
      "READ",
      [
        "storage",
        "002a9825",
        null,
        "string"
      ]
    ],
    [
      "005c0b84",
      "READ",
      [
        "storage",
        "002a9834",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c0b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c0/005c0b0c.md#insn-005c0b4c) · [`005c0b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c0/005c0b0c.md#insn-005c0b78) · [`005c0b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c0/005c0b0c.md#insn-005c0b7c)
- 新版 `005c0b4c`（命令位置の公開資料なし） · `005c0b78`（命令位置の公開資料なし）

~~~diff
- 005c0b4c ["COPY", "tmp:0:8", ["const:d28:8"]]
- 005c0b4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005c0b4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005c0b4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005c0b4c ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 005c0b4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005c0b4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005c0b4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005c0b4c bytes 08a13491
+ 005c0b4c bytes 08e13591
- 005c0b78 ["COPY", "tmp:0:8", ["const:816:8"]]
- 005c0b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005c0b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005c0b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005c0b78 ["COPY", "tmp:0:8", ["const:825:8"]]
+ 005c0b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005c0b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005c0b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005c0b78 bytes 08592091
+ 005c0b78 bytes 08952091
- 005c0b7c ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 005c0b7c bytes 89e7ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57141f406953528ba8744d0b6e9cc522"></a>

### [`005c1d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c1/005c1d18.md) → [`005c1d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c1/005c1d18.md) _INIT_67

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005c1d54",
      "incomplete_value": true,
      "site": "005c1d70",
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
      "definition_site": "005c1d54",
      "incomplete_value": true,
      "site": "005c1d70",
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
      "definition_site": "005c1db8",
      "incomplete_value": true,
      "site": "005c1dd0",
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
      "definition_site": "005c1db8",
      "incomplete_value": true,
      "site": "005c1dd0",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005c1dd4",
      "incomplete_value": true,
      "site": "005c1df0",
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
      "definition_site": "005c1dd4",
      "incomplete_value": true,
      "site": "005c1df0",
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
      "005c1d54",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "005c1d78",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "005c1d98",
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
      "005c1d54",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "005c1d78",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "005c1d98",
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

- 旧版 [`005c1d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c1/005c1d18.md#insn-005c1d44) · [`005c1d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c1/005c1d18.md#insn-005c1d4c)
- 新版 `005c1d44`（命令位置の公開資料なし） · `005c1d4c`（命令位置の公開資料なし）

~~~diff
- 005c1d44 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 005c1d44 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005c1d44 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005c1d44 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005c1d44 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 005c1d44 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005c1d44 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005c1d44 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005c1d44 bytes 73c22791
+ 005c1d44 bytes 73c22891
- 005c1d4c ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 005c1d4c bytes 29e7ffd0
+ 005c1d4c ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 005c1d4c bytes 29e7ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a05e614519df02349a902af0218640e"></a>

### [`005c2380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2380.md) → [`005c2380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2380.md) _INIT_68

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005c23bc",
      "incomplete_value": true,
      "site": "005c23d8",
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
      "definition_site": "005c23bc",
      "incomplete_value": true,
      "site": "005c23d8",
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
      "definition_site": "005c23e0",
      "incomplete_value": true,
      "site": "005c23fc",
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
      "definition_site": "005c23e0",
      "incomplete_value": true,
      "site": "005c23fc",
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
      "definition_site": "005c2400",
      "incomplete_value": true,
      "site": "005c241c",
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
      "definition_site": "005c2400",
      "incomplete_value": true,
      "site": "005c241c",
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
      "005c23bc",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "005c23e0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "005c2400",
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
      "005c23bc",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "005c23e0",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "005c2400",
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

- 旧版 [`005c23ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2380.md#insn-005c23ac) · [`005c23b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2380.md#insn-005c23b4)
- 新版 `005c23ac`（命令位置の公開資料なし） · `005c23b4`（命令位置の公開資料なし）

~~~diff
- 005c23ac ["COPY", "tmp:0:8", ["const:a08:8"]]
- 005c23ac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005c23ac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005c23ac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005c23ac ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 005c23ac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005c23ac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005c23ac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005c23ac bytes 73222891
+ 005c23ac bytes 73222991
- 005c23b4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 005c23b4 bytes 29e7ffb0
+ 005c23b4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 005c23b4 bytes 29e7ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c24622c1997f8bc8870611e6be972c34"></a>

### [`005c361c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c3/005c361c.md) → [`005c361c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c3/005c361c.md) _INIT_69

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005c3658",
      "incomplete_value": true,
      "site": "005c3674",
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
      "definition_site": "005c3658",
      "incomplete_value": true,
      "site": "005c3674",
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
      "definition_site": "005c36bc",
      "incomplete_value": true,
      "site": "005c36d4",
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
                "const:6ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c36bc",
      "incomplete_value": true,
      "site": "005c36d4",
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
                "const:73b:8"
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
      "definition_site": "005c3844",
      "incomplete_value": false,
      "site": "005c3850",
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
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c3844",
      "incomplete_value": false,
      "site": "005c3850",
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
            "const:a20:8"
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
      "005c3658",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "005c367c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "005c369c",
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
      "005c3658",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "005c367c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "005c369c",
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

- 旧版 [`005c3648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c3/005c361c.md#insn-005c3648) · [`005c3650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c3/005c361c.md#insn-005c3650)
- 新版 `005c3648`（命令位置の公開資料なし） · `005c3650`（命令位置の公開資料なし）

~~~diff
- 005c3648 ["COPY", "tmp:0:8", ["const:a20:8"]]
- 005c3648 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005c3648 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005c3648 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005c3648 ["COPY", "tmp:0:8", ["const:a60:8"]]
+ 005c3648 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005c3648 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005c3648 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005c3648 bytes 73822891
+ 005c3648 bytes 73822991
- 005c3650 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 005c3650 bytes 29e7ff90
+ 005c3650 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 005c3650 bytes 29e7ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1739056a8c80de6b8eb6ea5e050583b"></a>

### [`005c47c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c4/005c47c4.md) → [`005c47c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c4/005c47c4.md) FUN_005c47c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005c43a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c4/005c43a4.md) [`005c47c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c4/005c47c4.md) · 呼出先 43件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md)
- 新版 呼出元 2件 [`005c43a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c4/005c43a4.md) [`005c47c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c4/005c47c4.md) · 呼出先 43件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 98.05% / 新版 98.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件, `store_value` 10件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005c4808",
      "incomplete_value": false,
      "site": "005c4810",
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
      "definition_site": "005c4808",
      "incomplete_value": false,
      "site": "005c4810",
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
      "definition_site": "005c4834",
      "incomplete_value": true,
      "site": "005c4834",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:723:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c4834",
      "incomplete_value": true,
      "site": "005c4834",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:698:8"
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
      "definition_site": "005c51b0",
      "incomplete_value": true,
      "site": "005c51c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:803:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c51b0",
      "incomplete_value": true,
      "site": "005c51c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 82,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005c4810",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "005c4828",
      "READ",
      [
        "storage",
        "0029e698",
        null,
        "string"
      ]
    ],
    [
      "005c4a14",
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
      "005c4810",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "005c4828",
      "READ",
      [
        "storage",
        "0029e723",
        null,
        "string"
      ]
    ],
    [
      "005c4a14",
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

- 旧版 [`005c4808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c4/005c47c4.md#insn-005c4808) · [`005c4824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c4/005c47c4.md#insn-005c4824) · [`005c4a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c4/005c47c4.md#insn-005c4a14)
- 新版 `005c4808`（命令位置の公開資料なし） · `005c4824`（命令位置の公開資料なし） · `005c4a14`（命令位置の公開資料なし）

~~~diff
- 005c4808 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 005c4808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005c4808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005c4808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005c4808 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 005c4808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005c4808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005c4808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005c4808 bytes 08a13491
+ 005c4808 bytes 08e13591
- 005c4824 ["COPY", "tmp:0:8", ["const:698:8"]]
- 005c4824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005c4824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005c4824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005c4824 ["COPY", "tmp:0:8", ["const:723:8"]]
+ 005c4824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005c4824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005c4824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005c4824 bytes 08611a91
+ 005c4824 bytes 088d1c91
- 005c4a14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 005c4a14 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005c4a14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 005c4a14 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005c4a14 bytes 003d45f9
+ 005c4a14 bytes 005d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4af7cf1841b46d1b272d4ecfdf379af0"></a>

### [`005c8d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c8/005c8d50.md) → [`005c8d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c8/005c8d50.md) FUN_005c8d50

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) · 呼出先 37件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00445044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445044.md)
- 新版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 37件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00445044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445044.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 99.72% / 新版 99.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005c8d90",
      "incomplete_value": true,
      "site": "005c8d90",
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
      "definition_site": "005c8d90",
      "incomplete_value": true,
      "site": "005c8d90",
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
      "definition_site": "005c8d98",
      "incomplete_value": false,
      "site": "005c8da8",
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
      "definition_site": "005c8d98",
      "incomplete_value": false,
      "site": "005c8da8",
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
      "definition_site": "005c8da0",
      "incomplete_value": false,
      "site": "005c8da8",
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
      "definition_site": "005c8da0",
      "incomplete_value": false,
      "site": "005c8da8",
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
      "005c8d8c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "005c8d98",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005c8da0",
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
      "005c8d8c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "005c8d98",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005c8da0",
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

- 旧版 [`005c8d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c8/005c8d50.md#insn-005c8d8c) · [`005c8d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c8/005c8d50.md#insn-005c8d98) · [`005c8da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c8/005c8d50.md#insn-005c8da0)
- 新版 `005c8d8c`（命令位置の公開資料なし） · `005c8d98`（命令位置の公開資料なし） · `005c8da0`（命令位置の公開資料なし）

~~~diff
- 005c8d8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 005c8d8c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005c8d8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 005c8d8c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005c8d8c bytes 003d45f9
+ 005c8d8c bytes 005d45f9
- 005c8d98 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 005c8d98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005c8d98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005c8d98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005c8d98 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 005c8d98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005c8d98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005c8d98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005c8d98 bytes 21203991
+ 005c8d98 bytes 21603a91
- 005c8da0 ["COPY", "tmp:0:8", ["const:500:8"]]
- 005c8da0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 005c8da0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 005c8da0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 005c8da0 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 005c8da0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 005c8da0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 005c8da0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 005c8da0 bytes 42001491
+ 005c8da0 bytes 42401591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5b93a3a011b9cbe76f372bcb97dff64"></a>

### [`005c98a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c9/005c98a4.md) → [`005c98a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c9/005c98a4.md) FUN_005c98a4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) · 呼出先 38件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00445124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445124.md) [`00445d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d04.md)
- 新版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 38件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00445124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445124.md) [`00445d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d04.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.80% / 新版 99.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005c98f0",
      "incomplete_value": false,
      "site": "005c9900",
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
      "definition_site": "005c98f0",
      "incomplete_value": false,
      "site": "005c9900",
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
      "definition_site": "005c98f8",
      "incomplete_value": false,
      "site": "005c9900",
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
      "definition_site": "005c98f8",
      "incomplete_value": false,
      "site": "005c9900",
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
      "005c98e0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "005c98f0",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005c98f8",
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
      "005c98e0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "005c98f0",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005c98f8",
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

- 旧版 [`005c98e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c9/005c98a4.md#insn-005c98e0) · [`005c98f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c9/005c98a4.md#insn-005c98f0) · [`005c98f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c9/005c98a4.md#insn-005c98f8)
- 新版 `005c98e0`（命令位置の公開資料なし） · `005c98f0`（命令位置の公開資料なし） · `005c98f8`（命令位置の公開資料なし）

~~~diff
- 005c98e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 005c98e0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005c98e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 005c98e0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005c98e0 bytes 003d45f9
+ 005c98e0 bytes 005d45f9
- 005c98f0 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 005c98f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005c98f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005c98f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005c98f0 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 005c98f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005c98f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005c98f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005c98f0 bytes 21203991
+ 005c98f0 bytes 21603a91
- 005c98f8 ["COPY", "tmp:0:8", ["const:500:8"]]
- 005c98f8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 005c98f8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 005c98f8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 005c98f8 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 005c98f8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 005c98f8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 005c98f8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 005c98f8 bytes 42001491
+ 005c98f8 bytes 42401591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9b7eaa0c385d0f0a7a839f540d920be"></a>

### [`005ca880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ca/005ca880.md) → [`005ca880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ca/005ca880.md) FUN_005ca880

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) · 呼出先 34件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`004452e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/004452e8.md)
- 新版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 34件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`004452e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/004452e8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.63% / 新版 99.63%

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
      "definition_site": "005ca8c8",
      "incomplete_value": true,
      "site": "005ca8c8",
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
      "definition_site": "005ca8c8",
      "incomplete_value": true,
      "site": "005ca8c8",
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
      "definition_site": "005ca8d0",
      "incomplete_value": false,
      "site": "005ca8e0",
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
      "definition_site": "005ca8d0",
      "incomplete_value": false,
      "site": "005ca8e0",
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
      "definition_site": "005ca8d8",
      "incomplete_value": false,
      "site": "005ca8e0",
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
      "definition_site": "005ca8d8",
      "incomplete_value": false,
      "site": "005ca8e0",
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
      "005ca8b8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "005ca8d0",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005ca8d8",
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
      "005ca8b8",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "005ca8d0",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005ca8d8",
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

- 旧版 [`005ca8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ca/005ca880.md#insn-005ca8b8) · [`005ca8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ca/005ca880.md#insn-005ca8d0) · [`005ca8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ca/005ca880.md#insn-005ca8d8)
- 新版 `005ca8b8`（命令位置の公開資料なし） · `005ca8d0`（命令位置の公開資料なし） · `005ca8d8`（命令位置の公開資料なし）

~~~diff
- 005ca8b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 005ca8b8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ca8b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 005ca8b8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005ca8b8 bytes 003d45f9
+ 005ca8b8 bytes 005d45f9
- 005ca8d0 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 005ca8d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005ca8d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005ca8d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005ca8d0 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 005ca8d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005ca8d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005ca8d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005ca8d0 bytes 21203991
+ 005ca8d0 bytes 21603a91
- 005ca8d8 ["COPY", "tmp:0:8", ["const:500:8"]]
- 005ca8d8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 005ca8d8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 005ca8d8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 005ca8d8 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 005ca8d8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 005ca8d8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 005ca8d8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 005ca8d8 bytes 42001491
+ 005ca8d8 bytes 42401591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac54847499e03e2f96c203f39bdc9691"></a>

### [`005cb228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cb/005cb228.md) → [`005cb228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cb/005cb228.md) FUN_005cb228

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005c47c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c4/005c47c4.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`005c47c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c4/005c47c4.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "005cb234",
      "incomplete_value": false,
      "site": "005cb238",
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
      "definition_site": "005cb234",
      "incomplete_value": false,
      "site": "005cb238",
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
      "005cb234",
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
      "005cb234",
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

- 旧版 [`005cb234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cb/005cb228.md#insn-005cb234)
- 新版 `005cb234`（命令位置の公開資料なし）

~~~diff
- 005cb234 ["COPY", "tmp:0:8", ["const:303:8"]]
- 005cb234 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005cb234 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005cb234 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005cb234 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005cb234 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005cb234 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005cb234 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005cb234 bytes 000c0c91
+ 005cb234 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe9d3089d9356530c3e48ae5299d9655"></a>

### [`005cb46c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cb/005cb46c.md) → [`005cb46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cb/005cb46c.md) FUN_005cb46c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005cb23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cb/005cb23c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005cb23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cb/005cb23c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "005cb478",
      "incomplete_value": false,
      "site": "005cb47c",
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
      "definition_site": "005cb478",
      "incomplete_value": false,
      "site": "005cb47c",
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
      "005cb478",
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
      "005cb478",
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

- 旧版 [`005cb478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cb/005cb46c.md#insn-005cb478)
- 新版 `005cb478`（命令位置の公開資料なし）

~~~diff
- 005cb478 ["COPY", "tmp:0:8", ["const:303:8"]]
- 005cb478 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005cb478 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005cb478 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005cb478 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005cb478 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005cb478 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005cb478 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005cb478 bytes 000c0c91
+ 005cb478 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9deba8136007d9f20aa1aa8d92a647ef"></a>

### [`005cb480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cb/005cb480.md) → [`005cb480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cb/005cb480.md) FUN_005cb480

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`005c43a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c4/005c43a4.md) [`005c7548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c7/005c7548.md) [`005c8d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c8/005c8d50.md) [`005c98a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c9/005c98a4.md) [`005ca880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ca/005ca880.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 5件 [`005c43a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c4/005c43a4.md) [`005c7548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c7/005c7548.md) [`005c8d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c8/005c8d50.md) [`005c98a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c9/005c98a4.md) [`005ca880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ca/005ca880.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "005cb48c",
      "incomplete_value": false,
      "site": "005cb490",
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
      "definition_site": "005cb48c",
      "incomplete_value": false,
      "site": "005cb490",
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
      "005cb48c",
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
      "005cb48c",
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

- 旧版 [`005cb48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cb/005cb480.md#insn-005cb48c)
- 新版 `005cb48c`（命令位置の公開資料なし）

~~~diff
- 005cb48c ["COPY", "tmp:0:8", ["const:303:8"]]
- 005cb48c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005cb48c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005cb48c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005cb48c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005cb48c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005cb48c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005cb48c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005cb48c bytes 000c0c91
+ 005cb48c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b161df2f26defa51808356e8ea71dc37"></a>

### [`005cbd64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cb/005cbd64.md) → [`005cbd64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cb/005cbd64.md) FUN_005cbd64

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005cb494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cb/005cb494.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005cb494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cb/005cb494.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "005cbd70",
      "incomplete_value": false,
      "site": "005cbd74",
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
      "definition_site": "005cbd70",
      "incomplete_value": false,
      "site": "005cbd74",
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
      "005cbd70",
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
      "005cbd70",
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

- 旧版 [`005cbd70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cb/005cbd64.md#insn-005cbd70)
- 新版 `005cbd70`（命令位置の公開資料なし）

~~~diff
- 005cbd70 ["COPY", "tmp:0:8", ["const:303:8"]]
- 005cbd70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005cbd70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005cbd70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005cbd70 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005cbd70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005cbd70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005cbd70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005cbd70 bytes 000c0c91
+ 005cbd70 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0281faf4be78c4742461343566aab743"></a>

### [`005cc224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cc/005cc224.md) → [`005cc224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cc/005cc224.md) _INIT_70

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.40% / 新版 90.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005cc260",
      "incomplete_value": true,
      "site": "005cc27c",
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
      "definition_site": "005cc260",
      "incomplete_value": true,
      "site": "005cc27c",
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
      "definition_site": "005cc284",
      "incomplete_value": true,
      "site": "005cc2a0",
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
      "definition_site": "005cc284",
      "incomplete_value": true,
      "site": "005cc2a0",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005cc44c",
      "incomplete_value": false,
      "site": "005cc458",
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
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cc44c",
      "incomplete_value": false,
      "site": "005cc458",
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
            "const:a38:8"
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
      "005cc260",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "005cc284",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "005cc2a4",
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
      "005cc260",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "005cc284",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "005cc2a4",
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

- 旧版 [`005cc250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cc/005cc224.md#insn-005cc250) · [`005cc258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cc/005cc224.md#insn-005cc258)
- 新版 `005cc250`（命令位置の公開資料なし） · `005cc258`（命令位置の公開資料なし）

~~~diff
- 005cc250 ["COPY", "tmp:0:8", ["const:a38:8"]]
- 005cc250 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005cc250 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005cc250 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005cc250 ["COPY", "tmp:0:8", ["const:a78:8"]]
+ 005cc250 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005cc250 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005cc250 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005cc250 bytes 73e22891
+ 005cc250 bytes 73e22991
- 005cc258 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 005cc258 bytes c9e6fff0
+ 005cc258 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 005cc258 bytes c9e6fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e58b4b3fd5a849c0a09173b623c73e2d"></a>

### [`005cc5b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cc/005cc5b4.md) → [`005cc5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cc/005cc5b4.md) _INIT_71

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.96% / 新版 90.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005cc670",
      "incomplete_value": true,
      "site": "005cc68c",
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
      "definition_site": "005cc670",
      "incomplete_value": true,
      "site": "005cc68c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005cc7dc",
      "incomplete_value": false,
      "site": "005cc7e8",
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
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cc7dc",
      "incomplete_value": false,
      "site": "005cc7e8",
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
            "const:a50:8"
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
      "definition_site": "005cc7e4",
      "incomplete_value": false,
      "site": "005cc7e8",
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
      "definition_site": "005cc7e4",
      "incomplete_value": false,
      "site": "005cc7e8",
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
      "005cc5f0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "005cc614",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "005cc634",
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
      "005cc5f0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "005cc614",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "005cc634",
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

- 旧版 [`005cc5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cc/005cc5b4.md#insn-005cc5e0) · [`005cc5e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cc/005cc5b4.md#insn-005cc5e8)
- 新版 `005cc5e0`（命令位置の公開資料なし） · `005cc5e8`（命令位置の公開資料なし）

~~~diff
- 005cc5e0 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 005cc5e0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005cc5e0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005cc5e0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005cc5e0 ["COPY", "tmp:0:8", ["const:a90:8"]]
+ 005cc5e0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005cc5e0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005cc5e0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005cc5e0 bytes 73422991
+ 005cc5e0 bytes 73422a91
- 005cc5e8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 005cc5e8 bytes c9e6fff0
+ 005cc5e8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 005cc5e8 bytes c9e6fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-016676cedddff6a33f58ae16d07d306d"></a>

### [`005cdcac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cd/005cdcac.md) → [`005cdcac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cd/005cdcac.md) _INIT_72

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
      "definition_site": "005cdce8",
      "incomplete_value": true,
      "site": "005cdd04",
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
      "definition_site": "005cdce8",
      "incomplete_value": true,
      "site": "005cdd04",
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
      "definition_site": "005cdd0c",
      "incomplete_value": true,
      "site": "005cdd28",
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
      "definition_site": "005cdd0c",
      "incomplete_value": true,
      "site": "005cdd28",
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
      "definition_site": "005cdd2c",
      "incomplete_value": true,
      "site": "005cdd48",
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
      "definition_site": "005cdd2c",
      "incomplete_value": true,
      "site": "005cdd48",
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
      "005cdce8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "005cdd0c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "005cdd2c",
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
      "005cdce8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "005cdd0c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "005cdd2c",
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

- 旧版 [`005cdcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cd/005cdcac.md#insn-005cdcd8) · [`005cdce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cd/005cdcac.md#insn-005cdce0)
- 新版 `005cdcd8`（命令位置の公開資料なし） · `005cdce0`（命令位置の公開資料なし）

~~~diff
- 005cdcd8 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 005cdcd8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005cdcd8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005cdcd8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005cdcd8 ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 005cdcd8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005cdcd8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005cdcd8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005cdcd8 bytes 73a22991
+ 005cdcd8 bytes 73a22a91
- 005cdce0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 005cdce0 bytes c9e6ffd0
+ 005cdce0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 005cdce0 bytes c9e6ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4063b5e82ce826444afa05fe46a42d67"></a>

### [`005cf984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cf/005cf984.md) → [`005cf984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cf/005cf984.md) FUN_005cf984

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) [`006e443c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e443c.md) · 呼出先 19件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444bb0.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`004450d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/004450d4.md) [`00445124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445124.md)
- 新版 呼出元 2件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) [`006e443c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e443c.md) · 呼出先 19件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444bb0.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`004450d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/004450d4.md) [`00445124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445124.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.80% / 新版 98.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005cf9e8",
      "incomplete_value": false,
      "site": "005cf9ec",
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
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cf9e8",
      "incomplete_value": false,
      "site": "005cf9ec",
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
            "const:d70:8"
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
      "005cf9e8",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ],
    [
      "005cfa40",
      "READ",
      [
        "storage",
        "00c1b660",
        null,
        "pointer"
      ]
    ],
    [
      "005cfa54",
      "DATA",
      [
        "storage",
        "00c2454c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005cf9e8",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ],
    [
      "005cfa40",
      "READ",
      [
        "storage",
        "00c1b6b0",
        null,
        "pointer"
      ]
    ],
    [
      "005cfa54",
      "DATA",
      [
        "storage",
        "00c2459c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cf9e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cf/005cf984.md#insn-005cf9e8) · [`005cfa40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cf/005cf984.md#insn-005cfa40) · [`005cfae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cf/005cf984.md#insn-005cfae4)
- 新版 `005cf9e8`（命令位置の公開資料なし） · `005cfa40`（命令位置の公開資料なし） · `005cfae4`（命令位置の公開資料なし）

~~~diff
- 005cf9e8 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 005cf9e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005cf9e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005cf9e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005cf9e8 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 005cf9e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005cf9e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005cf9e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005cf9e8 bytes 00c03591
+ 005cf9e8 bytes 00c03691
- 005cfa40 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:660:8"]]
- 005cfa40 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005cfa40 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6b0:8"]]
+ 005cfa40 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005cfa40 bytes 293143f9
+ 005cfa40 bytes 295943f9
- 005cfae4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:660:8"]]
- 005cfae4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 005cfae4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:6b0:8"]]
+ 005cfae4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 005cfae4 bytes 4a3143f9
+ 005cfae4 bytes 4a5943f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1e7e89d1c1c91bf5acce5c2b5533ed3"></a>

### [`005d0044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d0/005d0044.md) → [`005d0044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d0/005d0044.md) FUN_005d0044

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) · 呼出先 9件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444bb0.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00448034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 9件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444bb0.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00448034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448034.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.28% / 新版 99.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d0090",
      "incomplete_value": false,
      "site": "005d0094",
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
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d0090",
      "incomplete_value": false,
      "site": "005d0094",
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
            "const:d70:8"
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
      "005d0090",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005d0090",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d0090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d0/005d0044.md#insn-005d0090)
- 新版 `005d0090`（命令位置の公開資料なし）

~~~diff
- 005d0090 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 005d0090 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005d0090 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005d0090 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d0090 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 005d0090 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d0090 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d0090 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005d0090 bytes 00c03591
+ 005d0090 bytes 00c03691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8b1df2c4299f07b1149f6c22d8157a2"></a>

### [`005d1f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d1/005d1f2c.md) → [`005d1f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d1/005d1f2c.md) FUN_005d1f2c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) [`006e4714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4714.md) · 呼出先 8件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449c84.md) [`00449d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449d44.md)
- 新版 呼出元 2件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) [`006e4714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4714.md) · 呼出先 8件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c84.md) [`00449d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449d44.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.00% / 新版 99.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d2384",
      "incomplete_value": true,
      "site": "005d2388",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d2384",
      "incomplete_value": true,
      "site": "005d2388",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
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
      "005d21cc",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "005d21d0",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ],
    [
      "005d21e4",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005d21cc",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "005d21d0",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ],
    [
      "005d21e4",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d21cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d1/005d1f2c.md#insn-005d21cc) · [`005d2380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d1/005d1f2c.md#insn-005d2380)
- 新版 `005d21cc`（命令位置の公開資料なし） · `005d2380`（命令位置の公開資料なし）

~~~diff
- 005d21cc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d28:8"]]
- 005d21cc ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d21cc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d78:8"]]
+ 005d21cc ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 005d21cc bytes d69646f9
+ 005d21cc bytes d6be46f9
- 005d2380 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d28:8"]]
- 005d2380 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d2380 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d78:8"]]
+ 005d2380 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 005d2380 bytes d69646f9
+ 005d2380 bytes d6be46f9
~~~


<a id="compare-e15fe8648068a7e04f688169fba892dd"></a>

### [`005d2408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d2/005d2408.md) → [`005d2408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d2/005d2408.md) FUN_005d2408

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) [`006e45a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e45a8.md) · 呼出先 11件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00448040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448040.md) [`00449c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449c34.md)
- 新版 呼出元 2件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) [`006e45a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e45a8.md) · 呼出先 11件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00448040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448040.md) [`00449c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c34.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.89% / 新版 97.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d24a8",
      "incomplete_value": true,
      "site": "005d24ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d24a8",
      "incomplete_value": true,
      "site": "005d24ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
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
      "definition_site": "005d25e8",
      "incomplete_value": true,
      "site": "005d25f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d25e8",
      "incomplete_value": true,
      "site": "005d25f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
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
      "definition_site": "005d273c",
      "incomplete_value": true,
      "site": "005d2748",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d273c",
      "incomplete_value": true,
      "site": "005d2748",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d24a4",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "005d24a8",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ],
    [
      "005d24d8",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005d24a4",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "005d24a8",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ],
    [
      "005d24d8",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d24a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d2/005d2408.md#insn-005d24a4) · [`005d25e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d2/005d2408.md#insn-005d25e0) · [`005d2734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d2/005d2408.md#insn-005d2734)
- 新版 `005d24a4`（命令位置の公開資料なし） · `005d25e0`（命令位置の公開資料なし） · `005d2734`（命令位置の公開資料なし）

~~~diff
- 005d24a4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d28:8"]]
- 005d24a4 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d24a4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d78:8"]]
+ 005d24a4 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 005d24a4 bytes f79646f9
+ 005d24a4 bytes f7be46f9
- 005d25e0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d28:8"]]
- 005d25e0 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d25e0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d78:8"]]
+ 005d25e0 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 005d25e0 bytes d69646f9
+ 005d25e0 bytes d6be46f9
- 005d2734 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d28:8"]]
- 005d2734 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d2734 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d78:8"]]
+ 005d2734 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 005d2734 bytes d69646f9
+ 005d2734 bytes d6be46f9
~~~


<a id="compare-abb48545638b670cbd57118f9914504d"></a>

### [`005d287c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d2/005d287c.md) → [`005d287c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d2/005d287c.md) FUN_005d287c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 8件 [`0044beb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044beb4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`005bc058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bc058.md) [`009019f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/009019f4.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 8件 [`0044beb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044beb4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`005bc058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc058.md) [`009019f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/009019f4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.89% / 新版 95.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d294c",
      "incomplete_value": true,
      "site": "005d2954",
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
                "const:add:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d294c",
      "incomplete_value": true,
      "site": "005d2954",
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
                "const:b6a:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d28dc",
      "incomplete_value": true,
      "site": "005d28e4",
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
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d28dc",
      "incomplete_value": true,
      "site": "005d28e4",
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
            "const:500:8"
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
      "005d28bc",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "005d28d4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d28dc",
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
      "005d28bc",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "005d28d4",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d28dc",
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

- 旧版 [`005d28bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d2/005d287c.md#insn-005d28bc) · [`005d28d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d2/005d287c.md#insn-005d28d4) · [`005d28dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d2/005d287c.md#insn-005d28dc)
- 新版 `005d28bc`（命令位置の公開資料なし） · `005d28d4`（命令位置の公開資料なし） · `005d28dc`（命令位置の公開資料なし）

~~~diff
- 005d28bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 005d28bc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d28bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 005d28bc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005d28bc bytes 003d45f9
+ 005d28bc bytes 005d45f9
- 005d28d4 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 005d28d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005d28d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005d28d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005d28d4 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 005d28d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005d28d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005d28d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005d28d4 bytes 21203991
+ 005d28d4 bytes 21603a91
- 005d28dc ["COPY", "tmp:0:8", ["const:500:8"]]
- 005d28dc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 005d28dc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 005d28dc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 005d28dc ["COPY", "tmp:0:8", ["const:550:8"]]
+ 005d28dc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 005d28dc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 005d28dc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 005d28dc bytes 42001491
+ 005d28dc bytes 42401591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-907fd0412650632c5ba39c05cacbb607"></a>

### [`005d2c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d2/005d2c18.md) → [`005d2c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d2/005d2c18.md) FUN_005d2c18

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 18件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044beb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044beb4.md) [`0059d12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d12c.md) [`005bbc10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bb/005bbc10.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 18件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044beb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044beb4.md) [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`005bbc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bbc10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.72% / 新版 97.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d2de4",
      "incomplete_value": true,
      "site": "005d2df4",
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
                "const:ad5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d2de4",
      "incomplete_value": true,
      "site": "005d2df4",
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
                "const:b69:8"
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
      "definition_site": "005d2e44",
      "incomplete_value": true,
      "site": "005d2e54",
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
                "const:7ca:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d2e44",
      "incomplete_value": true,
      "site": "005d2e54",
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
                "const:73f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d310c",
      "incomplete_value": true,
      "site": "005d311c",
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
                "const:7ca:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d310c",
      "incomplete_value": true,
      "site": "005d311c",
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
                "const:73f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 63,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d2cf8",
      "READ",
      [
        "storage",
        "00c1b628",
        null,
        "pointer"
      ]
    ],
    [
      "005d2d84",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d2d88",
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
      "005d2cf8",
      "READ",
      [
        "storage",
        "00c1b678",
        null,
        "pointer"
      ]
    ],
    [
      "005d2d84",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d2d88",
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

- 旧版 [`005d2cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d2/005d2c18.md#insn-005d2cf8) · [`005d2d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d2/005d2c18.md#insn-005d2d84) · [`005d2d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d2/005d2c18.md#insn-005d2d88)
- 新版 `005d2cf8`（命令位置の公開資料なし） · `005d2d84`（命令位置の公開資料なし） · `005d2d88`（命令位置の公開資料なし）

~~~diff
- 005d2cf8 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:628:8"]]
- 005d2cf8 ["LOAD", "register:40e0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d2cf8 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:678:8"]]
+ 005d2cf8 ["LOAD", "register:40e0:8", ["const:1b1:8", "tmp:0:8"]]
- 005d2cf8 bytes 9c1743f9
+ 005d2cf8 bytes 9c3f43f9
- 005d2d84 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 005d2d84 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005d2d84 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005d2d84 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005d2d84 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 005d2d84 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005d2d84 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005d2d84 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005d2d84 bytes 21203991
+ 005d2d84 bytes 21603a91
- 005d2d88 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
- 005d2d88 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d2d88 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ab8:8"]]
+ 005d2d88 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005d2d88 bytes 203d45f9
+ 005d2d88 bytes 205d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dc34a8b3b61db9816265d8d6171ba8f"></a>

### [`005d4158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d4/005d4158.md) → [`005d4158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d4/005d4158.md) FUN_005d4158

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 17件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`0044ab70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ab70.md) [`0044beb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044beb4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 17件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044ab70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ab70.md) [`0044beb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044beb4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.21% / 新版 98.21%

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
      "definition_site": "005d41a0",
      "incomplete_value": true,
      "site": "005d41a0",
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
      "definition_site": "005d41a0",
      "incomplete_value": true,
      "site": "005d41a0",
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
      "definition_site": "005d41a8",
      "incomplete_value": false,
      "site": "005d41b8",
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
      "definition_site": "005d41a8",
      "incomplete_value": false,
      "site": "005d41b8",
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
      "definition_site": "005d41b0",
      "incomplete_value": false,
      "site": "005d41b8",
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
      "definition_site": "005d41b0",
      "incomplete_value": false,
      "site": "005d41b8",
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
      "005d4194",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "005d41a8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d41b0",
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
      "005d4194",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "005d41a8",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d41b0",
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

- 旧版 [`005d4194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d4/005d4158.md#insn-005d4194) · [`005d41a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d4/005d4158.md#insn-005d41a8) · [`005d41b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d4/005d4158.md#insn-005d41b0)
- 新版 `005d4194`（命令位置の公開資料なし） · `005d41a8`（命令位置の公開資料なし） · `005d41b0`（命令位置の公開資料なし）

~~~diff
- 005d4194 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 005d4194 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d4194 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 005d4194 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005d4194 bytes 003d45f9
+ 005d4194 bytes 005d45f9
- 005d41a8 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 005d41a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005d41a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005d41a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005d41a8 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 005d41a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005d41a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005d41a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005d41a8 bytes 21203991
+ 005d41a8 bytes 21603a91
- 005d41b0 ["COPY", "tmp:0:8", ["const:500:8"]]
- 005d41b0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 005d41b0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 005d41b0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 005d41b0 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 005d41b0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 005d41b0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 005d41b0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 005d41b0 bytes 42001491
+ 005d41b0 bytes 42401591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27015fc217ee37c9a61dc2e91d3d5fe4"></a>

### [`005d4988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d4/005d4988.md) → [`005d4988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d4/005d4988.md) FUN_005d4988

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 17件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0044abfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abfc.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459f04.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 17件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044abfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abfc.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f04.md)

変更の種類 call_argument_candidate, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 92.39% / 新版 92.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 21件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d4a18",
      "incomplete_value": true,
      "site": "005d4a20",
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
                "const:a25:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d4a18",
      "incomplete_value": true,
      "site": "005d4a20",
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
                "const:98b:8"
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
      "definition_site": "005d4a1c",
      "incomplete_value": true,
      "site": "005d4a24",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005d4a1c",
      "incomplete_value": true,
      "site": "005d4a24",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d4be0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d4a18",
      "READ",
      [
        "storage",
        "002a698b",
        null,
        "string"
      ]
    ],
    [
      "005d4a1c",
      "READ",
      [
        "storage",
        "002a699a",
        null,
        "string"
      ]
    ],
    [
      "005d4bd8",
      "READ",
      [
        "storage",
        "00293ad3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005d4a18",
      "READ",
      [
        "storage",
        "002a6a25",
        null,
        "string"
      ]
    ],
    [
      "005d4a1c",
      "READ",
      [
        "storage",
        "002a6a34",
        null,
        "string"
      ]
    ],
    [
      "005d4bd8",
      "READ",
      [
        "storage",
        "00293a46",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d4be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d4/005d4988.md#insn-005d4be0) · [`005d4c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d4/005d4988.md#insn-005d4c9c)
- 新版 `005d4be0`（命令位置の公開資料なし）

~~~diff
- 005d4be0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 005d4be0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 005d4be0 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:17:8"]]
- 005d4be0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 005d4be0 bytes 1f5c0039
+ 005d4be0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 005d4be0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 005d4be0 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:17:8"]]
+ 005d4be0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 005d4be0 bytes 1f5c0039
- 005d4c9c ["COPY", "tmp:0:4", ["const:0:4"]]
- 005d4c9c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 005d4c9c ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:17:8"]]
- 005d4c9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 005d4c9c bytes 1f5c0039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0af4d7c95d2e06b69b62a59a7a6e4e6f"></a>

### [`005d57d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d5/005d57d0.md) → [`005d57d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d5/005d57d0.md) FUN_005d57d0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) · 呼出先 10件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00448e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448e7c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d1dc.md) [`005d9584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d9584.md)
- 新版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 10件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00448e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448e7c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d1dc.md) [`005d9584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d9584.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d599c",
      "incomplete_value": true,
      "site": "005d59a4",
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
                "const:f06:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d599c",
      "incomplete_value": true,
      "site": "005d59a4",
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
                "const:f08:8"
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
      "definition_site": "005d599c",
      "incomplete_value": true,
      "site": "005d59a8",
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
                "const:f06:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d599c",
      "incomplete_value": true,
      "site": "005d59a8",
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
                "const:f08:8"
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
      "definition_site": "005d59ac",
      "incomplete_value": true,
      "site": "005d59ac",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005d59ac",
      "incomplete_value": true,
      "site": "005d59ac",
      "value": [
        "LOAD",
        "8",
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
      "005d5990",
      "READ",
      [
        "storage",
        "00299f17",
        null,
        "string"
      ]
    ],
    [
      "005d599c",
      "READ",
      [
        "storage",
        "00299f08",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005d5990",
      "READ",
      [
        "storage",
        "00299f15",
        null,
        "string"
      ]
    ],
    [
      "005d599c",
      "READ",
      [
        "storage",
        "00299f06",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d598c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d5/005d57d0.md#insn-005d598c)
- 新版 `005d598c`（命令位置の公開資料なし）

~~~diff
- 005d598c ["COPY", "tmp:0:8", ["const:f08:8"]]
- 005d598c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005d598c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005d598c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005d598c ["COPY", "tmp:0:8", ["const:f06:8"]]
+ 005d598c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005d598c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005d598c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005d598c bytes 08213c91
+ 005d598c bytes 08193c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-271c865ec7d84b8bdd4d21cbd358c8f5"></a>

### [`005d5afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d5/005d5afc.md) → [`005d5afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d5/005d5afc.md) FUN_005d5afc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 16件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`005d62c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d62c8.md) [`00829328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829328.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 16件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`005d62c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d6/005d62c8.md) [`00829328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829328.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.47% / 新版 95.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005d61bc",
      "incomplete_value": false,
      "site": "005d61bc",
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
      "definition_site": "005d61bc",
      "incomplete_value": false,
      "site": "005d61bc",
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
    "ordinal": 53,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005d61c0",
      "incomplete_value": false,
      "site": "005d61c0",
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
      "definition_site": "005d61c0",
      "incomplete_value": false,
      "site": "005d61c0",
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
    "ordinal": 54,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005d61bc",
      "incomplete_value": false,
      "site": "005d61c0",
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
      "definition_site": "005d61bc",
      "incomplete_value": false,
      "site": "005d61c0",
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
    "ordinal": 54,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d5e94",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "005d5eb8",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "005d5eb8",
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
      "005d5e94",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "005d5eb8",
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "005d5eb8",
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

- 旧版 [`005d5e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d5/005d5afc.md#insn-005d5e90) · [`005d5eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d5/005d5afc.md#insn-005d5eb4) · [`005d5eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d5/005d5afc.md#insn-005d5eb8)
- 新版 `005d5e90`（命令位置の公開資料なし） · `005d5eb4`（命令位置の公開資料なし） · `005d5eb8`（命令位置の公開資料なし）

~~~diff
- 005d5e90 ["COPY", "tmp:0:8", ["const:38:8"]]
- 005d5e90 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
- 005d5e90 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
- 005d5e90 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
+ 005d5e90 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 005d5e90 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
+ 005d5e90 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
+ 005d5e90 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
- 005d5e90 bytes 9ce30091
+ 005d5e90 bytes 9ce30191
- 005d5eb4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 005d5eb4 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 005d5eb4 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 005d5eb4 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 005d5eb4 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 005d5eb4 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 005d5eb4 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 005d5eb4 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 005d5eb4 bytes 94020091
+ 005d5eb4 bytes 94020191
- 005d5eb8 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:e60:8"]]
- 005d5eb8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d5eb8 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:eb0:8"]]
+ 005d5eb8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005d5eb8 bytes 423047f9
+ 005d5eb8 bytes 425847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5abd25b52fc40ced9f9f94b3f380ce24"></a>

### [`005d6638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d6638.md) → [`005d6638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d6/005d6638.md) FUN_005d6638

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 2件 [`0044beb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044beb4.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 2件 [`0044beb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044beb4.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.88% / 新版 87.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005d6650",
      "incomplete_value": true,
      "site": "005d6650",
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
      "definition_site": "005d6650",
      "incomplete_value": true,
      "site": "005d6650",
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
      "definition_site": "005d6658",
      "incomplete_value": false,
      "site": "005d666c",
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
      "definition_site": "005d6658",
      "incomplete_value": false,
      "site": "005d666c",
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
      "definition_site": "005d6660",
      "incomplete_value": false,
      "site": "005d666c",
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
      "definition_site": "005d6660",
      "incomplete_value": false,
      "site": "005d666c",
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
      "005d664c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "005d6658",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d6660",
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
      "005d664c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "005d6658",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d6660",
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

- 旧版 [`005d664c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d6638.md#insn-005d664c) · [`005d6658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d6638.md#insn-005d6658) · [`005d6660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d6638.md#insn-005d6660)
- 新版 `005d664c`（命令位置の公開資料なし） · `005d6658`（命令位置の公開資料なし） · `005d6660`（命令位置の公開資料なし）

~~~diff
- 005d664c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 005d664c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d664c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 005d664c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d664c bytes 083d45f9
+ 005d664c bytes 085d45f9
- 005d6658 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 005d6658 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005d6658 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005d6658 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005d6658 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 005d6658 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005d6658 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005d6658 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005d6658 bytes 21203991
+ 005d6658 bytes 21603a91
- 005d6660 ["COPY", "tmp:0:8", ["const:500:8"]]
- 005d6660 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 005d6660 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 005d6660 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 005d6660 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 005d6660 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 005d6660 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 005d6660 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 005d6660 bytes 42001491
+ 005d6660 bytes 42401591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b624f2e2514a470d1bde0e845ec84871"></a>

### [`005d6c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d6c3c.md) → [`005d6c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d6/005d6c3c.md) FUN_005d6c3c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005d6740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d6740.md) · 呼出先 52件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`0044abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abe4.md) [`0047c518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c518.md)
- 新版 呼出元 1件 [`005d6740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d6/005d6740.md) · 呼出先 52件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044abe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abe4.md) [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.00% / 新版 99.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d7064",
      "incomplete_value": false,
      "site": "005d7070",
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
            "const:80f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d7064",
      "incomplete_value": false,
      "site": "005d7070",
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
            "const:784:8"
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d7144",
      "incomplete_value": false,
      "site": "005d714c",
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
            "const:74a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d7144",
      "incomplete_value": false,
      "site": "005d714c",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "ordinal": 50,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d6f8c",
      "PARAM",
      [
        "storage",
        "002a5784",
        null,
        "string"
      ]
    ],
    [
      "005d7064",
      "PARAM",
      [
        "storage",
        "002a5784",
        null,
        "string"
      ]
    ],
    [
      "005d7144",
      "PARAM",
      [
        "storage",
        "002a76b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005d6f8c",
      "PARAM",
      [
        "storage",
        "002a580f",
        null,
        "string"
      ]
    ],
    [
      "005d7064",
      "PARAM",
      [
        "storage",
        "002a580f",
        null,
        "string"
      ]
    ],
    [
      "005d7144",
      "PARAM",
      [
        "storage",
        "002a774a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d6f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d6c3c.md#insn-005d6f8c) · [`005d7064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d6c3c.md#insn-005d7064) · [`005d7144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d6c3c.md#insn-005d7144)
- 新版 `005d6f8c`（命令位置の公開資料なし） · `005d7064`（命令位置の公開資料なし） · `005d7144`（命令位置の公開資料なし）

~~~diff
- 005d6f8c ["COPY", "tmp:0:8", ["const:784:8"]]
- 005d6f8c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005d6f8c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005d6f8c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d6f8c ["COPY", "tmp:0:8", ["const:80f:8"]]
+ 005d6f8c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d6f8c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d6f8c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005d6f8c bytes 00101e91
+ 005d6f8c bytes 003c2091
- 005d7064 ["COPY", "tmp:0:8", ["const:784:8"]]
- 005d7064 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005d7064 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005d7064 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d7064 ["COPY", "tmp:0:8", ["const:80f:8"]]
+ 005d7064 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d7064 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d7064 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005d7064 bytes 00101e91
+ 005d7064 bytes 003c2091
- 005d7144 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 005d7144 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005d7144 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005d7144 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005d7144 ["COPY", "tmp:0:8", ["const:74a:8"]]
+ 005d7144 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005d7144 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005d7144 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005d7144 bytes 21c01a91
+ 005d7144 bytes 21281d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3def41e050fd0916ddd4d72e6435ba72"></a>

### [`005d9534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d9534.md) → [`005d9534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d9534.md) FUN_005d9534

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005d2c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d2/005d2c18.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005d2c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d2/005d2c18.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "005d9540",
      "incomplete_value": false,
      "site": "005d9544",
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
      "definition_site": "005d9540",
      "incomplete_value": false,
      "site": "005d9544",
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
      "005d9540",
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
      "005d9540",
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

- 旧版 [`005d9540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d9534.md#insn-005d9540)
- 新版 `005d9540`（命令位置の公開資料なし）

~~~diff
- 005d9540 ["COPY", "tmp:0:8", ["const:303:8"]]
- 005d9540 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005d9540 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005d9540 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d9540 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005d9540 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d9540 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d9540 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005d9540 bytes 000c0c91
+ 005d9540 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d442c4febfeb2d29314d5e56e4fc396"></a>

### [`005d9548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d9548.md) → [`005d9548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d9548.md) FUN_005d9548

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`005d3af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d3/005d3af8.md) [`005d3f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d3/005d3f6c.md) [`005d4158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d4/005d4158.md) [`006e92bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e92bc.md) [`006ea1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ea/006ea1c0.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 8件 [`005d3af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d3/005d3af8.md) [`005d3f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d3/005d3f6c.md) [`005d4158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d4/005d4158.md) [`006e92bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e92bc.md) [`006ea1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ea1c0.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "005d9554",
      "incomplete_value": false,
      "site": "005d9558",
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
      "definition_site": "005d9554",
      "incomplete_value": false,
      "site": "005d9558",
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
      "005d9554",
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
      "005d9554",
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

- 旧版 [`005d9554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d9548.md#insn-005d9554)
- 新版 `005d9554`（命令位置の公開資料なし）

~~~diff
- 005d9554 ["COPY", "tmp:0:8", ["const:303:8"]]
- 005d9554 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005d9554 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005d9554 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d9554 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005d9554 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d9554 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d9554 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005d9554 bytes 000c0c91
+ 005d9554 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3b2a721e2d061aed2087328beff1317"></a>

### [`005d955c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d955c.md) → [`005d955c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d955c.md) FUN_005d955c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`005d4158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d4/005d4158.md) [`006e92bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e92bc.md) [`006ea088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ea/006ea088.md) [`006ea1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ea/006ea1c0.md) [`006eb464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006eb/006eb464.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 5件 [`005d4158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d4/005d4158.md) [`006e92bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e92bc.md) [`006ea088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ea088.md) [`006ea1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ea1c0.md) [`006eb464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb464.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "005d9568",
      "incomplete_value": false,
      "site": "005d956c",
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
      "definition_site": "005d9568",
      "incomplete_value": false,
      "site": "005d956c",
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
      "005d9568",
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
      "005d9568",
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

- 旧版 [`005d9568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d955c.md#insn-005d9568)
- 新版 `005d9568`（命令位置の公開資料なし）

~~~diff
- 005d9568 ["COPY", "tmp:0:8", ["const:303:8"]]
- 005d9568 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005d9568 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005d9568 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d9568 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005d9568 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d9568 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d9568 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005d9568 bytes 000c0c91
+ 005d9568 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d65cbf60f277588e767c5c9dd154209"></a>

### [`005d9570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d9570.md) → [`005d9570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d9570.md) FUN_005d9570

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005d4824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d4/005d4824.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`005d4824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d4/005d4824.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "005d957c",
      "incomplete_value": true,
      "site": "005d9580",
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
      "definition_site": "005d957c",
      "incomplete_value": true,
      "site": "005d9580",
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
      "005d957c",
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
      "005d957c",
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

- 旧版 [`005d957c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d9570.md#insn-005d957c)
- 新版 `005d957c`（命令位置の公開資料なし）

~~~diff
- 005d957c ["COPY", "tmp:0:8", ["const:303:8"]]
- 005d957c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005d957c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005d957c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d957c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005d957c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d957c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d957c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005d957c bytes 000c0c91
+ 005d957c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fbb6b24fa1d501c6bbcf8715a44b610"></a>

### [`005d9584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d9584.md) → [`005d9584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d9584.md) FUN_005d9584

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005d4988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d4/005d4988.md) [`005d57d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d5/005d57d0.md) [`006eb364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006eb/006eb364.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 3件 [`005d4988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d4/005d4988.md) [`005d57d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d5/005d57d0.md) [`006eb364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb364.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "005d9590",
      "incomplete_value": false,
      "site": "005d9594",
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
      "definition_site": "005d9590",
      "incomplete_value": false,
      "site": "005d9594",
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
      "005d9590",
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
      "005d9590",
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

- 旧版 [`005d9590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d9584.md#insn-005d9590)
- 新版 `005d9590`（命令位置の公開資料なし）

~~~diff
- 005d9590 ["COPY", "tmp:0:8", ["const:303:8"]]
- 005d9590 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005d9590 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005d9590 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d9590 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005d9590 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d9590 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d9590 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005d9590 bytes 000c0c91
+ 005d9590 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35a49e5d6a665ea0f88d4a20330624f7"></a>

### [`005d95dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d95dc.md) → [`005d95dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d95dc.md) _INIT_73

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
      "definition_site": "005d9618",
      "incomplete_value": true,
      "site": "005d9634",
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
      "definition_site": "005d9618",
      "incomplete_value": true,
      "site": "005d9634",
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
      "definition_site": "005d963c",
      "incomplete_value": true,
      "site": "005d9658",
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
      "definition_site": "005d963c",
      "incomplete_value": true,
      "site": "005d9658",
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
      "definition_site": "005d965c",
      "incomplete_value": true,
      "site": "005d9678",
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
      "definition_site": "005d965c",
      "incomplete_value": true,
      "site": "005d9678",
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
      "005d9618",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "005d963c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "005d965c",
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
      "005d9618",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "005d963c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "005d965c",
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

- 旧版 [`005d9608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d95dc.md#insn-005d9608) · [`005d9610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d95dc.md#insn-005d9610)
- 新版 `005d9608`（命令位置の公開資料なし） · `005d9610`（命令位置の公開資料なし）

~~~diff
- 005d9608 ["COPY", "tmp:0:8", ["const:a80:8"]]
- 005d9608 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005d9608 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005d9608 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005d9608 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 005d9608 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005d9608 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005d9608 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005d9608 bytes 73022a91
+ 005d9608 bytes 73022b91
- 005d9610 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 005d9610 bytes 69e6ffd0
+ 005d9610 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 005d9610 bytes 69e6ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b4b794922729623c473deb99ad96330"></a>

### [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) → [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) FUN_005d996c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) [`007bdafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bdafc.md) · 呼出先 182件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md)
- 新版 呼出元 2件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`007bdafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bd/007bdafc.md) · 呼出先 182件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 99.45% / 新版 99.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 9件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005dc6d0",
      "incomplete_value": false,
      "site": "005dc6d0",
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
      "definition_site": "005dc6d0",
      "incomplete_value": false,
      "site": "005dc6d0",
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
    "ordinal": 460,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005dc6fc",
      "incomplete_value": false,
      "site": "005dc6fc",
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
            "const:a3d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005dc6fc",
      "incomplete_value": false,
      "site": "005dc6fc",
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
            "const:9a3:8"
          ]
        ]
      ]
    },
    "ordinal": 464,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005dc728",
      "incomplete_value": false,
      "site": "005dc728",
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
            "const:7bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005dc728",
      "incomplete_value": false,
      "site": "005dc728",
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
            "const:731:8"
          ]
        ]
      ]
    },
    "ordinal": 465,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d9ac8",
      "READ",
      [
        "storage",
        "002a57a3",
        null,
        "string"
      ]
    ],
    [
      "005da5bc",
      "READ",
      [
        "storage",
        "00c1b670",
        null,
        "pointer"
      ]
    ],
    [
      "005da5bc",
      "PARAM",
      [
        "storage",
        "0109e418",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "005d9ac8",
      "READ",
      [
        "storage",
        "002a582e",
        null,
        "string"
      ]
    ],
    [
      "005da5bc",
      "READ",
      [
        "storage",
        "00c1b6c0",
        null,
        "pointer"
      ]
    ],
    [
      "005da5bc",
      "PARAM",
      [
        "storage",
        "0109e458",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d9ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md#insn-005d9ac4) · [`005da5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md#insn-005da5bc) · [`005dbcf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md#insn-005dbcf8)
- 新版 `005d9ac4`（命令位置の公開資料なし） · `005da5bc`（命令位置の公開資料なし） · `005dbcf8`（命令位置の公開資料なし）

~~~diff
- 005d9ac4 ["COPY", "tmp:0:8", ["const:7a3:8"]]
- 005d9ac4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005d9ac4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005d9ac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005d9ac4 ["COPY", "tmp:0:8", ["const:82e:8"]]
+ 005d9ac4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005d9ac4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005d9ac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005d9ac4 bytes 088d1e91
+ 005d9ac4 bytes 08b92091
- 005da5bc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:670:8"]]
- 005da5bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005da5bc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:6c0:8"]]
+ 005da5bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005da5bc bytes 213843f9
+ 005da5bc bytes 216043f9
- 005dbcf8 ["COPY", "tmp:0:8", ["const:754:8"]]
- 005dbcf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005dbcf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005dbcf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005dbcf8 ["COPY", "tmp:0:8", ["const:7df:8"]]
+ 005dbcf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005dbcf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005dbcf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005dbcf8 bytes 29511d91
+ 005dbcf8 bytes 297d1f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73643dd3849c2e6c613b7dbe4a748b3c"></a>

### [`005e0200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e0/005e0200.md) → [`005e0200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e0/005e0200.md) FUN_005e0200

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) · 呼出先 4件 [`005f08d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f08d8.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) · 呼出先 4件 [`005f08d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f08d8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005e0234",
      "incomplete_value": true,
      "site": "005e0238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005e0234",
      "incomplete_value": true,
      "site": "005e0238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005e0278",
      "incomplete_value": true,
      "site": "005e027c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005e0278",
      "incomplete_value": true,
      "site": "005e027c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005e022c",
      "READ",
      [
        "storage",
        "00c1b528",
        null,
        "pointer"
      ]
    ],
    [
      "005e0238",
      "DATA",
      [
        "storage",
        "00c0bd40",
        null,
        "undefined *"
      ]
    ],
    [
      "005e0270",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005e022c",
      "READ",
      [
        "storage",
        "00c1b578",
        null,
        "pointer"
      ]
    ],
    [
      "005e0238",
      "DATA",
      [
        "storage",
        "00c0bd90",
        null,
        "undefined *"
      ]
    ],
    [
      "005e0270",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005e022c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e0/005e0200.md#insn-005e022c) · [`005e0270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e0/005e0200.md#insn-005e0270)
- 新版 `005e022c`（命令位置の公開資料なし） · `005e0270`（命令位置の公開資料なし）

~~~diff
- 005e022c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:528:8"]]
- 005e022c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005e022c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:578:8"]]
+ 005e022c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005e022c bytes 089542f9
+ 005e022c bytes 08bd42f9
- 005e0270 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:520:8"]]
- 005e0270 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005e0270 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:570:8"]]
+ 005e0270 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005e0270 bytes 089142f9
+ 005e0270 bytes 08b942f9
~~~


<a id="compare-7bb1f4cf4ecc27de9f37cdf1fe49eb08"></a>

### [`005e02b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e0/005e02b0.md) → [`005e02b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e0/005e02b0.md) FUN_005e02b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 55件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449d9c.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 55件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449d9c.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.91% / 新版 99.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005e1320",
      "incomplete_value": true,
      "site": "005e1324",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005e1320",
      "incomplete_value": true,
      "site": "005e1324",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 107,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005e1320",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "005e1320",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005e1320",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "005e1320",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005e1320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e0/005e02b0.md#insn-005e1320)
- 新版 `005e1320`（命令位置の公開資料なし）

~~~diff
- 005e1320 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d28:8"]]
- 005e1320 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005e1320 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d78:8"]]
+ 005e1320 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005e1320 bytes 009446f9
+ 005e1320 bytes 00bc46f9
~~~


<a id="compare-04045aa81365498d08b7150a5c513b50"></a>

### [`005e144c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e144c.md) → [`005e144c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e144c.md) FUN_005e144c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 22件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449c84.md) [`00449d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449d9c.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`005f08d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f08d8.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 22件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c84.md) [`00449d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449d9c.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`005f08d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f08d8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005e1560",
      "incomplete_value": false,
      "site": "005e1560",
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
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005e1560",
      "incomplete_value": false,
      "site": "005e1560",
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
            "const:850:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005e184c",
      "incomplete_value": false,
      "site": "005e184c",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005e184c",
      "incomplete_value": false,
      "site": "005e184c",
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
            "const:8d0:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005e148c",
      "incomplete_value": true,
      "site": "005e148c",
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
      "definition_site": "005e148c",
      "incomplete_value": true,
      "site": "005e148c",
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
      "005e1488",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "005e1494",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005e149c",
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
      "005e1488",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "005e1494",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005e149c",
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

- 旧版 [`005e1488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e144c.md#insn-005e1488) · [`005e1494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e144c.md#insn-005e1494) · [`005e149c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e144c.md#insn-005e149c)
- 新版 `005e1488`（命令位置の公開資料なし） · `005e1494`（命令位置の公開資料なし） · `005e149c`（命令位置の公開資料なし）

~~~diff
- 005e1488 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 005e1488 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005e1488 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 005e1488 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005e1488 bytes 003d45f9
+ 005e1488 bytes 005d45f9
- 005e1494 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 005e1494 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005e1494 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005e1494 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005e1494 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 005e1494 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005e1494 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005e1494 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005e1494 bytes 21203991
+ 005e1494 bytes 21603a91
- 005e149c ["COPY", "tmp:0:8", ["const:500:8"]]
- 005e149c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 005e149c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 005e149c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 005e149c ["COPY", "tmp:0:8", ["const:550:8"]]
+ 005e149c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 005e149c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 005e149c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 005e149c bytes 42001491
+ 005e149c bytes 42401591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3167246f5c63bc17c01bb8dd72dde153"></a>

### [`005e1a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md) → [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) FUN_005e1a5c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 135件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 135件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.65% / 新版 96.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 33件, `call_target` 3件, `store_value` 19件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005e1db8",
      "incomplete_value": false,
      "site": "005e1db8",
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
      "definition_site": "005e1db8",
      "incomplete_value": false,
      "site": "005e1db8",
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
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005e1dec",
      "incomplete_value": false,
      "site": "005e1dec",
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
      "definition_site": "005e1dec",
      "incomplete_value": false,
      "site": "005e1dec",
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
    "ordinal": 46,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005e1fb0",
      "incomplete_value": false,
      "site": "005e1fb8",
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
      "definition_site": "005e1fb0",
      "incomplete_value": false,
      "site": "005e1fb8",
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
      "005e1d90",
      "PARAM",
      [
        "storage",
        "002a1742",
        null,
        "string"
      ]
    ],
    [
      "005e1db8",
      "DATA",
      [
        "storage",
        "00bf4a50",
        null,
        "undefined *"
      ]
    ],
    [
      "005e1dec",
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
      "005e1d90",
      "PARAM",
      [
        "storage",
        "002a17cd",
        null,
        "string"
      ]
    ],
    [
      "005e1db8",
      "DATA",
      [
        "storage",
        "00bf4aa0",
        null,
        "undefined *"
      ]
    ],
    [
      "005e1dec",
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

- 旧版 [`005e1f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md#insn-005e1f70) · [`005e1d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md#insn-005e1d90) · [`005e1db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md#insn-005e1db0)
- 新版 `005e1f70`（命令位置の公開資料なし） · `005e1d90`（命令位置の公開資料なし） · `005e1db0`（命令位置の公開資料なし）

~~~diff
- 005e1f70 ["INT_ADD", "register:40f0:8", ["const:5e1f70:8", "const:4:8"]]
- 005e1f70 ["CALL", null, ["ram:a09924:8"]]
+ 005e1f70 ["INT_ADD", "register:40f0:8", ["const:5e1f70:8", "const:4:8"]]
+ 005e1f70 ["CALL", null, ["ram:a09968:8"]]
- 005e1f70 bytes 6d9e1094
+ 005e1f70 bytes 7e9e1094
- 005e1d90 ["COPY", "tmp:0:8", ["const:742:8"]]
- 005e1d90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005e1d90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005e1d90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005e1d90 ["COPY", "tmp:0:8", ["const:7cd:8"]]
+ 005e1d90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005e1d90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005e1d90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005e1d90 bytes 21081d91
+ 005e1d90 bytes 21341f91
- 005e1db0 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 005e1db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005e1db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005e1db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005e1db0 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 005e1db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005e1db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005e1db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005e1db0 bytes 08412991
+ 005e1db0 bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cc435cb6b62e8adb886433b7f73d040"></a>

### [`005e53dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e5/005e53dc.md) → [`005e53dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e5/005e53dc.md) FUN_005e53dc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005e1a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 35件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md)
- 新版 呼出元 2件 [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 35件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.14% / 新版 98.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005e5b98",
      "incomplete_value": true,
      "site": "005e5b98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:647:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005e5b98",
      "incomplete_value": true,
      "site": "005e5b98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5bc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 89,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005e5c5c",
      "incomplete_value": false,
      "site": "005e5c68",
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
            "const:a43:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005e5c5c",
      "incomplete_value": false,
      "site": "005e5c68",
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
            "const:9a9:8"
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
      "definition_site": "005e5e70",
      "incomplete_value": true,
      "site": "005e5e78",
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
            "const:81c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005e5e70",
      "incomplete_value": true,
      "site": "005e5e78",
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
            "const:791:8"
          ]
        ]
      ]
    },
    "ordinal": 56,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005e542c",
      "READ",
      [
        "storage",
        "0029b679",
        null,
        "string"
      ]
    ],
    [
      "005e54c8",
      "READ",
      [
        "storage",
        "002a982e",
        null,
        "string"
      ]
    ],
    [
      "005e54cc",
      "READ",
      [
        "storage",
        "002a9835",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005e542c",
      "READ",
      [
        "storage",
        "0029b677",
        null,
        "string"
      ]
    ],
    [
      "005e54c8",
      "READ",
      [
        "storage",
        "002a983d",
        null,
        "string"
      ]
    ],
    [
      "005e54cc",
      "READ",
      [
        "storage",
        "002a9844",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005e5424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e5/005e53dc.md#insn-005e5424) · [`005e54c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e5/005e53dc.md#insn-005e54c0) · [`005e5670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e5/005e53dc.md#insn-005e5670)
- 新版 `005e5424`（命令位置の公開資料なし） · `005e54c0`（命令位置の公開資料なし） · `005e5670`（命令位置の公開資料なし）

~~~diff
- 005e5424 ["COPY", "tmp:0:8", ["const:679:8"]]
- 005e5424 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005e5424 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005e5424 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005e5424 ["COPY", "tmp:0:8", ["const:677:8"]]
+ 005e5424 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005e5424 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005e5424 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005e5424 bytes 29e51991
+ 005e5424 bytes 29dd1991
- 005e54c0 ["COPY", "tmp:0:8", ["const:82e:8"]]
- 005e54c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005e54c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005e54c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005e54c0 ["COPY", "tmp:0:8", ["const:83d:8"]]
+ 005e54c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005e54c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005e54c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005e54c0 bytes 29b92091
+ 005e54c0 bytes 29f52091
- 005e5670 ["COPY", "tmp:0:8", ["const:82e:8"]]
- 005e5670 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005e5670 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005e5670 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005e5670 ["COPY", "tmp:0:8", ["const:83d:8"]]
+ 005e5670 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005e5670 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005e5670 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005e5670 bytes 29b92091
+ 005e5670 bytes 29f52091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5443453d15fc9821e660dc618476ef8a"></a>

### [`005e82fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e8/005e82fc.md) → [`005e82fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e8/005e82fc.md) FUN_005e82fc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005e1a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md) [`005efee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ef/005efee8.md) [`006f308c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f3/006f308c.md)
- 新版 呼出元 2件 [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md) [`005efee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ef/005efee8.md) [`006f308c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f308c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.03% / 新版 97.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005e8418",
      "incomplete_value": true,
      "site": "005e8424",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005e8418",
      "incomplete_value": true,
      "site": "005e8424",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:40:8"
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
      "005e8334",
      "READ",
      [
        "storage",
        "002a0794",
        null,
        "string"
      ]
    ],
    [
      "005e8338",
      "READ",
      [
        "storage",
        "002a07a2",
        null,
        "string"
      ]
    ],
    [
      "005e8418",
      "READ",
      [
        "storage",
        "00299040",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005e8334",
      "READ",
      [
        "storage",
        "002a081f",
        null,
        "string"
      ]
    ],
    [
      "005e8338",
      "READ",
      [
        "storage",
        "002a082d",
        null,
        "string"
      ]
    ],
    [
      "005e8418",
      "READ",
      [
        "storage",
        "00298fb3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005e8328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e8/005e82fc.md#insn-005e8328) · [`005e8410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e8/005e82fc.md#insn-005e8410) · [`005e8414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e8/005e82fc.md#insn-005e8414)
- 新版 `005e8328`（命令位置の公開資料なし） · `005e8410`（命令位置の公開資料なし） · `005e8414`（命令位置の公開資料なし）

~~~diff
- 005e8328 ["COPY", "tmp:0:8", ["const:794:8"]]
- 005e8328 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005e8328 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005e8328 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005e8328 ["COPY", "tmp:0:8", ["const:81f:8"]]
+ 005e8328 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005e8328 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005e8328 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005e8328 bytes 29511e91
+ 005e8328 bytes 297d2091
- 005e8410 ["COPY", "register:4040:8", ["const:299000:8"]]
+ 005e8410 ["COPY", "register:4040:8", ["const:298000:8"]]
- 005e8410 bytes 88e5ffb0
+ 005e8410 bytes 88e5ff90
- 005e8414 ["COPY", "tmp:0:8", ["const:40:8"]]
- 005e8414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005e8414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005e8414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005e8414 ["COPY", "tmp:0:8", ["const:fb3:8"]]
+ 005e8414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005e8414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005e8414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005e8414 bytes 08010191
+ 005e8414 bytes 08cd3e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57338dbdf214e1ebc81fcaefe7dc4f5f"></a>

### [`005e8d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e8/005e8d4c.md) → [`005e8d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e8/005e8d4c.md) FUN_005e8d4c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`005e1a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md) [`005eb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005eb/005eb040.md) [`005f182c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f182c.md) [`008ffa34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ffa34.md) · 呼出先 37件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0044abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abe4.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 4件 [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`005eb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005eb/005eb040.md) [`005f182c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f182c.md) [`008ffa34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffa34.md) · 呼出先 37件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0044abe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abe4.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005e9128",
      "incomplete_value": true,
      "site": "005e913c",
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005e9128",
      "incomplete_value": true,
      "site": "005e913c",
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
                "const:6de:8"
              ]
            ]
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
      "definition_site": "005e912c",
      "incomplete_value": true,
      "site": "005e9140",
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
      "definition_site": "005e912c",
      "incomplete_value": true,
      "site": "005e9140",
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005e9200",
      "incomplete_value": true,
      "site": "005e9210",
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
                "const:fa1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005e9200",
      "incomplete_value": true,
      "site": "005e9210",
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
                "const:2e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005e9128",
      "READ",
      [
        "storage",
        "002a76de",
        null,
        "string"
      ]
    ],
    [
      "005e912c",
      "READ",
      [
        "storage",
        "002a76ea",
        null,
        "string"
      ]
    ],
    [
      "005e9174",
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
      "005e9128",
      "READ",
      [
        "storage",
        "002a7778",
        null,
        "string"
      ]
    ],
    [
      "005e912c",
      "READ",
      [
        "storage",
        "002a7784",
        null,
        "string"
      ]
    ],
    [
      "005e9174",
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

- 旧版 [`005e9120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e8/005e8d4c.md#insn-005e9120) · [`005e9124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e8/005e8d4c.md#insn-005e9124)
- 新版 `005e9120`（命令位置の公開資料なし） · `005e9124`（命令位置の公開資料なし）

~~~diff
- 005e9120 ["COPY", "tmp:0:8", ["const:6de:8"]]
- 005e9120 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005e9120 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005e9120 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005e9120 ["COPY", "tmp:0:8", ["const:778:8"]]
+ 005e9120 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005e9120 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005e9120 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005e9120 bytes 08791b91
+ 005e9120 bytes 08e11d91
- 005e9124 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 005e9124 bytes 49e6ff90
+ 005e9124 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 005e9124 bytes 49e6ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80a1ae30be89a2461c04f4cd8a4dfeeb"></a>

### [`005e97d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e9/005e97d8.md) → [`005e97d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e9/005e97d8.md) FUN_005e97d8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) · 呼出先 37件 [`00444c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00445d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d90.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md)
- 新版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 37件 [`00444c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00445d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d90.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005ea940",
      "incomplete_value": true,
      "site": "005ea948",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ea940",
      "incomplete_value": true,
      "site": "005ea948",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 123,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005e98e0",
      "READ",
      [
        "storage",
        "00c1b6a0",
        null,
        "pointer"
      ]
    ],
    [
      "005e98ec",
      "READ",
      [
        "storage",
        "00c24134",
        null,
        "undefined4"
      ]
    ],
    [
      "005e9938",
      "READ",
      [
        "storage",
        "00c1b6a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005e98e0",
      "READ",
      [
        "storage",
        "00c1b6f0",
        null,
        "pointer"
      ]
    ],
    [
      "005e98ec",
      "READ",
      [
        "storage",
        "00c24184",
        null,
        "undefined4"
      ]
    ],
    [
      "005e9938",
      "READ",
      [
        "storage",
        "00c1b6f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005e98e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e9/005e97d8.md#insn-005e98e0) · [`005e9938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e9/005e97d8.md#insn-005e9938) · [`005e9970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e9/005e97d8.md#insn-005e9970)
- 新版 `005e98e0`（命令位置の公開資料なし） · `005e9938`（命令位置の公開資料なし） · `005e9970`（命令位置の公開資料なし）

~~~diff
- 005e98e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6a0:8"]]
- 005e98e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005e98e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6f0:8"]]
+ 005e98e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005e98e0 bytes 085143f9
+ 005e98e0 bytes 087943f9
- 005e9938 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6a0:8"]]
- 005e9938 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005e9938 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6f0:8"]]
+ 005e9938 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005e9938 bytes 085143f9
+ 005e9938 bytes 087943f9
- 005e9970 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
- 005e9970 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005e9970 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6f0:8"]]
+ 005e9970 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 005e9970 bytes 945243f9
+ 005e9970 bytes 947a43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-526a95309bec458e4b224b3e6f2182ee"></a>

### [`005eb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005eb/005eb040.md) → [`005eb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005eb/005eb040.md) FUN_005eb040

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 63件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 63件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.28% / 新版 96.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 9件, `store_destination` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005eb79c",
      "incomplete_value": false,
      "site": "005eb79c",
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
      "definition_site": "005eb79c",
      "incomplete_value": false,
      "site": "005eb79c",
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
    "ordinal": 62,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005eb7a0",
      "incomplete_value": false,
      "site": "005eb7a0",
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
      "definition_site": "005eb7a0",
      "incomplete_value": false,
      "site": "005eb7a0",
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
    "ordinal": 63,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005eb79c",
      "incomplete_value": false,
      "site": "005eb7a0",
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
      "definition_site": "005eb79c",
      "incomplete_value": false,
      "site": "005eb7a0",
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
    "ordinal": 63,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005eb4a8",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "005eb4d4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "005eb4e4",
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
      "005eb4a8",
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "005eb4d4",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "005eb4e4",
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

- 旧版 [`005eb48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005eb/005eb040.md#insn-005eb48c) · [`005eb4a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005eb/005eb040.md#insn-005eb4a4) · [`005eb4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005eb/005eb040.md#insn-005eb4a8)
- 新版 `005eb48c`（命令位置の公開資料なし） · `005eb4a4`（命令位置の公開資料なし） · `005eb4a8`（命令位置の公開資料なし）

~~~diff
- 005eb48c ["COPY", "tmp:0:8", ["const:38:8"]]
- 005eb48c ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 005eb48c ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 005eb48c ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 005eb48c ["COPY", "tmp:0:8", ["const:78:8"]]
+ 005eb48c ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 005eb48c ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 005eb48c ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 005eb48c bytes 94e20091
+ 005eb48c bytes 94e20191
- 005eb4a4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 005eb4a4 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 005eb4a4 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 005eb4a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 005eb4a4 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 005eb4a4 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 005eb4a4 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 005eb4a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 005eb4a4 bytes b5020091
+ 005eb4a4 bytes b5020191
- 005eb4a8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:e60:8"]]
- 005eb4a8 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 005eb4a8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:eb0:8"]]
+ 005eb4a8 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 005eb4a8 bytes f73247f9
+ 005eb4a8 bytes f75a47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b97bd385d8c1dedb3cce29bab247bde2"></a>

### [`005ec96c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ec/005ec96c.md) → [`005ec96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ec/005ec96c.md) FUN_005ec96c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`005eb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005eb/005eb040.md) [`00600a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600a74.md) · 呼出先 13件 [`005c13f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c1/005c13f4.md) [`006f23b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f2/006f23b4.md) [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfcd8.md)
- 新版 呼出元 2件 [`005eb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005eb/005eb040.md) [`00600a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600a74.md) · 呼出先 13件 [`005c13f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c1/005c13f4.md) [`006f23b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f23b4.md) [`007cf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfcd8.md)

変更の種類 call, call_count, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 93.36% / 新版 93.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005eca34",
      "incomplete_value": false,
      "site": "005eca40",
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
            "const:a3d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005eca34",
      "incomplete_value": false,
      "site": "005eca40",
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
            "const:9a3:8"
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
      "definition_site": "005ecab4",
      "incomplete_value": false,
      "site": "005ecabc",
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
            "const:d85:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ecab4",
      "incomplete_value": false,
      "site": "005ecabc",
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
            "const:e12:8"
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
      "definition_site": "005ecb10",
      "incomplete_value": false,
      "site": "005ecb14",
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
            "const:7cd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ecb10",
      "incomplete_value": false,
      "site": "005ecb14",
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
            "const:742:8"
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
      "005eca14",
      "DATA",
      [
        "storage",
        "0029e6a4",
        null,
        "string"
      ]
    ],
    [
      "unmatched:005eca2c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdd9e0"
      ]
    ],
    [
      "005eca40",
      "DATA",
      [
        "storage",
        "002a69a3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005eca14",
      "DATA",
      [
        "storage",
        "0029e72f",
        null,
        "string"
      ]
    ],
    [
      "005eca2c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdd9e0"
      ]
    ],
    [
      "005eca40",
      "DATA",
      [
        "storage",
        "002a6a3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005eca2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ec/005ec96c.md#insn-005eca2c) · [`005eca0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ec/005ec96c.md#insn-005eca0c)
- 新版 `005eca2c`（命令位置の公開資料なし） · `005eca0c`（命令位置の公開資料なし）

~~~diff
- 005eca2c ["INT_ADD", "register:40f0:8", ["const:5eca2c:8", "const:4:8"]]
- 005eca2c ["CALL", null, ["callee:00bdd9e0:8"]]
- 005eca2c bytes d9c31794
+ 005eca2c ["INT_ADD", "register:40f0:8", ["const:5eca2c:8", "const:4:8"]]
+ 005eca2c ["CALL", null, ["callee:00bdd9e0:8"]]
+ 005eca2c bytes edc31794
- 005eca0c ["COPY", "tmp:0:8", ["const:6a4:8"]]
- 005eca0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005eca0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005eca0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005eca0c ["COPY", "tmp:0:8", ["const:72f:8"]]
+ 005eca0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005eca0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005eca0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005eca0c bytes 08911a91
+ 005eca0c bytes 08bd1c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66cb9b00a32ca98313f36e802dc7ecd7"></a>

### [`005ecde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ec/005ecde0.md) → [`005ecde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ec/005ecde0.md) FUN_005ecde0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) · 呼出先 22件 [`00444c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00445044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445044.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md)
- 新版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 22件 [`00444c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00445044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445044.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044592c.md)

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
      "definition_site": "005ed864",
      "incomplete_value": true,
      "site": "005ed86c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ed864",
      "incomplete_value": true,
      "site": "005ed86c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 57,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005ecfa0",
      "READ",
      [
        "storage",
        "00c1b6b8",
        null,
        "pointer"
      ]
    ],
    [
      "005ecfb8",
      "READ",
      [
        "storage",
        "00c241e4",
        null,
        "undefined4"
      ]
    ],
    [
      "005ecffc",
      "READ",
      [
        "storage",
        "00c1b6a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ecfa0",
      "READ",
      [
        "storage",
        "00c1b708",
        null,
        "pointer"
      ]
    ],
    [
      "005ecfb8",
      "READ",
      [
        "storage",
        "00c24234",
        null,
        "undefined4"
      ]
    ],
    [
      "005ecffc",
      "READ",
      [
        "storage",
        "00c1b6f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ecfa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ec/005ecde0.md#insn-005ecfa0) · [`005ecffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ec/005ecde0.md#insn-005ecffc) · [`005ed2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ec/005ecde0.md#insn-005ed2e4)
- 新版 `005ecfa0`（命令位置の公開資料なし） · `005ecffc`（命令位置の公開資料なし） · `005ed2e4`（命令位置の公開資料なし）

~~~diff
- 005ecfa0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6b8:8"]]
- 005ecfa0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ecfa0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:708:8"]]
+ 005ecfa0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ecfa0 bytes 085d43f9
+ 005ecfa0 bytes 088543f9
- 005ecffc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6a8:8"]]
- 005ecffc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ecffc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6f8:8"]]
+ 005ecffc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005ecffc bytes 295543f9
+ 005ecffc bytes 297d43f9
- 005ed2e4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:660:8"]]
- 005ed2e4 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ed2e4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:6b0:8"]]
+ 005ed2e4 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 005ed2e4 bytes f73243f9
+ 005ed2e4 bytes f75a43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-023bc6aaff0d8818c1dbb616116f4663"></a>

### [`005edb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ed/005edb40.md) → [`005edb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ed/005edb40.md) FUN_005edb40

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 43件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459a90.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 43件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459a90.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.57% / 新版 93.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_destination` 2件, `store_value` 9件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005eded0",
      "incomplete_value": false,
      "site": "005eded0",
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
      "definition_site": "005eded0",
      "incomplete_value": false,
      "site": "005eded0",
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
    "ordinal": 38,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005ee070",
      "incomplete_value": true,
      "site": "005ee080",
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
                "const:afb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ee070",
      "incomplete_value": true,
      "site": "005ee080",
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
                "const:b88:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005ee084",
      "incomplete_value": true,
      "site": "005ee084",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005ee084",
      "incomplete_value": true,
      "site": "005ee084",
      "value": [
        "LOAD",
        "8",
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
      "005edca4",
      "READ",
      [
        "storage",
        "00c24070",
        null,
        "undefined4"
      ]
    ],
    [
      "005edd7c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "005edd88",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005edca4",
      "READ",
      [
        "storage",
        "00c240c0",
        null,
        "undefined4"
      ]
    ],
    [
      "005edd7c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "005edd88",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005edc88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ed/005edb40.md#insn-005edc88) · [`005edd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ed/005edb40.md#insn-005edd7c) · [`005edd88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ed/005edb40.md#insn-005edd88)
- 新版 `005edc88`（命令位置の公開資料なし） · `005edd7c`（命令位置の公開資料なし） · `005edd88`（命令位置の公開資料なし）

~~~diff
- 005edc88 ["COPY", "tmp:0:8", ["const:70:8"]]
- 005edc88 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005edc88 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005edc88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005edc88 ["COPY", "tmp:0:8", ["const:c0:8"]]
+ 005edc88 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005edc88 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005edc88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005edc88 bytes 29c10191
+ 005edc88 bytes 29010391
- 005edd7c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 005edd7c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005edd7c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 005edd7c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005edd7c bytes 003d45f9
+ 005edd7c bytes 005d45f9
- 005edd88 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 005edd88 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005edd88 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005edd88 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005edd88 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 005edd88 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005edd88 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005edd88 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005edd88 bytes 21203991
+ 005edd88 bytes 21603a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e7c8c64ac9d259a3aa0ad9f3f61fa27"></a>

### [`005ee758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ee/005ee758.md) → [`005ee758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ee/005ee758.md) FUN_005ee758

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) · 呼出先 25件 [`00444c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446784.md)
- 新版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 25件 [`00444c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446784.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005eeeb0",
      "incomplete_value": true,
      "site": "005eeeb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005eeeb0",
      "incomplete_value": true,
      "site": "005eeeb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005eef7c",
      "incomplete_value": true,
      "site": "005eef80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "005eef7c",
      "incomplete_value": true,
      "site": "005eef80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 62,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005eef68",
      "incomplete_value": false,
      "site": "005eef80",
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
      "definition_site": "005eef68",
      "incomplete_value": false,
      "site": "005eef80",
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
    "ordinal": 62,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005ee7e8",
      "READ",
      [
        "storage",
        "00c1b6a0",
        null,
        "pointer"
      ]
    ],
    [
      "005ee800",
      "READ",
      [
        "storage",
        "00c24134",
        null,
        "undefined4"
      ]
    ],
    [
      "005ee85c",
      "READ",
      [
        "storage",
        "00c24134",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "005ee7e8",
      "READ",
      [
        "storage",
        "00c1b6f0",
        null,
        "pointer"
      ]
    ],
    [
      "005ee800",
      "READ",
      [
        "storage",
        "00c24184",
        null,
        "undefined4"
      ]
    ],
    [
      "005ee85c",
      "READ",
      [
        "storage",
        "00c24184",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ee7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ee/005ee758.md#insn-005ee7e8) · [`005eed98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ee/005ee758.md#insn-005eed98) · [`005eeda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ee/005ee758.md#insn-005eeda8)
- 新版 `005ee7e8`（命令位置の公開資料なし） · `005eed98`（命令位置の公開資料なし） · `005eeda8`（命令位置の公開資料なし）

~~~diff
- 005ee7e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
- 005ee7e8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ee7e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6f0:8"]]
+ 005ee7e8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 005ee7e8 bytes 945243f9
+ 005ee7e8 bytes 947a43f9
- 005eed98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
- 005eed98 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005eed98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6b0:8"]]
+ 005eed98 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 005eed98 bytes 943243f9
+ 005eed98 bytes 945a43f9
- 005eeda8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d28:8"]]
- 005eeda8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005eeda8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d78:8"]]
+ 005eeda8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005eeda8 bytes 009446f9
+ 005eeda8 bytes 00bc46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca9cb04d58d996eb92f765ee5c7efc32"></a>

### [`005ef020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ef/005ef020.md) → [`005ef020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ef/005ef020.md) FUN_005ef020

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 45件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449d9c.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 45件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449d9c.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.89% / 新版 97.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005ef30c",
      "incomplete_value": false,
      "site": "005ef314",
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
      "definition_site": "005ef30c",
      "incomplete_value": false,
      "site": "005ef314",
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
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005ef348",
      "incomplete_value": false,
      "site": "005ef348",
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
      "definition_site": "005ef348",
      "incomplete_value": false,
      "site": "005ef348",
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
    "ordinal": 42,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005ef748",
      "incomplete_value": false,
      "site": "005ef750",
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
      "definition_site": "005ef748",
      "incomplete_value": false,
      "site": "005ef750",
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
    "ordinal": 66,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005ef2b8",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "005ef2b8",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ],
    [
      "005ef2ec",
      "PARAM",
      [
        "storage",
        "002a1742",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005ef2b8",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "005ef2b8",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ],
    [
      "005ef2ec",
      "PARAM",
      [
        "storage",
        "002a17cd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ef2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ef/005ef020.md#insn-005ef2b8) · [`005ef2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ef/005ef020.md#insn-005ef2ec) · [`005ef30c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ef/005ef020.md#insn-005ef30c)
- 新版 `005ef2b8`（命令位置の公開資料なし） · `005ef2ec`（命令位置の公開資料なし） · `005ef30c`（命令位置の公開資料なし）

~~~diff
- 005ef2b8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d28:8"]]
- 005ef2b8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ef2b8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d78:8"]]
+ 005ef2b8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005ef2b8 bytes 009446f9
+ 005ef2b8 bytes 00bc46f9
- 005ef2ec ["COPY", "tmp:0:8", ["const:742:8"]]
- 005ef2ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005ef2ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005ef2ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005ef2ec ["COPY", "tmp:0:8", ["const:7cd:8"]]
+ 005ef2ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005ef2ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005ef2ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005ef2ec bytes 21081d91
+ 005ef2ec bytes 21341f91
- 005ef30c ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 005ef30c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ef30c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ef30c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ef30c ["COPY", "tmp:0:8", ["const:940:8"]]
+ 005ef30c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ef30c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ef30c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ef30c bytes 08c12391
+ 005ef30c bytes 08012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b6c624f90e5b4561916f145adf62495"></a>

### [`005f064c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f064c.md) → [`005f064c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f064c.md) FUN_005f064c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`005f0450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f0450.md) [`005f0660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f0660.md) [`0061b7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0061b/0061b7d4.md) [`00766148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00766/00766148.md) [`007693f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00769/007693f4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 7件 [`005f0450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0450.md) [`005f0660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0660.md) [`0061b7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0061b/0061b7d4.md) [`00766148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00766/00766148.md) [`007693f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00769/007693f4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "005f0658",
      "incomplete_value": false,
      "site": "005f065c",
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
      "definition_site": "005f0658",
      "incomplete_value": false,
      "site": "005f065c",
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
      "005f0658",
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
      "005f0658",
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

- 旧版 [`005f0658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f064c.md#insn-005f0658)
- 新版 `005f0658`（命令位置の公開資料なし）

~~~diff
- 005f0658 ["COPY", "tmp:0:8", ["const:303:8"]]
- 005f0658 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005f0658 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005f0658 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005f0658 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005f0658 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005f0658 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005f0658 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005f0658 bytes 000c0c91
+ 005f0658 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20e24b728fd9d145bbd0375e2c1adc91"></a>

### [`005f096c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f096c.md) → [`005f096c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f096c.md) FUN_005f096c

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
      "definition_site": "005f098c",
      "incomplete_value": false,
      "site": "005f0990",
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
            "const:590:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f098c",
      "incomplete_value": false,
      "site": "005f0990",
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
            "const:540:8"
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
      "005f0990",
      "DATA",
      [
        "storage",
        "00bf4540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f0990",
      "DATA",
      [
        "storage",
        "00bf4590",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f098c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f096c.md#insn-005f098c)
- 新版 `005f098c`（命令位置の公開資料なし）

~~~diff
- 005f098c ["COPY", "tmp:0:8", ["const:540:8"]]
- 005f098c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f098c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f098c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f098c ["COPY", "tmp:0:8", ["const:590:8"]]
+ 005f098c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f098c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f098c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f098c bytes 08011591
+ 005f098c bytes 08411691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff89494ab59d204058292afe6d2d754f"></a>

### [`005f09a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f09a4.md) → [`005f09a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f09a4.md) FUN_005f09a4

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
      "definition_site": "005f09a8",
      "incomplete_value": false,
      "site": "005f09ac",
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
            "const:590:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f09a8",
      "incomplete_value": false,
      "site": "005f09ac",
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
            "const:540:8"
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
      "005f09ac",
      "DATA",
      [
        "storage",
        "00bf4540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f09ac",
      "DATA",
      [
        "storage",
        "00bf4590",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f09a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f09a4.md#insn-005f09a8)
- 新版 `005f09a8`（命令位置の公開資料なし）

~~~diff
- 005f09a8 ["COPY", "tmp:0:8", ["const:540:8"]]
- 005f09a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f09a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f09a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f09a8 ["COPY", "tmp:0:8", ["const:590:8"]]
+ 005f09a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f09a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f09a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f09a8 bytes 08011591
+ 005f09a8 bytes 08411691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4105c5c6384d2f4e85f458311b0a9a63"></a>

### [`005f09c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f09c4.md) → [`005f09c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f09c4.md) FUN_005f09c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 18件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050ae28.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ae28.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005f0a88",
      "incomplete_value": true,
      "site": "005f0a88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7ea:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f0a88",
      "incomplete_value": true,
      "site": "005f0a88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:75f:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005f0bd0",
      "incomplete_value": false,
      "site": "005f0bd0",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f0bd0",
      "incomplete_value": false,
      "site": "005f0bd0",
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
            "const:5b0:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005f0a70",
      "READ",
      [
        "storage",
        "002a175f",
        null,
        "string"
      ]
    ],
    [
      "005f0b34",
      "PARAM",
      [
        "storage",
        "00296d5e",
        null,
        "string"
      ]
    ],
    [
      "005f0b34",
      "PARAM",
      [
        "storage",
        "00296d4d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005f0a70",
      "READ",
      [
        "storage",
        "002a17ea",
        null,
        "string"
      ]
    ],
    [
      "005f0b34",
      "PARAM",
      [
        "storage",
        "00296cd1",
        null,
        "string"
      ]
    ],
    [
      "005f0b34",
      "PARAM",
      [
        "storage",
        "00296cc0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f0a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f09c4.md#insn-005f0a68) · [`005f0b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f09c4.md#insn-005f0b20) · [`005f0b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f09c4.md#insn-005f0b28)
- 新版 `005f0a68`（命令位置の公開資料なし） · `005f0b20`（命令位置の公開資料なし）

~~~diff
- 005f0a68 ["COPY", "tmp:0:8", ["const:75f:8"]]
- 005f0a68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005f0a68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005f0a68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005f0a68 ["COPY", "tmp:0:8", ["const:7ea:8"]]
+ 005f0a68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005f0a68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005f0a68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005f0a68 bytes 297d1d91
+ 005f0a68 bytes 29a91f91
- 005f0b20 ["COPY", "tmp:0:8", ["const:d5e:8"]]
- 005f0b20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f0b20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f0b20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f0b20 ["COPY", "tmp:0:8", ["const:cd1:8"]]
+ 005f0b20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f0b20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f0b20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f0b20 bytes 08793591
+ 005f0b20 bytes 08453391
- 005f0b28 ["COPY", "register:4050:8", ["const:296000:8"]]
- 005f0b28 bytes 2ae5ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1dd1e56149bb4d13af9bbe6578af0e4"></a>

### [`005f0e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f0e34.md) → [`005f0e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0e34.md) FUN_005f0e34

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
      "definition_site": "005f0e58",
      "incomplete_value": false,
      "site": "005f0e5c",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f0e58",
      "incomplete_value": false,
      "site": "005f0e5c",
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
      "005f0e5c",
      "DATA",
      [
        "storage",
        "00bf45b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f0e5c",
      "DATA",
      [
        "storage",
        "00bf4600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f0e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f0e34.md#insn-005f0e58)
- 新版 `005f0e58`（命令位置の公開資料なし）

~~~diff
- 005f0e58 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 005f0e58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f0e58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f0e58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f0e58 ["COPY", "tmp:0:8", ["const:600:8"]]
+ 005f0e58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f0e58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f0e58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f0e58 bytes 08c11691
+ 005f0e58 bytes 08011891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cef3e773993a19fc1c3e5897d7b25ebe"></a>

### [`005f0e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f0e74.md) → [`005f0e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0e74.md) FUN_005f0e74

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
      "definition_site": "005f0e78",
      "incomplete_value": false,
      "site": "005f0e7c",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f0e78",
      "incomplete_value": false,
      "site": "005f0e7c",
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
      "005f0e7c",
      "DATA",
      [
        "storage",
        "00bf45b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f0e7c",
      "DATA",
      [
        "storage",
        "00bf4600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f0e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f0e74.md#insn-005f0e78)
- 新版 `005f0e78`（命令位置の公開資料なし）

~~~diff
- 005f0e78 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 005f0e78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f0e78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f0e78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f0e78 ["COPY", "tmp:0:8", ["const:600:8"]]
+ 005f0e78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f0e78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f0e78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f0e78 bytes 08c11691
+ 005f0e78 bytes 08011891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74a07dee866c5c45313a239716bf70ba"></a>

### [`005f0e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f0e9c.md) → [`005f0e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0e9c.md) FUN_005f0e9c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00459f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459f50.md) [`005f10c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f10c8.md) [`005f10cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f10cc.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00459f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f50.md) [`005f10c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f10c8.md) [`005f10cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f10cc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005f0f68",
      "incomplete_value": false,
      "site": "005f0f68",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f0f68",
      "incomplete_value": false,
      "site": "005f0f68",
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
            "const:620:8"
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
      "005f0f68",
      "DATA",
      [
        "storage",
        "00bf4620",
        null,
        "undefined *"
      ]
    ],
    [
      "005f0fc0",
      "READ",
      [
        "storage",
        "00bf4640",
        null,
        "pointer"
      ]
    ],
    [
      "005f0fc0",
      "READ",
      [
        "storage",
        "00bf4648",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f0f68",
      "DATA",
      [
        "storage",
        "00bf4670",
        null,
        "undefined *"
      ]
    ],
    [
      "005f0fc0",
      "READ",
      [
        "storage",
        "00bf4690",
        null,
        "pointer"
      ]
    ],
    [
      "005f0fc0",
      "READ",
      [
        "storage",
        "00bf4698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f0e9c.md#insn-005f0f60)
- 新版 `005f0f60`（命令位置の公開資料なし）

~~~diff
- 005f0f60 ["COPY", "tmp:0:8", ["const:620:8"]]
- 005f0f60 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005f0f60 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005f0f60 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005f0f60 ["COPY", "tmp:0:8", ["const:670:8"]]
+ 005f0f60 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005f0f60 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005f0f60 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005f0f60 bytes 4a811891
+ 005f0f60 bytes 4ac11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-165b176b15bec9cfc9c076997d3e62e8"></a>

### [`005f1068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f1068.md) → [`005f1068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1068.md) FUN_005f1068

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
      "definition_site": "005f108c",
      "incomplete_value": false,
      "site": "005f1090",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f108c",
      "incomplete_value": false,
      "site": "005f1090",
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
            "const:620:8"
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
      "005f1090",
      "DATA",
      [
        "storage",
        "00bf4620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f1090",
      "DATA",
      [
        "storage",
        "00bf4670",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f108c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f1068.md#insn-005f108c)
- 新版 `005f108c`（命令位置の公開資料なし）

~~~diff
- 005f108c ["COPY", "tmp:0:8", ["const:620:8"]]
- 005f108c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f108c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f108c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f108c ["COPY", "tmp:0:8", ["const:670:8"]]
+ 005f108c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f108c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f108c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f108c bytes 08811891
+ 005f108c bytes 08c11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76c505afed61b7089d14a086f7fb9067"></a>

### [`005f10a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f10a8.md) → [`005f10a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f10a8.md) FUN_005f10a8

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
      "definition_site": "005f10ac",
      "incomplete_value": false,
      "site": "005f10b0",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f10ac",
      "incomplete_value": false,
      "site": "005f10b0",
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
            "const:620:8"
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
      "005f10b0",
      "DATA",
      [
        "storage",
        "00bf4620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f10b0",
      "DATA",
      [
        "storage",
        "00bf4670",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f10ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f10a8.md#insn-005f10ac)
- 新版 `005f10ac`（命令位置の公開資料なし）

~~~diff
- 005f10ac ["COPY", "tmp:0:8", ["const:620:8"]]
- 005f10ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f10ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f10ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f10ac ["COPY", "tmp:0:8", ["const:670:8"]]
+ 005f10ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f10ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f10ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f10ac bytes 08811891
+ 005f10ac bytes 08c11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-937374e4a49c2d2a1cd38b1eaa3f29bc"></a>

### [`005f10d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f10d0.md) → [`005f10d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f10d0.md) FUN_005f10d0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 23件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0045a030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a030.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 23件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0045a030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a030.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.02% / 新版 95.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005f1228",
      "incomplete_value": false,
      "site": "005f1228",
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
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f1228",
      "incomplete_value": false,
      "site": "005f1228",
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
            "const:690:8"
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
      "definition_site": "005f12b4",
      "incomplete_value": true,
      "site": "005f12c8",
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
                "const:42e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f12b4",
      "incomplete_value": true,
      "site": "005f12c8",
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
                "const:394:8"
              ]
            ]
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
      "definition_site": "005f12e8",
      "incomplete_value": false,
      "site": "005f12e8",
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
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f12e8",
      "incomplete_value": false,
      "site": "005f12e8",
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
            "const:710:8"
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
      "005f1194",
      "PARAM",
      [
        "storage",
        "00292af8",
        null,
        "string"
      ]
    ],
    [
      "005f1194",
      "PARAM",
      [
        "storage",
        "00299f20",
        null,
        "string"
      ]
    ],
    [
      "005f1228",
      "DATA",
      [
        "storage",
        "00bf4690",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f1194",
      "PARAM",
      [
        "storage",
        "00292a6b",
        null,
        "string"
      ]
    ],
    [
      "005f1194",
      "PARAM",
      [
        "storage",
        "00299f1e",
        null,
        "string"
      ]
    ],
    [
      "005f1228",
      "DATA",
      [
        "storage",
        "00bf46e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f1170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f10d0.md#insn-005f1170) · [`005f118c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f10d0.md#insn-005f118c) · [`005f1220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f10d0.md#insn-005f1220)
- 新版 `005f1170`（命令位置の公開資料なし） · `005f118c`（命令位置の公開資料なし） · `005f1220`（命令位置の公開資料なし）

~~~diff
- 005f1170 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 005f1170 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005f1170 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005f1170 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005f1170 ["COPY", "tmp:0:8", ["const:f1e:8"]]
+ 005f1170 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005f1170 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005f1170 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005f1170 bytes 4a813c91
+ 005f1170 bytes 4a793c91
- 005f118c ["COPY", "tmp:0:8", ["const:af8:8"]]
- 005f118c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f118c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f118c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f118c ["COPY", "tmp:0:8", ["const:a6b:8"]]
+ 005f118c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f118c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f118c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f118c bytes 08e12b91
+ 005f118c bytes 08ad2991
- 005f1220 ["COPY", "tmp:0:8", ["const:690:8"]]
- 005f1220 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005f1220 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005f1220 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005f1220 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 005f1220 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005f1220 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005f1220 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005f1220 bytes 29411a91
+ 005f1220 bytes 29811b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afb45b57d1fecad40cd89bc3b308b063"></a>

### [`005f15cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f15cc.md) → [`005f15cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f15cc.md) FUN_005f15cc

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
      "definition_site": "005f15ec",
      "incomplete_value": false,
      "site": "005f15f0",
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
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f15ec",
      "incomplete_value": false,
      "site": "005f15f0",
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
            "const:690:8"
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
      "005f15f0",
      "DATA",
      [
        "storage",
        "00bf4690",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f15f0",
      "DATA",
      [
        "storage",
        "00bf46e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f15ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f15cc.md#insn-005f15ec)
- 新版 `005f15ec`（命令位置の公開資料なし）

~~~diff
- 005f15ec ["COPY", "tmp:0:8", ["const:690:8"]]
- 005f15ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f15ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f15ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f15ec ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 005f15ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f15ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f15ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f15ec bytes 08411a91
+ 005f15ec bytes 08811b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18c6a9c2091b14384d4df02a54755361"></a>

### [`005f16bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f16bc.md) → [`005f16bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f16bc.md) FUN_005f16bc

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
      "definition_site": "005f16c0",
      "incomplete_value": false,
      "site": "005f16c4",
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
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f16c0",
      "incomplete_value": false,
      "site": "005f16c4",
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
            "const:710:8"
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
      "005f16c4",
      "DATA",
      [
        "storage",
        "00bf4710",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f16c4",
      "DATA",
      [
        "storage",
        "00bf4760",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f16c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f16bc.md#insn-005f16c0)
- 新版 `005f16c0`（命令位置の公開資料なし）

~~~diff
- 005f16c0 ["COPY", "tmp:0:8", ["const:710:8"]]
- 005f16c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f16c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f16c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f16c0 ["COPY", "tmp:0:8", ["const:760:8"]]
+ 005f16c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f16c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f16c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f16c0 bytes 08411c91
+ 005f16c0 bytes 08811d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a40b53868afa317c994c983cc8ebd07"></a>

### [`005f1770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f1770.md) → [`005f1770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1770.md) FUN_005f1770

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
      "definition_site": "005f1784",
      "incomplete_value": false,
      "site": "005f1788",
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
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f1784",
      "incomplete_value": false,
      "site": "005f1788",
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
            "const:7c0:8"
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
      "005f1788",
      "DATA",
      [
        "storage",
        "00bf47c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f1788",
      "DATA",
      [
        "storage",
        "00bf4810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f1784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f1770.md#insn-005f1784)
- 新版 `005f1784`（命令位置の公開資料なし）

~~~diff
- 005f1784 ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 005f1784 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f1784 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f1784 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f1784 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 005f1784 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f1784 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f1784 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f1784 bytes 08011f91
+ 005f1784 bytes 08412091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8e6c428d6b2a3272603e7a82936ca4a"></a>

### [`005f1794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f1794.md) → [`005f1794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1794.md) FUN_005f1794

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
      "definition_site": "005f1798",
      "incomplete_value": false,
      "site": "005f179c",
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
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f1798",
      "incomplete_value": false,
      "site": "005f179c",
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
            "const:7c0:8"
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
      "005f179c",
      "DATA",
      [
        "storage",
        "00bf47c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f179c",
      "DATA",
      [
        "storage",
        "00bf4810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f1798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f1794.md#insn-005f1798)
- 新版 `005f1798`（命令位置の公開資料なし）

~~~diff
- 005f1798 ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 005f1798 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f1798 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f1798 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f1798 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 005f1798 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f1798 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f1798 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f1798 bytes 08011f91
+ 005f1798 bytes 08412091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-842b7a6e778fc285b11e8afa114cc9f8"></a>

### [`005f17dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f17dc.md) → [`005f17dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f17dc.md) FUN_005f17dc

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
      "definition_site": "005f1800",
      "incomplete_value": false,
      "site": "005f1800",
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
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f1800",
      "incomplete_value": false,
      "site": "005f1800",
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
            "const:850:8"
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
      "005f1800",
      "DATA",
      [
        "storage",
        "00bf4850",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f1800",
      "DATA",
      [
        "storage",
        "00bf48a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f17fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f17dc.md#insn-005f17fc)
- 新版 `005f17fc`（命令位置の公開資料なし）

~~~diff
- 005f17fc ["COPY", "tmp:0:8", ["const:850:8"]]
- 005f17fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f17fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f17fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f17fc ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 005f17fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f17fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f17fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f17fc bytes 08412191
+ 005f17fc bytes 08812291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3315c466a7eacabd5a745ca768ef4ce"></a>

### [`005f1810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f1810.md) → [`005f1810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1810.md) FUN_005f1810

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
      "definition_site": "005f181c",
      "incomplete_value": false,
      "site": "005f181c",
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
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f181c",
      "incomplete_value": false,
      "site": "005f181c",
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
            "const:850:8"
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
      "005f181c",
      "DATA",
      [
        "storage",
        "00bf4850",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f181c",
      "DATA",
      [
        "storage",
        "00bf48a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f1818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f1810.md#insn-005f1818)
- 新版 `005f1818`（命令位置の公開資料なし）

~~~diff
- 005f1818 ["COPY", "tmp:0:8", ["const:850:8"]]
- 005f1818 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005f1818 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005f1818 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005f1818 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 005f1818 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005f1818 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005f1818 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005f1818 bytes 29412191
+ 005f1818 bytes 29812291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-166d43c7ab09aab81e9a330200c5762d"></a>

### [`005f1af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f1af0.md) → [`005f1af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1af0.md) FUN_005f1af0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005f192c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f192c.md) [`005f1af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f1af0.md) [`005f6340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f6/005f6340.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041e778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e778.md)
- 新版 呼出元 3件 [`005f192c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f192c.md) [`005f1af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1af0.md) [`005f6340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f6/005f6340.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041e778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.92% / 新版 98.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005f1d18",
      "incomplete_value": false,
      "site": "005f1d20",
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
      "definition_site": "005f1d18",
      "incomplete_value": false,
      "site": "005f1d20",
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
      "definition_site": "005f1d30",
      "incomplete_value": false,
      "site": "005f1d40",
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
      "definition_site": "005f1d30",
      "incomplete_value": false,
      "site": "005f1d40",
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
      "definition_site": "005f1de4",
      "incomplete_value": false,
      "site": "005f1df4",
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
      "definition_site": "005f1de4",
      "incomplete_value": false,
      "site": "005f1df4",
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
      "005f1c60",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "005f1d18",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "005f1d30",
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
      "005f1c60",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "005f1d18",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "005f1d30",
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

- 旧版 [`005f1c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f1af0.md#insn-005f1c60) · [`005f1d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f1af0.md#insn-005f1d18) · [`005f1d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f1af0.md#insn-005f1d30)
- 新版 `005f1c60`（命令位置の公開資料なし） · `005f1d18`（命令位置の公開資料なし） · `005f1d30`（命令位置の公開資料なし）

~~~diff
- 005f1c60 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005f1c60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005f1c60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005f1c60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005f1c60 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 005f1c60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005f1c60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005f1c60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005f1c60 bytes 21280c91
+ 005f1c60 bytes 21900e91
- 005f1d18 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 005f1d18 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005f1d18 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005f1d18 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005f1d18 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 005f1d18 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005f1d18 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005f1d18 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005f1d18 bytes 21b80b91
+ 005f1d18 bytes 21e40d91
- 005f1d30 ["COPY", "tmp:0:8", ["const:919:8"]]
- 005f1d30 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005f1d30 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005f1d30 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005f1d30 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 005f1d30 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005f1d30 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005f1d30 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005f1d30 bytes 21642491
+ 005f1d30 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1b9323a3499f04bdc3cf2a1e986320f"></a>

### [`005f26c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f26c4.md) → [`005f26c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f26c4.md) FUN_005f26c4

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
      "definition_site": "005f26e8",
      "incomplete_value": false,
      "site": "005f26e8",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f26e8",
      "incomplete_value": false,
      "site": "005f26e8",
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
            "const:8d0:8"
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
      "005f26e8",
      "DATA",
      [
        "storage",
        "00bf48d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f26e8",
      "DATA",
      [
        "storage",
        "00bf4920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f26e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f26c4.md#insn-005f26e4)
- 新版 `005f26e4`（命令位置の公開資料なし）

~~~diff
- 005f26e4 ["COPY", "tmp:0:8", ["const:8d0:8"]]
- 005f26e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f26e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f26e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f26e4 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 005f26e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f26e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f26e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f26e4 bytes 08412391
+ 005f26e4 bytes 08812491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1d996a98160cf11ffac96408a3699d2"></a>

### [`005f26f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f26f8.md) → [`005f26f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f26f8.md) FUN_005f26f8

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
      "definition_site": "005f2704",
      "incomplete_value": false,
      "site": "005f2704",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f2704",
      "incomplete_value": false,
      "site": "005f2704",
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
            "const:8d0:8"
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
      "005f2704",
      "DATA",
      [
        "storage",
        "00bf48d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f2704",
      "DATA",
      [
        "storage",
        "00bf4920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f2700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f26f8.md#insn-005f2700)
- 新版 `005f2700`（命令位置の公開資料なし）

~~~diff
- 005f2700 ["COPY", "tmp:0:8", ["const:8d0:8"]]
- 005f2700 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005f2700 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005f2700 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005f2700 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 005f2700 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005f2700 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005f2700 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005f2700 bytes 29412391
+ 005f2700 bytes 29812491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04e3859d622cd65832870e87297cd85f"></a>

### [`005f2714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f2714.md) → [`005f2714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f2714.md) FUN_005f2714

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0057476c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/0057476c.md) [`005f2948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f2948.md) [`005f294c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f294c.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0057476c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057476c.md) [`005f2948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f2948.md) [`005f294c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f294c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005f2804",
      "incomplete_value": false,
      "site": "005f2804",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f2804",
      "incomplete_value": false,
      "site": "005f2804",
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
            "const:940:8"
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
      "005f2804",
      "DATA",
      [
        "storage",
        "00bf4940",
        null,
        "undefined *"
      ]
    ],
    [
      "005f283c",
      "READ",
      [
        "storage",
        "00bf4960",
        null,
        "pointer"
      ]
    ],
    [
      "005f283c",
      "READ",
      [
        "storage",
        "00bf4968",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f2804",
      "DATA",
      [
        "storage",
        "00bf4990",
        null,
        "undefined *"
      ]
    ],
    [
      "005f283c",
      "READ",
      [
        "storage",
        "00bf49b0",
        null,
        "pointer"
      ]
    ],
    [
      "005f283c",
      "READ",
      [
        "storage",
        "00bf49b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f27f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f2714.md#insn-005f27f8)
- 新版 `005f27f8`（命令位置の公開資料なし）

~~~diff
- 005f27f8 ["COPY", "tmp:0:8", ["const:940:8"]]
- 005f27f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f27f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f27f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f27f8 ["COPY", "tmp:0:8", ["const:990:8"]]
+ 005f27f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f27f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f27f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f27f8 bytes 08012591
+ 005f27f8 bytes 08412691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1ede5b3cbd09cbca9ded8e24a5e3878"></a>

### [`005f28e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f28e8.md) → [`005f28e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f28e8.md) FUN_005f28e8

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
      "definition_site": "005f290c",
      "incomplete_value": false,
      "site": "005f2910",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f290c",
      "incomplete_value": false,
      "site": "005f2910",
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
            "const:940:8"
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
      "005f2910",
      "DATA",
      [
        "storage",
        "00bf4940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f2910",
      "DATA",
      [
        "storage",
        "00bf4990",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f290c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f28e8.md#insn-005f290c)
- 新版 `005f290c`（命令位置の公開資料なし）

~~~diff
- 005f290c ["COPY", "tmp:0:8", ["const:940:8"]]
- 005f290c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f290c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f290c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f290c ["COPY", "tmp:0:8", ["const:990:8"]]
+ 005f290c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f290c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f290c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f290c bytes 08012591
+ 005f290c bytes 08412691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e547a74de96b1432c69f3a657573f66"></a>

### [`005f2928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f2928.md) → [`005f2928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f2928.md) FUN_005f2928

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
      "definition_site": "005f292c",
      "incomplete_value": false,
      "site": "005f2930",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f292c",
      "incomplete_value": false,
      "site": "005f2930",
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
            "const:940:8"
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
      "005f2930",
      "DATA",
      [
        "storage",
        "00bf4940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f2930",
      "DATA",
      [
        "storage",
        "00bf4990",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f292c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f2928.md#insn-005f292c)
- 新版 `005f292c`（命令位置の公開資料なし）

~~~diff
- 005f292c ["COPY", "tmp:0:8", ["const:940:8"]]
- 005f292c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f292c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f292c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f292c ["COPY", "tmp:0:8", ["const:990:8"]]
+ 005f292c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f292c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f292c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f292c bytes 08012591
+ 005f292c bytes 08412691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a3a22078227373f6d8437e334012b17"></a>

### [`005f2980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f2980.md) → [`005f2980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f2980.md) FUN_005f2980

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005f2950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f2950.md) · 呼出先 30件 [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0052dd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd50.md)
- 新版 呼出元 1件 [`005f2950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f2950.md) · 呼出先 30件 [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0052dd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd50.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.36% / 新版 92.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `call_target` 10件, `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005f29e8",
      "incomplete_value": true,
      "site": "005f29e8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:a7d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f29e8",
      "incomplete_value": true,
      "site": "005f29e8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:b0a:8"
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
      "definition_site": "005f29ec",
      "incomplete_value": true,
      "site": "005f29ec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005f29ec",
      "incomplete_value": true,
      "site": "005f29ec",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005f2c14",
      "incomplete_value": true,
      "site": "005f2c14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "005f2c14",
      "incomplete_value": true,
      "site": "005f2c14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "005f29b0",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "005f29c0",
      "READ",
      [
        "storage",
        "00c24d78",
        null,
        "undefined4"
      ]
    ],
    [
      "005f29c0",
      "READ",
      [
        "storage",
        "00c24d7c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "005f29b0",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "005f29c0",
      "READ",
      [
        "storage",
        "00c24db8",
        null,
        "undefined4"
      ]
    ],
    [
      "005f29c0",
      "READ",
      [
        "storage",
        "00c24dbc",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f2bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f2980.md#insn-005f2bf0) · [`005f2d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f2980.md#insn-005f2d0c) · [`005f2e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f2980.md#insn-005f2e44)
- 新版 `005f2bf0`（命令位置の公開資料なし） · `005f2d0c`（命令位置の公開資料なし） · `005f2e44`（命令位置の公開資料なし）

~~~diff
- 005f2bf0 ["INT_ADD", "register:40f0:8", ["const:5f2bf0:8", "const:4:8"]]
- 005f2bf0 ["CALL", null, ["ram:a09924:8"]]
+ 005f2bf0 ["INT_ADD", "register:40f0:8", ["const:5f2bf0:8", "const:4:8"]]
+ 005f2bf0 ["CALL", null, ["ram:a09968:8"]]
- 005f2bf0 bytes 4d5b1094
+ 005f2bf0 bytes 5e5b1094
- 005f2d0c ["INT_ADD", "register:40f0:8", ["const:5f2d0c:8", "const:4:8"]]
- 005f2d0c ["CALL", null, ["ram:a09924:8"]]
+ 005f2d0c ["INT_ADD", "register:40f0:8", ["const:5f2d0c:8", "const:4:8"]]
+ 005f2d0c ["CALL", null, ["ram:a09968:8"]]
- 005f2d0c bytes 065b1094
+ 005f2d0c bytes 175b1094
- 005f2e44 ["INT_ADD", "register:40f0:8", ["const:5f2e44:8", "const:4:8"]]
- 005f2e44 ["CALL", null, ["ram:a09924:8"]]
+ 005f2e44 ["INT_ADD", "register:40f0:8", ["const:5f2e44:8", "const:4:8"]]
+ 005f2e44 ["CALL", null, ["ram:a09968:8"]]
- 005f2e44 bytes b85a1094
+ 005f2e44 bytes c95a1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28ca521929537b9fc1bd4a54927fe945"></a>

### [`005f47e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f4/005f47e4.md) → [`005f47e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f4/005f47e4.md) FUN_005f47e4

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
      "definition_site": "005f4804",
      "incomplete_value": false,
      "site": "005f4808",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f4804",
      "incomplete_value": false,
      "site": "005f4808",
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
      "005f4808",
      "DATA",
      [
        "storage",
        "00bf49b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f4808",
      "DATA",
      [
        "storage",
        "00bf4a00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f4804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f4/005f47e4.md#insn-005f4804)
- 新版 `005f4804`（命令位置の公開資料なし）

~~~diff
- 005f4804 ["COPY", "tmp:0:8", ["const:9b0:8"]]
- 005f4804 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f4804 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f4804 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f4804 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005f4804 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f4804 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f4804 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f4804 bytes 08c12691
+ 005f4804 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27d575fc753b4c62f7dbf77dc5fdb2ca"></a>

### [`005f481c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f4/005f481c.md) → [`005f481c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f4/005f481c.md) FUN_005f481c

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
      "definition_site": "005f4820",
      "incomplete_value": false,
      "site": "005f4824",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005f4820",
      "incomplete_value": false,
      "site": "005f4824",
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
      "005f4824",
      "DATA",
      [
        "storage",
        "00bf49b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005f4824",
      "DATA",
      [
        "storage",
        "00bf4a00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f4820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f4/005f481c.md#insn-005f4820)
- 新版 `005f4820`（命令位置の公開資料なし）

~~~diff
- 005f4820 ["COPY", "tmp:0:8", ["const:9b0:8"]]
- 005f4820 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005f4820 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005f4820 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005f4820 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005f4820 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005f4820 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005f4820 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005f4820 bytes 08c12691
+ 005f4820 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c76cac0fc5c1acb497c185edca4e925"></a>

### [`005f4a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f4/005f4a84.md) → [`005f4a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f4/005f4a84.md) FUN_005f4a84

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005f48b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f4/005f48b8.md) [`005f4a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f4/005f4a84.md) [`00946864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00946/00946864.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`005f48b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f4/005f48b8.md) [`005f4a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f4/005f4a84.md) [`00946864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00946/00946864.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.93% / 新版 98.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005f4bf8",
      "incomplete_value": false,
      "site": "005f4c04",
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
      "definition_site": "005f4bf8",
      "incomplete_value": false,
      "site": "005f4c04",
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
      "definition_site": "005f4cb0",
      "incomplete_value": false,
      "site": "005f4cb8",
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
      "definition_site": "005f4cb0",
      "incomplete_value": false,
      "site": "005f4cb8",
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
      "definition_site": "005f501c",
      "incomplete_value": false,
      "site": "005f5028",
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
      "definition_site": "005f501c",
      "incomplete_value": false,
      "site": "005f5028",
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
    "ordinal": 22,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005f4bf8",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "005f4cb0",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "005f4cc8",
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
      "005f4bf8",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "005f4cb0",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "005f4cc8",
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

- 旧版 [`005f4bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f4/005f4a84.md#insn-005f4bf8) · [`005f4cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f4/005f4a84.md#insn-005f4cb0) · [`005f4cc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f4/005f4a84.md#insn-005f4cc8)
- 新版 `005f4bf8`（命令位置の公開資料なし） · `005f4cb0`（命令位置の公開資料なし） · `005f4cc8`（命令位置の公開資料なし）

~~~diff
- 005f4bf8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005f4bf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005f4bf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005f4bf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005f4bf8 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 005f4bf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005f4bf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005f4bf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005f4bf8 bytes 21280c91
+ 005f4bf8 bytes 21900e91
- 005f4cb0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 005f4cb0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005f4cb0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005f4cb0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005f4cb0 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 005f4cb0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005f4cb0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005f4cb0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005f4cb0 bytes 21b80b91
+ 005f4cb0 bytes 21e40d91
- 005f4cc8 ["COPY", "tmp:0:8", ["const:919:8"]]
- 005f4cc8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005f4cc8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005f4cc8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005f4cc8 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 005f4cc8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005f4cc8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005f4cc8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005f4cc8 bytes 21642491
+ 005f4cc8 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

