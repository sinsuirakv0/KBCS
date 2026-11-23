# v15.7.3 → v15.7.4 · 最優先の変更候補 (34)

[一覧の目次](README.md)

<a id="compare-602e29d0af1a3d07f54a116586456889"></a>

### [`0075b098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b098.md) → [`0075b098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b098.md) FUN_0075b098

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
      "definition_site": "0075b0ac",
      "incomplete_value": false,
      "site": "0075b0b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075b0ac",
      "incomplete_value": false,
      "site": "0075b0b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
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
      "0075b0b0",
      "DATA",
      [
        "storage",
        "00bfbca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075b0b0",
      "DATA",
      [
        "storage",
        "00bfbcf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075b0ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b098.md#insn-0075b0ac)
- 新版 [`0075b0ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b098.md#insn-0075b0ac)

~~~diff
- 0075b0ac ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 0075b0ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075b0ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075b0ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075b0ac ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 0075b0ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b0ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b0ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075b0ac bytes 08a13291
+ 0075b0ac bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-795f16ec13d8a95ac773ed1899d73709"></a>

### [`0075b0bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b0bc.md) → [`0075b0bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b0bc.md) FUN_0075b0bc

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
      "definition_site": "0075b0c0",
      "incomplete_value": false,
      "site": "0075b0c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075b0c0",
      "incomplete_value": false,
      "site": "0075b0c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
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
      "0075b0c4",
      "DATA",
      [
        "storage",
        "00bfbca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075b0c4",
      "DATA",
      [
        "storage",
        "00bfbcf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075b0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b0bc.md#insn-0075b0c0)
- 新版 [`0075b0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b0bc.md#insn-0075b0c0)

~~~diff
- 0075b0c0 ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 0075b0c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075b0c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075b0c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075b0c0 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 0075b0c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b0c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b0c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075b0c0 bytes 08a13291
+ 0075b0c0 bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ec7018c8763f2d093f2f2c4b7c84a71"></a>

### [`0075b1fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b1fc.md) → [`0075b1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b1fc.md) FUN_0075b1fc

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
      "definition_site": "0075b210",
      "incomplete_value": false,
      "site": "0075b214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075b210",
      "incomplete_value": false,
      "site": "0075b214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "0075b214",
      "DATA",
      [
        "storage",
        "00bfbd28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075b214",
      "DATA",
      [
        "storage",
        "00bfbd78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075b210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b1fc.md#insn-0075b210)
- 新版 [`0075b210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b1fc.md#insn-0075b210)

~~~diff
- 0075b210 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0075b210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075b210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075b210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075b210 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 0075b210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075b210 bytes 08a13491
+ 0075b210 bytes 08e13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47887d757f911bc15b6cc387d4aef4dc"></a>

### [`0075b220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b220.md) → [`0075b220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b220.md) FUN_0075b220

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
      "definition_site": "0075b224",
      "incomplete_value": false,
      "site": "0075b228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075b224",
      "incomplete_value": false,
      "site": "0075b228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
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
      "0075b228",
      "DATA",
      [
        "storage",
        "00bfbd28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075b228",
      "DATA",
      [
        "storage",
        "00bfbd78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075b224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b220.md#insn-0075b224)
- 新版 [`0075b224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b220.md#insn-0075b224)

~~~diff
- 0075b224 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0075b224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075b224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075b224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075b224 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 0075b224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075b224 bytes 08a13491
+ 0075b224 bytes 08e13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c071ff82d9bafdae2669080dcd5d5cf"></a>

### [`0075b2a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b2a8.md) → [`0075b2a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b2a8.md) FUN_0075b2a8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0074ff74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0074f/0074ff74.md) [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 2件 [`0074ff74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0074f/0074ff74.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "0075b2b4",
      "incomplete_value": false,
      "site": "0075b2b8",
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
      "definition_site": "0075b2b4",
      "incomplete_value": false,
      "site": "0075b2b8",
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
      "0075b2b4",
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
      "0075b2b4",
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

- 旧版 [`0075b2b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b2a8.md#insn-0075b2b4)
- 新版 [`0075b2b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b2a8.md#insn-0075b2b4)

~~~diff
- 0075b2b4 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0075b2b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0075b2b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0075b2b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0075b2b4 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0075b2b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0075b2b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0075b2b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0075b2b4 bytes 000c0c91
+ 0075b2b4 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-124c3db671665c8f0dde77f665589326"></a>

### [`0075b2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b2c0.md) → [`0075b2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b2c0.md) FUN_0075b2c0

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
      "definition_site": "0075b2e0",
      "incomplete_value": false,
      "site": "0075b2e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075b2e0",
      "incomplete_value": false,
      "site": "0075b2e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:da8:8"
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
      "0075b2e4",
      "DATA",
      [
        "storage",
        "00bfbda8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075b2e4",
      "DATA",
      [
        "storage",
        "00bfbdf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075b2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b2c0.md#insn-0075b2e0)
- 新版 [`0075b2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b2c0.md#insn-0075b2e0)

~~~diff
- 0075b2e0 ["COPY", "tmp:0:8", ["const:da8:8"]]
- 0075b2e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075b2e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075b2e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075b2e0 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 0075b2e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b2e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b2e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075b2e0 bytes 08a13691
+ 0075b2e0 bytes 08e13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d3ccb61e82db7cd509e2c7ca1691443"></a>

### [`0075b2f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b2f8.md) → [`0075b2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b2f8.md) FUN_0075b2f8

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
      "definition_site": "0075b2fc",
      "incomplete_value": false,
      "site": "0075b300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075b2fc",
      "incomplete_value": false,
      "site": "0075b300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
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
      "0075b300",
      "DATA",
      [
        "storage",
        "00bfbda8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075b300",
      "DATA",
      [
        "storage",
        "00bfbdf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075b2fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b2f8.md#insn-0075b2fc)
- 新版 [`0075b2fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b2f8.md#insn-0075b2fc)

~~~diff
- 0075b2fc ["COPY", "tmp:0:8", ["const:da8:8"]]
- 0075b2fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075b2fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075b2fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075b2fc ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 0075b2fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b2fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b2fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075b2fc bytes 08a13691
+ 0075b2fc bytes 08e13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-035a5240734adec3ca9fb9eb954202ae"></a>

### [`0075b414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b414.md) → [`0075b414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b414.md) FUN_0075b414

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
      "definition_site": "0075b438",
      "incomplete_value": false,
      "site": "0075b438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075b438",
      "incomplete_value": false,
      "site": "0075b438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "0075b438",
      "DATA",
      [
        "storage",
        "00bfbe28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075b438",
      "DATA",
      [
        "storage",
        "00bfbe78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075b434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b414.md#insn-0075b434)
- 新版 [`0075b434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b414.md#insn-0075b434)

~~~diff
- 0075b434 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 0075b434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075b434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075b434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075b434 ["COPY", "tmp:0:8", ["const:e78:8"]]
+ 0075b434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075b434 bytes 08a13891
+ 0075b434 bytes 08e13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f090e4d86b793dc266302bcb3ce8f180"></a>

### [`0075b448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b448.md) → [`0075b448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b448.md) FUN_0075b448

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
      "definition_site": "0075b454",
      "incomplete_value": false,
      "site": "0075b454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075b454",
      "incomplete_value": false,
      "site": "0075b454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
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
      "0075b454",
      "DATA",
      [
        "storage",
        "00bfbe28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075b454",
      "DATA",
      [
        "storage",
        "00bfbe78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075b450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b448.md#insn-0075b450)
- 新版 [`0075b450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b448.md#insn-0075b450)

~~~diff
- 0075b450 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 0075b450 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0075b450 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0075b450 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0075b450 ["COPY", "tmp:0:8", ["const:e78:8"]]
+ 0075b450 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0075b450 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0075b450 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0075b450 bytes 29a13891
+ 0075b450 bytes 29e13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be250ccf7a0fa06b52c38944d666aa34"></a>

### [`0075b4c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b4c8.md) → [`0075b4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b4c8.md) FUN_0075b4c8

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
      "definition_site": "0075b4ec",
      "incomplete_value": false,
      "site": "0075b4ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075b4ec",
      "incomplete_value": false,
      "site": "0075b4ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
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
      "0075b4ec",
      "DATA",
      [
        "storage",
        "00bfbea8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075b4ec",
      "DATA",
      [
        "storage",
        "00bfbef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075b4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b4c8.md#insn-0075b4e8)
- 新版 [`0075b4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b4c8.md#insn-0075b4e8)

~~~diff
- 0075b4e8 ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 0075b4e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075b4e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075b4e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075b4e8 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 0075b4e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b4e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b4e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075b4e8 bytes 08a13a91
+ 0075b4e8 bytes 08e13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b11c6ea08f1f96ef5b5b3300b300a45a"></a>

### [`0075b4fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b4fc.md) → [`0075b4fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b4fc.md) FUN_0075b4fc

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
      "definition_site": "0075b508",
      "incomplete_value": false,
      "site": "0075b508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075b508",
      "incomplete_value": false,
      "site": "0075b508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
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
      "0075b508",
      "DATA",
      [
        "storage",
        "00bfbea8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075b508",
      "DATA",
      [
        "storage",
        "00bfbef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075b504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b4fc.md#insn-0075b504)
- 新版 [`0075b504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b4fc.md#insn-0075b504)

~~~diff
- 0075b504 ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 0075b504 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0075b504 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0075b504 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0075b504 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 0075b504 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0075b504 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0075b504 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0075b504 bytes 29a13a91
+ 0075b504 bytes 29e13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-172ddd9ba2517293a36e31f2a506e0aa"></a>

### [`0075b518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b518.md) → [`0075b518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b518.md) FUN_0075b518

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`007cd2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd2ac.md) [`007d2db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d2/007d2db4.md) [`007d2e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d2/007d2e90.md) [`007d3cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d3/007d3cf0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`007cd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd2ac.md) [`007d2db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d2/007d2db4.md) [`007d2e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d2/007d2e90.md) [`007d3cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d3/007d3cf0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.73% / 新版 96.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0075b550",
      "incomplete_value": false,
      "site": "0075b55c",
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
      "definition_site": "0075b550",
      "incomplete_value": false,
      "site": "0075b55c",
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
      "0075b550",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "0075b75c",
      "PARAM",
      [
        "storage",
        "00299210",
        null,
        "string"
      ]
    ],
    [
      "0075b75c",
      "PARAM",
      [
        "storage",
        "00295e8a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0075b550",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "0075b75c",
      "PARAM",
      [
        "storage",
        "00299183",
        null,
        "string"
      ]
    ],
    [
      "0075b75c",
      "PARAM",
      [
        "storage",
        "00295dfd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075b550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b518.md#insn-0075b550) · [`0075b74c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b518.md#insn-0075b74c) · [`0075b754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b518.md#insn-0075b754)
- 新版 [`0075b550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b518.md#insn-0075b550) · [`0075b74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b518.md#insn-0075b74c)

~~~diff
- 0075b550 ["COPY", "tmp:0:8", ["const:866:8"]]
- 0075b550 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0075b550 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0075b550 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0075b550 ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 0075b550 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0075b550 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0075b550 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0075b550 bytes 21982191
+ 0075b550 bytes 21641f91
- 0075b74c ["COPY", "tmp:0:8", ["const:210:8"]]
- 0075b74c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075b74c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075b74c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075b74c ["COPY", "tmp:0:8", ["const:183:8"]]
+ 0075b74c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b74c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b74c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075b74c bytes 08410891
+ 0075b74c bytes 080d0691
- 0075b754 ["COPY", "register:4048:8", ["const:295000:8"]]
- 0075b754 bytes c9d9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f58805ec0a2fedb95653876de1c37bbd"></a>

### [`0075b7a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b7a4.md) → [`0075b7a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b7a4.md) _INIT_131

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
      "definition_site": "0075b7e0",
      "incomplete_value": true,
      "site": "0075b7fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0075b7e0",
      "incomplete_value": true,
      "site": "0075b7fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0075b804",
      "incomplete_value": true,
      "site": "0075b820",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0075b804",
      "incomplete_value": true,
      "site": "0075b820",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0075b824",
      "incomplete_value": true,
      "site": "0075b840",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0075b824",
      "incomplete_value": true,
      "site": "0075b840",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0075b7e0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0075b804",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0075b824",
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
      "0075b7e0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0075b804",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0075b824",
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

- 旧版 [`0075b7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b7a4.md#insn-0075b7d0) · [`0075b7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b7a4.md#insn-0075b7d8)
- 新版 [`0075b7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b7a4.md#insn-0075b7d0) · [`0075b7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b7a4.md#insn-0075b7d8)

~~~diff
- 0075b7d0 ["COPY", "tmp:0:8", ["const:ec8:8"]]
- 0075b7d0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0075b7d0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0075b7d0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0075b7d0 ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 0075b7d0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0075b7d0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0075b7d0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0075b7d0 bytes 73223b91
+ 0075b7d0 bytes 73223c91
- 0075b7d8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0075b7d8 bytes 69daff90
+ 0075b7d8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0075b7d8 bytes 69daff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af914a4266e66d429a29493056528200"></a>

### [`0075bf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075bf10.md) → [`0075bf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075bf10.md) FUN_0075bf10

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0075bc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075bc70.md) · 呼出先 14件 [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`0075dd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075d/0075dd30.md) [`0075dd34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075d/0075dd34.md) [`00883d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883d4c.md)
- 新版 呼出元 1件 [`0075bc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075bc70.md) · 呼出先 14件 [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`0075dd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075dd30.md) [`0075dd34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075dd34.md) [`00883d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883d4c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.25% / 新版 98.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0075c180",
      "incomplete_value": false,
      "site": "0075c180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075c180",
      "incomplete_value": false,
      "site": "0075c180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "0075c014",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "0075c028",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ],
    [
      "0075c040",
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
      "0075c014",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ],
    [
      "0075c028",
      "DATA",
      [
        "storage",
        "00c0bd38",
        null,
        "undefined *"
      ]
    ],
    [
      "0075c040",
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

- 旧版 [`0075c014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075bf10.md#insn-0075c014) · [`0075c040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075bf10.md#insn-0075c040) · [`0075c17c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075bf10.md#insn-0075c17c)
- 新版 [`0075c014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075bf10.md#insn-0075c014) · [`0075c040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075bf10.md#insn-0075c040) · [`0075c17c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075bf10.md#insn-0075c17c)

~~~diff
- 0075c014 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:520:8"]]
- 0075c014 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0075c014 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:570:8"]]
+ 0075c014 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 0075c014 bytes 7b9342f9
+ 0075c014 bytes 7bbb42f9
- 0075c040 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:528:8"]]
- 0075c040 ["LOAD", "register:40e0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0075c040 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:578:8"]]
+ 0075c040 ["LOAD", "register:40e0:8", ["const:1b1:8", "tmp:0:8"]]
- 0075c040 bytes 9c9742f9
+ 0075c040 bytes 9cbf42f9
- 0075c17c ["COPY", "tmp:0:8", ["const:f38:8"]]
- 0075c17c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075c17c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075c17c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075c17c ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 0075c17c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075c17c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075c17c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075c17c bytes 08e13c91
+ 0075c17c bytes 08213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-932b3e7897b8930aca10ba8fa1ad68f1"></a>

### [`0075c330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075c/0075c330.md) → [`0075c330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075c/0075c330.md) FUN_0075c330

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0075bc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075bc70.md) · 呼出先 13件 [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`0075dea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075d/0075dea0.md) [`00883e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883e08.md) [`009e964c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e964c.md) [`009e9790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e9790.md)
- 新版 呼出元 1件 [`0075bc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075bc70.md) · 呼出先 13件 [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`0075dea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075dea0.md) [`00883e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883e08.md) [`009e9690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9690.md) [`009e97d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e97d4.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "0075c464",
      "incomplete_value": true,
      "site": "0075c468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0075c464",
      "incomplete_value": true,
      "site": "0075c468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0075c518",
      "incomplete_value": false,
      "site": "0075c518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075c518",
      "incomplete_value": false,
      "site": "0075c518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
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
      "definition_site": "0075c5bc",
      "incomplete_value": true,
      "site": "0075c5c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0075c5bc",
      "incomplete_value": true,
      "site": "0075c5c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "0075c424",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "0075c43c",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ],
    [
      "0075c460",
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
      "0075c424",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ],
    [
      "0075c43c",
      "DATA",
      [
        "storage",
        "00c0bd38",
        null,
        "undefined *"
      ]
    ],
    [
      "0075c460",
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

- 旧版 [`0075c424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075c/0075c330.md#insn-0075c424) · [`0075c460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075c/0075c330.md#insn-0075c460) · [`0075c50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075c/0075c330.md#insn-0075c50c)
- 新版 [`0075c424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075c/0075c330.md#insn-0075c424) · [`0075c460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075c/0075c330.md#insn-0075c460) · [`0075c50c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075c/0075c330.md#insn-0075c50c)

~~~diff
- 0075c424 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:520:8"]]
- 0075c424 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0075c424 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:570:8"]]
+ 0075c424 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 0075c424 bytes 5a9342f9
+ 0075c424 bytes 5abb42f9
- 0075c460 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:528:8"]]
- 0075c460 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0075c460 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:578:8"]]
+ 0075c460 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0075c460 bytes 089542f9
+ 0075c460 bytes 08bd42f9
- 0075c50c ["COPY", "register:4040:8", ["const:bfb000:8"]]
+ 0075c50c ["COPY", "register:4040:8", ["const:bfc000:8"]]
- 0075c50c bytes e82400f0
+ 0075c50c bytes 08250090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ba2b2a004de7e440d53b42aff69163d"></a>

### [`0075c7f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075c/0075c7f8.md) → [`0075c7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075c/0075c7f8.md) FUN_0075c7f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0075bc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075bc70.md) · 呼出先 16件 [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`0075e018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075e/0075e018.md) [`0075e01c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075e/0075e01c.md) [`00883ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883ce0.md) [`00883e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883e08.md)
- 新版 呼出元 1件 [`0075bc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075bc70.md) · 呼出先 16件 [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`0075e018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e018.md) [`0075e01c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e01c.md) [`00883ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883ce0.md) [`00883e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883e08.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.07% / 新版 99.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0075cce4",
      "incomplete_value": false,
      "site": "0075cce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075cce4",
      "incomplete_value": false,
      "site": "0075cce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:38:8"
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
      "0075c900",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "0075c914",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ],
    [
      "0075c92c",
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
      "0075c900",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ],
    [
      "0075c914",
      "DATA",
      [
        "storage",
        "00c0bd38",
        null,
        "undefined *"
      ]
    ],
    [
      "0075c92c",
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

- 旧版 [`0075c900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075c/0075c7f8.md#insn-0075c900) · [`0075c92c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075c/0075c7f8.md#insn-0075c92c) · [`0075cce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075c/0075c7f8.md#insn-0075cce0)
- 新版 [`0075c900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075c/0075c7f8.md#insn-0075c900) · [`0075c92c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075c/0075c7f8.md#insn-0075c92c) · [`0075cce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075c/0075c7f8.md#insn-0075cce0)

~~~diff
- 0075c900 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:520:8"]]
- 0075c900 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0075c900 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:570:8"]]
+ 0075c900 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 0075c900 bytes 399342f9
+ 0075c900 bytes 39bb42f9
- 0075c92c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:528:8"]]
- 0075c92c ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0075c92c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:578:8"]]
+ 0075c92c ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 0075c92c bytes 5a9742f9
+ 0075c92c bytes 5abf42f9
- 0075cce0 ["COPY", "tmp:0:8", ["const:38:8"]]
- 0075cce0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075cce0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075cce0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075cce0 ["COPY", "tmp:0:8", ["const:88:8"]]
+ 0075cce0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075cce0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075cce0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075cce0 bytes 08e10091
+ 0075cce0 bytes 08210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce90cde9f288e728f0fca2f864f6023f"></a>

### [`0075d6ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075d/0075d6ec.md) → [`0075d6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d6ec.md) FUN_0075d6ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00749514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00749/00749514.md) · 呼出先 8件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00445d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d04.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md)
- 新版 呼出元 1件 [`00749514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/00749514.md) · 呼出先 8件 [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00445d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d04.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.33% / 新版 96.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0075d76c",
      "incomplete_value": true,
      "site": "0075d774",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "0075d76c",
      "incomplete_value": true,
      "site": "0075d774",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0075d790",
      "incomplete_value": true,
      "site": "0075d794",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "0075d790",
      "incomplete_value": true,
      "site": "0075d794",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0075d7b0",
      "incomplete_value": true,
      "site": "0075d7b4",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "0075d7b0",
      "incomplete_value": true,
      "site": "0075d7b4",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "0075d76c",
      "READ",
      [
        "storage",
        "00c23fd4",
        null,
        "undefined4"
      ]
    ],
    [
      "0075d790",
      "READ",
      [
        "storage",
        "00c23fd8",
        null,
        "undefined4"
      ]
    ],
    [
      "0075d7b0",
      "READ",
      [
        "storage",
        "00c23fdc",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0075d76c",
      "READ",
      [
        "storage",
        "00c24024",
        null,
        "undefined4"
      ]
    ],
    [
      "0075d790",
      "READ",
      [
        "storage",
        "00c24028",
        null,
        "undefined4"
      ]
    ],
    [
      "0075d7b0",
      "READ",
      [
        "storage",
        "00c2402c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075d764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075d/0075d6ec.md#insn-0075d764) · [`0075d76c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075d/0075d6ec.md#insn-0075d76c) · [`0075d788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075d/0075d6ec.md#insn-0075d788)
- 新版 [`0075d764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d6ec.md#insn-0075d764) · [`0075d76c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d6ec.md#insn-0075d76c) · [`0075d788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d6ec.md#insn-0075d788)

~~~diff
- 0075d764 ["COPY", "register:4040:8", ["const:c23000:8"]]
+ 0075d764 ["COPY", "register:4040:8", ["const:c24000:8"]]
- 0075d764 bytes 282600d0
+ 0075d764 bytes 282600f0
- 0075d76c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fd4:8"]]
- 0075d76c ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 0075d76c ["INT_ZEXT", "register:4008:8", ["tmp:1:4"]]
+ 0075d76c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:24:8"]]
+ 0075d76c ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 0075d76c ["INT_ZEXT", "register:4008:8", ["tmp:1:4"]]
- 0075d76c bytes 01d54fb9
+ 0075d76c bytes 012540b9
- 0075d788 ["COPY", "register:4040:8", ["const:c23000:8"]]
+ 0075d788 ["COPY", "register:4040:8", ["const:c24000:8"]]
- 0075d788 bytes 282600d0
+ 0075d788 bytes 282600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0898ed6e0445c1851d882cac2cb39216"></a>

### [`0075dce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075d/0075dce8.md) → [`0075dce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075dce8.md) FUN_0075dce8

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
      "definition_site": "0075dd0c",
      "incomplete_value": false,
      "site": "0075dd0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075dd0c",
      "incomplete_value": false,
      "site": "0075dd0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "0075dd0c",
      "DATA",
      [
        "storage",
        "00bfbf38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075dd0c",
      "DATA",
      [
        "storage",
        "00bfbf88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075dd08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075d/0075dce8.md#insn-0075dd08)
- 新版 [`0075dd08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075dce8.md#insn-0075dd08)

~~~diff
- 0075dd08 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 0075dd08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075dd08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075dd08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075dd08 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 0075dd08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075dd08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075dd08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075dd08 bytes 08e13c91
+ 0075dd08 bytes 08213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe026578c59df4d5ae41f39363024a4d"></a>

### [`0075dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075d/0075dd1c.md) → [`0075dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075dd1c.md) FUN_0075dd1c

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
      "definition_site": "0075dd28",
      "incomplete_value": false,
      "site": "0075dd28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075dd28",
      "incomplete_value": false,
      "site": "0075dd28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "0075dd28",
      "DATA",
      [
        "storage",
        "00bfbf38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075dd28",
      "DATA",
      [
        "storage",
        "00bfbf88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075dd24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075d/0075dd1c.md#insn-0075dd24)
- 新版 [`0075dd24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075dd1c.md#insn-0075dd24)

~~~diff
- 0075dd24 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 0075dd24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0075dd24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0075dd24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0075dd24 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 0075dd24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0075dd24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0075dd24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0075dd24 bytes 29e13c91
+ 0075dd24 bytes 29213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6055c389a082109794336ac47841c25c"></a>

### [`0075de7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075d/0075de7c.md) → [`0075de7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075de7c.md) FUN_0075de7c

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
      "definition_site": "0075de80",
      "incomplete_value": false,
      "site": "0075de84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075de80",
      "incomplete_value": false,
      "site": "0075de84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
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
      "0075de84",
      "DATA",
      [
        "storage",
        "00bfbfb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075de84",
      "DATA",
      [
        "storage",
        "00bfc008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075de7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075d/0075de7c.md#insn-0075de7c) · [`0075de80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075d/0075de7c.md#insn-0075de80)
- 新版 [`0075de7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075de7c.md#insn-0075de7c) · [`0075de80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075de7c.md#insn-0075de80)

~~~diff
- 0075de7c ["COPY", "register:4040:8", ["const:bfb000:8"]]
+ 0075de7c ["COPY", "register:4040:8", ["const:bfc000:8"]]
- 0075de7c bytes e82400d0
+ 0075de7c bytes e82400f0
- 0075de80 ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 0075de80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075de80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075de80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075de80 ["COPY", "tmp:0:8", ["const:8:8"]]
+ 0075de80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075de80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075de80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075de80 bytes 08e13e91
+ 0075de80 bytes 08210091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5d8ae1efa940c8af54f33f7d30faba8"></a>

### [`0075dfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075d/0075dfb8.md) → [`0075dfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075dfb8.md) FUN_0075dfb8

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
      "definition_site": "0075dfdc",
      "incomplete_value": false,
      "site": "0075dfe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075dfdc",
      "incomplete_value": false,
      "site": "0075dfe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:38:8"
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
      "0075dfe0",
      "DATA",
      [
        "storage",
        "00bfc038",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075dfe0",
      "DATA",
      [
        "storage",
        "00bfc088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075dfdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075d/0075dfb8.md#insn-0075dfdc)
- 新版 [`0075dfdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075dfb8.md#insn-0075dfdc)

~~~diff
- 0075dfdc ["COPY", "tmp:0:8", ["const:38:8"]]
- 0075dfdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075dfdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075dfdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075dfdc ["COPY", "tmp:0:8", ["const:88:8"]]
+ 0075dfdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075dfdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075dfdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075dfdc bytes 08e10091
+ 0075dfdc bytes 08210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9025cdb4442dfe9654f6586f5d56cf7"></a>

### [`0075dff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075d/0075dff8.md) → [`0075dff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075dff8.md) FUN_0075dff8

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
      "definition_site": "0075dffc",
      "incomplete_value": false,
      "site": "0075e000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075dffc",
      "incomplete_value": false,
      "site": "0075e000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:38:8"
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
      "0075e000",
      "DATA",
      [
        "storage",
        "00bfc038",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075e000",
      "DATA",
      [
        "storage",
        "00bfc088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075dffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075d/0075dff8.md#insn-0075dffc)
- 新版 [`0075dffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075dff8.md#insn-0075dffc)

~~~diff
- 0075dffc ["COPY", "tmp:0:8", ["const:38:8"]]
- 0075dffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075dffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075dffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075dffc ["COPY", "tmp:0:8", ["const:88:8"]]
+ 0075dffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075dffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075dffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075dffc bytes 08e10091
+ 0075dffc bytes 08210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4927dbc77a468f642273fbf71e963fe5"></a>

### [`0075e408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075e/0075e408.md) → [`0075e408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e408.md) _INIT_132

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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
      "definition_site": "0075e488",
      "incomplete_value": true,
      "site": "0075e4a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0075e488",
      "incomplete_value": true,
      "site": "0075e4a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0075e4a8",
      "incomplete_value": true,
      "site": "0075e4c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0075e4a8",
      "incomplete_value": true,
      "site": "0075e4c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0075e630",
      "incomplete_value": false,
      "site": "0075e63c",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075e630",
      "incomplete_value": false,
      "site": "0075e63c",
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
            "const:ee8:8"
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
      "0075e444",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0075e468",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0075e488",
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
      "0075e444",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0075e468",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0075e488",
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

- 旧版 [`0075e434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075e/0075e408.md#insn-0075e434) · [`0075e440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075e/0075e408.md#insn-0075e440) · [`0075e45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075e/0075e408.md#insn-0075e45c)
- 新版 [`0075e434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e408.md#insn-0075e434) · [`0075e440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e408.md#insn-0075e440) · [`0075e45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e408.md#insn-0075e45c)

~~~diff
- 0075e434 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 0075e434 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0075e434 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0075e434 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0075e434 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 0075e434 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0075e434 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0075e434 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0075e434 bytes 73a23b91
+ 0075e434 bytes 73a23c91
- 0075e440 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 0075e440 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0075e440 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0075e440 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0075e440 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 0075e440 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0075e440 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0075e440 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0075e440 bytes 29750b91
+ 0075e440 bytes 29dd0d91
- 0075e45c ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 0075e45c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0075e45c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0075e45c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0075e45c ["COPY", "tmp:0:8", ["const:38a:8"]]
+ 0075e45c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0075e45c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0075e45c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0075e45c bytes 4ac10b91
+ 0075e45c bytes 4a290e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c4a5764bda6e540a2ffd61461be419e"></a>

### [`0075e798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075e/0075e798.md) → [`0075e798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e798.md) FUN_0075e798

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 44件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`005e1400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1400.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 44件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`005e1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1400.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.36% / 新版 97.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0075e7e4",
      "incomplete_value": false,
      "site": "0075e7e4",
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
      "definition_site": "0075e7e4",
      "incomplete_value": false,
      "site": "0075e7e4",
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
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0075e7dc",
      "incomplete_value": true,
      "site": "0075e7e4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075e7dc",
      "incomplete_value": true,
      "site": "0075e7e4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:a78:8"
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
      "definition_site": "0075e7e8",
      "incomplete_value": true,
      "site": "0075e7e8",
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
      "definition_site": "0075e7e8",
      "incomplete_value": true,
      "site": "0075e7e8",
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
      "0075e7dc",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0075e7e0",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "0075e7e4",
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
      "0075e7dc",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0075e7e0",
      "READ",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "0075e7e4",
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

- 旧版 [`0075e7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075e/0075e798.md#insn-0075e7e4) · [`0075e7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075e/0075e798.md#insn-0075e7e8) · [`0075e800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075e/0075e798.md#insn-0075e800)
- 新版 [`0075e7e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e798.md#insn-0075e7e4) · [`0075e7e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e798.md#insn-0075e7e8) · [`0075e800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e798.md#insn-0075e800)

~~~diff
- 0075e7e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 0075e7e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0075e7e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa8:8"]]
+ 0075e7e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0075e7e4 bytes 093505f9
+ 0075e7e4 bytes 095505f9
- 0075e7e8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
- 0075e7e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 0075e7e8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab8:8"]]
+ 0075e7e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 0075e7e8 bytes aa3e05f9
+ 0075e7e8 bytes aa5e05f9
- 0075e800 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
- 0075e800 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 0075e800 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab8:8"]]
+ 0075e800 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 0075e800 bytes b43e05f9
+ 0075e800 bytes b45e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7a011a8c81eb0e65a369acc5f855742"></a>

### [`0075f8cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075f/0075f8cc.md) → [`0075f8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md) FUN_0075f8cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 64件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c24.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 64件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c24.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md)

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
      "definition_site": "0075f914",
      "incomplete_value": true,
      "site": "0075f914",
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
      "definition_site": "0075f914",
      "incomplete_value": true,
      "site": "0075f914",
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
      "definition_site": "0075f924",
      "incomplete_value": true,
      "site": "0075f938",
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
      "definition_site": "0075f924",
      "incomplete_value": true,
      "site": "0075f938",
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0075f92c",
      "incomplete_value": false,
      "site": "0075f938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075f92c",
      "incomplete_value": false,
      "site": "0075f938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:a8:8"
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
      "0075f910",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0075f924",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0075f92c",
      "PARAM",
      [
        "storage",
        "00bfc0a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0075f910",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0075f924",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0075f92c",
      "PARAM",
      [
        "storage",
        "00bfc0f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075f910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075f/0075f8cc.md#insn-0075f910) · [`0075f924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075f/0075f8cc.md#insn-0075f924) · [`0075f92c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075f/0075f8cc.md#insn-0075f92c)
- 新版 [`0075f910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md#insn-0075f910) · [`0075f924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md#insn-0075f924) · [`0075f92c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md#insn-0075f92c)

~~~diff
- 0075f910 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0075f910 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0075f910 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 0075f910 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0075f910 bytes 083d45f9
+ 0075f910 bytes 085d45f9
- 0075f924 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0075f924 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0075f924 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0075f924 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0075f924 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0075f924 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0075f924 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0075f924 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0075f924 bytes 21203991
+ 0075f924 bytes 21603a91
- 0075f92c ["COPY", "tmp:0:8", ["const:a8:8"]]
- 0075f92c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0075f92c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0075f92c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0075f92c ["COPY", "tmp:0:8", ["const:f8:8"]]
+ 0075f92c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0075f92c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0075f92c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0075f92c bytes 42a00291
+ 0075f92c bytes 42e00391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98107e4a047420369a8a2527a7be0c54"></a>

### [`00761844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00761/00761844.md) → [`00761844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761844.md) FUN_00761844

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00763a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763a24.md) · 呼出先 12件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`004707b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/004707b8.md) [`0047c518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c518.md) [`00764400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/00764400.md)
- 新版 呼出元 1件 [`00763a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763a24.md) · 呼出先 12件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`004707b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/004707b8.md) [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`00764400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764400.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00761900",
      "incomplete_value": false,
      "site": "00761900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00761900",
      "incomplete_value": false,
      "site": "00761900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:470:8"
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
      "definition_site": "0076194c",
      "incomplete_value": false,
      "site": "0076194c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076194c",
      "incomplete_value": false,
      "site": "0076194c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "00761900",
      "DATA",
      [
        "storage",
        "00bfc470",
        null,
        "undefined *"
      ]
    ],
    [
      "0076194c",
      "DATA",
      [
        "storage",
        "00bfc570",
        null,
        "undefined *"
      ]
    ],
    [
      "0076197c",
      "READ",
      [
        "storage",
        "00bfc490",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00761900",
      "DATA",
      [
        "storage",
        "00bfc4c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0076194c",
      "DATA",
      [
        "storage",
        "00bfc5c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0076197c",
      "READ",
      [
        "storage",
        "00bfc4e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007618f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00761/00761844.md#insn-007618f8) · [`00761944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00761/00761844.md#insn-00761944)
- 新版 [`007618f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761844.md#insn-007618f8) · [`00761944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761844.md#insn-00761944)

~~~diff
- 007618f8 ["COPY", "tmp:0:8", ["const:470:8"]]
- 007618f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007618f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007618f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007618f8 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 007618f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007618f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007618f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007618f8 bytes 08c11191
+ 007618f8 bytes 08011391
- 00761944 ["COPY", "tmp:0:8", ["const:570:8"]]
- 00761944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00761944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00761944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00761944 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 00761944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00761944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00761944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00761944 bytes 08c11591
+ 00761944 bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45af87f88e121a78512e4644b5c9ccdb"></a>

### [`00761ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00761/00761ab0.md) → [`00761ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761ab0.md) FUN_00761ab0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00763a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763a24.md) · 呼出先 11件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`004707b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/004707b8.md) [`0047c518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c518.md) [`0071b838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071b/0071b838.md)
- 新版 呼出元 1件 [`00763a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763a24.md) · 呼出先 11件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`004707b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/004707b8.md) [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`0071b838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071b/0071b838.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00761b6c",
      "incomplete_value": false,
      "site": "00761b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00761b6c",
      "incomplete_value": false,
      "site": "00761b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
      "definition_site": "00761ba4",
      "incomplete_value": false,
      "site": "00761ba4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00761ba4",
      "incomplete_value": false,
      "site": "00761ba4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "00761b6c",
      "DATA",
      [
        "storage",
        "00bfc4f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00761ba4",
      "DATA",
      [
        "storage",
        "00bfc570",
        null,
        "undefined *"
      ]
    ],
    [
      "00761be0",
      "READ",
      [
        "storage",
        "00bfc510",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00761b6c",
      "DATA",
      [
        "storage",
        "00bfc540",
        null,
        "undefined *"
      ]
    ],
    [
      "00761ba4",
      "DATA",
      [
        "storage",
        "00bfc5c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00761be0",
      "READ",
      [
        "storage",
        "00bfc560",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00761b64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00761/00761ab0.md#insn-00761b64) · [`00761b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00761/00761ab0.md#insn-00761b9c)
- 新版 [`00761b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761ab0.md#insn-00761b64) · [`00761b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761ab0.md#insn-00761b9c)

~~~diff
- 00761b64 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 00761b64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00761b64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00761b64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00761b64 ["COPY", "tmp:0:8", ["const:540:8"]]
+ 00761b64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00761b64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00761b64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00761b64 bytes 08c11391
+ 00761b64 bytes 08011591
- 00761b9c ["COPY", "tmp:0:8", ["const:570:8"]]
- 00761b9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00761b9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00761b9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00761b9c ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 00761b9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00761b9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00761b9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00761b9c bytes 08c11591
+ 00761b9c bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-317756642d34ade9ac0b58379707d46c"></a>

### [`00761d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00761/00761d08.md) → [`00761d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761d08.md) FUN_00761d08

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0075e798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075e/0075e798.md) · 呼出先 25件 [`0044b8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8ec.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md) [`0044c020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c020.md) [`0044c1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c1dc.md) [`0044c794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c794.md)
- 新版 呼出元 1件 [`0075e798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e798.md) · 呼出先 25件 [`0044b8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8ec.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md) [`0044c020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c020.md) [`0044c1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md) [`0044c794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c794.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.45% / 新版 88.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 46件, `store_destination` 14件, `store_value` 31件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00761d48",
      "incomplete_value": false,
      "site": "00761d4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00761d48",
      "incomplete_value": false,
      "site": "00761d4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:d0:8"
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
      "definition_site": "00761db8",
      "incomplete_value": true,
      "site": "00761db8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00761db8",
      "incomplete_value": true,
      "site": "00761db8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00761ea4",
      "incomplete_value": true,
      "site": "00761ea4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b3b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00761ea4",
      "incomplete_value": true,
      "site": "00761ea4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00761d4c",
      "DATA",
      [
        "storage",
        "00bfc0d0",
        null,
        "pointer"
      ]
    ],
    [
      "00761d88",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00761da8",
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
      "00761d4c",
      "DATA",
      [
        "storage",
        "00bfc120",
        null,
        "pointer"
      ]
    ],
    [
      "00761d88",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00761da8",
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

- 旧版 [`00761d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00761/00761d08.md#insn-00761d48) · [`00761d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00761/00761d08.md#insn-00761d84) · [`00761da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00761/00761d08.md#insn-00761da4)
- 新版 [`00761d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761d08.md#insn-00761d48) · [`00761d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761d08.md#insn-00761d84) · [`00761da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761d08.md#insn-00761da4)

~~~diff
- 00761d48 ["COPY", "tmp:0:8", ["const:d0:8"]]
- 00761d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00761d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00761d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00761d48 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 00761d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00761d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00761d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00761d48 bytes 08410391
+ 00761d48 bytes 08810491
- 00761d84 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00761d84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00761d84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00761d84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00761d84 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00761d84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00761d84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00761d84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00761d84 bytes 08e10091
+ 00761d84 bytes 08e10191
- 00761da4 ["COPY", "tmp:0:8", ["const:895:8"]]
- 00761da4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00761da4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00761da4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00761da4 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 00761da4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00761da4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00761da4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00761da4 bytes 08552291
+ 00761da4 bytes 08812491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-602648ac802db62ec8b746c894d660c2"></a>

### [`007638b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/007638b8.md) → [`007638b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/007638b8.md) FUN_007638b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0044b9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b9cc.md) [`0044c104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c104.md) [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`00763648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763648.md) [`00763798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763798.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md) [`0044c104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c104.md) [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`00763648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763648.md) [`00763798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763798.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007638c8",
      "incomplete_value": false,
      "site": "007638d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007638c8",
      "incomplete_value": false,
      "site": "007638d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:d0:8"
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
      "definition_site": "007638fc",
      "incomplete_value": false,
      "site": "00763900",
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
      "definition_site": "007638fc",
      "incomplete_value": false,
      "site": "00763900",
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
      "007638d0",
      "DATA",
      [
        "storage",
        "00bfc0d0",
        null,
        "pointer"
      ]
    ],
    [
      "00763900",
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
      "007638d0",
      "DATA",
      [
        "storage",
        "00bfc120",
        null,
        "pointer"
      ]
    ],
    [
      "00763900",
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

- 旧版 [`007638c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/007638b8.md#insn-007638c8) · [`007638fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/007638b8.md#insn-007638fc)
- 新版 [`007638c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/007638b8.md#insn-007638c8) · [`007638fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/007638b8.md#insn-007638fc)

~~~diff
- 007638c8 ["COPY", "tmp:0:8", ["const:d0:8"]]
- 007638c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007638c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007638c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007638c8 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 007638c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007638c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007638c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007638c8 bytes 08410391
+ 007638c8 bytes 08810491
- 007638fc ["COPY", "tmp:0:8", ["const:298:8"]]
- 007638fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007638fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007638fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007638fc ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 007638fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007638fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007638fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007638fc bytes 08610a91
+ 007638fc bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bf39e11a2597ffcb1a4ca417815344c"></a>

### [`00763940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763940.md) → [`00763940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763940.md) FUN_00763940

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0044b9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b9cc.md) [`0044c104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c104.md) [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`00763648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763648.md) [`00763798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763798.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md) [`0044c104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c104.md) [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`00763648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763648.md) [`00763798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763798.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00763950",
      "incomplete_value": false,
      "site": "00763958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00763950",
      "incomplete_value": false,
      "site": "00763958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:d0:8"
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
      "definition_site": "00763984",
      "incomplete_value": false,
      "site": "00763988",
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
      "definition_site": "00763984",
      "incomplete_value": false,
      "site": "00763988",
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
      "00763958",
      "DATA",
      [
        "storage",
        "00bfc0d0",
        null,
        "pointer"
      ]
    ],
    [
      "00763988",
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
      "00763958",
      "DATA",
      [
        "storage",
        "00bfc120",
        null,
        "pointer"
      ]
    ],
    [
      "00763988",
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

- 旧版 [`00763950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763940.md#insn-00763950) · [`00763984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763940.md#insn-00763984)
- 新版 [`00763950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763940.md#insn-00763950) · [`00763984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763940.md#insn-00763984)

~~~diff
- 00763950 ["COPY", "tmp:0:8", ["const:d0:8"]]
- 00763950 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00763950 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00763950 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00763950 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 00763950 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00763950 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00763950 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00763950 bytes 08410391
+ 00763950 bytes 08810491
- 00763984 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00763984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00763984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00763984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00763984 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 00763984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00763984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00763984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00763984 bytes 08610a91
+ 00763984 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0413317cd4a91e691a4a748fb52729e2"></a>

### [`007639d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/007639d4.md) → [`007639d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/007639d4.md) FUN_007639d4

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
      "definition_site": "007639f8",
      "incomplete_value": false,
      "site": "007639f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:140:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007639f8",
      "incomplete_value": false,
      "site": "007639f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:f0:8"
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
      "007639f8",
      "DATA",
      [
        "storage",
        "00bfc0f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007639f8",
      "DATA",
      [
        "storage",
        "00bfc140",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007639f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/007639d4.md#insn-007639f4)
- 新版 [`007639f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/007639d4.md#insn-007639f4)

~~~diff
- 007639f4 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 007639f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007639f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007639f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007639f4 ["COPY", "tmp:0:8", ["const:140:8"]]
+ 007639f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007639f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007639f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007639f4 bytes 08c10391
+ 007639f4 bytes 08010591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9eb8747541f30a2bae68961a110aa197"></a>

### [`00763a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763a08.md) → [`00763a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763a08.md) FUN_00763a08

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
      "definition_site": "00763a14",
      "incomplete_value": false,
      "site": "00763a14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:140:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00763a14",
      "incomplete_value": false,
      "site": "00763a14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:f0:8"
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
      "00763a14",
      "DATA",
      [
        "storage",
        "00bfc0f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00763a14",
      "DATA",
      [
        "storage",
        "00bfc140",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00763a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763a08.md#insn-00763a10)
- 新版 [`00763a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763a08.md#insn-00763a10)

~~~diff
- 00763a10 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00763a10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00763a10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00763a10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00763a10 ["COPY", "tmp:0:8", ["const:140:8"]]
+ 00763a10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00763a10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00763a10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00763a10 bytes 29c10391
+ 00763a10 bytes 29010591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cec87babe0165f9d9fba74c872b852e4"></a>

### [`00763a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763a24.md) → [`00763a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763a24.md) FUN_00763a24

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0047c518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c518.md) [`005e1400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1400.md) [`0071a0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071a/0071a0c4.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`005e1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1400.md) [`0071a0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071a/0071a0c4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.75% / 新版 98.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00763b38",
      "incomplete_value": false,
      "site": "00763b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00763b38",
      "incomplete_value": false,
      "site": "00763b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "00763b38",
      "DATA",
      [
        "storage",
        "00bfc570",
        null,
        "undefined *"
      ]
    ],
    [
      "00763c14",
      "READ",
      [
        "storage",
        "00bfc590",
        null,
        "pointer"
      ]
    ],
    [
      "00763c14",
      "READ",
      [
        "storage",
        "00bfc598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00763b38",
      "DATA",
      [
        "storage",
        "00bfc5c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00763c14",
      "READ",
      [
        "storage",
        "00bfc5e0",
        null,
        "pointer"
      ]
    ],
    [
      "00763c14",
      "READ",
      [
        "storage",
        "00bfc5e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00763b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763a24.md#insn-00763b30)
- 新版 [`00763b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763a24.md#insn-00763b30)

~~~diff
- 00763b30 ["COPY", "tmp:0:8", ["const:570:8"]]
- 00763b30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00763b30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00763b30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00763b30 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 00763b30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00763b30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00763b30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00763b30 bytes 08c11591
+ 00763b30 bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73d529a24f0c6a19d8d5fa0bfd38c1db"></a>

### [`00763d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763d1c.md) → [`00763d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763d1c.md) FUN_00763d1c

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
      "definition_site": "00763d40",
      "incomplete_value": false,
      "site": "00763d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00763d40",
      "incomplete_value": false,
      "site": "00763d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:170:8"
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
      "00763d40",
      "DATA",
      [
        "storage",
        "00bfc170",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00763d40",
      "DATA",
      [
        "storage",
        "00bfc1c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00763d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763d1c.md#insn-00763d3c)
- 新版 [`00763d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763d1c.md#insn-00763d3c)

~~~diff
- 00763d3c ["COPY", "tmp:0:8", ["const:170:8"]]
- 00763d3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00763d3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00763d3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00763d3c ["COPY", "tmp:0:8", ["const:1c0:8"]]
+ 00763d3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00763d3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00763d3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00763d3c bytes 08c10591
+ 00763d3c bytes 08010791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b316655644eb2bcf5c97510b595df62"></a>

### [`00763d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763d50.md) → [`00763d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763d50.md) FUN_00763d50

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
      "definition_site": "00763d5c",
      "incomplete_value": false,
      "site": "00763d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00763d5c",
      "incomplete_value": false,
      "site": "00763d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:170:8"
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
      "00763d5c",
      "DATA",
      [
        "storage",
        "00bfc170",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00763d5c",
      "DATA",
      [
        "storage",
        "00bfc1c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00763d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763d50.md#insn-00763d58)
- 新版 [`00763d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763d50.md#insn-00763d58)

~~~diff
- 00763d58 ["COPY", "tmp:0:8", ["const:170:8"]]
- 00763d58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00763d58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00763d58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00763d58 ["COPY", "tmp:0:8", ["const:1c0:8"]]
+ 00763d58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00763d58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00763d58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00763d58 bytes 29c10591
+ 00763d58 bytes 29010791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-816be3eeba15244aaf5c79696f099949"></a>

### [`00763f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763f3c.md) → [`00763f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763f3c.md) FUN_00763f3c

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
      "definition_site": "00763f60",
      "incomplete_value": false,
      "site": "00763f60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:240:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00763f60",
      "incomplete_value": false,
      "site": "00763f60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
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
      "00763f60",
      "DATA",
      [
        "storage",
        "00bfc1f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00763f60",
      "DATA",
      [
        "storage",
        "00bfc240",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00763f5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763f3c.md#insn-00763f5c)
- 新版 [`00763f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763f3c.md#insn-00763f5c)

~~~diff
- 00763f5c ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 00763f5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00763f5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00763f5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00763f5c ["COPY", "tmp:0:8", ["const:240:8"]]
+ 00763f5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00763f5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00763f5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00763f5c bytes 08c10791
+ 00763f5c bytes 08010991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dbf42fe36df2f92435194b02b56b04d"></a>

### [`00763f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763f70.md) → [`00763f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763f70.md) FUN_00763f70

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
      "definition_site": "00763f7c",
      "incomplete_value": false,
      "site": "00763f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:240:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00763f7c",
      "incomplete_value": false,
      "site": "00763f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
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
      "00763f7c",
      "DATA",
      [
        "storage",
        "00bfc1f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00763f7c",
      "DATA",
      [
        "storage",
        "00bfc240",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00763f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763f70.md#insn-00763f78)
- 新版 [`00763f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763f70.md#insn-00763f78)

~~~diff
- 00763f78 ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 00763f78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00763f78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00763f78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00763f78 ["COPY", "tmp:0:8", ["const:240:8"]]
+ 00763f78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00763f78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00763f78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00763f78 bytes 29c10791
+ 00763f78 bytes 29010991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ea33cf1e389db96e0f1807a84eb82d1"></a>

### [`00763ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763ffc.md) → [`00763ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763ffc.md) FUN_00763ffc

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
      "definition_site": "0076401c",
      "incomplete_value": false,
      "site": "00764020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076401c",
      "incomplete_value": false,
      "site": "00764020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "00764020",
      "DATA",
      [
        "storage",
        "00bfc270",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00764020",
      "DATA",
      [
        "storage",
        "00bfc2c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0076401c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763ffc.md#insn-0076401c)
- 新版 [`0076401c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763ffc.md#insn-0076401c)

~~~diff
- 0076401c ["COPY", "tmp:0:8", ["const:270:8"]]
- 0076401c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0076401c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0076401c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0076401c ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 0076401c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0076401c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0076401c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0076401c bytes 08c10991
+ 0076401c bytes 08010b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3592d6561da07c0c777ed6ded884a8da"></a>

### [`00764034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/00764034.md) → [`00764034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764034.md) FUN_00764034

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
      "definition_site": "00764038",
      "incomplete_value": false,
      "site": "0076403c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00764038",
      "incomplete_value": false,
      "site": "0076403c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "0076403c",
      "DATA",
      [
        "storage",
        "00bfc270",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0076403c",
      "DATA",
      [
        "storage",
        "00bfc2c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00764038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/00764034.md#insn-00764038)
- 新版 [`00764038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764034.md#insn-00764038)

~~~diff
- 00764038 ["COPY", "tmp:0:8", ["const:270:8"]]
- 00764038 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00764038 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00764038 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00764038 ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 00764038 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00764038 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00764038 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00764038 bytes 08c10991
+ 00764038 bytes 08010b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13833740ad097465ec54a98b031d4ea9"></a>

### [`00764084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/00764084.md) → [`00764084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764084.md) FUN_00764084

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
      "definition_site": "007640a8",
      "incomplete_value": false,
      "site": "007640a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007640a8",
      "incomplete_value": false,
      "site": "007640a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
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
      "007640a8",
      "DATA",
      [
        "storage",
        "00bfc2f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007640a8",
      "DATA",
      [
        "storage",
        "00bfc340",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007640a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/00764084.md#insn-007640a4)
- 新版 [`007640a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764084.md#insn-007640a4)

~~~diff
- 007640a4 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 007640a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007640a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007640a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007640a4 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 007640a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007640a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007640a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007640a4 bytes 08c10b91
+ 007640a4 bytes 08010d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff21a6f6ef3ce7560e0799705d81e3a8"></a>

### [`007640b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/007640b8.md) → [`007640b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007640b8.md) FUN_007640b8

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
      "definition_site": "007640c4",
      "incomplete_value": false,
      "site": "007640c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007640c4",
      "incomplete_value": false,
      "site": "007640c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
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
      "007640c4",
      "DATA",
      [
        "storage",
        "00bfc2f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007640c4",
      "DATA",
      [
        "storage",
        "00bfc340",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007640c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/007640b8.md#insn-007640c0)
- 新版 [`007640c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007640b8.md#insn-007640c0)

~~~diff
- 007640c0 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 007640c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007640c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007640c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007640c0 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 007640c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007640c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007640c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007640c0 bytes 29c10b91
+ 007640c0 bytes 29010d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f50e4ce049be3f40436bbd982bf29bc6"></a>

### [`00764140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/00764140.md) → [`00764140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764140.md) FUN_00764140

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
      "definition_site": "00764164",
      "incomplete_value": false,
      "site": "00764164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00764164",
      "incomplete_value": false,
      "site": "00764164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
      "00764164",
      "DATA",
      [
        "storage",
        "00bfc370",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00764164",
      "DATA",
      [
        "storage",
        "00bfc3c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00764160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/00764140.md#insn-00764160)
- 新版 [`00764160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764140.md#insn-00764160)

~~~diff
- 00764160 ["COPY", "tmp:0:8", ["const:370:8"]]
- 00764160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00764160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00764160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00764160 ["COPY", "tmp:0:8", ["const:3c0:8"]]
+ 00764160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00764160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00764160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00764160 bytes 08c10d91
+ 00764160 bytes 08010f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed79896f43886d8a3b59280cea34f23d"></a>

### [`00764174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/00764174.md) → [`00764174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764174.md) FUN_00764174

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
      "definition_site": "00764180",
      "incomplete_value": false,
      "site": "00764180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00764180",
      "incomplete_value": false,
      "site": "00764180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
      "00764180",
      "DATA",
      [
        "storage",
        "00bfc370",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00764180",
      "DATA",
      [
        "storage",
        "00bfc3c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0076417c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/00764174.md#insn-0076417c)
- 新版 [`0076417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764174.md#insn-0076417c)

~~~diff
- 0076417c ["COPY", "tmp:0:8", ["const:370:8"]]
- 0076417c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0076417c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0076417c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0076417c ["COPY", "tmp:0:8", ["const:3c0:8"]]
+ 0076417c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0076417c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0076417c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0076417c bytes 29c10d91
+ 0076417c bytes 29010f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82bdaef5b5b1ea51293d389b9e9a3562"></a>

### [`007642d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/007642d0.md) → [`007642d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007642d0.md) FUN_007642d0

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
      "definition_site": "007642f4",
      "incomplete_value": false,
      "site": "007642f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007642f4",
      "incomplete_value": false,
      "site": "007642f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
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
      "007642f4",
      "DATA",
      [
        "storage",
        "00bfc3e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007642f4",
      "DATA",
      [
        "storage",
        "00bfc430",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007642f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/007642d0.md#insn-007642f0)
- 新版 [`007642f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007642d0.md#insn-007642f0)

~~~diff
- 007642f0 ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 007642f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007642f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007642f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007642f0 ["COPY", "tmp:0:8", ["const:430:8"]]
+ 007642f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007642f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007642f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007642f0 bytes 08810f91
+ 007642f0 bytes 08c11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bb9fd7c919d039f5dcb639ed6c293b5"></a>

### [`00764304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/00764304.md) → [`00764304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764304.md) FUN_00764304

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
      "definition_site": "00764310",
      "incomplete_value": false,
      "site": "00764310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00764310",
      "incomplete_value": false,
      "site": "00764310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
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
      "00764310",
      "DATA",
      [
        "storage",
        "00bfc3e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00764310",
      "DATA",
      [
        "storage",
        "00bfc430",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0076430c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/00764304.md#insn-0076430c)
- 新版 [`0076430c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764304.md#insn-0076430c)

~~~diff
- 0076430c ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 0076430c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0076430c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0076430c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0076430c ["COPY", "tmp:0:8", ["const:430:8"]]
+ 0076430c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0076430c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0076430c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0076430c bytes 29810f91
+ 0076430c bytes 29c11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89cc8759d19fcd724e35d13c6deae79f"></a>

### [`00764398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/00764398.md) → [`00764398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764398.md) FUN_00764398

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0075f8cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075f/0075f8cc.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`0075f8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "007643a4",
      "incomplete_value": false,
      "site": "007643a8",
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
      "definition_site": "007643a4",
      "incomplete_value": false,
      "site": "007643a8",
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
      "007643a4",
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
      "007643a4",
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

- 旧版 [`007643a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/00764398.md#insn-007643a4)
- 新版 [`007643a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764398.md#insn-007643a4)

~~~diff
- 007643a4 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007643a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007643a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007643a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007643a4 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007643a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007643a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007643a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007643a4 bytes 000c0c91
+ 007643a4 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35f6f5e221ff153d02fcf7c3d5a41f91"></a>

### [`007643b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/007643b0.md) → [`007643b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007643b0.md) FUN_007643b0

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
      "definition_site": "007643d0",
      "incomplete_value": false,
      "site": "007643d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007643d0",
      "incomplete_value": false,
      "site": "007643d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:470:8"
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
      "007643d4",
      "DATA",
      [
        "storage",
        "00bfc470",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007643d4",
      "DATA",
      [
        "storage",
        "00bfc4c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007643d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/007643b0.md#insn-007643d0)
- 新版 [`007643d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007643b0.md#insn-007643d0)

~~~diff
- 007643d0 ["COPY", "tmp:0:8", ["const:470:8"]]
- 007643d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007643d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007643d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007643d0 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 007643d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007643d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007643d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007643d0 bytes 08c11191
+ 007643d0 bytes 08011391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31f0349f670b138ba23bf270f63470dd"></a>

### [`007643e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/007643e8.md) → [`007643e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007643e8.md) FUN_007643e8

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
      "definition_site": "007643ec",
      "incomplete_value": false,
      "site": "007643f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007643ec",
      "incomplete_value": false,
      "site": "007643f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:470:8"
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
      "007643f0",
      "DATA",
      [
        "storage",
        "00bfc470",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007643f0",
      "DATA",
      [
        "storage",
        "00bfc4c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007643ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/007643e8.md#insn-007643ec)
- 新版 [`007643ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007643e8.md#insn-007643ec)

~~~diff
- 007643ec ["COPY", "tmp:0:8", ["const:470:8"]]
- 007643ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007643ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007643ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007643ec ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 007643ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007643ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007643ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007643ec bytes 08c11191
+ 007643ec bytes 08011391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ba9a3460bc8a61ba68f36fb7beaea4d"></a>

### [`007645c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/007645c4.md) → [`007645c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007645c4.md) FUN_007645c4

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
      "definition_site": "007645e4",
      "incomplete_value": true,
      "site": "007645e8",
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
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007645e4",
      "incomplete_value": true,
      "site": "007645e8",
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
            "const:4f0:8"
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
      "007645e8",
      "DATA",
      [
        "storage",
        "00bfc4f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007645e8",
      "DATA",
      [
        "storage",
        "00bfc540",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007645e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/007645c4.md#insn-007645e4)
- 新版 [`007645e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007645c4.md#insn-007645e4)

~~~diff
- 007645e4 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 007645e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007645e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007645e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007645e4 ["COPY", "tmp:0:8", ["const:540:8"]]
+ 007645e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007645e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007645e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007645e4 bytes 08c11391
+ 007645e4 bytes 08011591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f2f942b5a5a49ccdca1f4df70b0c72f"></a>

### [`0076461c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/0076461c.md) → [`0076461c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/0076461c.md) FUN_0076461c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0047c518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c518.md) [`00764820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/00764820.md) [`00764824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/00764824.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`00764820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764820.md) [`00764824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764824.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.53% / 新版 97.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0076467c",
      "incomplete_value": false,
      "site": "0076467c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076467c",
      "incomplete_value": false,
      "site": "0076467c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "0076467c",
      "DATA",
      [
        "storage",
        "00bfc570",
        null,
        "undefined *"
      ]
    ],
    [
      "00764714",
      "READ",
      [
        "storage",
        "00bfc590",
        null,
        "pointer"
      ]
    ],
    [
      "00764714",
      "READ",
      [
        "storage",
        "00bfc598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0076467c",
      "DATA",
      [
        "storage",
        "00bfc5c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00764714",
      "READ",
      [
        "storage",
        "00bfc5e0",
        null,
        "pointer"
      ]
    ],
    [
      "00764714",
      "READ",
      [
        "storage",
        "00bfc5e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00764674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/0076461c.md#insn-00764674)
- 新版 [`00764674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/0076461c.md#insn-00764674)

~~~diff
- 00764674 ["COPY", "tmp:0:8", ["const:570:8"]]
- 00764674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00764674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00764674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00764674 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 00764674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00764674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00764674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00764674 bytes 08c11591
+ 00764674 bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-733285ba3bad63e1828a78d3508b0ac0"></a>

### [`007647d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/007647d8.md) → [`007647d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007647d8.md) FUN_007647d8

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
      "definition_site": "007647fc",
      "incomplete_value": false,
      "site": "007647fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007647fc",
      "incomplete_value": false,
      "site": "007647fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "007647fc",
      "DATA",
      [
        "storage",
        "00bfc570",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007647fc",
      "DATA",
      [
        "storage",
        "00bfc5c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007647f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/007647d8.md#insn-007647f8)
- 新版 [`007647f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007647d8.md#insn-007647f8)

~~~diff
- 007647f8 ["COPY", "tmp:0:8", ["const:570:8"]]
- 007647f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007647f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007647f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007647f8 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 007647f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007647f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007647f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007647f8 bytes 08c11591
+ 007647f8 bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64e884dc5de4abdf19b872a1131756b0"></a>

### [`0076480c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/0076480c.md) → [`0076480c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/0076480c.md) FUN_0076480c

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
      "definition_site": "00764818",
      "incomplete_value": false,
      "site": "00764818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00764818",
      "incomplete_value": false,
      "site": "00764818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "00764818",
      "DATA",
      [
        "storage",
        "00bfc570",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00764818",
      "DATA",
      [
        "storage",
        "00bfc5c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00764814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/0076480c.md#insn-00764814)
- 新版 [`00764814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/0076480c.md#insn-00764814)

~~~diff
- 00764814 ["COPY", "tmp:0:8", ["const:570:8"]]
- 00764814 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00764814 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00764814 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00764814 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 00764814 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00764814 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00764814 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00764814 bytes 29c11591
+ 00764814 bytes 29011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98185d48aa6d0be84e6b2aaa763d5aa4"></a>

### [`007648a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/007648a0.md) → [`007648a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007648a0.md) _INIT_133

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
      "definition_site": "007648dc",
      "incomplete_value": true,
      "site": "007648f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007648dc",
      "incomplete_value": true,
      "site": "007648f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00764900",
      "incomplete_value": true,
      "site": "0076491c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00764900",
      "incomplete_value": true,
      "site": "0076491c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00764920",
      "incomplete_value": true,
      "site": "0076493c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00764920",
      "incomplete_value": true,
      "site": "0076493c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "007648dc",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00764900",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00764920",
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
      "007648dc",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00764900",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00764920",
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

- 旧版 [`007648cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/007648a0.md#insn-007648cc) · [`007648d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00764/007648a0.md#insn-007648d4)
- 新版 [`007648cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007648a0.md#insn-007648cc) · [`007648d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007648a0.md#insn-007648d4)

~~~diff
- 007648cc ["COPY", "tmp:0:8", ["const:f00:8"]]
- 007648cc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 007648cc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 007648cc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 007648cc ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 007648cc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 007648cc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 007648cc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 007648cc bytes 73023c91
+ 007648cc bytes 73023d91
- 007648d4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 007648d4 bytes 09dafff0
+ 007648d4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 007648d4 bytes 09dafff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7b1ece5974491f02f77880ea0a948bc"></a>

### [`007659c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00765/007659c0.md) → [`007659c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00765/007659c0.md) FUN_007659c0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) · 呼出先 15件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00765cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00765/00765cf0.md) [`0076a364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076a364.md)
- 新版 呼出元 1件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · 呼出先 15件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00765cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00765/00765cf0.md) [`0076a364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a364.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.50% / 新版 86.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00765a50",
      "incomplete_value": false,
      "site": "00765a50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00765a50",
      "incomplete_value": false,
      "site": "00765a50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "definition_site": "00765b0c",
      "incomplete_value": false,
      "site": "00765b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00765b0c",
      "incomplete_value": false,
      "site": "00765b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
      "definition_site": "00765c1c",
      "incomplete_value": false,
      "site": "00765c1c",
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
      "definition_site": "00765c1c",
      "incomplete_value": false,
      "site": "00765c1c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007659f4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00765a00",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "00765a08",
      "PARAM",
      [
        "storage",
        "00c27f30",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "007659f4",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00765a00",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ],
    [
      "00765a08",
      "PARAM",
      [
        "storage",
        "00c27f70",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007659f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00765/007659c0.md#insn-007659f0) · [`00765a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00765/007659c0.md#insn-00765a00) · [`00765a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00765/007659c0.md#insn-00765a08)
- 新版 [`007659f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00765/007659c0.md#insn-007659f0) · [`00765a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00765/007659c0.md#insn-00765a00) · [`00765a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00765/007659c0.md#insn-00765a08)

~~~diff
- 007659f0 ["COPY", "tmp:0:8", ["const:38:8"]]
- 007659f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007659f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007659f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007659f0 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 007659f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007659f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007659f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007659f0 bytes 08e10091
+ 007659f0 bytes 08e10191
- 00765a00 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00765a00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00765a00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00765a00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00765a00 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 00765a00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00765a00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00765a00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00765a00 bytes 00000091
+ 00765a00 bytes 00000191
- 00765a08 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 00765a08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00765a08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00765a08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00765a08 ["COPY", "tmp:0:8", ["const:f70:8"]]
+ 00765a08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00765a08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00765a08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00765a08 bytes 21c03c91
+ 00765a08 bytes 21c03d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-beed519053b13fc7fa2f7acc8b2d9ebe"></a>

### [`00765cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00765/00765cf0.md) → [`00765cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00765/00765cf0.md) FUN_00765cf0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007659c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00765/007659c0.md) · 呼出先 12件 [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`0076ac68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076ac68.md) [`00883d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883d2c.md) [`00883e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883e08.md) [`009e964c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e964c.md)
- 新版 呼出元 1件 [`007659c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00765/007659c0.md) · 呼出先 12件 [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`0076ac68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076ac68.md) [`00883d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883d2c.md) [`00883e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883e08.md) [`009e9690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9690.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.64% / 新版 94.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00765e00",
      "incomplete_value": true,
      "site": "00765e04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00765e00",
      "incomplete_value": true,
      "site": "00765e04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00765e44",
      "incomplete_value": true,
      "site": "00765e44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00765e44",
      "incomplete_value": true,
      "site": "00765e44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00765edc",
      "incomplete_value": false,
      "site": "00765edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00765edc",
      "incomplete_value": false,
      "site": "00765edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
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
      "00765dc4",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "00765dd8",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ],
    [
      "00765dfc",
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
      "00765dc4",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ],
    [
      "00765dd8",
      "DATA",
      [
        "storage",
        "00c0bd38",
        null,
        "undefined *"
      ]
    ],
    [
      "00765dfc",
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

- 旧版 [`00765dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00765/00765cf0.md#insn-00765dc4) · [`00765dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00765/00765cf0.md#insn-00765dfc) · [`00765e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00765/00765cf0.md#insn-00765e3c)
- 新版 [`00765dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00765/00765cf0.md#insn-00765dc4) · [`00765dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00765/00765cf0.md#insn-00765dfc) · [`00765e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00765/00765cf0.md#insn-00765e3c)

~~~diff
- 00765dc4 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:520:8"]]
- 00765dc4 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00765dc4 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:570:8"]]
+ 00765dc4 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 00765dc4 bytes 7b9342f9
+ 00765dc4 bytes 7bbb42f9
- 00765dfc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:528:8"]]
- 00765dfc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00765dfc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:578:8"]]
+ 00765dfc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00765dfc bytes 089542f9
+ 00765dfc bytes 08bd42f9
- 00765e3c ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:520:8"]]
- 00765e3c ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00765e3c ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:570:8"]]
+ 00765e3c ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 00765e3c bytes 7b9342f9
+ 00765e3c bytes 7bbb42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d90b8651db8430e2793f811a0d047b9"></a>

### [`00769cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00769/00769cc0.md) → [`00769cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00769/00769cc0.md) FUN_00769cc0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00766d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00766/00766d10.md) [`007673fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00767/007673fc.md) [`0076794c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00767/0076794c.md) [`00767f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00767/00767f70.md) · 呼出先 16件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00470ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470ac0.md) [`0051d884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d884.md) [`00610c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/00610c14.md)
- 新版 呼出元 4件 [`00766d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00766/00766d10.md) [`007673fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00767/007673fc.md) [`0076794c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00767/0076794c.md) [`00767f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00767/00767f70.md) · 呼出先 16件 [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00470ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470ac0.md) [`0051d884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d884.md) [`00610c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610c14.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.00% / 新版 97.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00769e70",
      "incomplete_value": false,
      "site": "00769e84",
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
      "definition_site": "00769e70",
      "incomplete_value": false,
      "site": "00769e84",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00769e68",
      "incomplete_value": true,
      "site": "00769e84",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
              ],
              [
                "leaf",
                "const:eb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00769e68",
      "incomplete_value": true,
      "site": "00769e84",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
              ],
              [
                "leaf",
                "const:e60:8"
              ]
            ]
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
      "definition_site": "0076a15c",
      "incomplete_value": false,
      "site": "0076a160",
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
      "definition_site": "0076a15c",
      "incomplete_value": false,
      "site": "0076a160",
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
    "ordinal": 24,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00769d00",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00769e68",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "00769e68",
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
      "00769d00",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00769e68",
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "00769e68",
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

- 旧版 [`00769cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00769/00769cc0.md#insn-00769cfc) · [`00769e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00769/00769cc0.md#insn-00769e68) · [`00769e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00769/00769cc0.md#insn-00769e70)
- 新版 [`00769cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00769/00769cc0.md#insn-00769cfc) · [`00769e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00769/00769cc0.md#insn-00769e68) · [`00769e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00769/00769cc0.md#insn-00769e70)

~~~diff
- 00769cfc ["COPY", "tmp:0:8", ["const:38:8"]]
- 00769cfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00769cfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00769cfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00769cfc ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00769cfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00769cfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00769cfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00769cfc bytes 08e10091
+ 00769cfc bytes 08e10191
- 00769e68 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:e60:8"]]
- 00769e68 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00769e68 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:eb0:8"]]
+ 00769e68 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00769e68 bytes 423047f9
+ 00769e68 bytes 425847f9
- 00769e70 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00769e70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00769e70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00769e70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00769e70 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 00769e70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00769e70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00769e70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00769e70 bytes 00000091
+ 00769e70 bytes 00000191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34da13c2d0439aead5035c7d355aaccb"></a>

### [`0076a31c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076a31c.md) → [`0076a31c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a31c.md) FUN_0076a31c

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
      "definition_site": "0076a340",
      "incomplete_value": false,
      "site": "0076a340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076a340",
      "incomplete_value": false,
      "site": "0076a340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "0076a340",
      "DATA",
      [
        "storage",
        "00bfc5f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0076a340",
      "DATA",
      [
        "storage",
        "00bfc640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0076a33c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076a31c.md#insn-0076a33c)
- 新版 [`0076a33c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a31c.md#insn-0076a33c)

~~~diff
- 0076a33c ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 0076a33c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0076a33c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0076a33c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0076a33c ["COPY", "tmp:0:8", ["const:640:8"]]
+ 0076a33c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0076a33c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0076a33c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0076a33c bytes 08c11791
+ 0076a33c bytes 08011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d67ee94c431612c4d7880f73d29e038"></a>

### [`0076a350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076a350.md) → [`0076a350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a350.md) FUN_0076a350

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
      "definition_site": "0076a35c",
      "incomplete_value": false,
      "site": "0076a35c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076a35c",
      "incomplete_value": false,
      "site": "0076a35c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "0076a35c",
      "DATA",
      [
        "storage",
        "00bfc5f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0076a35c",
      "DATA",
      [
        "storage",
        "00bfc640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0076a358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076a350.md#insn-0076a358)
- 新版 [`0076a358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a350.md#insn-0076a358)

~~~diff
- 0076a358 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 0076a358 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0076a358 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0076a358 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0076a358 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 0076a358 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0076a358 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0076a358 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0076a358 bytes 29c11791
+ 0076a358 bytes 29011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-159bc410d16e71113f793d1baf2ebc9d"></a>

### [`0076a3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076a3a4.md) → [`0076a3a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a3a4.md) FUN_0076a3a4

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
      "definition_site": "0076a3c8",
      "incomplete_value": false,
      "site": "0076a3c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076a3c8",
      "incomplete_value": false,
      "site": "0076a3c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
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
      "0076a3c8",
      "DATA",
      [
        "storage",
        "00bfc670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0076a3c8",
      "DATA",
      [
        "storage",
        "00bfc6c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0076a3c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076a3a4.md#insn-0076a3c4)
- 新版 [`0076a3c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a3a4.md#insn-0076a3c4)

~~~diff
- 0076a3c4 ["COPY", "tmp:0:8", ["const:670:8"]]
- 0076a3c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0076a3c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0076a3c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0076a3c4 ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 0076a3c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0076a3c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0076a3c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0076a3c4 bytes 08c11991
+ 0076a3c4 bytes 08011b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-275cfe7e2b5168b4922fa10d97835f44"></a>

### [`0076a3d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076a3d8.md) → [`0076a3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a3d8.md) FUN_0076a3d8

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
      "definition_site": "0076a3e4",
      "incomplete_value": false,
      "site": "0076a3e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076a3e4",
      "incomplete_value": false,
      "site": "0076a3e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
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
      "0076a3e4",
      "DATA",
      [
        "storage",
        "00bfc670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0076a3e4",
      "DATA",
      [
        "storage",
        "00bfc6c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0076a3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076a3d8.md#insn-0076a3e0)
- 新版 [`0076a3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a3d8.md#insn-0076a3e0)

~~~diff
- 0076a3e0 ["COPY", "tmp:0:8", ["const:670:8"]]
- 0076a3e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0076a3e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0076a3e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0076a3e0 ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 0076a3e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0076a3e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0076a3e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0076a3e0 bytes 29c11991
+ 0076a3e0 bytes 29011b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45350fa23cb353a5ba9e18c46265ddf8"></a>

### [`0076a658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076a658.md) → [`0076a658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a658.md) FUN_0076a658

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0076a428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076a428.md) [`007d93c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d93c4.md) [`00acacd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acacd0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`0076a428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a428.md) [`007d93c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d9/007d93c4.md) [`00acad14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00acad14.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0076a664",
      "incomplete_value": false,
      "site": "0076a668",
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
      "definition_site": "0076a664",
      "incomplete_value": false,
      "site": "0076a668",
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
      "0076a664",
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
      "0076a664",
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

- 旧版 [`0076a664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076a658.md#insn-0076a664)
- 新版 [`0076a664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a658.md#insn-0076a664)

~~~diff
- 0076a664 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0076a664 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0076a664 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0076a664 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0076a664 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0076a664 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0076a664 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0076a664 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0076a664 bytes 000c0c91
+ 0076a664 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-352ebf5e46fee6198fafe1e63d7e35fc"></a>

### [`0076aa94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076aa94.md) → [`0076aa94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076aa94.md) FUN_0076aa94

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
      "definition_site": "0076aaa0",
      "incomplete_value": false,
      "site": "0076aaac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076aaa0",
      "incomplete_value": false,
      "site": "0076aaac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
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
      "0076aaac",
      "DATA",
      [
        "storage",
        "00bfc6f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0076aaac",
      "DATA",
      [
        "storage",
        "00bfc740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0076aaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076aa94.md#insn-0076aaa0)
- 新版 [`0076aaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076aa94.md#insn-0076aaa0)

~~~diff
- 0076aaa0 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 0076aaa0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0076aaa0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0076aaa0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0076aaa0 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 0076aaa0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0076aaa0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0076aaa0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0076aaa0 bytes 4ac11b91
+ 0076aaa0 bytes 4a011d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36b56cc80b6e039d114a3b950418b373"></a>

### [`0076aad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076aad8.md) → [`0076aad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076aad8.md) FUN_0076aad8

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
      "definition_site": "0076aaf0",
      "incomplete_value": false,
      "site": "0076aafc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076aaf0",
      "incomplete_value": false,
      "site": "0076aafc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
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
      "0076aafc",
      "DATA",
      [
        "storage",
        "00bfc6f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0076aafc",
      "DATA",
      [
        "storage",
        "00bfc740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0076aaf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076aad8.md#insn-0076aaf0)
- 新版 [`0076aaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076aad8.md#insn-0076aaf0)

~~~diff
- 0076aaf0 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 0076aaf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0076aaf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0076aaf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0076aaf0 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 0076aaf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0076aaf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0076aaf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0076aaf0 bytes 08c11b91
+ 0076aaf0 bytes 08011d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-982867e252364a7256e5c23a6dc87f0d"></a>

### [`0076ab34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076ab34.md) → [`0076ab34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076ab34.md) FUN_0076ab34

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
      "definition_site": "0076ab60",
      "incomplete_value": false,
      "site": "0076ab60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076ab60",
      "incomplete_value": false,
      "site": "0076ab60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
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
      "0076ab60",
      "DATA",
      [
        "storage",
        "00bfc6f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0076ab60",
      "DATA",
      [
        "storage",
        "00bfc740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0076ab58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076ab34.md#insn-0076ab58)
- 新版 [`0076ab58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076ab34.md#insn-0076ab58)

~~~diff
- 0076ab58 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 0076ab58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0076ab58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0076ab58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0076ab58 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 0076ab58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0076ab58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0076ab58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0076ab58 bytes 08c11b91
+ 0076ab58 bytes 08011d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fdc1cec36c7230c59ca1fde0b4ae53f"></a>

### [`0076abbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076abbc.md) → [`0076abbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076abbc.md) FUN_0076abbc

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
      "definition_site": "0076abd8",
      "incomplete_value": false,
      "site": "0076abd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076abd8",
      "incomplete_value": false,
      "site": "0076abd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
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
      "0076abd8",
      "DATA",
      [
        "storage",
        "00bfc6f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0076abd8",
      "DATA",
      [
        "storage",
        "00bfc740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0076abd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076abbc.md#insn-0076abd4)
- 新版 [`0076abd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076abbc.md#insn-0076abd4)

~~~diff
- 0076abd4 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 0076abd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0076abd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0076abd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0076abd4 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 0076abd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0076abd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0076abd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0076abd4 bytes 29c11b91
+ 0076abd4 bytes 29011d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-858a7897aaa417a396315f8916f569c6"></a>

### [`0076b160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b160.md) → [`0076b160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b160.md) FUN_0076b160

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0076ad44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076ad44.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0076ad44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076ad44.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0076b16c",
      "incomplete_value": false,
      "site": "0076b170",
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
      "definition_site": "0076b16c",
      "incomplete_value": false,
      "site": "0076b170",
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
      "0076b16c",
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
      "0076b16c",
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

- 旧版 [`0076b16c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b160.md#insn-0076b16c)
- 新版 [`0076b16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b160.md#insn-0076b16c)

~~~diff
- 0076b16c ["COPY", "tmp:0:8", ["const:303:8"]]
- 0076b16c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0076b16c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0076b16c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0076b16c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0076b16c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0076b16c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0076b16c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0076b16c bytes 000c0c91
+ 0076b16c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55d83ade991b5bbd43cd40092f0d14d2"></a>

### [`0076b174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b174.md) → [`0076b174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b174.md) _INIT_134

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.10% / 新版 85.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0076b230",
      "incomplete_value": true,
      "site": "0076b24c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076b230",
      "incomplete_value": true,
      "site": "0076b24c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0076b404",
      "incomplete_value": false,
      "site": "0076b404",
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
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076b404",
      "incomplete_value": false,
      "site": "0076b404",
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
            "const:f48:8"
          ]
        ]
      ]
    },
    "ordinal": 49,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0076b418",
      "incomplete_value": false,
      "site": "0076b418",
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
                "const:c27000:8"
              ],
              [
                "leaf",
                "const:f88:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:16:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076b418",
      "incomplete_value": false,
      "site": "0076b418",
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
                "const:c27000:8"
              ],
              [
                "leaf",
                "const:f48:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:16:8"
          ]
        ]
      ]
    },
    "ordinal": 50,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0076b1b0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0076b1d4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0076b1f4",
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
      "0076b1b0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0076b1d4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0076b1f4",
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

- 旧版 [`0076b1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b174.md#insn-0076b1a0) · [`0076b1a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b174.md#insn-0076b1a8)
- 新版 [`0076b1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b174.md#insn-0076b1a0) · [`0076b1a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b174.md#insn-0076b1a8)

~~~diff
- 0076b1a0 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 0076b1a0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0076b1a0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0076b1a0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0076b1a0 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 0076b1a0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0076b1a0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0076b1a0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0076b1a0 bytes 73623c91
+ 0076b1a0 bytes 73623d91
- 0076b1a8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0076b1a8 bytes e9d9ff90
+ 0076b1a8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0076b1a8 bytes e9d9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc587c5b847f7117b6108d5da204f8a9"></a>

### [`0076b580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b580.md) → [`0076b580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b580.md) _INIT_135

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
      "definition_site": "0076b5bc",
      "incomplete_value": true,
      "site": "0076b5d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076b5bc",
      "incomplete_value": true,
      "site": "0076b5d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076b5e0",
      "incomplete_value": true,
      "site": "0076b5fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076b5e0",
      "incomplete_value": true,
      "site": "0076b5fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076b600",
      "incomplete_value": true,
      "site": "0076b61c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076b600",
      "incomplete_value": true,
      "site": "0076b61c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0076b5bc",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0076b5e0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0076b600",
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
      "0076b5bc",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0076b5e0",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0076b600",
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

- 旧版 [`0076b5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b580.md#insn-0076b5ac) · [`0076b5b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b580.md#insn-0076b5b4)
- 新版 [`0076b5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b580.md#insn-0076b5ac) · [`0076b5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b580.md#insn-0076b5b4)

~~~diff
- 0076b5ac ["COPY", "tmp:0:8", ["const:f60:8"]]
- 0076b5ac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0076b5ac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0076b5ac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0076b5ac ["COPY", "tmp:0:8", ["const:fa0:8"]]
+ 0076b5ac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0076b5ac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0076b5ac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0076b5ac bytes 73823d91
+ 0076b5ac bytes 73823e91
- 0076b5b4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0076b5b4 bytes e9d9ff90
+ 0076b5b4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0076b5b4 bytes e9d9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2628579335192dce7ed455959f45812"></a>

### [`0076b910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b910.md) → [`0076b910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b910.md) FUN_0076b910

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 19件 [`00577df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00577/00577df0.md) [`00578500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578500.md) [`005891dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00589/005891dc.md) [`0058a2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058a/0058a2e0.md) [`0058d7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058d/0058d7b4.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 19件 [`00577df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577df0.md) [`00578500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578500.md) [`005891dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00589/005891dc.md) [`0058a2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058a/0058a2e0.md) [`0058d7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058d/0058d7b4.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0076b938",
      "incomplete_value": true,
      "site": "0076b938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076b938",
      "incomplete_value": true,
      "site": "0076b938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0076b924",
      "incomplete_value": true,
      "site": "0076b924",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "0076b924",
      "incomplete_value": true,
      "site": "0076b924",
      "value": [
        "INT_NOTEQUAL",
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
    "guard": [
      [
        "FALL_THROUGH",
        "0076b924"
      ],
      [
        "FALL_THROUGH",
        "0076b924"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "0076b924",
      "incomplete_value": true,
      "site": "0076b930",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "0076b924",
      "incomplete_value": true,
      "site": "0076b930",
      "value": [
        "INT_NOTEQUAL",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0076b920",
      "READ",
      [
        "storage",
        "00c27f90",
        null,
        "undefined8"
      ]
    ],
    [
      "0076b938",
      "WRITE",
      [
        "storage",
        "00c27f90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0076b920",
      "READ",
      [
        "storage",
        "00c27fd0",
        null,
        "undefined8"
      ]
    ],
    [
      "0076b938",
      "WRITE",
      [
        "storage",
        "00c27fd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0076b938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b910.md#insn-0076b938) · [`0076b920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b910.md#insn-0076b920)
- 新版 [`0076b938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b910.md#insn-0076b938) · [`0076b920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b910.md#insn-0076b920)

~~~diff
- 0076b938 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f90:8"]]
- 0076b938 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 0076b938 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fd0:8"]]
+ 0076b938 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 0076b938 bytes 60ca07f9
+ 0076b938 bytes 60ea07f9
- 0076b920 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f90:8"]]
- 0076b920 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0076b920 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fd0:8"]]
+ 0076b920 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0076b920 bytes 60ca47f9
+ 0076b920 bytes 60ea47f9
~~~


<a id="compare-44494bded126a0b5dc195b5f9a81d83a"></a>

### [`0076bd4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076bd4c.md) → [`0076bd4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076bd4c.md) FUN_0076bd4c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0076bbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076bbf0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0076bbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076bbf0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0076bd58",
      "incomplete_value": false,
      "site": "0076bd5c",
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
      "definition_site": "0076bd58",
      "incomplete_value": false,
      "site": "0076bd5c",
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
      "0076bd58",
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
      "0076bd58",
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

- 旧版 [`0076bd58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076bd4c.md#insn-0076bd58)
- 新版 [`0076bd58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076bd4c.md#insn-0076bd58)

~~~diff
- 0076bd58 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0076bd58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0076bd58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0076bd58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0076bd58 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0076bd58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0076bd58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0076bd58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0076bd58 bytes 000c0c91
+ 0076bd58 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7f26ecd268684edfdeabfefe07e574c"></a>

### [`0076bd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076bd60.md) → [`0076bd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076bd60.md) _INIT_136

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
      "definition_site": "0076bd9c",
      "incomplete_value": true,
      "site": "0076bdb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076bd9c",
      "incomplete_value": true,
      "site": "0076bdb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076bde0",
      "incomplete_value": true,
      "site": "0076bdfc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076bde0",
      "incomplete_value": true,
      "site": "0076bdfc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076be00",
      "incomplete_value": true,
      "site": "0076be18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076be00",
      "incomplete_value": true,
      "site": "0076be18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0076bd9c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0076bdc0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0076bde0",
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
      "0076bd9c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0076bdc0",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0076bde0",
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

- 旧版 [`0076bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076bd60.md#insn-0076bd8c) · [`0076bd94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076bd60.md#insn-0076bd94)
- 新版 [`0076bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076bd60.md#insn-0076bd8c) · [`0076bd94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076bd60.md#insn-0076bd94)

~~~diff
- 0076bd8c ["COPY", "tmp:0:8", ["const:f78:8"]]
- 0076bd8c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0076bd8c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0076bd8c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0076bd8c ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 0076bd8c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0076bd8c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0076bd8c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0076bd8c bytes 73e23d91
+ 0076bd8c bytes 73e23e91
- 0076bd94 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0076bd94 bytes e9d9ff90
+ 0076bd94 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0076bd94 bytes e9d9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3a604af29a1d761c3aede05c1673ee7"></a>

### [`0076c120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076c/0076c120.md) → [`0076c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076c120.md) FUN_0076c120

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0076c0f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076c/0076c0f0.md) · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0073a038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a038.md) [`0076cab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076c/0076cab8.md)
- 新版 呼出元 1件 [`0076c0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076c0f0.md) · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0073a038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a038.md) [`0076cab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076cab8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.62% / 新版 99.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0076c318",
      "incomplete_value": false,
      "site": "0076c32c",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076c318",
      "incomplete_value": false,
      "site": "0076c32c",
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
            "const:fc8:8"
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
      "0076c318",
      "PARAM",
      [
        "storage",
        "00c27fc8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0076c318",
      "PARAM",
      [
        "storage",
        "00c28008",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0076c314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076c/0076c120.md#insn-0076c314) · [`0076c318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076c/0076c120.md#insn-0076c318)
- 新版 [`0076c314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076c120.md#insn-0076c314) · [`0076c318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076c120.md#insn-0076c318)

~~~diff
- 0076c314 ["COPY", "register:4010:8", ["const:c27000:8"]]
+ 0076c314 ["COPY", "register:4010:8", ["const:c28000:8"]]
- 0076c314 bytes c22500f0
+ 0076c314 bytes e2250090
- 0076c318 ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 0076c318 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0076c318 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0076c318 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0076c318 ["COPY", "tmp:0:8", ["const:8:8"]]
+ 0076c318 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0076c318 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0076c318 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0076c318 bytes 42203f91
+ 0076c318 bytes 42200091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-019314bf273d25f953e28c0b2fd31bbd"></a>

### [`0076c5e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076c/0076c5e4.md) → [`0076c5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076c5e4.md) FUN_0076c5e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0076c0f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076c/0076c0f0.md) · 呼出先 7件 [`00759ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759ddc.md) [`008460c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/008460c4.md) [`00846f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/00846f70.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md)
- 新版 呼出元 1件 [`0076c0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076c0f0.md) · 呼出先 7件 [`00759ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759ddc.md) [`008460c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/008460c4.md) [`00846f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846f70.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.24% / 新版 89.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 9件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0076c620",
      "incomplete_value": false,
      "site": "0076c628",
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
            "const:6b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076c620",
      "incomplete_value": false,
      "site": "0076c628",
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
            "const:61c:8"
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
      "definition_site": "0076c648",
      "incomplete_value": false,
      "site": "0076c650",
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
            "const:94d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076c648",
      "incomplete_value": false,
      "site": "0076c650",
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
            "const:8c2:8"
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
      "definition_site": "0076c6a4",
      "incomplete_value": false,
      "site": "0076c6ac",
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
            "const:c06:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076c6a4",
      "incomplete_value": false,
      "site": "0076c6ac",
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
            "const:c93:8"
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
      "0076c628",
      "DATA",
      [
        "storage",
        "002a861c",
        null,
        "string"
      ]
    ],
    [
      "0076c650",
      "DATA",
      [
        "storage",
        "002a38c2",
        null,
        "string"
      ]
    ],
    [
      "0076c694",
      "PARAM",
      [
        "storage",
        "00c27fc8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0076c628",
      "DATA",
      [
        "storage",
        "002a86b6",
        null,
        "string"
      ]
    ],
    [
      "0076c650",
      "DATA",
      [
        "storage",
        "002a394d",
        null,
        "string"
      ]
    ],
    [
      "0076c694",
      "PARAM",
      [
        "storage",
        "00c28008",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0076c620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076c/0076c5e4.md#insn-0076c620) · [`0076c624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076c/0076c5e4.md#insn-0076c624)
- 新版 [`0076c620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076c5e4.md#insn-0076c620) · [`0076c624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076c5e4.md#insn-0076c624)

~~~diff
- 0076c620 ["COPY", "tmp:0:8", ["const:61c:8"]]
- 0076c620 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0076c620 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0076c620 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0076c620 ["COPY", "tmp:0:8", ["const:6b6:8"]]
+ 0076c620 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0076c620 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0076c620 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0076c620 bytes 08711891
+ 0076c620 bytes 08d91a91
- 0076c624 ["COPY", "tmp:0:8", ["const:78:8"]]
- 0076c624 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 0076c624 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 0076c624 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 0076c624 bytes f6e30191
+ 0076c624 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0076c624 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
+ 0076c624 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
+ 0076c624 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
+ 0076c624 bytes f6e30191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e59225396e3183925a216ba8e890621e"></a>

### [`0076cab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076c/0076cab8.md) → [`0076cab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076cab8.md) FUN_0076cab8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0076c120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076c/0076c120.md) · 呼出先 14件 [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`0076c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076c120.md) · 呼出先 14件 [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 90.84% / 新版 90.84%

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
      "definition_site": "0076caec",
      "incomplete_value": false,
      "site": "0076caf4",
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
      "definition_site": "0076caec",
      "incomplete_value": false,
      "site": "0076caf4",
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
      "definition_site": "0076cc24",
      "incomplete_value": true,
      "site": "0076cc28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0076cc24",
      "incomplete_value": true,
      "site": "0076cc28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0076cc20",
      "incomplete_value": true,
      "site": "0076cc2c",
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
      "definition_site": "0076cc20",
      "incomplete_value": true,
      "site": "0076cc2c",
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
      "0076caf4",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "0076cb1c",
      "PARAM",
      [
        "storage",
        "00c27fb0",
        null,
        null
      ]
    ],
    [
      "0076cc14",
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
      "0076caf4",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "0076cb1c",
      "PARAM",
      [
        "storage",
        "00c27ff0",
        null,
        null
      ]
    ],
    [
      "0076cc14",
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

- 旧版 [`0076caec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076c/0076cab8.md#insn-0076caec) · [`0076cb1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076c/0076cab8.md#insn-0076cb1c) · [`0076cc14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076c/0076cab8.md#insn-0076cc14)
- 新版 [`0076caec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076cab8.md#insn-0076caec) · [`0076cb1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076cab8.md#insn-0076cb1c) · [`0076cc14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076cab8.md#insn-0076cc14)

~~~diff
- 0076caec ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0076caec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0076caec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0076caec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0076caec ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 0076caec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0076caec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0076caec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0076caec bytes 08a13491
+ 0076caec bytes 08e13591
- 0076cb1c ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 0076cb1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0076cb1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0076cb1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0076cb1c ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 0076cb1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0076cb1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0076cb1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0076cb1c bytes 00c03e91
+ 0076cb1c bytes 00c03f91
- 0076cc14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 0076cc14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0076cc14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 0076cc14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0076cc14 bytes 08b946f9
+ 0076cc14 bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf363f76fb8869e91111860d69f91163"></a>

### [`0076cd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076c/0076cd80.md) → [`0076cd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076cd80.md) _INIT_137

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 79.81% / 新版 79.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 7件, `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0076cdbc",
      "incomplete_value": true,
      "site": "0076cdd8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076cdbc",
      "incomplete_value": true,
      "site": "0076cdd8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076cde0",
      "incomplete_value": true,
      "site": "0076cdfc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076cde0",
      "incomplete_value": true,
      "site": "0076cdfc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076ce00",
      "incomplete_value": true,
      "site": "0076ce1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076ce00",
      "incomplete_value": true,
      "site": "0076ce1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0076cdbc",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0076cde0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0076ce00",
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
      "0076cdbc",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0076cde0",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0076ce00",
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

- 旧版 [`0076cdac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076c/0076cd80.md#insn-0076cdac) · [`0076cdb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076c/0076cd80.md#insn-0076cdb4)
- 新版 [`0076cdac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076cd80.md#insn-0076cdac) · [`0076cdb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076c/0076cd80.md#insn-0076cdb4)

~~~diff
- 0076cdac ["COPY", "tmp:0:8", ["const:f98:8"]]
- 0076cdac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0076cdac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0076cdac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0076cdac ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 0076cdac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0076cdac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0076cdac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0076cdac bytes 73623e91
+ 0076cdac bytes 73623f91
- 0076cdb4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0076cdb4 bytes c9d9fff0
+ 0076cdb4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0076cdb4 bytes c9d9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ff604f0709de5805112af4073242ec8"></a>

### [`0076d18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076d/0076d18c.md) → [`0076d18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076d18c.md) _INIT_138

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
      "definition_site": "0076d1c8",
      "incomplete_value": true,
      "site": "0076d1e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076d1c8",
      "incomplete_value": true,
      "site": "0076d1e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076d1ec",
      "incomplete_value": true,
      "site": "0076d208",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076d1ec",
      "incomplete_value": true,
      "site": "0076d208",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076d20c",
      "incomplete_value": true,
      "site": "0076d228",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0076d20c",
      "incomplete_value": true,
      "site": "0076d228",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0076d1c8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0076d1ec",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0076d20c",
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
      "0076d1c8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0076d1ec",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0076d20c",
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

- 旧版 [`0076d1b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076d/0076d18c.md#insn-0076d1b4) · [`0076d1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076d/0076d18c.md#insn-0076d1b8) · [`0076d1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076d/0076d18c.md#insn-0076d1c0)
- 新版 [`0076d1b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076d18c.md#insn-0076d1b4) · [`0076d1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076d18c.md#insn-0076d1b8)

~~~diff
- 0076d1b4 ["COPY", "register:4098:8", ["const:c27000:8"]]
+ 0076d1b4 ["COPY", "register:4098:8", ["const:c28000:8"]]
- 0076d1b4 bytes d32500d0
+ 0076d1b4 bytes d32500f0
- 0076d1b8 ["COPY", "tmp:0:8", ["const:fe0:8"]]
- 0076d1b8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0076d1b8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0076d1b8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0076d1b8 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 0076d1b8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0076d1b8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0076d1b8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0076d1b8 bytes 73823f91
+ 0076d1b8 bytes 73820091
- 0076d1c0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0076d1c0 bytes c9d9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e51d0b6c718f175866ee62a1a73326a8"></a>

### [`0076db4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076d/0076db4c.md) → [`0076db4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076db4c.md) FUN_0076db4c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a30514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a30/00a30514.md) · 呼出先 10件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00772ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/00772ee4.md) [`00772ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/00772ee8.md) [`00776238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00776/00776238.md) [`00776270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00776/00776270.md)
- 新版 呼出元 1件 [`00a30558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a30/00a30558.md) · 呼出先 10件 [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00772ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772ee4.md) [`00772ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772ee8.md) [`00776238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00776/00776238.md) [`00776270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00776/00776270.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0076dbbc",
      "incomplete_value": true,
      "site": "0076dbcc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:859:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076dbbc",
      "incomplete_value": true,
      "site": "0076dbcc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7ce:8"
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
      "definition_site": "0076dbbc",
      "incomplete_value": true,
      "site": "0076dbcc",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0076dbbc",
      "incomplete_value": true,
      "site": "0076dbcc",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0076dbf8",
      "incomplete_value": false,
      "site": "0076dbf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076dbf8",
      "incomplete_value": false,
      "site": "0076dbf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "0076dbbc",
      "READ",
      [
        "storage",
        "0029e7ce",
        null,
        "string"
      ]
    ],
    [
      "0076dbbc",
      "READ",
      [
        "storage",
        "0029e7de",
        null,
        "string"
      ]
    ],
    [
      "0076dbf8",
      "DATA",
      [
        "storage",
        "00bfc770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0076dbbc",
      "READ",
      [
        "storage",
        "0029e859",
        null,
        "string"
      ]
    ],
    [
      "0076dbbc",
      "READ",
      [
        "storage",
        "0029e869",
        null,
        "string"
      ]
    ],
    [
      "0076dbf8",
      "DATA",
      [
        "storage",
        "00bfc7c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0076dbb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076d/0076db4c.md#insn-0076dbb8) · [`0076dbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076d/0076db4c.md#insn-0076dbf0) · [`0076dbf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076d/0076db4c.md#insn-0076dbf4)
- 新版 [`0076dbb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076db4c.md#insn-0076dbb8) · [`0076dbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076db4c.md#insn-0076dbf0)

~~~diff
- 0076dbb8 ["COPY", "tmp:0:8", ["const:7ce:8"]]
- 0076dbb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0076dbb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0076dbb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0076dbb8 ["COPY", "tmp:0:8", ["const:859:8"]]
+ 0076dbb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0076dbb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0076dbb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0076dbb8 bytes 08391f91
+ 0076dbb8 bytes 08652191
- 0076dbf0 ["COPY", "tmp:0:8", ["const:770:8"]]
- 0076dbf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0076dbf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0076dbf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0076dbf0 ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 0076dbf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0076dbf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0076dbf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0076dbf0 bytes 08c11d91
+ 0076dbf0 bytes 08011f91
- 0076dbf4 ["INT_SUB", "register:40a0:8", ["register:40e8:8", "const:40:8"]]
- 0076dbf4 bytes b40301d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f4d1dc130d899f21eb387d65e3224d4"></a>

### [`0076dd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076d/0076dd00.md) → [`0076dd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076dd00.md) FUN_0076dd00

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008648a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md) · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0051dea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051dea4.md) [`00776238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00776/00776238.md) [`00776270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00776/00776270.md)
- 新版 呼出元 1件 [`008648a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008648a8.md) · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0051dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`00776238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00776/00776238.md) [`00776270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00776/00776270.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.97% / 新版 97.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0076def0",
      "incomplete_value": true,
      "site": "0076df00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:87c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076def0",
      "incomplete_value": true,
      "site": "0076df00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7f1:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0076def4",
      "incomplete_value": true,
      "site": "0076df04",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0076def4",
      "incomplete_value": true,
      "site": "0076df04",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 33,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0076e454",
      "incomplete_value": true,
      "site": "0076e46c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6c5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076e454",
      "incomplete_value": true,
      "site": "0076e46c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:62b:8"
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
      "0076dd74",
      "READ",
      [
        "storage",
        "002a38c8",
        null,
        "string"
      ]
    ],
    [
      "0076dd78",
      "READ",
      [
        "storage",
        "002a38d7",
        null,
        "string"
      ]
    ],
    [
      "0076def0",
      "READ",
      [
        "storage",
        "0029e7f1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0076dd74",
      "READ",
      [
        "storage",
        "002a3953",
        null,
        "string"
      ]
    ],
    [
      "0076dd78",
      "READ",
      [
        "storage",
        "002a3962",
        null,
        "string"
      ]
    ],
    [
      "0076def0",
      "READ",
      [
        "storage",
        "0029e87c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0076dd6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076d/0076dd00.md#insn-0076dd6c) · [`0076dd70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076d/0076dd00.md#insn-0076dd70)
- 新版 [`0076dd6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076dd00.md#insn-0076dd6c) · [`0076dd70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076dd00.md#insn-0076dd70)

~~~diff
- 0076dd6c ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 0076dd6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0076dd6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0076dd6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0076dd6c ["COPY", "tmp:0:8", ["const:953:8"]]
+ 0076dd6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0076dd6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0076dd6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0076dd6c bytes 08212391
+ 0076dd6c bytes 084d2591
- 0076dd70 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0076dd70 bytes 09dafff0
+ 0076dd70 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0076dd70 bytes 09dafff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a5749d5d529868fb55e3f5da2ad60bd"></a>

### [`0076e98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076e/0076e98c.md) → [`0076e98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e98c.md) FUN_0076e98c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008648a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md) · 呼出先 31件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md) [`0042eb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md) [`00436518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436518.md) [`00436954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436954.md)
- 新版 呼出元 1件 [`008648a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008648a8.md) · 呼出先 31件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0042e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md) [`0042eb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md) [`00436518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436518.md) [`00436954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436954.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.73% / 新版 93.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 14件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0076e9d0",
      "incomplete_value": false,
      "site": "0076e9dc",
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
      "definition_site": "0076e9d0",
      "incomplete_value": false,
      "site": "0076e9dc",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0076ea08",
      "incomplete_value": true,
      "site": "0076ea1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e84:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076ea08",
      "incomplete_value": true,
      "site": "0076ea1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f11:8"
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
      "definition_site": "0076ea08",
      "incomplete_value": true,
      "site": "0076ea1c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0076ea08",
      "incomplete_value": true,
      "site": "0076ea1c",
      "value": [
        "LOAD",
        "16",
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
      "0076e9dc",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ],
    [
      "0076ea08",
      "READ",
      [
        "storage",
        "00296f11",
        null,
        "string"
      ]
    ],
    [
      "0076ea08",
      "READ",
      [
        "storage",
        "00296f21",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0076e9dc",
      "DATA",
      [
        "storage",
        "00be6b20",
        null,
        "pointer"
      ]
    ],
    [
      "0076ea08",
      "READ",
      [
        "storage",
        "00296e84",
        null,
        "string"
      ]
    ],
    [
      "0076ea08",
      "READ",
      [
        "storage",
        "00296e94",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0076e9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076e/0076e98c.md#insn-0076e9d0) · [`0076e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076e/0076e98c.md#insn-0076e9d8)
- 新版 [`0076e9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e98c.md#insn-0076e9d0) · [`0076e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e98c.md#insn-0076e9d8)

~~~diff
- 0076e9d0 ["COPY", "tmp:0:8", ["const:ad0:8"]]
- 0076e9d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0076e9d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0076e9d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0076e9d0 ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 0076e9d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0076e9d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0076e9d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0076e9d0 bytes 29412b91
+ 0076e9d0 bytes 29812c91
- 0076e9d8 ["COPY", "register:4040:8", ["register:4000:8"]]
- 0076e9d8 bytes e80300aa
+ 0076e9d8 ["COPY", "register:4040:8", ["register:4000:8"]]
+ 0076e9d8 bytes e80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67f3c3da015f3cdea158ad964d29db48"></a>

### [`0077032c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/0077032c.md) → [`0077032c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/0077032c.md) FUN_0077032c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00859148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859148.md) [`00a2c36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2c/00a2c36c.md) · 呼出先 6件 [`0077047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/0077047c.md) [`00773348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773348.md) [`0077334c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/0077334c.md) [`007733d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007733d0.md) [`007733d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007733d4.md)
- 新版 呼出元 2件 [`00859148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859148.md) [`00a2c3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2c/00a2c3b0.md) · 呼出先 6件 [`0077047c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/0077047c.md) [`00773348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773348.md) [`0077334c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/0077334c.md) [`007733d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007733d0.md) [`007733d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007733d4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00770354",
      "incomplete_value": false,
      "site": "00770354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00770354",
      "incomplete_value": false,
      "site": "00770354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
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
      "definition_site": "0077036c",
      "incomplete_value": false,
      "site": "0077036c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077036c",
      "incomplete_value": false,
      "site": "0077036c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "00770354",
      "DATA",
      [
        "storage",
        "00bfc7f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0077036c",
      "DATA",
      [
        "storage",
        "00bfc870",
        null,
        "undefined *"
      ]
    ],
    [
      "007703a4",
      "READ",
      [
        "storage",
        "00bfc890",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00770354",
      "DATA",
      [
        "storage",
        "00bfc840",
        null,
        "undefined *"
      ]
    ],
    [
      "0077036c",
      "DATA",
      [
        "storage",
        "00bfc8c0",
        null,
        "undefined *"
      ]
    ],
    [
      "007703a4",
      "READ",
      [
        "storage",
        "00bfc8e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00770350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/0077032c.md#insn-00770350) · [`00770364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/0077032c.md#insn-00770364)
- 新版 [`00770350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/0077032c.md#insn-00770350) · [`00770364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/0077032c.md#insn-00770364)

~~~diff
- 00770350 ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 00770350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00770350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00770350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00770350 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 00770350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00770350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00770350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00770350 bytes 08c11f91
+ 00770350 bytes 08012191
- 00770364 ["COPY", "tmp:0:8", ["const:870:8"]]
- 00770364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00770364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00770364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00770364 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00770364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00770364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00770364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00770364 bytes 08c12191
+ 00770364 bytes 08012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-222a3a0ef998f236d3f5c0591ff09209"></a>

### [`0077047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/0077047c.md) → [`0077047c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/0077047c.md) FUN_0077047c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0077032c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/0077032c.md) · 呼出先 14件 [`005760a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576268.md) [`00578ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578ff0.md) [`0076b910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b910.md) [`0076b948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b948.md)
- 新版 呼出元 1件 [`0077032c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/0077032c.md) · 呼出先 14件 [`005760a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576268.md) [`00578ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md) [`0076b910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b910.md) [`0076b948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b948.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.35% / 新版 96.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007704d8",
      "incomplete_value": false,
      "site": "007704dc",
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
                "const:bf1000:8"
              ],
              [
                "leaf",
                "const:6e8:8"
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
      "definition_site": "007704d8",
      "incomplete_value": false,
      "site": "007704dc",
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
                "const:bf1000:8"
              ],
              [
                "leaf",
                "const:698:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00770508",
      "incomplete_value": false,
      "site": "0077050c",
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
      "definition_site": "00770508",
      "incomplete_value": false,
      "site": "0077050c",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007705dc",
      "incomplete_value": false,
      "site": "007705dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007705dc",
      "incomplete_value": false,
      "site": "007705dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:c90:8"
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
      "007704dc",
      "DATA",
      [
        "storage",
        "00bf16a8",
        null,
        "undefined *"
      ]
    ],
    [
      "0077050c",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ],
    [
      "007705dc",
      "DATA",
      [
        "storage",
        "00bfcc90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007704dc",
      "DATA",
      [
        "storage",
        "00bf16f8",
        null,
        "undefined *"
      ]
    ],
    [
      "0077050c",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ],
    [
      "007705dc",
      "DATA",
      [
        "storage",
        "00bfcce0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007704d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/0077047c.md#insn-007704d0) · [`00770500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/0077047c.md#insn-00770500) · [`007705d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/0077047c.md#insn-007705d4)
- 新版 [`007704d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/0077047c.md#insn-007704d0) · [`00770500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/0077047c.md#insn-00770500) · [`007705d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/0077047c.md#insn-007705d4)

~~~diff
- 007704d0 ["COPY", "tmp:0:8", ["const:698:8"]]
- 007704d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007704d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007704d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007704d0 ["COPY", "tmp:0:8", ["const:6e8:8"]]
+ 007704d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007704d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007704d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007704d0 bytes 08611a91
+ 007704d0 bytes 08a11b91
- 00770500 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 00770500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00770500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00770500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00770500 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 00770500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00770500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00770500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00770500 bytes 08012891
+ 00770500 bytes 08412991
- 007705d4 ["COPY", "tmp:0:8", ["const:c90:8"]]
- 007705d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007705d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007705d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007705d4 ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 007705d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007705d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007705d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007705d4 bytes 08413291
+ 007705d4 bytes 08813391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21bee5ad40ea330d950bfcc28b408593"></a>

### [`00770bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/00770bfc.md) → [`00770bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/00770bfc.md) FUN_00770bfc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00770a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/00770a74.md) · 呼出先 9件 [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) [`0042fd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fd7c.md) [`0073a038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a038.md) [`0073e258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e258.md) [`007734c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007734c8.md)
- 新版 呼出元 1件 [`00770a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/00770a74.md) · 呼出先 9件 [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`0042fd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md) [`0073a038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a038.md) [`0073e258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e258.md) [`007734c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007734c8.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "00770c40",
      "incomplete_value": false,
      "site": "00770c40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00770c40",
      "incomplete_value": false,
      "site": "00770c40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
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
      "00770c40",
      "DATA",
      [
        "storage",
        "00bfc8f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00770c80",
      "READ",
      [
        "storage",
        "00bfc910",
        null,
        "pointer"
      ]
    ],
    [
      "00770c80",
      "READ",
      [
        "storage",
        "00bfc918",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00770c40",
      "DATA",
      [
        "storage",
        "00bfc940",
        null,
        "undefined *"
      ]
    ],
    [
      "00770c80",
      "READ",
      [
        "storage",
        "00bfc960",
        null,
        "pointer"
      ]
    ],
    [
      "00770c80",
      "READ",
      [
        "storage",
        "00bfc968",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00770c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/00770bfc.md#insn-00770c3c)
- 新版 [`00770c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/00770bfc.md#insn-00770c3c)

~~~diff
- 00770c3c ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 00770c3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00770c3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00770c3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00770c3c ["COPY", "tmp:0:8", ["const:940:8"]]
+ 00770c3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00770c3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00770c3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00770c3c bytes 08c12391
+ 00770c3c bytes 08012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f47651a27843deb5253ae6306ba5da5e"></a>

### [`00770d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/00770d6c.md) → [`00770d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/00770d6c.md) FUN_00770d6c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`007734d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007734d0.md) · 呼出先 6件 [`00770eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/00770eb8.md) [`007735f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007735f8.md) [`007735fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007735fc.md) [`0077367c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/0077367c.md) [`00773680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773680.md)
- 新版 呼出元 1件 [`007734d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007734d0.md) · 呼出先 6件 [`00770eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/00770eb8.md) [`007735f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007735f8.md) [`007735fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007735fc.md) [`0077367c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/0077367c.md) [`00773680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773680.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00770d94",
      "incomplete_value": false,
      "site": "00770d94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00770d94",
      "incomplete_value": false,
      "site": "00770d94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "definition_site": "00770da8",
      "incomplete_value": false,
      "site": "00770da8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00770da8",
      "incomplete_value": false,
      "site": "00770da8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "00770d94",
      "DATA",
      [
        "storage",
        "00bfc970",
        null,
        "undefined *"
      ]
    ],
    [
      "00770da8",
      "DATA",
      [
        "storage",
        "00bfca00",
        null,
        "undefined *"
      ]
    ],
    [
      "00770de0",
      "READ",
      [
        "storage",
        "00bfca20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00770d94",
      "DATA",
      [
        "storage",
        "00bfc9c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00770da8",
      "DATA",
      [
        "storage",
        "00bfca50",
        null,
        "undefined *"
      ]
    ],
    [
      "00770de0",
      "READ",
      [
        "storage",
        "00bfca70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00770d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/00770d6c.md#insn-00770d90) · [`00770da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/00770d6c.md#insn-00770da4)
- 新版 [`00770d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/00770d6c.md#insn-00770d90) · [`00770da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/00770d6c.md#insn-00770da4)

~~~diff
- 00770d90 ["COPY", "tmp:0:8", ["const:970:8"]]
- 00770d90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00770d90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00770d90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00770d90 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00770d90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00770d90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00770d90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00770d90 bytes 08c12591
+ 00770d90 bytes 08012791
- 00770da4 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 00770da4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00770da4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00770da4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00770da4 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 00770da4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00770da4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00770da4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00770da4 bytes 08012891
+ 00770da4 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-130b41abe5c614b78b7e192e5aa7cb87"></a>

### [`00770eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/00770eb8.md) → [`00770eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/00770eb8.md) FUN_00770eb8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00770d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/00770d6c.md) · 呼出先 14件 [`005760a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576268.md) [`00578ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578ff0.md) [`0076b910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b910.md) [`0076b948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b948.md)
- 新版 呼出元 1件 [`00770d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/00770d6c.md) · 呼出先 14件 [`005760a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576268.md) [`00578ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md) [`0076b910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b910.md) [`0076b948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b948.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.35% / 新版 96.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00770f14",
      "incomplete_value": false,
      "site": "00770f18",
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
                "const:bf1000:8"
              ],
              [
                "leaf",
                "const:860:8"
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
      "definition_site": "00770f14",
      "incomplete_value": false,
      "site": "00770f18",
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
                "const:bf1000:8"
              ],
              [
                "leaf",
                "const:810:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00770f44",
      "incomplete_value": false,
      "site": "00770f48",
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
      "definition_site": "00770f44",
      "incomplete_value": false,
      "site": "00770f48",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00771018",
      "incomplete_value": false,
      "site": "00771018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00771018",
      "incomplete_value": false,
      "site": "00771018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "00770f18",
      "DATA",
      [
        "storage",
        "00bf1820",
        null,
        "undefined *"
      ]
    ],
    [
      "00770f48",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ],
    [
      "00771018",
      "DATA",
      [
        "storage",
        "00bfcd90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00770f18",
      "DATA",
      [
        "storage",
        "00bf1870",
        null,
        "undefined *"
      ]
    ],
    [
      "00770f48",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ],
    [
      "00771018",
      "DATA",
      [
        "storage",
        "00bfcde0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00770f0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/00770eb8.md#insn-00770f0c) · [`00770f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/00770eb8.md#insn-00770f3c) · [`00771010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/00770eb8.md#insn-00771010)
- 新版 [`00770f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/00770eb8.md#insn-00770f0c) · [`00770f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/00770eb8.md#insn-00770f3c) · [`00771010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/00770eb8.md#insn-00771010)

~~~diff
- 00770f0c ["COPY", "tmp:0:8", ["const:810:8"]]
- 00770f0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00770f0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00770f0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00770f0c ["COPY", "tmp:0:8", ["const:860:8"]]
+ 00770f0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00770f0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00770f0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00770f0c bytes 08412091
+ 00770f0c bytes 08812191
- 00770f3c ["COPY", "tmp:0:8", ["const:a00:8"]]
- 00770f3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00770f3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00770f3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00770f3c ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 00770f3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00770f3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00770f3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00770f3c bytes 08012891
+ 00770f3c bytes 08412991
- 00771010 ["COPY", "tmp:0:8", ["const:d90:8"]]
- 00771010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00771010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00771010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00771010 ["COPY", "tmp:0:8", ["const:de0:8"]]
+ 00771010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00771010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00771010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00771010 bytes 08413691
+ 00771010 bytes 08813791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c05d503b8b7ba1bd4cf2a376e8403bee"></a>

### [`007717a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00771/007717a8.md) → [`007717a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00771/007717a8.md) FUN_007717a8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`007714b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00771/007714b0.md) · 呼出先 6件 [`007718f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00771/007718f4.md) [`00773774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773774.md) [`00773778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773778.md) [`007737f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007737f8.md) [`007737fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007737fc.md)
- 新版 呼出元 1件 [`007714b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00771/007714b0.md) · 呼出先 6件 [`007718f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00771/007718f4.md) [`00773774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773774.md) [`00773778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773778.md) [`007737f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007737f8.md) [`007737fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007737fc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007717d0",
      "incomplete_value": false,
      "site": "007717d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007717d0",
      "incomplete_value": false,
      "site": "007717d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "definition_site": "007717e4",
      "incomplete_value": false,
      "site": "007717e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007717e4",
      "incomplete_value": false,
      "site": "007717e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:b10:8"
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
      "007717d0",
      "DATA",
      [
        "storage",
        "00bfca80",
        null,
        "undefined *"
      ]
    ],
    [
      "007717e4",
      "DATA",
      [
        "storage",
        "00bfcb10",
        null,
        "undefined *"
      ]
    ],
    [
      "0077181c",
      "READ",
      [
        "storage",
        "00bfcb30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007717d0",
      "DATA",
      [
        "storage",
        "00bfcad0",
        null,
        "undefined *"
      ]
    ],
    [
      "007717e4",
      "DATA",
      [
        "storage",
        "00bfcb60",
        null,
        "undefined *"
      ]
    ],
    [
      "0077181c",
      "READ",
      [
        "storage",
        "00bfcb80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007717cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00771/007717a8.md#insn-007717cc) · [`007717e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00771/007717a8.md#insn-007717e0)
- 新版 [`007717cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00771/007717a8.md#insn-007717cc) · [`007717e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00771/007717a8.md#insn-007717e0)

~~~diff
- 007717cc ["COPY", "tmp:0:8", ["const:a80:8"]]
- 007717cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007717cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007717cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007717cc ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 007717cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007717cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007717cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007717cc bytes 08012a91
+ 007717cc bytes 08412b91
- 007717e0 ["COPY", "tmp:0:8", ["const:b10:8"]]
- 007717e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007717e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007717e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007717e0 ["COPY", "tmp:0:8", ["const:b60:8"]]
+ 007717e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007717e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007717e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007717e0 bytes 08412c91
+ 007717e0 bytes 08812d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3198f7c7303f37840130b1589667398"></a>

### [`007718f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00771/007718f4.md) → [`007718f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00771/007718f4.md) FUN_007718f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007717a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00771/007717a8.md) · 呼出先 15件 [`005760a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576268.md) [`0057efa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057efa8.md) [`0076b910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b910.md) [`0076b948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b948.md)
- 新版 呼出元 1件 [`007717a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00771/007717a8.md) · 呼出先 15件 [`005760a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576268.md) [`0057efa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057efa8.md) [`0076b910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b910.md) [`0076b948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b948.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.43% / 新版 98.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00771a04",
      "incomplete_value": false,
      "site": "00771a04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00771a04",
      "incomplete_value": false,
      "site": "00771a04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "definition_site": "00771b84",
      "incomplete_value": false,
      "site": "00771b84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00771b84",
      "incomplete_value": false,
      "site": "00771b84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "00771a04",
      "DATA",
      [
        "storage",
        "00bfcb90",
        null,
        "undefined *"
      ]
    ],
    [
      "00771ab8",
      "READ",
      [
        "storage",
        "00bfcbb8",
        null,
        "undefined *"
      ]
    ],
    [
      "00771b84",
      "DATA",
      [
        "storage",
        "00bfcc10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00771a04",
      "DATA",
      [
        "storage",
        "00bfcbe0",
        null,
        "undefined *"
      ]
    ],
    [
      "00771ab8",
      "READ",
      [
        "storage",
        "00bfcc08",
        null,
        "undefined *"
      ]
    ],
    [
      "00771b84",
      "DATA",
      [
        "storage",
        "00bfcc60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007719fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00771/007718f4.md#insn-007719fc) · [`00771b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00771/007718f4.md#insn-00771b7c)
- 新版 [`007719fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00771/007718f4.md#insn-007719fc) · [`00771b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00771/007718f4.md#insn-00771b7c)

~~~diff
- 007719fc ["COPY", "tmp:0:8", ["const:b90:8"]]
- 007719fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007719fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007719fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007719fc ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 007719fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007719fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007719fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007719fc bytes 08412e91
+ 007719fc bytes 08812f91
- 00771b7c ["COPY", "tmp:0:8", ["const:c10:8"]]
- 00771b7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00771b7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00771b7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00771b7c ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 00771b7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00771b7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00771b7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00771b7c bytes 08413091
+ 00771b7c bytes 08813191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-972eb472a174a1d49d4d1c90d1003872"></a>

### [`0077252c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/0077252c.md) → [`0077252c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/0077252c.md) FUN_0077252c

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
      "definition_site": "00772550",
      "incomplete_value": false,
      "site": "00772554",
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
      "definition_site": "00772550",
      "incomplete_value": false,
      "site": "00772554",
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
      "00772554",
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
      "00772554",
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

- 旧版 [`00772548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/0077252c.md#insn-00772548)
- 新版 [`00772548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/0077252c.md#insn-00772548)

~~~diff
- 00772548 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 00772548 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00772548 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00772548 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00772548 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 00772548 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00772548 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00772548 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00772548 bytes 08012891
+ 00772548 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df2b65bc701b236b38cec1de4435362e"></a>

### [`00772614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/00772614.md) → [`00772614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772614.md) FUN_00772614

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
      "definition_site": "00772638",
      "incomplete_value": false,
      "site": "0077263c",
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
      "definition_site": "00772638",
      "incomplete_value": false,
      "site": "0077263c",
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
      "0077263c",
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
      "0077263c",
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

- 旧版 [`00772630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/00772614.md#insn-00772630)
- 新版 [`00772630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772614.md#insn-00772630)

~~~diff
- 00772630 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 00772630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00772630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00772630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00772630 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 00772630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00772630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00772630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00772630 bytes 08012891
+ 00772630 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed7afa2ab978e42abdc62a9de41bb66e"></a>

### [`00772eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/00772eb0.md) → [`00772eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772eb0.md) FUN_00772eb0

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
      "definition_site": "00772ec4",
      "incomplete_value": false,
      "site": "00772ec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00772ec4",
      "incomplete_value": false,
      "site": "00772ec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "00772ec8",
      "DATA",
      [
        "storage",
        "00bfc770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00772ec8",
      "DATA",
      [
        "storage",
        "00bfc7c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00772ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/00772eb0.md#insn-00772ec4)
- 新版 [`00772ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772eb0.md#insn-00772ec4)

~~~diff
- 00772ec4 ["COPY", "tmp:0:8", ["const:770:8"]]
- 00772ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00772ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00772ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00772ec4 ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 00772ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00772ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00772ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00772ec4 bytes 08c11d91
+ 00772ec4 bytes 08011f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f146f92d39c0961187298cdacf1b786"></a>

### [`00772ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/00772ed4.md) → [`00772ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772ed4.md) FUN_00772ed4

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
      "definition_site": "00772ed8",
      "incomplete_value": false,
      "site": "00772edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00772ed8",
      "incomplete_value": false,
      "site": "00772edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "00772edc",
      "DATA",
      [
        "storage",
        "00bfc770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00772edc",
      "DATA",
      [
        "storage",
        "00bfc7c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00772ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/00772ed4.md#insn-00772ed8)
- 新版 [`00772ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772ed4.md#insn-00772ed8)

~~~diff
- 00772ed8 ["COPY", "tmp:0:8", ["const:770:8"]]
- 00772ed8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00772ed8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00772ed8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00772ed8 ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 00772ed8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00772ed8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00772ed8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00772ed8 bytes 08c11d91
+ 00772ed8 bytes 08011f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dc725bc3f266fcd46d9d51a701d2f2f"></a>

### [`007730a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007730a4.md) → [`007730a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007730a4.md) FUN_007730a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00772f5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/00772f5c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00772f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772f5c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "007730b0",
      "incomplete_value": false,
      "site": "007730b4",
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
      "definition_site": "007730b0",
      "incomplete_value": false,
      "site": "007730b4",
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
      "007730b0",
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
      "007730b0",
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

- 旧版 [`007730b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007730a4.md#insn-007730b0)
- 新版 [`007730b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007730a4.md#insn-007730b0)

~~~diff
- 007730b0 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007730b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007730b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007730b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007730b0 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007730b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007730b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007730b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007730b0 bytes 000c0c91
+ 007730b0 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44437eb0d6df2deb3a47f01f9f6250f9"></a>

### [`00773300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773300.md) → [`00773300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773300.md) FUN_00773300

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
      "definition_site": "00773324",
      "incomplete_value": false,
      "site": "00773324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00773324",
      "incomplete_value": false,
      "site": "00773324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
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
      "00773324",
      "DATA",
      [
        "storage",
        "00bfc7f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00773324",
      "DATA",
      [
        "storage",
        "00bfc840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00773320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773300.md#insn-00773320)
- 新版 [`00773320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773300.md#insn-00773320)

~~~diff
- 00773320 ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 00773320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00773320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00773320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00773320 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 00773320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00773320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00773320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00773320 bytes 08c11f91
+ 00773320 bytes 08012191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6827532b8d20b1f9d047ca18e518e6d1"></a>

### [`00773334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773334.md) → [`00773334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773334.md) FUN_00773334

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
      "definition_site": "00773340",
      "incomplete_value": false,
      "site": "00773340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00773340",
      "incomplete_value": false,
      "site": "00773340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
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
      "00773340",
      "DATA",
      [
        "storage",
        "00bfc7f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00773340",
      "DATA",
      [
        "storage",
        "00bfc840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077333c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773334.md#insn-0077333c)
- 新版 [`0077333c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773334.md#insn-0077333c)

~~~diff
- 0077333c ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 0077333c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0077333c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0077333c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0077333c ["COPY", "tmp:0:8", ["const:840:8"]]
+ 0077333c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0077333c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0077333c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0077333c bytes 29c11f91
+ 0077333c bytes 29012191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87b12c299f567963b01dcbd4786db334"></a>

### [`00773388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773388.md) → [`00773388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773388.md) FUN_00773388

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
      "definition_site": "007733ac",
      "incomplete_value": false,
      "site": "007733ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007733ac",
      "incomplete_value": false,
      "site": "007733ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
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
      "007733ac",
      "DATA",
      [
        "storage",
        "00bfc870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007733ac",
      "DATA",
      [
        "storage",
        "00bfc8c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007733a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773388.md#insn-007733a8)
- 新版 [`007733a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773388.md#insn-007733a8)

~~~diff
- 007733a8 ["COPY", "tmp:0:8", ["const:870:8"]]
- 007733a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007733a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007733a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007733a8 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 007733a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007733a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007733a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007733a8 bytes 08c12191
+ 007733a8 bytes 08012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd929ce4f6703d735a6402625abefb3d"></a>

### [`007733bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007733bc.md) → [`007733bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007733bc.md) FUN_007733bc

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
      "definition_site": "007733c8",
      "incomplete_value": false,
      "site": "007733c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007733c8",
      "incomplete_value": false,
      "site": "007733c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
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
      "007733c8",
      "DATA",
      [
        "storage",
        "00bfc870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007733c8",
      "DATA",
      [
        "storage",
        "00bfc8c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007733c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007733bc.md#insn-007733c4)
- 新版 [`007733c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007733bc.md#insn-007733c4)

~~~diff
- 007733c4 ["COPY", "tmp:0:8", ["const:870:8"]]
- 007733c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007733c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007733c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007733c4 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 007733c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007733c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007733c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007733c4 bytes 29c12191
+ 007733c4 bytes 29012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce1db64265b6339e68c5150e67af93fe"></a>

### [`00773480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773480.md) → [`00773480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773480.md) FUN_00773480

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
      "definition_site": "007734a4",
      "incomplete_value": false,
      "site": "007734a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007734a4",
      "incomplete_value": false,
      "site": "007734a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
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
      "007734a4",
      "DATA",
      [
        "storage",
        "00bfc8f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007734a4",
      "DATA",
      [
        "storage",
        "00bfc940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007734a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773480.md#insn-007734a0)
- 新版 [`007734a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773480.md#insn-007734a0)

~~~diff
- 007734a0 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 007734a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007734a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007734a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007734a0 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 007734a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007734a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007734a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007734a0 bytes 08c12391
+ 007734a0 bytes 08012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d893cab4483f8976c6b95881754f64a8"></a>

### [`007734b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007734b4.md) → [`007734b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007734b4.md) FUN_007734b4

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
      "definition_site": "007734c0",
      "incomplete_value": false,
      "site": "007734c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007734c0",
      "incomplete_value": false,
      "site": "007734c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
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
      "007734c0",
      "DATA",
      [
        "storage",
        "00bfc8f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007734c0",
      "DATA",
      [
        "storage",
        "00bfc940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007734bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007734b4.md#insn-007734bc)
- 新版 [`007734bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007734b4.md#insn-007734bc)

~~~diff
- 007734bc ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 007734bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007734bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007734bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007734bc ["COPY", "tmp:0:8", ["const:940:8"]]
+ 007734bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007734bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007734bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007734bc bytes 29c12391
+ 007734bc bytes 29012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e117e2d13d92bcfbb3a26bf764897c43"></a>

### [`007735b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007735b0.md) → [`007735b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007735b0.md) FUN_007735b0

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
      "definition_site": "007735d4",
      "incomplete_value": false,
      "site": "007735d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007735d4",
      "incomplete_value": false,
      "site": "007735d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
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
      "007735d4",
      "DATA",
      [
        "storage",
        "00bfc970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007735d4",
      "DATA",
      [
        "storage",
        "00bfc9c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007735d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007735b0.md#insn-007735d0)
- 新版 [`007735d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007735b0.md#insn-007735d0)

~~~diff
- 007735d0 ["COPY", "tmp:0:8", ["const:970:8"]]
- 007735d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007735d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007735d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007735d0 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 007735d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007735d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007735d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007735d0 bytes 08c12591
+ 007735d0 bytes 08012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0f5d7e7c3a5d10c85b5446b0f7faae8"></a>

### [`007735e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007735e4.md) → [`007735e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007735e4.md) FUN_007735e4

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
      "definition_site": "007735f0",
      "incomplete_value": false,
      "site": "007735f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007735f0",
      "incomplete_value": false,
      "site": "007735f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
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
      "007735f0",
      "DATA",
      [
        "storage",
        "00bfc970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007735f0",
      "DATA",
      [
        "storage",
        "00bfc9c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007735ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007735e4.md#insn-007735ec)
- 新版 [`007735ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007735e4.md#insn-007735ec)

~~~diff
- 007735ec ["COPY", "tmp:0:8", ["const:970:8"]]
- 007735ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007735ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007735ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007735ec ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 007735ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007735ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007735ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007735ec bytes 29c12591
+ 007735ec bytes 29012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d111b0dee9f9017bb365f9a6972a5b5a"></a>

### [`00773634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773634.md) → [`00773634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773634.md) FUN_00773634

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
      "definition_site": "00773658",
      "incomplete_value": false,
      "site": "00773658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00773658",
      "incomplete_value": false,
      "site": "00773658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "00773658",
      "DATA",
      [
        "storage",
        "00bfca00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00773658",
      "DATA",
      [
        "storage",
        "00bfca50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00773654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773634.md#insn-00773654)
- 新版 [`00773654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773634.md#insn-00773654)

~~~diff
- 00773654 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 00773654 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00773654 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00773654 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00773654 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 00773654 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00773654 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00773654 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00773654 bytes 08012891
+ 00773654 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

