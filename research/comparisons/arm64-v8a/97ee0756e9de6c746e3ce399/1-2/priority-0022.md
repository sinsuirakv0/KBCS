# v15.7.3 → v15.7.4 · 最優先の変更候補 (22)

[一覧の目次](README.md)

<a id="compare-5507915e631907745601cad8bd876e2a"></a>

### [`00590d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590d18.md) → [`00590d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590d18.md) FUN_00590d18

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
      "definition_site": "00590d3c",
      "incomplete_value": false,
      "site": "00590d3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590d3c",
      "incomplete_value": false,
      "site": "00590d3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
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
      "00590d3c",
      "DATA",
      [
        "storage",
        "00bf22c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590d3c",
      "DATA",
      [
        "storage",
        "00bf2318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590d18.md#insn-00590d38)
- 新版 `00590d38`（命令位置の公開資料なし）

~~~diff
- 00590d38 ["COPY", "tmp:0:8", ["const:2c8:8"]]
- 00590d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00590d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00590d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00590d38 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 00590d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00590d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00590d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00590d38 bytes 08210b91
+ 00590d38 bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e72ef7614548c813cb9afb2ce2ecec78"></a>

### [`00590d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590d4c.md) → [`00590d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590d4c.md) FUN_00590d4c

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
      "definition_site": "00590d58",
      "incomplete_value": false,
      "site": "00590d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590d58",
      "incomplete_value": false,
      "site": "00590d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
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
      "00590d58",
      "DATA",
      [
        "storage",
        "00bf22c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590d58",
      "DATA",
      [
        "storage",
        "00bf2318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590d4c.md#insn-00590d54)
- 新版 `00590d54`（命令位置の公開資料なし）

~~~diff
- 00590d54 ["COPY", "tmp:0:8", ["const:2c8:8"]]
- 00590d54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00590d54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00590d54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00590d54 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 00590d54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00590d54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00590d54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00590d54 bytes 29210b91
+ 00590d54 bytes 29610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db0bbe178a36cd80662cf92830332370"></a>

### [`00590dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590dc4.md) → [`00590dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590dc4.md) FUN_00590dc4

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
      "definition_site": "00590dcc",
      "incomplete_value": false,
      "site": "00590dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590dcc",
      "incomplete_value": false,
      "site": "00590dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:358:8"
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
      "00590dd0",
      "DATA",
      [
        "storage",
        "00bf2358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590dd0",
      "DATA",
      [
        "storage",
        "00bf23a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590dc4.md#insn-00590dcc)
- 新版 `00590dcc`（命令位置の公開資料なし）

~~~diff
- 00590dcc ["COPY", "tmp:0:8", ["const:358:8"]]
- 00590dcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00590dcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00590dcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00590dcc ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 00590dcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00590dcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00590dcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00590dcc bytes 29610d91
+ 00590dcc bytes 29a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce27ccd162ad2a645ee492751e3c0915"></a>

### [`00590de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590de4.md) → [`00590de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590de4.md) FUN_00590de4

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
      "definition_site": "00590dec",
      "incomplete_value": false,
      "site": "00590df0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590dec",
      "incomplete_value": false,
      "site": "00590df0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:358:8"
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
      "00590df0",
      "DATA",
      [
        "storage",
        "00bf2358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590df0",
      "DATA",
      [
        "storage",
        "00bf23a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590de4.md#insn-00590dec)
- 新版 `00590dec`（命令位置の公開資料なし）

~~~diff
- 00590dec ["COPY", "tmp:0:8", ["const:358:8"]]
- 00590dec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00590dec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00590dec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00590dec ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 00590dec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00590dec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00590dec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00590dec bytes 29610d91
+ 00590dec bytes 29a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73acb29ea6e3cc15e42a8035482b2ad7"></a>

### [`00590e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590e24.md) → [`00590e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590e24.md) FUN_00590e24

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00590e54",
      "incomplete_value": false,
      "site": "00590e54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590e54",
      "incomplete_value": false,
      "site": "00590e54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:358:8"
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
      "00590e54",
      "DATA",
      [
        "storage",
        "00bf2358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590e54",
      "DATA",
      [
        "storage",
        "00bf23a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590e24.md#insn-00590e48)
- 新版 `00590e48`（命令位置の公開資料なし）

~~~diff
- 00590e48 ["COPY", "tmp:0:8", ["const:358:8"]]
- 00590e48 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00590e48 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00590e48 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00590e48 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 00590e48 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00590e48 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00590e48 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00590e48 bytes 6b610d91
+ 00590e48 bytes 6ba10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38892e22230e70a0255c41b7d5bf2a6a"></a>

### [`00590ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590ea0.md) → [`00590ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590ea0.md) FUN_00590ea0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)

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
      "definition_site": "00590eac",
      "incomplete_value": false,
      "site": "00590eac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590eac",
      "incomplete_value": false,
      "site": "00590eac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:358:8"
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
      "00590eac",
      "DATA",
      [
        "storage",
        "00bf2358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590eac",
      "DATA",
      [
        "storage",
        "00bf23a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590ea0.md#insn-00590ea8)
- 新版 `00590ea8`（命令位置の公開資料なし）

~~~diff
- 00590ea8 ["COPY", "tmp:0:8", ["const:358:8"]]
- 00590ea8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00590ea8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00590ea8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00590ea8 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 00590ea8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00590ea8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00590ea8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00590ea8 bytes 29610d91
+ 00590ea8 bytes 29a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d24789273b87aee39ca84dda04f23e8"></a>

### [`00590f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590f64.md) → [`00590f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590f64.md) FUN_00590f64

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
      "definition_site": "00590f88",
      "incomplete_value": false,
      "site": "00590f88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590f88",
      "incomplete_value": false,
      "site": "00590f88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
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
      "00590f88",
      "DATA",
      [
        "storage",
        "00bf23e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590f88",
      "DATA",
      [
        "storage",
        "00bf2438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590f64.md#insn-00590f84)
- 新版 `00590f84`（命令位置の公開資料なし）

~~~diff
- 00590f84 ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 00590f84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00590f84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00590f84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00590f84 ["COPY", "tmp:0:8", ["const:438:8"]]
+ 00590f84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00590f84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00590f84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00590f84 bytes 08a10f91
+ 00590f84 bytes 08e11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7027f7c148bbe6fbe5194f18da243c2b"></a>

### [`00590f98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590f98.md) → [`00590f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590f98.md) FUN_00590f98

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
      "definition_site": "00590fa4",
      "incomplete_value": false,
      "site": "00590fa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590fa4",
      "incomplete_value": false,
      "site": "00590fa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
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
      "00590fa4",
      "DATA",
      [
        "storage",
        "00bf23e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590fa4",
      "DATA",
      [
        "storage",
        "00bf2438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590f98.md#insn-00590fa0)
- 新版 `00590fa0`（命令位置の公開資料なし）

~~~diff
- 00590fa0 ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 00590fa0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00590fa0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00590fa0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00590fa0 ["COPY", "tmp:0:8", ["const:438:8"]]
+ 00590fa0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00590fa0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00590fa0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00590fa0 bytes 29a10f91
+ 00590fa0 bytes 29e11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10e08a6c152455c3c68f68317740ecfb"></a>

### [`0059101c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059101c.md) → [`0059101c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/0059101c.md) FUN_0059101c

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
      "definition_site": "00591040",
      "incomplete_value": false,
      "site": "00591040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:4b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591040",
      "incomplete_value": false,
      "site": "00591040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:468:8"
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
      "00591040",
      "DATA",
      [
        "storage",
        "00bf2468",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591040",
      "DATA",
      [
        "storage",
        "00bf24b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059103c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059101c.md#insn-0059103c)
- 新版 `0059103c`（命令位置の公開資料なし）

~~~diff
- 0059103c ["COPY", "tmp:0:8", ["const:468:8"]]
- 0059103c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059103c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059103c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059103c ["COPY", "tmp:0:8", ["const:4b8:8"]]
+ 0059103c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059103c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059103c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059103c bytes 08a11191
+ 0059103c bytes 08e11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ec37ee321e96cf4438a894bd54d43b8"></a>

### [`00591050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591050.md) → [`00591050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591050.md) FUN_00591050

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
      "definition_site": "0059105c",
      "incomplete_value": false,
      "site": "0059105c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:4b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059105c",
      "incomplete_value": false,
      "site": "0059105c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:468:8"
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
      "0059105c",
      "DATA",
      [
        "storage",
        "00bf2468",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059105c",
      "DATA",
      [
        "storage",
        "00bf24b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591050.md#insn-00591058)
- 新版 `00591058`（命令位置の公開資料なし）

~~~diff
- 00591058 ["COPY", "tmp:0:8", ["const:468:8"]]
- 00591058 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00591058 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00591058 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00591058 ["COPY", "tmp:0:8", ["const:4b8:8"]]
+ 00591058 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00591058 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00591058 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00591058 bytes 29a11191
+ 00591058 bytes 29e11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e8ea5a25ffb9adbfb5c4e0727aa4f53"></a>

### [`005910a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005910a0.md) → [`005910a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005910a0.md) FUN_005910a0

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
      "definition_site": "005910c4",
      "incomplete_value": false,
      "site": "005910c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005910c4",
      "incomplete_value": false,
      "site": "005910c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:4e8:8"
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
      "005910c4",
      "DATA",
      [
        "storage",
        "00bf24e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005910c4",
      "DATA",
      [
        "storage",
        "00bf2538",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005910c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005910a0.md#insn-005910c0)
- 新版 `005910c0`（命令位置の公開資料なし）

~~~diff
- 005910c0 ["COPY", "tmp:0:8", ["const:4e8:8"]]
- 005910c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005910c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005910c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005910c0 ["COPY", "tmp:0:8", ["const:538:8"]]
+ 005910c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005910c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005910c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005910c0 bytes 08a11391
+ 005910c0 bytes 08e11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f069295d6acc770ac07e1a158b0c4992"></a>

### [`005910d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005910d4.md) → [`005910d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005910d4.md) FUN_005910d4

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
      "definition_site": "005910e0",
      "incomplete_value": false,
      "site": "005910e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005910e0",
      "incomplete_value": false,
      "site": "005910e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:4e8:8"
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
      "005910e0",
      "DATA",
      [
        "storage",
        "00bf24e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005910e0",
      "DATA",
      [
        "storage",
        "00bf2538",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005910dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005910d4.md#insn-005910dc)
- 新版 `005910dc`（命令位置の公開資料なし）

~~~diff
- 005910dc ["COPY", "tmp:0:8", ["const:4e8:8"]]
- 005910dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005910dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005910dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005910dc ["COPY", "tmp:0:8", ["const:538:8"]]
+ 005910dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005910dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005910dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005910dc bytes 29a11391
+ 005910dc bytes 29e11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e50296368c2b50ad01126b491b06bc6f"></a>

### [`00591154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591154.md) → [`00591154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591154.md) FUN_00591154

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
      "definition_site": "00591178",
      "incomplete_value": false,
      "site": "00591178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591178",
      "incomplete_value": false,
      "site": "00591178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:568:8"
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
      "00591178",
      "DATA",
      [
        "storage",
        "00bf2568",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591178",
      "DATA",
      [
        "storage",
        "00bf25b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591154.md#insn-00591174)
- 新版 `00591174`（命令位置の公開資料なし）

~~~diff
- 00591174 ["COPY", "tmp:0:8", ["const:568:8"]]
- 00591174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591174 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 00591174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591174 bytes 08a11591
+ 00591174 bytes 08e11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04a0cea327fe6413633504c0443f930c"></a>

### [`00591188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591188.md) → [`00591188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591188.md) FUN_00591188

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
      "definition_site": "00591194",
      "incomplete_value": false,
      "site": "00591194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591194",
      "incomplete_value": false,
      "site": "00591194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:568:8"
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
      "00591194",
      "DATA",
      [
        "storage",
        "00bf2568",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591194",
      "DATA",
      [
        "storage",
        "00bf25b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591188.md#insn-00591190)
- 新版 `00591190`（命令位置の公開資料なし）

~~~diff
- 00591190 ["COPY", "tmp:0:8", ["const:568:8"]]
- 00591190 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00591190 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00591190 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00591190 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 00591190 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00591190 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00591190 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00591190 bytes 29a11591
+ 00591190 bytes 29e11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9772947aa1f88fe6bc43f3ea770a26a2"></a>

### [`005911a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005911a4.md) → [`005911a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005911a4.md) FUN_005911a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`00591404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591404.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`00591404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591404.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00591220",
      "incomplete_value": false,
      "site": "00591228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591220",
      "incomplete_value": false,
      "site": "00591228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "00591228",
      "DATA",
      [
        "storage",
        "00bf25d8",
        null,
        "pointer"
      ]
    ],
    [
      "005912c0",
      "READ",
      [
        "storage",
        "00bf25e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591228",
      "DATA",
      [
        "storage",
        "00bf2628",
        null,
        "pointer"
      ]
    ],
    [
      "005912c0",
      "READ",
      [
        "storage",
        "00bf2638",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005911a4.md#insn-00591220) · [`00591224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005911a4.md#insn-00591224)
- 新版 `00591220`（命令位置の公開資料なし） · `00591224`（命令位置の公開資料なし）

~~~diff
- 00591220 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00591220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591220 ["COPY", "tmp:0:8", ["const:628:8"]]
+ 00591220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591220 bytes 08611791
+ 00591220 bytes 08a11891
- 00591224 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00591224 bytes f30300aa
+ 00591224 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00591224 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc8793bdc2bbb503e668eb46809141ae"></a>

### [`005913c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005913c4.md) → [`005913c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005913c4.md) FUN_005913c4

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
      "definition_site": "005913c8",
      "incomplete_value": false,
      "site": "005913cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005913c8",
      "incomplete_value": false,
      "site": "005913cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "005913cc",
      "DATA",
      [
        "storage",
        "00bf25d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005913cc",
      "DATA",
      [
        "storage",
        "00bf2628",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005913c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005913c4.md#insn-005913c8)
- 新版 `005913c8`（命令位置の公開資料なし）

~~~diff
- 005913c8 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 005913c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005913c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005913c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005913c8 ["COPY", "tmp:0:8", ["const:628:8"]]
+ 005913c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005913c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005913c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005913c8 bytes 08611791
+ 005913c8 bytes 08a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bba9829bfc34a4b16e48cb3eb531c4c"></a>

### [`005913d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005913d4.md) → [`005913d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005913d4.md) FUN_005913d4

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
      "definition_site": "005913e4",
      "incomplete_value": false,
      "site": "005913ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005913e4",
      "incomplete_value": false,
      "site": "005913ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "005913ec",
      "DATA",
      [
        "storage",
        "00bf25d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005913ec",
      "DATA",
      [
        "storage",
        "00bf2628",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005913e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005913d4.md#insn-005913e4)
- 新版 `005913e4`（命令位置の公開資料なし）

~~~diff
- 005913e4 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 005913e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005913e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005913e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005913e4 ["COPY", "tmp:0:8", ["const:628:8"]]
+ 005913e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005913e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005913e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005913e4 bytes 08611791
+ 005913e4 bytes 08a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a38448e8a443f612fec038a0fc970e0"></a>

### [`00591420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591420.md) → [`00591420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591420.md) FUN_00591420

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
      "definition_site": "00591444",
      "incomplete_value": false,
      "site": "00591444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591444",
      "incomplete_value": false,
      "site": "00591444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:638:8"
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
      "00591444",
      "DATA",
      [
        "storage",
        "00bf2638",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591444",
      "DATA",
      [
        "storage",
        "00bf2688",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591420.md#insn-00591440)
- 新版 `00591440`（命令位置の公開資料なし）

~~~diff
- 00591440 ["COPY", "tmp:0:8", ["const:638:8"]]
- 00591440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591440 ["COPY", "tmp:0:8", ["const:688:8"]]
+ 00591440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591440 bytes 08e11891
+ 00591440 bytes 08211a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e5f83c99f974e43c6c38e8aea699657"></a>

### [`00591454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591454.md) → [`00591454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591454.md) FUN_00591454

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
      "definition_site": "00591460",
      "incomplete_value": false,
      "site": "00591460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591460",
      "incomplete_value": false,
      "site": "00591460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:638:8"
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
      "00591460",
      "DATA",
      [
        "storage",
        "00bf2638",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591460",
      "DATA",
      [
        "storage",
        "00bf2688",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059145c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591454.md#insn-0059145c)
- 新版 `0059145c`（命令位置の公開資料なし）

~~~diff
- 0059145c ["COPY", "tmp:0:8", ["const:638:8"]]
- 0059145c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059145c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059145c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059145c ["COPY", "tmp:0:8", ["const:688:8"]]
+ 0059145c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059145c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059145c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059145c bytes 29e11891
+ 0059145c bytes 29211a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-614f0d7cf1a608a576720ed127b67fd6"></a>

### [`005914e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005914e4.md) → [`005914e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005914e4.md) FUN_005914e4

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
      "definition_site": "00591504",
      "incomplete_value": false,
      "site": "00591508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591504",
      "incomplete_value": false,
      "site": "00591508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
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
      "00591508",
      "DATA",
      [
        "storage",
        "00bf26c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591508",
      "DATA",
      [
        "storage",
        "00bf2718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005914e4.md#insn-00591504)
- 新版 `00591504`（命令位置の公開資料なし）

~~~diff
- 00591504 ["COPY", "tmp:0:8", ["const:6c8:8"]]
- 00591504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591504 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 00591504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591504 bytes 08211b91
+ 00591504 bytes 08611c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d41639d05f2863e7aada7cb4d24aad36"></a>

### [`0059151c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059151c.md) → [`0059151c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/0059151c.md) FUN_0059151c

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
      "definition_site": "00591520",
      "incomplete_value": false,
      "site": "00591524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591520",
      "incomplete_value": false,
      "site": "00591524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
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
      "00591524",
      "DATA",
      [
        "storage",
        "00bf26c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591524",
      "DATA",
      [
        "storage",
        "00bf2718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059151c.md#insn-00591520)
- 新版 `00591520`（命令位置の公開資料なし）

~~~diff
- 00591520 ["COPY", "tmp:0:8", ["const:6c8:8"]]
- 00591520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591520 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 00591520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591520 bytes 08211b91
+ 00591520 bytes 08611c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cae19d99bd04eb4bc17d202e76c9e299"></a>

### [`0059158c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059158c.md) → [`0059158c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/0059158c.md) FUN_0059158c

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
      "definition_site": "005915b0",
      "incomplete_value": false,
      "site": "005915b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005915b0",
      "incomplete_value": false,
      "site": "005915b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:748:8"
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
      "005915b0",
      "DATA",
      [
        "storage",
        "00bf2748",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005915b0",
      "DATA",
      [
        "storage",
        "00bf2798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005915ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059158c.md#insn-005915ac)
- 新版 `005915ac`（命令位置の公開資料なし）

~~~diff
- 005915ac ["COPY", "tmp:0:8", ["const:748:8"]]
- 005915ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005915ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005915ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005915ac ["COPY", "tmp:0:8", ["const:798:8"]]
+ 005915ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005915ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005915ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005915ac bytes 08211d91
+ 005915ac bytes 08611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab8b802094554926d2656cc2df8b91a1"></a>

### [`005915c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005915c0.md) → [`005915c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005915c0.md) FUN_005915c0

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
      "definition_site": "005915cc",
      "incomplete_value": false,
      "site": "005915cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005915cc",
      "incomplete_value": false,
      "site": "005915cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:748:8"
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
      "005915cc",
      "DATA",
      [
        "storage",
        "00bf2748",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005915cc",
      "DATA",
      [
        "storage",
        "00bf2798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005915c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005915c0.md#insn-005915c8)
- 新版 `005915c8`（命令位置の公開資料なし）

~~~diff
- 005915c8 ["COPY", "tmp:0:8", ["const:748:8"]]
- 005915c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005915c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005915c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005915c8 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 005915c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005915c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005915c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005915c8 bytes 29211d91
+ 005915c8 bytes 29611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-100934fd4e179b9dcc539887e8749780"></a>

### [`00591620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591620.md) → [`00591620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591620.md) FUN_00591620

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
      "definition_site": "00591644",
      "incomplete_value": false,
      "site": "00591644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591644",
      "incomplete_value": false,
      "site": "00591644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:7c8:8"
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
      "00591644",
      "DATA",
      [
        "storage",
        "00bf27c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591644",
      "DATA",
      [
        "storage",
        "00bf2818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591620.md#insn-00591640)
- 新版 `00591640`（命令位置の公開資料なし）

~~~diff
- 00591640 ["COPY", "tmp:0:8", ["const:7c8:8"]]
- 00591640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591640 ["COPY", "tmp:0:8", ["const:818:8"]]
+ 00591640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591640 bytes 08211f91
+ 00591640 bytes 08612091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-839f193b465cc2148635fb10bf52bbf7"></a>

### [`00591654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591654.md) → [`00591654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591654.md) FUN_00591654

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
      "definition_site": "00591660",
      "incomplete_value": false,
      "site": "00591660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591660",
      "incomplete_value": false,
      "site": "00591660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:7c8:8"
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
      "00591660",
      "DATA",
      [
        "storage",
        "00bf27c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591660",
      "DATA",
      [
        "storage",
        "00bf2818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059165c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591654.md#insn-0059165c)
- 新版 `0059165c`（命令位置の公開資料なし）

~~~diff
- 0059165c ["COPY", "tmp:0:8", ["const:7c8:8"]]
- 0059165c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059165c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059165c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059165c ["COPY", "tmp:0:8", ["const:818:8"]]
+ 0059165c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059165c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059165c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059165c bytes 29211f91
+ 0059165c bytes 29612091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5211691ea74061b6a3c3a92c4f3d6875"></a>

### [`0059177c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059177c.md) → [`0059177c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/0059177c.md) FUN_0059177c

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
      "definition_site": "00591788",
      "incomplete_value": false,
      "site": "00591788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591788",
      "incomplete_value": false,
      "site": "00591788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
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
      "00591788",
      "DATA",
      [
        "storage",
        "00bf2848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591788",
      "DATA",
      [
        "storage",
        "00bf2898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059177c.md#insn-00591784)
- 新版 `00591784`（命令位置の公開資料なし）

~~~diff
- 00591784 ["COPY", "tmp:0:8", ["const:848:8"]]
- 00591784 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00591784 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00591784 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00591784 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00591784 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00591784 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00591784 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00591784 bytes 29212191
+ 00591784 bytes 29612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a43a22876b2965aac815a4096e500e5a"></a>

### [`005917e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005917e0.md) → [`005917e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005917e0.md) FUN_005917e0

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
      "definition_site": "00591800",
      "incomplete_value": false,
      "site": "00591804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591800",
      "incomplete_value": false,
      "site": "00591804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
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
      "00591804",
      "DATA",
      [
        "storage",
        "00bf28c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591804",
      "DATA",
      [
        "storage",
        "00bf2918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005917e0.md#insn-00591800)
- 新版 `00591800`（命令位置の公開資料なし）

~~~diff
- 00591800 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 00591800 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591800 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591800 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591800 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 00591800 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591800 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591800 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591800 bytes 08212391
+ 00591800 bytes 08612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-599200dc27c5409e87a89838e7e68369"></a>

### [`00591818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591818.md) → [`00591818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591818.md) FUN_00591818

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059181c",
      "incomplete_value": true,
      "site": "00591820",
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
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059181c",
      "incomplete_value": true,
      "site": "00591820",
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
      "00591820",
      "DATA",
      [
        "storage",
        "00bf28c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591820",
      "DATA",
      [
        "storage",
        "00bf2918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059181c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591818.md#insn-0059181c)
- 新版 `0059181c`（命令位置の公開資料なし）

~~~diff
- 0059181c ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 0059181c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059181c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059181c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059181c ["COPY", "tmp:0:8", ["const:918:8"]]
+ 0059181c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059181c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059181c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059181c bytes 08212391
+ 0059181c bytes 08612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b52e18d7efdac35a7338dd2953cd44d"></a>

### [`00591934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591934.md) → [`00591934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591934.md) FUN_00591934

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
      "definition_site": "00591954",
      "incomplete_value": false,
      "site": "00591958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591954",
      "incomplete_value": false,
      "site": "00591958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "00591958",
      "DATA",
      [
        "storage",
        "00bf2958",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591958",
      "DATA",
      [
        "storage",
        "00bf29a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591934.md#insn-00591954)
- 新版 `00591954`（命令位置の公開資料なし）

~~~diff
- 00591954 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00591954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591954 ["COPY", "tmp:0:8", ["const:9a8:8"]]
+ 00591954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591954 bytes 08612591
+ 00591954 bytes 08a12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-475563f265a152cf8f72a5746523619d"></a>

### [`0059196c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059196c.md) → [`0059196c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/0059196c.md) FUN_0059196c

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
      "definition_site": "00591970",
      "incomplete_value": false,
      "site": "00591974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591970",
      "incomplete_value": false,
      "site": "00591974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "00591974",
      "DATA",
      [
        "storage",
        "00bf2958",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591974",
      "DATA",
      [
        "storage",
        "00bf29a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059196c.md#insn-00591970)
- 新版 `00591970`（命令位置の公開資料なし）

~~~diff
- 00591970 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00591970 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591970 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591970 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591970 ["COPY", "tmp:0:8", ["const:9a8:8"]]
+ 00591970 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591970 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591970 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591970 bytes 08612591
+ 00591970 bytes 08a12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93c5f9160948396e9c3fbe1be5ada515"></a>

### [`00591a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591a9c.md) → [`00591a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591a9c.md) FUN_00591a9c

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
      "definition_site": "00591abc",
      "incomplete_value": false,
      "site": "00591ac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591abc",
      "incomplete_value": false,
      "site": "00591ac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
      "00591ac0",
      "DATA",
      [
        "storage",
        "00bf29e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591ac0",
      "DATA",
      [
        "storage",
        "00bf2a38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591a9c.md#insn-00591abc)
- 新版 `00591abc`（命令位置の公開資料なし）

~~~diff
- 00591abc ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 00591abc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591abc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591abc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591abc ["COPY", "tmp:0:8", ["const:a38:8"]]
+ 00591abc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591abc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591abc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591abc bytes 08a12791
+ 00591abc bytes 08e12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae81d3fa1bfaa4c699a3561d2e7a9c16"></a>

### [`00591ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591ad4.md) → [`00591ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591ad4.md) FUN_00591ad4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00591ad8",
      "incomplete_value": true,
      "site": "00591adc",
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
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591ad8",
      "incomplete_value": true,
      "site": "00591adc",
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
            "const:9e8:8"
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
      "00591adc",
      "DATA",
      [
        "storage",
        "00bf29e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591adc",
      "DATA",
      [
        "storage",
        "00bf2a38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591ad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591ad4.md#insn-00591ad8)
- 新版 `00591ad8`（命令位置の公開資料なし）

~~~diff
- 00591ad8 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 00591ad8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591ad8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591ad8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591ad8 ["COPY", "tmp:0:8", ["const:a38:8"]]
+ 00591ad8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591ad8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591ad8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591ad8 bytes 08a12791
+ 00591ad8 bytes 08e12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed0f4ca1d1f9ec15901999a91c1c8691"></a>

### [`00591b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591b34.md) → [`00591b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591b34.md) FUN_00591b34

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
      "definition_site": "00591b58",
      "incomplete_value": false,
      "site": "00591b58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591b58",
      "incomplete_value": false,
      "site": "00591b58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "00591b58",
      "DATA",
      [
        "storage",
        "00bf2a68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591b58",
      "DATA",
      [
        "storage",
        "00bf2ab8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591b34.md#insn-00591b54)
- 新版 `00591b54`（命令位置の公開資料なし）

~~~diff
- 00591b54 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 00591b54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591b54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591b54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591b54 ["COPY", "tmp:0:8", ["const:ab8:8"]]
+ 00591b54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591b54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591b54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591b54 bytes 08a12991
+ 00591b54 bytes 08e12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59fa4089296f1d71955a07b198c8aeab"></a>

### [`00591b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591b68.md) → [`00591b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591b68.md) FUN_00591b68

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
      "definition_site": "00591b74",
      "incomplete_value": false,
      "site": "00591b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591b74",
      "incomplete_value": false,
      "site": "00591b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "00591b74",
      "DATA",
      [
        "storage",
        "00bf2a68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591b74",
      "DATA",
      [
        "storage",
        "00bf2ab8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591b68.md#insn-00591b70)
- 新版 `00591b70`（命令位置の公開資料なし）

~~~diff
- 00591b70 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 00591b70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00591b70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00591b70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00591b70 ["COPY", "tmp:0:8", ["const:ab8:8"]]
+ 00591b70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00591b70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00591b70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00591b70 bytes 29a12991
+ 00591b70 bytes 29e12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9fc5bf61d9d4433844ed680c8aaa41c"></a>

### [`00591be8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591be8.md) → [`00591be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591be8.md) FUN_00591be8

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
      "definition_site": "00591c0c",
      "incomplete_value": false,
      "site": "00591c0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591c0c",
      "incomplete_value": false,
      "site": "00591c0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "00591c0c",
      "DATA",
      [
        "storage",
        "00bf2ae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591c0c",
      "DATA",
      [
        "storage",
        "00bf2b38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591be8.md#insn-00591c08)
- 新版 `00591c08`（命令位置の公開資料なし）

~~~diff
- 00591c08 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 00591c08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591c08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591c08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591c08 ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 00591c08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591c08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591c08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591c08 bytes 08a12b91
+ 00591c08 bytes 08e12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f4eb1b05c21bb19b15cceb29193f723"></a>

### [`00591c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591c1c.md) → [`00591c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591c1c.md) FUN_00591c1c

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
      "definition_site": "00591c28",
      "incomplete_value": false,
      "site": "00591c28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591c28",
      "incomplete_value": false,
      "site": "00591c28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "00591c28",
      "DATA",
      [
        "storage",
        "00bf2ae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591c28",
      "DATA",
      [
        "storage",
        "00bf2b38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591c1c.md#insn-00591c24)
- 新版 `00591c24`（命令位置の公開資料なし）

~~~diff
- 00591c24 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 00591c24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00591c24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00591c24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00591c24 ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 00591c24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00591c24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00591c24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00591c24 bytes 29a12b91
+ 00591c24 bytes 29e12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd806d2499f978e31b59ed7860871ebd"></a>

### [`00591d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591d10.md) → [`00591d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591d10.md) FUN_00591d10

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
      "definition_site": "00591d34",
      "incomplete_value": false,
      "site": "00591d34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591d34",
      "incomplete_value": false,
      "site": "00591d34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "00591d34",
      "DATA",
      [
        "storage",
        "00bf2b68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591d34",
      "DATA",
      [
        "storage",
        "00bf2bb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591d10.md#insn-00591d30)
- 新版 `00591d30`（命令位置の公開資料なし）

~~~diff
- 00591d30 ["COPY", "tmp:0:8", ["const:b68:8"]]
- 00591d30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591d30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591d30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591d30 ["COPY", "tmp:0:8", ["const:bb8:8"]]
+ 00591d30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591d30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591d30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591d30 bytes 08a12d91
+ 00591d30 bytes 08e12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48df43f44a57b8b86aa25707227c00b1"></a>

### [`00591d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591d44.md) → [`00591d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591d44.md) FUN_00591d44

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
      "definition_site": "00591d50",
      "incomplete_value": false,
      "site": "00591d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591d50",
      "incomplete_value": false,
      "site": "00591d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "00591d50",
      "DATA",
      [
        "storage",
        "00bf2b68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591d50",
      "DATA",
      [
        "storage",
        "00bf2bb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591d44.md#insn-00591d4c)
- 新版 `00591d4c`（命令位置の公開資料なし）

~~~diff
- 00591d4c ["COPY", "tmp:0:8", ["const:b68:8"]]
- 00591d4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00591d4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00591d4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00591d4c ["COPY", "tmp:0:8", ["const:bb8:8"]]
+ 00591d4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00591d4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00591d4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00591d4c bytes 29a12d91
+ 00591d4c bytes 29e12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5710029e9b57e0dfa239298588092d06"></a>

### [`00591da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591da8.md) → [`00591da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591da8.md) FUN_00591da8

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
      "definition_site": "00591dcc",
      "incomplete_value": false,
      "site": "00591dcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591dcc",
      "incomplete_value": false,
      "site": "00591dcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "00591dcc",
      "DATA",
      [
        "storage",
        "00bf2be8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591dcc",
      "DATA",
      [
        "storage",
        "00bf2c38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591da8.md#insn-00591dc8)
- 新版 `00591dc8`（命令位置の公開資料なし）

~~~diff
- 00591dc8 ["COPY", "tmp:0:8", ["const:be8:8"]]
- 00591dc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591dc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591dc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591dc8 ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 00591dc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591dc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591dc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591dc8 bytes 08a12f91
+ 00591dc8 bytes 08e13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c38ea0a3fc57620768adf5fb8c33442"></a>

### [`00591ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591ddc.md) → [`00591ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591ddc.md) FUN_00591ddc

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
      "definition_site": "00591de8",
      "incomplete_value": true,
      "site": "00591de8",
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
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591de8",
      "incomplete_value": true,
      "site": "00591de8",
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
            "const:be8:8"
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
      "00591de8",
      "DATA",
      [
        "storage",
        "00bf2be8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591de8",
      "DATA",
      [
        "storage",
        "00bf2c38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591ddc.md#insn-00591de4)
- 新版 `00591de4`（命令位置の公開資料なし）

~~~diff
- 00591de4 ["COPY", "tmp:0:8", ["const:be8:8"]]
- 00591de4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00591de4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00591de4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00591de4 ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 00591de4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00591de4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00591de4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00591de4 bytes 29a12f91
+ 00591de4 bytes 29e13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d15b19e1575ad0c673d85fe4702f9a1"></a>

### [`00591df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591df8.md) → [`00591df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591df8.md) FUN_00591df8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0051c140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051c140.md) [`0059201c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059201c.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0051c140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c140.md) [`0059201c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/0059201c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00591e74",
      "incomplete_value": false,
      "site": "00591e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591e74",
      "incomplete_value": false,
      "site": "00591e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:c68:8"
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
      "00591e8c",
      "DATA",
      [
        "storage",
        "00bf2c68",
        null,
        "pointer"
      ]
    ],
    [
      "00591ef0",
      "READ",
      [
        "storage",
        "00bf2c78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591e8c",
      "DATA",
      [
        "storage",
        "00bf2cb8",
        null,
        "pointer"
      ]
    ],
    [
      "00591ef0",
      "READ",
      [
        "storage",
        "00bf2cc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591df8.md#insn-00591e74)
- 新版 `00591e74`（命令位置の公開資料なし）

~~~diff
- 00591e74 ["COPY", "tmp:0:8", ["const:c68:8"]]
- 00591e74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00591e74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00591e74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00591e74 ["COPY", "tmp:0:8", ["const:cb8:8"]]
+ 00591e74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00591e74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00591e74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00591e74 bytes 29a13191
+ 00591e74 bytes 29e13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03bc08ac38546730596f60f45f5dc239"></a>

### [`00591fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591fdc.md) → [`00591fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591fdc.md) FUN_00591fdc

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
      "definition_site": "00591fe0",
      "incomplete_value": false,
      "site": "00591fe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591fe0",
      "incomplete_value": false,
      "site": "00591fe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:c68:8"
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
      "00591fe4",
      "DATA",
      [
        "storage",
        "00bf2c68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00591fe4",
      "DATA",
      [
        "storage",
        "00bf2cb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591fdc.md#insn-00591fe0)
- 新版 `00591fe0`（命令位置の公開資料なし）

~~~diff
- 00591fe0 ["COPY", "tmp:0:8", ["const:c68:8"]]
- 00591fe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591fe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591fe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591fe0 ["COPY", "tmp:0:8", ["const:cb8:8"]]
+ 00591fe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591fe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591fe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591fe0 bytes 08a13191
+ 00591fe0 bytes 08e13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7005db7618a8ab87d576583e6d2da1d1"></a>

### [`00591fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591fec.md) → [`00591fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591fec.md) FUN_00591fec

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
      "definition_site": "00591ffc",
      "incomplete_value": false,
      "site": "00592004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591ffc",
      "incomplete_value": false,
      "site": "00592004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:c68:8"
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
      "00592004",
      "DATA",
      [
        "storage",
        "00bf2c68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00592004",
      "DATA",
      [
        "storage",
        "00bf2cb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591fec.md#insn-00591ffc)
- 新版 `00591ffc`（命令位置の公開資料なし）

~~~diff
- 00591ffc ["COPY", "tmp:0:8", ["const:c68:8"]]
- 00591ffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591ffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591ffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591ffc ["COPY", "tmp:0:8", ["const:cb8:8"]]
+ 00591ffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591ffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591ffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591ffc bytes 08a13191
+ 00591ffc bytes 08e13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-834029bd9b0f2318a28912ff9a24bb08"></a>

### [`005920d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005920d4.md) → [`005920d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/005920d4.md) FUN_005920d4

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
      "definition_site": "005920e0",
      "incomplete_value": false,
      "site": "005920e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005920e0",
      "incomplete_value": false,
      "site": "005920e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
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
      "005920e0",
      "DATA",
      [
        "storage",
        "00bf2cc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005920e0",
      "DATA",
      [
        "storage",
        "00bf2d18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005920dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005920d4.md#insn-005920dc)
- 新版 `005920dc`（命令位置の公開資料なし）

~~~diff
- 005920dc ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 005920dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005920dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005920dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005920dc ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 005920dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005920dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005920dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005920dc bytes 29213391
+ 005920dc bytes 29613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fe92dc45dbc6b69bf403c11e31a4703"></a>

### [`00592138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592138.md) → [`00592138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592138.md) FUN_00592138

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
      "definition_site": "0059215c",
      "incomplete_value": false,
      "site": "0059215c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059215c",
      "incomplete_value": false,
      "site": "0059215c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:d48:8"
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
      "0059215c",
      "DATA",
      [
        "storage",
        "00bf2d48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059215c",
      "DATA",
      [
        "storage",
        "00bf2d98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592138.md#insn-00592158)
- 新版 `00592158`（命令位置の公開資料なし）

~~~diff
- 00592158 ["COPY", "tmp:0:8", ["const:d48:8"]]
- 00592158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592158 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 00592158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592158 bytes 08213591
+ 00592158 bytes 08613691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0371774906bba1781197d95d3719ad0"></a>

### [`0059216c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059216c.md) → [`0059216c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/0059216c.md) FUN_0059216c

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
      "definition_site": "00592178",
      "incomplete_value": false,
      "site": "00592178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592178",
      "incomplete_value": false,
      "site": "00592178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:d48:8"
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
      "00592178",
      "DATA",
      [
        "storage",
        "00bf2d48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592178",
      "DATA",
      [
        "storage",
        "00bf2d98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059216c.md#insn-00592174)
- 新版 `00592174`（命令位置の公開資料なし）

~~~diff
- 00592174 ["COPY", "tmp:0:8", ["const:d48:8"]]
- 00592174 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00592174 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00592174 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00592174 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 00592174 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00592174 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00592174 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00592174 bytes 29213591
+ 00592174 bytes 29613691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb62334c2bde41c397c9d05ad5eca5fa"></a>

### [`005921c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005921c0.md) → [`005921c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/005921c0.md) FUN_005921c0

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
      "definition_site": "005921e4",
      "incomplete_value": false,
      "site": "005921e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005921e4",
      "incomplete_value": false,
      "site": "005921e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
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
      "005921e4",
      "DATA",
      [
        "storage",
        "00bf2dd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005921e4",
      "DATA",
      [
        "storage",
        "00bf2e28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005921e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005921c0.md#insn-005921e0)
- 新版 `005921e0`（命令位置の公開資料なし）

~~~diff
- 005921e0 ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 005921e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005921e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005921e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005921e0 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 005921e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005921e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005921e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005921e0 bytes 08613791
+ 005921e0 bytes 08a13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b3d489201044f0af0a65e7fcacbb5d8"></a>

### [`005921f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005921f4.md) → [`005921f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/005921f4.md) FUN_005921f4

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
      "definition_site": "00592200",
      "incomplete_value": false,
      "site": "00592200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592200",
      "incomplete_value": false,
      "site": "00592200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
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
      "00592200",
      "DATA",
      [
        "storage",
        "00bf2dd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592200",
      "DATA",
      [
        "storage",
        "00bf2e28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005921fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005921f4.md#insn-005921fc)
- 新版 `005921fc`（命令位置の公開資料なし）

~~~diff
- 005921fc ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 005921fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005921fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005921fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005921fc ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 005921fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005921fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005921fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005921fc bytes 29613791
+ 005921fc bytes 29a13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dddf80e0404733500036e1e82804324"></a>

### [`00592258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592258.md) → [`00592258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592258.md) FUN_00592258

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
      "definition_site": "0059227c",
      "incomplete_value": false,
      "site": "0059227c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059227c",
      "incomplete_value": false,
      "site": "0059227c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "0059227c",
      "DATA",
      [
        "storage",
        "00bf2e58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059227c",
      "DATA",
      [
        "storage",
        "00bf2ea8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592258.md#insn-00592278)
- 新版 `00592278`（命令位置の公開資料なし）

~~~diff
- 00592278 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 00592278 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592278 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592278 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592278 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 00592278 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592278 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592278 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592278 bytes 08613991
+ 00592278 bytes 08a13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ba4eb213f5fe8667ff4c2cd5fd586c1"></a>

### [`0059228c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059228c.md) → [`0059228c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/0059228c.md) FUN_0059228c

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
      "definition_site": "00592298",
      "incomplete_value": false,
      "site": "00592298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592298",
      "incomplete_value": false,
      "site": "00592298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "00592298",
      "DATA",
      [
        "storage",
        "00bf2e58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592298",
      "DATA",
      [
        "storage",
        "00bf2ea8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059228c.md#insn-00592294)
- 新版 `00592294`（命令位置の公開資料なし）

~~~diff
- 00592294 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 00592294 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00592294 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00592294 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00592294 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 00592294 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00592294 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00592294 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00592294 bytes 29613991
+ 00592294 bytes 29a13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74f523393a6660e17f588d49d7eaa263"></a>

### [`005922a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005922a8.md) → [`005922a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/005922a8.md) FUN_005922a8

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0058c56c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058c/0058c56c.md) [`00590ba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590ba4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0058c56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058c56c.md) [`00590ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590ba4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.36% / 新版 90.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005922f0",
      "incomplete_value": true,
      "site": "00592304",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f34:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005922f0",
      "incomplete_value": true,
      "site": "00592304",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fc1:8"
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
      "definition_site": "005922f0",
      "incomplete_value": true,
      "site": "00592304",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "005922f0",
      "incomplete_value": true,
      "site": "00592304",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005922f8",
      "incomplete_value": true,
      "site": "00592308",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005922f8",
      "incomplete_value": true,
      "site": "00592308",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
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
      "005922f0",
      "READ",
      [
        "storage",
        "00298fc1",
        null,
        null
      ]
    ],
    [
      "005922f0",
      "READ",
      [
        "storage",
        "00298fd1",
        null,
        null
      ]
    ],
    [
      "005922f8",
      "READ",
      [
        "storage",
        "00298fe1",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005922f0",
      "READ",
      [
        "storage",
        "00298f34",
        null,
        null
      ]
    ],
    [
      "005922f0",
      "READ",
      [
        "storage",
        "00298f44",
        null,
        null
      ]
    ],
    [
      "005922f8",
      "READ",
      [
        "storage",
        "00298f54",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005922e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005922a8.md#insn-005922e8) · [`005922ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005922a8.md#insn-005922ec)
- 新版 `005922e8`（命令位置の公開資料なし） · `005922ec`（命令位置の公開資料なし）

~~~diff
- 005922e8 ["COPY", "tmp:0:8", ["const:fc1:8"]]
- 005922e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005922e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005922e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005922e8 ["COPY", "tmp:0:8", ["const:f34:8"]]
+ 005922e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005922e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005922e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005922e8 bytes 08053f91
+ 005922e8 bytes 08d13c91
- 005922ec ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 005922ec bytes e9e8fff0
+ 005922ec ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 005922ec bytes e9e8fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5fc7eaa322e00e07055d7cee926f024"></a>

### [`00592478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592478.md) → [`00592478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592478.md) FUN_00592478

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
      "definition_site": "0059249c",
      "incomplete_value": false,
      "site": "0059249c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059249c",
      "incomplete_value": false,
      "site": "0059249c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
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
      "0059249c",
      "DATA",
      [
        "storage",
        "00bf2ee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059249c",
      "DATA",
      [
        "storage",
        "00bf2f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592478.md#insn-00592498)
- 新版 `00592498`（命令位置の公開資料なし）

~~~diff
- 00592498 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 00592498 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592498 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592498 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592498 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00592498 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592498 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592498 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592498 bytes 08a13b91
+ 00592498 bytes 08e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86c2124f5bbb6ee6f5cfaab7415ed9db"></a>

### [`005924ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005924ac.md) → [`005924ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/005924ac.md) FUN_005924ac

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
      "definition_site": "005924b8",
      "incomplete_value": false,
      "site": "005924b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005924b8",
      "incomplete_value": false,
      "site": "005924b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
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
      "005924b8",
      "DATA",
      [
        "storage",
        "00bf2ee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005924b8",
      "DATA",
      [
        "storage",
        "00bf2f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005924b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005924ac.md#insn-005924b4)
- 新版 `005924b4`（命令位置の公開資料なし）

~~~diff
- 005924b4 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 005924b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005924b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005924b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005924b4 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 005924b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005924b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005924b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005924b4 bytes 29a13b91
+ 005924b4 bytes 29e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42bed5ac43753c649e353ebced0419e1"></a>

### [`005924c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005924c8.md) → [`005924c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/005924c8.md) FUN_005924c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0059277c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059277c.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0059277c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/0059277c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.46% / 新版 97.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059254c",
      "incomplete_value": false,
      "site": "00592554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059254c",
      "incomplete_value": false,
      "site": "00592554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:f68:8"
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
      "00592554",
      "DATA",
      [
        "storage",
        "00bf2f68",
        null,
        "pointer"
      ]
    ],
    [
      "0059264c",
      "READ",
      [
        "storage",
        "00bf2f78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592554",
      "DATA",
      [
        "storage",
        "00bf2fb8",
        null,
        "pointer"
      ]
    ],
    [
      "0059264c",
      "READ",
      [
        "storage",
        "00bf2fc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059254c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005924c8.md#insn-0059254c) · [`00592550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005924c8.md#insn-00592550)
- 新版 `0059254c`（命令位置の公開資料なし） · `00592550`（命令位置の公開資料なし）

~~~diff
- 0059254c ["COPY", "tmp:0:8", ["const:f68:8"]]
- 0059254c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059254c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059254c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059254c ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 0059254c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059254c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059254c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059254c bytes 08a13d91
+ 0059254c bytes 08e13e91
- 00592550 ["COPY", "register:40b0:8", ["register:4000:8"]]
- 00592550 bytes f60300aa
+ 00592550 ["COPY", "register:40b0:8", ["register:4000:8"]]
+ 00592550 bytes f60300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86713866ffba4a3c68f9333c1307bf10"></a>

### [`0059273c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059273c.md) → [`0059273c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/0059273c.md) FUN_0059273c

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
      "definition_site": "00592740",
      "incomplete_value": false,
      "site": "00592744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592740",
      "incomplete_value": false,
      "site": "00592744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:f68:8"
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
      "00592744",
      "DATA",
      [
        "storage",
        "00bf2f68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00592744",
      "DATA",
      [
        "storage",
        "00bf2fb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059273c.md#insn-00592740)
- 新版 `00592740`（命令位置の公開資料なし）

~~~diff
- 00592740 ["COPY", "tmp:0:8", ["const:f68:8"]]
- 00592740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592740 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 00592740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592740 bytes 08a13d91
+ 00592740 bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-317541a26bb073b3975307b29d7ff8ec"></a>

### [`0059274c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059274c.md) → [`0059274c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/0059274c.md) FUN_0059274c

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
      "definition_site": "0059275c",
      "incomplete_value": false,
      "site": "00592764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059275c",
      "incomplete_value": false,
      "site": "00592764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:f68:8"
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
      "00592764",
      "DATA",
      [
        "storage",
        "00bf2f68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00592764",
      "DATA",
      [
        "storage",
        "00bf2fb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059275c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059274c.md#insn-0059275c)
- 新版 `0059275c`（命令位置の公開資料なし）

~~~diff
- 0059275c ["COPY", "tmp:0:8", ["const:f68:8"]]
- 0059275c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059275c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059275c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059275c ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 0059275c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059275c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059275c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059275c bytes 08a13d91
+ 0059275c bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-507698dea3e4da7fa23886273599da7a"></a>

### [`0059280c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059280c.md) → [`0059280c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/0059280c.md) FUN_0059280c

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
      "definition_site": "00592830",
      "incomplete_value": false,
      "site": "00592830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592830",
      "incomplete_value": false,
      "site": "00592830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
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
      "00592830",
      "DATA",
      [
        "storage",
        "00bf2fc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592830",
      "DATA",
      [
        "storage",
        "00bf3018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059280c.md#insn-00592828) · [`0059282c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059280c.md#insn-0059282c)
- 新版 `00592828`（命令位置の公開資料なし） · `0059282c`（命令位置の公開資料なし）

~~~diff
- 00592828 ["COPY", "register:4040:8", ["const:bf2000:8"]]
+ 00592828 ["COPY", "register:4040:8", ["const:bf3000:8"]]
- 00592828 bytes 08330090
+ 00592828 bytes 083300b0
- 0059282c ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 0059282c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059282c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059282c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059282c ["COPY", "tmp:0:8", ["const:18:8"]]
+ 0059282c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059282c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059282c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059282c bytes 08213f91
+ 0059282c bytes 08610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f23ef2df01ee3c2240d55dd726cf3e63"></a>

### [`00592840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592840.md) → [`00592840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592840.md) FUN_00592840

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
      "definition_site": "0059284c",
      "incomplete_value": false,
      "site": "0059284c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059284c",
      "incomplete_value": false,
      "site": "0059284c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
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
      "0059284c",
      "DATA",
      [
        "storage",
        "00bf2fc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059284c",
      "DATA",
      [
        "storage",
        "00bf3018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592840.md#insn-00592844) · [`00592848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592840.md#insn-00592848)
- 新版 `00592844`（命令位置の公開資料なし） · `00592848`（命令位置の公開資料なし）

~~~diff
- 00592844 ["COPY", "register:4048:8", ["const:bf2000:8"]]
+ 00592844 ["COPY", "register:4048:8", ["const:bf3000:8"]]
- 00592844 bytes 09330090
+ 00592844 bytes 093300b0
- 00592848 ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 00592848 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00592848 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00592848 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00592848 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 00592848 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00592848 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00592848 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00592848 bytes 29213f91
+ 00592848 bytes 29610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d4a75e9d69668d80b633e5ad9a0f961"></a>

### [`00592958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592958.md) → [`00592958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592958.md) FUN_00592958

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
      "definition_site": "0059297c",
      "incomplete_value": false,
      "site": "0059297c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059297c",
      "incomplete_value": false,
      "site": "0059297c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:48:8"
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
      "0059297c",
      "DATA",
      [
        "storage",
        "00bf3048",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059297c",
      "DATA",
      [
        "storage",
        "00bf3098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592958.md#insn-00592978)
- 新版 `00592978`（命令位置の公開資料なし）

~~~diff
- 00592978 ["COPY", "tmp:0:8", ["const:48:8"]]
- 00592978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592978 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 00592978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592978 bytes 08210191
+ 00592978 bytes 08610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df0f7a123d9e032247047b27b09a8cde"></a>

### [`0059298c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059298c.md) → [`0059298c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/0059298c.md) FUN_0059298c

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
      "definition_site": "00592998",
      "incomplete_value": false,
      "site": "00592998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592998",
      "incomplete_value": false,
      "site": "00592998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:48:8"
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
      "00592998",
      "DATA",
      [
        "storage",
        "00bf3048",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592998",
      "DATA",
      [
        "storage",
        "00bf3098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059298c.md#insn-00592994)
- 新版 `00592994`（命令位置の公開資料なし）

~~~diff
- 00592994 ["COPY", "tmp:0:8", ["const:48:8"]]
- 00592994 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00592994 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00592994 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00592994 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 00592994 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00592994 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00592994 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00592994 bytes 29210191
+ 00592994 bytes 29610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3703031f5ebe7943562e0f1e34308c2d"></a>

### [`00592a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592a84.md) → [`00592a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592a84.md) FUN_00592a84

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
      "definition_site": "00592aa8",
      "incomplete_value": false,
      "site": "00592aa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592aa8",
      "incomplete_value": false,
      "site": "00592aa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:c8:8"
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
      "00592aa8",
      "DATA",
      [
        "storage",
        "00bf30c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592aa8",
      "DATA",
      [
        "storage",
        "00bf3118",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592a84.md#insn-00592aa4)
- 新版 `00592aa4`（命令位置の公開資料なし）

~~~diff
- 00592aa4 ["COPY", "tmp:0:8", ["const:c8:8"]]
- 00592aa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592aa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592aa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592aa4 ["COPY", "tmp:0:8", ["const:118:8"]]
+ 00592aa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592aa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592aa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592aa4 bytes 08210391
+ 00592aa4 bytes 08610491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-812db3c714c33d46cc64957f0cf3f060"></a>

### [`00592ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ab8.md) → [`00592ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592ab8.md) FUN_00592ab8

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
      "definition_site": "00592ac4",
      "incomplete_value": false,
      "site": "00592ac4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592ac4",
      "incomplete_value": false,
      "site": "00592ac4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:c8:8"
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
      "00592ac4",
      "DATA",
      [
        "storage",
        "00bf30c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592ac4",
      "DATA",
      [
        "storage",
        "00bf3118",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ab8.md#insn-00592ac0)
- 新版 `00592ac0`（命令位置の公開資料なし）

~~~diff
- 00592ac0 ["COPY", "tmp:0:8", ["const:c8:8"]]
- 00592ac0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00592ac0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00592ac0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00592ac0 ["COPY", "tmp:0:8", ["const:118:8"]]
+ 00592ac0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00592ac0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00592ac0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00592ac0 bytes 29210391
+ 00592ac0 bytes 29610491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5864b9f642ca014879223ee53b43b026"></a>

### [`00592b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592b14.md) → [`00592b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592b14.md) FUN_00592b14

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0058f504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f504.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`0058f504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058f/0058f504.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592ccc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592b4c",
      "incomplete_value": false,
      "site": "00592b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592b4c",
      "incomplete_value": false,
      "site": "00592b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
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
      "00592b54",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00592c0c",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592b54",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "pointer"
      ]
    ],
    [
      "00592c0c",
      "READ",
      [
        "storage",
        "00bf31a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592b14.md#insn-00592b4c) · [`00592b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592b14.md#insn-00592b50)
- 新版 `00592b4c`（命令位置の公開資料なし） · `00592b50`（命令位置の公開資料なし）

~~~diff
- 00592b4c ["COPY", "tmp:0:8", ["const:148:8"]]
- 00592b4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592b4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592b4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592b4c ["COPY", "tmp:0:8", ["const:198:8"]]
+ 00592b4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592b4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592b4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592b4c bytes 08210591
+ 00592b4c bytes 08610691
- 00592b50 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00592b50 bytes f30300aa
+ 00592b50 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00592b50 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58497c78278c204b754632c846877792"></a>

### [`00592c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592c8c.md) → [`00592c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592c8c.md) FUN_00592c8c

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
      "definition_site": "00592c90",
      "incomplete_value": false,
      "site": "00592c94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592c90",
      "incomplete_value": false,
      "site": "00592c94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
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
      "00592c94",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00592c94",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592c8c.md#insn-00592c90)
- 新版 `00592c90`（命令位置の公開資料なし）

~~~diff
- 00592c90 ["COPY", "tmp:0:8", ["const:148:8"]]
- 00592c90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592c90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592c90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592c90 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 00592c90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592c90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592c90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592c90 bytes 08210591
+ 00592c90 bytes 08610691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dd60d5edbbfea3b192a5858fed1514a"></a>

### [`00592c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592c9c.md) → [`00592c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592c9c.md) FUN_00592c9c

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
      "definition_site": "00592cac",
      "incomplete_value": false,
      "site": "00592cb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592cac",
      "incomplete_value": false,
      "site": "00592cb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
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
      "00592cb4",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00592cb4",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592cac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592c9c.md#insn-00592cac)
- 新版 `00592cac`（命令位置の公開資料なし）

~~~diff
- 00592cac ["COPY", "tmp:0:8", ["const:148:8"]]
- 00592cac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592cac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592cac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592cac ["COPY", "tmp:0:8", ["const:198:8"]]
+ 00592cac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592cac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592cac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592cac bytes 08210591
+ 00592cac bytes 08610691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82e44423beb23c59ac8e2ca258dd498c"></a>

### [`00592cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592cdc.md) → [`00592cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592cdc.md) FUN_00592cdc

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
      "definition_site": "00592ce8",
      "incomplete_value": false,
      "site": "00592cf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592ce8",
      "incomplete_value": false,
      "site": "00592cf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:198:8"
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
      "00592cf4",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592cf4",
      "DATA",
      [
        "storage",
        "00bf31e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592cdc.md#insn-00592ce8)
- 新版 `00592ce8`（命令位置の公開資料なし）

~~~diff
- 00592ce8 ["COPY", "tmp:0:8", ["const:198:8"]]
- 00592ce8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00592ce8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00592ce8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00592ce8 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 00592ce8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00592ce8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00592ce8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00592ce8 bytes 4a610691
+ 00592ce8 bytes 4aa10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-237ce26ab8b36e1e955b1cf64a874aac"></a>

### [`00592d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592d20.md) → [`00592d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592d20.md) FUN_00592d20

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00592d38",
      "incomplete_value": true,
      "site": "00592d44",
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
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592d38",
      "incomplete_value": true,
      "site": "00592d44",
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
            "const:198:8"
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
      "00592d44",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592d44",
      "DATA",
      [
        "storage",
        "00bf31e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592d20.md#insn-00592d38)
- 新版 `00592d38`（命令位置の公開資料なし）

~~~diff
- 00592d38 ["COPY", "tmp:0:8", ["const:198:8"]]
- 00592d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592d38 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 00592d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592d38 bytes 08610691
+ 00592d38 bytes 08a10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39dbc841557d1578ec3e73813414e08e"></a>

### [`00592d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592d7c.md) → [`00592d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592d7c.md) FUN_00592d7c

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
      "definition_site": "00592da8",
      "incomplete_value": false,
      "site": "00592da8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592da8",
      "incomplete_value": false,
      "site": "00592da8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:198:8"
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
      "00592da8",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592da8",
      "DATA",
      [
        "storage",
        "00bf31e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592d7c.md#insn-00592da0)
- 新版 `00592da0`（命令位置の公開資料なし）

~~~diff
- 00592da0 ["COPY", "tmp:0:8", ["const:198:8"]]
- 00592da0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592da0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592da0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592da0 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 00592da0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592da0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592da0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592da0 bytes 08610691
+ 00592da0 bytes 08a10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-863d0d912afb09e215bb8aeb4d153633"></a>

### [`00592e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592e04.md) → [`00592e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592e04.md) FUN_00592e04

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
      "definition_site": "00592e20",
      "incomplete_value": false,
      "site": "00592e20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592e20",
      "incomplete_value": false,
      "site": "00592e20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:198:8"
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
      "00592e20",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592e20",
      "DATA",
      [
        "storage",
        "00bf31e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592e04.md#insn-00592e1c)
- 新版 `00592e1c`（命令位置の公開資料なし）

~~~diff
- 00592e1c ["COPY", "tmp:0:8", ["const:198:8"]]
- 00592e1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00592e1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00592e1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00592e1c ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 00592e1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00592e1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00592e1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00592e1c bytes 29610691
+ 00592e1c bytes 29a10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c495ce576ccd5a12d5e134916299960b"></a>

### [`005930c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/005930c4.md) → [`005930c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/005930c4.md) FUN_005930c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0058d7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058d/0058d7b4.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`0058d7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058d/0058d7b4.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00593104",
      "incomplete_value": false,
      "site": "00593108",
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
      "definition_site": "00593104",
      "incomplete_value": false,
      "site": "00593108",
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
      "00593108",
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
      "00593108",
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

- 旧版 [`005930fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/005930c4.md#insn-005930fc)
- 新版 `005930fc`（命令位置の公開資料なし）

~~~diff
- 005930fc ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005930fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005930fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005930fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005930fc ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 005930fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005930fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005930fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005930fc bytes 08012891
+ 005930fc bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2965c673c2fc1c0ea31d602edabf685"></a>

### [`0059313c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/0059313c.md) → [`0059313c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/0059313c.md) FUN_0059313c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0058d7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058d/0058d7b4.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`0058d7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058d/0058d7b4.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592ccc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00593174",
      "incomplete_value": false,
      "site": "0059317c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593174",
      "incomplete_value": false,
      "site": "0059317c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
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
      "0059317c",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00593234",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059317c",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "pointer"
      ]
    ],
    [
      "00593234",
      "READ",
      [
        "storage",
        "00bf31a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/0059313c.md#insn-00593174) · [`00593178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/0059313c.md#insn-00593178)
- 新版 `00593174`（命令位置の公開資料なし） · `00593178`（命令位置の公開資料なし）

~~~diff
- 00593174 ["COPY", "tmp:0:8", ["const:148:8"]]
- 00593174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00593174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00593174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593174 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 00593174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00593174 bytes 08210591
+ 00593174 bytes 08610691
- 00593178 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00593178 bytes f30300aa
+ 00593178 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00593178 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-317ce67bb8f7a8d310cb81f54a2754ee"></a>

### [`005932b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/005932b4.md) → [`005932b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/005932b4.md) FUN_005932b4

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
      "definition_site": "005932c0",
      "incomplete_value": false,
      "site": "005932cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005932c0",
      "incomplete_value": false,
      "site": "005932cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
      "005932cc",
      "DATA",
      [
        "storage",
        "00bf3228",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005932cc",
      "DATA",
      [
        "storage",
        "00bf3278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005932c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/005932b4.md#insn-005932c0)
- 新版 `005932c0`（命令位置の公開資料なし）

~~~diff
- 005932c0 ["COPY", "tmp:0:8", ["const:228:8"]]
- 005932c0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005932c0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005932c0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005932c0 ["COPY", "tmp:0:8", ["const:278:8"]]
+ 005932c0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005932c0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005932c0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005932c0 bytes 4aa10891
+ 005932c0 bytes 4ae10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-927dc113f183c739758d2976d2f24647"></a>

### [`00593354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593354.md) → [`00593354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593354.md) FUN_00593354

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
      "definition_site": "00593380",
      "incomplete_value": false,
      "site": "00593380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593380",
      "incomplete_value": false,
      "site": "00593380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
      "00593380",
      "DATA",
      [
        "storage",
        "00bf3228",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593380",
      "DATA",
      [
        "storage",
        "00bf3278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593354.md#insn-00593378)
- 新版 `00593378`（命令位置の公開資料なし）

~~~diff
- 00593378 ["COPY", "tmp:0:8", ["const:228:8"]]
- 00593378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00593378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00593378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593378 ["COPY", "tmp:0:8", ["const:278:8"]]
+ 00593378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00593378 bytes 08a10891
+ 00593378 bytes 08e10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2916230e6c90176b115b22ef69eff6b7"></a>

### [`00593688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593688.md) → [`00593688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593688.md) FUN_00593688

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0058ef88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058ef88.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`0058ef88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058ef88.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592ccc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005936c0",
      "incomplete_value": false,
      "site": "005936c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005936c0",
      "incomplete_value": false,
      "site": "005936c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
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
      "005936c8",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00593780",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005936c8",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "pointer"
      ]
    ],
    [
      "00593780",
      "READ",
      [
        "storage",
        "00bf31a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005936c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593688.md#insn-005936c0) · [`005936c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593688.md#insn-005936c4)
- 新版 `005936c0`（命令位置の公開資料なし） · `005936c4`（命令位置の公開資料なし）

~~~diff
- 005936c0 ["COPY", "tmp:0:8", ["const:148:8"]]
- 005936c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005936c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005936c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005936c0 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 005936c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005936c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005936c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005936c0 bytes 08210591
+ 005936c0 bytes 08610691
- 005936c4 ["COPY", "register:4098:8", ["register:4000:8"]]
- 005936c4 bytes f30300aa
+ 005936c4 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 005936c4 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6729f3dae452d937b2d1b2a0d9e353c"></a>

### [`00593800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593800.md) → [`00593800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593800.md) FUN_00593800

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
      "definition_site": "0059380c",
      "incomplete_value": false,
      "site": "00593818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059380c",
      "incomplete_value": false,
      "site": "00593818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
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
      "00593818",
      "DATA",
      [
        "storage",
        "00bf32a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593818",
      "DATA",
      [
        "storage",
        "00bf32f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059380c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593800.md#insn-0059380c)
- 新版 `0059380c`（命令位置の公開資料なし）

~~~diff
- 0059380c ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 0059380c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059380c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059380c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059380c ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 0059380c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059380c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059380c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059380c bytes 4aa10a91
+ 0059380c bytes 4ae10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20244c8301d616a52f9fc503e4bca727"></a>

### [`00593844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593844.md) → [`00593844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593844.md) FUN_00593844

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
      "definition_site": "0059385c",
      "incomplete_value": false,
      "site": "00593868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059385c",
      "incomplete_value": false,
      "site": "00593868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
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
      "00593868",
      "DATA",
      [
        "storage",
        "00bf32a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593868",
      "DATA",
      [
        "storage",
        "00bf32f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059385c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593844.md#insn-0059385c)
- 新版 `0059385c`（命令位置の公開資料なし）

~~~diff
- 0059385c ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 0059385c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059385c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059385c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059385c ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 0059385c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059385c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059385c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059385c bytes 08a10a91
+ 0059385c bytes 08e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bf57bfdb2d1189ffac02e9555e242af"></a>

### [`005938a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/005938a0.md) → [`005938a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/005938a0.md) FUN_005938a0

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
      "definition_site": "005938cc",
      "incomplete_value": false,
      "site": "005938cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005938cc",
      "incomplete_value": false,
      "site": "005938cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
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
      "005938cc",
      "DATA",
      [
        "storage",
        "00bf32a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005938cc",
      "DATA",
      [
        "storage",
        "00bf32f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005938c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/005938a0.md#insn-005938c4)
- 新版 `005938c4`（命令位置の公開資料なし）

~~~diff
- 005938c4 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 005938c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005938c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005938c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005938c4 ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 005938c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005938c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005938c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005938c4 bytes 08a10a91
+ 005938c4 bytes 08e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb9c491ccbdf9b8dcbb18f8097f68ec4"></a>

### [`00593928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593928.md) → [`00593928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593928.md) FUN_00593928

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
      "definition_site": "00593944",
      "incomplete_value": false,
      "site": "00593944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593944",
      "incomplete_value": false,
      "site": "00593944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
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
      "00593944",
      "DATA",
      [
        "storage",
        "00bf32a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593944",
      "DATA",
      [
        "storage",
        "00bf32f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593928.md#insn-00593940)
- 新版 `00593940`（命令位置の公開資料なし）

~~~diff
- 00593940 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 00593940 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00593940 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00593940 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00593940 ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 00593940 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00593940 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00593940 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00593940 bytes 29a10a91
+ 00593940 bytes 29e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0276d6d5826ee2f3c7c50d54914f62ef"></a>

### [`00593a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593a6c.md) → [`00593a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593a6c.md) FUN_00593a6c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0058e0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058e0ec.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`0058e0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058e0ec.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592ccc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00593aa4",
      "incomplete_value": false,
      "site": "00593aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593aa4",
      "incomplete_value": false,
      "site": "00593aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
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
      "00593aac",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00593b64",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593aac",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "pointer"
      ]
    ],
    [
      "00593b64",
      "READ",
      [
        "storage",
        "00bf31a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593a6c.md#insn-00593aa4) · [`00593aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593a6c.md#insn-00593aa8)
- 新版 `00593aa4`（命令位置の公開資料なし） · `00593aa8`（命令位置の公開資料なし）

~~~diff
- 00593aa4 ["COPY", "tmp:0:8", ["const:148:8"]]
- 00593aa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00593aa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00593aa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593aa4 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 00593aa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593aa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593aa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00593aa4 bytes 08210591
+ 00593aa4 bytes 08610691
- 00593aa8 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00593aa8 bytes f30300aa
+ 00593aa8 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00593aa8 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-256c636178a7157211a733d120bd0bba"></a>

### [`00593be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593be4.md) → [`00593be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593be4.md) FUN_00593be4

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
      "definition_site": "00593bf0",
      "incomplete_value": false,
      "site": "00593bfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593bf0",
      "incomplete_value": false,
      "site": "00593bfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "00593bfc",
      "DATA",
      [
        "storage",
        "00bf3328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593bfc",
      "DATA",
      [
        "storage",
        "00bf3378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593be4.md#insn-00593bf0)
- 新版 `00593bf0`（命令位置の公開資料なし）

~~~diff
- 00593bf0 ["COPY", "tmp:0:8", ["const:328:8"]]
- 00593bf0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00593bf0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00593bf0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00593bf0 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 00593bf0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00593bf0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00593bf0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00593bf0 bytes 4aa10c91
+ 00593bf0 bytes 4ae10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3739656a602f324449c34a462c44f28"></a>

### [`00593c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593c28.md) → [`00593c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593c28.md) FUN_00593c28

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
      "definition_site": "00593c40",
      "incomplete_value": false,
      "site": "00593c4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593c40",
      "incomplete_value": false,
      "site": "00593c4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "00593c4c",
      "DATA",
      [
        "storage",
        "00bf3328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593c4c",
      "DATA",
      [
        "storage",
        "00bf3378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593c28.md#insn-00593c40)
- 新版 `00593c40`（命令位置の公開資料なし）

~~~diff
- 00593c40 ["COPY", "tmp:0:8", ["const:328:8"]]
- 00593c40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00593c40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00593c40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593c40 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 00593c40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593c40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593c40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00593c40 bytes 08a10c91
+ 00593c40 bytes 08e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5bf33a668e699ab35d1723d55ce5365"></a>

### [`00593c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593c84.md) → [`00593c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593c84.md) FUN_00593c84

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
      "definition_site": "00593cb0",
      "incomplete_value": false,
      "site": "00593cb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593cb0",
      "incomplete_value": false,
      "site": "00593cb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "00593cb0",
      "DATA",
      [
        "storage",
        "00bf3328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593cb0",
      "DATA",
      [
        "storage",
        "00bf3378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593c84.md#insn-00593ca8)
- 新版 `00593ca8`（命令位置の公開資料なし）

~~~diff
- 00593ca8 ["COPY", "tmp:0:8", ["const:328:8"]]
- 00593ca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00593ca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00593ca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593ca8 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 00593ca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593ca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593ca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00593ca8 bytes 08a10c91
+ 00593ca8 bytes 08e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ddaa9cd6fae7c785bbe483053d0a854"></a>

### [`00593d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593d0c.md) → [`00593d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593d0c.md) FUN_00593d0c

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
      "definition_site": "00593d28",
      "incomplete_value": false,
      "site": "00593d28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593d28",
      "incomplete_value": false,
      "site": "00593d28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "00593d28",
      "DATA",
      [
        "storage",
        "00bf3328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593d28",
      "DATA",
      [
        "storage",
        "00bf3378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593d0c.md#insn-00593d24)
- 新版 `00593d24`（命令位置の公開資料なし）

~~~diff
- 00593d24 ["COPY", "tmp:0:8", ["const:328:8"]]
- 00593d24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00593d24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00593d24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00593d24 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 00593d24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00593d24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00593d24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00593d24 bytes 29a10c91
+ 00593d24 bytes 29e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-925316c747c24a344f2841f430fea123"></a>

### [`00593e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593e50.md) → [`00593e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593e50.md) FUN_00593e50

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0058f9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f9b0.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`0058f9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058f/0058f9b0.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592ccc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00593e88",
      "incomplete_value": false,
      "site": "00593e90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593e88",
      "incomplete_value": false,
      "site": "00593e90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
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
      "00593e90",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00593f48",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593e90",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "pointer"
      ]
    ],
    [
      "00593f48",
      "READ",
      [
        "storage",
        "00bf31a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593e50.md#insn-00593e88) · [`00593e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593e50.md#insn-00593e8c)
- 新版 `00593e88`（命令位置の公開資料なし） · `00593e8c`（命令位置の公開資料なし）

~~~diff
- 00593e88 ["COPY", "tmp:0:8", ["const:148:8"]]
- 00593e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00593e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00593e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593e88 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 00593e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00593e88 bytes 08210591
+ 00593e88 bytes 08610691
- 00593e8c ["COPY", "register:4098:8", ["register:4000:8"]]
- 00593e8c bytes f30300aa
+ 00593e8c ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00593e8c bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90e52947611418dc5d2bba9abd02896b"></a>

### [`00593fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593fc8.md) → [`00593fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593fc8.md) FUN_00593fc8

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
      "definition_site": "00593fd4",
      "incomplete_value": false,
      "site": "00593fe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593fd4",
      "incomplete_value": false,
      "site": "00593fe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
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
      "00593fe0",
      "DATA",
      [
        "storage",
        "00bf33a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593fe0",
      "DATA",
      [
        "storage",
        "00bf33f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593fc8.md#insn-00593fd4)
- 新版 `00593fd4`（命令位置の公開資料なし）

~~~diff
- 00593fd4 ["COPY", "tmp:0:8", ["const:3a8:8"]]
- 00593fd4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00593fd4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00593fd4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00593fd4 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 00593fd4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00593fd4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00593fd4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00593fd4 bytes 4aa10e91
+ 00593fd4 bytes 4ae10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d2b7abee84d68f004684a57743b264b"></a>

### [`0059400c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/0059400c.md) → [`0059400c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/0059400c.md) FUN_0059400c

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
      "definition_site": "00594024",
      "incomplete_value": false,
      "site": "00594030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594024",
      "incomplete_value": false,
      "site": "00594030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
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
      "00594030",
      "DATA",
      [
        "storage",
        "00bf33a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594030",
      "DATA",
      [
        "storage",
        "00bf33f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/0059400c.md#insn-00594024)
- 新版 `00594024`（命令位置の公開資料なし）

~~~diff
- 00594024 ["COPY", "tmp:0:8", ["const:3a8:8"]]
- 00594024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00594024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00594024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00594024 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 00594024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00594024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00594024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00594024 bytes 08a10e91
+ 00594024 bytes 08e10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9a2b310c9c38e3c5f825881b3bf895f"></a>

### [`00594068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594068.md) → [`00594068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594068.md) FUN_00594068

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
      "definition_site": "00594094",
      "incomplete_value": false,
      "site": "00594094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594094",
      "incomplete_value": false,
      "site": "00594094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
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
      "00594094",
      "DATA",
      [
        "storage",
        "00bf33a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594094",
      "DATA",
      [
        "storage",
        "00bf33f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059408c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594068.md#insn-0059408c)
- 新版 `0059408c`（命令位置の公開資料なし）

~~~diff
- 0059408c ["COPY", "tmp:0:8", ["const:3a8:8"]]
- 0059408c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059408c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059408c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059408c ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 0059408c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059408c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059408c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059408c bytes 08a10e91
+ 0059408c bytes 08e10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3282936fec453d0c74a02d86a0f6bae"></a>

### [`005940f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/005940f0.md) → [`005940f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/005940f0.md) FUN_005940f0

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
      "definition_site": "0059410c",
      "incomplete_value": false,
      "site": "0059410c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059410c",
      "incomplete_value": false,
      "site": "0059410c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
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
      "0059410c",
      "DATA",
      [
        "storage",
        "00bf33a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059410c",
      "DATA",
      [
        "storage",
        "00bf33f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/005940f0.md#insn-00594108)
- 新版 `00594108`（命令位置の公開資料なし）

~~~diff
- 00594108 ["COPY", "tmp:0:8", ["const:3a8:8"]]
- 00594108 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00594108 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00594108 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00594108 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 00594108 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00594108 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00594108 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00594108 bytes 29a10e91
+ 00594108 bytes 29e10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfdd8280a0f1819de4ddfc6b3bca9e28"></a>

### [`005943f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/005943f4.md) → [`005943f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/005943f4.md) FUN_005943f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0058ff20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058ff20.md) · 呼出先 7件 [`00588310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00588/00588310.md) [`005945ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/005945ac.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`0058ff20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058f/0058ff20.md) · 呼出先 7件 [`00588310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588310.md) [`005945ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/005945ac.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059442c",
      "incomplete_value": false,
      "site": "00594434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059442c",
      "incomplete_value": false,
      "site": "00594434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:428:8"
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
      "00594434",
      "DATA",
      [
        "storage",
        "00bf3428",
        null,
        "pointer"
      ]
    ],
    [
      "005944ec",
      "READ",
      [
        "storage",
        "00bf3438",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594434",
      "DATA",
      [
        "storage",
        "00bf3478",
        null,
        "pointer"
      ]
    ],
    [
      "005944ec",
      "READ",
      [
        "storage",
        "00bf3488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059442c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/005943f4.md#insn-0059442c) · [`00594430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/005943f4.md#insn-00594430)
- 新版 `0059442c`（命令位置の公開資料なし） · `00594430`（命令位置の公開資料なし）

~~~diff
- 0059442c ["COPY", "tmp:0:8", ["const:428:8"]]
- 0059442c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059442c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059442c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059442c ["COPY", "tmp:0:8", ["const:478:8"]]
+ 0059442c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059442c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059442c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059442c bytes 08a11091
+ 0059442c bytes 08e11191
- 00594430 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00594430 bytes f30300aa
+ 00594430 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00594430 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfdf984663aaa05cb604a5ed02192e49"></a>

### [`0059457c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/0059457c.md) → [`0059457c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/0059457c.md) FUN_0059457c

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
      "definition_site": "0059458c",
      "incomplete_value": false,
      "site": "00594594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059458c",
      "incomplete_value": false,
      "site": "00594594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:428:8"
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
      "00594594",
      "DATA",
      [
        "storage",
        "00bf3428",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00594594",
      "DATA",
      [
        "storage",
        "00bf3478",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059458c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/0059457c.md#insn-0059458c)
- 新版 `0059458c`（命令位置の公開資料なし）

~~~diff
- 0059458c ["COPY", "tmp:0:8", ["const:428:8"]]
- 0059458c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059458c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059458c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059458c ["COPY", "tmp:0:8", ["const:478:8"]]
+ 0059458c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059458c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059458c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059458c bytes 08a11091
+ 0059458c bytes 08e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba08f1cd8776c1594807ca06c1bbb768"></a>

### [`0059465c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/0059465c.md) → [`0059465c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/0059465c.md) FUN_0059465c

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
      "definition_site": "00594688",
      "incomplete_value": false,
      "site": "00594688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594688",
      "incomplete_value": false,
      "site": "00594688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "00594688",
      "DATA",
      [
        "storage",
        "00bf3478",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594688",
      "DATA",
      [
        "storage",
        "00bf34c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/0059465c.md#insn-00594680)
- 新版 `00594680`（命令位置の公開資料なし）

~~~diff
- 00594680 ["COPY", "tmp:0:8", ["const:478:8"]]
- 00594680 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00594680 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00594680 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00594680 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 00594680 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00594680 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00594680 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00594680 bytes 08e11191
+ 00594680 bytes 08211391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d50bdf1daf83cf7bc4f51e200ef6ca1"></a>

### [`005946e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/005946e4.md) → [`005946e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/005946e4.md) FUN_005946e4

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
      "definition_site": "00594700",
      "incomplete_value": false,
      "site": "00594700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594700",
      "incomplete_value": false,
      "site": "00594700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "00594700",
      "DATA",
      [
        "storage",
        "00bf3478",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594700",
      "DATA",
      [
        "storage",
        "00bf34c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005946fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/005946e4.md#insn-005946fc)
- 新版 `005946fc`（命令位置の公開資料なし）

~~~diff
- 005946fc ["COPY", "tmp:0:8", ["const:478:8"]]
- 005946fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005946fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005946fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005946fc ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 005946fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005946fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005946fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005946fc bytes 29e11191
+ 005946fc bytes 29211391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-501b903a989567b50c023f94c9160216"></a>

### [`00594944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594944.md) → [`00594944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594944.md) FUN_00594944

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00590428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590428.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`00590428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590428.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592ccc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059497c",
      "incomplete_value": false,
      "site": "00594984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059497c",
      "incomplete_value": false,
      "site": "00594984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
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
      "00594984",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00594a3c",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594984",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "pointer"
      ]
    ],
    [
      "00594a3c",
      "READ",
      [
        "storage",
        "00bf31a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059497c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594944.md#insn-0059497c) · [`00594980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594944.md#insn-00594980)
- 新版 `0059497c`（命令位置の公開資料なし） · `00594980`（命令位置の公開資料なし）

~~~diff
- 0059497c ["COPY", "tmp:0:8", ["const:148:8"]]
- 0059497c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059497c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059497c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059497c ["COPY", "tmp:0:8", ["const:198:8"]]
+ 0059497c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059497c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059497c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059497c bytes 08210591
+ 0059497c bytes 08610691
- 00594980 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00594980 bytes f30300aa
+ 00594980 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00594980 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96957e1e6de7bb9a00d5b9bcf96a2206"></a>

### [`00594abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594abc.md) → [`00594abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594abc.md) FUN_00594abc

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
      "definition_site": "00594ac8",
      "incomplete_value": false,
      "site": "00594ad4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594ac8",
      "incomplete_value": false,
      "site": "00594ad4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
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
      "00594ad4",
      "DATA",
      [
        "storage",
        "00bf34f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594ad4",
      "DATA",
      [
        "storage",
        "00bf3548",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594abc.md#insn-00594ac8)
- 新版 `00594ac8`（命令位置の公開資料なし）

~~~diff
- 00594ac8 ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 00594ac8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00594ac8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00594ac8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00594ac8 ["COPY", "tmp:0:8", ["const:548:8"]]
+ 00594ac8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00594ac8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00594ac8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00594ac8 bytes 4ae11391
+ 00594ac8 bytes 4a211591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d276eb8ceac54f4d398f9972ae327a5"></a>

### [`00594b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594b00.md) → [`00594b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594b00.md) FUN_00594b00

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
      "definition_site": "00594b18",
      "incomplete_value": false,
      "site": "00594b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594b18",
      "incomplete_value": false,
      "site": "00594b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
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
      "00594b24",
      "DATA",
      [
        "storage",
        "00bf34f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594b24",
      "DATA",
      [
        "storage",
        "00bf3548",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594b00.md#insn-00594b18)
- 新版 `00594b18`（命令位置の公開資料なし）

~~~diff
- 00594b18 ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 00594b18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00594b18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00594b18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00594b18 ["COPY", "tmp:0:8", ["const:548:8"]]
+ 00594b18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00594b18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00594b18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00594b18 bytes 08e11391
+ 00594b18 bytes 08211591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-276d135db6bc3bb7d278dadebc4883dd"></a>

### [`00594b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594b5c.md) → [`00594b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594b5c.md) FUN_00594b5c

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
      "definition_site": "00594b88",
      "incomplete_value": false,
      "site": "00594b88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594b88",
      "incomplete_value": false,
      "site": "00594b88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
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
      "00594b88",
      "DATA",
      [
        "storage",
        "00bf34f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594b88",
      "DATA",
      [
        "storage",
        "00bf3548",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594b5c.md#insn-00594b80)
- 新版 `00594b80`（命令位置の公開資料なし）

~~~diff
- 00594b80 ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 00594b80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00594b80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00594b80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00594b80 ["COPY", "tmp:0:8", ["const:548:8"]]
+ 00594b80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00594b80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00594b80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00594b80 bytes 08e11391
+ 00594b80 bytes 08211591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dad1594003b0b4191b8300ae2f108478"></a>

### [`00594be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594be4.md) → [`00594be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594be4.md) FUN_00594be4

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
      "definition_site": "00594c00",
      "incomplete_value": false,
      "site": "00594c00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594c00",
      "incomplete_value": false,
      "site": "00594c00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
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
      "00594c00",
      "DATA",
      [
        "storage",
        "00bf34f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594c00",
      "DATA",
      [
        "storage",
        "00bf3548",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594be4.md#insn-00594bfc)
- 新版 `00594bfc`（命令位置の公開資料なし）

~~~diff
- 00594bfc ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 00594bfc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00594bfc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00594bfc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00594bfc ["COPY", "tmp:0:8", ["const:548:8"]]
+ 00594bfc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00594bfc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00594bfc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00594bfc bytes 29e11391
+ 00594bfc bytes 29211591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e780fb9a05b0537c9cb84347dea245f2"></a>

### [`00594ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594ff8.md) → [`00594ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594ff8.md) _INIT_58

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.22% / 新版 93.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00595220",
      "incomplete_value": false,
      "site": "0059522c",
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
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595220",
      "incomplete_value": false,
      "site": "0059522c",
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
            "const:8f8:8"
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
      "definition_site": "00595228",
      "incomplete_value": false,
      "site": "0059522c",
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
      "definition_site": "00595228",
      "incomplete_value": false,
      "site": "0059522c",
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
      "00595034",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00595058",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00595078",
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
      "00595034",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00595058",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00595078",
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

- 旧版 [`00595024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594ff8.md#insn-00595024) · [`00595030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594ff8.md#insn-00595030) · [`0059504c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594ff8.md#insn-0059504c)
- 新版 `00595024`（命令位置の公開資料なし） · `00595030`（命令位置の公開資料なし） · `0059504c`（命令位置の公開資料なし）

~~~diff
- 00595024 ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 00595024 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00595024 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00595024 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00595024 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 00595024 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00595024 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00595024 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00595024 bytes 73e22391
+ 00595024 bytes 73e22491
- 00595030 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00595030 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00595030 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00595030 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00595030 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00595030 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00595030 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00595030 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00595030 bytes 29750b91
+ 00595030 bytes 29dd0d91
- 0059504c ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 0059504c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059504c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059504c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059504c ["COPY", "tmp:0:8", ["const:38a:8"]]
+ 0059504c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059504c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059504c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059504c bytes 4ac10b91
+ 0059504c bytes 4a290e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f076e3a4fffa157d2772c9173109a7ab"></a>

### [`005954e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00595/005954e4.md) → [`005954e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/005954e4.md) FUN_005954e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00595470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00595/00595470.md) · 呼出先 18件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00595470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/00595470.md) · 呼出先 18件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.65% / 新版 93.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00595534",
      "incomplete_value": false,
      "site": "0059553c",
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
      "definition_site": "00595534",
      "incomplete_value": false,
      "site": "0059553c",
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
      "definition_site": "00595724",
      "incomplete_value": true,
      "site": "00595728",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00595724",
      "incomplete_value": true,
      "site": "00595728",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "definition_site": "00595720",
      "incomplete_value": true,
      "site": "0059572c",
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
      "definition_site": "00595720",
      "incomplete_value": true,
      "site": "0059572c",
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
      "0059553c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00595564",
      "PARAM",
      [
        "storage",
        "00c26930",
        null,
        null
      ]
    ],
    [
      "00595714",
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
      "0059553c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00595564",
      "PARAM",
      [
        "storage",
        "00c26970",
        null,
        null
      ]
    ],
    [
      "00595714",
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

- 旧版 [`00595534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00595/005954e4.md#insn-00595534) · [`00595564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00595/005954e4.md#insn-00595564) · [`00595714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00595/005954e4.md#insn-00595714)
- 新版 `00595534`（命令位置の公開資料なし） · `00595564`（命令位置の公開資料なし） · `00595714`（命令位置の公開資料なし）

~~~diff
- 00595534 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00595534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00595534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00595534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00595534 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00595534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00595534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00595534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00595534 bytes 08a13491
+ 00595534 bytes 08e13591
- 00595564 ["COPY", "tmp:0:8", ["const:930:8"]]
- 00595564 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00595564 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00595564 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00595564 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 00595564 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00595564 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00595564 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00595564 bytes 00c02491
+ 00595564 bytes 00c02591
- 00595714 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 00595714 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00595714 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 00595714 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00595714 bytes 08b946f9
+ 00595714 bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d79039f68d9d41611132d115a08fead3"></a>

### [`005958c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00595/005958c4.md) → [`005958c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/005958c4.md) _INIT_59

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.69% / 新版 84.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 2件, `store_value` 7件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00595900",
      "incomplete_value": true,
      "site": "0059591c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00595900",
      "incomplete_value": true,
      "site": "0059591c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00595924",
      "incomplete_value": true,
      "site": "00595940",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00595924",
      "incomplete_value": true,
      "site": "00595940",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00595944",
      "incomplete_value": true,
      "site": "00595960",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00595944",
      "incomplete_value": true,
      "site": "00595960",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00595900",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00595924",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00595944",
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
      "00595900",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00595924",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00595944",
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

- 旧版 [`005958f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00595/005958c4.md#insn-005958f0) · [`005958f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00595/005958c4.md#insn-005958f8)
- 新版 `005958f0`（命令位置の公開資料なし） · `005958f8`（命令位置の公開資料なし）

~~~diff
- 005958f0 ["COPY", "tmp:0:8", ["const:910:8"]]
- 005958f0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005958f0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005958f0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005958f0 ["COPY", "tmp:0:8", ["const:950:8"]]
+ 005958f0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005958f0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005958f0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005958f0 bytes 73422491
+ 005958f0 bytes 73422591
- 005958f8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 005958f8 bytes 89e8ffd0
+ 005958f8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 005958f8 bytes 89e8ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

