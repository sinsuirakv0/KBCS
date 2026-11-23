# v15.7.3 → v15.7.4 · 最優先の変更候補 (31)

[一覧の目次](README.md)

<a id="compare-511b4b628bc129b0bdbad577728d0644"></a>

### [`006d52bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d52bc.md) → [`006d52bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d52bc.md) FUN_006d52bc

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
      "definition_site": "006d52c0",
      "incomplete_value": false,
      "site": "006d52c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d52c0",
      "incomplete_value": false,
      "site": "006d52c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "006d52c4",
      "DATA",
      [
        "storage",
        "00bf9d20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d52c4",
      "DATA",
      [
        "storage",
        "00bf9d70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d52c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d52bc.md#insn-006d52c0)
- 新版 `006d52c0`（命令位置の公開資料なし）

~~~diff
- 006d52c0 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 006d52c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d52c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d52c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d52c0 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 006d52c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d52c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d52c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d52c0 bytes 08813491
+ 006d52c0 bytes 08c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c0fca7c870aaba492938fbb1e307f85"></a>

### [`006d53b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d53b8.md) → [`006d53b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d53b8.md) FUN_006d53b8

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
      "definition_site": "006d53dc",
      "incomplete_value": false,
      "site": "006d53dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d53dc",
      "incomplete_value": false,
      "site": "006d53dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:da0:8"
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
      "006d53dc",
      "DATA",
      [
        "storage",
        "00bf9da0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d53dc",
      "DATA",
      [
        "storage",
        "00bf9df0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d53d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d53b8.md#insn-006d53d8)
- 新版 `006d53d8`（命令位置の公開資料なし）

~~~diff
- 006d53d8 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 006d53d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d53d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d53d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d53d8 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 006d53d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d53d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d53d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d53d8 bytes 08813691
+ 006d53d8 bytes 08c13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a65d2b2f0d1b100c32e7576ce89abd00"></a>

### [`006d54d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d54d4.md) → [`006d54d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d54d4.md) FUN_006d54d4

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
      "definition_site": "006d54f8",
      "incomplete_value": false,
      "site": "006d54f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d54f8",
      "incomplete_value": false,
      "site": "006d54f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "006d54f8",
      "DATA",
      [
        "storage",
        "00bf9e20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d54f8",
      "DATA",
      [
        "storage",
        "00bf9e70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d54f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d54d4.md#insn-006d54f4)
- 新版 `006d54f4`（命令位置の公開資料なし）

~~~diff
- 006d54f4 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 006d54f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d54f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d54f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d54f4 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 006d54f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d54f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d54f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d54f4 bytes 08813891
+ 006d54f4 bytes 08c13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f86e312e478f643f8118b5aeb7749898"></a>

### [`006d5508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d5508.md) → [`006d5508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5508.md) FUN_006d5508

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
      "definition_site": "006d5514",
      "incomplete_value": false,
      "site": "006d5514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d5514",
      "incomplete_value": false,
      "site": "006d5514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "006d5514",
      "DATA",
      [
        "storage",
        "00bf9e20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d5514",
      "DATA",
      [
        "storage",
        "00bf9e70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d5510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d5508.md#insn-006d5510)
- 新版 `006d5510`（命令位置の公開資料なし）

~~~diff
- 006d5510 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 006d5510 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d5510 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d5510 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d5510 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 006d5510 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d5510 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d5510 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d5510 bytes 29813891
+ 006d5510 bytes 29c13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e73102c55b9d404cb5fc8bf843a17b8"></a>

### [`006d5524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d5524.md) → [`006d5524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5524.md) FUN_006d5524

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00459f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459f50.md) [`0068c09c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068c/0068c09c.md) [`0068c0a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068c/0068c0a8.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00459f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f50.md) [`0068c09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068c/0068c09c.md) [`0068c0a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068c/0068c0a8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.64% / 新版 98.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d56b4",
      "incomplete_value": false,
      "site": "006d56bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d56b4",
      "incomplete_value": false,
      "site": "006d56bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
      "006d56bc",
      "DATA",
      [
        "storage",
        "00bf9e90",
        null,
        "undefined *"
      ]
    ],
    [
      "006d56f4",
      "READ",
      [
        "storage",
        "00bf9eb0",
        null,
        "pointer"
      ]
    ],
    [
      "006d56f4",
      "READ",
      [
        "storage",
        "00bf9eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d56bc",
      "DATA",
      [
        "storage",
        "00bf9ee0",
        null,
        "undefined *"
      ]
    ],
    [
      "006d56f4",
      "READ",
      [
        "storage",
        "00bf9f00",
        null,
        "pointer"
      ]
    ],
    [
      "006d56f4",
      "READ",
      [
        "storage",
        "00bf9f08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d56b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d5524.md#insn-006d56b4)
- 新版 `006d56b4`（命令位置の公開資料なし）

~~~diff
- 006d56b4 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 006d56b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d56b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d56b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d56b4 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 006d56b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d56b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d56b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d56b4 bytes 08413a91
+ 006d56b4 bytes 08813b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78339a193bf5a0a82ce1141711e9988c"></a>

### [`006d5810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d5810.md) → [`006d5810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5810.md) FUN_006d5810

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
      "definition_site": "006d5824",
      "incomplete_value": false,
      "site": "006d5828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d5824",
      "incomplete_value": false,
      "site": "006d5828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
      "006d5828",
      "DATA",
      [
        "storage",
        "00bf9e90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d5828",
      "DATA",
      [
        "storage",
        "00bf9ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d5824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d5810.md#insn-006d5824)
- 新版 `006d5824`（命令位置の公開資料なし）

~~~diff
- 006d5824 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 006d5824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d5824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d5824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d5824 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 006d5824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d5824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d5824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d5824 bytes 08413a91
+ 006d5824 bytes 08813b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32c9fe7a6c71e04bfcc4f3cc70065b53"></a>

### [`006d5834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d5834.md) → [`006d5834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5834.md) FUN_006d5834

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
      "definition_site": "006d5838",
      "incomplete_value": false,
      "site": "006d583c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d5838",
      "incomplete_value": false,
      "site": "006d583c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
      "006d583c",
      "DATA",
      [
        "storage",
        "00bf9e90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d583c",
      "DATA",
      [
        "storage",
        "00bf9ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d5838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d5834.md#insn-006d5838)
- 新版 `006d5838`（命令位置の公開資料なし）

~~~diff
- 006d5838 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 006d5838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d5838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d5838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d5838 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 006d5838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d5838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d5838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d5838 bytes 08413a91
+ 006d5838 bytes 08813b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5488d173dde44f1c774f2a229bb39807"></a>

### [`006d584c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d584c.md) → [`006d584c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d584c.md) FUN_006d584c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 26件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`0045a030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a030.md)
- 新版 呼出元 0件  · 呼出先 26件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`0045a030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a030.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.79% / 新版 94.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006d58e4",
      "incomplete_value": true,
      "site": "006d58f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b96:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d58e4",
      "incomplete_value": true,
      "site": "006d58f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c23:8"
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
      "definition_site": "006d596c",
      "incomplete_value": true,
      "site": "006d5980",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006d596c",
      "incomplete_value": true,
      "site": "006d5980",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d59a0",
      "incomplete_value": false,
      "site": "006d59a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d59a0",
      "incomplete_value": false,
      "site": "006d59a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:f80:8"
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
      "006d58e4",
      "READ",
      [
        "storage",
        "00293c23",
        null,
        "string"
      ]
    ],
    [
      "006d596c",
      "READ",
      [
        "storage",
        "002a8394",
        null,
        "string"
      ]
    ],
    [
      "006d59a0",
      "DATA",
      [
        "storage",
        "00bf9f80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d58e4",
      "READ",
      [
        "storage",
        "00293b96",
        null,
        "string"
      ]
    ],
    [
      "006d596c",
      "READ",
      [
        "storage",
        "002a842e",
        null,
        "string"
      ]
    ],
    [
      "006d59a0",
      "DATA",
      [
        "storage",
        "00bf9fd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d58dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d584c.md#insn-006d58dc) · [`006d5964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d584c.md#insn-006d5964) · [`006d5998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d584c.md#insn-006d5998)
- 新版 `006d58dc`（命令位置の公開資料なし） · `006d5964`（命令位置の公開資料なし） · `006d5998`（命令位置の公開資料なし）

~~~diff
- 006d58dc ["COPY", "tmp:0:8", ["const:c23:8"]]
- 006d58dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d58dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d58dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d58dc ["COPY", "tmp:0:8", ["const:b96:8"]]
+ 006d58dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d58dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d58dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d58dc bytes 298d3091
+ 006d58dc bytes 29592e91
- 006d5964 ["COPY", "tmp:0:8", ["const:394:8"]]
- 006d5964 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d5964 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d5964 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d5964 ["COPY", "tmp:0:8", ["const:42e:8"]]
+ 006d5964 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d5964 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d5964 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d5964 bytes 29510e91
+ 006d5964 bytes 29b91091
- 006d5998 ["COPY", "tmp:0:8", ["const:f80:8"]]
- 006d5998 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d5998 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d5998 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d5998 ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 006d5998 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d5998 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d5998 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d5998 bytes 08013e91
+ 006d5998 bytes 08413f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccc4222bec199a994c0d0d87580c8429"></a>

### [`006d6008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6008.md) → [`006d6008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6008.md) FUN_006d6008

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
      "definition_site": "006d601c",
      "incomplete_value": false,
      "site": "006d6020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d601c",
      "incomplete_value": false,
      "site": "006d6020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:f00:8"
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
      "006d6020",
      "DATA",
      [
        "storage",
        "00bf9f00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d6020",
      "DATA",
      [
        "storage",
        "00bf9f50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d601c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6008.md#insn-006d601c)
- 新版 `006d601c`（命令位置の公開資料なし）

~~~diff
- 006d601c ["COPY", "tmp:0:8", ["const:f00:8"]]
- 006d601c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d601c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d601c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d601c ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 006d601c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d601c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d601c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d601c bytes 08013c91
+ 006d601c bytes 08413d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4252656fb420a88c3edff3bc88b6151a"></a>

### [`006d602c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d602c.md) → [`006d602c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d602c.md) FUN_006d602c

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
      "definition_site": "006d6030",
      "incomplete_value": false,
      "site": "006d6034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d6030",
      "incomplete_value": false,
      "site": "006d6034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:f00:8"
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
      "006d6034",
      "DATA",
      [
        "storage",
        "00bf9f00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d6034",
      "DATA",
      [
        "storage",
        "00bf9f50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d6030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d602c.md#insn-006d6030)
- 新版 `006d6030`（命令位置の公開資料なし）

~~~diff
- 006d6030 ["COPY", "tmp:0:8", ["const:f00:8"]]
- 006d6030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d6030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d6030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d6030 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 006d6030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d6030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d6030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d6030 bytes 08013c91
+ 006d6030 bytes 08413d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93248a8bd4f84947e7b94bf5d784ae70"></a>

### [`006d60b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d60b8.md) → [`006d60b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d60b8.md) FUN_006d60b8

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
      "definition_site": "006d60cc",
      "incomplete_value": false,
      "site": "006d60d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d60cc",
      "incomplete_value": false,
      "site": "006d60d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:f80:8"
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
      "006d60d0",
      "DATA",
      [
        "storage",
        "00bf9f80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d60d0",
      "DATA",
      [
        "storage",
        "00bf9fd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d60cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d60b8.md#insn-006d60cc)
- 新版 `006d60cc`（命令位置の公開資料なし）

~~~diff
- 006d60cc ["COPY", "tmp:0:8", ["const:f80:8"]]
- 006d60cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d60cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d60cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d60cc ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 006d60cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d60cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d60cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d60cc bytes 08013e91
+ 006d60cc bytes 08413f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2148d2600cf3edd76bb602d6583e934b"></a>

### [`006d60dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d60dc.md) → [`006d60dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d60dc.md) FUN_006d60dc

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
      "definition_site": "006d60e0",
      "incomplete_value": false,
      "site": "006d60e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d60e0",
      "incomplete_value": false,
      "site": "006d60e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:f80:8"
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
      "006d60e4",
      "DATA",
      [
        "storage",
        "00bf9f80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d60e4",
      "DATA",
      [
        "storage",
        "00bf9fd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d60e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d60dc.md#insn-006d60e0)
- 新版 `006d60e0`（命令位置の公開資料なし）

~~~diff
- 006d60e0 ["COPY", "tmp:0:8", ["const:f80:8"]]
- 006d60e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d60e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d60e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d60e0 ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 006d60e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d60e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d60e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d60e0 bytes 08013e91
+ 006d60e0 bytes 08413f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73cf339a9cecf1754b811c56a147fb3b"></a>

### [`006d6164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6164.md) → [`006d6164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6164.md) FUN_006d6164

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
      "definition_site": "006d6170",
      "incomplete_value": false,
      "site": "006d6174",
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
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d6170",
      "incomplete_value": false,
      "site": "006d6174",
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
            "const:20:8"
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
      "006d6174",
      "DATA",
      [
        "storage",
        "00bfa020",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d6174",
      "DATA",
      [
        "storage",
        "00bfa070",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d6170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6164.md#insn-006d6170)
- 新版 `006d6170`（命令位置の公開資料なし）

~~~diff
- 006d6170 ["COPY", "tmp:0:8", ["const:20:8"]]
- 006d6170 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d6170 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d6170 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d6170 ["COPY", "tmp:0:8", ["const:70:8"]]
+ 006d6170 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d6170 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d6170 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d6170 bytes 29810091
+ 006d6170 bytes 29c10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed78b03c4d4477cac89e880683197b45"></a>

### [`006d6188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6188.md) → [`006d6188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6188.md) FUN_006d6188

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
      "definition_site": "006d6190",
      "incomplete_value": false,
      "site": "006d6194",
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
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d6190",
      "incomplete_value": false,
      "site": "006d6194",
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
            "const:20:8"
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
      "006d6194",
      "DATA",
      [
        "storage",
        "00bfa020",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d6194",
      "DATA",
      [
        "storage",
        "00bfa070",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d6190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6188.md#insn-006d6190)
- 新版 `006d6190`（命令位置の公開資料なし）

~~~diff
- 006d6190 ["COPY", "tmp:0:8", ["const:20:8"]]
- 006d6190 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d6190 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d6190 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d6190 ["COPY", "tmp:0:8", ["const:70:8"]]
+ 006d6190 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d6190 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d6190 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d6190 bytes 29810091
+ 006d6190 bytes 29c10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dc4dc9564891b4355db54eba7fb3ed8"></a>

### [`006d61c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d61c8.md) → [`006d61c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d61c8.md) FUN_006d61c8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

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
      "definition_site": "006d61f8",
      "incomplete_value": false,
      "site": "006d61f8",
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
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d61f8",
      "incomplete_value": false,
      "site": "006d61f8",
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
            "const:20:8"
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
      "006d61f8",
      "DATA",
      [
        "storage",
        "00bfa020",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d61f8",
      "DATA",
      [
        "storage",
        "00bfa070",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d61ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d61c8.md#insn-006d61ec) · [`006d61f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d61c8.md#insn-006d61f0)
- 新版 `006d61ec`（命令位置の公開資料なし） · `006d61f0`（命令位置の公開資料なし）

~~~diff
- 006d61ec ["COPY", "tmp:0:8", ["const:20:8"]]
- 006d61ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d61ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d61ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d61ec ["COPY", "tmp:0:8", ["const:70:8"]]
+ 006d61ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d61ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d61ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d61ec bytes 08810091
+ 006d61ec bytes 08c10191
- 006d61f0 ["COPY", "register:4098:8", ["register:4000:8"]]
- 006d61f0 bytes f30300aa
+ 006d61f0 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 006d61f0 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb55a9efab33f93659b506d2a569efd5"></a>

### [`006d627c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d627c.md) → [`006d627c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d627c.md) FUN_006d627c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

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
      "definition_site": "006d62a8",
      "incomplete_value": false,
      "site": "006d62a8",
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
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d62a8",
      "incomplete_value": false,
      "site": "006d62a8",
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
            "const:20:8"
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
      "006d62a8",
      "DATA",
      [
        "storage",
        "00bfa020",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d62a8",
      "DATA",
      [
        "storage",
        "00bfa070",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d62a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d627c.md#insn-006d62a0)
- 新版 `006d62a0`（命令位置の公開資料なし）

~~~diff
- 006d62a0 ["COPY", "tmp:0:8", ["const:20:8"]]
- 006d62a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 006d62a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 006d62a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006d62a0 ["COPY", "tmp:0:8", ["const:70:8"]]
+ 006d62a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006d62a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006d62a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 006d62a0 bytes 4a810091
+ 006d62a0 bytes 4ac10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ed094ddf225a689789212dd6b43cf9b"></a>

### [`006d6550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6550.md) → [`006d6550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6550.md) FUN_006d6550

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
      "definition_site": "006d655c",
      "incomplete_value": false,
      "site": "006d6560",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d655c",
      "incomplete_value": false,
      "site": "006d6560",
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
            "const:a0:8"
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
      "006d6560",
      "DATA",
      [
        "storage",
        "00bfa0a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d6560",
      "DATA",
      [
        "storage",
        "00bfa0f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d655c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6550.md#insn-006d655c)
- 新版 `006d655c`（命令位置の公開資料なし）

~~~diff
- 006d655c ["COPY", "tmp:0:8", ["const:a0:8"]]
- 006d655c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d655c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d655c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d655c ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 006d655c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d655c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d655c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d655c bytes 29810291
+ 006d655c bytes 29c10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61d087a25268dde080a0ab417a7ff2be"></a>

### [`006d6574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6574.md) → [`006d6574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6574.md) FUN_006d6574

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
      "definition_site": "006d657c",
      "incomplete_value": false,
      "site": "006d6580",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d657c",
      "incomplete_value": false,
      "site": "006d6580",
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
            "const:a0:8"
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
      "006d6580",
      "DATA",
      [
        "storage",
        "00bfa0a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d6580",
      "DATA",
      [
        "storage",
        "00bfa0f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d657c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6574.md#insn-006d657c)
- 新版 `006d657c`（命令位置の公開資料なし）

~~~diff
- 006d657c ["COPY", "tmp:0:8", ["const:a0:8"]]
- 006d657c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d657c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d657c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d657c ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 006d657c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d657c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d657c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d657c bytes 29810291
+ 006d657c bytes 29c10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc2ee77bb56fb04eec4c8a4ce30df8ee"></a>

### [`006d65b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d65b4.md) → [`006d65b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d65b4.md) FUN_006d65b4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

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
      "definition_site": "006d65e4",
      "incomplete_value": false,
      "site": "006d65e4",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d65e4",
      "incomplete_value": false,
      "site": "006d65e4",
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
            "const:a0:8"
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
      "006d65e4",
      "DATA",
      [
        "storage",
        "00bfa0a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d65e4",
      "DATA",
      [
        "storage",
        "00bfa0f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d65d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d65b4.md#insn-006d65d8) · [`006d65dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d65b4.md#insn-006d65dc)
- 新版 `006d65d8`（命令位置の公開資料なし） · `006d65dc`（命令位置の公開資料なし）

~~~diff
- 006d65d8 ["COPY", "tmp:0:8", ["const:a0:8"]]
- 006d65d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d65d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d65d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d65d8 ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 006d65d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d65d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d65d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d65d8 bytes 08810291
+ 006d65d8 bytes 08c10391
- 006d65dc ["COPY", "register:4098:8", ["register:4000:8"]]
- 006d65dc bytes f30300aa
+ 006d65dc ["COPY", "register:4098:8", ["register:4000:8"]]
+ 006d65dc bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa87e55e75568000e67aa204a56dcd55"></a>

### [`006d6668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6668.md) → [`006d6668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6668.md) FUN_006d6668

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

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
      "definition_site": "006d6694",
      "incomplete_value": false,
      "site": "006d6694",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d6694",
      "incomplete_value": false,
      "site": "006d6694",
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
            "const:a0:8"
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
      "006d6694",
      "DATA",
      [
        "storage",
        "00bfa0a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d6694",
      "DATA",
      [
        "storage",
        "00bfa0f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d668c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6668.md#insn-006d668c)
- 新版 `006d668c`（命令位置の公開資料なし）

~~~diff
- 006d668c ["COPY", "tmp:0:8", ["const:a0:8"]]
- 006d668c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 006d668c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 006d668c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006d668c ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 006d668c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006d668c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006d668c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 006d668c bytes 4a810291
+ 006d668c bytes 4ac10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c77ed0055485613753cb65088b7a047"></a>

### [`006d6750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6750.md) → [`006d6750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6750.md) FUN_006d6750

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 11件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444edc.md) [`00447378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447378.md) [`0053770c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/0053770c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444edc.md) [`00447378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447378.md) [`0053770c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053770c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.70% / 新版 93.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006d67f4",
      "incomplete_value": true,
      "site": "006d67f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "006d67f4",
      "incomplete_value": true,
      "site": "006d67f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006d67e0",
      "incomplete_value": false,
      "site": "006d67f8",
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
      "definition_site": "006d67e0",
      "incomplete_value": false,
      "site": "006d67f8",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006d67ec",
      "incomplete_value": false,
      "site": "006d67f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d67ec",
      "incomplete_value": false,
      "site": "006d67f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "006d67e0",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006d67e4",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006d67ec",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006d67e0",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006d67e4",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006d67ec",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d67e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6750.md#insn-006d67e0) · [`006d67e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6750.md#insn-006d67e4) · [`006d67ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6750.md#insn-006d67ec)
- 新版 `006d67e0`（命令位置の公開資料なし） · `006d67e4`（命令位置の公開資料なし） · `006d67ec`（命令位置の公開資料なし）

~~~diff
- 006d67e0 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 006d67e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006d67e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006d67e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006d67e0 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 006d67e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006d67e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006d67e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006d67e0 bytes 21203991
+ 006d67e0 bytes 21603a91
- 006d67e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006d67e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006d67e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 006d67e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006d67e4 bytes 083d45f9
+ 006d67e4 bytes 085d45f9
- 006d67ec ["COPY", "tmp:0:8", ["const:298:8"]]
- 006d67ec ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006d67ec ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006d67ec ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006d67ec ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 006d67ec ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006d67ec ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006d67ec ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006d67ec bytes 42600a91
+ 006d67ec bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b2bc1d355dea2ccb6b711723947244a"></a>

### [`006d6974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6974.md) → [`006d6974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6974.md) _INIT_108

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
      "definition_site": "006d69b0",
      "incomplete_value": true,
      "site": "006d69cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006d69b0",
      "incomplete_value": true,
      "site": "006d69cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006d69d4",
      "incomplete_value": true,
      "site": "006d69f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006d69d4",
      "incomplete_value": true,
      "site": "006d69f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006d69f4",
      "incomplete_value": true,
      "site": "006d6a10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006d69f4",
      "incomplete_value": true,
      "site": "006d6a10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "006d69b0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "006d69d4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "006d69f4",
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
      "006d69b0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "006d69d4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "006d69f4",
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

- 旧版 [`006d69a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6974.md#insn-006d69a0) · [`006d69a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6974.md#insn-006d69a8)
- 新版 `006d69a0`（命令位置の公開資料なし） · `006d69a8`（命令位置の公開資料なし）

~~~diff
- 006d69a0 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 006d69a0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006d69a0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006d69a0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006d69a0 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 006d69a0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006d69a0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006d69a0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006d69a0 bytes 73623291
+ 006d69a0 bytes 73623391
- 006d69a8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 006d69a8 bytes 89deffb0
+ 006d69a8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 006d69a8 bytes 89deffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65fcb8cad832a9dee5c314b2395cf693"></a>

### [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) → [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) FUN_006d6d04

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 288件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 288件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md)

変更の種類 branch_value, call_argument_candidate, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 99.29% / 新版 99.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_destination` 1件, `store_value` 11件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006d6d5c",
      "incomplete_value": true,
      "site": "006d6d5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5f7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d6d5c",
      "incomplete_value": true,
      "site": "006d6d5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:55d:8"
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
      "definition_site": "006d6d60",
      "incomplete_value": true,
      "site": "006d6d60",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006d6d60",
      "incomplete_value": true,
      "site": "006d6d60",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006d6d9c",
      "incomplete_value": true,
      "site": "006d6db0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:71d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d6d9c",
      "incomplete_value": true,
      "site": "006d6db0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:683:8"
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
      "006d6d3c",
      "READ",
      [
        "storage",
        "002a855d",
        null,
        "string"
      ]
    ],
    [
      "006d6d54",
      "READ",
      [
        "storage",
        "002a8562",
        null,
        "string"
      ]
    ],
    [
      "006d6d9c",
      "READ",
      [
        "storage",
        "002a7683",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006d6d3c",
      "READ",
      [
        "storage",
        "002a85f7",
        null,
        "string"
      ]
    ],
    [
      "006d6d54",
      "READ",
      [
        "storage",
        "002a85fc",
        null,
        "string"
      ]
    ],
    [
      "006d6d9c",
      "READ",
      [
        "storage",
        "002a771d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d6d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md#insn-006d6d34) · [`006d6d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md#insn-006d6d94) · [`006d6df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md#insn-006d6df8)
- 新版 `006d6d34`（命令位置の公開資料なし） · `006d6d94`（命令位置の公開資料なし） · `006d6df8`（命令位置の公開資料なし）

~~~diff
- 006d6d34 ["COPY", "tmp:0:8", ["const:55d:8"]]
- 006d6d34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d6d34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d6d34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d6d34 ["COPY", "tmp:0:8", ["const:5f7:8"]]
+ 006d6d34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d6d34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d6d34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d6d34 bytes 29751591
+ 006d6d34 bytes 29dd1791
- 006d6d94 ["COPY", "tmp:0:8", ["const:683:8"]]
- 006d6d94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d6d94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d6d94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d6d94 ["COPY", "tmp:0:8", ["const:71d:8"]]
+ 006d6d94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d6d94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d6d94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d6d94 bytes 290d1a91
+ 006d6d94 bytes 29751c91
- 006d6df8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006d6df8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006d6df8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 006d6df8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 006d6df8 bytes 003d45f9
+ 006d6df8 bytes 005d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dc916f71b44ab2145118cd2a6f46421"></a>

### [`006dd65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006dd65c.md) → [`006dd65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006dd65c.md) FUN_006dd65c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) [`008ffd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ffd00.md) · 呼出先 14件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`005bce08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bce08.md) [`005bce20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bce20.md) [`0063e588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e588.md)
- 新版 呼出元 2件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`008ffd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffd00.md) · 呼出先 14件 [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`005bce08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bce08.md) [`005bce20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bce20.md) [`0063e588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e588.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.62% / 新版 88.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 7件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006dd8c4",
      "incomplete_value": false,
      "site": "006dd8c4",
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
      "definition_site": "006dd8c4",
      "incomplete_value": false,
      "site": "006dd8c4",
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
    "ordinal": 17,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006dd8c8",
      "incomplete_value": false,
      "site": "006dd8c8",
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
      "definition_site": "006dd8c8",
      "incomplete_value": false,
      "site": "006dd8c8",
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
    "ordinal": 18,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006dd8c4",
      "incomplete_value": false,
      "site": "006dd8c8",
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
      "definition_site": "006dd8c4",
      "incomplete_value": false,
      "site": "006dd8c8",
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
      "006dd68c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006dd698",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006dd6a0",
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
      "006dd68c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006dd698",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006dd6a0",
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

- 旧版 [`006dd68c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006dd65c.md#insn-006dd68c) · [`006dd698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006dd65c.md#insn-006dd698) · [`006dd6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006dd65c.md#insn-006dd6a0)
- 新版 `006dd68c`（命令位置の公開資料なし） · `006dd698`（命令位置の公開資料なし） · `006dd6a0`（命令位置の公開資料なし）

~~~diff
- 006dd68c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006dd68c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006dd68c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 006dd68c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006dd68c bytes 083d45f9
+ 006dd68c bytes 085d45f9
- 006dd698 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 006dd698 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006dd698 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006dd698 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006dd698 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 006dd698 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006dd698 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006dd698 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006dd698 bytes 21203991
+ 006dd698 bytes 21603a91
- 006dd6a0 ["COPY", "tmp:0:8", ["const:500:8"]]
- 006dd6a0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006dd6a0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006dd6a0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006dd6a0 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 006dd6a0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006dd6a0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006dd6a0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006dd6a0 bytes 42001491
+ 006dd6a0 bytes 42401591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c59663cd344c8d3d1700be32ccad001"></a>

### [`006dd924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006dd924.md) → [`006dd924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006dd924.md) FUN_006dd924

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 3件 [`009019f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/009019f4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 3件 [`009019f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/009019f4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006dd958",
      "incomplete_value": true,
      "site": "006dd96c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:628:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006dd958",
      "incomplete_value": true,
      "site": "006dd96c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:58e:8"
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
      "definition_site": "006dd970",
      "incomplete_value": true,
      "site": "006dd970",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006dd970",
      "incomplete_value": true,
      "site": "006dd970",
      "value": [
        "LOAD",
        "8",
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
      "006dd958",
      "READ",
      [
        "storage",
        "002a858e",
        null,
        "string"
      ]
    ],
    [
      "006dd95c",
      "READ",
      [
        "storage",
        "002a859b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006dd958",
      "READ",
      [
        "storage",
        "002a8628",
        null,
        "string"
      ]
    ],
    [
      "006dd95c",
      "READ",
      [
        "storage",
        "002a8635",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006dd950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006dd924.md#insn-006dd950)
- 新版 `006dd950`（命令位置の公開資料なし）

~~~diff
- 006dd950 ["COPY", "tmp:0:8", ["const:58e:8"]]
- 006dd950 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006dd950 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006dd950 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006dd950 ["COPY", "tmp:0:8", ["const:628:8"]]
+ 006dd950 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006dd950 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006dd950 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006dd950 bytes 29391691
+ 006dd950 bytes 29a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80fb1e30602e9bbc0165396441dd6b75"></a>

### [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) → [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) FUN_006ddfb8

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 173件 [`00444bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444bb0.md) [`00444c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c18.md) [`00444c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c24.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 173件 [`00444bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444bb0.md) [`00444c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c18.md) [`00444c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c24.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_value

命令の説明率　旧版 98.94% / 新版 98.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 8件, `store_condition` 2件, `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e0820",
      "incomplete_value": true,
      "site": "006e0838",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:617:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e0820",
      "incomplete_value": true,
      "site": "006e0838",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:57d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 150,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e0874",
      "incomplete_value": true,
      "site": "006e0884",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:91e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e0874",
      "incomplete_value": true,
      "site": "006e0884",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:893:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 153,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e0a18",
      "incomplete_value": true,
      "site": "006e0a30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:88d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e0a18",
      "incomplete_value": true,
      "site": "006e0a30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 157,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006de028",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006de054",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006de05c",
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
      "006de028",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006de054",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006de05c",
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

- 旧版 [`006de028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md#insn-006de028) · [`006de054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md#insn-006de054) · [`006de05c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md#insn-006de05c)
- 新版 `006de028`（命令位置の公開資料なし） · `006de054`（命令位置の公開資料なし） · `006de05c`（命令位置の公開資料なし）

~~~diff
- 006de028 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
- 006de028 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006de028 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ab8:8"]]
+ 006de028 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 006de028 bytes 203d45f9
+ 006de028 bytes 205d45f9
- 006de054 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 006de054 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006de054 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006de054 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006de054 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 006de054 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006de054 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006de054 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006de054 bytes 21203991
+ 006de054 bytes 21603a91
- 006de05c ["COPY", "tmp:0:8", ["const:500:8"]]
- 006de05c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006de05c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006de05c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006de05c ["COPY", "tmp:0:8", ["const:550:8"]]
+ 006de05c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006de05c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006de05c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006de05c bytes 42001491
+ 006de05c bytes 42401591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f5b396d159e62ad1c453586d050e47e"></a>

### [`006e34b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e3/006e34b0.md) → [`006e34b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e3/006e34b0.md) FUN_006e34b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) · 呼出先 19件 [`005c022c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c0/005c022c.md) [`005dfeb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005df/005dfeb0.md) [`005e0000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e0/005e0000.md) [`00663624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00663/00663624.md) [`006f23b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f2/006f23b4.md)
- 新版 呼出元 1件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) · 呼出先 19件 [`005c022c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c0/005c022c.md) [`005dfeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005df/005dfeb0.md) [`005e0000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e0/005e0000.md) [`00663624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/00663624.md) [`006f23b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f23b4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.47% / 新版 97.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006e369c",
      "incomplete_value": false,
      "site": "006e36a8",
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
      "definition_site": "006e369c",
      "incomplete_value": false,
      "site": "006e36a8",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006e36d4",
      "incomplete_value": false,
      "site": "006e36d8",
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
      "definition_site": "006e36d4",
      "incomplete_value": false,
      "site": "006e36d8",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006e3778",
      "incomplete_value": false,
      "site": "006e377c",
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
      "definition_site": "006e3778",
      "incomplete_value": false,
      "site": "006e377c",
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
      "006e367c",
      "DATA",
      [
        "storage",
        "0029e6a4",
        null,
        "string"
      ]
    ],
    [
      "006e36a8",
      "DATA",
      [
        "storage",
        "002a69a3",
        null,
        "string"
      ]
    ],
    [
      "006e36d8",
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
      "006e367c",
      "DATA",
      [
        "storage",
        "0029e72f",
        null,
        "string"
      ]
    ],
    [
      "006e36a8",
      "DATA",
      [
        "storage",
        "002a6a3d",
        null,
        "string"
      ]
    ],
    [
      "006e36d8",
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

- 旧版 [`006e3674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e3/006e34b0.md#insn-006e3674) · [`006e369c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e3/006e34b0.md#insn-006e369c) · [`006e36d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e3/006e34b0.md#insn-006e36d4)
- 新版 `006e3674`（命令位置の公開資料なし） · `006e369c`（命令位置の公開資料なし） · `006e36d4`（命令位置の公開資料なし）

~~~diff
- 006e3674 ["COPY", "tmp:0:8", ["const:6a4:8"]]
- 006e3674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006e3674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006e3674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006e3674 ["COPY", "tmp:0:8", ["const:72f:8"]]
+ 006e3674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006e3674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006e3674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006e3674 bytes 08911a91
+ 006e3674 bytes 08bd1c91
- 006e369c ["COPY", "tmp:0:8", ["const:9a3:8"]]
- 006e369c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006e369c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006e369c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006e369c ["COPY", "tmp:0:8", ["const:a3d:8"]]
+ 006e369c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006e369c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006e369c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006e369c bytes 088d2691
+ 006e369c bytes 08f52891
- 006e36d4 ["COPY", "tmp:0:8", ["const:731:8"]]
- 006e36d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006e36d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006e36d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006e36d4 ["COPY", "tmp:0:8", ["const:7bc:8"]]
+ 006e36d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006e36d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006e36d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006e36d4 bytes 08c51c91
+ 006e36d4 bytes 08f11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14dc66281f9d0e72032825fda72c3bfd"></a>

### [`006e4220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4220.md) → [`006e4220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4220.md) FUN_006e4220

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
      "definition_site": "006e4244",
      "incomplete_value": false,
      "site": "006e4244",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e4244",
      "incomplete_value": false,
      "site": "006e4244",
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
            "const:120:8"
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
      "006e4244",
      "DATA",
      [
        "storage",
        "00bfa120",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006e4244",
      "DATA",
      [
        "storage",
        "00bfa170",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e4240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4220.md#insn-006e4240)
- 新版 `006e4240`（命令位置の公開資料なし）

~~~diff
- 006e4240 ["COPY", "tmp:0:8", ["const:120:8"]]
- 006e4240 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006e4240 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006e4240 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006e4240 ["COPY", "tmp:0:8", ["const:170:8"]]
+ 006e4240 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006e4240 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006e4240 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006e4240 bytes 08810491
+ 006e4240 bytes 08c10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68524cb9482e4ad71d80c50b5cf4314a"></a>

### [`006e4254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4254.md) → [`006e4254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4254.md) FUN_006e4254

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
      "definition_site": "006e4260",
      "incomplete_value": false,
      "site": "006e4260",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e4260",
      "incomplete_value": false,
      "site": "006e4260",
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
            "const:120:8"
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
      "006e4260",
      "DATA",
      [
        "storage",
        "00bfa120",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006e4260",
      "DATA",
      [
        "storage",
        "00bfa170",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e425c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4254.md#insn-006e425c)
- 新版 `006e425c`（命令位置の公開資料なし）

~~~diff
- 006e425c ["COPY", "tmp:0:8", ["const:120:8"]]
- 006e425c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006e425c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006e425c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006e425c ["COPY", "tmp:0:8", ["const:170:8"]]
+ 006e425c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006e425c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006e425c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006e425c bytes 29810491
+ 006e425c bytes 29c10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58c71b20a6617d3e2533640207704f28"></a>

### [`006e42fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e42fc.md) → [`006e42fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e42fc.md) FUN_006e42fc

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
      "definition_site": "006e4320",
      "incomplete_value": false,
      "site": "006e4320",
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
            "const:1f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e4320",
      "incomplete_value": false,
      "site": "006e4320",
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
            "const:1a0:8"
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
      "006e4320",
      "DATA",
      [
        "storage",
        "00bfa1a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006e4320",
      "DATA",
      [
        "storage",
        "00bfa1f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e431c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e42fc.md#insn-006e431c)
- 新版 `006e431c`（命令位置の公開資料なし）

~~~diff
- 006e431c ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 006e431c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006e431c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006e431c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006e431c ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 006e431c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006e431c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006e431c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006e431c bytes 08810691
+ 006e431c bytes 08c10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f6e9d86119e69fa0215724021719cdf"></a>

### [`006e4330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4330.md) → [`006e4330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4330.md) FUN_006e4330

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
      "definition_site": "006e433c",
      "incomplete_value": false,
      "site": "006e433c",
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
            "const:1f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e433c",
      "incomplete_value": false,
      "site": "006e433c",
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
            "const:1a0:8"
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
      "006e433c",
      "DATA",
      [
        "storage",
        "00bfa1a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006e433c",
      "DATA",
      [
        "storage",
        "00bfa1f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e4338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4330.md#insn-006e4338)
- 新版 `006e4338`（命令位置の公開資料なし）

~~~diff
- 006e4338 ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 006e4338 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006e4338 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006e4338 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006e4338 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 006e4338 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006e4338 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006e4338 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006e4338 bytes 29810691
+ 006e4338 bytes 29c10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc529dd05cc6516f2e2a453073e88782"></a>

### [`006e43e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e43e4.md) → [`006e43e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e43e4.md) FUN_006e43e4

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
      "definition_site": "006e4404",
      "incomplete_value": false,
      "site": "006e4408",
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
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e4404",
      "incomplete_value": false,
      "site": "006e4408",
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
            "const:220:8"
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
      "006e4408",
      "DATA",
      [
        "storage",
        "00bfa220",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006e4408",
      "DATA",
      [
        "storage",
        "00bfa270",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e4404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e43e4.md#insn-006e4404)
- 新版 `006e4404`（命令位置の公開資料なし）

~~~diff
- 006e4404 ["COPY", "tmp:0:8", ["const:220:8"]]
- 006e4404 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006e4404 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006e4404 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006e4404 ["COPY", "tmp:0:8", ["const:270:8"]]
+ 006e4404 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006e4404 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006e4404 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006e4404 bytes 08810891
+ 006e4404 bytes 08c10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f826b8ac66f7f1ce0a891abfd54b655"></a>

### [`006e441c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e441c.md) → [`006e441c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e441c.md) FUN_006e441c

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
      "definition_site": "006e4420",
      "incomplete_value": false,
      "site": "006e4424",
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
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e4420",
      "incomplete_value": false,
      "site": "006e4424",
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
            "const:220:8"
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
      "006e4424",
      "DATA",
      [
        "storage",
        "00bfa220",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006e4424",
      "DATA",
      [
        "storage",
        "00bfa270",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e4420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e441c.md#insn-006e4420)
- 新版 `006e4420`（命令位置の公開資料なし）

~~~diff
- 006e4420 ["COPY", "tmp:0:8", ["const:220:8"]]
- 006e4420 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006e4420 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006e4420 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006e4420 ["COPY", "tmp:0:8", ["const:270:8"]]
+ 006e4420 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006e4420 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006e4420 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006e4420 bytes 08810891
+ 006e4420 bytes 08c10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99313974f1b617a325222297903cf766"></a>

### [`006e4474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4474.md) → [`006e4474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4474.md) FUN_006e4474

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
      "definition_site": "006e4498",
      "incomplete_value": false,
      "site": "006e4498",
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
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e4498",
      "incomplete_value": false,
      "site": "006e4498",
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
            "const:2a0:8"
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
      "006e4498",
      "DATA",
      [
        "storage",
        "00bfa2a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006e4498",
      "DATA",
      [
        "storage",
        "00bfa2f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e4494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4474.md#insn-006e4494)
- 新版 `006e4494`（命令位置の公開資料なし）

~~~diff
- 006e4494 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 006e4494 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006e4494 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006e4494 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006e4494 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 006e4494 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006e4494 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006e4494 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006e4494 bytes 08810a91
+ 006e4494 bytes 08c10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4648d1023f4d3127f9df11575b358559"></a>

### [`006e44a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e44a8.md) → [`006e44a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e44a8.md) FUN_006e44a8

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
      "definition_site": "006e44b4",
      "incomplete_value": false,
      "site": "006e44b4",
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
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e44b4",
      "incomplete_value": false,
      "site": "006e44b4",
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
            "const:2a0:8"
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
      "006e44b4",
      "DATA",
      [
        "storage",
        "00bfa2a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006e44b4",
      "DATA",
      [
        "storage",
        "00bfa2f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e44b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e44a8.md#insn-006e44b0)
- 新版 `006e44b0`（命令位置の公開資料なし）

~~~diff
- 006e44b0 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 006e44b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006e44b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006e44b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006e44b0 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 006e44b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006e44b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006e44b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006e44b0 bytes 29810a91
+ 006e44b0 bytes 29c10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9637fd535e00fb86884d3f59d30efde4"></a>

### [`006e4550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4550.md) → [`006e4550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4550.md) FUN_006e4550

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
      "definition_site": "006e4570",
      "incomplete_value": false,
      "site": "006e4574",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e4570",
      "incomplete_value": false,
      "site": "006e4574",
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
            "const:320:8"
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
      "006e4574",
      "DATA",
      [
        "storage",
        "00bfa320",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006e4574",
      "DATA",
      [
        "storage",
        "00bfa370",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e4570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4550.md#insn-006e4570)
- 新版 `006e4570`（命令位置の公開資料なし）

~~~diff
- 006e4570 ["COPY", "tmp:0:8", ["const:320:8"]]
- 006e4570 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006e4570 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006e4570 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006e4570 ["COPY", "tmp:0:8", ["const:370:8"]]
+ 006e4570 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006e4570 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006e4570 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006e4570 bytes 08810c91
+ 006e4570 bytes 08c10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c0d75f114611762d5789dcc29c12da7"></a>

### [`006e4588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4588.md) → [`006e4588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4588.md) FUN_006e4588

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
      "definition_site": "006e458c",
      "incomplete_value": false,
      "site": "006e4590",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e458c",
      "incomplete_value": false,
      "site": "006e4590",
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
            "const:320:8"
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
      "006e4590",
      "DATA",
      [
        "storage",
        "00bfa320",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006e4590",
      "DATA",
      [
        "storage",
        "00bfa370",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e458c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4588.md#insn-006e458c)
- 新版 `006e458c`（命令位置の公開資料なし）

~~~diff
- 006e458c ["COPY", "tmp:0:8", ["const:320:8"]]
- 006e458c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006e458c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006e458c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006e458c ["COPY", "tmp:0:8", ["const:370:8"]]
+ 006e458c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006e458c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006e458c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006e458c bytes 08810c91
+ 006e458c bytes 08c10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d1609c7acb71b3647d99e83159471ce"></a>

### [`006e45e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e45e0.md) → [`006e45e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e45e0.md) FUN_006e45e0

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
      "definition_site": "006e4604",
      "incomplete_value": false,
      "site": "006e4604",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e4604",
      "incomplete_value": false,
      "site": "006e4604",
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
            "const:3a0:8"
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
      "006e4604",
      "DATA",
      [
        "storage",
        "00bfa3a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006e4604",
      "DATA",
      [
        "storage",
        "00bfa3f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e4600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e45e0.md#insn-006e4600)
- 新版 `006e4600`（命令位置の公開資料なし）

~~~diff
- 006e4600 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 006e4600 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006e4600 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006e4600 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006e4600 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 006e4600 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006e4600 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006e4600 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006e4600 bytes 08810e91
+ 006e4600 bytes 08c10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e9b51ed01494f1e48c5aa65d143905e"></a>

### [`006e4614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4614.md) → [`006e4614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4614.md) FUN_006e4614

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
      "definition_site": "006e4620",
      "incomplete_value": false,
      "site": "006e4620",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e4620",
      "incomplete_value": false,
      "site": "006e4620",
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
            "const:3a0:8"
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
      "006e4620",
      "DATA",
      [
        "storage",
        "00bfa3a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006e4620",
      "DATA",
      [
        "storage",
        "00bfa3f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e461c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4614.md#insn-006e461c)
- 新版 `006e461c`（命令位置の公開資料なし）

~~~diff
- 006e461c ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 006e461c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006e461c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006e461c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006e461c ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 006e461c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006e461c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006e461c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006e461c bytes 29810e91
+ 006e461c bytes 29c10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b323724f8ae0275cdc87ac2044c5af58"></a>

### [`006e46bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e46bc.md) → [`006e46bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e46bc.md) FUN_006e46bc

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
      "definition_site": "006e46dc",
      "incomplete_value": false,
      "site": "006e46e0",
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
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e46dc",
      "incomplete_value": false,
      "site": "006e46e0",
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
            "const:420:8"
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
      "006e46e0",
      "DATA",
      [
        "storage",
        "00bfa420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006e46e0",
      "DATA",
      [
        "storage",
        "00bfa470",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e46dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e46bc.md#insn-006e46dc)
- 新版 `006e46dc`（命令位置の公開資料なし）

~~~diff
- 006e46dc ["COPY", "tmp:0:8", ["const:420:8"]]
- 006e46dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006e46dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006e46dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006e46dc ["COPY", "tmp:0:8", ["const:470:8"]]
+ 006e46dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006e46dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006e46dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006e46dc bytes 08811091
+ 006e46dc bytes 08c11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f91df96f32034936caa888e29cf3d596"></a>

### [`006e46f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e46f4.md) → [`006e46f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e46f4.md) FUN_006e46f4

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
      "definition_site": "006e46f8",
      "incomplete_value": true,
      "site": "006e46fc",
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
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e46f8",
      "incomplete_value": true,
      "site": "006e46fc",
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
            "const:420:8"
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
      "006e46fc",
      "DATA",
      [
        "storage",
        "00bfa420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006e46fc",
      "DATA",
      [
        "storage",
        "00bfa470",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e46f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e46f4.md#insn-006e46f8)
- 新版 `006e46f8`（命令位置の公開資料なし）

~~~diff
- 006e46f8 ["COPY", "tmp:0:8", ["const:420:8"]]
- 006e46f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006e46f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006e46f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006e46f8 ["COPY", "tmp:0:8", ["const:470:8"]]
+ 006e46f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006e46f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006e46f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006e46f8 bytes 08811091
+ 006e46f8 bytes 08c11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c9f5f5b111dd58ee8f7553c7619bb73"></a>

### [`006e4748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4748.md) → [`006e4748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4748.md) FUN_006e4748

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "006e4754",
      "incomplete_value": true,
      "site": "006e4758",
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
      "definition_site": "006e4754",
      "incomplete_value": true,
      "site": "006e4758",
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
      "006e4754",
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
      "006e4754",
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

- 旧版 [`006e4754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4748.md#insn-006e4754)
- 新版 `006e4754`（命令位置の公開資料なし）

~~~diff
- 006e4754 ["COPY", "tmp:0:8", ["const:303:8"]]
- 006e4754 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006e4754 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006e4754 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006e4754 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 006e4754 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006e4754 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006e4754 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006e4754 bytes 000c0c91
+ 006e4754 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-531b44f9da887b922c6c90ee362ac573"></a>

### [`006e475c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e475c.md) → [`006e475c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e475c.md) _INIT_109

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.09% / 新版 92.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006e4984",
      "incomplete_value": false,
      "site": "006e4990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c27000:8"
          ],
          [
            "leaf",
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e4984",
      "incomplete_value": false,
      "site": "006e4990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c27000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
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
      "definition_site": "006e498c",
      "incomplete_value": false,
      "site": "006e4990",
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
      "definition_site": "006e498c",
      "incomplete_value": false,
      "site": "006e4990",
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
      "006e4798",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "006e47bc",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "006e47dc",
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
      "006e4798",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "006e47bc",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "006e47dc",
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

- 旧版 [`006e4788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e475c.md#insn-006e4788) · [`006e4790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e475c.md#insn-006e4790)
- 新版 `006e4788`（命令位置の公開資料なし） · `006e4790`（命令位置の公開資料なし）

~~~diff
- 006e4788 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 006e4788 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006e4788 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006e4788 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006e4788 ["COPY", "tmp:0:8", ["const:cf0:8"]]
+ 006e4788 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006e4788 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006e4788 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006e4788 bytes 73c23291
+ 006e4788 bytes 73c23391
- 006e4790 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 006e4790 bytes 09defff0
+ 006e4790 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 006e4790 bytes 09defff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-440b8e6bc723c223e084fba9da4b1592"></a>

### [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) → [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) FUN_006e4aec

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`006e92bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e92bc.md) [`006eab4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ea/006eab4c.md) [`006eaef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ea/006eaef0.md) [`006eb364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006eb/006eb364.md) · 呼出先 86件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md)
- 新版 呼出元 4件 [`006e92bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e92bc.md) [`006eab4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006eab4c.md) [`006eaef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006eaef0.md) [`006eb364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb364.md) · 呼出先 86件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 99.10% / 新版 99.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e5d0c",
      "incomplete_value": true,
      "site": "006e5d1c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "006e5d0c",
      "incomplete_value": true,
      "site": "006e5d1c",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 118,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e5d08",
      "incomplete_value": true,
      "site": "006e5d1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:940:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e5d08",
      "incomplete_value": true,
      "site": "006e5d1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8b5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 119,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e5d08",
      "incomplete_value": true,
      "site": "006e5d20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:940:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e5d08",
      "incomplete_value": true,
      "site": "006e5d20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8b5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 120,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e526c",
      "PARAM",
      [
        "storage",
        "00296e2a",
        null,
        null
      ]
    ],
    [
      "006e5d08",
      "READ",
      [
        "storage",
        "0029f8b5",
        null,
        "string"
      ]
    ],
    [
      "006e5d0c",
      "READ",
      [
        "storage",
        "0029f8be",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006e526c",
      "PARAM",
      [
        "storage",
        "00296d9d",
        null,
        null
      ]
    ],
    [
      "006e5d08",
      "READ",
      [
        "storage",
        "0029f940",
        null,
        "string"
      ]
    ],
    [
      "006e5d0c",
      "READ",
      [
        "storage",
        "0029f949",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e526c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md#insn-006e526c) · [`006e5d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md#insn-006e5d00) · [`006e5d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md#insn-006e5d04)
- 新版 `006e526c`（命令位置の公開資料なし） · `006e5d00`（命令位置の公開資料なし）

~~~diff
- 006e526c ["COPY", "tmp:0:8", ["const:e2a:8"]]
- 006e526c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006e526c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006e526c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006e526c ["COPY", "tmp:0:8", ["const:d9d:8"]]
+ 006e526c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006e526c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006e526c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006e526c bytes 21a83891
+ 006e526c bytes 21743691
- 006e5d00 ["COPY", "tmp:0:8", ["const:8b5:8"]]
- 006e5d00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006e5d00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006e5d00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006e5d00 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 006e5d00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006e5d00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006e5d00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006e5d00 bytes 08d52291
+ 006e5d00 bytes 08012591
- 006e5d04 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 006e5d04 bytes 69deff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffb569c1c9b6de98564653d25d7f940f"></a>

### [`006e62f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e62f8.md) → [`006e62f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e62f8.md) FUN_006e62f8

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`005d6c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d6c3c.md) [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 60件 [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`005bc198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bc198.md) [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0063a050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063a/0063a050.md) [`0063c178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063c178.md)
- 新版 呼出元 3件 [`005d6c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d6/005d6c3c.md) [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 60件 [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`005bc198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc198.md) [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0063a050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063a/0063a050.md) [`0063c178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c178.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.27% / 新版 98.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e6c5c",
      "incomplete_value": true,
      "site": "006e6c70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e6c5c",
      "incomplete_value": true,
      "site": "006e6c70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 67,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e6c5c",
      "incomplete_value": true,
      "site": "006e6c74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e6c5c",
      "incomplete_value": true,
      "site": "006e6c74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 68,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e723c",
      "incomplete_value": true,
      "site": "006e7254",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dcb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e723c",
      "incomplete_value": true,
      "site": "006e7254",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e58:8"
              ]
            ]
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
      "006e6708",
      "READ",
      [
        "storage",
        "0029b7f4",
        null,
        "string"
      ]
    ],
    [
      "006e670c",
      "READ",
      [
        "storage",
        "0029b803",
        null,
        "string"
      ]
    ],
    [
      "006e6874",
      "READ",
      [
        "storage",
        "002a18ef",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006e6708",
      "READ",
      [
        "storage",
        "0029b7f2",
        null,
        "string"
      ]
    ],
    [
      "006e670c",
      "READ",
      [
        "storage",
        "0029b801",
        null,
        "string"
      ]
    ],
    [
      "006e6874",
      "READ",
      [
        "storage",
        "002a197a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e66fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e62f8.md#insn-006e66fc) · [`006e6700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e62f8.md#insn-006e6700)
- 新版 `006e66fc`（命令位置の公開資料なし） · `006e6700`（命令位置の公開資料なし）

~~~diff
- 006e66fc ["COPY", "register:4040:8", ["const:29b000:8"]]
- 006e66fc bytes a8ddffb0
+ 006e66fc ["COPY", "register:4040:8", ["const:29b000:8"]]
+ 006e66fc bytes a8ddffb0
- 006e6700 ["COPY", "tmp:0:8", ["const:7f4:8"]]
- 006e6700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006e6700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006e6700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006e6700 ["COPY", "tmp:0:8", ["const:7f2:8"]]
+ 006e6700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006e6700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006e6700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006e6700 bytes 08d11f91
+ 006e6700 bytes 08c91f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0cf1cdb18d0803c1327e0ae07fb65db"></a>

### [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) → [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) FUN_006e79bc

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`006ea1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ea/006ea1c0.md) [`006ead1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ea/006ead1c.md) [`006eaef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ea/006eaef0.md) [`006eb364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006eb/006eb364.md) · 呼出先 97件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`0044abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abe4.md) [`005bc198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bc198.md) [`005bc1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bc1dc.md)
- 新版 呼出元 4件 [`006ea1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ea1c0.md) [`006ead1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ead1c.md) [`006eaef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006eaef0.md) [`006eb364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb364.md) · 呼出先 97件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044abe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abe4.md) [`005bc198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc198.md) [`005bc1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc1dc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.20% / 新版 99.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006e887c",
      "incomplete_value": false,
      "site": "006e8884",
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
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e887c",
      "incomplete_value": false,
      "site": "006e8884",
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
            "const:78a:8"
          ]
        ]
      ]
    },
    "ordinal": 137,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006e8ae4",
      "incomplete_value": false,
      "site": "006e8aec",
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
            "const:10b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e8ae4",
      "incomplete_value": false,
      "site": "006e8aec",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "ordinal": 157,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006e8bc8",
      "incomplete_value": false,
      "site": "006e8bd0",
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
            "const:8af:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e8bc8",
      "incomplete_value": false,
      "site": "006e8bd0",
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
            "const:815:8"
          ]
        ]
      ]
    },
    "ordinal": 169,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e887c",
      "PARAM",
      [
        "storage",
        "0029b78a",
        null,
        null
      ]
    ],
    [
      "006e8ae4",
      "PARAM",
      [
        "storage",
        "00299198",
        null,
        null
      ]
    ],
    [
      "006e8bc8",
      "PARAM",
      [
        "storage",
        "002a7815",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006e887c",
      "PARAM",
      [
        "storage",
        "0029b788",
        null,
        null
      ]
    ],
    [
      "006e8ae4",
      "PARAM",
      [
        "storage",
        "0029910b",
        null,
        null
      ]
    ],
    [
      "006e8bc8",
      "PARAM",
      [
        "storage",
        "002a78af",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e887c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md#insn-006e887c) · [`006e8ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md#insn-006e8ae4) · [`006e8bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md#insn-006e8bc8)
- 新版 `006e887c`（命令位置の公開資料なし） · `006e8ae4`（命令位置の公開資料なし） · `006e8bc8`（命令位置の公開資料なし）

~~~diff
- 006e887c ["COPY", "tmp:0:8", ["const:78a:8"]]
- 006e887c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006e887c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006e887c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006e887c ["COPY", "tmp:0:8", ["const:788:8"]]
+ 006e887c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006e887c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006e887c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006e887c bytes 21281e91
+ 006e887c bytes 21201e91
- 006e8ae4 ["COPY", "tmp:0:8", ["const:198:8"]]
- 006e8ae4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006e8ae4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006e8ae4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006e8ae4 ["COPY", "tmp:0:8", ["const:10b:8"]]
+ 006e8ae4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006e8ae4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006e8ae4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006e8ae4 bytes 21600691
+ 006e8ae4 bytes 212c0491
- 006e8bc8 ["COPY", "tmp:0:8", ["const:815:8"]]
- 006e8bc8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006e8bc8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006e8bc8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006e8bc8 ["COPY", "tmp:0:8", ["const:8af:8"]]
+ 006e8bc8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006e8bc8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006e8bc8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006e8bc8 bytes 21542091
+ 006e8bc8 bytes 21bc2291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a81c97683265ec6366e70f0843e44fd1"></a>

### [`006eb464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006eb/006eb464.md) → [`006eb464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb464.md) FUN_006eb464

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) · 呼出先 81件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`0044ab70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ab70.md) [`0044abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abe4.md) [`0044abfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abfc.md)
- 新版 呼出元 2件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 81件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044ab70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ab70.md) [`0044abe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abe4.md) [`0044abfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abfc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.04% / 新版 99.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006ebbd8",
      "incomplete_value": true,
      "site": "006ebbe8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "006ebbd8",
      "incomplete_value": true,
      "site": "006ebbe8",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 57,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006ebbe4",
      "incomplete_value": true,
      "site": "006ebbec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:63e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ebbe4",
      "incomplete_value": true,
      "site": "006ebbec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5a4:8"
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
      "definition_site": "006ebbe4",
      "incomplete_value": true,
      "site": "006ebbf0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:63e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ebbe4",
      "incomplete_value": true,
      "site": "006ebbf0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5a4:8"
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
      "006eb854",
      "READ",
      [
        "storage",
        "00c1b6e0",
        null,
        "pointer"
      ]
    ],
    [
      "006eb858",
      "DATA",
      [
        "storage",
        "00c24074",
        null,
        null
      ]
    ],
    [
      "006eb858",
      "DATA",
      [
        "storage",
        "00c240d4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006eb854",
      "READ",
      [
        "storage",
        "00c1b730",
        null,
        "pointer"
      ]
    ],
    [
      "006eb858",
      "DATA",
      [
        "storage",
        "00c240c4",
        null,
        null
      ]
    ],
    [
      "006eb858",
      "DATA",
      [
        "storage",
        "00c24124",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006eb854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006eb/006eb464.md#insn-006eb854) · [`006ebbd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006eb/006eb464.md#insn-006ebbd4) · [`006ebdbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006eb/006eb464.md#insn-006ebdbc)
- 新版 `006eb854`（命令位置の公開資料なし） · `006ebbd4`（命令位置の公開資料なし） · `006ebdbc`（命令位置の公開資料なし）

~~~diff
- 006eb854 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6e0:8"]]
- 006eb854 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 006eb854 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:730:8"]]
+ 006eb854 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 006eb854 bytes 297143f9
+ 006eb854 bytes 299943f9
- 006ebbd4 ["COPY", "tmp:0:8", ["const:5a4:8"]]
- 006ebbd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ebbd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ebbd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ebbd4 ["COPY", "tmp:0:8", ["const:63e:8"]]
+ 006ebbd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ebbd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ebbd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ebbd4 bytes 08911691
+ 006ebbd4 bytes 08f91891
- 006ebdbc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:730:8"]]
- 006ebdbc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 006ebdbc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:780:8"]]
+ 006ebdbc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 006ebdbc bytes 299943f9
+ 006ebdbc bytes 29c143f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5aa1f7f9aad92580d747f86ca9da3ae5"></a>

### [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) → [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) FUN_006eccf4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 122件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`0044ab70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ab70.md) [`0044abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abe4.md) [`0044abfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abfc.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 122件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044ab70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ab70.md) [`0044abe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abe4.md) [`0044abfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abfc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.60% / 新版 99.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006ed670",
      "incomplete_value": false,
      "site": "006ed674",
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
            "const:63e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ed670",
      "incomplete_value": false,
      "site": "006ed674",
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
            "const:5a4:8"
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
      "definition_site": "006ed6e0",
      "incomplete_value": false,
      "site": "006ed6e4",
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
            "const:63e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ed6e0",
      "incomplete_value": false,
      "site": "006ed6e4",
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
            "const:5a4:8"
          ]
        ]
      ]
    },
    "ordinal": 96,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006edc8c",
      "incomplete_value": false,
      "site": "006edc90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:10b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006edc8c",
      "incomplete_value": false,
      "site": "006edc90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:10d:8"
          ]
        ]
      ]
    },
    "ordinal": 152,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ed4ac",
      "READ",
      [
        "storage",
        "00c1b6e0",
        null,
        "pointer"
      ]
    ],
    [
      "006ed4b0",
      "DATA",
      [
        "storage",
        "00c24074",
        null,
        null
      ]
    ],
    [
      "006ed4b0",
      "DATA",
      [
        "storage",
        "00c240d4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006ed4ac",
      "READ",
      [
        "storage",
        "00c1b730",
        null,
        "pointer"
      ]
    ],
    [
      "006ed4b0",
      "DATA",
      [
        "storage",
        "00c240c4",
        null,
        null
      ]
    ],
    [
      "006ed4b0",
      "DATA",
      [
        "storage",
        "00c24124",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ed4ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md#insn-006ed4ac) · [`006ed670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md#insn-006ed670) · [`006ed6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md#insn-006ed6e0)
- 新版 `006ed4ac`（命令位置の公開資料なし） · `006ed670`（命令位置の公開資料なし） · `006ed6e0`（命令位置の公開資料なし）

~~~diff
- 006ed4ac ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6e0:8"]]
- 006ed4ac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 006ed4ac ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:730:8"]]
+ 006ed4ac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 006ed4ac bytes 297143f9
+ 006ed4ac bytes 299943f9
- 006ed670 ["COPY", "tmp:0:8", ["const:5a4:8"]]
- 006ed670 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006ed670 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006ed670 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006ed670 ["COPY", "tmp:0:8", ["const:63e:8"]]
+ 006ed670 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006ed670 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006ed670 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006ed670 bytes 21901691
+ 006ed670 bytes 21f81891
- 006ed6e0 ["COPY", "tmp:0:8", ["const:5a4:8"]]
- 006ed6e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006ed6e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006ed6e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006ed6e0 ["COPY", "tmp:0:8", ["const:63e:8"]]
+ 006ed6e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006ed6e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006ed6e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006ed6e0 bytes 21901691
+ 006ed6e0 bytes 21f81891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2738ad6faa027e1e17e08369711ab3a7"></a>

### [`006ef664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ef/006ef664.md) → [`006ef664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ef/006ef664.md) FUN_006ef664

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006e92bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e92bc.md) [`006ea1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ea/006ea1c0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`006e92bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e92bc.md) [`006ea1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ea1c0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "006ef670",
      "incomplete_value": false,
      "site": "006ef674",
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
      "definition_site": "006ef670",
      "incomplete_value": false,
      "site": "006ef674",
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
      "006ef670",
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
      "006ef670",
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

- 旧版 [`006ef670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ef/006ef664.md#insn-006ef670)
- 新版 `006ef670`（命令位置の公開資料なし）

~~~diff
- 006ef670 ["COPY", "tmp:0:8", ["const:303:8"]]
- 006ef670 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006ef670 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006ef670 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006ef670 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 006ef670 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006ef670 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006ef670 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006ef670 bytes 000c0c91
+ 006ef670 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be2e0f26787045ea22d8af6fc10c0a89"></a>

### [`006ef678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ef/006ef678.md) → [`006ef678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ef/006ef678.md) FUN_006ef678

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006eaef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ea/006eaef0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`006eaef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006eaef0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "006ef684",
      "incomplete_value": false,
      "site": "006ef688",
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
      "definition_site": "006ef684",
      "incomplete_value": false,
      "site": "006ef688",
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
      "006ef684",
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
      "006ef684",
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

- 旧版 [`006ef684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ef/006ef678.md#insn-006ef684)
- 新版 `006ef684`（命令位置の公開資料なし）

~~~diff
- 006ef684 ["COPY", "tmp:0:8", ["const:303:8"]]
- 006ef684 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006ef684 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006ef684 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006ef684 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 006ef684 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006ef684 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006ef684 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006ef684 bytes 000c0c91
+ 006ef684 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7f33abfb5b38b4609da5fa23f653adb"></a>

### [`006ef768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ef/006ef768.md) → [`006ef768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ef/006ef768.md) _INIT_110

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
      "definition_site": "006ef7a4",
      "incomplete_value": true,
      "site": "006ef7c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006ef7a4",
      "incomplete_value": true,
      "site": "006ef7c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006ef7e8",
      "incomplete_value": true,
      "site": "006ef804",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006ef7e8",
      "incomplete_value": true,
      "site": "006ef804",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006ef808",
      "incomplete_value": true,
      "site": "006ef820",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006ef808",
      "incomplete_value": true,
      "site": "006ef820",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "006ef7a4",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "006ef7c8",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "006ef7e8",
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
      "006ef7a4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "006ef7c8",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "006ef7e8",
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

- 旧版 [`006ef794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ef/006ef768.md#insn-006ef794) · [`006ef79c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ef/006ef768.md#insn-006ef79c)
- 新版 `006ef794`（命令位置の公開資料なし） · `006ef79c`（命令位置の公開資料なし）

~~~diff
- 006ef794 ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 006ef794 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006ef794 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006ef794 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006ef794 ["COPY", "tmp:0:8", ["const:d08:8"]]
+ 006ef794 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006ef794 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006ef794 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006ef794 bytes 73223391
+ 006ef794 bytes 73223491
- 006ef79c ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 006ef79c bytes c9ddff90
+ 006ef79c ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 006ef79c bytes c9ddff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17e4fde55685efe0327c76da9ab4f62b"></a>

### [`006efbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ef/006efbbc.md) → [`006efbbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ef/006efbbc.md) FUN_006efbbc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009a311c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a3/009a311c.md) · 呼出先 18件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`009a311c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a3/009a311c.md) · 呼出先 18件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.84% / 新版 96.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006efc00",
      "incomplete_value": false,
      "site": "006efc04",
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
      "definition_site": "006efc00",
      "incomplete_value": false,
      "site": "006efc04",
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
      "definition_site": "006efc28",
      "incomplete_value": true,
      "site": "006efc44",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ba8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006efc28",
      "incomplete_value": true,
      "site": "006efc44",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c35:8"
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
      "definition_site": "006efc28",
      "incomplete_value": true,
      "site": "006efc44",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "006efc28",
      "incomplete_value": true,
      "site": "006efc44",
      "value": [
        "LOAD",
        "16",
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
      "006efc04",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "006efc28",
      "READ",
      [
        "storage",
        "00293c35",
        null,
        "string"
      ]
    ],
    [
      "006efc28",
      "READ",
      [
        "storage",
        "00293c45",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006efc04",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "006efc28",
      "READ",
      [
        "storage",
        "00293ba8",
        null,
        "string"
      ]
    ],
    [
      "006efc28",
      "READ",
      [
        "storage",
        "00293bb8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006efc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ef/006efbbc.md#insn-006efc00) · [`006efc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ef/006efbbc.md#insn-006efc20) · [`006efc24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ef/006efbbc.md#insn-006efc24)
- 新版 `006efc00`（命令位置の公開資料なし） · `006efc20`（命令位置の公開資料なし）

~~~diff
- 006efc00 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 006efc00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006efc00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006efc00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006efc00 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 006efc00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006efc00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006efc00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006efc00 bytes 08a13491
+ 006efc00 bytes 08e13591
- 006efc20 ["COPY", "tmp:0:8", ["const:c35:8"]]
- 006efc20 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 006efc20 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 006efc20 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006efc20 ["COPY", "tmp:0:8", ["const:ba8:8"]]
+ 006efc20 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006efc20 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006efc20 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 006efc20 bytes 4ad53091
+ 006efc20 bytes 4aa12e91
- 006efc24 ["COPY", "register:4040:8", ["const:2b1000:8"]]
- 006efc24 bytes 08deffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7faf76bd96f9cfa4f10f0354dccf6a44"></a>

### [`006f02e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f0/006f02e0.md) → [`006f02e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f0/006f02e0.md) FUN_006f02e0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006efbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ef/006efbbc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`006efbbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ef/006efbbc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "006f02ec",
      "incomplete_value": false,
      "site": "006f02f0",
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
      "definition_site": "006f02ec",
      "incomplete_value": false,
      "site": "006f02f0",
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
      "006f02ec",
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
      "006f02ec",
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

- 旧版 [`006f02ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f0/006f02e0.md#insn-006f02ec)
- 新版 `006f02ec`（命令位置の公開資料なし）

~~~diff
- 006f02ec ["COPY", "tmp:0:8", ["const:303:8"]]
- 006f02ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006f02ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006f02ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006f02ec ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 006f02ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006f02ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006f02ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006f02ec bytes 000c0c91
+ 006f02ec bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfce883dcdcbfe3065057d0b9977a829"></a>

### [`006f02f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f0/006f02f4.md) → [`006f02f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f0/006f02f4.md) FUN_006f02f4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006efbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ef/006efbbc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`006efbbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ef/006efbbc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "006f0300",
      "incomplete_value": false,
      "site": "006f0304",
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
      "definition_site": "006f0300",
      "incomplete_value": false,
      "site": "006f0304",
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
      "006f0300",
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
      "006f0300",
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

- 旧版 [`006f0300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f0/006f02f4.md#insn-006f0300)
- 新版 `006f0300`（命令位置の公開資料なし）

~~~diff
- 006f0300 ["COPY", "tmp:0:8", ["const:303:8"]]
- 006f0300 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006f0300 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006f0300 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006f0300 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 006f0300 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006f0300 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006f0300 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006f0300 bytes 000c0c91
+ 006f0300 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d013bf1f0b3578008d6481ec578112d"></a>

### [`006f0308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f0/006f0308.md) → [`006f0308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f0/006f0308.md) _INIT_111

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
      "definition_site": "006f0344",
      "incomplete_value": true,
      "site": "006f0360",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f0344",
      "incomplete_value": true,
      "site": "006f0360",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f0368",
      "incomplete_value": true,
      "site": "006f0384",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f0368",
      "incomplete_value": true,
      "site": "006f0384",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f0388",
      "incomplete_value": true,
      "site": "006f03a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f0388",
      "incomplete_value": true,
      "site": "006f03a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "006f0344",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "006f0368",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "006f0388",
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
      "006f0344",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "006f0368",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "006f0388",
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

- 旧版 [`006f0334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f0/006f0308.md#insn-006f0334) · [`006f033c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f0/006f0308.md#insn-006f033c)
- 新版 `006f0334`（命令位置の公開資料なし） · `006f033c`（命令位置の公開資料なし）

~~~diff
- 006f0334 ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 006f0334 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006f0334 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006f0334 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006f0334 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 006f0334 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006f0334 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006f0334 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006f0334 bytes 73823391
+ 006f0334 bytes 73823491
- 006f033c ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 006f033c bytes a9ddfff0
+ 006f033c ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 006f033c bytes a9ddfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60a9e7654c6dcf1946fb9aa5beb67149"></a>

### [`006f0cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f0/006f0cb8.md) → [`006f0cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f0/006f0cb8.md) FUN_006f0cb8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009a311c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a3/009a311c.md) · 呼出先 23件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`009a311c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a3/009a311c.md) · 呼出先 23件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006f0f10",
      "incomplete_value": true,
      "site": "006f0f28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:993:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006f0f10",
      "incomplete_value": true,
      "site": "006f0f28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:908:8"
              ]
            ]
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
      "definition_site": "006f111c",
      "incomplete_value": true,
      "site": "006f1130",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:812:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006f111c",
      "incomplete_value": true,
      "site": "006f1130",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:814:8"
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
      "definition_site": "006f1120",
      "incomplete_value": true,
      "site": "006f1134",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "006f1120",
      "incomplete_value": true,
      "site": "006f1134",
      "value": [
        "LOAD",
        "16",
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
      "006f0d08",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "006f0d20",
      "READ",
      [
        "storage",
        "00294cdb",
        null,
        "string"
      ]
    ],
    [
      "006f0f10",
      "READ",
      [
        "storage",
        "002a1908",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006f0d08",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "006f0d20",
      "READ",
      [
        "storage",
        "00294c4e",
        null,
        "string"
      ]
    ],
    [
      "006f0f10",
      "READ",
      [
        "storage",
        "002a1993",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006f0d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f0/006f0cb8.md#insn-006f0d00) · [`006f0d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f0/006f0cb8.md#insn-006f0d1c) · [`006f0f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f0/006f0cb8.md#insn-006f0f08)
- 新版 `006f0d00`（命令位置の公開資料なし） · `006f0d1c`（命令位置の公開資料なし） · `006f0f08`（命令位置の公開資料なし）

~~~diff
- 006f0d00 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 006f0d00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006f0d00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006f0d00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006f0d00 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 006f0d00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006f0d00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006f0d00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006f0d00 bytes 08a13491
+ 006f0d00 bytes 08e13591
- 006f0d1c ["COPY", "tmp:0:8", ["const:cdb:8"]]
- 006f0d1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006f0d1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006f0d1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006f0d1c ["COPY", "tmp:0:8", ["const:c4e:8"]]
+ 006f0d1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006f0d1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006f0d1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006f0d1c bytes 086d3391
+ 006f0d1c bytes 08393191
- 006f0f08 ["COPY", "tmp:0:8", ["const:908:8"]]
- 006f0f08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006f0f08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006f0f08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006f0f08 ["COPY", "tmp:0:8", ["const:993:8"]]
+ 006f0f08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006f0f08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006f0f08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006f0f08 bytes 29212491
+ 006f0f08 bytes 294d2691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e505aefd023f7f81c2021170af3e6a1"></a>

### [`006f1484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f1484.md) → [`006f1484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1484.md) FUN_006f1484

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006f0cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f0/006f0cb8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`006f0cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f0/006f0cb8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "006f1490",
      "incomplete_value": false,
      "site": "006f1494",
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
      "definition_site": "006f1490",
      "incomplete_value": false,
      "site": "006f1494",
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
      "006f1490",
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
      "006f1490",
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

- 旧版 [`006f1490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f1484.md#insn-006f1490)
- 新版 `006f1490`（命令位置の公開資料なし）

~~~diff
- 006f1490 ["COPY", "tmp:0:8", ["const:303:8"]]
- 006f1490 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006f1490 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006f1490 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006f1490 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 006f1490 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006f1490 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006f1490 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006f1490 bytes 000c0c91
+ 006f1490 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-251edec74066efe1bd9797a0734ed362"></a>

### [`006f1498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f1498.md) → [`006f1498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1498.md) _INIT_112

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
      "definition_site": "006f14f8",
      "incomplete_value": true,
      "site": "006f1514",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f14f8",
      "incomplete_value": true,
      "site": "006f1514",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f1518",
      "incomplete_value": true,
      "site": "006f1534",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f1518",
      "incomplete_value": true,
      "site": "006f1534",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f1538",
      "incomplete_value": true,
      "site": "006f1550",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f1538",
      "incomplete_value": true,
      "site": "006f1550",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "006f14d4",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "006f14f8",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "006f1518",
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
      "006f14d4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "006f14f8",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "006f1518",
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

- 旧版 [`006f14c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f1498.md#insn-006f14c4) · [`006f14cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f1498.md#insn-006f14cc)
- 新版 `006f14c4`（命令位置の公開資料なし） · `006f14cc`（命令位置の公開資料なし）

~~~diff
- 006f14c4 ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 006f14c4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006f14c4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006f14c4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006f14c4 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 006f14c4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006f14c4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006f14c4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006f14c4 bytes 73e23391
+ 006f14c4 bytes 73e23491
- 006f14cc ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 006f14cc bytes a9ddffd0
+ 006f14cc ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 006f14cc bytes a9ddffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b667beb99bc8ef3c220e0307f22a700"></a>

### [`006f1e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f1e2c.md) → [`006f1e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1e2c.md) FUN_006f1e2c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 60件 [`005c27f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c27f4.md) [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e8d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e8/005e8d4c.md) [`006015d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/006015d4.md) [`0060217c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/0060217c.md) · 呼出先 7件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`006f18c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f18c4.md) [`007dcdc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dc/007dcdc4.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a0b69c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0b/00a0b69c.md)
- 新版 呼出元 60件 [`005c27f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c27f4.md) [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e8d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e8/005e8d4c.md) [`006015d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006015d4.md) [`0060217c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/0060217c.md) · 呼出先 7件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`006f18c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f18c4.md) [`007dcdc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dc/007dcdc4.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a0b6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b6e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.70% / 新版 99.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006f236c",
      "incomplete_value": false,
      "site": "006f2370",
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
      "definition_site": "006f236c",
      "incomplete_value": false,
      "site": "006f2370",
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
    "ordinal": 29,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006f236c",
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
      "006f236c",
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

- 旧版 [`006f236c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f1e2c.md#insn-006f236c)
- 新版 `006f236c`（命令位置の公開資料なし）

~~~diff
- 006f236c ["COPY", "tmp:0:8", ["const:5cf:8"]]
- 006f236c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006f236c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006f236c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006f236c ["COPY", "tmp:0:8", ["const:65a:8"]]
+ 006f236c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006f236c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006f236c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006f236c bytes 003c1791
+ 006f236c bytes 00681991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-353e90a8a22199f76185efd4d6cb697b"></a>

### [`006f3154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f3/006f3154.md) → [`006f3154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f3154.md) FUN_006f3154

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`00625684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00625/00625684.md) [`006280a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00628/006280a4.md) [`0066ff48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066f/0066ff48.md) [`00672a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672a4c.md) [`006bf5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bf/006bf5a0.md) · 呼出先 17件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`005c3468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c3/005c3468.md) [`00670de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670de0.md) [`006f18c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f18c4.md) [`006f424c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f4/006f424c.md)
- 新版 呼出元 8件 [`00625684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00625/00625684.md) [`006280a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00628/006280a4.md) [`0066ff48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066ff48.md) [`00672a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672a4c.md) [`006bf5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bf/006bf5a0.md) · 呼出先 17件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`005c3468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c3/005c3468.md) [`00670de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670de0.md) [`006f18c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f18c4.md) [`006f424c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f424c.md)

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
      "definition_site": "006f4240",
      "incomplete_value": false,
      "site": "006f4244",
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
      "definition_site": "006f4240",
      "incomplete_value": false,
      "site": "006f4244",
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
    "ordinal": 148,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006f4240",
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
      "006f4240",
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

- 旧版 [`006f4240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f3/006f3154.md#insn-006f4240)
- 新版 `006f4240`（命令位置の公開資料なし）

~~~diff
- 006f4240 ["COPY", "tmp:0:8", ["const:5cf:8"]]
- 006f4240 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006f4240 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006f4240 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006f4240 ["COPY", "tmp:0:8", ["const:65a:8"]]
+ 006f4240 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006f4240 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006f4240 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006f4240 bytes 003c1791
+ 006f4240 bytes 00681991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a4852ce2f6ac72f4f5685163205cbd5"></a>

### [`006f5028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f5/006f5028.md) → [`006f5028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f5/006f5028.md) _INIT_113

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
      "definition_site": "006f50c8",
      "incomplete_value": true,
      "site": "006f50e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f50c8",
      "incomplete_value": true,
      "site": "006f50e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f50e4",
      "incomplete_value": true,
      "site": "006f5100",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f50e4",
      "incomplete_value": true,
      "site": "006f5100",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f5250",
      "incomplete_value": false,
      "site": "006f525c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c27000:8"
          ],
          [
            "leaf",
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006f5250",
      "incomplete_value": false,
      "site": "006f525c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c27000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "006f5064",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "006f5088",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "006f50a8",
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
      "006f5064",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "006f5088",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "006f50a8",
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

- 旧版 [`006f5054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f5/006f5028.md#insn-006f5054) · [`006f505c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f5/006f5028.md#insn-006f505c)
- 新版 `006f5054`（命令位置の公開資料なし） · `006f505c`（命令位置の公開資料なし）

~~~diff
- 006f5054 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 006f5054 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006f5054 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006f5054 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006f5054 ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 006f5054 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006f5054 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006f5054 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006f5054 bytes 73423491
+ 006f5054 bytes 73423591
- 006f505c ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 006f505c bytes 89ddffd0
+ 006f505c ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 006f505c bytes 89ddffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb8b1649f21877e1b399ef8eb4779d45"></a>

### [`006f5538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f5/006f5538.md) → [`006f5538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f5/006f5538.md) _INIT_114

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
      "definition_site": "006f55b8",
      "incomplete_value": true,
      "site": "006f55d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f55b8",
      "incomplete_value": true,
      "site": "006f55d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006f5760",
      "incomplete_value": false,
      "site": "006f576c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c27000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006f5760",
      "incomplete_value": false,
      "site": "006f576c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c27000:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006f5768",
      "incomplete_value": false,
      "site": "006f576c",
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
      "definition_site": "006f5768",
      "incomplete_value": false,
      "site": "006f576c",
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
      "006f5574",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "006f5598",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "006f55b8",
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
      "006f5574",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "006f5598",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "006f55b8",
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

- 旧版 [`006f5564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f5/006f5538.md#insn-006f5564) · [`006f556c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f5/006f5538.md#insn-006f556c)
- 新版 `006f5564`（命令位置の公開資料なし） · `006f556c`（命令位置の公開資料なし）

~~~diff
- 006f5564 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 006f5564 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006f5564 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006f5564 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006f5564 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 006f5564 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006f5564 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006f5564 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006f5564 bytes 73a23491
+ 006f5564 bytes 73a23591
- 006f556c ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 006f556c bytes 89ddffd0
+ 006f556c ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 006f556c bytes 89ddffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-308487d33ab5b774707a774694c40cd4"></a>

### [`006f58c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f5/006f58c8.md) → [`006f58c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f5/006f58c8.md) _INIT_115

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006f5904",
      "incomplete_value": true,
      "site": "006f5920",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f5904",
      "incomplete_value": true,
      "site": "006f5920",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f5928",
      "incomplete_value": true,
      "site": "006f5944",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f5928",
      "incomplete_value": true,
      "site": "006f5944",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f5948",
      "incomplete_value": true,
      "site": "006f5964",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f5948",
      "incomplete_value": true,
      "site": "006f5964",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "006f5904",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "006f5928",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "006f5948",
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
      "006f5904",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "006f5928",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "006f5948",
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

- 旧版 [`006f58f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f5/006f58c8.md#insn-006f58f4) · [`006f58fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f5/006f58c8.md#insn-006f58fc)
- 新版 `006f58f4`（命令位置の公開資料なし） · `006f58fc`（命令位置の公開資料なし）

~~~diff
- 006f58f4 ["COPY", "tmp:0:8", ["const:d40:8"]]
- 006f58f4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006f58f4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006f58f4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006f58f4 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 006f58f4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006f58f4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006f58f4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006f58f4 bytes 73023591
+ 006f58f4 bytes 73023691
- 006f58fc ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 006f58fc bytes 89ddffd0
+ 006f58fc ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 006f58fc bytes 89ddffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79720d1ff8ffb93e36b2c8047424548e"></a>

### [`006f5c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f5/006f5c58.md) → [`006f5c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f5/006f5c58.md) _INIT_116

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
      "definition_site": "006f5c94",
      "incomplete_value": true,
      "site": "006f5cb0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f5c94",
      "incomplete_value": true,
      "site": "006f5cb0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f5cb8",
      "incomplete_value": true,
      "site": "006f5cd4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f5cb8",
      "incomplete_value": true,
      "site": "006f5cd4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f5cf8",
      "incomplete_value": true,
      "site": "006f5d10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006f5cf8",
      "incomplete_value": true,
      "site": "006f5d10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "006f5c94",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "006f5cb8",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "006f5cd8",
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
      "006f5c94",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "006f5cb8",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "006f5cd8",
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

- 旧版 [`006f5c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f5/006f5c58.md#insn-006f5c84) · [`006f5c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f5/006f5c58.md#insn-006f5c8c)
- 新版 `006f5c84`（命令位置の公開資料なし） · `006f5c8c`（命令位置の公開資料なし）

~~~diff
- 006f5c84 ["COPY", "tmp:0:8", ["const:d58:8"]]
- 006f5c84 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006f5c84 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006f5c84 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006f5c84 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 006f5c84 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006f5c84 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006f5c84 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006f5c84 bytes 73623591
+ 006f5c84 bytes 73623691
- 006f5c8c ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 006f5c8c bytes 89ddffd0
+ 006f5c8c ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 006f5c8c bytes 89ddffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1032e37194dc367bad0eb68a7c31285c"></a>

### [`006f5fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f5/006f5fe8.md) → [`006f5fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f5/006f5fe8.md) FUN_006f5fe8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 49件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`0044aa9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aa9c.md) [`0044b660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b660.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 49件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044aa9c.md) [`0044b660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b660.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 96.65% / 新版 96.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 44件, `store_destination` 14件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006f8828",
      "incomplete_value": false,
      "site": "006f8828",
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
      "definition_site": "006f8828",
      "incomplete_value": false,
      "site": "006f8828",
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
    "ordinal": 283,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006f882c",
      "incomplete_value": false,
      "site": "006f882c",
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
      "definition_site": "006f882c",
      "incomplete_value": false,
      "site": "006f882c",
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
    "ordinal": 284,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006f8828",
      "incomplete_value": false,
      "site": "006f882c",
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
      "definition_site": "006f8828",
      "incomplete_value": false,
      "site": "006f882c",
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
    "ordinal": 284,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006f61dc",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "006f61f4",
      "PARAM",
      [
        "storage",
        "00c250d8",
        null,
        "undefined1"
      ]
    ],
    [
      "006f6224",
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
      "006f61dc",
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "006f61f4",
      "PARAM",
      [
        "storage",
        "00c25118",
        null,
        "undefined1"
      ]
    ],
    [
      "006f6224",
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

- 旧版 [`006f61dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f5/006f5fe8.md#insn-006f61dc) · [`006f625c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f5/006f5fe8.md#insn-006f625c) · [`006f627c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f5/006f5fe8.md#insn-006f627c)
- 新版 `006f61dc`（命令位置の公開資料なし） · `006f625c`（命令位置の公開資料なし） · `006f627c`（命令位置の公開資料なし）

~~~diff
- 006f61dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e60:8"]]
- 006f61dc ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 006f61dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:eb0:8"]]
+ 006f61dc ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 006f61dc bytes b53247f9
+ 006f61dc bytes b55a47f9
- 006f625c ["COPY", "tmp:0:8", ["const:38:8"]]
- 006f625c ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 006f625c ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 006f625c ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 006f625c ["COPY", "tmp:0:8", ["const:78:8"]]
+ 006f625c ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 006f625c ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 006f625c ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 006f625c bytes 39e30091
+ 006f625c bytes 39e30191
- 006f627c ["COPY", "tmp:0:8", ["const:0:8"]]
- 006f627c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 006f627c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 006f627c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 006f627c ["COPY", "tmp:0:8", ["const:40:8"]]
+ 006f627c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 006f627c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 006f627c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 006f627c bytes b5020091
+ 006f627c bytes b5020191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed4b2fe28751b11b781f0f8e5261b846"></a>

### [`006fa320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fa/006fa320.md) → [`006fa320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fa/006fa320.md) _INIT_117

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006fa380",
      "incomplete_value": true,
      "site": "006fa39c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006fa380",
      "incomplete_value": true,
      "site": "006fa39c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006fa3a0",
      "incomplete_value": true,
      "site": "006fa3bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006fa3a0",
      "incomplete_value": true,
      "site": "006fa3bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006fa3dc",
      "incomplete_value": true,
      "site": "006fa3f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006fa3dc",
      "incomplete_value": true,
      "site": "006fa3f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "006fa35c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "006fa380",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "006fa3a0",
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
      "006fa35c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "006fa380",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "006fa3a0",
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

- 旧版 [`006fa34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fa/006fa320.md#insn-006fa34c) · [`006fa358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fa/006fa320.md#insn-006fa358) · [`006fa374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fa/006fa320.md#insn-006fa374)
- 新版 `006fa34c`（命令位置の公開資料なし） · `006fa358`（命令位置の公開資料なし） · `006fa374`（命令位置の公開資料なし）

~~~diff
- 006fa34c ["COPY", "tmp:0:8", ["const:d70:8"]]
- 006fa34c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006fa34c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006fa34c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006fa34c ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 006fa34c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006fa34c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006fa34c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006fa34c bytes 73c23591
+ 006fa34c bytes 73c23691
- 006fa358 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 006fa358 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006fa358 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006fa358 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006fa358 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 006fa358 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006fa358 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006fa358 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006fa358 bytes 29750b91
+ 006fa358 bytes 29dd0d91
- 006fa374 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 006fa374 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 006fa374 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 006fa374 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006fa374 ["COPY", "tmp:0:8", ["const:38a:8"]]
+ 006fa374 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006fa374 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006fa374 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 006fa374 bytes 4ac10b91
+ 006fa374 bytes 4a290e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02c30e3862f9dc575e445e9f4f90b798"></a>

### [`006fa6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fa/006fa6b0.md) → [`006fa6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fa/006fa6b0.md) FUN_006fa6b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 21件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 21件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.54% / 新版 95.54%

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
      "definition_site": "006fa6f4",
      "incomplete_value": false,
      "site": "006fa700",
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
      "definition_site": "006fa6f4",
      "incomplete_value": false,
      "site": "006fa700",
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
      "definition_site": "006fa7e8",
      "incomplete_value": true,
      "site": "006fa7f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:991:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fa7e8",
      "incomplete_value": true,
      "site": "006fa7f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:982:8"
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
      "definition_site": "006faed8",
      "incomplete_value": true,
      "site": "006faee4",
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
      "definition_site": "006faed8",
      "incomplete_value": true,
      "site": "006faee4",
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
    "ordinal": 99,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fa700",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "006fa7e8",
      "READ",
      [
        "storage",
        "002a9982",
        null,
        "string"
      ]
    ],
    [
      "006fa88c",
      "READ",
      [
        "storage",
        "002a784f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006fa700",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "006fa7e8",
      "READ",
      [
        "storage",
        "002a9991",
        null,
        "string"
      ]
    ],
    [
      "006fa88c",
      "READ",
      [
        "storage",
        "002a78e9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fa6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fa/006fa6b0.md#insn-006fa6f4) · [`006fa7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fa/006fa6b0.md#insn-006fa7e0) · [`006fa884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fa/006fa6b0.md#insn-006fa884)
- 新版 `006fa6f4`（命令位置の公開資料なし） · `006fa7e0`（命令位置の公開資料なし） · `006fa884`（命令位置の公開資料なし）

~~~diff
- 006fa6f4 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 006fa6f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fa6f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fa6f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fa6f4 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 006fa6f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fa6f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fa6f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fa6f4 bytes 08a13491
+ 006fa6f4 bytes 08e13591
- 006fa7e0 ["COPY", "tmp:0:8", ["const:982:8"]]
- 006fa7e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006fa7e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006fa7e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006fa7e0 ["COPY", "tmp:0:8", ["const:991:8"]]
+ 006fa7e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006fa7e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006fa7e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006fa7e0 bytes 29092691
+ 006fa7e0 bytes 29452691
- 006fa884 ["COPY", "tmp:0:8", ["const:84f:8"]]
- 006fa884 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 006fa884 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 006fa884 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 006fa884 ["COPY", "tmp:0:8", ["const:8e9:8"]]
+ 006fa884 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 006fa884 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 006fa884 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 006fa884 bytes 6b3d2191
+ 006fa884 bytes 6ba52391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41e2499ccd49fe4bcc6fb816b4896ad5"></a>

### [`006fbf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fb/006fbf4c.md) → [`006fbf4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fb/006fbf4c.md) FUN_006fbf4c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`006fbd74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fb/006fbd74.md) [`00751cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/00751cec.md) [`009dbd20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009db/009dbd20.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`006fbd74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fb/006fbd74.md) [`00751cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751cec.md) [`009dbd64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009db/009dbd64.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "006fbf58",
      "incomplete_value": false,
      "site": "006fbf5c",
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
      "definition_site": "006fbf58",
      "incomplete_value": false,
      "site": "006fbf5c",
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
      "006fbf58",
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
      "006fbf58",
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

- 旧版 [`006fbf58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fb/006fbf4c.md#insn-006fbf58)
- 新版 `006fbf58`（命令位置の公開資料なし）

~~~diff
- 006fbf58 ["COPY", "tmp:0:8", ["const:303:8"]]
- 006fbf58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006fbf58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006fbf58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006fbf58 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 006fbf58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006fbf58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006fbf58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006fbf58 bytes 000c0c91
+ 006fbf58 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-662750f5db0490de2d4ea4307a629471"></a>

### [`006fc120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fc/006fc120.md) → [`006fc120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fc/006fc120.md) FUN_006fc120

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`006fbfc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fb/006fbfc4.md) [`007520b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/007520b8.md) [`009dbb8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009db/009dbb8c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`006fbfc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fb/006fbfc4.md) [`007520b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007520b8.md) [`009dbbd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009db/009dbbd0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "006fc12c",
      "incomplete_value": false,
      "site": "006fc130",
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
      "definition_site": "006fc12c",
      "incomplete_value": false,
      "site": "006fc130",
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
      "006fc12c",
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
      "006fc12c",
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

- 旧版 [`006fc12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fc/006fc120.md#insn-006fc12c)
- 新版 `006fc12c`（命令位置の公開資料なし）

~~~diff
- 006fc12c ["COPY", "tmp:0:8", ["const:303:8"]]
- 006fc12c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006fc12c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006fc12c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006fc12c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 006fc12c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006fc12c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006fc12c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006fc12c bytes 000c0c91
+ 006fc12c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d028bab07df8fe686c7c9e5d40189217"></a>

### [`006fc2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fc/006fc2f0.md) → [`006fc2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fc/006fc2f0.md) _INIT_118

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
      "definition_site": "006fc32c",
      "incomplete_value": true,
      "site": "006fc348",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006fc32c",
      "incomplete_value": true,
      "site": "006fc348",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006fc350",
      "incomplete_value": true,
      "site": "006fc36c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006fc350",
      "incomplete_value": true,
      "site": "006fc36c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006fc370",
      "incomplete_value": true,
      "site": "006fc38c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006fc370",
      "incomplete_value": true,
      "site": "006fc38c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "006fc32c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "006fc350",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "006fc370",
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
      "006fc32c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "006fc350",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "006fc370",
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

- 旧版 [`006fc31c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fc/006fc2f0.md#insn-006fc31c) · [`006fc324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fc/006fc2f0.md#insn-006fc324)
- 新版 `006fc31c`（命令位置の公開資料なし） · `006fc324`（命令位置の公開資料なし）

~~~diff
- 006fc31c ["COPY", "tmp:0:8", ["const:d88:8"]]
- 006fc31c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006fc31c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006fc31c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006fc31c ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 006fc31c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006fc31c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006fc31c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006fc31c bytes 73223691
+ 006fc31c bytes 73223791
- 006fc324 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 006fc324 bytes 49ddfff0
+ 006fc324 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 006fc324 bytes 49ddfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c936f5e38ed5b9b5bb04248ec8c69967"></a>

### [`006fc680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fc/006fc680.md) → [`006fc680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fc/006fc680.md) FUN_006fc680

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b28.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b28.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 95.50% / 新版 95.50%

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
      "definition_site": "006fc6c8",
      "incomplete_value": false,
      "site": "006fc6d8",
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
      "definition_site": "006fc6c8",
      "incomplete_value": false,
      "site": "006fc6d8",
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
      "definition_site": "006fcbf4",
      "incomplete_value": true,
      "site": "006fcc00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:82d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fcbf4",
      "incomplete_value": true,
      "site": "006fcc00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:82f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 91,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006fcbf8",
      "incomplete_value": true,
      "site": "006fcc04",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "006fcbf8",
      "incomplete_value": true,
      "site": "006fcc04",
      "value": [
        "LOAD",
        "16",
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
      "006fc6d8",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "006fc6ec",
      "READ",
      [
        "storage",
        "002991cd",
        null,
        "string"
      ]
    ],
    [
      "006fc6f4",
      "READ",
      [
        "storage",
        "002991d2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006fc6d8",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "006fc6ec",
      "READ",
      [
        "storage",
        "00299140",
        null,
        "string"
      ]
    ],
    [
      "006fc6f4",
      "READ",
      [
        "storage",
        "00299145",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fc6c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fc/006fc680.md#insn-006fc6c8) · [`006fc6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fc/006fc680.md#insn-006fc6e8) · [`006fcbec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fc/006fc680.md#insn-006fcbec)
- 新版 `006fc6c8`（命令位置の公開資料なし） · `006fc6e8`（命令位置の公開資料なし） · `006fcbec`（命令位置の公開資料なし）

~~~diff
- 006fc6c8 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 006fc6c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fc6c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fc6c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fc6c8 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 006fc6c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fc6c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fc6c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fc6c8 bytes 08a13491
+ 006fc6c8 bytes 08e13591
- 006fc6e8 ["COPY", "tmp:0:8", ["const:1cd:8"]]
- 006fc6e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006fc6e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006fc6e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006fc6e8 ["COPY", "tmp:0:8", ["const:140:8"]]
+ 006fc6e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006fc6e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006fc6e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006fc6e8 bytes 29350791
+ 006fc6e8 bytes 29010591
- 006fcbec ["COPY", "tmp:0:8", ["const:82f:8"]]
- 006fcbec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fcbec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fcbec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fcbec ["COPY", "tmp:0:8", ["const:82d:8"]]
+ 006fcbec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fcbec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fcbec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fcbec bytes 08bd2091
+ 006fcbec bytes 08b52091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb12168573ae879635216a00fb2254bb"></a>

### [`006fd500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fd500.md) → [`006fd500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd500.md) _INIT_119

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
      "definition_site": "006fd53c",
      "incomplete_value": true,
      "site": "006fd558",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006fd53c",
      "incomplete_value": true,
      "site": "006fd558",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006fd560",
      "incomplete_value": true,
      "site": "006fd57c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006fd560",
      "incomplete_value": true,
      "site": "006fd57c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006fd5a0",
      "incomplete_value": true,
      "site": "006fd5b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006fd5a0",
      "incomplete_value": true,
      "site": "006fd5b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "006fd53c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "006fd560",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "006fd580",
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
      "006fd53c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "006fd560",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "006fd580",
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

- 旧版 [`006fd52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fd500.md#insn-006fd52c) · [`006fd534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fd500.md#insn-006fd534)
- 新版 `006fd52c`（命令位置の公開資料なし） · `006fd534`（命令位置の公開資料なし）

~~~diff
- 006fd52c ["COPY", "tmp:0:8", ["const:da0:8"]]
- 006fd52c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006fd52c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006fd52c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006fd52c ["COPY", "tmp:0:8", ["const:de0:8"]]
+ 006fd52c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006fd52c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006fd52c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006fd52c bytes 73823691
+ 006fd52c bytes 73823791
- 006fd534 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 006fd534 bytes 49ddffd0
+ 006fd534 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 006fd534 bytes 49ddffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08edf20ad7504b517b27b70d4e1d02a7"></a>

### [`006fdfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fdfc0.md) → [`006fdfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdfc0.md) FUN_006fdfc0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 17件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 17件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.90% / 新版 93.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 3件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fe004",
      "incomplete_value": false,
      "site": "006fe008",
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
      "definition_site": "006fe004",
      "incomplete_value": false,
      "site": "006fe008",
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006fe048",
      "incomplete_value": false,
      "site": "006fe048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c27000:8"
          ],
          [
            "leaf",
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe048",
      "incomplete_value": false,
      "site": "006fe048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c27000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006fe050",
      "incomplete_value": false,
      "site": "006fe050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c27000:8"
          ],
          [
            "leaf",
            "const:e14:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe050",
      "incomplete_value": false,
      "site": "006fe050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c27000:8"
          ],
          [
            "leaf",
            "const:dd4:8"
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
      "006fe008",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "006fe048",
      "WRITE",
      [
        "storage",
        "00c27dd0",
        null,
        "undefined4"
      ]
    ],
    [
      "006fe050",
      "WRITE",
      [
        "storage",
        "00c27dd4",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "006fe008",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "006fe048",
      "WRITE",
      [
        "storage",
        "00c27e10",
        null,
        "undefined4"
      ]
    ],
    [
      "006fe050",
      "WRITE",
      [
        "storage",
        "00c27e14",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fdfc0.md#insn-006fe048) · [`006fe050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fdfc0.md#insn-006fe050) · [`006fe004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fdfc0.md#insn-006fe004)
- 新版 `006fe048`（命令位置の公開資料なし） · `006fe050`（命令位置の公開資料なし） · `006fe004`（命令位置の公開資料なし）

~~~diff
- 006fe048 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 006fe048 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 006fe048 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
+ 006fe048 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 006fe048 bytes 09d10db9
+ 006fe048 bytes 09110eb9
- 006fe050 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:dd4:8"]]
- 006fe050 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 006fe050 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e14:8"]]
+ 006fe050 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 006fe050 bytes 49d50db9
+ 006fe050 bytes 49150eb9
- 006fe004 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 006fe004 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006fe004 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006fe004 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006fe004 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 006fe004 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006fe004 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006fe004 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006fe004 bytes 29a13491
+ 006fe004 bytes 29e13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27166213631b1f64ddf9e2e724254766"></a>

### [`006fefc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fe/006fefc8.md) → [`006fefc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fefc8.md) FUN_006fefc8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00734830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/00734830.md) [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) [`00996eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00996/00996eec.md) · 呼出先 23件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abe4.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md)
- 新版 呼出元 3件 [`00734830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/00734830.md) [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`00996eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996eec.md) · 呼出先 23件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044abe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abe4.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.15% / 新版 97.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006ff430",
      "incomplete_value": true,
      "site": "006ff440",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:14e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ff430",
      "incomplete_value": true,
      "site": "006ff440",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1db:8"
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
      "definition_site": "006ff444",
      "incomplete_value": true,
      "site": "006ff444",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006ff444",
      "incomplete_value": true,
      "site": "006ff444",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006ff304",
      "incomplete_value": true,
      "site": "006ff304",
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
      "definition_site": "006ff304",
      "incomplete_value": true,
      "site": "006ff304",
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
    "ordinal": 28,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ff300",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006ff30c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006ff314",
      "PARAM",
      [
        "storage",
        "00bfa490",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006ff300",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006ff30c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006ff314",
      "PARAM",
      [
        "storage",
        "00bfa4e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ff228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fe/006fefc8.md#insn-006ff228) · [`006ff22c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fe/006fefc8.md#insn-006ff22c)
- 新版 `006ff228`（命令位置の公開資料なし） · `006ff22c`（命令位置の公開資料なし）

~~~diff
- 006ff228 ["COPY", "tmp:0:8", ["const:38:8"]]
- 006ff228 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 006ff228 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 006ff228 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 006ff228 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 006ff228 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 006ff228 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 006ff228 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 006ff228 bytes 39e30091
+ 006ff228 bytes 39e30191
- 006ff22c ["COPY", "register:40a8:8", ["const:c25000:8"]]
- 006ff22c bytes 352900d0
+ 006ff22c ["COPY", "register:40a8:8", ["const:c25000:8"]]
+ 006ff22c bytes 352900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e84ad89c5c80dda5f9fdd132e2d0c069"></a>

### [`006ff964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ff/006ff964.md) → [`006ff964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ff/006ff964.md) FUN_006ff964

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00749514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00749/00749514.md) [`0075d8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075d/0075d8a0.md) · 呼出先 2件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)
- 新版 呼出元 2件 [`00749514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/00749514.md) [`0075d8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d8a0.md) · 呼出先 2件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006ff980",
      "incomplete_value": true,
      "site": "006ff980",
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
      "definition_site": "006ff980",
      "incomplete_value": true,
      "site": "006ff980",
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
      "definition_site": "006ff988",
      "incomplete_value": false,
      "site": "006ff99c",
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
      "definition_site": "006ff988",
      "incomplete_value": false,
      "site": "006ff99c",
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
      "definition_site": "006ff990",
      "incomplete_value": false,
      "site": "006ff99c",
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
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ff990",
      "incomplete_value": false,
      "site": "006ff99c",
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
            "const:490:8"
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
      "006ff97c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006ff988",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006ff990",
      "PARAM",
      [
        "storage",
        "00bfa490",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006ff97c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006ff988",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006ff990",
      "PARAM",
      [
        "storage",
        "00bfa4e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ff97c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ff/006ff964.md#insn-006ff97c) · [`006ff988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ff/006ff964.md#insn-006ff988) · [`006ff990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ff/006ff964.md#insn-006ff990)
- 新版 `006ff97c`（命令位置の公開資料なし） · `006ff988`（命令位置の公開資料なし） · `006ff990`（命令位置の公開資料なし）

~~~diff
- 006ff97c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006ff97c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006ff97c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 006ff97c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006ff97c bytes 083d45f9
+ 006ff97c bytes 085d45f9
- 006ff988 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 006ff988 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006ff988 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006ff988 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006ff988 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 006ff988 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006ff988 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006ff988 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006ff988 bytes 21203991
+ 006ff988 bytes 21603a91
- 006ff990 ["COPY", "tmp:0:8", ["const:490:8"]]
- 006ff990 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006ff990 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006ff990 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006ff990 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 006ff990 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006ff990 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006ff990 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006ff990 bytes 42401291
+ 006ff990 bytes 42801391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf700913dbad93c1b5c37bdb3f8a1cf2"></a>

### [`00702374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00702/00702374.md) → [`00702374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/00702374.md) _INIT_120

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.01% / 新版 87.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007023b0",
      "incomplete_value": true,
      "site": "007023cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007023b0",
      "incomplete_value": true,
      "site": "007023cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007023d4",
      "incomplete_value": true,
      "site": "007023f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007023d4",
      "incomplete_value": true,
      "site": "007023f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007023f4",
      "incomplete_value": true,
      "site": "00702410",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007023f4",
      "incomplete_value": true,
      "site": "00702410",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "007023b0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "007023d4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "007023f4",
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
      "007023b0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "007023d4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "007023f4",
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

- 旧版 [`007023a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00702/00702374.md#insn-007023a0) · [`007023a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00702/00702374.md#insn-007023a8)
- 新版 `007023a0`（命令位置の公開資料なし） · `007023a8`（命令位置の公開資料なし）

~~~diff
- 007023a0 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 007023a0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 007023a0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 007023a0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 007023a0 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 007023a0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 007023a0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 007023a0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 007023a0 bytes 73e23691
+ 007023a0 bytes 73e23791
- 007023a8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 007023a8 bytes 29ddffb0
+ 007023a8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 007023a8 bytes 29ddffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5736b5e737e54e24d9d2ac6b0dd8a6d"></a>

### [`007028d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00702/007028d0.md) → [`007028d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/007028d0.md) FUN_007028d0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 25件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 25件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.64% / 新版 98.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00702924",
      "incomplete_value": false,
      "site": "0070292c",
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
      "definition_site": "00702924",
      "incomplete_value": false,
      "site": "0070292c",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00702958",
      "incomplete_value": true,
      "site": "00702958",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:824:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00702958",
      "incomplete_value": true,
      "site": "00702958",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:799:8"
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
      "definition_site": "00702954",
      "incomplete_value": true,
      "site": "0070295c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00702954",
      "incomplete_value": true,
      "site": "0070295c",
      "value": [
        "LOAD",
        "8",
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
      "0070292c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00702940",
      "READ",
      [
        "storage",
        "002a3799",
        null,
        "string"
      ]
    ],
    [
      "00702954",
      "READ",
      [
        "storage",
        "002a37a0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0070292c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00702940",
      "READ",
      [
        "storage",
        "002a3824",
        null,
        "string"
      ]
    ],
    [
      "00702954",
      "READ",
      [
        "storage",
        "002a382b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00702924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00702/007028d0.md#insn-00702924) · [`0070293c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00702/007028d0.md#insn-0070293c) · [`0070334c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00702/007028d0.md#insn-0070334c)
- 新版 `00702924`（命令位置の公開資料なし） · `0070293c`（命令位置の公開資料なし） · `0070334c`（命令位置の公開資料なし）

~~~diff
- 00702924 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00702924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00702924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00702924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00702924 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00702924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00702924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00702924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00702924 bytes 08a13491
+ 00702924 bytes 08e13591
- 0070293c ["COPY", "tmp:0:8", ["const:799:8"]]
- 0070293c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0070293c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0070293c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0070293c ["COPY", "tmp:0:8", ["const:824:8"]]
+ 0070293c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0070293c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0070293c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0070293c bytes 29651e91
+ 0070293c bytes 29912091
- 0070334c ["COPY", "tmp:0:8", ["const:750:8"]]
- 0070334c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0070334c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0070334c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0070334c ["COPY", "tmp:0:8", ["const:7db:8"]]
+ 0070334c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0070334c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0070334c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0070334c bytes 29411d91
+ 0070334c bytes 296d1f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30afb1e7524906b76c614d3be85b5b07"></a>

### [`00707840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/00707840.md) → [`00707840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/00707840.md) FUN_00707840

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007028d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00702/007028d0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`007028d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/007028d0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0070784c",
      "incomplete_value": false,
      "site": "00707850",
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
      "definition_site": "0070784c",
      "incomplete_value": false,
      "site": "00707850",
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
      "0070784c",
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
      "0070784c",
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

- 旧版 [`0070784c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/00707840.md#insn-0070784c)
- 新版 `0070784c`（命令位置の公開資料なし）

~~~diff
- 0070784c ["COPY", "tmp:0:8", ["const:303:8"]]
- 0070784c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0070784c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0070784c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0070784c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0070784c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0070784c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0070784c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0070784c bytes 000c0c91
+ 0070784c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d968167fdf2c4aba3b3af42ca9ea6b9"></a>

### [`00707854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/00707854.md) → [`00707854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/00707854.md) FUN_00707854

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007028d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00702/007028d0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`007028d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/007028d0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00707860",
      "incomplete_value": false,
      "site": "00707864",
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
      "definition_site": "00707860",
      "incomplete_value": false,
      "site": "00707864",
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
      "00707860",
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
      "00707860",
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

- 旧版 [`00707860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/00707854.md#insn-00707860)
- 新版 `00707860`（命令位置の公開資料なし）

~~~diff
- 00707860 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00707860 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00707860 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00707860 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00707860 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00707860 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00707860 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00707860 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00707860 bytes 000c0c91
+ 00707860 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c2ff4effeb24eb66a2b0f5b91a1b9ac"></a>

### [`0070792c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/0070792c.md) → [`0070792c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/0070792c.md) FUN_0070792c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007028d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00702/007028d0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`007028d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/007028d0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00707938",
      "incomplete_value": false,
      "site": "0070793c",
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
      "definition_site": "00707938",
      "incomplete_value": false,
      "site": "0070793c",
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
      "00707938",
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
      "00707938",
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

- 旧版 [`00707938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/0070792c.md#insn-00707938)
- 新版 `00707938`（命令位置の公開資料なし）

~~~diff
- 00707938 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00707938 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00707938 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00707938 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00707938 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00707938 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00707938 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00707938 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00707938 bytes 000c0c91
+ 00707938 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-734ee6d6c085764f3f4d6b2a8ec96d71"></a>

### [`00707990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/00707990.md) → [`00707990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/00707990.md) FUN_00707990

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00704be8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00704/00704be8.md) [`00705098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00705/00705098.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00704be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00704/00704be8.md) [`00705098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00705/00705098.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0070799c",
      "incomplete_value": false,
      "site": "007079a0",
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
      "definition_site": "0070799c",
      "incomplete_value": false,
      "site": "007079a0",
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
      "0070799c",
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
      "0070799c",
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

- 旧版 [`0070799c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/00707990.md#insn-0070799c)
- 新版 `0070799c`（命令位置の公開資料なし）

~~~diff
- 0070799c ["COPY", "tmp:0:8", ["const:303:8"]]
- 0070799c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0070799c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0070799c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0070799c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0070799c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0070799c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0070799c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0070799c bytes 000c0c91
+ 0070799c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07410a7e9ee45fdfb3387ddd64bd8a39"></a>

### [`007079a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/007079a4.md) → [`007079a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007079a4.md) FUN_007079a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00706bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00706/00706bbc.md) [`00706c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00706/00706c3c.md) [`007071e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/007071e8.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 3件 [`00706bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00706/00706bbc.md) [`00706c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00706/00706c3c.md) [`007071e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007071e8.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "007079b0",
      "incomplete_value": false,
      "site": "007079b4",
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
      "definition_site": "007079b0",
      "incomplete_value": false,
      "site": "007079b4",
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
      "007079b0",
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
      "007079b0",
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

- 旧版 [`007079b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/007079a4.md#insn-007079b0)
- 新版 `007079b0`（命令位置の公開資料なし）

~~~diff
- 007079b0 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007079b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007079b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007079b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007079b0 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007079b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007079b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007079b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007079b0 bytes 000c0c91
+ 007079b0 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e279bfc57153c3245fda1249dd44d8c"></a>

### [`007079b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/007079b8.md) → [`007079b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007079b8.md) FUN_007079b8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0070276c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00702/0070276c.md) [`007027d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00702/007027d4.md) [`00705098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00705/00705098.md) [`007059c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00705/007059c8.md) [`00706234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00706/00706234.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 7件 [`0070276c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/0070276c.md) [`007027d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/007027d4.md) [`00705098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00705/00705098.md) [`007059c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00705/007059c8.md) [`00706234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00706/00706234.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "007079c4",
      "incomplete_value": false,
      "site": "007079c8",
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
      "definition_site": "007079c4",
      "incomplete_value": false,
      "site": "007079c8",
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
      "007079c4",
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
      "007079c4",
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

- 旧版 [`007079c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/007079b8.md#insn-007079c4)
- 新版 `007079c4`（命令位置の公開資料なし）

~~~diff
- 007079c4 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007079c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007079c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007079c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007079c4 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007079c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007079c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007079c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007079c4 bytes 000c0c91
+ 007079c4 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69cbf367daf7f4997b90d1b891b00294"></a>

### [`007079cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/007079cc.md) → [`007079cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007079cc.md) FUN_007079cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00706234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00706/00706234.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`00706234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00706/00706234.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "007079d8",
      "incomplete_value": false,
      "site": "007079dc",
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
      "definition_site": "007079d8",
      "incomplete_value": false,
      "site": "007079dc",
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
      "007079d8",
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
      "007079d8",
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

- 旧版 [`007079d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/007079cc.md#insn-007079d8)
- 新版 `007079d8`（命令位置の公開資料なし）

~~~diff
- 007079d8 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007079d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007079d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007079d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007079d8 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007079d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007079d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007079d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007079d8 bytes 000c0c91
+ 007079d8 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78e06a830b3e7bf5efe02db24eef6b97"></a>

### [`007079e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/007079e0.md) → [`007079e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007079e0.md) FUN_007079e0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00706234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00706/00706234.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`00706234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00706/00706234.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "007079ec",
      "incomplete_value": false,
      "site": "007079f0",
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
      "definition_site": "007079ec",
      "incomplete_value": false,
      "site": "007079f0",
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
      "007079ec",
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
      "007079ec",
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

- 旧版 [`007079ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/007079e0.md#insn-007079ec)
- 新版 `007079ec`（命令位置の公開資料なし）

~~~diff
- 007079ec ["COPY", "tmp:0:8", ["const:303:8"]]
- 007079ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007079ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007079ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007079ec ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007079ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007079ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007079ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007079ec bytes 000c0c91
+ 007079ec bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a70c9fbf4d5004ec34b1245d6d4d62a9"></a>

### [`007079f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/007079f4.md) → [`007079f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007079f4.md) _INIT_121

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00707a30",
      "incomplete_value": true,
      "site": "00707a4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00707a30",
      "incomplete_value": true,
      "site": "00707a4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00707a54",
      "incomplete_value": true,
      "site": "00707a70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00707a54",
      "incomplete_value": true,
      "site": "00707a70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00707a74",
      "incomplete_value": true,
      "site": "00707a90",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00707a74",
      "incomplete_value": true,
      "site": "00707a90",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00707a30",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00707a54",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00707a74",
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
      "00707a30",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00707a54",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00707a74",
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

- 旧版 [`00707a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/007079f4.md#insn-00707a20) · [`00707a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/007079f4.md#insn-00707a28)
- 新版 `00707a20`（命令位置の公開資料なし） · `00707a28`（命令位置の公開資料なし）

~~~diff
- 00707a20 ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 00707a20 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00707a20 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00707a20 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00707a20 ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 00707a20 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00707a20 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00707a20 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00707a20 bytes 73623791
+ 00707a20 bytes 73623891
- 00707a28 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00707a28 bytes 09ddff90
+ 00707a28 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00707a28 bytes 09ddff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49120837d2940b99db12096a45cc4842"></a>

### [`00707d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/00707d84.md) → [`00707d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/00707d84.md) FUN_00707d84

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00900ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900ae0.md) · 呼出先 4件 [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`00a6d884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d884.md) [`00a6dd44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6dd44.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 1件 [`00900ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900ae0.md) · 呼出先 4件 [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`00a6d8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d8c8.md) [`00a6dd88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dd88.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00707db0",
      "incomplete_value": false,
      "site": "00707db8",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00707db0",
      "incomplete_value": false,
      "site": "00707db8",
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
            "const:4b8:8"
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
      "00707db8",
      "DATA",
      [
        "storage",
        "00bfa4b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00707db8",
      "DATA",
      [
        "storage",
        "00bfa508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00707db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/00707d84.md#insn-00707db0)
- 新版 `00707db0`（命令位置の公開資料なし）

~~~diff
- 00707db0 ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 00707db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00707db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00707db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00707db0 ["COPY", "tmp:0:8", ["const:508:8"]]
+ 00707db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00707db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00707db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00707db0 bytes 08e11291
+ 00707db0 bytes 08211491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0252a2fb54cf63241c483eed6f1457ce"></a>

### [`00707e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/00707e2c.md) → [`00707e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/00707e2c.md) FUN_00707e2c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00a6d8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d8b4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00a6d8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d8f8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "00707e44",
      "incomplete_value": false,
      "site": "00707e48",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00707e44",
      "incomplete_value": false,
      "site": "00707e48",
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
            "const:4b8:8"
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
      "00707e48",
      "DATA",
      [
        "storage",
        "00bfa4b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00707e48",
      "DATA",
      [
        "storage",
        "00bfa508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00707e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/00707e2c.md#insn-00707e44)
- 新版 `00707e44`（命令位置の公開資料なし）

~~~diff
- 00707e44 ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 00707e44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00707e44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00707e44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00707e44 ["COPY", "tmp:0:8", ["const:508:8"]]
+ 00707e44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00707e44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00707e44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00707e44 bytes 08e11291
+ 00707e44 bytes 08211491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1c170ddf9e916358d20dd4f7d56cd01"></a>

### [`00707e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/00707e88.md) → [`00707e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/00707e88.md) FUN_00707e88

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00a6d8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d8b4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00a6d8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d8f8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00707ea0",
      "incomplete_value": false,
      "site": "00707ea4",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00707ea0",
      "incomplete_value": false,
      "site": "00707ea4",
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
            "const:4b8:8"
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
      "00707ea4",
      "DATA",
      [
        "storage",
        "00bfa4b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00707ea4",
      "DATA",
      [
        "storage",
        "00bfa508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00707ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/00707e88.md#insn-00707ea0)
- 新版 `00707ea0`（命令位置の公開資料なし）

~~~diff
- 00707ea0 ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 00707ea0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00707ea0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00707ea0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00707ea0 ["COPY", "tmp:0:8", ["const:508:8"]]
+ 00707ea0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00707ea0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00707ea0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00707ea0 bytes 08e11291
+ 00707ea0 bytes 08211491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3818ec4edeb50467d80c07693f317a01"></a>

### [`00707f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/00707f9c.md) → [`00707f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/00707f9c.md) _INIT_122

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
      "definition_site": "00707fd8",
      "incomplete_value": true,
      "site": "00707ff4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00707fd8",
      "incomplete_value": true,
      "site": "00707ff4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00708058",
      "incomplete_value": true,
      "site": "00708074",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00708058",
      "incomplete_value": true,
      "site": "00708074",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007081c4",
      "incomplete_value": true,
      "site": "007081d0",
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
            "const:e30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007081c4",
      "incomplete_value": true,
      "site": "007081d0",
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
            "const:df0:8"
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
      "00707fd8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00707ffc",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0070801c",
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
      "00707fd8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00707ffc",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0070801c",
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

- 旧版 [`00707fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/00707f9c.md#insn-00707fc8) · [`00707fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/00707f9c.md#insn-00707fd0)
- 新版 `00707fc8`（命令位置の公開資料なし） · `00707fd0`（命令位置の公開資料なし）

~~~diff
- 00707fc8 ["COPY", "tmp:0:8", ["const:df0:8"]]
- 00707fc8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00707fc8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00707fc8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00707fc8 ["COPY", "tmp:0:8", ["const:e30:8"]]
+ 00707fc8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00707fc8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00707fc8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00707fc8 bytes 73c23791
+ 00707fc8 bytes 73c23891
- 00707fd0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00707fd0 bytes 09ddff90
+ 00707fd0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00707fd0 bytes 09ddff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3067343d62fdb10dba8c3f955fc4065d"></a>

### [`0070832c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00708/0070832c.md) → [`0070832c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00708/0070832c.md) _INIT_123

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.53% / 新版 91.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007083e8",
      "incomplete_value": true,
      "site": "00708404",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007083e8",
      "incomplete_value": true,
      "site": "00708404",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "store_value",
    "new": {
      "definition_site": "00708428",
      "incomplete_value": true,
      "site": "0070846c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:526:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00708428",
      "incomplete_value": true,
      "site": "0070846c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5b3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00708554",
      "incomplete_value": false,
      "site": "00708560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c27000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00708554",
      "incomplete_value": false,
      "site": "00708560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c27000:8"
          ],
          [
            "leaf",
            "const:e08:8"
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
      "00708368",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0070838c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "007083ac",
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
      "00708368",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0070838c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "007083ac",
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

- 旧版 [`00708358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00708/0070832c.md#insn-00708358) · [`00708364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00708/0070832c.md#insn-00708364) · [`00708380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00708/0070832c.md#insn-00708380)
- 新版 `00708358`（命令位置の公開資料なし） · `00708364`（命令位置の公開資料なし） · `00708380`（命令位置の公開資料なし）

~~~diff
- 00708358 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 00708358 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00708358 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00708358 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00708358 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00708358 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00708358 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00708358 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00708358 bytes 73223891
+ 00708358 bytes 73223991
- 00708364 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00708364 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00708364 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00708364 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00708364 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00708364 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00708364 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00708364 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00708364 bytes 29750b91
+ 00708364 bytes 29dd0d91
- 00708380 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 00708380 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00708380 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00708380 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00708380 ["COPY", "tmp:0:8", ["const:38a:8"]]
+ 00708380 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00708380 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00708380 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00708380 bytes 4ac10b91
+ 00708380 bytes 4a290e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f86766cd28389aff45d11d81917dba68"></a>

### [`00708b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00708/00708b44.md) → [`00708b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00708/00708b44.md) FUN_00708b44

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`00796dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00796/00796dfc.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) [`007bdafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bdafc.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 7件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`00796dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00796/00796dfc.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) [`007bdafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bd/007bdafc.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "00708b68",
      "incomplete_value": false,
      "site": "00708b6c",
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
      "definition_site": "00708b68",
      "incomplete_value": false,
      "site": "00708b6c",
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
      "00708b68",
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
      "00708b68",
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

- 旧版 [`00708b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00708/00708b44.md#insn-00708b68)
- 新版 `00708b68`（命令位置の公開資料なし）

~~~diff
- 00708b68 ["COPY", "tmp:0:8", ["const:5cf:8"]]
- 00708b68 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00708b68 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00708b68 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00708b68 ["COPY", "tmp:0:8", ["const:65a:8"]]
+ 00708b68 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00708b68 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00708b68 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00708b68 bytes 003c1791
+ 00708b68 bytes 00681991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-616c2fd3e98f59680b68ff7d1ec6cbff"></a>

### [`00708b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00708/00708b70.md) → [`00708b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00708/00708b70.md) FUN_00708b70

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00708bb0",
      "incomplete_value": false,
      "site": "00708bb4",
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
      "definition_site": "00708bb0",
      "incomplete_value": false,
      "site": "00708bb4",
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
      "00708bb0",
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
      "00708bb0",
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

- 旧版 [`00708bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00708/00708b70.md#insn-00708bb0)
- 新版 `00708bb0`（命令位置の公開資料なし）

~~~diff
- 00708bb0 ["COPY", "tmp:0:8", ["const:5cf:8"]]
- 00708bb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00708bb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00708bb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00708bb0 ["COPY", "tmp:0:8", ["const:65a:8"]]
+ 00708bb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00708bb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00708bb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00708bb0 bytes 003c1791
+ 00708bb0 bytes 00681991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6db30b90bcd2007218f2fd41db2196d"></a>

### [`00709280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00709/00709280.md) → [`00709280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00709/00709280.md) FUN_00709280

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00708d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00708/00708d8c.md) [`00859898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859898.md) [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0046b1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b1e0.md) [`00709704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00709/00709704.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 3件 [`00708d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00708/00708d8c.md) [`00859898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0046b1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b1e0.md) [`00709704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00709/00709704.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.18% / 新版 97.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007092f0",
      "incomplete_value": false,
      "site": "007092fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:12c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007092f0",
      "incomplete_value": false,
      "site": "007092fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:12e:8"
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
      "definition_site": "0070938c",
      "incomplete_value": false,
      "site": "00709398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:12c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070938c",
      "incomplete_value": false,
      "site": "00709398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:12e:8"
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
      "definition_site": "00709444",
      "incomplete_value": false,
      "site": "00709450",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:12c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00709444",
      "incomplete_value": false,
      "site": "00709450",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:12e:8"
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
      "007092a8",
      "READ",
      [
        "storage",
        "00c1b740",
        null,
        "pointer"
      ]
    ],
    [
      "007092b4",
      "READ",
      [
        "storage",
        "00c28148",
        null,
        "undefined8"
      ]
    ],
    [
      "007092b4",
      "READ",
      [
        "storage",
        "00c28150",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "007092a8",
      "READ",
      [
        "storage",
        "00c1b790",
        null,
        "pointer"
      ]
    ],
    [
      "007092b4",
      "READ",
      [
        "storage",
        "00c28188",
        null,
        "undefined8"
      ]
    ],
    [
      "007092b4",
      "READ",
      [
        "storage",
        "00c28190",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007092a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00709/00709280.md#insn-007092a8) · [`007092f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00709/00709280.md#insn-007092f0) · [`0070938c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00709/00709280.md#insn-0070938c)
- 新版 `007092a8`（命令位置の公開資料なし） · `007092f0`（命令位置の公開資料なし） · `0070938c`（命令位置の公開資料なし）

~~~diff
- 007092a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:740:8"]]
- 007092a8 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 007092a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:790:8"]]
+ 007092a8 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 007092a8 bytes b5a243f9
+ 007092a8 bytes b5ca43f9
- 007092f0 ["COPY", "tmp:0:8", ["const:12e:8"]]
- 007092f0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007092f0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007092f0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007092f0 ["COPY", "tmp:0:8", ["const:12c:8"]]
+ 007092f0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007092f0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007092f0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007092f0 bytes 42b80491
+ 007092f0 bytes 42b00491
- 0070938c ["COPY", "tmp:0:8", ["const:12e:8"]]
- 0070938c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0070938c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0070938c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0070938c ["COPY", "tmp:0:8", ["const:12c:8"]]
+ 0070938c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0070938c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0070938c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0070938c bytes 42b80491
+ 0070938c bytes 42b00491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fa7a3558c086957e724a6ee016153ac"></a>

### [`007099b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00709/007099b8.md) → [`007099b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00709/007099b8.md) FUN_007099b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00859898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859898.md) · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0046b1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b1e0.md) [`00709d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00709/00709d24.md) [`00709e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00709/00709e04.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`00859898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0046b1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b1e0.md) [`00709d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00709/00709d24.md) [`00709e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00709/00709e04.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.35% / 新版 96.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00709a44",
      "incomplete_value": true,
      "site": "00709a50",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c28000:8"
              ],
              [
                "leaf",
                "const:188:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00709a44",
      "incomplete_value": true,
      "site": "00709a50",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c28000:8"
              ],
              [
                "leaf",
                "const:148:8"
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
      "definition_site": "00709a4c",
      "incomplete_value": true,
      "site": "00709a50",
      "value": [
        "INT_SRIGHT",
        "8",
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
            "const:2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00709a4c",
      "incomplete_value": true,
      "site": "00709a50",
      "value": [
        "INT_SRIGHT",
        "8",
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
            "const:2:8"
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
      "definition_site": "00709a78",
      "incomplete_value": false,
      "site": "00709a84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:12c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00709a78",
      "incomplete_value": false,
      "site": "00709a84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:12e:8"
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
      "00709a44",
      "READ",
      [
        "storage",
        "00c28148",
        null,
        "undefined8"
      ]
    ],
    [
      "00709a44",
      "READ",
      [
        "storage",
        "00c28150",
        null,
        "undefined8"
      ]
    ],
    [
      "00709a54",
      "READ",
      [
        "storage",
        "00c28150",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00709a44",
      "READ",
      [
        "storage",
        "00c28188",
        null,
        "undefined8"
      ]
    ],
    [
      "00709a44",
      "READ",
      [
        "storage",
        "00c28190",
        null,
        "undefined8"
      ]
    ],
    [
      "00709a54",
      "READ",
      [
        "storage",
        "00c28190",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00709a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00709/007099b8.md#insn-00709a3c) · [`00709a78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00709/007099b8.md#insn-00709a78) · [`00709b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00709/007099b8.md#insn-00709b38)
- 新版 `00709a3c`（命令位置の公開資料なし） · `00709a78`（命令位置の公開資料なし） · `00709b38`（命令位置の公開資料なし）

~~~diff
- 00709a3c ["COPY", "tmp:0:8", ["const:148:8"]]
- 00709a3c ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00709a3c ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00709a3c ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00709a3c ["COPY", "tmp:0:8", ["const:188:8"]]
+ 00709a3c ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00709a3c ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00709a3c ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00709a3c bytes d6220591
+ 00709a3c bytes d6220691
- 00709a78 ["COPY", "tmp:0:8", ["const:12e:8"]]
- 00709a78 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00709a78 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00709a78 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00709a78 ["COPY", "tmp:0:8", ["const:12c:8"]]
+ 00709a78 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00709a78 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00709a78 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00709a78 bytes 42b80491
+ 00709a78 bytes 42b00491
- 00709b38 ["COPY", "tmp:0:8", ["const:12e:8"]]
- 00709b38 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00709b38 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00709b38 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00709b38 ["COPY", "tmp:0:8", ["const:12c:8"]]
+ 00709b38 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00709b38 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00709b38 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00709b38 bytes 42b80491
+ 00709b38 bytes 42b00491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2266385c2b2c42074a999e546f0e31a"></a>

### [`00709f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00709/00709f30.md) → [`00709f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00709/00709f30.md) FUN_00709f30

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00708ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00708/00708ff4.md) [`0070d798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070d/0070d798.md) [`0070da24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070d/0070da24.md) [`0070f364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070f/0070f364.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0070a03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070a/0070a03c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 4件 [`00708ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00708/00708ff4.md) [`0070d798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070d/0070d798.md) [`0070da24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070d/0070da24.md) [`0070f364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070f/0070f364.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0070a03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070a/0070a03c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00709f54",
      "incomplete_value": true,
      "site": "00709f6c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00709f54",
      "incomplete_value": true,
      "site": "00709f6c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c65:8"
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
      "definition_site": "00709fa4",
      "incomplete_value": false,
      "site": "00709fb0",
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
            "const:8c5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00709fa4",
      "incomplete_value": false,
      "site": "00709fb0",
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
            "const:952:8"
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
      "00709f54",
      "READ",
      [
        "storage",
        "00293c65",
        null,
        "string"
      ]
    ],
    [
      "00709fa4",
      "PARAM",
      [
        "storage",
        "00297952",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00709f54",
      "READ",
      [
        "storage",
        "00293bd8",
        null,
        "string"
      ]
    ],
    [
      "00709fa4",
      "PARAM",
      [
        "storage",
        "002978c5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00709f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00709/00709f30.md#insn-00709f48) · [`00709fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00709/00709f30.md#insn-00709fa4)
- 新版 `00709f48`（命令位置の公開資料なし） · `00709fa4`（命令位置の公開資料なし）

~~~diff
- 00709f48 ["COPY", "tmp:0:8", ["const:c65:8"]]
- 00709f48 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00709f48 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00709f48 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00709f48 ["COPY", "tmp:0:8", ["const:bd8:8"]]
+ 00709f48 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00709f48 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00709f48 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00709f48 bytes 4a953191
+ 00709f48 bytes 4a612f91
- 00709fa4 ["COPY", "tmp:0:8", ["const:952:8"]]
- 00709fa4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00709fa4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00709fa4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00709fa4 ["COPY", "tmp:0:8", ["const:8c5:8"]]
+ 00709fa4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00709fa4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00709fa4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00709fa4 bytes 21482591
+ 00709fa4 bytes 21142391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae0103d4a736fc20b4ca1c1c8c279d3b"></a>

### [`0070af3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070a/0070af3c.md) → [`0070af3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070a/0070af3c.md) FUN_0070af3c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0059d12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d12c.md)
- 新版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0070afac",
      "incomplete_value": false,
      "site": "0070afb0",
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
      "definition_site": "0070afac",
      "incomplete_value": false,
      "site": "0070afb0",
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
      "0070afac",
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
      "0070afac",
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

- 旧版 [`0070afac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070a/0070af3c.md#insn-0070afac)
- 新版 `0070afac`（命令位置の公開資料なし）

~~~diff
- 0070afac ["COPY", "tmp:0:8", ["const:5cf:8"]]
- 0070afac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0070afac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0070afac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0070afac ["COPY", "tmp:0:8", ["const:65a:8"]]
+ 0070afac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0070afac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0070afac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0070afac bytes 003c1791
+ 0070afac bytes 00681991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c1c427cf4a5898da52d7d04de82a171"></a>

### [`0070afb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070a/0070afb4.md) → [`0070afb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070a/0070afb4.md) FUN_0070afb4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.77% / 新版 96.77%

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
      "definition_site": "0070b000",
      "incomplete_value": false,
      "site": "0070b008",
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
      "definition_site": "0070b000",
      "incomplete_value": false,
      "site": "0070b008",
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
      "definition_site": "0070b428",
      "incomplete_value": true,
      "site": "0070b42c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0070b428",
      "incomplete_value": true,
      "site": "0070b42c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 67,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0070b424",
      "incomplete_value": true,
      "site": "0070b430",
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
      "definition_site": "0070b424",
      "incomplete_value": true,
      "site": "0070b430",
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
    "ordinal": 68,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0070b008",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "0070b418",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      "0070b41c",
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
      "0070b008",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "0070b418",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      "0070b41c",
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

- 旧版 [`0070b000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070a/0070afb4.md#insn-0070b000) · [`0070b418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070a/0070afb4.md#insn-0070b418) · [`0070b41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070a/0070afb4.md#insn-0070b41c)
- 新版 `0070b000`（命令位置の公開資料なし） · `0070b418`（命令位置の公開資料なし） · `0070b41c`（命令位置の公開資料なし）

~~~diff
- 0070b000 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0070b000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0070b000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0070b000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0070b000 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 0070b000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0070b000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0070b000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0070b000 bytes 08a13491
+ 0070b000 bytes 08e13591
- 0070b418 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 0070b418 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0070b418 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 0070b418 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0070b418 bytes 08b946f9
+ 0070b418 bytes 08e146f9
- 0070b41c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d78:8"]]
- 0070b41c ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0070b41c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dc8:8"]]
+ 0070b41c ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 0070b41c bytes b5be46f9
+ 0070b41c bytes b5e646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7750057bcc5df6e834cafc68351a4d55"></a>

### [`0070cadc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070c/0070cadc.md) → [`0070cadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070c/0070cadc.md) FUN_0070cadc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0070ea48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070e/0070ea48.md) · 呼出先 10件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00471738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471738.md) [`007095c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00709/007095c8.md) [`0070b570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070b/0070b570.md) [`00710e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00710/00710e1c.md)
- 新版 呼出元 1件 [`0070ea48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070e/0070ea48.md) · 呼出先 10件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`007095c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00709/007095c8.md) [`0070b570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070b/0070b570.md) [`00710e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710e1c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.16% / 新版 98.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0070cd3c",
      "incomplete_value": true,
      "site": "0070cd50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:76f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070cd3c",
      "incomplete_value": true,
      "site": "0070cd50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6e4:8"
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
      "definition_site": "0070cd54",
      "incomplete_value": true,
      "site": "0070cd54",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0070cd54",
      "incomplete_value": true,
      "site": "0070cd54",
      "value": [
        "LOAD",
        "8",
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
      "0070cb84",
      "READ",
      [
        "storage",
        "00c1b740",
        null,
        "pointer"
      ]
    ],
    [
      "0070cb8c",
      "READ",
      [
        "storage",
        "00c28148",
        null,
        "undefined8"
      ]
    ],
    [
      "0070cd3c",
      "READ",
      [
        "storage",
        "0029d6e4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0070cb84",
      "READ",
      [
        "storage",
        "00c1b790",
        null,
        "pointer"
      ]
    ],
    [
      "0070cb8c",
      "READ",
      [
        "storage",
        "00c28188",
        null,
        "undefined8"
      ]
    ],
    [
      "0070cd3c",
      "READ",
      [
        "storage",
        "0029d76f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070cb84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070c/0070cadc.md#insn-0070cb84) · [`0070cd34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070c/0070cadc.md#insn-0070cd34)
- 新版 `0070cb84`（命令位置の公開資料なし） · `0070cd34`（命令位置の公開資料なし）

~~~diff
- 0070cb84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:740:8"]]
- 0070cb84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0070cb84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:790:8"]]
+ 0070cb84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0070cb84 bytes 08a143f9
+ 0070cb84 bytes 08c943f9
- 0070cd34 ["COPY", "tmp:0:8", ["const:6e4:8"]]
- 0070cd34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0070cd34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0070cd34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0070cd34 ["COPY", "tmp:0:8", ["const:76f:8"]]
+ 0070cd34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0070cd34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0070cd34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0070cd34 bytes 29911b91
+ 0070cd34 bytes 29bd1d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0557bd4760f9d9c6b45fb75f58f17009"></a>

### [`0070eee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070e/0070eee8.md) → [`0070eee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070e/0070eee8.md) FUN_0070eee8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00859898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859898.md) · 呼出先 7件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`006f1e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f1e2c.md) [`0070db34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070d/0070db34.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00859898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) · 呼出先 7件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`006f1e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1e2c.md) [`0070db34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070d/0070db34.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.01% / 新版 99.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0070f070",
      "incomplete_value": false,
      "site": "0070f074",
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
      "definition_site": "0070f070",
      "incomplete_value": false,
      "site": "0070f074",
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
      "0070f070",
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
      "0070f070",
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

- 旧版 [`0070f070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070e/0070eee8.md#insn-0070f070)
- 新版 `0070f070`（命令位置の公開資料なし）

~~~diff
- 0070f070 ["COPY", "tmp:0:8", ["const:5cf:8"]]
- 0070f070 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0070f070 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0070f070 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0070f070 ["COPY", "tmp:0:8", ["const:65a:8"]]
+ 0070f070 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0070f070 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0070f070 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0070f070 bytes 003c1791
+ 0070f070 bytes 00681991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

