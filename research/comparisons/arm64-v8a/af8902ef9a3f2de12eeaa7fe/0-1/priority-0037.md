# v15.7.3 → v15.7.4 · 最優先の変更候補 (37)

[一覧の目次](README.md)

<a id="compare-bd1814fe1d06d5d1dcf81b925fb4844e"></a>

### [`007c7fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7fac.md) → [`007c7fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c7fac.md) FUN_007c7fac

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
      "definition_site": "007c7fb0",
      "incomplete_value": false,
      "site": "007c7fb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c7fb0",
      "incomplete_value": false,
      "site": "007c7fb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:e18:8"
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
      "007c7fb4",
      "DATA",
      [
        "storage",
        "00bfee18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c7fb4",
      "DATA",
      [
        "storage",
        "00bfee68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c7fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7fac.md#insn-007c7fb0)
- 新版 [`007c7fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c7fac.md#insn-007c7fb0)

~~~diff
- 007c7fb0 ["COPY", "tmp:0:8", ["const:e18:8"]]
- 007c7fb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c7fb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c7fb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c7fb0 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 007c7fb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7fb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7fb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c7fb0 bytes 08613891
+ 007c7fb0 bytes 08a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0245494aaecf4efbadd6aa80c886fdb6"></a>

### [`007c8038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8038.md) → [`007c8038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8038.md) FUN_007c8038

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
      "definition_site": "007c805c",
      "incomplete_value": false,
      "site": "007c8060",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c805c",
      "incomplete_value": false,
      "site": "007c8060",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
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
      "007c8060",
      "DATA",
      [
        "storage",
        "00bfeea8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c8060",
      "DATA",
      [
        "storage",
        "00bfeef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c805c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8038.md#insn-007c805c)
- 新版 [`007c805c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8038.md#insn-007c805c)

~~~diff
- 007c805c ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 007c805c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c805c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c805c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c805c ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 007c805c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c805c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c805c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c805c bytes 08a13a91
+ 007c805c bytes 08e13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efd46ddffa6634214483b577c2045e17"></a>

### [`007c8078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8078.md) → [`007c8078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8078.md) FUN_007c8078

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
      "definition_site": "007c807c",
      "incomplete_value": false,
      "site": "007c8080",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c807c",
      "incomplete_value": false,
      "site": "007c8080",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
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
      "007c8080",
      "DATA",
      [
        "storage",
        "00bfeea8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c8080",
      "DATA",
      [
        "storage",
        "00bfeef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c807c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8078.md#insn-007c807c)
- 新版 [`007c807c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8078.md#insn-007c807c)

~~~diff
- 007c807c ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 007c807c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c807c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c807c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c807c ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 007c807c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c807c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c807c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c807c bytes 08a13a91
+ 007c807c bytes 08e13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-717dc1a149b1d061fe9c39fd5ca49c1e"></a>

### [`007c80a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c80a0.md) → [`007c80a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c80a0.md) FUN_007c80a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 36件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`00445d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d90.md)
- 新版 呼出元 0件  · 呼出先 36件 [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044592c.md) [`00445d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.72% / 新版 99.72%

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
      "definition_site": "007c8114",
      "incomplete_value": true,
      "site": "007c8114",
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
      "definition_site": "007c8114",
      "incomplete_value": true,
      "site": "007c8114",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007c8124",
      "incomplete_value": true,
      "site": "007c812c",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c8124",
      "incomplete_value": true,
      "site": "007c812c",
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
            "const:518:8"
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
      "007c8104",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007c811c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c8124",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007c8104",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007c811c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c8124",
      "PARAM",
      [
        "storage",
        "00bf4568",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c8104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c80a0.md#insn-007c8104) · [`007c811c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c80a0.md#insn-007c811c) · [`007c8124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c80a0.md#insn-007c8124)
- 新版 [`007c8104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c80a0.md#insn-007c8104) · [`007c811c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c80a0.md#insn-007c811c) · [`007c8124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c80a0.md#insn-007c8124)

~~~diff
- 007c8104 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007c8104 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c8104 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007c8104 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007c8104 bytes 003d45f9
+ 007c8104 bytes 005d45f9
- 007c811c ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007c811c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007c811c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007c811c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007c811c ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007c811c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007c811c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007c811c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007c811c bytes 21203991
+ 007c811c bytes 21603a91
- 007c8124 ["COPY", "tmp:0:8", ["const:518:8"]]
- 007c8124 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c8124 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c8124 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c8124 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 007c8124 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c8124 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c8124 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c8124 bytes 42601491
+ 007c8124 bytes 42a01591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d533047d3693a40549acd6d0190d5f65"></a>

### [`007c8c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8c10.md) → [`007c8c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8c10.md) FUN_007c8c10

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
      "definition_site": "007c8c34",
      "incomplete_value": false,
      "site": "007c8c38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c8c34",
      "incomplete_value": false,
      "site": "007c8c38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "007c8c38",
      "DATA",
      [
        "storage",
        "00bfef28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c8c38",
      "DATA",
      [
        "storage",
        "00bfef78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c8c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8c10.md#insn-007c8c34)
- 新版 [`007c8c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8c10.md#insn-007c8c34)

~~~diff
- 007c8c34 ["COPY", "tmp:0:8", ["const:f28:8"]]
- 007c8c34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c8c34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c8c34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c8c34 ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 007c8c34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8c34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8c34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c8c34 bytes 08a13c91
+ 007c8c34 bytes 08e13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-567ab9aff2813e6a59449c7c4c3611a3"></a>

### [`007c8c50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8c50.md) → [`007c8c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8c50.md) FUN_007c8c50

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
      "definition_site": "007c8c54",
      "incomplete_value": false,
      "site": "007c8c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c8c54",
      "incomplete_value": false,
      "site": "007c8c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "007c8c58",
      "DATA",
      [
        "storage",
        "00bfef28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c8c58",
      "DATA",
      [
        "storage",
        "00bfef78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c8c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8c50.md#insn-007c8c54)
- 新版 [`007c8c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8c50.md#insn-007c8c54)

~~~diff
- 007c8c54 ["COPY", "tmp:0:8", ["const:f28:8"]]
- 007c8c54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c8c54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c8c54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c8c54 ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 007c8c54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8c54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8c54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c8c54 bytes 08a13c91
+ 007c8c54 bytes 08e13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b75042e1bd541f857f79e7ac378f87fa"></a>

### [`007c8ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8ebc.md) → [`007c8ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8ebc.md) FUN_007c8ebc

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
      "definition_site": "007c8ed0",
      "incomplete_value": false,
      "site": "007c8ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c8ed0",
      "incomplete_value": false,
      "site": "007c8ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
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
      "007c8ed4",
      "DATA",
      [
        "storage",
        "00bfefa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c8ed4",
      "DATA",
      [
        "storage",
        "00bfeff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c8ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8ebc.md#insn-007c8ed0)
- 新版 [`007c8ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8ebc.md#insn-007c8ed0)

~~~diff
- 007c8ed0 ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 007c8ed0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c8ed0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c8ed0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c8ed0 ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 007c8ed0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8ed0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8ed0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c8ed0 bytes 08a13e91
+ 007c8ed0 bytes 08e13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0be1ea5c76d1bb0f8505527e83594a3"></a>

### [`007c8ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8ee0.md) → [`007c8ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8ee0.md) FUN_007c8ee0

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
      "definition_site": "007c8ee4",
      "incomplete_value": false,
      "site": "007c8ee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c8ee4",
      "incomplete_value": false,
      "site": "007c8ee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
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
      "007c8ee8",
      "DATA",
      [
        "storage",
        "00bfefa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c8ee8",
      "DATA",
      [
        "storage",
        "00bfeff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c8ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8ee0.md#insn-007c8ee4)
- 新版 [`007c8ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8ee0.md#insn-007c8ee4)

~~~diff
- 007c8ee4 ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 007c8ee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c8ee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c8ee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c8ee4 ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 007c8ee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8ee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8ee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c8ee4 bytes 08a13e91
+ 007c8ee4 bytes 08e13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a42f073831cb1b201455fd665ae83bee"></a>

### [`007c8f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8f6c.md) → [`007c8f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8f6c.md) FUN_007c8f6c

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
      "definition_site": "007c8f80",
      "incomplete_value": false,
      "site": "007c8f84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c8f80",
      "incomplete_value": false,
      "site": "007c8f84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:28:8"
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
      "007c8f84",
      "DATA",
      [
        "storage",
        "00bff028",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c8f84",
      "DATA",
      [
        "storage",
        "00bff078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c8f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8f6c.md#insn-007c8f80)
- 新版 [`007c8f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8f6c.md#insn-007c8f80)

~~~diff
- 007c8f80 ["COPY", "tmp:0:8", ["const:28:8"]]
- 007c8f80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c8f80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c8f80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c8f80 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 007c8f80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8f80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8f80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c8f80 bytes 08a10091
+ 007c8f80 bytes 08e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d7222a57fe1e87384e850e2cb339e88"></a>

### [`007c8f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8f90.md) → [`007c8f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8f90.md) FUN_007c8f90

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
      "definition_site": "007c8f94",
      "incomplete_value": false,
      "site": "007c8f98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c8f94",
      "incomplete_value": false,
      "site": "007c8f98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:28:8"
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
      "007c8f98",
      "DATA",
      [
        "storage",
        "00bff028",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c8f98",
      "DATA",
      [
        "storage",
        "00bff078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c8f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8f90.md#insn-007c8f94)
- 新版 [`007c8f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8f90.md#insn-007c8f94)

~~~diff
- 007c8f94 ["COPY", "tmp:0:8", ["const:28:8"]]
- 007c8f94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c8f94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c8f94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c8f94 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 007c8f94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8f94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8f94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c8f94 bytes 08a10091
+ 007c8f94 bytes 08e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2e9f5baaa447c35d6718ee9f7a9fdd5"></a>

### [`007c901c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c901c.md) → [`007c901c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c901c.md) FUN_007c901c

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
      "definition_site": "007c9030",
      "incomplete_value": false,
      "site": "007c9034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9030",
      "incomplete_value": false,
      "site": "007c9034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:a8:8"
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
      "007c9034",
      "DATA",
      [
        "storage",
        "00bff0a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9034",
      "DATA",
      [
        "storage",
        "00bff0f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c901c.md#insn-007c9030)
- 新版 [`007c9030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c901c.md#insn-007c9030)

~~~diff
- 007c9030 ["COPY", "tmp:0:8", ["const:a8:8"]]
- 007c9030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9030 ["COPY", "tmp:0:8", ["const:f8:8"]]
+ 007c9030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9030 bytes 08a10291
+ 007c9030 bytes 08e10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-beee6c64aed453d013133c0a563a4efa"></a>

### [`007c9040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9040.md) → [`007c9040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9040.md) FUN_007c9040

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
      "definition_site": "007c9044",
      "incomplete_value": false,
      "site": "007c9048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9044",
      "incomplete_value": false,
      "site": "007c9048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:a8:8"
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
      "007c9048",
      "DATA",
      [
        "storage",
        "00bff0a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9048",
      "DATA",
      [
        "storage",
        "00bff0f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9040.md#insn-007c9044)
- 新版 [`007c9044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9040.md#insn-007c9044)

~~~diff
- 007c9044 ["COPY", "tmp:0:8", ["const:a8:8"]]
- 007c9044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9044 ["COPY", "tmp:0:8", ["const:f8:8"]]
+ 007c9044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9044 bytes 08a10291
+ 007c9044 bytes 08e10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31641dd8b219ad426de6d171a50bf907"></a>

### [`007c90cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c90cc.md) → [`007c90cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c90cc.md) FUN_007c90cc

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
      "definition_site": "007c90f0",
      "incomplete_value": false,
      "site": "007c90f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c90f0",
      "incomplete_value": false,
      "site": "007c90f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:128:8"
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
      "007c90f0",
      "DATA",
      [
        "storage",
        "00bff128",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c90f0",
      "DATA",
      [
        "storage",
        "00bff178",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c90ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c90cc.md#insn-007c90ec)
- 新版 [`007c90ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c90cc.md#insn-007c90ec)

~~~diff
- 007c90ec ["COPY", "tmp:0:8", ["const:128:8"]]
- 007c90ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c90ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c90ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c90ec ["COPY", "tmp:0:8", ["const:178:8"]]
+ 007c90ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c90ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c90ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c90ec bytes 08a10491
+ 007c90ec bytes 08e10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e0eaaaf3f27f906a1d61ee90f3bb117"></a>

### [`007c9100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9100.md) → [`007c9100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9100.md) FUN_007c9100

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
      "definition_site": "007c910c",
      "incomplete_value": false,
      "site": "007c910c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c910c",
      "incomplete_value": false,
      "site": "007c910c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:128:8"
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
      "007c910c",
      "DATA",
      [
        "storage",
        "00bff128",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c910c",
      "DATA",
      [
        "storage",
        "00bff178",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9100.md#insn-007c9108)
- 新版 [`007c9108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9100.md#insn-007c9108)

~~~diff
- 007c9108 ["COPY", "tmp:0:8", ["const:128:8"]]
- 007c9108 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c9108 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c9108 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c9108 ["COPY", "tmp:0:8", ["const:178:8"]]
+ 007c9108 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c9108 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c9108 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c9108 bytes 29a10491
+ 007c9108 bytes 29e10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-962c245d7e569f4b44c7bec9bc0866d0"></a>

### [`007c9190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9190.md) → [`007c9190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9190.md) FUN_007c9190

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
      "definition_site": "007c91b4",
      "incomplete_value": false,
      "site": "007c91b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c91b4",
      "incomplete_value": false,
      "site": "007c91b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
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
      "007c91b4",
      "DATA",
      [
        "storage",
        "00bff1a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c91b4",
      "DATA",
      [
        "storage",
        "00bff1f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c91b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9190.md#insn-007c91b0)
- 新版 [`007c91b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9190.md#insn-007c91b0)

~~~diff
- 007c91b0 ["COPY", "tmp:0:8", ["const:1a8:8"]]
- 007c91b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c91b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c91b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c91b0 ["COPY", "tmp:0:8", ["const:1f8:8"]]
+ 007c91b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c91b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c91b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c91b0 bytes 08a10691
+ 007c91b0 bytes 08e10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35c21d65bd0bc9032cc855f925e18157"></a>

### [`007c91c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c91c4.md) → [`007c91c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c91c4.md) FUN_007c91c4

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
      "definition_site": "007c91d0",
      "incomplete_value": false,
      "site": "007c91d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c91d0",
      "incomplete_value": false,
      "site": "007c91d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
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
      "007c91d0",
      "DATA",
      [
        "storage",
        "00bff1a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c91d0",
      "DATA",
      [
        "storage",
        "00bff1f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c91cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c91c4.md#insn-007c91cc)
- 新版 [`007c91cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c91c4.md#insn-007c91cc)

~~~diff
- 007c91cc ["COPY", "tmp:0:8", ["const:1a8:8"]]
- 007c91cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c91cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c91cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c91cc ["COPY", "tmp:0:8", ["const:1f8:8"]]
+ 007c91cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c91cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c91cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c91cc bytes 29a10691
+ 007c91cc bytes 29e10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb607f0a6c0a0cb054e73713d00ef928"></a>

### [`007c9254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9254.md) → [`007c9254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9254.md) FUN_007c9254

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
      "definition_site": "007c9268",
      "incomplete_value": false,
      "site": "007c926c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9268",
      "incomplete_value": false,
      "site": "007c926c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
      "007c926c",
      "DATA",
      [
        "storage",
        "00bff228",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c926c",
      "DATA",
      [
        "storage",
        "00bff278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9254.md#insn-007c9268)
- 新版 [`007c9268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9254.md#insn-007c9268)

~~~diff
- 007c9268 ["COPY", "tmp:0:8", ["const:228:8"]]
- 007c9268 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9268 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9268 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9268 ["COPY", "tmp:0:8", ["const:278:8"]]
+ 007c9268 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9268 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9268 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9268 bytes 08a10891
+ 007c9268 bytes 08e10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38f75d646cde81e76562aa91f1c6ce5e"></a>

### [`007c9278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9278.md) → [`007c9278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9278.md) FUN_007c9278

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
      "definition_site": "007c927c",
      "incomplete_value": false,
      "site": "007c9280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c927c",
      "incomplete_value": false,
      "site": "007c9280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
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
      "007c9280",
      "DATA",
      [
        "storage",
        "00bff228",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9280",
      "DATA",
      [
        "storage",
        "00bff278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c927c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9278.md#insn-007c927c)
- 新版 [`007c927c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9278.md#insn-007c927c)

~~~diff
- 007c927c ["COPY", "tmp:0:8", ["const:228:8"]]
- 007c927c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c927c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c927c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c927c ["COPY", "tmp:0:8", ["const:278:8"]]
+ 007c927c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c927c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c927c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c927c bytes 08a10891
+ 007c927c bytes 08e10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d9170aa0cc5d21ba47a8eec84c4dba7"></a>

### [`007c9304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9304.md) → [`007c9304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9304.md) FUN_007c9304

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
      "definition_site": "007c9328",
      "incomplete_value": false,
      "site": "007c9328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9328",
      "incomplete_value": false,
      "site": "007c9328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
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
      "007c9328",
      "DATA",
      [
        "storage",
        "00bff2a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9328",
      "DATA",
      [
        "storage",
        "00bff2f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9304.md#insn-007c9324)
- 新版 [`007c9324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9304.md#insn-007c9324)

~~~diff
- 007c9324 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 007c9324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9324 ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 007c9324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9324 bytes 08a10a91
+ 007c9324 bytes 08e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4188381b3055e0c3c17449b1b57e269"></a>

### [`007c9338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9338.md) → [`007c9338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9338.md) FUN_007c9338

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
      "definition_site": "007c9344",
      "incomplete_value": false,
      "site": "007c9344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9344",
      "incomplete_value": false,
      "site": "007c9344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
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
      "007c9344",
      "DATA",
      [
        "storage",
        "00bff2a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9344",
      "DATA",
      [
        "storage",
        "00bff2f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9338.md#insn-007c9340)
- 新版 [`007c9340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9338.md#insn-007c9340)

~~~diff
- 007c9340 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 007c9340 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c9340 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c9340 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c9340 ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 007c9340 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c9340 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c9340 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c9340 bytes 29a10a91
+ 007c9340 bytes 29e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f084db4aaf8bd51c6d0e9f2ef0602f55"></a>

### [`007c9410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9410.md) → [`007c9410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9410.md) FUN_007c9410

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
      "definition_site": "007c9424",
      "incomplete_value": false,
      "site": "007c9428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9424",
      "incomplete_value": false,
      "site": "007c9428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "007c9428",
      "DATA",
      [
        "storage",
        "00bff328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9428",
      "DATA",
      [
        "storage",
        "00bff378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9410.md#insn-007c9424)
- 新版 [`007c9424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9410.md#insn-007c9424)

~~~diff
- 007c9424 ["COPY", "tmp:0:8", ["const:328:8"]]
- 007c9424 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9424 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9424 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9424 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 007c9424 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9424 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9424 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9424 bytes 08a10c91
+ 007c9424 bytes 08e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8af25f25b4710b6b3e7f9e7cf3ffe65"></a>

### [`007c9434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9434.md) → [`007c9434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9434.md) FUN_007c9434

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
      "definition_site": "007c9438",
      "incomplete_value": false,
      "site": "007c943c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9438",
      "incomplete_value": false,
      "site": "007c943c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
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
      "007c943c",
      "DATA",
      [
        "storage",
        "00bff328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c943c",
      "DATA",
      [
        "storage",
        "00bff378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9434.md#insn-007c9438)
- 新版 [`007c9438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9434.md#insn-007c9438)

~~~diff
- 007c9438 ["COPY", "tmp:0:8", ["const:328:8"]]
- 007c9438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9438 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 007c9438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9438 bytes 08a10c91
+ 007c9438 bytes 08e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0497e364772bd0f4524a95806bca4a3"></a>

### [`007c94f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c94f0.md) → [`007c94f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c94f0.md) FUN_007c94f0

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
      "definition_site": "007c9504",
      "incomplete_value": false,
      "site": "007c9508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9504",
      "incomplete_value": false,
      "site": "007c9508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
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
      "007c9508",
      "DATA",
      [
        "storage",
        "00bff3a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9508",
      "DATA",
      [
        "storage",
        "00bff3f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c94f0.md#insn-007c9504)
- 新版 [`007c9504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c94f0.md#insn-007c9504)

~~~diff
- 007c9504 ["COPY", "tmp:0:8", ["const:3a8:8"]]
- 007c9504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9504 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 007c9504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9504 bytes 08a10e91
+ 007c9504 bytes 08e10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f08640f7604c3661828dc16232fc4d3"></a>

### [`007c9514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9514.md) → [`007c9514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9514.md) FUN_007c9514

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
      "definition_site": "007c9518",
      "incomplete_value": false,
      "site": "007c951c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9518",
      "incomplete_value": false,
      "site": "007c951c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
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
      "007c951c",
      "DATA",
      [
        "storage",
        "00bff3a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c951c",
      "DATA",
      [
        "storage",
        "00bff3f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9514.md#insn-007c9518)
- 新版 [`007c9518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9514.md#insn-007c9518)

~~~diff
- 007c9518 ["COPY", "tmp:0:8", ["const:3a8:8"]]
- 007c9518 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9518 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9518 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9518 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 007c9518 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9518 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9518 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9518 bytes 08a10e91
+ 007c9518 bytes 08e10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75ecbc4ab603024b40be884125870f3e"></a>

### [`007c9640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9640.md) → [`007c9640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9640.md) FUN_007c9640

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
      "definition_site": "007c9654",
      "incomplete_value": false,
      "site": "007c9658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9654",
      "incomplete_value": false,
      "site": "007c9658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:428:8"
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
      "007c9658",
      "DATA",
      [
        "storage",
        "00bff428",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9658",
      "DATA",
      [
        "storage",
        "00bff478",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9640.md#insn-007c9654)
- 新版 [`007c9654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9640.md#insn-007c9654)

~~~diff
- 007c9654 ["COPY", "tmp:0:8", ["const:428:8"]]
- 007c9654 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9654 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9654 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9654 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 007c9654 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9654 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9654 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9654 bytes 08a11091
+ 007c9654 bytes 08e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2152e909423f8c3c4a5fd3563e66db77"></a>

### [`007c9664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9664.md) → [`007c9664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9664.md) FUN_007c9664

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
      "definition_site": "007c9668",
      "incomplete_value": false,
      "site": "007c966c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9668",
      "incomplete_value": false,
      "site": "007c966c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:428:8"
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
      "007c966c",
      "DATA",
      [
        "storage",
        "00bff428",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c966c",
      "DATA",
      [
        "storage",
        "00bff478",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9664.md#insn-007c9668)
- 新版 [`007c9668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9664.md#insn-007c9668)

~~~diff
- 007c9668 ["COPY", "tmp:0:8", ["const:428:8"]]
- 007c9668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9668 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 007c9668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9668 bytes 08a11091
+ 007c9668 bytes 08e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c132367f232a2a0a2bc342a24072c75"></a>

### [`007c96f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c96f0.md) → [`007c96f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c96f0.md) FUN_007c96f0

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
      "definition_site": "007c9704",
      "incomplete_value": false,
      "site": "007c9708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9704",
      "incomplete_value": false,
      "site": "007c9708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
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
      "007c9708",
      "DATA",
      [
        "storage",
        "00bff4a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9708",
      "DATA",
      [
        "storage",
        "00bff4f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c96f0.md#insn-007c9704)
- 新版 [`007c9704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c96f0.md#insn-007c9704)

~~~diff
- 007c9704 ["COPY", "tmp:0:8", ["const:4a8:8"]]
- 007c9704 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9704 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9704 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9704 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 007c9704 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9704 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9704 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9704 bytes 08a11291
+ 007c9704 bytes 08e11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7daef3213f3f941393a875216f31833e"></a>

### [`007c9714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9714.md) → [`007c9714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9714.md) FUN_007c9714

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
      "definition_site": "007c9718",
      "incomplete_value": false,
      "site": "007c971c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9718",
      "incomplete_value": false,
      "site": "007c971c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
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
      "007c971c",
      "DATA",
      [
        "storage",
        "00bff4a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c971c",
      "DATA",
      [
        "storage",
        "00bff4f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9714.md#insn-007c9718)
- 新版 [`007c9718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9714.md#insn-007c9718)

~~~diff
- 007c9718 ["COPY", "tmp:0:8", ["const:4a8:8"]]
- 007c9718 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9718 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9718 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9718 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 007c9718 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9718 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9718 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9718 bytes 08a11291
+ 007c9718 bytes 08e11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4920dff1f902e24b7150a585dcd3d1e9"></a>

### [`007c97a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c97a0.md) → [`007c97a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c97a0.md) FUN_007c97a0

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
      "definition_site": "007c97b4",
      "incomplete_value": false,
      "site": "007c97b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c97b4",
      "incomplete_value": false,
      "site": "007c97b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "007c97b8",
      "DATA",
      [
        "storage",
        "00bff528",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c97b8",
      "DATA",
      [
        "storage",
        "00bff578",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c97b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c97a0.md#insn-007c97b4)
- 新版 [`007c97b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c97a0.md#insn-007c97b4)

~~~diff
- 007c97b4 ["COPY", "tmp:0:8", ["const:528:8"]]
- 007c97b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c97b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c97b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c97b4 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 007c97b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c97b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c97b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c97b4 bytes 08a11491
+ 007c97b4 bytes 08e11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cd3bcc60b13748d45a66d1da05e6683"></a>

### [`007c97c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c97c4.md) → [`007c97c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c97c4.md) FUN_007c97c4

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
      "definition_site": "007c97c8",
      "incomplete_value": false,
      "site": "007c97cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c97c8",
      "incomplete_value": false,
      "site": "007c97cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "007c97cc",
      "DATA",
      [
        "storage",
        "00bff528",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c97cc",
      "DATA",
      [
        "storage",
        "00bff578",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c97c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c97c4.md#insn-007c97c8)
- 新版 [`007c97c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c97c4.md#insn-007c97c8)

~~~diff
- 007c97c8 ["COPY", "tmp:0:8", ["const:528:8"]]
- 007c97c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c97c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c97c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c97c8 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 007c97c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c97c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c97c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c97c8 bytes 08a11491
+ 007c97c8 bytes 08e11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abefe5d4880acf1111313ba825539161"></a>

### [`007c9850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9850.md) → [`007c9850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9850.md) FUN_007c9850

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
      "definition_site": "007c9874",
      "incomplete_value": false,
      "site": "007c9874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9874",
      "incomplete_value": false,
      "site": "007c9874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
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
      "007c9874",
      "DATA",
      [
        "storage",
        "00bff5a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9874",
      "DATA",
      [
        "storage",
        "00bff5f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9850.md#insn-007c9870)
- 新版 [`007c9870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9850.md#insn-007c9870)

~~~diff
- 007c9870 ["COPY", "tmp:0:8", ["const:5a8:8"]]
- 007c9870 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9870 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9870 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9870 ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 007c9870 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9870 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9870 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9870 bytes 08a11691
+ 007c9870 bytes 08e11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a899c17c32e25055a9784d7fafe930d"></a>

### [`007c9884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9884.md) → [`007c9884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9884.md) FUN_007c9884

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
      "definition_site": "007c9890",
      "incomplete_value": false,
      "site": "007c9890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9890",
      "incomplete_value": false,
      "site": "007c9890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
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
      "007c9890",
      "DATA",
      [
        "storage",
        "00bff5a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9890",
      "DATA",
      [
        "storage",
        "00bff5f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c988c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9884.md#insn-007c988c)
- 新版 [`007c988c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9884.md#insn-007c988c)

~~~diff
- 007c988c ["COPY", "tmp:0:8", ["const:5a8:8"]]
- 007c988c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c988c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c988c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c988c ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 007c988c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c988c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c988c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c988c bytes 29a11691
+ 007c988c bytes 29e11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-011cc4be0d0a6303d97c7af80955ce26"></a>

### [`007c9988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9988.md) → [`007c9988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9988.md) FUN_007c9988

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
      "definition_site": "007c99a8",
      "incomplete_value": false,
      "site": "007c99ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c99a8",
      "incomplete_value": false,
      "site": "007c99ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
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
      "007c99ac",
      "DATA",
      [
        "storage",
        "00bff628",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c99ac",
      "DATA",
      [
        "storage",
        "00bff678",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c99a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9988.md#insn-007c99a8)
- 新版 [`007c99a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9988.md#insn-007c99a8)

~~~diff
- 007c99a8 ["COPY", "tmp:0:8", ["const:628:8"]]
- 007c99a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c99a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c99a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c99a8 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 007c99a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c99a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c99a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c99a8 bytes 08a11891
+ 007c99a8 bytes 08e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f33d8c66491d63309e44550d46fc035"></a>

### [`007c99c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c99c0.md) → [`007c99c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c99c0.md) FUN_007c99c0

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
      "definition_site": "007c99c8",
      "incomplete_value": false,
      "site": "007c99cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c99c8",
      "incomplete_value": false,
      "site": "007c99cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
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
      "007c99cc",
      "DATA",
      [
        "storage",
        "00bff628",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c99cc",
      "DATA",
      [
        "storage",
        "00bff678",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c99c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c99c0.md#insn-007c99c8)
- 新版 [`007c99c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c99c0.md#insn-007c99c8)

~~~diff
- 007c99c8 ["COPY", "tmp:0:8", ["const:628:8"]]
- 007c99c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c99c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c99c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c99c8 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 007c99c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c99c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c99c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c99c8 bytes 29a11891
+ 007c99c8 bytes 29e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b24ddc7b3412bbd2616dc922dc9eaa48"></a>

### [`007c9abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9abc.md) → [`007c9abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9abc.md) FUN_007c9abc

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
      "definition_site": "007c9adc",
      "incomplete_value": false,
      "site": "007c9ae0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9adc",
      "incomplete_value": false,
      "site": "007c9ae0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "007c9ae0",
      "DATA",
      [
        "storage",
        "00bff6a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9ae0",
      "DATA",
      [
        "storage",
        "00bff6f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9abc.md#insn-007c9adc)
- 新版 [`007c9adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9abc.md#insn-007c9adc)

~~~diff
- 007c9adc ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 007c9adc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9adc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9adc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9adc ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 007c9adc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9adc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9adc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9adc bytes 08a11a91
+ 007c9adc bytes 08e11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88df1fd812f069a39b96436f63c697f8"></a>

### [`007c9af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9af4.md) → [`007c9af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9af4.md) FUN_007c9af4

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
      "definition_site": "007c9afc",
      "incomplete_value": false,
      "site": "007c9b00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9afc",
      "incomplete_value": false,
      "site": "007c9b00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "007c9b00",
      "DATA",
      [
        "storage",
        "00bff6a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9b00",
      "DATA",
      [
        "storage",
        "00bff6f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9af4.md#insn-007c9afc)
- 新版 [`007c9afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9af4.md#insn-007c9afc)

~~~diff
- 007c9afc ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 007c9afc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c9afc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c9afc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c9afc ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 007c9afc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c9afc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c9afc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c9afc bytes 29a11a91
+ 007c9afc bytes 29e11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5f07c4c20934d97c352b2df98fca2e6"></a>

### [`007c9b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9b88.md) → [`007c9b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9b88.md) FUN_007c9b88

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
      "definition_site": "007c9ba8",
      "incomplete_value": false,
      "site": "007c9bac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9ba8",
      "incomplete_value": false,
      "site": "007c9bac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:728:8"
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
      "007c9bac",
      "DATA",
      [
        "storage",
        "00bff728",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9bac",
      "DATA",
      [
        "storage",
        "00bff778",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9b88.md#insn-007c9ba8)
- 新版 [`007c9ba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9b88.md#insn-007c9ba8)

~~~diff
- 007c9ba8 ["COPY", "tmp:0:8", ["const:728:8"]]
- 007c9ba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9ba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9ba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9ba8 ["COPY", "tmp:0:8", ["const:778:8"]]
+ 007c9ba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9ba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9ba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9ba8 bytes 08a11c91
+ 007c9ba8 bytes 08e11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa17cd996d0b818f62e005cd29d29933"></a>

### [`007c9bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9bc0.md) → [`007c9bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9bc0.md) FUN_007c9bc0

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
      "definition_site": "007c9bc8",
      "incomplete_value": false,
      "site": "007c9bcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9bc8",
      "incomplete_value": false,
      "site": "007c9bcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:728:8"
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
      "007c9bcc",
      "DATA",
      [
        "storage",
        "00bff728",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9bcc",
      "DATA",
      [
        "storage",
        "00bff778",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9bc0.md#insn-007c9bc8)
- 新版 [`007c9bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9bc0.md#insn-007c9bc8)

~~~diff
- 007c9bc8 ["COPY", "tmp:0:8", ["const:728:8"]]
- 007c9bc8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c9bc8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c9bc8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c9bc8 ["COPY", "tmp:0:8", ["const:778:8"]]
+ 007c9bc8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c9bc8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c9bc8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c9bc8 bytes 29a11c91
+ 007c9bc8 bytes 29e11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c773cc0632f737496550f851d989eb8"></a>

### [`007c9c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9c54.md) → [`007c9c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9c54.md) FUN_007c9c54

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
      "definition_site": "007c9c74",
      "incomplete_value": false,
      "site": "007c9c78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9c74",
      "incomplete_value": false,
      "site": "007c9c78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
      "007c9c78",
      "DATA",
      [
        "storage",
        "00bff7a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9c78",
      "DATA",
      [
        "storage",
        "00bff7f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9c54.md#insn-007c9c74)
- 新版 [`007c9c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9c54.md#insn-007c9c74)

~~~diff
- 007c9c74 ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 007c9c74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9c74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9c74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9c74 ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 007c9c74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9c74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9c74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9c74 bytes 08a11e91
+ 007c9c74 bytes 08e11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-422530ba4f4c74b38df00f2658bfd3fa"></a>

### [`007c9c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9c8c.md) → [`007c9c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9c8c.md) FUN_007c9c8c

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
      "definition_site": "007c9c90",
      "incomplete_value": false,
      "site": "007c9c94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9c90",
      "incomplete_value": false,
      "site": "007c9c94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
      "007c9c94",
      "DATA",
      [
        "storage",
        "00bff7a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9c94",
      "DATA",
      [
        "storage",
        "00bff7f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9c8c.md#insn-007c9c90)
- 新版 [`007c9c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9c8c.md#insn-007c9c90)

~~~diff
- 007c9c90 ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 007c9c90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9c90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9c90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9c90 ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 007c9c90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9c90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9c90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9c90 bytes 08a11e91
+ 007c9c90 bytes 08e11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3f57b67e91c9a08ab4d826978293a46"></a>

### [`007c9d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9d44.md) → [`007c9d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9d44.md) FUN_007c9d44

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
      "definition_site": "007c9d64",
      "incomplete_value": false,
      "site": "007c9d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9d64",
      "incomplete_value": false,
      "site": "007c9d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:828:8"
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
      "007c9d68",
      "DATA",
      [
        "storage",
        "00bff828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9d68",
      "DATA",
      [
        "storage",
        "00bff878",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9d44.md#insn-007c9d64)
- 新版 [`007c9d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9d44.md#insn-007c9d64)

~~~diff
- 007c9d64 ["COPY", "tmp:0:8", ["const:828:8"]]
- 007c9d64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9d64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9d64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9d64 ["COPY", "tmp:0:8", ["const:878:8"]]
+ 007c9d64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9d64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9d64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9d64 bytes 08a12091
+ 007c9d64 bytes 08e12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a858db69e3a2c81194c73db64b1a65e8"></a>

### [`007c9d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9d7c.md) → [`007c9d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9d7c.md) FUN_007c9d7c

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
      "definition_site": "007c9d80",
      "incomplete_value": false,
      "site": "007c9d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9d80",
      "incomplete_value": false,
      "site": "007c9d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:828:8"
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
      "007c9d84",
      "DATA",
      [
        "storage",
        "00bff828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9d84",
      "DATA",
      [
        "storage",
        "00bff878",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9d7c.md#insn-007c9d80)
- 新版 [`007c9d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9d7c.md#insn-007c9d80)

~~~diff
- 007c9d80 ["COPY", "tmp:0:8", ["const:828:8"]]
- 007c9d80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9d80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9d80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9d80 ["COPY", "tmp:0:8", ["const:878:8"]]
+ 007c9d80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9d80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9d80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9d80 bytes 08a12091
+ 007c9d80 bytes 08e12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01382046194ac125f65904e68ccddf28"></a>

### [`007c9e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9e34.md) → [`007c9e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9e34.md) FUN_007c9e34

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
      "definition_site": "007c9e48",
      "incomplete_value": false,
      "site": "007c9e4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9e48",
      "incomplete_value": false,
      "site": "007c9e4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
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
      "007c9e4c",
      "DATA",
      [
        "storage",
        "00bff8a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9e4c",
      "DATA",
      [
        "storage",
        "00bff8f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9e34.md#insn-007c9e48)
- 新版 [`007c9e48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9e34.md#insn-007c9e48)

~~~diff
- 007c9e48 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 007c9e48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9e48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9e48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9e48 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 007c9e48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9e48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9e48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9e48 bytes 08a12291
+ 007c9e48 bytes 08e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17caaeb27ee6734859b08dc6c03db992"></a>

### [`007c9e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9e58.md) → [`007c9e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9e58.md) FUN_007c9e58

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
      "definition_site": "007c9e5c",
      "incomplete_value": false,
      "site": "007c9e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9e5c",
      "incomplete_value": false,
      "site": "007c9e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
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
      "007c9e60",
      "DATA",
      [
        "storage",
        "00bff8a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9e60",
      "DATA",
      [
        "storage",
        "00bff8f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9e58.md#insn-007c9e5c)
- 新版 [`007c9e5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9e58.md#insn-007c9e5c)

~~~diff
- 007c9e5c ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 007c9e5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9e5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9e5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9e5c ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 007c9e5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9e5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9e5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9e5c bytes 08a12291
+ 007c9e5c bytes 08e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2f51cdebcdc7cf7ef962617b8c85c59"></a>

### [`007c9ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9ee4.md) → [`007c9ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9ee4.md) FUN_007c9ee4

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
      "definition_site": "007c9f08",
      "incomplete_value": false,
      "site": "007c9f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9f08",
      "incomplete_value": false,
      "site": "007c9f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "007c9f0c",
      "DATA",
      [
        "storage",
        "00bff928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9f0c",
      "DATA",
      [
        "storage",
        "00bff978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9ee4.md#insn-007c9f08)
- 新版 [`007c9f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9ee4.md#insn-007c9f08)

~~~diff
- 007c9f08 ["COPY", "tmp:0:8", ["const:928:8"]]
- 007c9f08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9f08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9f08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9f08 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 007c9f08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9f08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9f08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9f08 bytes 08a12491
+ 007c9f08 bytes 08e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fe42a4b9d3e12f077fe79cab56dce5c"></a>

### [`007c9f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9f24.md) → [`007c9f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9f24.md) FUN_007c9f24

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
      "definition_site": "007c9f28",
      "incomplete_value": false,
      "site": "007c9f2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9f28",
      "incomplete_value": false,
      "site": "007c9f2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "007c9f2c",
      "DATA",
      [
        "storage",
        "00bff928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9f2c",
      "DATA",
      [
        "storage",
        "00bff978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9f24.md#insn-007c9f28)
- 新版 [`007c9f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9f24.md#insn-007c9f28)

~~~diff
- 007c9f28 ["COPY", "tmp:0:8", ["const:928:8"]]
- 007c9f28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9f28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9f28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9f28 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 007c9f28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9f28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9f28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9f28 bytes 08a12491
+ 007c9f28 bytes 08e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d14da3560ea8f595176667dab0abbbf5"></a>

### [`007ca0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca0e4.md) → [`007ca0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca0e4.md) FUN_007ca0e4

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
      "definition_site": "007ca104",
      "incomplete_value": false,
      "site": "007ca108",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ca104",
      "incomplete_value": false,
      "site": "007ca108",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
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
      "007ca108",
      "DATA",
      [
        "storage",
        "00bff9a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ca108",
      "DATA",
      [
        "storage",
        "00bff9f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ca104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca0e4.md#insn-007ca104)
- 新版 [`007ca104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca0e4.md#insn-007ca104)

~~~diff
- 007ca104 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 007ca104 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ca104 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ca104 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ca104 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 007ca104 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca104 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca104 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ca104 bytes 08a12691
+ 007ca104 bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a243f3dd159feb23e7cce5722b2154e1"></a>

### [`007ca11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca11c.md) → [`007ca11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca11c.md) FUN_007ca11c

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
      "definition_site": "007ca120",
      "incomplete_value": false,
      "site": "007ca124",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ca120",
      "incomplete_value": false,
      "site": "007ca124",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
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
      "007ca124",
      "DATA",
      [
        "storage",
        "00bff9a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ca124",
      "DATA",
      [
        "storage",
        "00bff9f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ca120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca11c.md#insn-007ca120)
- 新版 [`007ca120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca11c.md#insn-007ca120)

~~~diff
- 007ca120 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 007ca120 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ca120 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ca120 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ca120 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 007ca120 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca120 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca120 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ca120 bytes 08a12691
+ 007ca120 bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9a7a54e25a18b65d92982fb97ef9404"></a>

### [`007ca13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca13c.md) → [`007ca13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca13c.md) FUN_007ca13c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00459f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459f50.md) [`007ca3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca3a8.md) [`007ca3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca3ac.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00459f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f50.md) [`007ca3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca3a8.md) [`007ca3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca3ac.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.89% / 新版 97.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ca1e4",
      "incomplete_value": false,
      "site": "007ca1e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ca1e4",
      "incomplete_value": false,
      "site": "007ca1e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:a18:8"
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
      "007ca1e4",
      "DATA",
      [
        "storage",
        "00bffa18",
        null,
        "undefined *"
      ]
    ],
    [
      "007ca280",
      "READ",
      [
        "storage",
        "00bffa38",
        null,
        "pointer"
      ]
    ],
    [
      "007ca280",
      "READ",
      [
        "storage",
        "00bffa40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ca1e4",
      "DATA",
      [
        "storage",
        "00bffa68",
        null,
        "undefined *"
      ]
    ],
    [
      "007ca280",
      "READ",
      [
        "storage",
        "00bffa88",
        null,
        "pointer"
      ]
    ],
    [
      "007ca280",
      "READ",
      [
        "storage",
        "00bffa90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ca1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca13c.md#insn-007ca1dc)
- 新版 [`007ca1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca13c.md#insn-007ca1dc)

~~~diff
- 007ca1dc ["COPY", "tmp:0:8", ["const:a18:8"]]
- 007ca1dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ca1dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ca1dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ca1dc ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 007ca1dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ca1dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ca1dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ca1dc bytes 29612891
+ 007ca1dc bytes 29a12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eeb864e717ca5583bd6d908d40921238"></a>

### [`007ca358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca358.md) → [`007ca358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca358.md) FUN_007ca358

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
      "definition_site": "007ca378",
      "incomplete_value": false,
      "site": "007ca37c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ca378",
      "incomplete_value": false,
      "site": "007ca37c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:a18:8"
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
      "007ca37c",
      "DATA",
      [
        "storage",
        "00bffa18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ca37c",
      "DATA",
      [
        "storage",
        "00bffa68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ca378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca358.md#insn-007ca378)
- 新版 [`007ca378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca358.md#insn-007ca378)

~~~diff
- 007ca378 ["COPY", "tmp:0:8", ["const:a18:8"]]
- 007ca378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ca378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ca378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ca378 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 007ca378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ca378 bytes 08612891
+ 007ca378 bytes 08a12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bd76002618a0b55eae46a4cf0f209b5"></a>

### [`007ca390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca390.md) → [`007ca390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca390.md) FUN_007ca390

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
      "definition_site": "007ca394",
      "incomplete_value": false,
      "site": "007ca398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ca394",
      "incomplete_value": false,
      "site": "007ca398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:a18:8"
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
      "007ca398",
      "DATA",
      [
        "storage",
        "00bffa18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ca398",
      "DATA",
      [
        "storage",
        "00bffa68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ca394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca390.md#insn-007ca394)
- 新版 [`007ca394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca390.md#insn-007ca394)

~~~diff
- 007ca394 ["COPY", "tmp:0:8", ["const:a18:8"]]
- 007ca394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ca394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ca394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ca394 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 007ca394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ca394 bytes 08612891
+ 007ca394 bytes 08a12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-468f82470634f0f3015616f949870793"></a>

### [`007ca3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca3b0.md) → [`007ca3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca3b0.md) FUN_007ca3b0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 23件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`0045a030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a030.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00574ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff4.md)
- 新版 呼出元 0件  · 呼出先 23件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`0045a030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a030.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00574ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff4.md)

変更の種類 call, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.33% / 新版 90.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ca4e8",
      "incomplete_value": true,
      "site": "007ca4e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a6a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ca4e8",
      "incomplete_value": true,
      "site": "007ca4e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9df:8"
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
      "definition_site": "007ca4ec",
      "incomplete_value": true,
      "site": "007ca4ec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007ca4ec",
      "incomplete_value": true,
      "site": "007ca4ec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007ca550",
      "incomplete_value": true,
      "site": "007ca564",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007ca550",
      "incomplete_value": true,
      "site": "007ca564",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007ca41c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a26cbc"
      ]
    ],
    [
      "007ca470",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a26cbc"
      ]
    ],
    [
      "007ca4d8",
      "READ",
      [
        "storage",
        "0029f9df",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007ca41c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a26d00"
      ]
    ],
    [
      "007ca470",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a26d00"
      ]
    ],
    [
      "007ca4d8",
      "READ",
      [
        "storage",
        "0029fa6a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ca41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca3b0.md#insn-007ca41c) · [`007ca470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca3b0.md#insn-007ca470) · [`007ca608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca3b0.md#insn-007ca608)
- 新版 [`007ca41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca3b0.md#insn-007ca41c) · [`007ca470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca3b0.md#insn-007ca470) · [`007ca608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca3b0.md#insn-007ca608)

~~~diff
- 007ca41c ["INT_ADD", "register:40f0:8", ["const:7ca41c:8", "const:4:8"]]
- 007ca41c ["CALL", null, ["ram:a26cbc:8"]]
+ 007ca41c ["INT_ADD", "register:40f0:8", ["const:7ca41c:8", "const:4:8"]]
+ 007ca41c ["CALL", null, ["ram:a26d00:8"]]
- 007ca41c bytes 28720994
+ 007ca41c bytes 39720994
- 007ca470 ["INT_ADD", "register:40f0:8", ["const:7ca470:8", "const:4:8"]]
- 007ca470 ["CALL", null, ["ram:a26cbc:8"]]
+ 007ca470 ["INT_ADD", "register:40f0:8", ["const:7ca470:8", "const:4:8"]]
+ 007ca470 ["CALL", null, ["ram:a26d00:8"]]
- 007ca470 bytes 13720994
+ 007ca470 bytes 24720994
- 007ca608 ["INT_ADD", "register:40f0:8", ["const:7ca608:8", "const:4:8"]]
- 007ca608 ["CALL", null, ["ram:a26cbc:8"]]
+ 007ca608 ["INT_ADD", "register:40f0:8", ["const:7ca608:8", "const:4:8"]]
+ 007ca608 ["CALL", null, ["ram:a26d00:8"]]
- 007ca608 bytes ad710994
+ 007ca608 bytes be710994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e46bea988dcd022df77b537413ecade7"></a>

### [`007ca9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca9e0.md) → [`007ca9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca9e0.md) FUN_007ca9e0

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
      "definition_site": "007ca9f4",
      "incomplete_value": false,
      "site": "007ca9f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ca9f4",
      "incomplete_value": false,
      "site": "007ca9f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
      "007ca9f8",
      "DATA",
      [
        "storage",
        "00bffa88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ca9f8",
      "DATA",
      [
        "storage",
        "00bffad8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ca9f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca9e0.md#insn-007ca9f4)
- 新版 [`007ca9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca9e0.md#insn-007ca9f4)

~~~diff
- 007ca9f4 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 007ca9f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ca9f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ca9f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ca9f4 ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 007ca9f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca9f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca9f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ca9f4 bytes 08212a91
+ 007ca9f4 bytes 08612b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff5265df1b30bcad5b04ed848bc33280"></a>

### [`007caa04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007caa04.md) → [`007caa04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007caa04.md) FUN_007caa04

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
      "definition_site": "007caa08",
      "incomplete_value": false,
      "site": "007caa0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007caa08",
      "incomplete_value": false,
      "site": "007caa0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
      "007caa0c",
      "DATA",
      [
        "storage",
        "00bffa88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007caa0c",
      "DATA",
      [
        "storage",
        "00bffad8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007caa08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007caa04.md#insn-007caa08)
- 新版 [`007caa08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007caa04.md#insn-007caa08)

~~~diff
- 007caa08 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 007caa08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007caa08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007caa08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007caa08 ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 007caa08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007caa08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007caa08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007caa08 bytes 08212a91
+ 007caa08 bytes 08612b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-952aa36c616c574add5bce1c8354736c"></a>

### [`007caab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007caab4.md) → [`007caab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007caab4.md) FUN_007caab4

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
      "definition_site": "007caab8",
      "incomplete_value": false,
      "site": "007caabc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007caab8",
      "incomplete_value": false,
      "site": "007caabc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:b08:8"
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
      "007caabc",
      "DATA",
      [
        "storage",
        "00bffb08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007caabc",
      "DATA",
      [
        "storage",
        "00bffb58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007caab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007caab4.md#insn-007caab8)
- 新版 [`007caab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007caab4.md#insn-007caab8)

~~~diff
- 007caab8 ["COPY", "tmp:0:8", ["const:b08:8"]]
- 007caab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007caab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007caab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007caab8 ["COPY", "tmp:0:8", ["const:b58:8"]]
+ 007caab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007caab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007caab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007caab8 bytes 08212c91
+ 007caab8 bytes 08612d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3028a2b31cad942bcf193561485794fd"></a>

### [`007cab40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007cab40.md) → [`007cab40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007cab40.md) FUN_007cab40

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
      "definition_site": "007cab60",
      "incomplete_value": false,
      "site": "007cab64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cab60",
      "incomplete_value": false,
      "site": "007cab64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      "007cab64",
      "DATA",
      [
        "storage",
        "00bffba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cab64",
      "DATA",
      [
        "storage",
        "00bffbf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cab60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007cab40.md#insn-007cab60)
- 新版 [`007cab60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007cab40.md#insn-007cab60)

~~~diff
- 007cab60 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 007cab60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cab60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cab60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cab60 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 007cab60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cab60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cab60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cab60 bytes 08a12e91
+ 007cab60 bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1473445ce24309cb938084bbcbd40ecf"></a>

### [`007cab78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007cab78.md) → [`007cab78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007cab78.md) FUN_007cab78

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
      "definition_site": "007cab80",
      "incomplete_value": false,
      "site": "007cab84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cab80",
      "incomplete_value": false,
      "site": "007cab84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      "007cab84",
      "DATA",
      [
        "storage",
        "00bffba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cab84",
      "DATA",
      [
        "storage",
        "00bffbf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cab80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007cab78.md#insn-007cab80)
- 新版 [`007cab80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007cab78.md#insn-007cab80)

~~~diff
- 007cab80 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 007cab80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cab80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cab80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cab80 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 007cab80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cab80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cab80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cab80 bytes 29a12e91
+ 007cab80 bytes 29e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-698974cbda2604c28e52949287a56996"></a>

### [`007cac74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007cac74.md) → [`007cac74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007cac74.md) FUN_007cac74

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
      "definition_site": "007cac88",
      "incomplete_value": false,
      "site": "007cac8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cac88",
      "incomplete_value": false,
      "site": "007cac8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "007cac8c",
      "DATA",
      [
        "storage",
        "00bffc28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cac8c",
      "DATA",
      [
        "storage",
        "00bffc78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cac88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007cac74.md#insn-007cac88)
- 新版 [`007cac88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007cac74.md#insn-007cac88)

~~~diff
- 007cac88 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 007cac88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cac88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cac88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cac88 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 007cac88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cac88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cac88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cac88 bytes 08a13091
+ 007cac88 bytes 08e13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18dd0b34d19915885d8dba0d2fc5d3c6"></a>

### [`007cac98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007cac98.md) → [`007cac98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007cac98.md) FUN_007cac98

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
      "definition_site": "007cac9c",
      "incomplete_value": false,
      "site": "007caca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cac9c",
      "incomplete_value": false,
      "site": "007caca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "007caca0",
      "DATA",
      [
        "storage",
        "00bffc28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007caca0",
      "DATA",
      [
        "storage",
        "00bffc78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cac9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007cac98.md#insn-007cac9c)
- 新版 [`007cac9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007cac98.md#insn-007cac9c)

~~~diff
- 007cac9c ["COPY", "tmp:0:8", ["const:c28:8"]]
- 007cac9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cac9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cac9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cac9c ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 007cac9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cac9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cac9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cac9c bytes 08a13091
+ 007cac9c bytes 08e13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57f7e1b1cdbab1441076337366cf5aa7"></a>

### [`007cad1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007cad1c.md) → [`007cad1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007cad1c.md) FUN_007cad1c

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
      "definition_site": "007cad40",
      "incomplete_value": false,
      "site": "007cad40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cad40",
      "incomplete_value": false,
      "site": "007cad40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
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
      "007cad40",
      "DATA",
      [
        "storage",
        "00bffca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cad40",
      "DATA",
      [
        "storage",
        "00bffcf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cad3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007cad1c.md#insn-007cad3c)
- 新版 [`007cad3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007cad1c.md#insn-007cad3c)

~~~diff
- 007cad3c ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 007cad3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cad3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cad3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cad3c ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 007cad3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cad3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cad3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cad3c bytes 08a13291
+ 007cad3c bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c66db28772a57ff8efeae88862e37da0"></a>

### [`007cae68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007cae68.md) → [`007cae68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007cae68.md) FUN_007cae68

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
      "definition_site": "007cae88",
      "incomplete_value": false,
      "site": "007cae8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cae88",
      "incomplete_value": false,
      "site": "007cae8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "007cae8c",
      "DATA",
      [
        "storage",
        "00bffd28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cae8c",
      "DATA",
      [
        "storage",
        "00bffd78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cae88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007cae68.md#insn-007cae88)
- 新版 [`007cae88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007cae68.md#insn-007cae88)

~~~diff
- 007cae88 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 007cae88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cae88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cae88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cae88 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 007cae88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cae88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cae88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cae88 bytes 08a13491
+ 007cae88 bytes 08e13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0d91148f58ec4c0c4fb5b980d223ea1"></a>

### [`007caea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007caea0.md) → [`007caea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007caea0.md) FUN_007caea0

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
      "definition_site": "007caea8",
      "incomplete_value": false,
      "site": "007caeac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007caea8",
      "incomplete_value": false,
      "site": "007caeac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "007caeac",
      "DATA",
      [
        "storage",
        "00bffd28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007caeac",
      "DATA",
      [
        "storage",
        "00bffd78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007caea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007caea0.md#insn-007caea8)
- 新版 [`007caea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007caea0.md#insn-007caea8)

~~~diff
- 007caea8 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 007caea8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007caea8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007caea8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007caea8 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 007caea8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007caea8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007caea8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007caea8 bytes 29a13491
+ 007caea8 bytes 29e13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73268922e3f5beb16ba3b8a1e1708b3a"></a>

### [`007caec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007caec0.md) → [`007caec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007caec0.md) FUN_007caec0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 17件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446784.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044592c.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446784.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 98.35% / 新版 98.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007caf1c",
      "incomplete_value": true,
      "site": "007caf1c",
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
      "definition_site": "007caf1c",
      "incomplete_value": true,
      "site": "007caf1c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007caf18",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007caf24",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007caf2c",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007caf18",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007caf24",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007caf2c",
      "PARAM",
      [
        "storage",
        "00bf4568",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007caf18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007caec0.md#insn-007caf18) · [`007caf24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007caec0.md#insn-007caf24) · [`007caf2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007caec0.md#insn-007caf2c)
- 新版 [`007caf18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007caec0.md#insn-007caf18) · [`007caf24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007caec0.md#insn-007caf24) · [`007caf2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007caec0.md#insn-007caf2c)

~~~diff
- 007caf18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007caf18 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007caf18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007caf18 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007caf18 bytes 003d45f9
+ 007caf18 bytes 005d45f9
- 007caf24 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007caf24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007caf24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007caf24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007caf24 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007caf24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007caf24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007caf24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007caf24 bytes 21203991
+ 007caf24 bytes 21603a91
- 007caf2c ["COPY", "tmp:0:8", ["const:518:8"]]
- 007caf2c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007caf2c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007caf2c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007caf2c ["COPY", "tmp:0:8", ["const:568:8"]]
+ 007caf2c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007caf2c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007caf2c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007caf2c bytes 42601491
+ 007caf2c bytes 42a01591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cbd59bf0291836a15640f219418331d"></a>

### [`007cb2e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cb2e8.md) → [`007cb2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cb2e8.md) FUN_007cb2e8

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
      "definition_site": "007cb2f4",
      "incomplete_value": false,
      "site": "007cb2f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cb2f4",
      "incomplete_value": false,
      "site": "007cb2f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:da8:8"
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
      "007cb2f4",
      "DATA",
      [
        "storage",
        "00bffda8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cb2f4",
      "DATA",
      [
        "storage",
        "00bffdf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cb2e8.md#insn-007cb2f0)
- 新版 [`007cb2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cb2e8.md#insn-007cb2f0)

~~~diff
- 007cb2f0 ["COPY", "tmp:0:8", ["const:da8:8"]]
- 007cb2f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cb2f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cb2f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cb2f0 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 007cb2f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cb2f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cb2f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cb2f0 bytes 29a13691
+ 007cb2f0 bytes 29e13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3882cf2b5e53614cc9d050633f9e5e3"></a>

### [`007cb37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cb37c.md) → [`007cb37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cb37c.md) FUN_007cb37c

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
      "definition_site": "007cb388",
      "incomplete_value": false,
      "site": "007cb38c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cb388",
      "incomplete_value": false,
      "site": "007cb38c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "007cb38c",
      "DATA",
      [
        "storage",
        "00bffe28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cb38c",
      "DATA",
      [
        "storage",
        "00bffe78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cb388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cb37c.md#insn-007cb388)
- 新版 [`007cb388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cb37c.md#insn-007cb388)

~~~diff
- 007cb388 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 007cb388 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cb388 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cb388 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cb388 ["COPY", "tmp:0:8", ["const:e78:8"]]
+ 007cb388 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cb388 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cb388 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cb388 bytes 29a13891
+ 007cb388 bytes 29e13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48d30d217c2612e327b25c925f53f24e"></a>

### [`007cb3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cb3a0.md) → [`007cb3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cb3a0.md) FUN_007cb3a0

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
      "definition_site": "007cb3a8",
      "incomplete_value": false,
      "site": "007cb3ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cb3a8",
      "incomplete_value": false,
      "site": "007cb3ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "007cb3ac",
      "DATA",
      [
        "storage",
        "00bffe28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cb3ac",
      "DATA",
      [
        "storage",
        "00bffe78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cb3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cb3a0.md#insn-007cb3a8)
- 新版 [`007cb3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cb3a0.md#insn-007cb3a8)

~~~diff
- 007cb3a8 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 007cb3a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cb3a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cb3a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cb3a8 ["COPY", "tmp:0:8", ["const:e78:8"]]
+ 007cb3a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cb3a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cb3a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cb3a8 bytes 29a13891
+ 007cb3a8 bytes 29e13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ae4555d10024da8c412eba4fb415ed4"></a>

### [`007cb4a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cb4a4.md) → [`007cb4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cb4a4.md) FUN_007cb4a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

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
      "definition_site": "007cb4dc",
      "incomplete_value": false,
      "site": "007cb4dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cb4dc",
      "incomplete_value": false,
      "site": "007cb4dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "007cb4dc",
      "DATA",
      [
        "storage",
        "00bffe28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cb4dc",
      "DATA",
      [
        "storage",
        "00bffe78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cb4d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cb4a4.md#insn-007cb4d8)
- 新版 [`007cb4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cb4a4.md#insn-007cb4d8)

~~~diff
- 007cb4d8 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 007cb4d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007cb4d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007cb4d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007cb4d8 ["COPY", "tmp:0:8", ["const:e78:8"]]
+ 007cb4d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007cb4d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007cb4d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007cb4d8 bytes 4aa13891
+ 007cb4d8 bytes 4ae13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6bffc6bd9093d7595f41a462d2a4fea"></a>

### [`007cb5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cb5a0.md) → [`007cb5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cb5a0.md) FUN_007cb5a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007cbcc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbcc0.md) [`007cbcc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbcc4.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`007cbcc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbcc0.md) [`007cbcc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbcc4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.51% / 新版 97.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007cb680",
      "incomplete_value": true,
      "site": "007cb690",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ea6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cb680",
      "incomplete_value": true,
      "site": "007cb690",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f33:8"
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
      "definition_site": "007cb6a8",
      "incomplete_value": false,
      "site": "007cb6b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cb6a8",
      "incomplete_value": false,
      "site": "007cb6b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:e98:8"
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
      "definition_site": "007cb6e8",
      "incomplete_value": true,
      "site": "007cb6fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fdf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cb6e8",
      "incomplete_value": true,
      "site": "007cb6fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6c:8"
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
      "007cb680",
      "READ",
      [
        "storage",
        "00295f33",
        null,
        "string"
      ]
    ],
    [
      "007cb6b0",
      "DATA",
      [
        "storage",
        "00bffe98",
        null,
        "undefined *"
      ]
    ],
    [
      "007cb6e8",
      "READ",
      [
        "storage",
        "0029806c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007cb680",
      "READ",
      [
        "storage",
        "00295ea6",
        null,
        "string"
      ]
    ],
    [
      "007cb6b0",
      "DATA",
      [
        "storage",
        "00bffee8",
        null,
        "undefined *"
      ]
    ],
    [
      "007cb6e8",
      "READ",
      [
        "storage",
        "00297fdf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cb678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cb5a0.md#insn-007cb678) · [`007cb6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cb5a0.md#insn-007cb6a8) · [`007cb6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cb5a0.md#insn-007cb6dc)
- 新版 [`007cb678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cb5a0.md#insn-007cb678) · [`007cb6a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cb5a0.md#insn-007cb6a8) · [`007cb6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cb5a0.md#insn-007cb6dc)

~~~diff
- 007cb678 ["COPY", "tmp:0:8", ["const:f33:8"]]
- 007cb678 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cb678 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cb678 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cb678 ["COPY", "tmp:0:8", ["const:ea6:8"]]
+ 007cb678 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cb678 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cb678 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cb678 bytes 29cd3c91
+ 007cb678 bytes 29993a91
- 007cb6a8 ["COPY", "tmp:0:8", ["const:e98:8"]]
- 007cb6a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cb6a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cb6a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cb6a8 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 007cb6a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cb6a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cb6a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cb6a8 bytes 08613a91
+ 007cb6a8 bytes 08a13b91
- 007cb6dc ["COPY", "register:4048:8", ["const:298000:8"]]
+ 007cb6dc ["COPY", "register:4048:8", ["const:297000:8"]]
- 007cb6dc bytes 69d6ffb0
+ 007cb6dc bytes 69d6ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29d35def660bd04e70756d4481454033"></a>

### [`007cbc8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbc8c.md) → [`007cbc8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbc8c.md) FUN_007cbc8c

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
      "definition_site": "007cbca0",
      "incomplete_value": false,
      "site": "007cbca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cbca0",
      "incomplete_value": false,
      "site": "007cbca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:e98:8"
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
      "007cbca4",
      "DATA",
      [
        "storage",
        "00bffe98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cbca4",
      "DATA",
      [
        "storage",
        "00bffee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cbca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbc8c.md#insn-007cbca0)
- 新版 [`007cbca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbc8c.md#insn-007cbca0)

~~~diff
- 007cbca0 ["COPY", "tmp:0:8", ["const:e98:8"]]
- 007cbca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cbca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cbca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cbca0 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 007cbca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cbca0 bytes 08613a91
+ 007cbca0 bytes 08a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a57adcabeb898017c18e822ab338db12"></a>

### [`007cbcb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbcb0.md) → [`007cbcb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbcb0.md) FUN_007cbcb0

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
      "definition_site": "007cbcb4",
      "incomplete_value": false,
      "site": "007cbcb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cbcb4",
      "incomplete_value": false,
      "site": "007cbcb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:e98:8"
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
      "007cbcb8",
      "DATA",
      [
        "storage",
        "00bffe98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cbcb8",
      "DATA",
      [
        "storage",
        "00bffee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cbcb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbcb0.md#insn-007cbcb4)
- 新版 [`007cbcb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbcb0.md#insn-007cbcb4)

~~~diff
- 007cbcb4 ["COPY", "tmp:0:8", ["const:e98:8"]]
- 007cbcb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cbcb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cbcb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cbcb4 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 007cbcb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbcb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbcb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cbcb4 bytes 08613a91
+ 007cbcb4 bytes 08a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb12d462a0e4d4e547ff8549d48a3ab9"></a>

### [`007cbd0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbd0c.md) → [`007cbd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbd0c.md) FUN_007cbd0c

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
      "definition_site": "007cbd20",
      "incomplete_value": false,
      "site": "007cbd24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cbd20",
      "incomplete_value": false,
      "site": "007cbd24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "007cbd24",
      "DATA",
      [
        "storage",
        "00bfff18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cbd24",
      "DATA",
      [
        "storage",
        "00bfff68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cbd20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbd0c.md#insn-007cbd20)
- 新版 [`007cbd20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbd0c.md#insn-007cbd20)

~~~diff
- 007cbd20 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 007cbd20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cbd20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cbd20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cbd20 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 007cbd20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbd20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbd20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cbd20 bytes 08613c91
+ 007cbd20 bytes 08a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1bf78b50f6be9ff823177cc89a64735"></a>

### [`007cbd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbd30.md) → [`007cbd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbd30.md) FUN_007cbd30

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
      "definition_site": "007cbd34",
      "incomplete_value": false,
      "site": "007cbd38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cbd34",
      "incomplete_value": false,
      "site": "007cbd38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "007cbd38",
      "DATA",
      [
        "storage",
        "00bfff18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cbd38",
      "DATA",
      [
        "storage",
        "00bfff68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cbd34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbd30.md#insn-007cbd34)
- 新版 [`007cbd34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbd30.md#insn-007cbd34)

~~~diff
- 007cbd34 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 007cbd34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cbd34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cbd34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cbd34 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 007cbd34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbd34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbd34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cbd34 bytes 08613c91
+ 007cbd34 bytes 08a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-403e433412b1556f9a34fac5aed6607c"></a>

### [`007cbd88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbd88.md) → [`007cbd88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbd88.md) FUN_007cbd88

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
      "definition_site": "007cbd94",
      "incomplete_value": false,
      "site": "007cbd98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cbd94",
      "incomplete_value": false,
      "site": "007cbd98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
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
      "007cbd98",
      "DATA",
      [
        "storage",
        "00bfffa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cbd98",
      "DATA",
      [
        "storage",
        "00bffff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cbd94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbd88.md#insn-007cbd94)
- 新版 [`007cbd94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbd88.md#insn-007cbd94)

~~~diff
- 007cbd94 ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 007cbd94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cbd94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cbd94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cbd94 ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 007cbd94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cbd94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cbd94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cbd94 bytes 29a13e91
+ 007cbd94 bytes 29e13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d92fff3b07c4c969731920b04fc555a8"></a>

### [`007cbdac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbdac.md) → [`007cbdac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbdac.md) FUN_007cbdac

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
      "definition_site": "007cbdb4",
      "incomplete_value": false,
      "site": "007cbdb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cbdb4",
      "incomplete_value": false,
      "site": "007cbdb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
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
      "007cbdb8",
      "DATA",
      [
        "storage",
        "00bfffa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cbdb8",
      "DATA",
      [
        "storage",
        "00bffff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cbdb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbdac.md#insn-007cbdb4)
- 新版 [`007cbdb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbdac.md#insn-007cbdb4)

~~~diff
- 007cbdb4 ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 007cbdb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cbdb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cbdb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cbdb4 ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 007cbdb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cbdb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cbdb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cbdb4 bytes 29a13e91
+ 007cbdb4 bytes 29e13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-576c18f2ee76cf1c50e5d8534fd28241"></a>

### [`007cbdec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbdec.md) → [`007cbdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbdec.md) FUN_007cbdec

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
      "definition_site": "007cbe1c",
      "incomplete_value": false,
      "site": "007cbe1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cbe1c",
      "incomplete_value": false,
      "site": "007cbe1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
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
      "007cbe1c",
      "DATA",
      [
        "storage",
        "00bfffa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cbe1c",
      "DATA",
      [
        "storage",
        "00bffff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cbe10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbdec.md#insn-007cbe10) · [`007cbe14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbdec.md#insn-007cbe14)
- 新版 [`007cbe10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbdec.md#insn-007cbe10) · [`007cbe14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbdec.md#insn-007cbe14)

~~~diff
- 007cbe10 ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 007cbe10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cbe10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cbe10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cbe10 ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 007cbe10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbe10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cbe10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cbe10 bytes 08a13e91
+ 007cbe10 bytes 08e13f91
- 007cbe14 ["COPY", "register:4098:8", ["register:4000:8"]]
- 007cbe14 bytes f30300aa
+ 007cbe14 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 007cbe14 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37998bb380ad704fea64546b8717848d"></a>

### [`007cc094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc094.md) → [`007cc094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc094.md) FUN_007cc094

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
      "definition_site": "007cc0b4",
      "incomplete_value": false,
      "site": "007cc0b8",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc0b4",
      "incomplete_value": false,
      "site": "007cc0b8",
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
            "const:28:8"
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
      "007cc0b8",
      "DATA",
      [
        "storage",
        "00c00028",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc0b8",
      "DATA",
      [
        "storage",
        "00c00078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc094.md#insn-007cc0b4)
- 新版 [`007cc0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc094.md#insn-007cc0b4)

~~~diff
- 007cc0b4 ["COPY", "tmp:0:8", ["const:28:8"]]
- 007cc0b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc0b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc0b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc0b4 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 007cc0b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc0b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc0b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc0b4 bytes 08a10091
+ 007cc0b4 bytes 08e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cf28b35f4d1de57becb133510ad887f"></a>

### [`007cc0cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc0cc.md) → [`007cc0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc0cc.md) FUN_007cc0cc

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
      "definition_site": "007cc0d0",
      "incomplete_value": false,
      "site": "007cc0d4",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc0d0",
      "incomplete_value": false,
      "site": "007cc0d4",
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
            "const:28:8"
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
      "007cc0d4",
      "DATA",
      [
        "storage",
        "00c00028",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc0d4",
      "DATA",
      [
        "storage",
        "00c00078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc0cc.md#insn-007cc0d0)
- 新版 [`007cc0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc0cc.md#insn-007cc0d0)

~~~diff
- 007cc0d0 ["COPY", "tmp:0:8", ["const:28:8"]]
- 007cc0d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc0d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc0d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc0d0 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 007cc0d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc0d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc0d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc0d0 bytes 08a10091
+ 007cc0d0 bytes 08e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89cb5cb8ef8287320deb5f3d0a7618dd"></a>

### [`007cc0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc0ec.md) → [`007cc0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc0ec.md) FUN_007cc0ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007cc37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc37c.md) [`007cc380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc380.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`007cc37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc37c.md) [`007cc380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc380.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.18% / 新版 98.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007cc208",
      "incomplete_value": false,
      "site": "007cc208",
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
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc208",
      "incomplete_value": false,
      "site": "007cc208",
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
            "const:98:8"
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
      "007cc208",
      "DATA",
      [
        "storage",
        "00c00098",
        null,
        "undefined *"
      ]
    ],
    [
      "007cc264",
      "READ",
      [
        "storage",
        "00c000b8",
        null,
        "pointer"
      ]
    ],
    [
      "007cc264",
      "READ",
      [
        "storage",
        "00c000c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc208",
      "DATA",
      [
        "storage",
        "00c000e8",
        null,
        "undefined *"
      ]
    ],
    [
      "007cc264",
      "READ",
      [
        "storage",
        "00c00108",
        null,
        "pointer"
      ]
    ],
    [
      "007cc264",
      "READ",
      [
        "storage",
        "00c00110",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc0ec.md#insn-007cc200)
- 新版 [`007cc200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc0ec.md#insn-007cc200)

~~~diff
- 007cc200 ["COPY", "tmp:0:8", ["const:98:8"]]
- 007cc200 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cc200 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cc200 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cc200 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 007cc200 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc200 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc200 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cc200 bytes 29610291
+ 007cc200 bytes 29a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12bd7ed9f42c10170b6c67b98282f9ea"></a>

### [`007cc32c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc32c.md) → [`007cc32c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc32c.md) FUN_007cc32c

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
      "definition_site": "007cc34c",
      "incomplete_value": false,
      "site": "007cc350",
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
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc34c",
      "incomplete_value": false,
      "site": "007cc350",
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
            "const:98:8"
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
      "007cc350",
      "DATA",
      [
        "storage",
        "00c00098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc350",
      "DATA",
      [
        "storage",
        "00c000e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc32c.md#insn-007cc34c)
- 新版 [`007cc34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc32c.md#insn-007cc34c)

~~~diff
- 007cc34c ["COPY", "tmp:0:8", ["const:98:8"]]
- 007cc34c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc34c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc34c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc34c ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 007cc34c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc34c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc34c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc34c bytes 08610291
+ 007cc34c bytes 08a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4b8c28fc4b9593a14e7aef5d7a334d0"></a>

### [`007cc364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc364.md) → [`007cc364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc364.md) FUN_007cc364

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
      "definition_site": "007cc368",
      "incomplete_value": false,
      "site": "007cc36c",
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
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc368",
      "incomplete_value": false,
      "site": "007cc36c",
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
            "const:98:8"
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
      "007cc36c",
      "DATA",
      [
        "storage",
        "00c00098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc36c",
      "DATA",
      [
        "storage",
        "00c000e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc364.md#insn-007cc368)
- 新版 [`007cc368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc364.md#insn-007cc368)

~~~diff
- 007cc368 ["COPY", "tmp:0:8", ["const:98:8"]]
- 007cc368 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc368 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc368 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc368 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 007cc368 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc368 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc368 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc368 bytes 08610291
+ 007cc368 bytes 08a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bc827b3b78dd74ff6ceb3f166e6469d"></a>

### [`007cc3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc3f8.md) → [`007cc3f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc3f8.md) FUN_007cc3f8

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
      "definition_site": "007cc418",
      "incomplete_value": false,
      "site": "007cc41c",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc418",
      "incomplete_value": false,
      "site": "007cc41c",
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
            "const:128:8"
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
      "007cc41c",
      "DATA",
      [
        "storage",
        "00c00128",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc41c",
      "DATA",
      [
        "storage",
        "00c00178",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc3f8.md#insn-007cc418)
- 新版 [`007cc418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc3f8.md#insn-007cc418)

~~~diff
- 007cc418 ["COPY", "tmp:0:8", ["const:128:8"]]
- 007cc418 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc418 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc418 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc418 ["COPY", "tmp:0:8", ["const:178:8"]]
+ 007cc418 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc418 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc418 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc418 bytes 08a10491
+ 007cc418 bytes 08e10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e08a900d2362bc758309d706e4d7e75e"></a>

### [`007cc430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc430.md) → [`007cc430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc430.md) FUN_007cc430

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
      "definition_site": "007cc434",
      "incomplete_value": false,
      "site": "007cc438",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc434",
      "incomplete_value": false,
      "site": "007cc438",
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
            "const:128:8"
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
      "007cc438",
      "DATA",
      [
        "storage",
        "00c00128",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc438",
      "DATA",
      [
        "storage",
        "00c00178",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc430.md#insn-007cc434)
- 新版 [`007cc434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc430.md#insn-007cc434)

~~~diff
- 007cc434 ["COPY", "tmp:0:8", ["const:128:8"]]
- 007cc434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc434 ["COPY", "tmp:0:8", ["const:178:8"]]
+ 007cc434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc434 bytes 08a10491
+ 007cc434 bytes 08e10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-105f02449b2681901a77daf287432f8f"></a>

### [`007cc450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc450.md) → [`007cc450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc450.md) FUN_007cc450

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007cc658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc658.md) [`007cc65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc65c.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`007cc658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc658.md) [`007cc65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc65c.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007cc4f0",
      "incomplete_value": false,
      "site": "007cc4f0",
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
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc4f0",
      "incomplete_value": false,
      "site": "007cc4f0",
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
            "const:198:8"
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
      "007cc4f0",
      "DATA",
      [
        "storage",
        "00c00198",
        null,
        "undefined *"
      ]
    ],
    [
      "007cc548",
      "READ",
      [
        "storage",
        "00c001b8",
        null,
        "pointer"
      ]
    ],
    [
      "007cc548",
      "READ",
      [
        "storage",
        "00c001c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc4f0",
      "DATA",
      [
        "storage",
        "00c001e8",
        null,
        "undefined *"
      ]
    ],
    [
      "007cc548",
      "READ",
      [
        "storage",
        "00c00208",
        null,
        "pointer"
      ]
    ],
    [
      "007cc548",
      "READ",
      [
        "storage",
        "00c00210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc450.md#insn-007cc4e8) · [`007cc4ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc450.md#insn-007cc4ec)
- 新版 [`007cc4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc450.md#insn-007cc4e8) · [`007cc4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc450.md#insn-007cc4ec)

~~~diff
- 007cc4e8 ["COPY", "tmp:0:8", ["const:198:8"]]
- 007cc4e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc4e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc4e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc4e8 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 007cc4e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc4e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc4e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc4e8 bytes 08610691
+ 007cc4e8 bytes 08a10791
- 007cc4ec ["COPY", "tmp:0:8", ["const:20:8"]]
- 007cc4ec ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 007cc4ec ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 007cc4ec ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 007cc4ec bytes f3830091
+ 007cc4ec ["COPY", "tmp:0:8", ["const:20:8"]]
+ 007cc4ec ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
+ 007cc4ec ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
+ 007cc4ec ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
+ 007cc4ec bytes f3830091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30f70f19427e73bd1a6bc29d370d161f"></a>

### [`007cc610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc610.md) → [`007cc610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc610.md) FUN_007cc610

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
      "definition_site": "007cc634",
      "incomplete_value": false,
      "site": "007cc634",
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
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc634",
      "incomplete_value": false,
      "site": "007cc634",
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
      "007cc634",
      "DATA",
      [
        "storage",
        "00c00198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc634",
      "DATA",
      [
        "storage",
        "00c001e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc610.md#insn-007cc630)
- 新版 [`007cc630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc610.md#insn-007cc630)

~~~diff
- 007cc630 ["COPY", "tmp:0:8", ["const:198:8"]]
- 007cc630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc630 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 007cc630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc630 bytes 08610691
+ 007cc630 bytes 08a10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7103a786a568d673029f7d78bc01812c"></a>

### [`007cc644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc644.md) → [`007cc644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc644.md) FUN_007cc644

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
      "definition_site": "007cc650",
      "incomplete_value": false,
      "site": "007cc650",
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
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc650",
      "incomplete_value": false,
      "site": "007cc650",
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
      "007cc650",
      "DATA",
      [
        "storage",
        "00c00198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc650",
      "DATA",
      [
        "storage",
        "00c001e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc644.md#insn-007cc64c)
- 新版 [`007cc64c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc644.md#insn-007cc64c)

~~~diff
- 007cc64c ["COPY", "tmp:0:8", ["const:198:8"]]
- 007cc64c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cc64c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cc64c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cc64c ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 007cc64c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc64c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc64c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cc64c bytes 29610691
+ 007cc64c bytes 29a10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7900f74b2eae193535e0a24c5a844922"></a>

### [`007cc6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc6d4.md) → [`007cc6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc6d4.md) FUN_007cc6d4

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
      "definition_site": "007cc6f8",
      "incomplete_value": false,
      "site": "007cc6f8",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc6f8",
      "incomplete_value": false,
      "site": "007cc6f8",
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
            "const:228:8"
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
      "007cc6f8",
      "DATA",
      [
        "storage",
        "00c00228",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc6f8",
      "DATA",
      [
        "storage",
        "00c00278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc6d4.md#insn-007cc6f4)
- 新版 [`007cc6f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc6d4.md#insn-007cc6f4)

~~~diff
- 007cc6f4 ["COPY", "tmp:0:8", ["const:228:8"]]
- 007cc6f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc6f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc6f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc6f4 ["COPY", "tmp:0:8", ["const:278:8"]]
+ 007cc6f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc6f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc6f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc6f4 bytes 08a10891
+ 007cc6f4 bytes 08e10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f09f72b463f875f6e790d50d3e6ac91e"></a>

### [`007cc708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc708.md) → [`007cc708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc708.md) FUN_007cc708

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
      "definition_site": "007cc714",
      "incomplete_value": false,
      "site": "007cc714",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc714",
      "incomplete_value": false,
      "site": "007cc714",
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
      "007cc714",
      "DATA",
      [
        "storage",
        "00c00228",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc714",
      "DATA",
      [
        "storage",
        "00c00278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc708.md#insn-007cc710)
- 新版 [`007cc710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc708.md#insn-007cc710)

~~~diff
- 007cc710 ["COPY", "tmp:0:8", ["const:228:8"]]
- 007cc710 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cc710 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cc710 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cc710 ["COPY", "tmp:0:8", ["const:278:8"]]
+ 007cc710 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc710 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc710 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cc710 bytes 29a10891
+ 007cc710 bytes 29e10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fa0a907495626ce0fee618463bcf68c"></a>

### [`007cc7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc7c4.md) → [`007cc7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc7c4.md) FUN_007cc7c4

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
      "definition_site": "007cc7cc",
      "incomplete_value": false,
      "site": "007cc7d0",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc7cc",
      "incomplete_value": false,
      "site": "007cc7d0",
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
      "007cc7d0",
      "DATA",
      [
        "storage",
        "00c002a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc7d0",
      "DATA",
      [
        "storage",
        "00c002f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc7cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc7c4.md#insn-007cc7cc)
- 新版 [`007cc7cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc7c4.md#insn-007cc7cc)

~~~diff
- 007cc7cc ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 007cc7cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cc7cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cc7cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cc7cc ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 007cc7cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc7cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc7cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cc7cc bytes 29a10a91
+ 007cc7cc bytes 29e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af85dd58bae802ed2ae17d0578144117"></a>

### [`007cc7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc7e4.md) → [`007cc7e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc7e4.md) FUN_007cc7e4

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
      "definition_site": "007cc7ec",
      "incomplete_value": false,
      "site": "007cc7f0",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc7ec",
      "incomplete_value": false,
      "site": "007cc7f0",
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
      "007cc7f0",
      "DATA",
      [
        "storage",
        "00c002a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc7f0",
      "DATA",
      [
        "storage",
        "00c002f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc7ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc7e4.md#insn-007cc7ec)
- 新版 [`007cc7ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc7e4.md#insn-007cc7ec)

~~~diff
- 007cc7ec ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 007cc7ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cc7ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cc7ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cc7ec ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 007cc7ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc7ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc7ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cc7ec bytes 29a10a91
+ 007cc7ec bytes 29e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69a7bfcce1e60d812f29bd7141ad378c"></a>

### [`007cc824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc824.md) → [`007cc824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc824.md) FUN_007cc824

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "007cc858",
      "incomplete_value": false,
      "site": "007cc858",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc858",
      "incomplete_value": false,
      "site": "007cc858",
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
      "007cc858",
      "DATA",
      [
        "storage",
        "00c002a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc858",
      "DATA",
      [
        "storage",
        "00c002f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc824.md#insn-007cc848)
- 新版 [`007cc848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc824.md#insn-007cc848)

~~~diff
- 007cc848 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 007cc848 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cc848 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cc848 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cc848 ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 007cc848 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc848 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cc848 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cc848 bytes 29a10a91
+ 007cc848 bytes 29e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8a2a925bebd3adfa0d41a87d9624358"></a>

### [`007cc8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc8a8.md) → [`007cc8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc8a8.md) FUN_007cc8a8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)

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
      "definition_site": "007cc8ac",
      "incomplete_value": false,
      "site": "007cc8b0",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cc8ac",
      "incomplete_value": false,
      "site": "007cc8b0",
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
      "007cc8b0",
      "DATA",
      [
        "storage",
        "00c002a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cc8b0",
      "DATA",
      [
        "storage",
        "00c002f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cc8ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc8a8.md#insn-007cc8ac)
- 新版 [`007cc8ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc8a8.md#insn-007cc8ac)

~~~diff
- 007cc8ac ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 007cc8ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cc8ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cc8ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cc8ac ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 007cc8ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc8ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cc8ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cc8ac bytes 08a10a91
+ 007cc8ac bytes 08e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19d77edaf0d42c6a51c43c400030137e"></a>

### [`007cc93c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc93c.md) → [`007cc93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc93c.md) FUN_007cc93c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007ccbb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007ccbb4.md) [`007ccbb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007ccbb8.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`007ccbb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007ccbb4.md) [`007ccbb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007ccbb8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.20% / 新版 98.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007cca08",
      "incomplete_value": false,
      "site": "007cca10",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cca08",
      "incomplete_value": false,
      "site": "007cca10",
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
            "const:318:8"
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
      "007cca10",
      "DATA",
      [
        "storage",
        "00c00318",
        null,
        "undefined *"
      ]
    ],
    [
      "007ccab4",
      "READ",
      [
        "storage",
        "00c00338",
        null,
        "pointer"
      ]
    ],
    [
      "007ccab4",
      "READ",
      [
        "storage",
        "00c00340",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007cca10",
      "DATA",
      [
        "storage",
        "00c00368",
        null,
        "undefined *"
      ]
    ],
    [
      "007ccab4",
      "READ",
      [
        "storage",
        "00c00388",
        null,
        "pointer"
      ]
    ],
    [
      "007ccab4",
      "READ",
      [
        "storage",
        "00c00390",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc93c.md#insn-007cca08)
- 新版 [`007cca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc93c.md#insn-007cca08)

~~~diff
- 007cca08 ["COPY", "tmp:0:8", ["const:318:8"]]
- 007cca08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cca08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cca08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cca08 ["COPY", "tmp:0:8", ["const:368:8"]]
+ 007cca08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cca08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cca08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cca08 bytes 08610c91
+ 007cca08 bytes 08a10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d9240444a3fc8b546a6fef59ed989d3"></a>

### [`007ccb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007ccb80.md) → [`007ccb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007ccb80.md) FUN_007ccb80

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
      "definition_site": "007ccb94",
      "incomplete_value": false,
      "site": "007ccb98",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ccb94",
      "incomplete_value": false,
      "site": "007ccb98",
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
            "const:318:8"
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
      "007ccb98",
      "DATA",
      [
        "storage",
        "00c00318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ccb98",
      "DATA",
      [
        "storage",
        "00c00368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ccb94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007ccb80.md#insn-007ccb94)
- 新版 [`007ccb94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007ccb80.md#insn-007ccb94)

~~~diff
- 007ccb94 ["COPY", "tmp:0:8", ["const:318:8"]]
- 007ccb94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ccb94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ccb94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ccb94 ["COPY", "tmp:0:8", ["const:368:8"]]
+ 007ccb94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ccb94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ccb94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ccb94 bytes 08610c91
+ 007ccb94 bytes 08a10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34d1d951ff0c454440dede471d7fdecf"></a>

### [`007ccba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007ccba4.md) → [`007ccba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007ccba4.md) FUN_007ccba4

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
      "definition_site": "007ccba8",
      "incomplete_value": true,
      "site": "007ccbac",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ccba8",
      "incomplete_value": true,
      "site": "007ccbac",
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
            "const:318:8"
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
      "007ccbac",
      "DATA",
      [
        "storage",
        "00c00318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ccbac",
      "DATA",
      [
        "storage",
        "00c00368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ccba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007ccba4.md#insn-007ccba8)
- 新版 [`007ccba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007ccba4.md#insn-007ccba8)

~~~diff
- 007ccba8 ["COPY", "tmp:0:8", ["const:318:8"]]
- 007ccba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ccba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ccba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ccba8 ["COPY", "tmp:0:8", ["const:368:8"]]
+ 007ccba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ccba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ccba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ccba8 bytes 08610c91
+ 007ccba8 bytes 08a10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-addc45ff68466ae22a06994af49bdaf5"></a>

### [`007ccd70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007ccd70.md) → [`007ccd70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007ccd70.md) _INIT_141

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
      "definition_site": "007ccdac",
      "incomplete_value": true,
      "site": "007ccdc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007ccdac",
      "incomplete_value": true,
      "site": "007ccdc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007ccdd0",
      "incomplete_value": true,
      "site": "007ccdec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007ccdd0",
      "incomplete_value": true,
      "site": "007ccdec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007ccdf0",
      "incomplete_value": true,
      "site": "007cce0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007ccdf0",
      "incomplete_value": true,
      "site": "007cce0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "007ccdac",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "007ccdd0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "007ccdf0",
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
      "007ccdac",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "007ccdd0",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "007ccdf0",
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

- 旧版 [`007ccd9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007ccd70.md#insn-007ccd9c) · [`007ccda4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007ccd70.md#insn-007ccda4)
- 新版 [`007ccd9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007ccd70.md#insn-007ccd9c) · [`007ccda4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007ccd70.md#insn-007ccda4)

~~~diff
- 007ccd9c ["COPY", "tmp:0:8", ["const:28:8"]]
- 007ccd9c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 007ccd9c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 007ccd9c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 007ccd9c ["COPY", "tmp:0:8", ["const:68:8"]]
+ 007ccd9c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 007ccd9c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 007ccd9c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 007ccd9c bytes 73a20091
+ 007ccd9c bytes 73a20191
- 007ccda4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 007ccda4 bytes c9d6fff0
+ 007ccda4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 007ccda4 bytes c9d6fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c41c2bc683e540dd2879e6494b9635a4"></a>

### [`007cd8ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd8ac.md) → [`007cd8ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd8ac.md) FUN_007cd8ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0044dabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044dabc.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0044dabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044dabc.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 99.10% / 新版 99.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007cd8f0",
      "incomplete_value": false,
      "site": "007cd8fc",
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
      "definition_site": "007cd8f0",
      "incomplete_value": false,
      "site": "007cd8fc",
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
      "definition_site": "007ce868",
      "incomplete_value": true,
      "site": "007ce874",
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
      "definition_site": "007ce868",
      "incomplete_value": true,
      "site": "007ce874",
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
    "ordinal": 231,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "007ce880",
      "incomplete_value": true,
      "site": "007ce880",
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:48:8"
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
      "definition_site": "007ce880",
      "incomplete_value": true,
      "site": "007ce880",
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:48:8"
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
    "ordinal": 232,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007cd8fc",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "007cda6c",
      "READ",
      [
        "storage",
        "00292cf1",
        null,
        "string"
      ]
    ],
    [
      "007cda80",
      "READ",
      [
        "storage",
        "00292cf7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007cd8fc",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "007cda6c",
      "READ",
      [
        "storage",
        "00292c64",
        null,
        "string"
      ]
    ],
    [
      "007cda80",
      "READ",
      [
        "storage",
        "00292c6a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cd8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd8ac.md#insn-007cd8f0) · [`007cda68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd8ac.md#insn-007cda68) · [`007ce85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd8ac.md#insn-007ce85c)
- 新版 [`007cd8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd8ac.md#insn-007cd8f0) · [`007cda68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd8ac.md#insn-007cda68) · [`007ce85c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd8ac.md#insn-007ce85c)

~~~diff
- 007cd8f0 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 007cd8f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cd8f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cd8f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cd8f0 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 007cd8f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cd8f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cd8f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cd8f0 bytes 08a13491
+ 007cd8f0 bytes 08e13591
- 007cda68 ["COPY", "tmp:0:8", ["const:cf1:8"]]
- 007cda68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007cda68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007cda68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007cda68 ["COPY", "tmp:0:8", ["const:c64:8"]]
+ 007cda68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007cda68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007cda68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007cda68 bytes 29c53391
+ 007cda68 bytes 29913191
- 007ce85c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 007ce85c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007ce85c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 007ce85c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007ce85c bytes 08b946f9
+ 007ce85c bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f56fbb0f19ee5561832be6196a1ffe47"></a>

### [`007d22d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d2/007d22d4.md) → [`007d22d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d2/007d22d4.md) FUN_007d22d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 36件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e8d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e8/005e8d4c.md) [`005e97d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e9/005e97d8.md) [`0065042c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00650/0065042c.md) [`00651720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00651/00651720.md) · 呼出先 3件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`007db210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007db210.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 36件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e8d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e8/005e8d4c.md) [`005e97d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e9/005e97d8.md) [`0065042c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/0065042c.md) [`00651720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00651/00651720.md) · 呼出先 3件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`007db210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007db/007db210.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.86% / 新版 98.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007d242c",
      "incomplete_value": false,
      "site": "007d2430",
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
      "definition_site": "007d242c",
      "incomplete_value": false,
      "site": "007d2430",
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
      "007d242c",
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
      "007d242c",
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

- 旧版 [`007d242c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d2/007d22d4.md#insn-007d242c)
- 新版 [`007d242c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d2/007d22d4.md#insn-007d242c)

~~~diff
- 007d242c ["COPY", "tmp:0:8", ["const:5cf:8"]]
- 007d242c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007d242c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007d242c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007d242c ["COPY", "tmp:0:8", ["const:65a:8"]]
+ 007d242c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007d242c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007d242c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007d242c bytes 003c1791
+ 007d242c bytes 00681991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34e16a21e6d7be99d1ede7b7ca7c7b2f"></a>

### [`007d48f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d4/007d48f8.md) → [`007d48f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d4/007d48f8.md) FUN_007d48f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 21件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 21件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 96.61% / 新版 96.61%

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
      "definition_site": "007d493c",
      "incomplete_value": false,
      "site": "007d4948",
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
      "definition_site": "007d493c",
      "incomplete_value": false,
      "site": "007d4948",
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
      "definition_site": "007d4ac0",
      "incomplete_value": true,
      "site": "007d4ae0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d31:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007d4ac0",
      "incomplete_value": true,
      "site": "007d4ae0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dbe:8"
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
      "definition_site": "007d5400",
      "incomplete_value": true,
      "site": "007d5404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "007d5400",
      "incomplete_value": true,
      "site": "007d5404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 151,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007d4948",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "007d495c",
      "READ",
      [
        "storage",
        "00291ee1",
        null,
        "string"
      ]
    ],
    [
      "007d4ac0",
      "READ",
      [
        "storage",
        "00294dbe",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007d4948",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "007d495c",
      "READ",
      [
        "storage",
        "00291e54",
        null,
        "string"
      ]
    ],
    [
      "007d4ac0",
      "READ",
      [
        "storage",
        "00294d31",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007d493c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d4/007d48f8.md#insn-007d493c) · [`007d4950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d4/007d48f8.md#insn-007d4950)
- 新版 [`007d493c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d4/007d48f8.md#insn-007d493c) · [`007d4950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d4/007d48f8.md#insn-007d4950)

~~~diff
- 007d493c ["COPY", "tmp:0:8", ["const:d28:8"]]
- 007d493c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007d493c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007d493c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007d493c ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 007d493c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007d493c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007d493c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007d493c bytes 08a13491
+ 007d493c bytes 08e13591
- 007d4950 ["COPY", "register:4048:8", ["const:291000:8"]]
- 007d4950 bytes e9d5ffb0
+ 007d4950 ["COPY", "register:4048:8", ["const:291000:8"]]
+ 007d4950 bytes e9d5ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1799a7d30007730eab70d40d3657bee7"></a>

### [`007d7f14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d7/007d7f14.md) → [`007d7f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7f14.md) FUN_007d7f14

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`007d55c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d5/007d55c8.md) [`00a5e6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5e/00a5e6e0.md) [`00a5f0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f0e4.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 3件 [`007d55c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d5/007d55c8.md) [`00a5e724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e724.md) [`00a5f128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f128.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "007d7f20",
      "incomplete_value": false,
      "site": "007d7f24",
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
      "definition_site": "007d7f20",
      "incomplete_value": false,
      "site": "007d7f24",
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
      "007d7f20",
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
      "007d7f20",
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

- 旧版 [`007d7f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d7/007d7f14.md#insn-007d7f20)
- 新版 [`007d7f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7f14.md#insn-007d7f20)

~~~diff
- 007d7f20 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007d7f20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007d7f20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007d7f20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007d7f20 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007d7f20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007d7f20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007d7f20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007d7f20 bytes 000c0c91
+ 007d7f20 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f4bcff478bd0bd0460599444848c52b"></a>

### [`007d7f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d7/007d7f28.md) → [`007d7f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7f28.md) _INIT_142

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`007cd858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd858.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`007cd858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd858.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 83.86% / 新版 83.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 9件, `store_value` 7件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007d7f68",
      "incomplete_value": true,
      "site": "007d7f84",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007d7f68",
      "incomplete_value": true,
      "site": "007d7f84",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007d7f8c",
      "incomplete_value": true,
      "site": "007d7fa8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007d7f8c",
      "incomplete_value": true,
      "site": "007d7fa8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007d7fac",
      "incomplete_value": true,
      "site": "007d7fc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007d7fac",
      "incomplete_value": true,
      "site": "007d7fc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007d7f68",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "007d7f8c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "007d7fac",
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
      "007d7f68",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "007d7f8c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "007d7fac",
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

- 旧版 [`007d8164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d7/007d7f28.md#insn-007d8164) · [`007d7f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d7/007d7f28.md#insn-007d7f58)
- 新版 [`007d8164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7f28.md#insn-007d8164) · [`007d7f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d7/007d7f28.md#insn-007d7f58)

~~~diff
- 007d8164 ["INT_ADD", "register:40f0:8", ["const:7d8164:8", "const:4:8"]]
- 007d8164 ["CALL", null, ["callee:00bdafe0:8"]]
- 007d8164 bytes 8b0b1094
+ 007d8164 ["INT_ADD", "register:40f0:8", ["const:7d8164:8", "const:4:8"]]
+ 007d8164 ["CALL", null, ["callee:00bdafe0:8"]]
+ 007d8164 bytes 9f0b1094
- 007d7f58 ["COPY", "tmp:0:8", ["const:40:8"]]
- 007d7f58 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 007d7f58 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 007d7f58 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 007d7f58 ["COPY", "tmp:0:8", ["const:80:8"]]
+ 007d7f58 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 007d7f58 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 007d7f58 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 007d7f58 bytes 73020191
+ 007d7f58 bytes 73020291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

