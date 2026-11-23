# v15.7.3 → v15.7.4 · 最優先の変更候補 (60)

[一覧の目次](README.md)

<a id="compare-db2ced69f8c4f5f86ac23e40c441e0ec"></a>

### [`00acd7bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd7bc.md) → [`00acd800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd800.md) FUN_00acd800

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00acd5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd5b8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00acd5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd5fc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00acd80c",
      "incomplete_value": false,
      "site": "00acd810",
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
      "definition_site": "00acd7c8",
      "incomplete_value": false,
      "site": "00acd7cc",
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
      "00acd80c",
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
      "00acd80c",
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

- 旧版 [`00acd7cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd7bc.md#insn-00acd7cc) · [`00acd7c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd7bc.md#insn-00acd7c8)
- 新版 [`00acd810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd800.md#insn-00acd810) · [`00acd80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd800.md#insn-00acd80c)

~~~diff
- 00acd7cc ["INT_ADD", "register:40f0:8", ["const:acd7cc:8", "const:4:8"]]
- 00acd7cc ["CALL", null, ["callee:00418c38:8"]]
+ 00acd810 ["INT_ADD", "register:40f0:8", ["const:acd810:8", "const:4:8"]]
+ 00acd810 ["CALL", null, ["callee:00418c38:8"]]
- 00acd7cc bytes 1b2de597
+ 00acd810 bytes 0a2de597
- 00acd7c8 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00acd7c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00acd7c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00acd7c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00acd80c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00acd80c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00acd80c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00acd80c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00acd7c8 bytes 000c0c91
+ 00acd80c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d74969faa193c36a641d6ca09acb45f6"></a>

### [`00acd7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd7d0.md) → [`00acd814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd814.md) FUN_00acd814

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00acd81c",
      "incomplete_value": false,
      "site": "00acd820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acd7d8",
      "incomplete_value": false,
      "site": "00acd7dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "00acd820",
      "DATA",
      [
        "storage",
        "00c0f7f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acd820",
      "DATA",
      [
        "storage",
        "00c0f848",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acd7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd7d0.md#insn-00acd7d8)
- 新版 [`00acd81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd814.md#insn-00acd81c)

~~~diff
- 00acd7d8 ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 00acd7d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00acd7d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00acd7d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00acd81c ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00acd81c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00acd81c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00acd81c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00acd7d8 bytes 29e11f91
+ 00acd81c bytes 29212191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f68352131db2d49e659ed78c7a225d8f"></a>

### [`00acd7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd7f0.md) → [`00acd834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd834.md) FUN_00acd834

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00acd83c",
      "incomplete_value": false,
      "site": "00acd840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acd7f8",
      "incomplete_value": false,
      "site": "00acd7fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "00acd840",
      "DATA",
      [
        "storage",
        "00c0f7f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acd840",
      "DATA",
      [
        "storage",
        "00c0f848",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acd7f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd7f0.md#insn-00acd7f8) · [`00acd81c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd7f0.md#insn-00acd81c)
- 新版 [`00acd83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd834.md#insn-00acd83c) · [`00acd860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd834.md#insn-00acd860)

~~~diff
- 00acd7f8 ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 00acd7f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00acd7f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00acd7f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00acd83c ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00acd83c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00acd83c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00acd83c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00acd7f8 bytes 29e11f91
+ 00acd83c bytes 29212191
- 00acd81c ["INT_ADD", "register:40f0:8", ["const:acd81c:8", "const:4:8"]]
- 00acd81c ["CALL", null, ["callee:00bdb060:8"]]
+ 00acd860 ["INT_ADD", "register:40f0:8", ["const:acd860:8", "const:4:8"]]
+ 00acd860 ["CALL", null, ["callee:00bdb060:8"]]
- 00acd81c bytes fd350494
+ 00acd860 bytes 00360494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d2eaba81d4da6f6802f01051ce11aaf"></a>

### [`00acd830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd830.md) → [`00acd874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd874.md) FUN_00acd874

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00acd8a4",
      "incomplete_value": false,
      "site": "00acd8a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acd860",
      "incomplete_value": false,
      "site": "00acd860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "00acd8a4",
      "DATA",
      [
        "storage",
        "00c0f7f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acd8a4",
      "DATA",
      [
        "storage",
        "00c0f848",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acd844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd830.md#insn-00acd844) · [`00acd854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd830.md#insn-00acd854) · [`00acd884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd830.md#insn-00acd884)
- 新版 [`00acd888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd874.md#insn-00acd888) · [`00acd898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd874.md#insn-00acd898) · [`00acd8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd874.md#insn-00acd8c8)

~~~diff
- 00acd844 ["INT_ADD", "register:40f0:8", ["const:acd844:8", "const:4:8"]]
- 00acd844 ["CALL", null, ["callee:00bdb040:8"]]
+ 00acd888 ["INT_ADD", "register:40f0:8", ["const:acd888:8", "const:4:8"]]
+ 00acd888 ["CALL", null, ["callee:00bdb040:8"]]
- 00acd844 bytes eb350494
+ 00acd888 bytes ee350494
- 00acd854 ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 00acd854 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00acd854 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00acd854 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00acd898 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00acd898 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00acd898 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00acd898 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00acd854 bytes 6be11f91
+ 00acd898 bytes 6b212191
- 00acd884 ["INT_ADD", "register:40f0:8", ["const:acd884:8", "const:4:8"]]
- 00acd884 ["CALL", null, ["callee:00418fe0:8"]]
+ 00acd8c8 ["INT_ADD", "register:40f0:8", ["const:acd8c8:8", "const:4:8"]]
+ 00acd8c8 ["CALL", null, ["callee:00418fe0:8"]]
- 00acd884 bytes d72de597
+ 00acd8c8 bytes c62de597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1899bb0b1ccb737d8ed34e51bbf8fa6"></a>

### [`00acd8ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd8ac.md) → [`00acd8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd8f0.md) FUN_00acd8f0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00acd8fc",
      "incomplete_value": false,
      "site": "00acd8fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acd8b8",
      "incomplete_value": false,
      "site": "00acd8b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "00acd8fc",
      "DATA",
      [
        "storage",
        "00c0f7f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acd8fc",
      "DATA",
      [
        "storage",
        "00c0f848",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acd8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd8ac.md#insn-00acd8b4)
- 新版 [`00acd8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd8f0.md#insn-00acd8f8)

~~~diff
- 00acd8b4 ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 00acd8b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00acd8b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00acd8b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00acd8f8 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00acd8f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00acd8f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00acd8f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00acd8b4 bytes 29e11f91
+ 00acd8f8 bytes 29212191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a88035faabbcc453f594948f2636c3a2"></a>

### [`00acd96c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd96c.md) → [`00acd9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd9b0.md) _INIT_252

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 76.44% / 新版 76.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 11件, `store_value` 8件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00acd9ec",
      "incomplete_value": true,
      "site": "00acda08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acd9a8",
      "incomplete_value": true,
      "site": "00acd9c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acda10",
      "incomplete_value": true,
      "site": "00acda2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acd9cc",
      "incomplete_value": true,
      "site": "00acd9e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acda30",
      "incomplete_value": true,
      "site": "00acda4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acd9ec",
      "incomplete_value": true,
      "site": "00acda08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00acd9ec",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00acda10",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00acda30",
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
      "00acd9ec",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00acda10",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00acda30",
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

- 旧版 [`00acd9a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd96c.md#insn-00acd9a4) · [`00acdacc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd96c.md#insn-00acdacc) · [`00acdb84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd96c.md#insn-00acdb84)
- 新版 [`00acd9e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd9b0.md#insn-00acd9e8) · [`00acdb10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd9b0.md#insn-00acdb10) · [`00acdbc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd9b0.md#insn-00acdbc8)

~~~diff
- 00acd9a4 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00acd9a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00acd9a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00acd9a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00acd9e8 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00acd9e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00acd9e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00acd9e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00acd9a4 bytes 29750b91
+ 00acd9e8 bytes 29dd0d91
- 00acdacc ["INT_ADD", "register:40f0:8", ["const:acdacc:8", "const:4:8"]]
- 00acdacc ["CALL", null, ["callee:00418cb8:8"]]
+ 00acdb10 ["INT_ADD", "register:40f0:8", ["const:acdb10:8", "const:4:8"]]
+ 00acdb10 ["CALL", null, ["callee:00418cb8:8"]]
- 00acdacc bytes 7b2ce597
+ 00acdb10 bytes 6a2ce597
- 00acdb84 ["INT_ADD", "register:40f0:8", ["const:acdb84:8", "const:4:8"]]
- 00acdb84 ["CALL", null, ["callee:00bdb060:8"]]
+ 00acdbc8 ["INT_ADD", "register:40f0:8", ["const:acdbc8:8", "const:4:8"]]
+ 00acdbc8 ["CALL", null, ["callee:00bdb060:8"]]
- 00acdb84 bytes 23350494
+ 00acdbc8 bytes 26350494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d97ac59336ad01cf6c8b1e4a2bdb0a0c"></a>

### [`00acdd78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acdd78.md) → [`00acddbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acddbc.md) FUN_00acddbc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00657e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00657/00657e7c.md) · 呼出先 2件 [`00adcc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adcc94.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)
- 新版 呼出元 1件 [`00657e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/00657e7c.md) · 呼出先 2件 [`00adccd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adccd8.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)

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
      "definition_site": "00acddd4",
      "incomplete_value": false,
      "site": "00acdde4",
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
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acdd90",
      "incomplete_value": false,
      "site": "00acdda0",
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
            "const:2b8:8"
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
      "00acdde4",
      "DATA",
      [
        "storage",
        "00bf72b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00acdde4",
      "DATA",
      [
        "storage",
        "00bf7308",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acdd88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acdd78.md#insn-00acdd88) · [`00acdd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acdd78.md#insn-00acdd90) · [`00acdda4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acdd78.md#insn-00acdda4)
- 新版 [`00acddcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acddbc.md#insn-00acddcc) · [`00acddd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acddbc.md#insn-00acddd4) · [`00acdde8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acddbc.md#insn-00acdde8)

~~~diff
- 00acdd88 ["INT_ADD", "register:40f0:8", ["const:acdd88:8", "const:4:8"]]
- 00acdd88 ["CALL", null, ["callee:00adccd8:8"]]
+ 00acddcc ["INT_ADD", "register:40f0:8", ["const:acddcc:8", "const:4:8"]]
+ 00acddcc ["CALL", null, ["callee:00adccd8:8"]]
- 00acdd88 bytes c33b0094
+ 00acddcc bytes c33b0094
- 00acdd90 ["COPY", "tmp:0:8", ["const:2b8:8"]]
- 00acdd90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acdd90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acdd90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acddd4 ["COPY", "tmp:0:8", ["const:308:8"]]
+ 00acddd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acddd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acddd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acdd90 bytes 08e10a91
+ 00acddd4 bytes 08210c91
- 00acdda4 ["INT_ADD", "register:40f0:8", ["const:acdda4:8", "const:4:8"]]
- 00acdda4 ["CALL", null, ["callee:00bdb240:8"]]
+ 00acdde8 ["INT_ADD", "register:40f0:8", ["const:acdde8:8", "const:4:8"]]
+ 00acdde8 ["CALL", null, ["callee:00bdb240:8"]]
- 00acdda4 bytes 13350494
+ 00acdde8 bytes 16350494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a87848de1ed56404ab75898d93b7f130"></a>

### [`00acddbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acddbc.md) → [`00acde00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acde00.md) FUN_00acde00

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`0092e43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0092e/0092e43c.md) [`0093249c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00932/0093249c.md) [`0093c1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0093c/0093c1ac.md) [`00a6731c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a67/00a6731c.md) [`00a68ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a68/00a68ac0.md) · 呼出先 11件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`008321a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00832/008321a8.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 6件 [`0092e43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0092e/0092e43c.md) [`0093249c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00932/0093249c.md) [`0093c1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0093c/0093c1ac.md) [`00a67360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a67/00a67360.md) [`00a68b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a68/00a68b04.md) · 呼出先 11件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`008321a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00832/008321a8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 66.94% / 新版 66.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 35件, `store_destination` 49件, `store_value` 30件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00acde90",
      "incomplete_value": true,
      "site": "00acde90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00acde4c",
      "incomplete_value": true,
      "site": "00acde4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00acdf38",
      "incomplete_value": true,
      "site": "00acdf38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acdef4",
      "incomplete_value": true,
      "site": "00acdef4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff5:8"
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
      "definition_site": "00acdf3c",
      "incomplete_value": true,
      "site": "00acdf3c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00acdef8",
      "incomplete_value": true,
      "site": "00acdef8",
      "value": [
        "LOAD",
        "8",
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
      "00acde60",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00acde80",
      "READ",
      [
        "storage",
        "00292bc8",
        null,
        "string"
      ]
    ],
    [
      "00acdeb4",
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
      "00acde60",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00acde80",
      "READ",
      [
        "storage",
        "00292b3b",
        null,
        "string"
      ]
    ],
    [
      "00acdeb4",
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

- 旧版 [`00ace030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acddbc.md#insn-00ace030) · [`00ace0a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acddbc.md#insn-00ace0a8) · [`00ace230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acddbc.md#insn-00ace230)
- 新版 [`00ace074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acde00.md#insn-00ace074) · [`00ace0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acde00.md#insn-00ace0ec) · [`00ace274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acde00.md#insn-00ace274)

~~~diff
- 00ace030 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00ace030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ace030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ace030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ace074 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00ace074 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ace074 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ace074 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ace030 bytes 08e10091
+ 00ace074 bytes 08e10191
- 00ace0a8 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00ace0a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ace0a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ace0a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ace0ec ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00ace0ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ace0ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ace0ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ace0a8 bytes 08e10091
+ 00ace0ec bytes 08e10191
- 00ace230 ["INT_ADD", "register:40f0:8", ["const:ace230:8", "const:4:8"]]
- 00ace230 ["CALL", null, ["callee:00bd6e90:8"]]
+ 00ace274 ["INT_ADD", "register:40f0:8", ["const:ace274:8", "const:4:8"]]
+ 00ace274 ["CALL", null, ["callee:00bd6e90:8"]]
- 00ace230 bytes 08230494
+ 00ace274 bytes 07230494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59a908459eb591181424eebd04724eaa"></a>

### [`00ace594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ace/00ace594.md) → [`00ace5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ace/00ace5d8.md) FUN_00ace5d8

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 11件 [`008d99b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d9/008d99b0.md) [`0092e43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0092e/0092e43c.md) [`00932074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00932/00932074.md) [`0093249c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00932/0093249c.md) [`00938cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00938/00938cc0.md) · 呼出先 24件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044b660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b660.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md)
- 新版 呼出元 11件 [`008d99b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d9/008d99b0.md) [`0092e43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0092e/0092e43c.md) [`00932074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00932/00932074.md) [`0093249c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00932/0093249c.md) [`00938cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00938/00938cc0.md) · 呼出先 24件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044b660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b660.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.81% / 新版 83.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 36件, `store_destination` 42件, `store_value` 21件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ace67c",
      "incomplete_value": true,
      "site": "00ace67c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ace638",
      "incomplete_value": true,
      "site": "00ace638",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf5:8"
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
      "definition_site": "00ace974",
      "incomplete_value": true,
      "site": "00ace974",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00ace930",
      "incomplete_value": true,
      "site": "00ace930",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ace98c",
      "incomplete_value": true,
      "site": "00ace98c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00ace948",
      "incomplete_value": true,
      "site": "00ace948",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00ace64c",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00ace66c",
      "READ",
      [
        "storage",
        "00294bf5",
        null,
        "string"
      ]
    ],
    [
      "00ace6a0",
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
      "00ace64c",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00ace66c",
      "READ",
      [
        "storage",
        "00294b68",
        null,
        "string"
      ]
    ],
    [
      "00ace6a0",
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

- 旧版 [`00ace98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ace/00ace594.md#insn-00ace98c) · [`00acea8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ace/00ace594.md#insn-00acea8c) · [`00acefec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ace/00ace594.md#insn-00acefec)
- 新版 [`00ace9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ace/00ace5d8.md#insn-00ace9d0) · [`00acead0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ace/00ace5d8.md#insn-00acead0) · [`00acf030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ace/00ace5d8.md#insn-00acf030)

~~~diff
- 00ace98c ["INT_ADD", "register:40f0:8", ["const:ace98c:8", "const:4:8"]]
- 00ace98c ["CALL", null, ["callee:0081f580:8"]]
+ 00ace9d0 ["INT_ADD", "register:40f0:8", ["const:ace9d0:8", "const:4:8"]]
+ 00ace9d0 ["CALL", null, ["callee:0081f580:8"]]
- 00ace98c bytes fd42f597
+ 00ace9d0 bytes ec42f597
- 00acea8c ["COPY", "tmp:0:8", ["const:38:8"]]
- 00acea8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acea8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acea8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acead0 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00acead0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acead0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acead0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acea8c bytes 08e10091
+ 00acead0 bytes 08e10191
- 00acefec ["INT_ADD", "register:40f0:8", ["const:acefec:8", "const:4:8"]]
- 00acefec ["CALL", null, ["callee:0045b734:8"]]
+ 00acf030 ["INT_ADD", "register:40f0:8", ["const:acf030:8", "const:4:8"]]
+ 00acf030 ["CALL", null, ["callee:0045b734:8"]]
- 00acefec bytes d231e697
+ 00acf030 bytes c131e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32d30975bd3bc0cf221f6b4b7c68d2a9"></a>

### [`00acf494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf494.md) → [`00acf4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf4d8.md) _INIT_253

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00acf514",
      "incomplete_value": true,
      "site": "00acf530",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acf4d0",
      "incomplete_value": true,
      "site": "00acf4ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acf538",
      "incomplete_value": true,
      "site": "00acf554",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acf4f4",
      "incomplete_value": true,
      "site": "00acf510",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acf558",
      "incomplete_value": true,
      "site": "00acf574",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acf514",
      "incomplete_value": true,
      "site": "00acf530",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00acf514",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00acf538",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00acf558",
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
      "00acf514",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00acf538",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00acf558",
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

- 旧版 [`00acf4cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf494.md#insn-00acf4cc) · [`00acf5f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf494.md#insn-00acf5f4) · [`00acf6c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf494.md#insn-00acf6c8)
- 新版 [`00acf510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf4d8.md#insn-00acf510) · [`00acf638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf4d8.md#insn-00acf638) · [`00acf70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf4d8.md#insn-00acf70c)

~~~diff
- 00acf4cc ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00acf4cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00acf4cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00acf4cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00acf510 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00acf510 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00acf510 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00acf510 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00acf4cc bytes 29750b91
+ 00acf510 bytes 29dd0d91
- 00acf5f4 ["INT_ADD", "register:40f0:8", ["const:acf5f4:8", "const:4:8"]]
- 00acf5f4 ["CALL", null, ["callee:00418cb8:8"]]
+ 00acf638 ["INT_ADD", "register:40f0:8", ["const:acf638:8", "const:4:8"]]
+ 00acf638 ["CALL", null, ["callee:00418cb8:8"]]
- 00acf5f4 bytes b125e597
+ 00acf638 bytes a025e597
- 00acf6c8 ["INT_ADD", "register:40f0:8", ["const:acf6c8:8", "const:4:8"]]
- 00acf6c8 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00acf70c ["INT_ADD", "register:40f0:8", ["const:acf70c:8", "const:4:8"]]
+ 00acf70c ["CALL", null, ["callee:00bdafe0:8"]]
- 00acf6c8 bytes 322e0494
+ 00acf70c bytes 352e0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c3c8c2a0d316a92a26e93c1f94289c2"></a>

### [`00acf824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf824.md) → [`00acf868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf868.md) FUN_00acf868

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`009a9ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a9/009a9ce0.md) [`00a37688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37688.md) · 呼出先 1件 [`00adc01c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc01c.md)
- 新版 呼出元 2件 [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) [`00a376cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a37/00a376cc.md) · 呼出先 1件 [`00adc060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc060.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00acf8a4",
      "incomplete_value": false,
      "site": "00acf8a4",
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
      "definition_site": "00acf860",
      "incomplete_value": false,
      "site": "00acf860",
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
      "00acf8a4",
      "WRITE",
      [
        "storage",
        "00c23f64",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00acf8a4",
      "WRITE",
      [
        "storage",
        "00c23fb4",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acf860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf824.md#insn-00acf860) · [`00acf854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf824.md#insn-00acf854)
- 新版 [`00acf8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf868.md#insn-00acf8a4) · [`00acf898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf868.md#insn-00acf898)

~~~diff
- 00acf860 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00acf860 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:f64:8"]]
- 00acf860 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00acf8a4 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00acf8a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:fb4:8"]]
+ 00acf8a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00acf860 bytes 09913d39
+ 00acf8a4 bytes 09d13e39
- 00acf854 ["INT_ADD", "register:40f0:8", ["const:acf854:8", "const:4:8"]]
- 00acf854 ["CALL", null, ["callee:00adc060:8"]]
+ 00acf898 ["INT_ADD", "register:40f0:8", ["const:acf898:8", "const:4:8"]]
+ 00acf898 ["CALL", null, ["callee:00adc060:8"]]
- 00acf854 bytes f2310094
+ 00acf898 bytes f2310094
~~~


<a id="compare-a3bacd057e296de2f59280e0ca79ebc6"></a>

### [`00acf86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf86c.md) → [`00acf8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf8b0.md) FUN_00acf8b0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00733374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00733/00733374.md) · 呼出先 2件 [`00adc01c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc01c.md) [`00adc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc050.md)
- 新版 呼出元 1件 [`00733374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00733/00733374.md) · 呼出先 2件 [`00adc060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc060.md) [`00adc094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc094.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00acf900",
      "incomplete_value": false,
      "site": "00acf900",
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
      "definition_site": "00acf8bc",
      "incomplete_value": false,
      "site": "00acf8bc",
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
      "00acf900",
      "WRITE",
      [
        "storage",
        "00c23f64",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00acf900",
      "WRITE",
      [
        "storage",
        "00c23fb4",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acf8bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf86c.md#insn-00acf8bc) · [`00acf880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf86c.md#insn-00acf880) · [`00acf8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf86c.md#insn-00acf8b0)
- 新版 [`00acf900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf8b0.md#insn-00acf900) · [`00acf8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf8b0.md#insn-00acf8c4) · [`00acf8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf8b0.md#insn-00acf8f4)

~~~diff
- 00acf8bc ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00acf8bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:f64:8"]]
- 00acf8bc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00acf900 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00acf900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:fb4:8"]]
+ 00acf900 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00acf8bc bytes 09913d39
+ 00acf900 bytes 09d13e39
- 00acf880 ["INT_ADD", "register:40f0:8", ["const:acf880:8", "const:4:8"]]
- 00acf880 ["CALL", null, ["callee:00adc094:8"]]
+ 00acf8c4 ["INT_ADD", "register:40f0:8", ["const:acf8c4:8", "const:4:8"]]
+ 00acf8c4 ["CALL", null, ["callee:00adc094:8"]]
- 00acf880 bytes f4310094
+ 00acf8c4 bytes f4310094
- 00acf8b0 ["INT_ADD", "register:40f0:8", ["const:acf8b0:8", "const:4:8"]]
- 00acf8b0 ["CALL", null, ["callee:00adc060:8"]]
+ 00acf8f4 ["INT_ADD", "register:40f0:8", ["const:acf8f4:8", "const:4:8"]]
+ 00acf8f4 ["CALL", null, ["callee:00adc060:8"]]
- 00acf8b0 bytes db310094
+ 00acf8f4 bytes db310094
~~~


<a id="compare-fe33b4d7cfd29ee4a3c3faba18a97e3b"></a>

### [`00acf8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf8f0.md) → [`00acf934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf934.md) FUN_00acf934

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00733374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00733/00733374.md) · 呼出先 2件 [`00adc01c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc01c.md) [`00adc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc050.md)
- 新版 呼出元 1件 [`00733374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00733/00733374.md) · 呼出先 2件 [`00adc060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc060.md) [`00adc094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc094.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00acf990",
      "incomplete_value": false,
      "site": "00acf990",
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
      "definition_site": "00acf94c",
      "incomplete_value": false,
      "site": "00acf94c",
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
      "00acf990",
      "WRITE",
      [
        "storage",
        "00c23f64",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00acf990",
      "WRITE",
      [
        "storage",
        "00c23fb4",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acf94c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf8f0.md#insn-00acf94c) · [`00acf904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf8f0.md#insn-00acf904) · [`00acf940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf8f0.md#insn-00acf940)
- 新版 [`00acf990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf934.md#insn-00acf990) · [`00acf948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf934.md#insn-00acf948) · [`00acf984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf934.md#insn-00acf984)

~~~diff
- 00acf94c ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00acf94c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:f64:8"]]
- 00acf94c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00acf990 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00acf990 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:fb4:8"]]
+ 00acf990 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00acf94c bytes 09913d39
+ 00acf990 bytes 09d13e39
- 00acf904 ["INT_ADD", "register:40f0:8", ["const:acf904:8", "const:4:8"]]
- 00acf904 ["CALL", null, ["callee:00adc094:8"]]
+ 00acf948 ["INT_ADD", "register:40f0:8", ["const:acf948:8", "const:4:8"]]
+ 00acf948 ["CALL", null, ["callee:00adc094:8"]]
- 00acf904 bytes d3310094
+ 00acf948 bytes d3310094
- 00acf940 ["INT_ADD", "register:40f0:8", ["const:acf940:8", "const:4:8"]]
- 00acf940 ["CALL", null, ["callee:00adc060:8"]]
+ 00acf984 ["INT_ADD", "register:40f0:8", ["const:acf984:8", "const:4:8"]]
+ 00acf984 ["CALL", null, ["callee:00adc060:8"]]
- 00acf940 bytes b7310094
+ 00acf984 bytes b7310094
~~~


<a id="compare-9e07f1259b76ef1ba9530c48325b7c4a"></a>

### [`00acf984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf984.md) → [`00acf9c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf9c8.md) FUN_00acf9c8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 4件 [`0072f020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072f/0072f020.md) [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) [`00960f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00960/00960f9c.md) [`009a9ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a9/009a9ce0.md) · 呼出先 2件 [`00adc01c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc01c.md) [`00adc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc050.md)
- 新版 呼出元 4件 [`0072f020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072f/0072f020.md) [`00957f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00957/00957f9c.md) [`00960f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00960/00960f9c.md) [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 2件 [`00adc060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc060.md) [`00adc094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc094.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00acfa38",
      "incomplete_value": false,
      "site": "00acfa38",
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
      "definition_site": "00acf9f4",
      "incomplete_value": false,
      "site": "00acf9f4",
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
      "00acfa38",
      "WRITE",
      [
        "storage",
        "00c23f64",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00acfa38",
      "WRITE",
      [
        "storage",
        "00c23fb4",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acf9f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf984.md#insn-00acf9f4) · [`00acf99c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf984.md#insn-00acf99c) · [`00acf9bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf984.md#insn-00acf9bc)
- 新版 [`00acfa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf9c8.md#insn-00acfa38) · [`00acf9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf9c8.md#insn-00acf9e0) · [`00acfa00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf9c8.md#insn-00acfa00)

~~~diff
- 00acf9f4 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00acf9f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:f64:8"]]
- 00acf9f4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00acfa38 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00acfa38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:fb4:8"]]
+ 00acfa38 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00acf9f4 bytes 09913d39
+ 00acfa38 bytes 09d13e39
- 00acf99c ["INT_ADD", "register:40f0:8", ["const:acf99c:8", "const:4:8"]]
- 00acf99c ["CALL", null, ["callee:00adc094:8"]]
+ 00acf9e0 ["INT_ADD", "register:40f0:8", ["const:acf9e0:8", "const:4:8"]]
+ 00acf9e0 ["CALL", null, ["callee:00adc094:8"]]
- 00acf99c bytes ad310094
+ 00acf9e0 bytes ad310094
- 00acf9bc ["INT_ADD", "register:40f0:8", ["const:acf9bc:8", "const:4:8"]]
- 00acf9bc ["CALL", null, ["callee:00adc094:8"]]
+ 00acfa00 ["INT_ADD", "register:40f0:8", ["const:acfa00:8", "const:4:8"]]
+ 00acfa00 ["CALL", null, ["callee:00adc094:8"]]
- 00acf9bc bytes a5310094
+ 00acfa00 bytes a5310094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1292b421a0502cc6c3359b8eed828515"></a>

### [`00acfa08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfa08.md) → [`00acfa4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfa4c.md) FUN_00acfa4c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 6件 [`006e34b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e3/006e34b0.md) [`0072f020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072f/0072f020.md) [`0092bc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0092b/0092bc08.md) [`0092d380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0092d/0092d380.md) [`009a9ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a9/009a9ce0.md) · 呼出先 2件 [`00adc01c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc01c.md) [`00adc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc050.md)
- 新版 呼出元 6件 [`006e34b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e3/006e34b0.md) [`0072f020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072f/0072f020.md) [`0092bc08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0092b/0092bc08.md) [`0092d380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0092d/0092d380.md) [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 2件 [`00adc060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc060.md) [`00adc094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc094.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00acfac4",
      "incomplete_value": false,
      "site": "00acfac4",
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
      "definition_site": "00acfa80",
      "incomplete_value": false,
      "site": "00acfa80",
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
    "ordinal": 6,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00acfac4",
      "WRITE",
      [
        "storage",
        "00c23f64",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00acfac4",
      "WRITE",
      [
        "storage",
        "00c23fb4",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acfa3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfa08.md#insn-00acfa3c) · [`00acfa80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfa08.md#insn-00acfa80) · [`00acfa20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfa08.md#insn-00acfa20)
- 新版 [`00acfa80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfa4c.md#insn-00acfa80) · [`00acfac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfa4c.md#insn-00acfac4) · [`00acfa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfa4c.md#insn-00acfa64)

~~~diff
- 00acfa3c ["INT_ADD", "register:40f0:8", ["const:acfa3c:8", "const:4:8"]]
- 00acfa3c ["CALL", null, ["callee:00adc094:8"]]
+ 00acfa80 ["INT_ADD", "register:40f0:8", ["const:acfa80:8", "const:4:8"]]
+ 00acfa80 ["CALL", null, ["callee:00adc094:8"]]
- 00acfa3c bytes 85310094
+ 00acfa80 bytes 85310094
- 00acfa80 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00acfa80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:f64:8"]]
- 00acfa80 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00acfac4 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00acfac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:fb4:8"]]
+ 00acfac4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00acfa80 bytes 09913d39
+ 00acfac4 bytes 09d13e39
- 00acfa20 ["INT_ADD", "register:40f0:8", ["const:acfa20:8", "const:4:8"]]
- 00acfa20 ["CALL", null, ["callee:00adc094:8"]]
+ 00acfa64 ["INT_ADD", "register:40f0:8", ["const:acfa64:8", "const:4:8"]]
+ 00acfa64 ["CALL", null, ["callee:00adc094:8"]]
- 00acfa20 bytes 8c310094
+ 00acfa64 bytes 8c310094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86ed62aa04eea384f4746d21f6bcd382"></a>

### [`00acfae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfae8.md) → [`00acfb2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfb2c.md) FUN_00acfb2c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00453c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00453/00453c78.md) · 呼出先 15件 [`0044abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abe4.md) [`00574f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574f30.md) [`00574f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574f70.md) [`00728090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/00728090.md) [`0073a038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a038.md)
- 新版 呼出元 1件 [`00453c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/00453c78.md) · 呼出先 15件 [`0044abe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abe4.md) [`00574f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574f30.md) [`00574f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574f70.md) [`00728090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/00728090.md) [`0073a038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a038.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00acfbf0",
      "incomplete_value": true,
      "site": "00acfc00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f21:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acfbac",
      "incomplete_value": true,
      "site": "00acfbbc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e96:8"
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
      "definition_site": "00acfbf0",
      "incomplete_value": true,
      "site": "00acfc00",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00acfbac",
      "incomplete_value": true,
      "site": "00acfbbc",
      "value": [
        "LOAD",
        "16",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00acfc04",
      "incomplete_value": true,
      "site": "00acfc0c",
      "value": [
        "LOAD",
        "16",
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
                "const:1b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acfbc0",
      "incomplete_value": true,
      "site": "00acfbc8",
      "value": [
        "LOAD",
        "16",
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
                "const:1b:8"
              ]
            ]
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
      "00acfb70",
      "PARAM",
      [
        "storage",
        "002a8b55",
        null,
        "string"
      ]
    ],
    [
      "00acfbf0",
      "READ",
      [
        "storage",
        "0029fe96",
        null,
        "string"
      ]
    ],
    [
      "00acfbf0",
      "READ",
      [
        "storage",
        "0029fea6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00acfb70",
      "PARAM",
      [
        "storage",
        "002a8bef",
        null,
        "string"
      ]
    ],
    [
      "00acfbf0",
      "READ",
      [
        "storage",
        "0029ff21",
        null,
        "string"
      ]
    ],
    [
      "00acfbf0",
      "READ",
      [
        "storage",
        "0029ff31",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acfb38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfae8.md#insn-00acfb38) · [`00acfb84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfae8.md#insn-00acfb84) · [`00acfc8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfae8.md#insn-00acfc8c)
- 新版 [`00acfb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfb2c.md#insn-00acfb7c) · [`00acfbc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfb2c.md#insn-00acfbc8) · [`00acfcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfb2c.md#insn-00acfcd0)

~~~diff
- 00acfb38 ["INT_ADD", "register:40f0:8", ["const:acfb38:8", "const:4:8"]]
- 00acfb38 ["CALL", null, ["callee:00bdb110:8"]]
+ 00acfb7c ["INT_ADD", "register:40f0:8", ["const:acfb7c:8", "const:4:8"]]
+ 00acfb7c ["CALL", null, ["callee:00bdb110:8"]]
- 00acfb38 bytes 622d0494
+ 00acfb7c bytes 652d0494
- 00acfb84 ["INT_ADD", "register:40f0:8", ["const:acfb84:8", "const:4:8"]]
- 00acfb84 ["CALL", null, ["callee:00bdb060:8"]]
+ 00acfbc8 ["INT_ADD", "register:40f0:8", ["const:acfbc8:8", "const:4:8"]]
+ 00acfbc8 ["CALL", null, ["callee:00bdb060:8"]]
- 00acfb84 bytes 232d0494
+ 00acfbc8 bytes 262d0494
- 00acfc8c ["INT_ADD", "register:40f0:8", ["const:acfc8c:8", "const:4:8"]]
- 00acfc8c ["CALL", null, ["callee:00bdb110:8"]]
+ 00acfcd0 ["INT_ADD", "register:40f0:8", ["const:acfcd0:8", "const:4:8"]]
+ 00acfcd0 ["CALL", null, ["callee:00bdb110:8"]]
- 00acfc8c bytes 0d2d0494
+ 00acfcd0 bytes 102d0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31262cb2425750bb2f8861eeacf0963d"></a>

### [`00ad021c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad021c.md) → [`00ad0260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad0/00ad0260.md) FUN_00ad0260

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0042fd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fd7c.md) [`004349a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/004349a0.md) [`00435358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/00435358.md) · 呼出先 11件 [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md) [`00436bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436bf8.md) [`00438f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438f20.md) [`00574744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574744.md) [`0057474c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/0057474c.md)
- 新版 呼出元 3件 [`0042fd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md) [`004349a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/004349a0.md) [`00435358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/00435358.md) · 呼出先 11件 [`0042e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md) [`00436bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436bf8.md) [`00438f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438f20.md) [`00574744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574744.md) [`0057474c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057474c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.55% / 新版 97.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad02bc",
      "incomplete_value": false,
      "site": "00ad02d0",
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
      "definition_site": "00ad0278",
      "incomplete_value": false,
      "site": "00ad028c",
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
      "definition_site": "00ad03c8",
      "incomplete_value": true,
      "site": "00ad03c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c0a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad0384",
      "incomplete_value": true,
      "site": "00ad0384",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c97:8"
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
      "00ad02d0",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ],
    [
      "00ad02f8",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ],
    [
      "00ad032c",
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
      "00ad02d0",
      "DATA",
      [
        "storage",
        "00be6b20",
        null,
        "pointer"
      ]
    ],
    [
      "00ad02f8",
      "DATA",
      [
        "storage",
        "00be6b20",
        null,
        "pointer"
      ]
    ],
    [
      "00ad032c",
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

- 旧版 [`00ad0340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad021c.md#insn-00ad0340) · [`00ad024c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad021c.md#insn-00ad024c) · [`00ad0278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad021c.md#insn-00ad0278)
- 新版 [`00ad0384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad0/00ad0260.md#insn-00ad0384) · [`00ad0290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad0/00ad0260.md#insn-00ad0290) · [`00ad02bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad0/00ad0260.md#insn-00ad02bc)

~~~diff
- 00ad0340 ["INT_ADD", "register:40f0:8", ["const:ad0340:8", "const:4:8"]]
- 00ad0340 ["CALL", null, ["callee:0042e8c4:8"]]
+ 00ad0384 ["INT_ADD", "register:40f0:8", ["const:ad0384:8", "const:4:8"]]
+ 00ad0384 ["CALL", null, ["callee:0042e8c4:8"]]
- 00ad0340 bytes 6179e597
+ 00ad0384 bytes 5079e597
- 00ad024c ["INT_ADD", "register:40f0:8", ["const:ad024c:8", "const:4:8"]]
- 00ad024c ["CALL", null, ["callee:00bdb040:8"]]
+ 00ad0290 ["INT_ADD", "register:40f0:8", ["const:ad0290:8", "const:4:8"]]
+ 00ad0290 ["CALL", null, ["callee:00bdb040:8"]]
- 00ad024c bytes 692b0494
+ 00ad0290 bytes 6c2b0494
- 00ad0278 ["COPY", "tmp:0:8", ["const:ad0:8"]]
- 00ad0278 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 00ad0278 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 00ad0278 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 00ad02bc ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 00ad02bc ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 00ad02bc ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 00ad02bc ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 00ad0278 bytes 18432b91
+ 00ad02bc bytes 18832c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98484e19f575f0910ab26699c9db001d"></a>

### [`00ad08f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad08f4.md) → [`00ad0938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad0/00ad0938.md) FUN_00ad0938

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00acfe1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfe1c.md) [`00ad08f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad08f4.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00acfe60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfe60.md) [`00ad0938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad0/00ad0938.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.66% / 新版 98.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ad0aa8",
      "incomplete_value": false,
      "site": "00ad0ab0",
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
      "definition_site": "00ad0a64",
      "incomplete_value": false,
      "site": "00ad0a6c",
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
      "definition_site": "00ad0b68",
      "incomplete_value": false,
      "site": "00ad0b70",
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
      "definition_site": "00ad0b24",
      "incomplete_value": false,
      "site": "00ad0b2c",
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
      "definition_site": "00ad0b84",
      "incomplete_value": false,
      "site": "00ad0b90",
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
      "definition_site": "00ad0b40",
      "incomplete_value": false,
      "site": "00ad0b4c",
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
      "00ad0aa8",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00ad0b68",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00ad0b84",
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
      "00ad0aa8",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00ad0b68",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "00ad0b84",
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

- 旧版 [`00ad0a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad08f4.md#insn-00ad0a6c) · [`00ad0b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad08f4.md#insn-00ad0b2c) · [`00ad0b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad08f4.md#insn-00ad0b4c)
- 新版 [`00ad0ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad0/00ad0938.md#insn-00ad0ab0) · [`00ad0b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad0/00ad0938.md#insn-00ad0b70) · [`00ad0b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad0/00ad0938.md#insn-00ad0b90)

~~~diff
- 00ad0a6c ["INT_ADD", "register:40f0:8", ["const:ad0a6c:8", "const:4:8"]]
- 00ad0a6c ["CALL", null, ["callee:0041f354:8"]]
+ 00ad0ab0 ["INT_ADD", "register:40f0:8", ["const:ad0ab0:8", "const:4:8"]]
+ 00ad0ab0 ["CALL", null, ["callee:0041f354:8"]]
- 00ad0a6c bytes 3a3ae597
+ 00ad0ab0 bytes 293ae597
- 00ad0b2c ["INT_ADD", "register:40f0:8", ["const:ad0b2c:8", "const:4:8"]]
- 00ad0b2c ["CALL", null, ["callee:0041f354:8"]]
+ 00ad0b70 ["INT_ADD", "register:40f0:8", ["const:ad0b70:8", "const:4:8"]]
+ 00ad0b70 ["CALL", null, ["callee:0041f354:8"]]
- 00ad0b2c bytes 0a3ae597
+ 00ad0b70 bytes f939e597
- 00ad0b4c ["INT_ADD", "register:40f0:8", ["const:ad0b4c:8", "const:4:8"]]
- 00ad0b4c ["CALL", null, ["callee:0041fcb4:8"]]
+ 00ad0b90 ["INT_ADD", "register:40f0:8", ["const:ad0b90:8", "const:4:8"]]
+ 00ad0b90 ["CALL", null, ["callee:0041fcb4:8"]]
- 00ad0b4c bytes 5a3ce597
+ 00ad0b90 bytes 493ce597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f34379fd5fb54a17af0b5ffc5a0edd7"></a>

### [`00ad11f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad11f4.md) → [`00ad1238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad1/00ad1238.md) FUN_00ad1238

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00ad08f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad08f4.md) [`00ad11f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad11f4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00ad0938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad0/00ad0938.md) [`00ad1238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad1/00ad1238.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ad138c",
      "incomplete_value": false,
      "site": "00ad1394",
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
      "definition_site": "00ad1348",
      "incomplete_value": false,
      "site": "00ad1350",
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
      "definition_site": "00ad13b0",
      "incomplete_value": false,
      "site": "00ad13bc",
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
      "definition_site": "00ad136c",
      "incomplete_value": false,
      "site": "00ad1378",
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
      "definition_site": "00ad14e4",
      "incomplete_value": false,
      "site": "00ad14ec",
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
      "definition_site": "00ad14a0",
      "incomplete_value": false,
      "site": "00ad14a8",
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
      "00ad138c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00ad13b0",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "00ad14e4",
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
      "00ad138c",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00ad13b0",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00ad14e4",
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

- 旧版 [`00ad1350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad11f4.md#insn-00ad1350) · [`00ad1378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad11f4.md#insn-00ad1378) · [`00ad14a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad11f4.md#insn-00ad14a8)
- 新版 [`00ad1394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad1/00ad1238.md#insn-00ad1394) · [`00ad13bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad1/00ad1238.md#insn-00ad13bc) · [`00ad14ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad1/00ad1238.md#insn-00ad14ec)

~~~diff
- 00ad1350 ["INT_ADD", "register:40f0:8", ["const:ad1350:8", "const:4:8"]]
- 00ad1350 ["CALL", null, ["callee:0041f354:8"]]
+ 00ad1394 ["INT_ADD", "register:40f0:8", ["const:ad1394:8", "const:4:8"]]
+ 00ad1394 ["CALL", null, ["callee:0041f354:8"]]
- 00ad1350 bytes 0138e597
+ 00ad1394 bytes f037e597
- 00ad1378 ["INT_ADD", "register:40f0:8", ["const:ad1378:8", "const:4:8"]]
- 00ad1378 ["CALL", null, ["callee:0041fcb4:8"]]
+ 00ad13bc ["INT_ADD", "register:40f0:8", ["const:ad13bc:8", "const:4:8"]]
+ 00ad13bc ["CALL", null, ["callee:0041fcb4:8"]]
- 00ad1378 bytes 4f3ae597
+ 00ad13bc bytes 3e3ae597
- 00ad14a8 ["INT_ADD", "register:40f0:8", ["const:ad14a8:8", "const:4:8"]]
- 00ad14a8 ["CALL", null, ["callee:0041f354:8"]]
+ 00ad14ec ["INT_ADD", "register:40f0:8", ["const:ad14ec:8", "const:4:8"]]
+ 00ad14ec ["CALL", null, ["callee:0041f354:8"]]
- 00ad14a8 bytes ab37e597
+ 00ad14ec bytes 9a37e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c21c14b74692c821f990ca7dd4c2ff33"></a>

### [`00ad1c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad1c34.md) → [`00ad1c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad1/00ad1c78.md) FUN_00ad1c78

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00ad19f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad19f4.md) [`00ad1c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad1c34.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00ad1a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad1/00ad1a38.md) [`00ad1c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad1/00ad1c78.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.08% / 新版 99.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ad1dd8",
      "incomplete_value": false,
      "site": "00ad1de0",
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
      "definition_site": "00ad1d94",
      "incomplete_value": false,
      "site": "00ad1d9c",
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
      "definition_site": "00ad1dfc",
      "incomplete_value": false,
      "site": "00ad1e08",
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
      "definition_site": "00ad1db8",
      "incomplete_value": false,
      "site": "00ad1dc4",
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
      "definition_site": "00ad1f38",
      "incomplete_value": false,
      "site": "00ad1f40",
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
      "definition_site": "00ad1ef4",
      "incomplete_value": false,
      "site": "00ad1efc",
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
      "00ad1dd8",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00ad1dfc",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "00ad1f38",
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
      "00ad1dd8",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00ad1dfc",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00ad1f38",
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

- 旧版 [`00ad1d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad1c34.md#insn-00ad1d9c) · [`00ad1dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad1c34.md#insn-00ad1dc4) · [`00ad1efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad1c34.md#insn-00ad1efc)
- 新版 [`00ad1de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad1/00ad1c78.md#insn-00ad1de0) · [`00ad1e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad1/00ad1c78.md#insn-00ad1e08) · [`00ad1f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad1/00ad1c78.md#insn-00ad1f40)

~~~diff
- 00ad1d9c ["INT_ADD", "register:40f0:8", ["const:ad1d9c:8", "const:4:8"]]
- 00ad1d9c ["CALL", null, ["callee:0041f354:8"]]
+ 00ad1de0 ["INT_ADD", "register:40f0:8", ["const:ad1de0:8", "const:4:8"]]
+ 00ad1de0 ["CALL", null, ["callee:0041f354:8"]]
- 00ad1d9c bytes 6e35e597
+ 00ad1de0 bytes 5d35e597
- 00ad1dc4 ["INT_ADD", "register:40f0:8", ["const:ad1dc4:8", "const:4:8"]]
- 00ad1dc4 ["CALL", null, ["callee:0041fcb4:8"]]
+ 00ad1e08 ["INT_ADD", "register:40f0:8", ["const:ad1e08:8", "const:4:8"]]
+ 00ad1e08 ["CALL", null, ["callee:0041fcb4:8"]]
- 00ad1dc4 bytes bc37e597
+ 00ad1e08 bytes ab37e597
- 00ad1efc ["INT_ADD", "register:40f0:8", ["const:ad1efc:8", "const:4:8"]]
- 00ad1efc ["CALL", null, ["callee:0041f354:8"]]
+ 00ad1f40 ["INT_ADD", "register:40f0:8", ["const:ad1f40:8", "const:4:8"]]
+ 00ad1f40 ["CALL", null, ["callee:0041f354:8"]]
- 00ad1efc bytes 1635e597
+ 00ad1f40 bytes 0535e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a17be3fec50f97c64bbd4bf381a3c706"></a>

### [`00ad2b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad2/00ad2b0c.md) → [`00ad2b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad2/00ad2b50.md) _INIT_254

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.09% / 新版 92.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad2b8c",
      "incomplete_value": true,
      "site": "00ad2ba8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad2b48",
      "incomplete_value": true,
      "site": "00ad2b64",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ad2b8c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00ad2bb0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00ad2bd0",
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
      "00ad2b8c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00ad2bb0",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00ad2bd0",
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

- 旧版 [`00ad2b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad2/00ad2b0c.md#insn-00ad2b38) · [`00ad2b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad2/00ad2b0c.md#insn-00ad2b40) · [`00ad2b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad2/00ad2b0c.md#insn-00ad2b44)
- 新版 [`00ad2b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad2/00ad2b50.md#insn-00ad2b7c) · [`00ad2b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad2/00ad2b50.md#insn-00ad2b88)

~~~diff
- 00ad2b38 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 00ad2b38 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00ad2b38 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00ad2b38 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00ad2b7c ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 00ad2b7c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00ad2b7c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00ad2b7c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00ad2b38 bytes 73022f91
+ 00ad2b7c bytes 73023091
- 00ad2b40 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00ad2b40 bytes a9beffb0
- 00ad2b44 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00ad2b44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ad2b44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ad2b44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ad2b88 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00ad2b88 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad2b88 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad2b88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ad2b44 bytes 29750b91
+ 00ad2b88 bytes 29dd0d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0234e71664a9f66bc8698adc679a7af0"></a>

### [`00ad2e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad2/00ad2e9c.md) → [`00ad2ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad2/00ad2ee0.md) _INIT_255

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00ad2f1c",
      "incomplete_value": true,
      "site": "00ad2f38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad2ed8",
      "incomplete_value": true,
      "site": "00ad2ef4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad2f40",
      "incomplete_value": true,
      "site": "00ad2f5c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad2efc",
      "incomplete_value": true,
      "site": "00ad2f18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad2f60",
      "incomplete_value": true,
      "site": "00ad2f7c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad2f1c",
      "incomplete_value": true,
      "site": "00ad2f38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00ad2f1c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00ad2f40",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00ad2f60",
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
      "00ad2f1c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00ad2f40",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00ad2f60",
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

- 旧版 [`00ad2ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad2/00ad2e9c.md#insn-00ad2ed4) · [`00ad30d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad2/00ad2e9c.md#insn-00ad30d0) · [`00ad2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad2/00ad2e9c.md#insn-00ad2ec8)
- 新版 [`00ad2f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad2/00ad2ee0.md#insn-00ad2f18) · [`00ad3114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad2/00ad2ee0.md#insn-00ad3114) · [`00ad2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad2/00ad2ee0.md#insn-00ad2f0c)

~~~diff
- 00ad2ed4 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00ad2ed4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ad2ed4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ad2ed4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ad2f18 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00ad2f18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad2f18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad2f18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ad2ed4 bytes 29750b91
+ 00ad2f18 bytes 29dd0d91
- 00ad30d0 ["INT_ADD", "register:40f0:8", ["const:ad30d0:8", "const:4:8"]]
- 00ad30d0 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00ad3114 ["INT_ADD", "register:40f0:8", ["const:ad3114:8", "const:4:8"]]
+ 00ad3114 ["CALL", null, ["callee:00bdafe0:8"]]
- 00ad30d0 bytes b01f0494
+ 00ad3114 bytes b31f0494
- 00ad2ec8 ["COPY", "tmp:0:8", ["const:bd8:8"]]
- 00ad2ec8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00ad2ec8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00ad2ec8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00ad2f0c ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 00ad2f0c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00ad2f0c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00ad2f0c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00ad2ec8 bytes 73622f91
+ 00ad2f0c bytes 73623091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c843681df9f272fbe89dbba21072328a"></a>

### [`00ad33fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad33fc.md) → [`00ad3440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3440.md) FUN_00ad3440

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00a4f438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4f/00a4f438.md) [`00a4fd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4f/00a4fd14.md) · 呼出先 12件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 2件 [`00a4f47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4f47c.md) [`00a4fd58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4fd58.md) · 呼出先 12件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.83% / 新版 90.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad3498",
      "incomplete_value": true,
      "site": "00ad34a8",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:200:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad3454",
      "incomplete_value": true,
      "site": "00ad3464",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:28d:8"
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
      "definition_site": "00ad34c0",
      "incomplete_value": true,
      "site": "00ad34d0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00ad347c",
      "incomplete_value": true,
      "site": "00ad348c",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad34c0",
      "incomplete_value": true,
      "site": "00ad34d0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00ad347c",
      "incomplete_value": true,
      "site": "00ad348c",
      "value": [
        "LOAD",
        "16",
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
      "00ad3498",
      "READ",
      [
        "storage",
        "0029528d",
        null,
        "string"
      ]
    ],
    [
      "00ad34c0",
      "READ",
      [
        "storage",
        "002a2c6d",
        null,
        "string"
      ]
    ],
    [
      "00ad34c0",
      "READ",
      [
        "storage",
        "002a2c7d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ad3498",
      "READ",
      [
        "storage",
        "00295200",
        null,
        "string"
      ]
    ],
    [
      "00ad34c0",
      "READ",
      [
        "storage",
        "002a2cf8",
        null,
        "string"
      ]
    ],
    [
      "00ad34c0",
      "READ",
      [
        "storage",
        "002a2d08",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad343c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad33fc.md#insn-00ad343c) · [`00ad3444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad33fc.md#insn-00ad3444) · [`00ad344c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad33fc.md#insn-00ad344c)
- 新版 [`00ad3480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3440.md#insn-00ad3480) · [`00ad3488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3440.md#insn-00ad3488) · [`00ad3490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3440.md#insn-00ad3490)

~~~diff
- 00ad343c ["INT_ADD", "register:40f0:8", ["const:ad343c:8", "const:4:8"]]
- 00ad343c ["CALL", null, ["callee:00565f94:8"]]
+ 00ad3480 ["INT_ADD", "register:40f0:8", ["const:ad3480:8", "const:4:8"]]
+ 00ad3480 ["CALL", null, ["callee:00565f94:8"]]
- 00ad343c bytes d64aea97
+ 00ad3480 bytes c54aea97
- 00ad3444 ["INT_ADD", "register:40f0:8", ["const:ad3444:8", "const:4:8"]]
- 00ad3444 ["CALL", null, ["callee:00566284:8"]]
+ 00ad3488 ["INT_ADD", "register:40f0:8", ["const:ad3488:8", "const:4:8"]]
+ 00ad3488 ["CALL", null, ["callee:00566284:8"]]
- 00ad3444 bytes 904bea97
+ 00ad3488 bytes 7f4bea97
- 00ad344c ["COPY", "tmp:0:8", ["const:28d:8"]]
- 00ad344c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ad344c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ad344c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ad3490 ["COPY", "tmp:0:8", ["const:200:8"]]
+ 00ad3490 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad3490 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad3490 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ad344c bytes 29350a91
+ 00ad3490 bytes 29010891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7c2f59a624357ac87a2492172339aa1"></a>

### [`00ad37a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad37a8.md) → [`00ad37ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad37ec.md) _INIT_256

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.54% / 新版 86.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad3828",
      "incomplete_value": true,
      "site": "00ad3844",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad37e4",
      "incomplete_value": true,
      "site": "00ad3800",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad384c",
      "incomplete_value": true,
      "site": "00ad3868",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad3808",
      "incomplete_value": true,
      "site": "00ad3824",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad38a8",
      "incomplete_value": true,
      "site": "00ad38c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad3864",
      "incomplete_value": true,
      "site": "00ad3880",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00ad3828",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00ad384c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00ad386c",
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
      "00ad3828",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00ad384c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00ad386c",
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

- 旧版 [`00ad37e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad37a8.md#insn-00ad37e0) · [`00ad39e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad37a8.md#insn-00ad39e0) · [`00ad3a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad37a8.md#insn-00ad3a20)
- 新版 [`00ad3824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad37ec.md#insn-00ad3824) · [`00ad3a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad37ec.md#insn-00ad3a24) · [`00ad3a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad37ec.md#insn-00ad3a64)

~~~diff
- 00ad37e0 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00ad37e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ad37e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ad37e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ad3824 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00ad3824 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad3824 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad3824 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ad37e0 bytes 29750b91
+ 00ad3824 bytes 29dd0d91
- 00ad39e0 ["INT_ADD", "register:40f0:8", ["const:ad39e0:8", "const:4:8"]]
- 00ad39e0 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00ad3a24 ["INT_ADD", "register:40f0:8", ["const:ad3a24:8", "const:4:8"]]
+ 00ad3a24 ["CALL", null, ["callee:00bdafe0:8"]]
- 00ad39e0 bytes 6c1d0494
+ 00ad3a24 bytes 6f1d0494
- 00ad3a20 ["INT_ADD", "register:40f0:8", ["const:ad3a20:8", "const:4:8"]]
- 00ad3a20 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00ad3a64 ["INT_ADD", "register:40f0:8", ["const:ad3a64:8", "const:4:8"]]
+ 00ad3a64 ["CALL", null, ["callee:00bdafe0:8"]]
- 00ad3a20 bytes 5c1d0494
+ 00ad3a64 bytes 5f1d0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18bada3aa6e3ac326f7deced3180987c"></a>

### [`00ad3bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3bb8.md) → [`00ad3bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3bfc.md) FUN_00ad3bfc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0041cad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cad8.md) · 呼出先 10件 [`00449b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449b7c.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)
- 新版 呼出元 1件 [`0041cad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cad8.md) · 呼出先 10件 [`00449b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449b7c.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.84% / 新版 87.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad3c80",
      "incomplete_value": true,
      "site": "00ad3c80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e3b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad3c3c",
      "incomplete_value": true,
      "site": "00ad3c3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db0:8"
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
      "definition_site": "00ad3d5c",
      "incomplete_value": true,
      "site": "00ad3d5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e3b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad3d18",
      "incomplete_value": true,
      "site": "00ad3d18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db0:8"
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
      "definition_site": "00ad3d78",
      "incomplete_value": true,
      "site": "00ad3d88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e5b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad3d34",
      "incomplete_value": true,
      "site": "00ad3d44",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dd0:8"
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
      "00ad3c50",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "00ad3c54",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad3c70",
      "READ",
      [
        "storage",
        "002a1db0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ad3c50",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "00ad3c54",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad3c70",
      "READ",
      [
        "storage",
        "002a1e3b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad3c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3bb8.md#insn-00ad3c14) · [`00ad3d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3bb8.md#insn-00ad3d00) · [`00ad3d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3bb8.md#insn-00ad3d88)
- 新版 [`00ad3c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3bfc.md#insn-00ad3c58) · [`00ad3d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3bfc.md#insn-00ad3d44) · [`00ad3dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3bfc.md#insn-00ad3dcc)

~~~diff
- 00ad3c14 ["INT_ADD", "register:40f0:8", ["const:ad3c14:8", "const:4:8"]]
- 00ad3c14 ["CALL", null, ["callee:00449b7c:8"]]
+ 00ad3c58 ["INT_ADD", "register:40f0:8", ["const:ad3c58:8", "const:4:8"]]
+ 00ad3c58 ["CALL", null, ["callee:00449b7c:8"]]
- 00ad3c14 bytes dad7e597
+ 00ad3c58 bytes c9d7e597
- 00ad3d00 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 00ad3d00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ad3d00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ad3d00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ad3d44 ["COPY", "tmp:0:8", ["const:e3b:8"]]
+ 00ad3d44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad3d44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad3d44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ad3d00 bytes 29c13691
+ 00ad3d44 bytes 29ed3891
- 00ad3d88 ["INT_ADD", "register:40f0:8", ["const:ad3d88:8", "const:4:8"]]
- 00ad3d88 ["CALL", null, ["callee:00bdb060:8"]]
+ 00ad3dcc ["INT_ADD", "register:40f0:8", ["const:ad3dcc:8", "const:4:8"]]
+ 00ad3dcc ["CALL", null, ["callee:00bdb060:8"]]
- 00ad3d88 bytes a21c0494
+ 00ad3dcc bytes a51c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8850672d2449b6b2eb4607182a4922c0"></a>

### [`00ad3f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3f6c.md) → [`00ad3fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3fb0.md) _INIT_257

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00ad3fec",
      "incomplete_value": true,
      "site": "00ad4008",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad3fa8",
      "incomplete_value": true,
      "site": "00ad3fc4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad4030",
      "incomplete_value": true,
      "site": "00ad404c",
      "value": [
        "LOAD",
        "16",
        [
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
      "definition_site": "00ad3fec",
      "incomplete_value": true,
      "site": "00ad4008",
      "value": [
        "LOAD",
        "16",
        [
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
      "definition_site": "00ad4050",
      "incomplete_value": true,
      "site": "00ad4068",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad400c",
      "incomplete_value": true,
      "site": "00ad4024",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00ad3fec",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00ad4010",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00ad4030",
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
      "00ad3fec",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00ad4010",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00ad4030",
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

- 旧版 [`00ad41a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3f6c.md#insn-00ad41a0) · [`00ad3f98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3f6c.md#insn-00ad3f98) · [`00ad3fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3f6c.md#insn-00ad3fa0)
- 新版 [`00ad41e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3fb0.md#insn-00ad41e4) · [`00ad3fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3fb0.md#insn-00ad3fdc)

~~~diff
- 00ad41a0 ["INT_ADD", "register:40f0:8", ["const:ad41a0:8", "const:4:8"]]
- 00ad41a0 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00ad41e4 ["INT_ADD", "register:40f0:8", ["const:ad41e4:8", "const:4:8"]]
+ 00ad41e4 ["CALL", null, ["callee:00bdafe0:8"]]
- 00ad41a0 bytes 7c1b0494
+ 00ad41e4 bytes 7f1b0494
- 00ad3f98 ["COPY", "tmp:0:8", ["const:c38:8"]]
- 00ad3f98 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00ad3f98 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00ad3f98 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00ad3fdc ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 00ad3fdc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00ad3fdc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00ad3fdc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00ad3f98 bytes 73e23091
+ 00ad3fdc bytes 73e23191
- 00ad3fa0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00ad3fa0 bytes a9beff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bebb29c1a92915d05adec83972d624a3"></a>

### [`00ad435c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad435c.md) → [`00ad43a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad43a0.md) FUN_00ad43a0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058cfe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058c/0058cfe0.md) · 呼出先 2件 [`00ad48e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad48e8.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0058cfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058cfe0.md) · 呼出先 2件 [`00ad492c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad492c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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
      "definition_site": "00ad4408",
      "incomplete_value": false,
      "site": "00ad4414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad43c4",
      "incomplete_value": false,
      "site": "00ad43d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:c50:8"
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
      "00ad4408",
      "PARAM",
      [
        "storage",
        "0109fc50",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad4408",
      "PARAM",
      [
        "storage",
        "0109fc90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad43d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad435c.md#insn-00ad43d0) · [`00ad4394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad435c.md#insn-00ad4394) · [`00ad43bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad435c.md#insn-00ad43bc)
- 新版 [`00ad4414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad43a0.md#insn-00ad4414) · [`00ad43d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad43a0.md#insn-00ad43d8) · [`00ad4400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad43a0.md#insn-00ad4400)

~~~diff
- 00ad43d0 ["INT_ADD", "register:40f0:8", ["const:ad43d0:8", "const:4:8"]]
- 00ad43d0 ["CALL", null, ["callee:00ad492c:8"]]
+ 00ad4414 ["INT_ADD", "register:40f0:8", ["const:ad4414:8", "const:4:8"]]
+ 00ad4414 ["CALL", null, ["callee:00ad492c:8"]]
- 00ad43d0 bytes 46010094
+ 00ad4414 bytes 46010094
- 00ad4394 ["COPY", "register:0:8", ["register:4048:8"]]
- 00ad4394 ["INT_ADD", "register:40f0:8", ["const:ad4394:8", "const:4:8"]]
- 00ad4394 ["CALLIND", null, ["register:0:8"]]
+ 00ad43d8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00ad43d8 ["INT_ADD", "register:40f0:8", ["const:ad43d8:8", "const:4:8"]]
+ 00ad43d8 ["CALLIND", null, ["register:0:8"]]
- 00ad4394 bytes 20013fd6
+ 00ad43d8 bytes 20013fd6
- 00ad43bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad43bc ["INT_ADD", "register:40f0:8", ["const:ad43bc:8", "const:4:8"]]
- 00ad43bc ["CALLIND", null, ["register:0:8"]]
+ 00ad4400 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad4400 ["INT_ADD", "register:40f0:8", ["const:ad4400:8", "const:4:8"]]
+ 00ad4400 ["CALLIND", null, ["register:0:8"]]
- 00ad43bc bytes 00013fd6
+ 00ad4400 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70247f260d0ad8d2a76c4b0f97ffeba7"></a>

### [`00ad4424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4424.md) → [`00ad4468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4468.md) FUN_00ad4468

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058cfe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058c/0058cfe0.md) · 呼出先 2件 [`00ad4a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4a50.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0058cfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058cfe0.md) · 呼出先 2件 [`00ad4a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4a94.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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
      "definition_site": "00ad44d0",
      "incomplete_value": false,
      "site": "00ad44dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad448c",
      "incomplete_value": false,
      "site": "00ad4498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
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
      "00ad44d0",
      "PARAM",
      [
        "storage",
        "0109fc80",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad44d0",
      "PARAM",
      [
        "storage",
        "0109fcc0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad4498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4424.md#insn-00ad4498) · [`00ad445c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4424.md#insn-00ad445c) · [`00ad4484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4424.md#insn-00ad4484)
- 新版 [`00ad44dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4468.md#insn-00ad44dc) · [`00ad44a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4468.md#insn-00ad44a0) · [`00ad44c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4468.md#insn-00ad44c8)

~~~diff
- 00ad4498 ["INT_ADD", "register:40f0:8", ["const:ad4498:8", "const:4:8"]]
- 00ad4498 ["CALL", null, ["callee:00ad4a94:8"]]
+ 00ad44dc ["INT_ADD", "register:40f0:8", ["const:ad44dc:8", "const:4:8"]]
+ 00ad44dc ["CALL", null, ["callee:00ad4a94:8"]]
- 00ad4498 bytes 6e010094
+ 00ad44dc bytes 6e010094
- 00ad445c ["COPY", "register:0:8", ["register:4048:8"]]
- 00ad445c ["INT_ADD", "register:40f0:8", ["const:ad445c:8", "const:4:8"]]
- 00ad445c ["CALLIND", null, ["register:0:8"]]
+ 00ad44a0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00ad44a0 ["INT_ADD", "register:40f0:8", ["const:ad44a0:8", "const:4:8"]]
+ 00ad44a0 ["CALLIND", null, ["register:0:8"]]
- 00ad445c bytes 20013fd6
+ 00ad44a0 bytes 20013fd6
- 00ad4484 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad4484 ["INT_ADD", "register:40f0:8", ["const:ad4484:8", "const:4:8"]]
- 00ad4484 ["CALLIND", null, ["register:0:8"]]
+ 00ad44c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad44c8 ["INT_ADD", "register:40f0:8", ["const:ad44c8:8", "const:4:8"]]
+ 00ad44c8 ["CALLIND", null, ["register:0:8"]]
- 00ad4484 bytes 00013fd6
+ 00ad44c8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8cc76f1d3866c387fe8a4a02a544bce"></a>

### [`00ad44ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad44ec.md) → [`00ad4530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4530.md) FUN_00ad4530

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058cfe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058c/0058cfe0.md) · 呼出先 13件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00848b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848b34.md) [`00848bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848bc0.md) [`00ad4bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4bb8.md) [`00ad4db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4db4.md)
- 新版 呼出元 1件 [`0058cfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058cfe0.md) · 呼出先 13件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00848b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848b34.md) [`00848bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848bc0.md) [`00ad4bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4bfc.md) [`00ad4df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4df8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad4668",
      "incomplete_value": false,
      "site": "00ad4674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad4624",
      "incomplete_value": false,
      "site": "00ad4630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:878:8"
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
      "definition_site": "00ad4680",
      "incomplete_value": false,
      "site": "00ad4680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad463c",
      "incomplete_value": false,
      "site": "00ad463c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ad462c",
      "incomplete_value": false,
      "site": "00ad4634",
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
            "const:8ef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad45e8",
      "incomplete_value": false,
      "site": "00ad45f0",
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
            "const:855:8"
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
      "00ad462c",
      "PARAM",
      [
        "storage",
        "002a8855",
        null,
        null
      ]
    ],
    [
      "00ad4674",
      "DATA",
      [
        "storage",
        "00c0f878",
        null,
        "undefined *"
      ]
    ],
    [
      "00ad4680",
      "DATA",
      [
        "storage",
        "00c0f878",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ad462c",
      "PARAM",
      [
        "storage",
        "002a88ef",
        null,
        null
      ]
    ],
    [
      "00ad4674",
      "DATA",
      [
        "storage",
        "00c0f8c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00ad4680",
      "DATA",
      [
        "storage",
        "00c0f8c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad45f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad44ec.md#insn-00ad45f0) · [`00ad4674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad44ec.md#insn-00ad4674) · [`00ad455c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad44ec.md#insn-00ad455c)
- 新版 [`00ad4634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4530.md#insn-00ad4634) · [`00ad46b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4530.md#insn-00ad46b8) · [`00ad45a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4530.md#insn-00ad45a0)

~~~diff
- 00ad45f0 ["INT_ADD", "register:40f0:8", ["const:ad45f0:8", "const:4:8"]]
- 00ad45f0 ["CALL", null, ["callee:00ad4df8:8"]]
+ 00ad4634 ["INT_ADD", "register:40f0:8", ["const:ad4634:8", "const:4:8"]]
+ 00ad4634 ["CALL", null, ["callee:00ad4df8:8"]]
- 00ad45f0 bytes f1010094
+ 00ad4634 bytes f1010094
- 00ad4674 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad4674 ["INT_ADD", "register:40f0:8", ["const:ad4674:8", "const:4:8"]]
- 00ad4674 ["CALLIND", null, ["register:0:8"]]
+ 00ad46b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad46b8 ["INT_ADD", "register:40f0:8", ["const:ad46b8:8", "const:4:8"]]
+ 00ad46b8 ["CALLIND", null, ["register:0:8"]]
- 00ad4674 bytes 00013fd6
+ 00ad46b8 bytes 00013fd6
- 00ad455c ["INT_ADD", "register:40f0:8", ["const:ad455c:8", "const:4:8"]]
- 00ad455c ["CALL", null, ["callee:00bdb5e0:8"]]
+ 00ad45a0 ["INT_ADD", "register:40f0:8", ["const:ad45a0:8", "const:4:8"]]
+ 00ad45a0 ["CALL", null, ["callee:00bdb5e0:8"]]
- 00ad455c bytes 0d1c0494
+ 00ad45a0 bytes 101c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37c1decc86203c1e190058ec929eb9fe"></a>

### [`00ad4fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4fb8.md) → [`00ad4ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4ffc.md) FUN_00ad4ffc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ad5010",
      "incomplete_value": false,
      "site": "00ad5014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad4fcc",
      "incomplete_value": false,
      "site": "00ad4fd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:878:8"
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
      "00ad5014",
      "DATA",
      [
        "storage",
        "00c0f878",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ad5014",
      "DATA",
      [
        "storage",
        "00c0f8c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad4fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4fb8.md#insn-00ad4fc4) · [`00ad4fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4fb8.md#insn-00ad4fcc)
- 新版 [`00ad5008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4ffc.md#insn-00ad5008) · [`00ad5010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4ffc.md#insn-00ad5010)

~~~diff
- 00ad4fc4 ["INT_ADD", "register:40f0:8", ["const:ad4fc4:8", "const:4:8"]]
- 00ad4fc4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ad5008 ["INT_ADD", "register:40f0:8", ["const:ad5008:8", "const:4:8"]]
+ 00ad5008 ["CALL", null, ["callee:00bdb040:8"]]
- 00ad4fc4 bytes 0b180494
+ 00ad5008 bytes 0e180494
- 00ad4fcc ["COPY", "tmp:0:8", ["const:878:8"]]
- 00ad4fcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ad4fcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ad4fcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ad5010 ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 00ad5010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ad5010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ad5010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ad4fcc bytes 08e12191
+ 00ad5010 bytes 08212391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6724fe27164125a134e93841215b2719"></a>

### [`00ad4fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4fdc.md) → [`00ad5020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5020.md) FUN_00ad5020

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ad5024",
      "incomplete_value": false,
      "site": "00ad5028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad4fe0",
      "incomplete_value": false,
      "site": "00ad4fe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:878:8"
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
      "00ad5028",
      "DATA",
      [
        "storage",
        "00c0f878",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ad5028",
      "DATA",
      [
        "storage",
        "00c0f8c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad4fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4fdc.md#insn-00ad4fe0)
- 新版 [`00ad5024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5020.md#insn-00ad5024)

~~~diff
- 00ad4fe0 ["COPY", "tmp:0:8", ["const:878:8"]]
- 00ad4fe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ad4fe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ad4fe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ad5024 ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 00ad5024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ad5024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ad5024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ad4fe0 bytes 08e12191
+ 00ad5024 bytes 08212391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-652186743c54f38a2682cf691e553762"></a>

### [`00ad553c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad553c.md) → [`00ad5580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5580.md) FUN_00ad5580

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ad5594",
      "incomplete_value": false,
      "site": "00ad5598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad5550",
      "incomplete_value": false,
      "site": "00ad5554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "00ad5598",
      "DATA",
      [
        "storage",
        "00c0f8e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ad5598",
      "DATA",
      [
        "storage",
        "00c0f938",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad5548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad553c.md#insn-00ad5548) · [`00ad5550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad553c.md#insn-00ad5550)
- 新版 [`00ad558c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5580.md#insn-00ad558c) · [`00ad5594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5580.md#insn-00ad5594)

~~~diff
- 00ad5548 ["INT_ADD", "register:40f0:8", ["const:ad5548:8", "const:4:8"]]
- 00ad5548 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ad558c ["INT_ADD", "register:40f0:8", ["const:ad558c:8", "const:4:8"]]
+ 00ad558c ["CALL", null, ["callee:00bdb040:8"]]
- 00ad5548 bytes aa160494
+ 00ad558c bytes ad160494
- 00ad5550 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 00ad5550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ad5550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ad5550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ad5594 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 00ad5594 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ad5594 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ad5594 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ad5550 bytes 08a12391
+ 00ad5594 bytes 08e12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1438cc464a10811beb5086045d0072e0"></a>

### [`00ad5578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5578.md) → [`00ad55bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad55bc.md) FUN_00ad55bc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 98.13% / 新版 98.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ad56b0",
      "incomplete_value": true,
      "site": "00ad56b0",
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
      "definition_site": "00ad566c",
      "incomplete_value": true,
      "site": "00ad566c",
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
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ad56a4",
      "READ",
      [
        "storage",
        "0109fc70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ad56a4",
      "READ",
      [
        "storage",
        "0109fcb0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad55a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5578.md#insn-00ad55a4) · [`00ad55bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5578.md#insn-00ad55bc) · [`00ad55d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5578.md#insn-00ad55d0)
- 新版 [`00ad55e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad55bc.md#insn-00ad55e8) · [`00ad5600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad55bc.md#insn-00ad5600) · [`00ad5614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad55bc.md#insn-00ad5614)

~~~diff
- 00ad55a4 ["INT_ADD", "register:40f0:8", ["const:ad55a4:8", "const:4:8"]]
- 00ad55a4 ["CALL", null, ["callee:00bddc20:8"]]
+ 00ad55e8 ["INT_ADD", "register:40f0:8", ["const:ad55e8:8", "const:4:8"]]
+ 00ad55e8 ["CALL", null, ["callee:00bddc20:8"]]
- 00ad55a4 bytes 8b210494
+ 00ad55e8 bytes 8e210494
- 00ad55bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad55bc ["INT_ADD", "register:40f0:8", ["const:ad55bc:8", "const:4:8"]]
- 00ad55bc ["CALLIND", null, ["register:0:8"]]
+ 00ad5600 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad5600 ["INT_ADD", "register:40f0:8", ["const:ad5600:8", "const:4:8"]]
+ 00ad5600 ["CALLIND", null, ["register:0:8"]]
- 00ad55bc bytes 00013fd6
+ 00ad5600 bytes 00013fd6
- 00ad55d0 ["INT_ADD", "register:40f0:8", ["const:ad55d0:8", "const:4:8"]]
- 00ad55d0 ["CALL", null, ["callee:00bddc30:8"]]
+ 00ad5614 ["INT_ADD", "register:40f0:8", ["const:ad5614:8", "const:4:8"]]
+ 00ad5614 ["CALL", null, ["callee:00bddc30:8"]]
- 00ad55d0 bytes 84210494
+ 00ad5614 bytes 87210494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d973d57670358d5f64e1ee61079805fe"></a>

### [`00ad57c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad57c4.md) → [`00ad5808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5808.md) _INIT_258

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00ad42fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad42fc.md) [`00ad432c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad432c.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00ad4340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4340.md) [`00ad4370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4370.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 52.38% / 新版 52.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ad5830",
      "incomplete_value": false,
      "site": "00ad5830",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:c90:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad57ec",
      "incomplete_value": false,
      "site": "00ad57ec",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:c50:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ad584c",
      "incomplete_value": false,
      "site": "00ad584c",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:cc0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad5808",
      "incomplete_value": false,
      "site": "00ad5808",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:c80:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
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
      "definition_site": "00ad5828",
      "incomplete_value": false,
      "site": "00ad5834",
      "value": [
        "leaf",
        "const:ad4340:8"
      ]
    },
    "old": {
      "definition_site": "00ad57e4",
      "incomplete_value": false,
      "site": "00ad57f0",
      "value": [
        "leaf",
        "const:ad42fc:8"
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
      "00ad5820",
      "PARAM",
      [
        "storage",
        "0109fc50",
        null,
        null
      ]
    ],
    [
      "unmatched:00ad57e4",
      "PARAM",
      [
        "storage",
        "00ad42fc",
        null,
        null
      ]
    ],
    [
      "00ad582c",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ad5820",
      "PARAM",
      [
        "storage",
        "0109fc90",
        null,
        null
      ]
    ],
    [
      "00ad5828",
      "PARAM",
      [
        "storage",
        "00ad4340",
        null,
        null
      ]
    ],
    [
      "00ad582c",
      "PARAM",
      [
        "storage",
        "00be5fd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad57f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad57c4.md#insn-00ad57f0) · [`00ad57d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad57c4.md#insn-00ad57d4) · [`00ad57d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad57c4.md#insn-00ad57d8)
- 新版 [`00ad5834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5808.md#insn-00ad5834) · [`00ad5818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5808.md#insn-00ad5818)

~~~diff
- 00ad57f0 ["INT_ADD", "register:40f0:8", ["const:ad57f0:8", "const:4:8"]]
- 00ad57f0 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00ad5834 ["INT_ADD", "register:40f0:8", ["const:ad5834:8", "const:4:8"]]
+ 00ad5834 ["CALL", null, ["callee:00bdafe0:8"]]
- 00ad57f0 bytes e8150494
+ 00ad5834 bytes eb150494
- 00ad57d4 ["COPY", "tmp:0:8", ["const:f80:8"]]
- 00ad57d4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00ad57d4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00ad57d4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00ad5818 ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 00ad5818 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00ad5818 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00ad5818 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00ad57d4 bytes 73023e91
+ 00ad5818 bytes 73423f91
- 00ad57d8 ["COPY", "register:4008:8", ["const:109f000:8"]]
- 00ad57d8 bytes 412e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-618599de9b94d8c7d46fb73eb901b6de"></a>

### [`00ad5b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5b2c.md) → [`00ad5b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5b70.md) _INIT_259

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00ad5bac",
      "incomplete_value": true,
      "site": "00ad5bc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad5b68",
      "incomplete_value": true,
      "site": "00ad5b84",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad5bd0",
      "incomplete_value": true,
      "site": "00ad5bec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad5b8c",
      "incomplete_value": true,
      "site": "00ad5ba8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad5bf0",
      "incomplete_value": true,
      "site": "00ad5c0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad5bac",
      "incomplete_value": true,
      "site": "00ad5bc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00ad5bac",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00ad5bd0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00ad5bf0",
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
      "00ad5bac",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00ad5bd0",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00ad5bf0",
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

- 旧版 [`00ad5b64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5b2c.md#insn-00ad5b64) · [`00ad5c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5b2c.md#insn-00ad5c8c) · [`00ad5d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5b2c.md#insn-00ad5d60)
- 新版 [`00ad5ba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5b70.md#insn-00ad5ba8) · [`00ad5cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5b70.md#insn-00ad5cd0) · [`00ad5da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5b70.md#insn-00ad5da4)

~~~diff
- 00ad5b64 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00ad5b64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ad5b64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ad5b64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ad5ba8 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00ad5ba8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad5ba8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad5ba8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ad5b64 bytes 29750b91
+ 00ad5ba8 bytes 29dd0d91
- 00ad5c8c ["INT_ADD", "register:40f0:8", ["const:ad5c8c:8", "const:4:8"]]
- 00ad5c8c ["CALL", null, ["callee:00418cb8:8"]]
+ 00ad5cd0 ["INT_ADD", "register:40f0:8", ["const:ad5cd0:8", "const:4:8"]]
+ 00ad5cd0 ["CALL", null, ["callee:00418cb8:8"]]
- 00ad5c8c bytes 0b0ce597
+ 00ad5cd0 bytes fa0be597
- 00ad5d60 ["INT_ADD", "register:40f0:8", ["const:ad5d60:8", "const:4:8"]]
- 00ad5d60 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00ad5da4 ["INT_ADD", "register:40f0:8", ["const:ad5da4:8", "const:4:8"]]
+ 00ad5da4 ["CALL", null, ["callee:00bdafe0:8"]]
- 00ad5d60 bytes 8c140494
+ 00ad5da4 bytes 8f140494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad0e5005b92fbbd20bb02373fdaf2de1"></a>

### [`00ad5ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5ec8.md) → [`00ad5f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5f0c.md) FUN_00ad5f0c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00418b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418b94.md) · 呼出先 5件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00ad60b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad60b4.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00418b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418b94.md) · 呼出先 5件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00ad60f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad60f8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

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
      "definition_site": "00ad5f3c",
      "incomplete_value": true,
      "site": "00ad5f3c",
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
      "definition_site": "00ad5ef8",
      "incomplete_value": true,
      "site": "00ad5ef8",
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
      "definition_site": "00ad5fec",
      "incomplete_value": false,
      "site": "00ad5ff8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad5fa8",
      "incomplete_value": false,
      "site": "00ad5fb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "00ad5f38",
      "READ",
      [
        "storage",
        "0109fcd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad5fec",
      "PARAM",
      [
        "storage",
        "0109fcd0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ad5f38",
      "READ",
      [
        "storage",
        "0109fd18",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad5fec",
      "PARAM",
      [
        "storage",
        "0109fd10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad5fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5ec8.md#insn-00ad5fb4) · [`00ad5ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5ec8.md#insn-00ad5ef4) · [`00ad5f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5ec8.md#insn-00ad5f54)
- 新版 [`00ad5ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5f0c.md#insn-00ad5ff8) · [`00ad5f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5f0c.md#insn-00ad5f38) · [`00ad5f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5f0c.md#insn-00ad5f98)

~~~diff
- 00ad5fb4 ["INT_ADD", "register:40f0:8", ["const:ad5fb4:8", "const:4:8"]]
- 00ad5fb4 ["CALL", null, ["callee:00ad60f8:8"]]
+ 00ad5ff8 ["INT_ADD", "register:40f0:8", ["const:ad5ff8:8", "const:4:8"]]
+ 00ad5ff8 ["CALL", null, ["callee:00ad60f8:8"]]
- 00ad5fb4 bytes 40000094
+ 00ad5ff8 bytes 40000094
- 00ad5ef4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd8:8"]]
- 00ad5ef4 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ad5f38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d18:8"]]
+ 00ad5f38 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ad5ef4 bytes 186d46f9
+ 00ad5f38 bytes 188d46f9
- 00ad5f54 ["INT_ADD", "register:40f0:8", ["const:ad5f54:8", "const:4:8"]]
- 00ad5f54 ["CALL", null, ["callee:00bdb200:8"]]
+ 00ad5f98 ["INT_ADD", "register:40f0:8", ["const:ad5f98:8", "const:4:8"]]
+ 00ad5f98 ["CALL", null, ["callee:00bdb200:8"]]
- 00ad5f54 bytes 97140494
+ 00ad5f98 bytes 9a140494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e98c977298878d446a8bf71f7feae2ee"></a>

### [`00ad61b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad61b8.md) → [`00ad61fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad61fc.md) _INIT_260

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00ad5ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5ec0.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00ad5f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5f04.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 45.45% / 新版 45.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ad6218",
      "incomplete_value": false,
      "site": "00ad6218",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:d10:8"
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
      "definition_site": "00ad61d4",
      "incomplete_value": false,
      "site": "00ad61d4",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:cd0:8"
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ad621c",
      "incomplete_value": false,
      "site": "00ad621c",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:d10:8"
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
      "definition_site": "00ad61d8",
      "incomplete_value": false,
      "site": "00ad61d8",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:cd0:8"
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ad6220",
      "incomplete_value": false,
      "site": "00ad6220",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad61dc",
      "incomplete_value": false,
      "site": "00ad61dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "00ad6200",
      "PARAM",
      [
        "storage",
        "0109fcd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad6208",
      "PARAM",
      [
        "storage",
        "00ad5ec0",
        null,
        null
      ]
    ],
    [
      "00ad6214",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ad6200",
      "PARAM",
      [
        "storage",
        "0109fd10",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad6208",
      "PARAM",
      [
        "storage",
        "00ad5f04",
        null,
        null
      ]
    ],
    [
      "00ad6214",
      "PARAM",
      [
        "storage",
        "00be5fd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad61bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad61b8.md#insn-00ad61bc) · [`00ad61c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad61b8.md#insn-00ad61c4) · [`00ad61d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad61b8.md#insn-00ad61d0)
- 新版 [`00ad6200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad61fc.md#insn-00ad6200) · [`00ad6208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad61fc.md#insn-00ad6208) · [`00ad6214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad61fc.md#insn-00ad6214)

~~~diff
- 00ad61bc ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 00ad61bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00ad61bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00ad61bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00ad6200 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 00ad6200 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00ad6200 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00ad6200 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00ad61bc bytes 21403391
+ 00ad6200 bytes 21403491
- 00ad61c4 ["COPY", "register:4000:8", ["const:ad5ec0:8"]]
+ 00ad6208 ["COPY", "register:4000:8", ["const:ad5f04:8"]]
- 00ad61c4 bytes e0e7ff10
+ 00ad6208 bytes e0e7ff10
- 00ad61d0 ["COPY", "tmp:0:8", ["const:f80:8"]]
- 00ad61d0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00ad61d0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00ad61d0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00ad6214 ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 00ad6214 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00ad6214 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00ad6214 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00ad61d0 bytes 42003e91
+ 00ad6214 bytes 42403f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b23f0a9c20993ea459e5103c9566d684"></a>

### [`00ad6320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6320.md) → [`00ad6364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6364.md) FUN_00ad6364

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00596660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596660.md) [`008648a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md) · 呼出先 10件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 2件 [`00596660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596660.md) [`008648a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008648a8.md) · 呼出先 10件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.47% / 新版 92.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad63b0",
      "incomplete_value": true,
      "site": "00ad63c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:73:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad636c",
      "incomplete_value": true,
      "site": "00ad637c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fd9:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00ad63b4",
      "incomplete_value": true,
      "site": "00ad63e0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00ad6370",
      "incomplete_value": true,
      "site": "00ad639c",
      "value": [
        "LOAD",
        "16",
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
      "00ad63b0",
      "READ",
      [
        "storage",
        "002a6fd9",
        null,
        "string"
      ]
    ],
    [
      "00ad63b4",
      "READ",
      [
        "storage",
        "002a6fe3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ad63b0",
      "READ",
      [
        "storage",
        "002a7073",
        null,
        "string"
      ]
    ],
    [
      "00ad63b4",
      "READ",
      [
        "storage",
        "002a707d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad6358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6320.md#insn-00ad6358) · [`00ad63c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6320.md#insn-00ad63c0) · [`00ad6344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6320.md#insn-00ad6344)
- 新版 [`00ad639c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6364.md#insn-00ad639c) · [`00ad6404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6364.md#insn-00ad6404) · [`00ad6388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6364.md#insn-00ad6388)

~~~diff
- 00ad6358 ["INT_ADD", "register:40f0:8", ["const:ad6358:8", "const:4:8"]]
- 00ad6358 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ad639c ["INT_ADD", "register:40f0:8", ["const:ad639c:8", "const:4:8"]]
+ 00ad639c ["CALL", null, ["callee:00bdb040:8"]]
- 00ad6358 bytes 26130494
+ 00ad639c bytes 29130494
- 00ad63c0 ["INT_ADD", "register:40f0:8", ["const:ad63c0:8", "const:4:8"]]
- 00ad63c0 ["CALL", null, ["callee:00566448:8"]]
+ 00ad6404 ["INT_ADD", "register:40f0:8", ["const:ad6404:8", "const:4:8"]]
+ 00ad6404 ["CALL", null, ["callee:00566448:8"]]
- 00ad63c0 bytes 2240ea97
+ 00ad6404 bytes 1140ea97
- 00ad6344 ["INT_ADD", "register:40f0:8", ["const:ad6344:8", "const:4:8"]]
- 00ad6344 ["CALL", null, ["callee:00565f94:8"]]
+ 00ad6388 ["INT_ADD", "register:40f0:8", ["const:ad6388:8", "const:4:8"]]
+ 00ad6388 ["CALL", null, ["callee:00565f94:8"]]
- 00ad6344 bytes 143fea97
+ 00ad6388 bytes 033fea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b906fdead431d2b4d47f9ce2df393ca5"></a>

### [`00ad64d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad64d0.md) → [`00ad6514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6514.md) _INIT_261

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 44.44% / 新版 44.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ad652c",
      "incomplete_value": false,
      "site": "00ad652c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad64e8",
      "incomplete_value": false,
      "site": "00ad64e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ad652c",
      "incomplete_value": false,
      "site": "00ad652c",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:d28:8"
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
      "definition_site": "00ad64e8",
      "incomplete_value": false,
      "site": "00ad64e8",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:ce8:8"
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ad6530",
      "incomplete_value": false,
      "site": "00ad6530",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:d28:8"
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
      "definition_site": "00ad64ec",
      "incomplete_value": false,
      "site": "00ad64ec",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:ce8:8"
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
      "00ad651c",
      "PARAM",
      [
        "storage",
        "0109fce8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad6520",
      "READ",
      [
        "storage",
        "00c1adb8",
        null,
        "pointer"
      ]
    ],
    [
      "00ad6520",
      "PARAM",
      [
        "storage",
        "00b55618",
        "_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev",
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad651c",
      "PARAM",
      [
        "storage",
        "0109fd28",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad6520",
      "READ",
      [
        "storage",
        "00c1ae08",
        null,
        "pointer"
      ]
    ],
    [
      "00ad6520",
      "PARAM",
      [
        "storage",
        "00b5565c",
        "_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad64d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad64d0.md#insn-00ad64d8) · [`00ad64dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad64d0.md#insn-00ad64dc) · [`00ad64e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad64d0.md#insn-00ad64e4)
- 新版 [`00ad651c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6514.md#insn-00ad651c) · [`00ad6520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6514.md#insn-00ad6520) · [`00ad6528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6514.md#insn-00ad6528)

~~~diff
- 00ad64d8 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 00ad64d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00ad64d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00ad64d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00ad651c ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00ad651c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00ad651c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00ad651c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00ad64d8 bytes 21a03391
+ 00ad651c bytes 21a03491
- 00ad64dc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:db8:8"]]
- 00ad64dc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ad6520 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:e08:8"]]
+ 00ad6520 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00ad64dc bytes 00dc46f9
+ 00ad6520 bytes 000447f9
- 00ad64e4 ["COPY", "tmp:0:8", ["const:f80:8"]]
- 00ad64e4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00ad64e4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00ad64e4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00ad6528 ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 00ad6528 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00ad6528 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00ad6528 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00ad64e4 bytes 42003e91
+ 00ad6528 bytes 42403f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac9f276474b338eb4a9e68c7693a07f4"></a>

### [`00ad64f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad64f4.md) → [`00ad6538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6538.md) FUN_00ad6538

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084b738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084b/0084b738.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0084b738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084b738.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad658c",
      "incomplete_value": true,
      "site": "00ad658c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f4d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad6548",
      "incomplete_value": true,
      "site": "00ad6548",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec2:8"
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
      "definition_site": "00ad6594",
      "incomplete_value": true,
      "site": "00ad6594",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ad6550",
      "incomplete_value": true,
      "site": "00ad6550",
      "value": [
        "LOAD",
        "8",
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
      "00ad6574",
      "READ",
      [
        "storage",
        "0029fec2",
        null,
        "string"
      ]
    ],
    [
      "00ad657c",
      "READ",
      [
        "storage",
        "0029fec8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ad6574",
      "READ",
      [
        "storage",
        "0029ff4d",
        null,
        "string"
      ]
    ],
    [
      "00ad657c",
      "READ",
      [
        "storage",
        "0029ff53",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad6518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad64f4.md#insn-00ad6518) · [`00ad6520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad64f4.md#insn-00ad6520) · [`00ad652c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad64f4.md#insn-00ad652c)
- 新版 [`00ad655c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6538.md#insn-00ad655c) · [`00ad6564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6538.md#insn-00ad6564) · [`00ad6570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6538.md#insn-00ad6570)

~~~diff
- 00ad6518 ["INT_ADD", "register:40f0:8", ["const:ad6518:8", "const:4:8"]]
- 00ad6518 ["CALL", null, ["callee:00565f94:8"]]
+ 00ad655c ["INT_ADD", "register:40f0:8", ["const:ad655c:8", "const:4:8"]]
+ 00ad655c ["CALL", null, ["callee:00565f94:8"]]
- 00ad6518 bytes 9f3eea97
+ 00ad655c bytes 8e3eea97
- 00ad6520 ["INT_ADD", "register:40f0:8", ["const:ad6520:8", "const:4:8"]]
- 00ad6520 ["CALL", null, ["callee:00566284:8"]]
+ 00ad6564 ["INT_ADD", "register:40f0:8", ["const:ad6564:8", "const:4:8"]]
+ 00ad6564 ["CALL", null, ["callee:00566284:8"]]
- 00ad6520 bytes 593fea97
+ 00ad6564 bytes 483fea97
- 00ad652c ["COPY", "tmp:0:8", ["const:ec2:8"]]
- 00ad652c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ad652c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ad652c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ad6570 ["COPY", "tmp:0:8", ["const:f4d:8"]]
+ 00ad6570 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad6570 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad6570 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ad652c bytes 29093b91
+ 00ad6570 bytes 29353d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-625b77989e709782ec6f1e331412367b"></a>

### [`00ad6700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6700.md) → [`00ad6744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6744.md) _INIT_262

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00ad6780",
      "incomplete_value": true,
      "site": "00ad679c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad673c",
      "incomplete_value": true,
      "site": "00ad6758",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad67a4",
      "incomplete_value": true,
      "site": "00ad67c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad6760",
      "incomplete_value": true,
      "site": "00ad677c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad67c4",
      "incomplete_value": true,
      "site": "00ad67e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad6780",
      "incomplete_value": true,
      "site": "00ad679c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00ad6780",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00ad67a4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00ad67c4",
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
      "00ad6780",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00ad67a4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00ad67c4",
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

- 旧版 [`00ad6738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6700.md#insn-00ad6738) · [`00ad6934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6700.md#insn-00ad6934) · [`00ad672c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6700.md#insn-00ad672c)
- 新版 [`00ad677c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6744.md#insn-00ad677c) · [`00ad6978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6744.md#insn-00ad6978) · [`00ad6770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6744.md#insn-00ad6770)

~~~diff
- 00ad6738 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00ad6738 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ad6738 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ad6738 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ad677c ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00ad677c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad677c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad677c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ad6738 bytes 29750b91
+ 00ad677c bytes 29dd0d91
- 00ad6934 ["INT_ADD", "register:40f0:8", ["const:ad6934:8", "const:4:8"]]
- 00ad6934 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00ad6978 ["INT_ADD", "register:40f0:8", ["const:ad6978:8", "const:4:8"]]
+ 00ad6978 ["CALL", null, ["callee:00bdafe0:8"]]
- 00ad6934 bytes 97110494
+ 00ad6978 bytes 9a110494
- 00ad672c ["COPY", "tmp:0:8", ["const:d00:8"]]
- 00ad672c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00ad672c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00ad672c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00ad6770 ["COPY", "tmp:0:8", ["const:d40:8"]]
+ 00ad6770 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00ad6770 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00ad6770 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00ad672c bytes 73023491
+ 00ad6770 bytes 73023591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46cea012b7ed8634709bfa58301daa2d"></a>

### [`00ad6a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6a90.md) → [`00ad6ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6ad4.md) FUN_00ad6ad4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0058cea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058c/0058cea4.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0058cea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058cea4.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad6b24",
      "incomplete_value": true,
      "site": "00ad6b24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d1a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad6ae0",
      "incomplete_value": true,
      "site": "00ad6ae0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c8f:8"
              ]
            ]
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
      "00ad6b10",
      "READ",
      [
        "storage",
        "0029dc8f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ad6b10",
      "READ",
      [
        "storage",
        "0029dd1a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad6ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6a90.md#insn-00ad6ac0) · [`00ad6ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6a90.md#insn-00ad6ae8) · [`00ad6af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6a90.md#insn-00ad6af0)
- 新版 [`00ad6b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6ad4.md#insn-00ad6b04) · [`00ad6b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6ad4.md#insn-00ad6b2c) · [`00ad6b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6ad4.md#insn-00ad6b34)

~~~diff
- 00ad6ac0 ["COPY", "tmp:0:8", ["const:c8f:8"]]
- 00ad6ac0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ad6ac0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ad6ac0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ad6b04 ["COPY", "tmp:0:8", ["const:d1a:8"]]
+ 00ad6b04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad6b04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad6b04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ad6ac0 bytes 293d3291
+ 00ad6b04 bytes 29693491
- 00ad6ae8 ["INT_ADD", "register:40f0:8", ["const:ad6ae8:8", "const:4:8"]]
- 00ad6ae8 ["CALL", null, ["callee:00565f94:8"]]
+ 00ad6b2c ["INT_ADD", "register:40f0:8", ["const:ad6b2c:8", "const:4:8"]]
+ 00ad6b2c ["CALL", null, ["callee:00565f94:8"]]
- 00ad6ae8 bytes 2b3dea97
+ 00ad6b2c bytes 1a3dea97
- 00ad6af0 ["INT_ADD", "register:40f0:8", ["const:ad6af0:8", "const:4:8"]]
- 00ad6af0 ["CALL", null, ["callee:00566284:8"]]
+ 00ad6b34 ["INT_ADD", "register:40f0:8", ["const:ad6b34:8", "const:4:8"]]
+ 00ad6b34 ["CALL", null, ["callee:00566284:8"]]
- 00ad6af0 bytes e53dea97
+ 00ad6b34 bytes d43dea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20d7680e042a0a6bc9bf230e8f460839"></a>

### [`00ad6bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6bb0.md) → [`00ad6bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6bf4.md) FUN_00ad6bf4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058cea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058c/0058cea4.md) · 呼出先 2件 [`00ad48e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad48e8.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0058cea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058cea4.md) · 呼出先 2件 [`00ad492c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad492c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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
      "definition_site": "00ad6c5c",
      "incomplete_value": false,
      "site": "00ad6c68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad6c18",
      "incomplete_value": false,
      "site": "00ad6c24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:d30:8"
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
      "00ad6c5c",
      "PARAM",
      [
        "storage",
        "0109fd30",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad6c5c",
      "PARAM",
      [
        "storage",
        "0109fd70",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad6c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6bb0.md#insn-00ad6c24) · [`00ad6be8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6bb0.md#insn-00ad6be8) · [`00ad6c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6bb0.md#insn-00ad6c10)
- 新版 [`00ad6c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6bf4.md#insn-00ad6c68) · [`00ad6c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6bf4.md#insn-00ad6c2c) · [`00ad6c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6bf4.md#insn-00ad6c54)

~~~diff
- 00ad6c24 ["INT_ADD", "register:40f0:8", ["const:ad6c24:8", "const:4:8"]]
- 00ad6c24 ["CALL", null, ["callee:00ad492c:8"]]
+ 00ad6c68 ["INT_ADD", "register:40f0:8", ["const:ad6c68:8", "const:4:8"]]
+ 00ad6c68 ["CALL", null, ["callee:00ad492c:8"]]
- 00ad6c24 bytes 31f7ff97
+ 00ad6c68 bytes 31f7ff97
- 00ad6be8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00ad6be8 ["INT_ADD", "register:40f0:8", ["const:ad6be8:8", "const:4:8"]]
- 00ad6be8 ["CALLIND", null, ["register:0:8"]]
+ 00ad6c2c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00ad6c2c ["INT_ADD", "register:40f0:8", ["const:ad6c2c:8", "const:4:8"]]
+ 00ad6c2c ["CALLIND", null, ["register:0:8"]]
- 00ad6be8 bytes 20013fd6
+ 00ad6c2c bytes 20013fd6
- 00ad6c10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad6c10 ["INT_ADD", "register:40f0:8", ["const:ad6c10:8", "const:4:8"]]
- 00ad6c10 ["CALLIND", null, ["register:0:8"]]
+ 00ad6c54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad6c54 ["INT_ADD", "register:40f0:8", ["const:ad6c54:8", "const:4:8"]]
+ 00ad6c54 ["CALLIND", null, ["register:0:8"]]
- 00ad6c10 bytes 00013fd6
+ 00ad6c54 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e466af34811ab1f44532edee0fec0a5"></a>

### [`00ad6c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6c78.md) → [`00ad6cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6cbc.md) FUN_00ad6cbc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058cea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058c/0058cea4.md) · 呼出先 2件 [`00ad4a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4a50.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0058cea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058cea4.md) · 呼出先 2件 [`00ad4a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4a94.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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
      "definition_site": "00ad6d24",
      "incomplete_value": false,
      "site": "00ad6d30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad6ce0",
      "incomplete_value": false,
      "site": "00ad6cec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
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
      "00ad6d24",
      "PARAM",
      [
        "storage",
        "0109fd60",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad6d24",
      "PARAM",
      [
        "storage",
        "0109fda0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad6cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6c78.md#insn-00ad6cec) · [`00ad6cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6c78.md#insn-00ad6cb0) · [`00ad6cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6c78.md#insn-00ad6cd8)
- 新版 [`00ad6d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6cbc.md#insn-00ad6d30) · [`00ad6cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6cbc.md#insn-00ad6cf4) · [`00ad6d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6cbc.md#insn-00ad6d1c)

~~~diff
- 00ad6cec ["INT_ADD", "register:40f0:8", ["const:ad6cec:8", "const:4:8"]]
- 00ad6cec ["CALL", null, ["callee:00ad4a94:8"]]
+ 00ad6d30 ["INT_ADD", "register:40f0:8", ["const:ad6d30:8", "const:4:8"]]
+ 00ad6d30 ["CALL", null, ["callee:00ad4a94:8"]]
- 00ad6cec bytes 59f7ff97
+ 00ad6d30 bytes 59f7ff97
- 00ad6cb0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00ad6cb0 ["INT_ADD", "register:40f0:8", ["const:ad6cb0:8", "const:4:8"]]
- 00ad6cb0 ["CALLIND", null, ["register:0:8"]]
+ 00ad6cf4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00ad6cf4 ["INT_ADD", "register:40f0:8", ["const:ad6cf4:8", "const:4:8"]]
+ 00ad6cf4 ["CALLIND", null, ["register:0:8"]]
- 00ad6cb0 bytes 20013fd6
+ 00ad6cf4 bytes 20013fd6
- 00ad6cd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad6cd8 ["INT_ADD", "register:40f0:8", ["const:ad6cd8:8", "const:4:8"]]
- 00ad6cd8 ["CALLIND", null, ["register:0:8"]]
+ 00ad6d1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad6d1c ["INT_ADD", "register:40f0:8", ["const:ad6d1c:8", "const:4:8"]]
+ 00ad6d1c ["CALLIND", null, ["register:0:8"]]
- 00ad6cd8 bytes 00013fd6
+ 00ad6d1c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01748cfa0e4994a488da135f56cc43b1"></a>

### [`00ad6e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6e74.md) → [`00ad6eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6eb8.md) Java_jp_co_ponos_battlecats_MyGoogleSignInListener_onFailure

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 88.37% / 新版 88.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad6ef4",
      "incomplete_value": true,
      "site": "00ad6f04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d1a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad6eb0",
      "incomplete_value": true,
      "site": "00ad6ec0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c80:8"
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
      "definition_site": "00ad6efc",
      "incomplete_value": true,
      "site": "00ad6f0c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00ad6eb8",
      "incomplete_value": true,
      "site": "00ad6ec8",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ad6edc",
      "incomplete_value": true,
      "site": "00ad6edc",
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
      "definition_site": "00ad6e98",
      "incomplete_value": true,
      "site": "00ad6e98",
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
      "00ad6ed8",
      "READ",
      [
        "storage",
        "0109fd80",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad6ef4",
      "READ",
      [
        "storage",
        "002a7c80",
        null,
        null
      ]
    ],
    [
      "00ad6efc",
      "READ",
      [
        "storage",
        "002a7c8d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad6ed8",
      "READ",
      [
        "storage",
        "0109fdc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad6ef4",
      "READ",
      [
        "storage",
        "002a7d1a",
        null,
        null
      ]
    ],
    [
      "00ad6efc",
      "READ",
      [
        "storage",
        "002a7d27",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad6e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6e74.md#insn-00ad6e94) · [`00ad6ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6e74.md#insn-00ad6ea0) · [`00ad6eac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6e74.md#insn-00ad6eac)
- 新版 [`00ad6ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6eb8.md#insn-00ad6ed8) · [`00ad6ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6eb8.md#insn-00ad6ee4) · [`00ad6ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6eb8.md#insn-00ad6ef0)

~~~diff
- 00ad6e94 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
- 00ad6e94 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ad6ed8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 00ad6ed8 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00ad6e94 bytes 13c146f9
+ 00ad6ed8 bytes 13e146f9
- 00ad6ea0 ["INT_ADD", "register:40f0:8", ["const:ad6ea0:8", "const:4:8"]]
- 00ad6ea0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ad6ee4 ["INT_ADD", "register:40f0:8", ["const:ad6ee4:8", "const:4:8"]]
+ 00ad6ee4 ["CALL", null, ["callee:00bdb040:8"]]
- 00ad6ea0 bytes 54100494
+ 00ad6ee4 bytes 57100494
- 00ad6eac ["COPY", "tmp:0:8", ["const:c80:8"]]
- 00ad6eac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ad6eac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ad6eac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ad6ef0 ["COPY", "tmp:0:8", ["const:d1a:8"]]
+ 00ad6ef0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad6ef0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad6ef0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ad6eac bytes 29013291
+ 00ad6ef0 bytes 29693491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da02e087d766c643bcb9a082e43500ec"></a>

### [`00ad6f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6f4c.md) → [`00ad6f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6f90.md) Java_jp_co_ponos_battlecats_MyGoogleSignInListener_onCancel

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad6fcc",
      "incomplete_value": true,
      "site": "00ad6fe4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ea0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad6f88",
      "incomplete_value": true,
      "site": "00ad6fa0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e15:8"
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
      "definition_site": "00ad6fcc",
      "incomplete_value": true,
      "site": "00ad6fe4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00ad6f88",
      "incomplete_value": true,
      "site": "00ad6fa0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad6fe8",
      "incomplete_value": true,
      "site": "00ad6fe8",
      "value": [
        "LOAD",
        "8",
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
                "const:1d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad6fa4",
      "incomplete_value": true,
      "site": "00ad6fa4",
      "value": [
        "LOAD",
        "8",
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
                "const:1d:8"
              ]
            ]
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
      "00ad6fb0",
      "READ",
      [
        "storage",
        "0109fd80",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad6fcc",
      "READ",
      [
        "storage",
        "002a0e15",
        null,
        null
      ]
    ],
    [
      "00ad6fcc",
      "READ",
      [
        "storage",
        "002a0e25",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad6fb0",
      "READ",
      [
        "storage",
        "0109fdc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad6fcc",
      "READ",
      [
        "storage",
        "002a0ea0",
        null,
        null
      ]
    ],
    [
      "00ad6fcc",
      "READ",
      [
        "storage",
        "002a0eb0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad6f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6f4c.md#insn-00ad6f6c) · [`00ad6f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6f4c.md#insn-00ad6f78) · [`00ad6f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6f4c.md#insn-00ad6f80)
- 新版 [`00ad6fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6f90.md#insn-00ad6fb0) · [`00ad6fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6f90.md#insn-00ad6fbc) · [`00ad6fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6f90.md#insn-00ad6fc4)

~~~diff
- 00ad6f6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
- 00ad6f6c ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ad6fb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 00ad6fb0 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00ad6f6c bytes 13c146f9
+ 00ad6fb0 bytes 13e146f9
- 00ad6f78 ["INT_ADD", "register:40f0:8", ["const:ad6f78:8", "const:4:8"]]
- 00ad6f78 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ad6fbc ["INT_ADD", "register:40f0:8", ["const:ad6fbc:8", "const:4:8"]]
+ 00ad6fbc ["CALL", null, ["callee:00bdb040:8"]]
- 00ad6f78 bytes 1e100494
+ 00ad6fbc bytes 21100494
- 00ad6f80 ["COPY", "tmp:0:8", ["const:e15:8"]]
- 00ad6f80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ad6f80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ad6f80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ad6fc4 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 00ad6fc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ad6fc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ad6fc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ad6f80 bytes 08553891
+ 00ad6fc4 bytes 08813a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9276844cadc31549548127e7ab0a7232"></a>

### [`00ad7030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7030.md) → [`00ad7074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7074.md) _INIT_263

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00ad42fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad42fc.md) [`00ad432c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad432c.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00ad4340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4340.md) [`00ad4370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4370.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 5件, `store_value` 7件, `unresolved_call_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad70b0",
      "incomplete_value": true,
      "site": "00ad70cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad706c",
      "incomplete_value": true,
      "site": "00ad7088",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad70d4",
      "incomplete_value": true,
      "site": "00ad70f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad7090",
      "incomplete_value": true,
      "site": "00ad70ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad70f4",
      "incomplete_value": true,
      "site": "00ad7110",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ad70b0",
      "incomplete_value": true,
      "site": "00ad70cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00ad70b0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00ad70d4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00ad70f4",
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
      "00ad70b0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00ad70d4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00ad70f4",
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

- 旧版 [`00ad7068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7030.md#insn-00ad7068) · [`00ad7190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7030.md#insn-00ad7190) · [`00ad7268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7030.md#insn-00ad7268)
- 新版 [`00ad70ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7074.md#insn-00ad70ac) · [`00ad71d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7074.md#insn-00ad71d4)

~~~diff
- 00ad7068 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00ad7068 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ad7068 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ad7068 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ad70ac ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00ad70ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad70ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad70ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ad7068 bytes 29750b91
+ 00ad70ac bytes 29dd0d91
- 00ad7190 ["INT_ADD", "register:40f0:8", ["const:ad7190:8", "const:4:8"]]
- 00ad7190 ["CALL", null, ["callee:00418cb8:8"]]
+ 00ad71d4 ["INT_ADD", "register:40f0:8", ["const:ad71d4:8", "const:4:8"]]
+ 00ad71d4 ["CALL", null, ["callee:00418cb8:8"]]
- 00ad7190 bytes ca06e597
+ 00ad71d4 bytes b906e597
- 00ad7268 ["INT_ADD", "register:40f0:8", ["const:ad7268:8", "const:4:8"]]
- 00ad7268 ["CALL", null, ["callee:00bdafe0:8"]]
- 00ad7268 bytes 4a0f0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02847b362b5643065ddf07ad150cc50d"></a>

### [`00ad7598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7598.md) → [`00ad75dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad75dc.md) FUN_00ad75dc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00854808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854808.md) · 呼出先 16件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00558fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558fd0.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md)
- 新版 呼出元 1件 [`00854808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/00854808.md) · 呼出先 16件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00558fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558fd0.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.65% / 新版 96.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad763c",
      "incomplete_value": true,
      "site": "00ad763c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad75f8",
      "incomplete_value": true,
      "site": "00ad75f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff4:8"
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
      "definition_site": "00ad7640",
      "incomplete_value": true,
      "site": "00ad7640",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ad75fc",
      "incomplete_value": true,
      "site": "00ad75fc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ad7708",
      "incomplete_value": false,
      "site": "00ad7714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad76c4",
      "incomplete_value": false,
      "site": "00ad76d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "00ad7628",
      "READ",
      [
        "storage",
        "002a6ff4",
        null,
        "string"
      ]
    ],
    [
      "00ad7630",
      "READ",
      [
        "storage",
        "002a6ffa",
        null,
        "string"
      ]
    ],
    [
      "00ad7708",
      "PARAM",
      [
        "storage",
        "0109fd90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad7628",
      "READ",
      [
        "storage",
        "002a708e",
        null,
        "string"
      ]
    ],
    [
      "00ad7630",
      "READ",
      [
        "storage",
        "002a7094",
        null,
        "string"
      ]
    ],
    [
      "00ad7708",
      "PARAM",
      [
        "storage",
        "0109fdd0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad76d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7598.md#insn-00ad76d0) · [`00ad75cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7598.md#insn-00ad75cc) · [`00ad75d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7598.md#insn-00ad75d4)
- 新版 [`00ad7714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad75dc.md#insn-00ad7714) · [`00ad7610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad75dc.md#insn-00ad7610) · [`00ad7618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad75dc.md#insn-00ad7618)

~~~diff
- 00ad76d0 ["INT_ADD", "register:40f0:8", ["const:ad76d0:8", "const:4:8"]]
- 00ad76d0 ["CALL", null, ["callee:00558fd0:8"]]
+ 00ad7714 ["INT_ADD", "register:40f0:8", ["const:ad7714:8", "const:4:8"]]
+ 00ad7714 ["CALL", null, ["callee:00558fd0:8"]]
- 00ad76d0 bytes 4006ea97
+ 00ad7714 bytes 2f06ea97
- 00ad75cc ["INT_ADD", "register:40f0:8", ["const:ad75cc:8", "const:4:8"]]
- 00ad75cc ["CALL", null, ["callee:00565f94:8"]]
+ 00ad7610 ["INT_ADD", "register:40f0:8", ["const:ad7610:8", "const:4:8"]]
+ 00ad7610 ["CALL", null, ["callee:00565f94:8"]]
- 00ad75cc bytes 723aea97
+ 00ad7610 bytes 613aea97
- 00ad75d4 ["INT_ADD", "register:40f0:8", ["const:ad75d4:8", "const:4:8"]]
- 00ad75d4 ["CALL", null, ["callee:00566284:8"]]
+ 00ad7618 ["INT_ADD", "register:40f0:8", ["const:ad7618:8", "const:4:8"]]
+ 00ad7618 ["CALL", null, ["callee:00566284:8"]]
- 00ad75d4 bytes 2c3bea97
+ 00ad7618 bytes 1b3bea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f276da54139f8c56450ca5a4fb10b19"></a>

### [`00ad7970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7970.md) → [`00ad79b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad79b4.md) FUN_00ad79b4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008547f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008547f8.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 1件 [`008547f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/008547f8.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.16% / 新版 95.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad79fc",
      "incomplete_value": true,
      "site": "00ad7a18",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:20d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad79b8",
      "incomplete_value": true,
      "site": "00ad79d4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:2a1:8"
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
      "00ad79fc",
      "READ",
      [
        "storage",
        "002af2a1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ad79fc",
      "READ",
      [
        "storage",
        "002af20d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad7a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7970.md#insn-00ad7a18) · [`00ad7994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7970.md#insn-00ad7994) · [`00ad799c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7970.md#insn-00ad799c)
- 新版 [`00ad7a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad79b4.md#insn-00ad7a5c) · [`00ad79d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad79b4.md#insn-00ad79d8) · [`00ad79e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad79b4.md#insn-00ad79e0)

~~~diff
- 00ad7a18 ["INT_ADD", "register:40f0:8", ["const:ad7a18:8", "const:4:8"]]
- 00ad7a18 ["CALL", null, ["callee:0056626c:8"]]
+ 00ad7a5c ["INT_ADD", "register:40f0:8", ["const:ad7a5c:8", "const:4:8"]]
+ 00ad7a5c ["CALL", null, ["callee:0056626c:8"]]
- 00ad7a18 bytes 153aea97
+ 00ad7a5c bytes 043aea97
- 00ad7994 ["INT_ADD", "register:40f0:8", ["const:ad7994:8", "const:4:8"]]
- 00ad7994 ["CALL", null, ["callee:00565f94:8"]]
+ 00ad79d8 ["INT_ADD", "register:40f0:8", ["const:ad79d8:8", "const:4:8"]]
+ 00ad79d8 ["CALL", null, ["callee:00565f94:8"]]
- 00ad7994 bytes 8039ea97
+ 00ad79d8 bytes 6f39ea97
- 00ad799c ["INT_ADD", "register:40f0:8", ["const:ad799c:8", "const:4:8"]]
- 00ad799c ["CALL", null, ["callee:00566284:8"]]
+ 00ad79e0 ["INT_ADD", "register:40f0:8", ["const:ad79e0:8", "const:4:8"]]
+ 00ad79e0 ["CALL", null, ["callee:00566284:8"]]
- 00ad799c bytes 3a3aea97
+ 00ad79e0 bytes 293aea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dd876d1b233f9faa8b4ca362f5806bd"></a>

### [`00ad7bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7bd4.md) → [`00ad7c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7c18.md) FUN_00ad7c18

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008552d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/008552d4.md) [`00858c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858c14.md) · 呼出先 8件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 2件 [`008552d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/008552d4.md) [`00858c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858c14.md) · 呼出先 8件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad7c50",
      "incomplete_value": true,
      "site": "00ad7c60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad7c0c",
      "incomplete_value": true,
      "site": "00ad7c1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cb5:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00ad7c64",
      "incomplete_value": true,
      "site": "00ad7c64",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ad7c20",
      "incomplete_value": true,
      "site": "00ad7c20",
      "value": [
        "LOAD",
        "8",
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
      "00ad7c50",
      "READ",
      [
        "storage",
        "002a3cb5",
        null,
        "string"
      ]
    ],
    [
      "00ad7c58",
      "READ",
      [
        "storage",
        "002a3cc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ad7c50",
      "READ",
      [
        "storage",
        "002a3d40",
        null,
        "string"
      ]
    ],
    [
      "00ad7c58",
      "READ",
      [
        "storage",
        "002a3d4d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad7bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7bd4.md#insn-00ad7bf4) · [`00ad7bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7bd4.md#insn-00ad7bfc) · [`00ad7c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7bd4.md#insn-00ad7c08)
- 新版 [`00ad7c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7c18.md#insn-00ad7c38) · [`00ad7c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7c18.md#insn-00ad7c40) · [`00ad7c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7c18.md#insn-00ad7c4c)

~~~diff
- 00ad7bf4 ["INT_ADD", "register:40f0:8", ["const:ad7bf4:8", "const:4:8"]]
- 00ad7bf4 ["CALL", null, ["callee:00565f94:8"]]
+ 00ad7c38 ["INT_ADD", "register:40f0:8", ["const:ad7c38:8", "const:4:8"]]
+ 00ad7c38 ["CALL", null, ["callee:00565f94:8"]]
- 00ad7bf4 bytes e838ea97
+ 00ad7c38 bytes d738ea97
- 00ad7bfc ["INT_ADD", "register:40f0:8", ["const:ad7bfc:8", "const:4:8"]]
- 00ad7bfc ["CALL", null, ["callee:00566284:8"]]
+ 00ad7c40 ["INT_ADD", "register:40f0:8", ["const:ad7c40:8", "const:4:8"]]
+ 00ad7c40 ["CALL", null, ["callee:00566284:8"]]
- 00ad7bfc bytes a239ea97
+ 00ad7c40 bytes 9139ea97
- 00ad7c08 ["COPY", "tmp:0:8", ["const:cb5:8"]]
- 00ad7c08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ad7c08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ad7c08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ad7c4c ["COPY", "tmp:0:8", ["const:d40:8"]]
+ 00ad7c4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad7c4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad7c4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ad7c08 bytes 29d53291
+ 00ad7c4c bytes 29013591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9177760a8b9bc33b38c0bbe666bbd524"></a>

### [`00ad7d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7d44.md) → [`00ad7d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7d88.md) FUN_00ad7d88

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00856bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856bcc.md) [`008573b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/008573b0.md) [`00858c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858c14.md) · 呼出先 11件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00558fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558fd0.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)
- 新版 呼出元 3件 [`00856bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856bcc.md) [`008573b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/008573b0.md) [`00858c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858c14.md) · 呼出先 11件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00558fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558fd0.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.80% / 新版 93.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad7ed0",
      "incomplete_value": true,
      "site": "00ad7ee0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5d6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad7e8c",
      "incomplete_value": true,
      "site": "00ad7e9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:663:8"
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
      "definition_site": "00ad7ed4",
      "incomplete_value": true,
      "site": "00ad7ef8",
      "value": [
        "LOAD",
        "16",
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
                "const:b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad7e90",
      "incomplete_value": true,
      "site": "00ad7eb4",
      "value": [
        "LOAD",
        "16",
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
                "const:b:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ad7df0",
      "incomplete_value": false,
      "site": "00ad7dfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad7dac",
      "incomplete_value": false,
      "site": "00ad7db8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
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
      "00ad7df0",
      "PARAM",
      [
        "storage",
        "0109fdc0",
        null,
        null
      ]
    ],
    [
      "00ad7e70",
      "PARAM",
      [
        "storage",
        "0109fdf0",
        null,
        null
      ]
    ],
    [
      "00ad7ed0",
      "READ",
      [
        "storage",
        "00299663",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ad7df0",
      "PARAM",
      [
        "storage",
        "0109fe00",
        null,
        null
      ]
    ],
    [
      "00ad7e70",
      "PARAM",
      [
        "storage",
        "0109fe30",
        null,
        null
      ]
    ],
    [
      "00ad7ed0",
      "READ",
      [
        "storage",
        "002995d6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad7db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7d44.md#insn-00ad7db8) · [`00ad7e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7d44.md#insn-00ad7e38) · [`00ad7e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7d44.md#insn-00ad7e70)
- 新版 [`00ad7dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7d88.md#insn-00ad7dfc) · [`00ad7e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7d88.md#insn-00ad7e7c) · [`00ad7eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7d88.md#insn-00ad7eb4)

~~~diff
- 00ad7db8 ["INT_ADD", "register:40f0:8", ["const:ad7db8:8", "const:4:8"]]
- 00ad7db8 ["CALL", null, ["callee:00856594:8"]]
+ 00ad7dfc ["INT_ADD", "register:40f0:8", ["const:ad7dfc:8", "const:4:8"]]
+ 00ad7dfc ["CALL", null, ["callee:00856594:8"]]
- 00ad7db8 bytes f7f9f597
+ 00ad7dfc bytes e6f9f597
- 00ad7e38 ["INT_ADD", "register:40f0:8", ["const:ad7e38:8", "const:4:8"]]
- 00ad7e38 ["CALL", null, ["callee:00558fd0:8"]]
+ 00ad7e7c ["INT_ADD", "register:40f0:8", ["const:ad7e7c:8", "const:4:8"]]
+ 00ad7e7c ["CALL", null, ["callee:00558fd0:8"]]
- 00ad7e38 bytes 6604ea97
+ 00ad7e7c bytes 5504ea97
- 00ad7e70 ["INT_ADD", "register:40f0:8", ["const:ad7e70:8", "const:4:8"]]
- 00ad7e70 ["CALL", null, ["callee:00566284:8"]]
+ 00ad7eb4 ["INT_ADD", "register:40f0:8", ["const:ad7eb4:8", "const:4:8"]]
+ 00ad7eb4 ["CALL", null, ["callee:00566284:8"]]
- 00ad7e70 bytes 0539ea97
+ 00ad7eb4 bytes f438ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-381dd85a1b66370c90ed0690e0bbd590"></a>

### [`00ad7f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7f84.md) → [`00ad7fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7fc8.md) FUN_00ad7fc8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00855450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855450.md) · 呼出先 16件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)
- 新版 呼出元 1件 [`00855450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/00855450.md) · 呼出先 16件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.52% / 新版 97.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad8034",
      "incomplete_value": true,
      "site": "00ad8034",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad7ff0",
      "incomplete_value": true,
      "site": "00ad7ff0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3:8"
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
      "definition_site": "00ad803c",
      "incomplete_value": true,
      "site": "00ad803c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ad7ff8",
      "incomplete_value": true,
      "site": "00ad7ff8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ad81b0",
      "incomplete_value": false,
      "site": "00ad81b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad816c",
      "incomplete_value": false,
      "site": "00ad8174",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "00ad801c",
      "READ",
      [
        "storage",
        "002a7003",
        null,
        "string"
      ]
    ],
    [
      "00ad8024",
      "READ",
      [
        "storage",
        "002a7009",
        null,
        "string"
      ]
    ],
    [
      "00ad81b0",
      "PARAM",
      [
        "storage",
        "0109fe20",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad801c",
      "READ",
      [
        "storage",
        "002a709d",
        null,
        "string"
      ]
    ],
    [
      "00ad8024",
      "READ",
      [
        "storage",
        "002a70a3",
        null,
        "string"
      ]
    ],
    [
      "00ad81b0",
      "PARAM",
      [
        "storage",
        "0109fe60",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad8034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7f84.md#insn-00ad8034) · [`00ad8174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7f84.md#insn-00ad8174) · [`00ad7fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7f84.md#insn-00ad7fc0)
- 新版 [`00ad8078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7fc8.md#insn-00ad8078) · [`00ad81b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7fc8.md#insn-00ad81b8) · [`00ad8004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7fc8.md#insn-00ad8004)

~~~diff
- 00ad8034 ["INT_ADD", "register:40f0:8", ["const:ad8034:8", "const:4:8"]]
- 00ad8034 ["CALL", null, ["callee:00bdb060:8"]]
+ 00ad8078 ["INT_ADD", "register:40f0:8", ["const:ad8078:8", "const:4:8"]]
+ 00ad8078 ["CALL", null, ["callee:00bdb060:8"]]
- 00ad8034 bytes f70b0494
+ 00ad8078 bytes fa0b0494
- 00ad8174 ["INT_ADD", "register:40f0:8", ["const:ad8174:8", "const:4:8"]]
- 00ad8174 ["CALL", null, ["callee:00ad849c:8"]]
+ 00ad81b8 ["INT_ADD", "register:40f0:8", ["const:ad81b8:8", "const:4:8"]]
+ 00ad81b8 ["CALL", null, ["callee:00ad849c:8"]]
- 00ad8174 bytes b9000094
+ 00ad81b8 bytes b9000094
- 00ad7fc0 ["INT_ADD", "register:40f0:8", ["const:ad7fc0:8", "const:4:8"]]
- 00ad7fc0 ["CALL", null, ["callee:00565f94:8"]]
+ 00ad8004 ["INT_ADD", "register:40f0:8", ["const:ad8004:8", "const:4:8"]]
+ 00ad8004 ["CALL", null, ["callee:00565f94:8"]]
- 00ad7fc0 bytes f537ea97
+ 00ad8004 bytes e437ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5c8c5e574c9b398051c99ca0f77ae0a"></a>

### [`00ad867c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad867c.md) → [`00ad86c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad86c0.md) FUN_00ad86c0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00855df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855df0.md) · 呼出先 15件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)
- 新版 呼出元 1件 [`00855df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/00855df0.md) · 呼出先 15件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.21% / 新版 94.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad8710",
      "incomplete_value": true,
      "site": "00ad8720",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ec6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad86cc",
      "incomplete_value": true,
      "site": "00ad86dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e3b:8"
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
      "definition_site": "00ad8714",
      "incomplete_value": true,
      "site": "00ad873c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00ad86d0",
      "incomplete_value": true,
      "site": "00ad86f8",
      "value": [
        "LOAD",
        "16",
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
      "00ad8710",
      "READ",
      [
        "storage",
        "002a0e3b",
        null,
        "string"
      ]
    ],
    [
      "00ad8714",
      "READ",
      [
        "storage",
        "002a0e4a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ad8710",
      "READ",
      [
        "storage",
        "002a0ec6",
        null,
        "string"
      ]
    ],
    [
      "00ad8714",
      "READ",
      [
        "storage",
        "002a0ed5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad86a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad867c.md#insn-00ad86a4) · [`00ad86ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad867c.md#insn-00ad86ac) · [`00ad86b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad867c.md#insn-00ad86b8)
- 新版 [`00ad86e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad86c0.md#insn-00ad86e8) · [`00ad86f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad86c0.md#insn-00ad86f0) · [`00ad86fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad86c0.md#insn-00ad86fc)

~~~diff
- 00ad86a4 ["INT_ADD", "register:40f0:8", ["const:ad86a4:8", "const:4:8"]]
- 00ad86a4 ["CALL", null, ["callee:00565f94:8"]]
+ 00ad86e8 ["INT_ADD", "register:40f0:8", ["const:ad86e8:8", "const:4:8"]]
+ 00ad86e8 ["CALL", null, ["callee:00565f94:8"]]
- 00ad86a4 bytes 3c36ea97
+ 00ad86e8 bytes 2b36ea97
- 00ad86ac ["INT_ADD", "register:40f0:8", ["const:ad86ac:8", "const:4:8"]]
- 00ad86ac ["CALL", null, ["callee:00566284:8"]]
+ 00ad86f0 ["INT_ADD", "register:40f0:8", ["const:ad86f0:8", "const:4:8"]]
+ 00ad86f0 ["CALL", null, ["callee:00566284:8"]]
- 00ad86ac bytes f636ea97
+ 00ad86f0 bytes e536ea97
- 00ad86b8 ["INT_ADD", "register:40f0:8", ["const:ad86b8:8", "const:4:8"]]
- 00ad86b8 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ad86fc ["INT_ADD", "register:40f0:8", ["const:ad86fc:8", "const:4:8"]]
+ 00ad86fc ["CALL", null, ["callee:00bdb040:8"]]
- 00ad86b8 bytes 4e0a0494
+ 00ad86fc bytes 510a0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad5abfe06ae35dcbd3a61455652b65a0"></a>

### [`00ad88e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad88e0.md) → [`00ad8924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8924.md) Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdReady

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md) [`00574054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574054.md) [`0057473c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/0057473c.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00574054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574054.md) [`0057473c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057473c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ad894c",
      "incomplete_value": true,
      "site": "00ad894c",
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
      "definition_site": "00ad8908",
      "incomplete_value": true,
      "site": "00ad8908",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ad89dc",
      "incomplete_value": true,
      "site": "00ad89dc",
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
      "definition_site": "00ad8998",
      "incomplete_value": true,
      "site": "00ad8998",
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00ad8908"
      ],
      [
        "FALL_THROUGH",
        "00ad894c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ad894c",
      "incomplete_value": true,
      "site": "00ad896c",
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
      "definition_site": "00ad8908",
      "incomplete_value": true,
      "site": "00ad8928",
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
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ad8948",
      "READ",
      [
        "storage",
        "0109fde0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad89d8",
      "READ",
      [
        "storage",
        "0109fde0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ad8948",
      "READ",
      [
        "storage",
        "0109fe20",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad89d8",
      "READ",
      [
        "storage",
        "0109fe20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad894c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad88e0.md#insn-00ad894c) · [`00ad8904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad88e0.md#insn-00ad8904) · [`00ad8914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad88e0.md#insn-00ad8914)
- 新版 [`00ad8990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8924.md#insn-00ad8990) · [`00ad8948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8924.md#insn-00ad8948) · [`00ad8958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8924.md#insn-00ad8958)

~~~diff
- 00ad894c ["INT_ADD", "register:40f0:8", ["const:ad894c:8", "const:4:8"]]
- 00ad894c ["CALL", null, ["callee:00bd6e90:8"]]
+ 00ad8990 ["INT_ADD", "register:40f0:8", ["const:ad8990:8", "const:4:8"]]
+ 00ad8990 ["CALL", null, ["callee:00bd6e90:8"]]
- 00ad894c bytes 41f90394
+ 00ad8990 bytes 40f90394
- 00ad8904 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:de0:8"]]
- 00ad8904 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ad8948 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e20:8"]]
+ 00ad8948 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ad8904 bytes a8f246f9
+ 00ad8948 bytes a81247f9
- 00ad8914 ["INT_ADD", "register:40f0:8", ["const:ad8914:8", "const:4:8"]]
- 00ad8914 ["CALL", null, ["callee:00566a7c:8"]]
+ 00ad8958 ["INT_ADD", "register:40f0:8", ["const:ad8958:8", "const:4:8"]]
+ 00ad8958 ["CALL", null, ["callee:00566a7c:8"]]
- 00ad8914 bytes 5a38ea97
+ 00ad8958 bytes 4938ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-443dd61427c1c11690e607bd457bb9fc"></a>

### [`00ad8aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8aac.md) → [`00ad8af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8af0.md) Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdOpened

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md) [`00574054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574054.md) [`0057473c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/0057473c.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00574054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574054.md) [`0057473c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057473c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ad8b18",
      "incomplete_value": true,
      "site": "00ad8b18",
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
      "definition_site": "00ad8ad4",
      "incomplete_value": true,
      "site": "00ad8ad4",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ad8ba8",
      "incomplete_value": true,
      "site": "00ad8ba8",
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
      "definition_site": "00ad8b64",
      "incomplete_value": true,
      "site": "00ad8b64",
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00ad8ad4"
      ],
      [
        "FALL_THROUGH",
        "00ad8b18"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ad8b18",
      "incomplete_value": true,
      "site": "00ad8b38",
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
      "definition_site": "00ad8ad4",
      "incomplete_value": true,
      "site": "00ad8af4",
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
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ad8b14",
      "READ",
      [
        "storage",
        "0109fea0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad8ba4",
      "READ",
      [
        "storage",
        "0109fea0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ad8b14",
      "READ",
      [
        "storage",
        "0109fee0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad8ba4",
      "READ",
      [
        "storage",
        "0109fee0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad8b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8aac.md#insn-00ad8b18) · [`00ad8ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8aac.md#insn-00ad8ad0) · [`00ad8ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8aac.md#insn-00ad8ae0)
- 新版 [`00ad8b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8af0.md#insn-00ad8b5c) · [`00ad8b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8af0.md#insn-00ad8b14) · [`00ad8b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8af0.md#insn-00ad8b24)

~~~diff
- 00ad8b18 ["INT_ADD", "register:40f0:8", ["const:ad8b18:8", "const:4:8"]]
- 00ad8b18 ["CALL", null, ["callee:00bd6e90:8"]]
+ 00ad8b5c ["INT_ADD", "register:40f0:8", ["const:ad8b5c:8", "const:4:8"]]
+ 00ad8b5c ["CALL", null, ["callee:00bd6e90:8"]]
- 00ad8b18 bytes cef80394
+ 00ad8b5c bytes cdf80394
- 00ad8ad0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ea0:8"]]
- 00ad8ad0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ad8b14 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ee0:8"]]
+ 00ad8b14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ad8ad0 bytes a85247f9
+ 00ad8b14 bytes a87247f9
- 00ad8ae0 ["INT_ADD", "register:40f0:8", ["const:ad8ae0:8", "const:4:8"]]
- 00ad8ae0 ["CALL", null, ["callee:00566a7c:8"]]
+ 00ad8b24 ["INT_ADD", "register:40f0:8", ["const:ad8b24:8", "const:4:8"]]
+ 00ad8b24 ["CALL", null, ["callee:00566a7c:8"]]
- 00ad8ae0 bytes e737ea97
+ 00ad8b24 bytes d637ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7a0f310f4d842159c6a8211d68bacb6"></a>

### [`00ad8c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8c5c.md) → [`00ad8ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8ca0.md) Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdShowFailed

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 95.59% / 新版 95.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ad8cd0",
      "incomplete_value": true,
      "site": "00ad8cd0",
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
      "definition_site": "00ad8c8c",
      "incomplete_value": true,
      "site": "00ad8c8c",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ad8c8c"
      ],
      [
        "FALL_THROUGH",
        "00ad8cd0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ad8cd0",
      "incomplete_value": true,
      "site": "00ad8d24",
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
      "definition_site": "00ad8c8c",
      "incomplete_value": true,
      "site": "00ad8ce0",
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
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00ad8c8c"
      ],
      [
        "FALL_THROUGH",
        "00ad8cd0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ad8cd0",
      "incomplete_value": true,
      "site": "00ad8d24",
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
      "definition_site": "00ad8c8c",
      "incomplete_value": true,
      "site": "00ad8ce0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ad8ccc",
      "READ",
      [
        "storage",
        "0109fe40",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad8d1c",
      "READ",
      [
        "storage",
        "0109fe40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ad8ccc",
      "READ",
      [
        "storage",
        "0109fe80",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad8d1c",
      "READ",
      [
        "storage",
        "0109fe80",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad8d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8c5c.md#insn-00ad8d24) · [`00ad8c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8c5c.md#insn-00ad8c88) · [`00ad8ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8c5c.md#insn-00ad8ca8)
- 新版 [`00ad8d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8ca0.md#insn-00ad8d68) · [`00ad8ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8ca0.md#insn-00ad8ccc) · [`00ad8cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8ca0.md#insn-00ad8cec)

~~~diff
- 00ad8d24 ["INT_ADD", "register:40f0:8", ["const:ad8d24:8", "const:4:8"]]
- 00ad8d24 ["CALL", null, ["callee:00bdb060:8"]]
+ 00ad8d68 ["INT_ADD", "register:40f0:8", ["const:ad8d68:8", "const:4:8"]]
+ 00ad8d68 ["CALL", null, ["callee:00bdb060:8"]]
- 00ad8d24 bytes bb080494
+ 00ad8d68 bytes be080494
- 00ad8c88 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:e40:8"]]
- 00ad8c88 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ad8ccc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:e80:8"]]
+ 00ad8ccc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ad8c88 bytes e82247f9
+ 00ad8ccc bytes e84247f9
- 00ad8ca8 ["INT_ADD", "register:40f0:8", ["const:ad8ca8:8", "const:4:8"]]
- 00ad8ca8 ["CALL", null, ["callee:00566a7c:8"]]
+ 00ad8cec ["INT_ADD", "register:40f0:8", ["const:ad8cec:8", "const:4:8"]]
+ 00ad8cec ["CALL", null, ["callee:00566a7c:8"]]
- 00ad8ca8 bytes 7537ea97
+ 00ad8cec bytes 6437ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d97e89faf15243f9a7d62828cb70f05b"></a>

### [`00ad8db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8db4.md) → [`00ad8df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8df8.md) Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdRewarded

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ad8e20",
      "incomplete_value": true,
      "site": "00ad8e20",
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
      "definition_site": "00ad8ddc",
      "incomplete_value": true,
      "site": "00ad8ddc",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ad8ddc"
      ],
      [
        "FALL_THROUGH",
        "00ad8e20"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ad8e20",
      "incomplete_value": true,
      "site": "00ad8e48",
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
      "definition_site": "00ad8ddc",
      "incomplete_value": true,
      "site": "00ad8e04",
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
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ad8e1c",
      "READ",
      [
        "storage",
        "0109fe70",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad8e3c",
      "READ",
      [
        "storage",
        "0109fe70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ad8e1c",
      "READ",
      [
        "storage",
        "0109feb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad8e3c",
      "READ",
      [
        "storage",
        "0109feb0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad8dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8db4.md#insn-00ad8dd8) · [`00ad8dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8db4.md#insn-00ad8dec) · [`00ad8df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8db4.md#insn-00ad8df8)
- 新版 [`00ad8e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8df8.md#insn-00ad8e1c) · [`00ad8e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8df8.md#insn-00ad8e30) · [`00ad8e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8df8.md#insn-00ad8e3c)

~~~diff
- 00ad8dd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e70:8"]]
- 00ad8dd8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ad8e1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:eb0:8"]]
+ 00ad8e1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ad8dd8 bytes 683a47f9
+ 00ad8e1c bytes 685a47f9
- 00ad8dec ["INT_ADD", "register:40f0:8", ["const:ad8dec:8", "const:4:8"]]
- 00ad8dec ["CALL", null, ["callee:00566a7c:8"]]
+ 00ad8e30 ["INT_ADD", "register:40f0:8", ["const:ad8e30:8", "const:4:8"]]
+ 00ad8e30 ["CALL", null, ["callee:00566a7c:8"]]
- 00ad8dec bytes 2437ea97
+ 00ad8e30 bytes 1337ea97
- 00ad8df8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e70:8"]]
- 00ad8df8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ad8e3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:eb0:8"]]
+ 00ad8e3c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00ad8df8 bytes 603a47f9
+ 00ad8e3c bytes 605a47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62e33f0dce5667f0ba2dfa1981177e89"></a>

### [`00ad8e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8e94.md) → [`00ad8ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8ed8.md) Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdClosed

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md) [`00574054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574054.md) [`0057473c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/0057473c.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00574054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574054.md) [`0057473c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057473c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ad8f00",
      "incomplete_value": true,
      "site": "00ad8f00",
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
      "definition_site": "00ad8ebc",
      "incomplete_value": true,
      "site": "00ad8ebc",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ad8f90",
      "incomplete_value": true,
      "site": "00ad8f90",
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
      "definition_site": "00ad8f4c",
      "incomplete_value": true,
      "site": "00ad8f4c",
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00ad8ebc"
      ],
      [
        "FALL_THROUGH",
        "00ad8f00"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ad8f00",
      "incomplete_value": true,
      "site": "00ad8f20",
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
      "definition_site": "00ad8ebc",
      "incomplete_value": true,
      "site": "00ad8edc",
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
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ad8efc",
      "READ",
      [
        "storage",
        "0109fed0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad8f8c",
      "READ",
      [
        "storage",
        "0109fed0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ad8efc",
      "READ",
      [
        "storage",
        "0109ff10",
        null,
        "undefined8"
      ]
    ],
    [
      "00ad8f8c",
      "READ",
      [
        "storage",
        "0109ff10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad8f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8e94.md#insn-00ad8f00) · [`00ad8eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8e94.md#insn-00ad8eb8) · [`00ad8ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8e94.md#insn-00ad8ec8)
- 新版 [`00ad8f44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8ed8.md#insn-00ad8f44) · [`00ad8efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8ed8.md#insn-00ad8efc) · [`00ad8f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8ed8.md#insn-00ad8f0c)

~~~diff
- 00ad8f00 ["INT_ADD", "register:40f0:8", ["const:ad8f00:8", "const:4:8"]]
- 00ad8f00 ["CALL", null, ["callee:00bd6e90:8"]]
+ 00ad8f44 ["INT_ADD", "register:40f0:8", ["const:ad8f44:8", "const:4:8"]]
+ 00ad8f44 ["CALL", null, ["callee:00bd6e90:8"]]
- 00ad8f00 bytes d4f70394
+ 00ad8f44 bytes d3f70394
- 00ad8eb8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ed0:8"]]
- 00ad8eb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ad8efc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:f10:8"]]
+ 00ad8efc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ad8eb8 bytes a86a47f9
+ 00ad8efc bytes a88a47f9
- 00ad8ec8 ["INT_ADD", "register:40f0:8", ["const:ad8ec8:8", "const:4:8"]]
- 00ad8ec8 ["CALL", null, ["callee:00566a7c:8"]]
+ 00ad8f0c ["INT_ADD", "register:40f0:8", ["const:ad8f0c:8", "const:4:8"]]
+ 00ad8f0c ["CALL", null, ["callee:00566a7c:8"]]
- 00ad8ec8 bytes ed36ea97
+ 00ad8f0c bytes dc36ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eee0f1d07d76412f7d707a60f352c4c2"></a>

### [`00ad9044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad9044.md) → [`00ad9088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9088.md) _INIT_264

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00ad7400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7400.md) [`00ad7430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7430.md) [`00ad74b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad74b4.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00ad7444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7444.md) [`00ad7474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7474.md) [`00ad74f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad74f8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

変更の種類 call, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 34.38% / 新版 34.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 7件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ad90b0",
      "incomplete_value": false,
      "site": "00ad90b0",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:dd0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad906c",
      "incomplete_value": false,
      "site": "00ad906c",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:d90:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ad90cc",
      "incomplete_value": false,
      "site": "00ad90cc",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:e00:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad9088",
      "incomplete_value": false,
      "site": "00ad9088",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:dc0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ad90d0",
      "incomplete_value": false,
      "site": "00ad90d0",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:e00:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad908c",
      "incomplete_value": false,
      "site": "00ad908c",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:dc0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:50:8"
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
      "00ad90a0",
      "PARAM",
      [
        "storage",
        "0109fd90",
        null,
        null
      ]
    ],
    [
      "unmatched:00ad9064",
      "PARAM",
      [
        "storage",
        "00ad7400",
        null,
        null
      ]
    ],
    [
      "00ad90ac",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ad90a0",
      "PARAM",
      [
        "storage",
        "0109fdd0",
        null,
        null
      ]
    ],
    [
      "00ad90a8",
      "PARAM",
      [
        "storage",
        "00ad7444",
        null,
        null
      ]
    ],
    [
      "00ad90ac",
      "PARAM",
      [
        "storage",
        "00be5fd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad9070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad9044.md#insn-00ad9070) · [`00ad9090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad9044.md#insn-00ad9090)
- 新版 [`00ad90b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9088.md#insn-00ad90b4)

~~~diff
- 00ad9070 ["INT_ADD", "register:40f0:8", ["const:ad9070:8", "const:4:8"]]
- 00ad9070 ["CALL", null, ["callee:00bdafe0:8"]]
- 00ad9070 bytes c8070494
- 00ad9090 ["INT_ADD", "register:40f0:8", ["const:ad9090:8", "const:4:8"]]
- 00ad9090 ["CALL", null, ["callee:00bdafe0:8"]]
- 00ad9090 bytes c0070494
+ 00ad90b4 ["INT_ADD", "register:40f0:8", ["const:ad90b4:8", "const:4:8"]]
+ 00ad90b4 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00ad90b4 bytes cb070494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2953a205c80cc0f8402d952d9c83f993"></a>

### [`00ad90d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad90d4.md) → [`00ad9118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9118.md) FUN_00ad9118

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0085e130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e130.md) · 呼出先 12件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0085e130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e130.md) · 呼出先 12件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad91f8",
      "incomplete_value": true,
      "site": "00ad91f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:222:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad91b4",
      "incomplete_value": true,
      "site": "00ad91b4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:2b6:8"
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
      "definition_site": "00ad9200",
      "incomplete_value": true,
      "site": "00ad9200",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ad91bc",
      "incomplete_value": true,
      "site": "00ad91bc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ad918c",
      "incomplete_value": false,
      "site": "00ad9198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:f70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad9148",
      "incomplete_value": false,
      "site": "00ad9154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:f30:8"
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
      "00ad918c",
      "PARAM",
      [
        "storage",
        "0109ff30",
        null,
        null
      ]
    ],
    [
      "00ad91e0",
      "READ",
      [
        "storage",
        "002af2b6",
        null,
        "string"
      ]
    ],
    [
      "00ad91e8",
      "READ",
      [
        "storage",
        "002af2bb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ad918c",
      "PARAM",
      [
        "storage",
        "0109ff70",
        null,
        null
      ]
    ],
    [
      "00ad91e0",
      "READ",
      [
        "storage",
        "002af222",
        null,
        "string"
      ]
    ],
    [
      "00ad91e8",
      "READ",
      [
        "storage",
        "002af227",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad9154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad90d4.md#insn-00ad9154) · [`00ad9198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad90d4.md#insn-00ad9198) · [`00ad91f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad90d4.md#insn-00ad91f8)
- 新版 [`00ad9198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9118.md#insn-00ad9198) · [`00ad91dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9118.md#insn-00ad91dc) · [`00ad923c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9118.md#insn-00ad923c)

~~~diff
- 00ad9154 ["INT_ADD", "register:40f0:8", ["const:ad9154:8", "const:4:8"]]
- 00ad9154 ["CALL", null, ["callee:0056c55c:8"]]
+ 00ad9198 ["INT_ADD", "register:40f0:8", ["const:ad9198:8", "const:4:8"]]
+ 00ad9198 ["CALL", null, ["callee:0056c55c:8"]]
- 00ad9154 bytes 024dea97
+ 00ad9198 bytes f14cea97
- 00ad9198 ["COPY", "tmp:0:8", ["const:2b6:8"]]
- 00ad9198 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ad9198 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ad9198 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ad91dc ["COPY", "tmp:0:8", ["const:222:8"]]
+ 00ad91dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad91dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad91dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ad9198 bytes 29d90a91
+ 00ad91dc bytes 29890891
- 00ad91f8 ["INT_ADD", "register:40f0:8", ["const:ad91f8:8", "const:4:8"]]
- 00ad91f8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00ad923c ["INT_ADD", "register:40f0:8", ["const:ad923c:8", "const:4:8"]]
+ 00ad923c ["CALL", null, ["callee:00bdb060:8"]]
- 00ad91f8 bytes 86070494
+ 00ad923c bytes 89070494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ad0177eb1d7b4f341ec58763ff51adb"></a>

### [`00ad943c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad943c.md) → [`00ad9480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9480.md) FUN_00ad9480

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00733548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00733/00733548.md) [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) [`0085e130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e130.md) [`0085fc1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fc1c.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 4件 [`00733548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00733/00733548.md) [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`0085e130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e130.md) [`0085fc1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fc1c.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad94c4",
      "incomplete_value": true,
      "site": "00ad94dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:211:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad9480",
      "incomplete_value": true,
      "site": "00ad9498",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:29e:8"
              ]
            ]
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
      "00ad94c4",
      "READ",
      [
        "storage",
        "0029529e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ad94c4",
      "READ",
      [
        "storage",
        "00295211",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad9460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad943c.md#insn-00ad9460) · [`00ad9468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad943c.md#insn-00ad9468) · [`00ad9474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad943c.md#insn-00ad9474)
- 新版 [`00ad94a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9480.md#insn-00ad94a4) · [`00ad94ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9480.md#insn-00ad94ac) · [`00ad94b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9480.md#insn-00ad94b8)

~~~diff
- 00ad9460 ["INT_ADD", "register:40f0:8", ["const:ad9460:8", "const:4:8"]]
- 00ad9460 ["CALL", null, ["callee:00565f94:8"]]
+ 00ad94a4 ["INT_ADD", "register:40f0:8", ["const:ad94a4:8", "const:4:8"]]
+ 00ad94a4 ["CALL", null, ["callee:00565f94:8"]]
- 00ad9460 bytes cd32ea97
+ 00ad94a4 bytes bc32ea97
- 00ad9468 ["INT_ADD", "register:40f0:8", ["const:ad9468:8", "const:4:8"]]
- 00ad9468 ["CALL", null, ["callee:00566284:8"]]
+ 00ad94ac ["INT_ADD", "register:40f0:8", ["const:ad94ac:8", "const:4:8"]]
+ 00ad94ac ["CALL", null, ["callee:00566284:8"]]
- 00ad9468 bytes 8733ea97
+ 00ad94ac bytes 7633ea97
- 00ad9474 ["COPY", "tmp:0:8", ["const:29e:8"]]
- 00ad9474 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ad9474 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ad9474 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ad94b8 ["COPY", "tmp:0:8", ["const:211:8"]]
+ 00ad94b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad94b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad94b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ad9474 bytes 29790a91
+ 00ad94b8 bytes 29450891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d256bd651e89b3a326ff62939938f7a7"></a>

### [`00ad956c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad956c.md) → [`00ad95b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad95b0.md) FUN_00ad95b0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a3cca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3cca4.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00a3cce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cce8.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.80% / 新版 91.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad95ec",
      "incomplete_value": true,
      "site": "00ad95fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:224:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad95a8",
      "incomplete_value": true,
      "site": "00ad95b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2b1:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00ad9600",
      "incomplete_value": true,
      "site": "00ad9600",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ad95bc",
      "incomplete_value": true,
      "site": "00ad95bc",
      "value": [
        "LOAD",
        "8",
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
      "00ad95ec",
      "READ",
      [
        "storage",
        "002952b1",
        null,
        "string"
      ]
    ],
    [
      "00ad95f4",
      "READ",
      [
        "storage",
        "002952be",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ad95ec",
      "READ",
      [
        "storage",
        "00295224",
        null,
        "string"
      ]
    ],
    [
      "00ad95f4",
      "READ",
      [
        "storage",
        "00295231",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad9590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad956c.md#insn-00ad9590) · [`00ad9598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad956c.md#insn-00ad9598) · [`00ad95a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad956c.md#insn-00ad95a4)
- 新版 [`00ad95d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad95b0.md#insn-00ad95d4) · [`00ad95dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad95b0.md#insn-00ad95dc) · [`00ad95e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad95b0.md#insn-00ad95e8)

~~~diff
- 00ad9590 ["INT_ADD", "register:40f0:8", ["const:ad9590:8", "const:4:8"]]
- 00ad9590 ["CALL", null, ["callee:00565f94:8"]]
+ 00ad95d4 ["INT_ADD", "register:40f0:8", ["const:ad95d4:8", "const:4:8"]]
+ 00ad95d4 ["CALL", null, ["callee:00565f94:8"]]
- 00ad9590 bytes 8132ea97
+ 00ad95d4 bytes 7032ea97
- 00ad9598 ["INT_ADD", "register:40f0:8", ["const:ad9598:8", "const:4:8"]]
- 00ad9598 ["CALL", null, ["callee:00566284:8"]]
+ 00ad95dc ["INT_ADD", "register:40f0:8", ["const:ad95dc:8", "const:4:8"]]
+ 00ad95dc ["CALL", null, ["callee:00566284:8"]]
- 00ad9598 bytes 3b33ea97
+ 00ad95dc bytes 2a33ea97
- 00ad95a4 ["COPY", "tmp:0:8", ["const:2b1:8"]]
- 00ad95a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ad95a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ad95a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ad95e8 ["COPY", "tmp:0:8", ["const:224:8"]]
+ 00ad95e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad95e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad95e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ad95a4 bytes 29c50a91
+ 00ad95e8 bytes 29910891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ca7547037aedb31a26ea06ee2da6892"></a>

### [`00ad97d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad97d0.md) → [`00ad9814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9814.md) FUN_00ad9814

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00860170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860170.md) · 呼出先 12件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00860170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860170.md) · 呼出先 12件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad9860",
      "incomplete_value": true,
      "site": "00ad9870",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad981c",
      "incomplete_value": true,
      "site": "00ad982c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:469:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00ad9864",
      "incomplete_value": true,
      "site": "00ad988c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00ad9820",
      "incomplete_value": true,
      "site": "00ad9848",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad9888",
      "incomplete_value": true,
      "site": "00ad9894",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:57a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad9844",
      "incomplete_value": true,
      "site": "00ad9850",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4ef:8"
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
      "00ad9860",
      "READ",
      [
        "storage",
        "00297469",
        null,
        "string"
      ]
    ],
    [
      "00ad9864",
      "READ",
      [
        "storage",
        "00297473",
        null,
        "string"
      ]
    ],
    [
      "00ad9880",
      "READ",
      [
        "storage",
        "002a34fc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ad9860",
      "READ",
      [
        "storage",
        "002973dc",
        null,
        "string"
      ]
    ],
    [
      "00ad9864",
      "READ",
      [
        "storage",
        "002973e6",
        null,
        "string"
      ]
    ],
    [
      "00ad9880",
      "READ",
      [
        "storage",
        "002a3587",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad9810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad97d0.md#insn-00ad9810) · [`00ad9898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad97d0.md#insn-00ad9898) · [`00ad97f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad97d0.md#insn-00ad97f4)
- 新版 [`00ad9854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9814.md#insn-00ad9854) · [`00ad98dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9814.md#insn-00ad98dc) · [`00ad9838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9814.md#insn-00ad9838)

~~~diff
- 00ad9810 ["COPY", "tmp:0:8", ["const:469:8"]]
- 00ad9810 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ad9810 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ad9810 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ad9854 ["COPY", "tmp:0:8", ["const:3dc:8"]]
+ 00ad9854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ad9854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ad9854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ad9810 bytes 08a51191
+ 00ad9854 bytes 08710f91
- 00ad9898 ["INT_ADD", "register:40f0:8", ["const:ad9898:8", "const:4:8"]]
- 00ad9898 ["CALL", null, ["callee:0056626c:8"]]
+ 00ad98dc ["INT_ADD", "register:40f0:8", ["const:ad98dc:8", "const:4:8"]]
+ 00ad98dc ["CALL", null, ["callee:0056626c:8"]]
- 00ad9898 bytes 7532ea97
+ 00ad98dc bytes 6432ea97
- 00ad97f4 ["INT_ADD", "register:40f0:8", ["const:ad97f4:8", "const:4:8"]]
- 00ad97f4 ["CALL", null, ["callee:00565f94:8"]]
+ 00ad9838 ["INT_ADD", "register:40f0:8", ["const:ad9838:8", "const:4:8"]]
+ 00ad9838 ["CALL", null, ["callee:00565f94:8"]]
- 00ad97f4 bytes e831ea97
+ 00ad9838 bytes d731ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79b43917ab54ef31a7e1d181ff643cbd"></a>

### [`00ad9b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad9b20.md) → [`00ad9b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9b64.md) FUN_00ad9b64

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0085e328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e328.md) · 呼出先 14件 [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)
- 新版 呼出元 1件 [`0085e328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e328.md) · 呼出先 14件 [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.77% / 新版 97.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ad9d00",
      "incomplete_value": false,
      "site": "00ad9d18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad9cbc",
      "incomplete_value": false,
      "site": "00ad9cd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ad9bd0",
      "READ",
      [
        "storage",
        "002a4de8",
        null,
        "string"
      ]
    ],
    [
      "00ad9bd4",
      "READ",
      [
        "storage",
        "002a4df6",
        null,
        "string"
      ]
    ],
    [
      "00ad9d00",
      "PARAM",
      [
        "storage",
        "0109fef8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ad9bd0",
      "READ",
      [
        "storage",
        "002a4e73",
        null,
        "string"
      ]
    ],
    [
      "00ad9bd4",
      "READ",
      [
        "storage",
        "002a4e81",
        null,
        "string"
      ]
    ],
    [
      "00ad9d00",
      "PARAM",
      [
        "storage",
        "0109ff38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad9c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad9b20.md#insn-00ad9c90) · [`00ad9cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad9b20.md#insn-00ad9cd4) · [`00ad9b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad9b20.md#insn-00ad9b54)
- 新版 [`00ad9cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9b64.md#insn-00ad9cd4) · [`00ad9d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9b64.md#insn-00ad9d18) · [`00ad9b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9b64.md#insn-00ad9b98)

~~~diff
- 00ad9c90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad9c90 ["INT_ADD", "register:40f0:8", ["const:ad9c90:8", "const:4:8"]]
- 00ad9c90 ["CALLIND", null, ["register:0:8"]]
+ 00ad9cd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad9cd4 ["INT_ADD", "register:40f0:8", ["const:ad9cd4:8", "const:4:8"]]
+ 00ad9cd4 ["CALLIND", null, ["register:0:8"]]
- 00ad9c90 bytes 00013fd6
+ 00ad9cd4 bytes 00013fd6
- 00ad9cd4 ["INT_ADD", "register:40f0:8", ["const:ad9cd4:8", "const:4:8"]]
- 00ad9cd4 ["CALL", null, ["callee:00adb2ac:8"]]
+ 00ad9d18 ["INT_ADD", "register:40f0:8", ["const:ad9d18:8", "const:4:8"]]
+ 00ad9d18 ["CALL", null, ["callee:00adb2ac:8"]]
- 00ad9cd4 bytes 65050094
+ 00ad9d18 bytes 65050094
- 00ad9b54 ["INT_ADD", "register:40f0:8", ["const:ad9b54:8", "const:4:8"]]
- 00ad9b54 ["CALL", null, ["callee:00565f94:8"]]
+ 00ad9b98 ["INT_ADD", "register:40f0:8", ["const:ad9b98:8", "const:4:8"]]
+ 00ad9b98 ["CALL", null, ["callee:00565f94:8"]]
- 00ad9b54 bytes 1031ea97
+ 00ad9b98 bytes ff30ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-868b40631a3b4167d5efb7f67633fc34"></a>

### [`00ada110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada110.md) → [`00ada154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada154.md) FUN_00ada154

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0085ef84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085ef84.md) · 呼出先 12件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0085ef84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085ef84.md) · 呼出先 12件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.95% / 新版 95.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ada1a8",
      "incomplete_value": true,
      "site": "00ada1c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ada164",
      "incomplete_value": true,
      "site": "00ada184",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e5b:8"
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
      "definition_site": "00ada1cc",
      "incomplete_value": true,
      "site": "00ada1d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:57a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ada188",
      "incomplete_value": true,
      "site": "00ada194",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4ef:8"
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
      "definition_site": "00ada1dc",
      "incomplete_value": true,
      "site": "00ada1dc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ada198",
      "incomplete_value": true,
      "site": "00ada198",
      "value": [
        "LOAD",
        "8",
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
      "00ada1a8",
      "READ",
      [
        "storage",
        "002a0e5b",
        null,
        "string"
      ]
    ],
    [
      "00ada1cc",
      "READ",
      [
        "storage",
        "002a34ef",
        null,
        "string"
      ]
    ],
    [
      "00ada1d0",
      "READ",
      [
        "storage",
        "002a34fc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ada1a8",
      "READ",
      [
        "storage",
        "002a0ee6",
        null,
        "string"
      ]
    ],
    [
      "00ada1cc",
      "READ",
      [
        "storage",
        "002a357a",
        null,
        "string"
      ]
    ],
    [
      "00ada1d0",
      "READ",
      [
        "storage",
        "002a3587",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ada244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada110.md#insn-00ada244) · [`00ada288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada110.md#insn-00ada288) · [`00ada144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada110.md#insn-00ada144)
- 新版 [`00ada288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada154.md#insn-00ada288) · [`00ada2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada154.md#insn-00ada2cc) · [`00ada188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada154.md#insn-00ada188)

~~~diff
- 00ada244 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ada244 ["INT_ADD", "register:40f0:8", ["const:ada244:8", "const:4:8"]]
- 00ada244 ["CALLIND", null, ["register:0:8"]]
+ 00ada288 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ada288 ["INT_ADD", "register:40f0:8", ["const:ada288:8", "const:4:8"]]
+ 00ada288 ["CALLIND", null, ["register:0:8"]]
- 00ada244 bytes 00013fd6
+ 00ada288 bytes 00013fd6
- 00ada288 ["INT_ADD", "register:40f0:8", ["const:ada288:8", "const:4:8"]]
- 00ada288 ["CALL", null, ["callee:00adb5d0:8"]]
+ 00ada2cc ["INT_ADD", "register:40f0:8", ["const:ada2cc:8", "const:4:8"]]
+ 00ada2cc ["CALL", null, ["callee:00adb5d0:8"]]
- 00ada288 bytes c1040094
+ 00ada2cc bytes c1040094
- 00ada144 ["INT_ADD", "register:40f0:8", ["const:ada144:8", "const:4:8"]]
- 00ada144 ["CALL", null, ["callee:00565f94:8"]]
+ 00ada188 ["INT_ADD", "register:40f0:8", ["const:ada188:8", "const:4:8"]]
+ 00ada188 ["CALL", null, ["callee:00565f94:8"]]
- 00ada144 bytes 942fea97
+ 00ada188 bytes 832fea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-366210fb94ed83d842edd2ef92279d5c"></a>

### [`00ada5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada5ac.md) → [`00ada5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada5f0.md) FUN_00ada5f0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`0085e130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e130.md) [`0085fc1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fc1c.md) [`008710cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008710cc.md) [`00879ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879ea8.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 4件 [`0085e130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e130.md) [`0085fc1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fc1c.md) [`008710cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008710cc.md) [`00879ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879ea8.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.93% / 新版 92.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ada63c",
      "incomplete_value": true,
      "site": "00ada648",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ada5f8",
      "incomplete_value": true,
      "site": "00ada604",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ada638",
      "incomplete_value": true,
      "site": "00ada650",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:94:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ada5f4",
      "incomplete_value": true,
      "site": "00ada60c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:121:8"
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
      "definition_site": "00ada6fc",
      "incomplete_value": false,
      "site": "00ada708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ada6b8",
      "incomplete_value": false,
      "site": "00ada6c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:f60:8"
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
      "00ada638",
      "READ",
      [
        "storage",
        "00294121",
        null,
        "string"
      ]
    ],
    [
      "00ada63c",
      "READ",
      [
        "storage",
        "00294131",
        null,
        "string"
      ]
    ],
    [
      "00ada6fc",
      "PARAM",
      [
        "storage",
        "0109ff60",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ada638",
      "READ",
      [
        "storage",
        "00294094",
        null,
        "string"
      ]
    ],
    [
      "00ada63c",
      "READ",
      [
        "storage",
        "002940a4",
        null,
        "string"
      ]
    ],
    [
      "00ada6fc",
      "PARAM",
      [
        "storage",
        "0109ffa0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ada6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada5ac.md#insn-00ada6c4) · [`00ada5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada5ac.md#insn-00ada5d0) · [`00ada5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada5ac.md#insn-00ada5d8)
- 新版 [`00ada708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada5f0.md#insn-00ada708) · [`00ada614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada5f0.md#insn-00ada614) · [`00ada61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada5f0.md#insn-00ada61c)

~~~diff
- 00ada6c4 ["INT_ADD", "register:40f0:8", ["const:ada6c4:8", "const:4:8"]]
- 00ada6c4 ["CALL", null, ["callee:00adb8b8:8"]]
+ 00ada708 ["INT_ADD", "register:40f0:8", ["const:ada708:8", "const:4:8"]]
+ 00ada708 ["CALL", null, ["callee:00adb8b8:8"]]
- 00ada6c4 bytes 6c040094
+ 00ada708 bytes 6c040094
- 00ada5d0 ["INT_ADD", "register:40f0:8", ["const:ada5d0:8", "const:4:8"]]
- 00ada5d0 ["CALL", null, ["callee:00565f94:8"]]
+ 00ada614 ["INT_ADD", "register:40f0:8", ["const:ada614:8", "const:4:8"]]
+ 00ada614 ["CALL", null, ["callee:00565f94:8"]]
- 00ada5d0 bytes 712eea97
+ 00ada614 bytes 602eea97
- 00ada5d8 ["INT_ADD", "register:40f0:8", ["const:ada5d8:8", "const:4:8"]]
- 00ada5d8 ["CALL", null, ["callee:00566284:8"]]
+ 00ada61c ["INT_ADD", "register:40f0:8", ["const:ada61c:8", "const:4:8"]]
+ 00ada61c ["CALL", null, ["callee:00566284:8"]]
- 00ada5d8 bytes 2b2fea97
+ 00ada61c bytes 1a2fea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cba0de9a31d976c362b795d606e74e13"></a>

### [`00ada774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada774.md) → [`00ada7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada7b8.md) FUN_00ada7b8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0085f63c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f63c.md) [`00871208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871208.md) [`00879fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879fe4.md) · 呼出先 9件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 3件 [`0085f63c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f63c.md) [`00871208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871208.md) [`00879fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879fe4.md) · 呼出先 9件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.88% / 新版 95.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ada804",
      "incomplete_value": true,
      "site": "00ada820",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:23a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ada7c0",
      "incomplete_value": true,
      "site": "00ada7dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2c7:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ada8b8",
      "incomplete_value": false,
      "site": "00ada8c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ada874",
      "incomplete_value": false,
      "site": "00ada880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:f90:8"
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
      "00ada804",
      "READ",
      [
        "storage",
        "002952c7",
        null,
        "string"
      ]
    ],
    [
      "00ada8b8",
      "PARAM",
      [
        "storage",
        "0109ff90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ada804",
      "READ",
      [
        "storage",
        "0029523a",
        null,
        "string"
      ]
    ],
    [
      "00ada8b8",
      "PARAM",
      [
        "storage",
        "0109ffd0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ada820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada774.md#insn-00ada820) · [`00ada880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada774.md#insn-00ada880) · [`00ada79c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada774.md#insn-00ada79c)
- 新版 [`00ada864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada7b8.md#insn-00ada864) · [`00ada8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada7b8.md#insn-00ada8c4) · [`00ada7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada7b8.md#insn-00ada7e0)

~~~diff
- 00ada820 ["INT_ADD", "register:40f0:8", ["const:ada820:8", "const:4:8"]]
- 00ada820 ["CALL", null, ["callee:0056626c:8"]]
+ 00ada864 ["INT_ADD", "register:40f0:8", ["const:ada864:8", "const:4:8"]]
+ 00ada864 ["CALL", null, ["callee:0056626c:8"]]
- 00ada820 bytes 932eea97
+ 00ada864 bytes 822eea97
- 00ada880 ["INT_ADD", "register:40f0:8", ["const:ada880:8", "const:4:8"]]
- 00ada880 ["CALL", null, ["callee:00adb8b8:8"]]
+ 00ada8c4 ["INT_ADD", "register:40f0:8", ["const:ada8c4:8", "const:4:8"]]
+ 00ada8c4 ["CALL", null, ["callee:00adb8b8:8"]]
- 00ada880 bytes fd030094
+ 00ada8c4 bytes fd030094
- 00ada79c ["INT_ADD", "register:40f0:8", ["const:ada79c:8", "const:4:8"]]
- 00ada79c ["CALL", null, ["callee:00565f94:8"]]
+ 00ada7e0 ["INT_ADD", "register:40f0:8", ["const:ada7e0:8", "const:4:8"]]
+ 00ada7e0 ["CALL", null, ["callee:00565f94:8"]]
- 00ada79c bytes fe2dea97
+ 00ada7e0 bytes ed2dea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d3a50d30e8929f73dbb6f61a8c573c4"></a>

### [`00ada934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada934.md) → [`00ada978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada978.md) FUN_00ada978

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a9/009a9ce0.md) · 呼出先 9件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 9件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.34% / 新版 96.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ada9d0",
      "incomplete_value": true,
      "site": "00ada9e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:23d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ada98c",
      "incomplete_value": true,
      "site": "00ada9a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2ca:8"
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
      "definition_site": "00ada9d0",
      "incomplete_value": true,
      "site": "00ada9e4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00ada98c",
      "incomplete_value": true,
      "site": "00ada9a0",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ada9d0",
      "READ",
      [
        "storage",
        "002922ca",
        null,
        "string"
      ]
    ],
    [
      "00ada9d0",
      "READ",
      [
        "storage",
        "002922da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ada9d0",
      "READ",
      [
        "storage",
        "0029223d",
        null,
        "string"
      ]
    ],
    [
      "00ada9d0",
      "READ",
      [
        "storage",
        "0029224d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ada95c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada934.md#insn-00ada95c) · [`00ada9e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada934.md#insn-00ada9e4) · [`00ada954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada934.md#insn-00ada954)
- 新版 [`00ada9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada978.md#insn-00ada9a0) · [`00adaa28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada978.md#insn-00adaa28) · [`00ada998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada978.md#insn-00ada998)

~~~diff
- 00ada95c ["INT_ADD", "register:40f0:8", ["const:ada95c:8", "const:4:8"]]
- 00ada95c ["CALL", null, ["callee:00566284:8"]]
+ 00ada9a0 ["INT_ADD", "register:40f0:8", ["const:ada9a0:8", "const:4:8"]]
+ 00ada9a0 ["CALL", null, ["callee:00566284:8"]]
- 00ada95c bytes 4a2eea97
+ 00ada9a0 bytes 392eea97
- 00ada9e4 ["INT_ADD", "register:40f0:8", ["const:ada9e4:8", "const:4:8"]]
- 00ada9e4 ["CALL", null, ["callee:0056626c:8"]]
+ 00adaa28 ["INT_ADD", "register:40f0:8", ["const:adaa28:8", "const:4:8"]]
+ 00adaa28 ["CALL", null, ["callee:0056626c:8"]]
- 00ada9e4 bytes 222eea97
+ 00adaa28 bytes 112eea97
- 00ada954 ["INT_ADD", "register:40f0:8", ["const:ada954:8", "const:4:8"]]
- 00ada954 ["CALL", null, ["callee:00565f94:8"]]
+ 00ada998 ["INT_ADD", "register:40f0:8", ["const:ada998:8", "const:4:8"]]
+ 00ada998 ["CALL", null, ["callee:00565f94:8"]]
- 00ada954 bytes 902dea97
+ 00ada998 bytes 7f2dea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e9b08ed55687ff9312c9fdcb35b8f52"></a>

### [`00adab20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adab20.md) → [`00adab64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adab64.md) Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyGetCurrencyBalance

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00adab8c",
      "incomplete_value": true,
      "site": "00adab8c",
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
      "definition_site": "00adab48",
      "incomplete_value": true,
      "site": "00adab48",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00adaba8",
      "incomplete_value": true,
      "site": "00adaba8",
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
      "definition_site": "00adab64",
      "incomplete_value": true,
      "site": "00adab64",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00adab48"
      ],
      [
        "FALL_THROUGH",
        "00adab8c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00adab8c",
      "incomplete_value": true,
      "site": "00adaba4",
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
      "definition_site": "00adab48",
      "incomplete_value": true,
      "site": "00adab60",
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
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00adab88",
      "READ",
      [
        "storage",
        "0109ff80",
        null,
        "undefined8"
      ]
    ],
    [
      "00adaba0",
      "READ",
      [
        "storage",
        "0109ff80",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00adab88",
      "READ",
      [
        "storage",
        "0109ffc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00adaba0",
      "READ",
      [
        "storage",
        "0109ffc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adab44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adab20.md#insn-00adab44) · [`00adab58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adab20.md#insn-00adab58) · [`00adab5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adab20.md#insn-00adab5c)
- 新版 [`00adab88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adab64.md#insn-00adab88) · [`00adab9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adab64.md#insn-00adab9c) · [`00adaba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adab64.md#insn-00adaba0)

~~~diff
- 00adab44 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:f80:8"]]
- 00adab44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00adab88 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:fc0:8"]]
+ 00adab88 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00adab44 bytes a8c247f9
+ 00adab88 bytes a8e247f9
- 00adab58 ["INT_ADD", "register:40f0:8", ["const:adab58:8", "const:4:8"]]
- 00adab58 ["CALL", null, ["callee:00566a7c:8"]]
+ 00adab9c ["INT_ADD", "register:40f0:8", ["const:adab9c:8", "const:4:8"]]
+ 00adab9c ["CALL", null, ["callee:00566a7c:8"]]
- 00adab58 bytes c92fea97
+ 00adab9c bytes b82fea97
- 00adab5c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:f80:8"]]
- 00adab5c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00adaba0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:fc0:8"]]
+ 00adaba0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00adab5c bytes a0c247f9
+ 00adaba0 bytes a0e247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c417d0928e0b51defe2881e0fbbfc58"></a>

### [`00adabf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adabf4.md) → [`00adac38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adac38.md) Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoySpendCurrency

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00adac60",
      "incomplete_value": true,
      "site": "00adac60",
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
      "definition_site": "00adac1c",
      "incomplete_value": true,
      "site": "00adac1c",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00adac7c",
      "incomplete_value": true,
      "site": "00adac7c",
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
      "definition_site": "00adac38",
      "incomplete_value": true,
      "site": "00adac38",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00adac1c"
      ],
      [
        "FALL_THROUGH",
        "00adac60"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00adac60",
      "incomplete_value": true,
      "site": "00adac78",
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
      "definition_site": "00adac1c",
      "incomplete_value": true,
      "site": "00adac34",
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
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00adac5c",
      "READ",
      [
        "storage",
        "0109ffb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00adac74",
      "READ",
      [
        "storage",
        "0109ffb0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00adac5c",
      "READ",
      [
        "storage",
        "0109fff0",
        null,
        "undefined8"
      ]
    ],
    [
      "00adac74",
      "READ",
      [
        "storage",
        "0109fff0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adac18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adabf4.md#insn-00adac18) · [`00adac2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adabf4.md#insn-00adac2c) · [`00adac30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adabf4.md#insn-00adac30)
- 新版 [`00adac5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adac38.md#insn-00adac5c) · [`00adac70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adac38.md#insn-00adac70) · [`00adac74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adac38.md#insn-00adac74)

~~~diff
- 00adac18 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:fb0:8"]]
- 00adac18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00adac5c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ff0:8"]]
+ 00adac5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00adac18 bytes a8da47f9
+ 00adac5c bytes a8fa47f9
- 00adac2c ["INT_ADD", "register:40f0:8", ["const:adac2c:8", "const:4:8"]]
- 00adac2c ["CALL", null, ["callee:00566a7c:8"]]
+ 00adac70 ["INT_ADD", "register:40f0:8", ["const:adac70:8", "const:4:8"]]
+ 00adac70 ["CALL", null, ["callee:00566a7c:8"]]
- 00adac2c bytes 942fea97
+ 00adac70 bytes 832fea97
- 00adac30 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:fb0:8"]]
- 00adac30 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00adac74 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ff0:8"]]
+ 00adac74 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00adac30 bytes a0da47f9
+ 00adac74 bytes a0fa47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4eaa7dae35d352a7411cf23e577d7f8d"></a>

### [`00adacc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adacc8.md) → [`00adad0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adad0c.md) Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestSuccess

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md) [`00adb9dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb9dc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00adba20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adba20.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00adad38",
      "incomplete_value": false,
      "site": "00adad40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00adacf4",
      "incomplete_value": false,
      "site": "00adacfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
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
      "00adad38",
      "PARAM",
      [
        "storage",
        "0109fef8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00adad38",
      "PARAM",
      [
        "storage",
        "0109ff38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adacfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adacc8.md#insn-00adacfc) · [`00adacec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adacc8.md#insn-00adacec) · [`00adacf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adacc8.md#insn-00adacf4)
- 新版 [`00adad40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adad0c.md#insn-00adad40) · [`00adad30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adad0c.md#insn-00adad30) · [`00adad38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adad0c.md#insn-00adad38)

~~~diff
- 00adacfc ["INT_ADD", "register:40f0:8", ["const:adacfc:8", "const:4:8"]]
- 00adacfc ["CALL", null, ["callee:00adba20:8"]]
+ 00adad40 ["INT_ADD", "register:40f0:8", ["const:adad40:8", "const:4:8"]]
+ 00adad40 ["CALL", null, ["callee:00adba20:8"]]
- 00adacfc bytes 38030094
+ 00adad40 bytes 38030094
- 00adacec ["INT_ADD", "register:40f0:8", ["const:adacec:8", "const:4:8"]]
- 00adacec ["CALL", null, ["callee:00566a7c:8"]]
+ 00adad30 ["INT_ADD", "register:40f0:8", ["const:adad30:8", "const:4:8"]]
+ 00adad30 ["CALL", null, ["callee:00566a7c:8"]]
- 00adacec bytes 642fea97
+ 00adad30 bytes 532fea97
- 00adacf4 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 00adacf4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00adacf4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00adacf4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00adad38 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00adad38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00adad38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00adad38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00adacf4 bytes 00e03b91
+ 00adad38 bytes 00e03c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97daa083f38d3b120a68a0e68a38f60a"></a>

### [`00adad88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adad88.md) → [`00adadcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adadcc.md) Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestFailure

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md) [`00adb9dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb9dc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00adba20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adba20.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00adae28",
      "incomplete_value": true,
      "site": "00adae2c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4000:8"
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
      "definition_site": "00adade4",
      "incomplete_value": true,
      "site": "00adade8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4000:8"
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
      "definition_site": "00adae14",
      "incomplete_value": false,
      "site": "00adae1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00adadd0",
      "incomplete_value": false,
      "site": "00adadd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
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
      "00adae14",
      "PARAM",
      [
        "storage",
        "0109fef8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00adae14",
      "PARAM",
      [
        "storage",
        "0109ff38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adadd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adad88.md#insn-00adadd8) · [`00adadb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adad88.md#insn-00adadb8) · [`00adadc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adad88.md#insn-00adadc8)
- 新版 [`00adae1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adadcc.md#insn-00adae1c) · [`00adadfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adadcc.md#insn-00adadfc) · [`00adae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adadcc.md#insn-00adae0c)

~~~diff
- 00adadd8 ["INT_ADD", "register:40f0:8", ["const:adadd8:8", "const:4:8"]]
- 00adadd8 ["CALL", null, ["callee:00adba20:8"]]
+ 00adae1c ["INT_ADD", "register:40f0:8", ["const:adae1c:8", "const:4:8"]]
+ 00adae1c ["CALL", null, ["callee:00adba20:8"]]
- 00adadd8 bytes 01030094
+ 00adae1c bytes 01030094
- 00adadb8 ["INT_ADD", "register:40f0:8", ["const:adadb8:8", "const:4:8"]]
- 00adadb8 ["CALL", null, ["callee:00566a7c:8"]]
+ 00adadfc ["INT_ADD", "register:40f0:8", ["const:adadfc:8", "const:4:8"]]
+ 00adadfc ["CALL", null, ["callee:00566a7c:8"]]
- 00adadb8 bytes 312fea97
+ 00adadfc bytes 202fea97
- 00adadc8 ["INT_ADD", "register:40f0:8", ["const:adadc8:8", "const:4:8"]]
- 00adadc8 ["CALL", null, ["callee:00566a7c:8"]]
+ 00adae0c ["INT_ADD", "register:40f0:8", ["const:adae0c:8", "const:4:8"]]
+ 00adae0c ["CALL", null, ["callee:00566a7c:8"]]
- 00adadc8 bytes 2d2fea97
+ 00adae0c bytes 1c2fea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03736f0530c6a2ee6b80624069cc2742"></a>

### [`00adae94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adae94.md) → [`00adaed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adaed8.md) Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementContentReady

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md) [`00adb9dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb9dc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00adba20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adba20.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00adaf18",
      "incomplete_value": true,
      "site": "00adaf1c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4000:8"
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
      "definition_site": "00adaed4",
      "incomplete_value": true,
      "site": "00adaed8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4000:8"
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
      "definition_site": "00adaf04",
      "incomplete_value": false,
      "site": "00adaf0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00adaec0",
      "incomplete_value": false,
      "site": "00adaec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
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
      "00adaf04",
      "PARAM",
      [
        "storage",
        "0109fef8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00adaf04",
      "PARAM",
      [
        "storage",
        "0109ff38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adaec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adae94.md#insn-00adaec8) · [`00adaeb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adae94.md#insn-00adaeb8) · [`00adaec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adae94.md#insn-00adaec0)
- 新版 [`00adaf0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adaed8.md#insn-00adaf0c) · [`00adaefc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adaed8.md#insn-00adaefc) · [`00adaf04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adaed8.md#insn-00adaf04)

~~~diff
- 00adaec8 ["INT_ADD", "register:40f0:8", ["const:adaec8:8", "const:4:8"]]
- 00adaec8 ["CALL", null, ["callee:00adba20:8"]]
+ 00adaf0c ["INT_ADD", "register:40f0:8", ["const:adaf0c:8", "const:4:8"]]
+ 00adaf0c ["CALL", null, ["callee:00adba20:8"]]
- 00adaec8 bytes c5020094
+ 00adaf0c bytes c5020094
- 00adaeb8 ["INT_ADD", "register:40f0:8", ["const:adaeb8:8", "const:4:8"]]
- 00adaeb8 ["CALL", null, ["callee:00566a7c:8"]]
+ 00adaefc ["INT_ADD", "register:40f0:8", ["const:adaefc:8", "const:4:8"]]
+ 00adaefc ["CALL", null, ["callee:00566a7c:8"]]
- 00adaeb8 bytes f12eea97
+ 00adaefc bytes e02eea97
- 00adaec0 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 00adaec0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00adaec0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00adaec0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00adaf04 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00adaf04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00adaf04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00adaf04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00adaec0 bytes 00e03b91
+ 00adaf04 bytes 00e03c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5bc3ebea8f517c516c4c44a19793ff3"></a>

### [`00adaf54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adaf54.md) → [`00adaf98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adaf98.md) Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementShown

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md) [`00adbae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adbae0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00adbb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adbb24.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00adafd8",
      "incomplete_value": true,
      "site": "00adafdc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4000:8"
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
      "definition_site": "00adaf94",
      "incomplete_value": true,
      "site": "00adaf98",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4000:8"
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
      "definition_site": "00adafc4",
      "incomplete_value": false,
      "site": "00adafcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00adaf80",
      "incomplete_value": false,
      "site": "00adaf88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:f10:8"
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
      "00adafc4",
      "PARAM",
      [
        "storage",
        "0109ff10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00adafc4",
      "PARAM",
      [
        "storage",
        "0109ff50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adaf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adaf54.md#insn-00adaf88) · [`00adaf78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adaf54.md#insn-00adaf78) · [`00adaf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adaf54.md#insn-00adaf80)
- 新版 [`00adafcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adaf98.md#insn-00adafcc) · [`00adafbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adaf98.md#insn-00adafbc) · [`00adafc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adaf98.md#insn-00adafc4)

~~~diff
- 00adaf88 ["INT_ADD", "register:40f0:8", ["const:adaf88:8", "const:4:8"]]
- 00adaf88 ["CALL", null, ["callee:00adbb24:8"]]
+ 00adafcc ["INT_ADD", "register:40f0:8", ["const:adafcc:8", "const:4:8"]]
+ 00adafcc ["CALL", null, ["callee:00adbb24:8"]]
- 00adaf88 bytes d6020094
+ 00adafcc bytes d6020094
- 00adaf78 ["INT_ADD", "register:40f0:8", ["const:adaf78:8", "const:4:8"]]
- 00adaf78 ["CALL", null, ["callee:00566a7c:8"]]
+ 00adafbc ["INT_ADD", "register:40f0:8", ["const:adafbc:8", "const:4:8"]]
+ 00adafbc ["CALL", null, ["callee:00566a7c:8"]]
- 00adaf78 bytes c12eea97
+ 00adafbc bytes b02eea97
- 00adaf80 ["COPY", "tmp:0:8", ["const:f10:8"]]
- 00adaf80 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00adaf80 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00adaf80 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00adafc4 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 00adafc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00adafc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00adafc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00adaf80 bytes 00403c91
+ 00adafc4 bytes 00403d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a78a290a72c6752dc116dd7fddf98ed6"></a>

### [`00adb014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb014.md) → [`00adb058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb058.md) Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementDismissed

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md) [`00adbae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adbae0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00adbb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adbb24.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00adb098",
      "incomplete_value": true,
      "site": "00adb09c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4000:8"
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
      "definition_site": "00adb054",
      "incomplete_value": true,
      "site": "00adb058",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4000:8"
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
      "definition_site": "00adb084",
      "incomplete_value": false,
      "site": "00adb08c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00adb040",
      "incomplete_value": false,
      "site": "00adb048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:f10:8"
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
      "00adb084",
      "PARAM",
      [
        "storage",
        "0109ff10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00adb084",
      "PARAM",
      [
        "storage",
        "0109ff50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adb048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb014.md#insn-00adb048) · [`00adb038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb014.md#insn-00adb038) · [`00adb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb014.md#insn-00adb040)
- 新版 [`00adb08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb058.md#insn-00adb08c) · [`00adb07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb058.md#insn-00adb07c) · [`00adb084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb058.md#insn-00adb084)

~~~diff
- 00adb048 ["INT_ADD", "register:40f0:8", ["const:adb048:8", "const:4:8"]]
- 00adb048 ["CALL", null, ["callee:00adbb24:8"]]
+ 00adb08c ["INT_ADD", "register:40f0:8", ["const:adb08c:8", "const:4:8"]]
+ 00adb08c ["CALL", null, ["callee:00adbb24:8"]]
- 00adb048 bytes a6020094
+ 00adb08c bytes a6020094
- 00adb038 ["INT_ADD", "register:40f0:8", ["const:adb038:8", "const:4:8"]]
- 00adb038 ["CALL", null, ["callee:00566a7c:8"]]
+ 00adb07c ["INT_ADD", "register:40f0:8", ["const:adb07c:8", "const:4:8"]]
+ 00adb07c ["CALL", null, ["callee:00566a7c:8"]]
- 00adb038 bytes 912eea97
+ 00adb07c bytes 802eea97
- 00adb040 ["COPY", "tmp:0:8", ["const:f10:8"]]
- 00adb040 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00adb040 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00adb040 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00adb084 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 00adb084 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00adb084 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00adb084 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00adb040 bytes 00403c91
+ 00adb084 bytes 00403d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d52ae83f40e7a0fcef65928b7fd11b9b"></a>

### [`00adbbe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adbbe4.md) → [`00adbc28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adbc28.md) _INIT_265

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00569da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/00569da8.md) [`0085e2f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e2f8.md) [`00ad90c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad90c4.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00569da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569da8.md) [`0085e2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e2f8.md) [`00ad9108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9108.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 76.71% / 新版 76.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 8件, `store_value` 7件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00adbc64",
      "incomplete_value": true,
      "site": "00adbc80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00adbc20",
      "incomplete_value": true,
      "site": "00adbc3c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00adbc88",
      "incomplete_value": true,
      "site": "00adbca4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00adbc44",
      "incomplete_value": true,
      "site": "00adbc60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00adbca8",
      "incomplete_value": true,
      "site": "00adbcc4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00adbc64",
      "incomplete_value": true,
      "site": "00adbc80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00adbc64",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00adbc88",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00adbca8",
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
      "00adbc64",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00adbc88",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00adbca8",
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

- 旧版 [`00adbc1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adbbe4.md#insn-00adbc1c) · [`00adbdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adbbe4.md#insn-00adbdfc) · [`00adbe1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adbbe4.md#insn-00adbe1c)
- 新版 [`00adbc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adbc28.md#insn-00adbc60) · [`00adbe40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adbc28.md#insn-00adbe40)

~~~diff
- 00adbc1c ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00adbc1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00adbc1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00adbc1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00adbc60 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00adbc60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00adbc60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00adbc60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00adbc1c bytes 29750b91
+ 00adbc60 bytes 29dd0d91
- 00adbdfc ["INT_ADD", "register:40f0:8", ["const:adbdfc:8", "const:4:8"]]
- 00adbdfc ["CALL", null, ["callee:00bdb060:8"]]
+ 00adbe40 ["INT_ADD", "register:40f0:8", ["const:adbe40:8", "const:4:8"]]
+ 00adbe40 ["CALL", null, ["callee:00bdb060:8"]]
- 00adbdfc bytes 85fc0394
+ 00adbe40 bytes 88fc0394
- 00adbe1c ["INT_ADD", "register:40f0:8", ["const:adbe1c:8", "const:4:8"]]
- 00adbe1c ["CALL", null, ["callee:00bdafe0:8"]]
- 00adbe1c bytes 5dfc0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-386633a70597670d17d847d0482b1ea2"></a>

### [`00adc128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc128.md) → [`00adc16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc16c.md) _INIT_266

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00adc1a8",
      "incomplete_value": true,
      "site": "00adc1c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00adc164",
      "incomplete_value": true,
      "site": "00adc180",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00adc1cc",
      "incomplete_value": true,
      "site": "00adc1e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00adc188",
      "incomplete_value": true,
      "site": "00adc1a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00adc1ec",
      "incomplete_value": true,
      "site": "00adc208",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00adc1a8",
      "incomplete_value": true,
      "site": "00adc1c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00adc1a8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00adc1cc",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00adc1ec",
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
      "00adc1a8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00adc1cc",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00adc1ec",
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

- 旧版 [`00adc160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc128.md#insn-00adc160) · [`00adc35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc128.md#insn-00adc35c) · [`00adc150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc128.md#insn-00adc150)
- 新版 [`00adc1a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc16c.md#insn-00adc1a4) · [`00adc3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc16c.md#insn-00adc3a0) · [`00adc194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc16c.md#insn-00adc194)

~~~diff
- 00adc160 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00adc160 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00adc160 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00adc160 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00adc1a4 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00adc1a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00adc1a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00adc1a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00adc160 bytes 29750b91
+ 00adc1a4 bytes 29dd0d91
- 00adc35c ["INT_ADD", "register:40f0:8", ["const:adc35c:8", "const:4:8"]]
- 00adc35c ["CALL", null, ["callee:00bdafe0:8"]]
+ 00adc3a0 ["INT_ADD", "register:40f0:8", ["const:adc3a0:8", "const:4:8"]]
+ 00adc3a0 ["CALL", null, ["callee:00bdafe0:8"]]
- 00adc35c bytes 0dfb0394
+ 00adc3a0 bytes 10fb0394
- 00adc150 ["COPY", "register:4098:8", ["const:109f000:8"]]
+ 00adc194 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00adc150 bytes 132e00f0
+ 00adc194 bytes 332e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c82e6662929302a2fccb446ac67cf76b"></a>

### [`00adc624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc624.md) → [`00adc668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc668.md) FUN_00adc668

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00adc4c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc4c8.md) [`00adc880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc880.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac28.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb500.md) [`00bdb510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb510.md)
- 新版 呼出元 2件 [`00adc50c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc50c.md) [`00adc8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc8c4.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md) [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.78% / 新版 97.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00adc6b4",
      "incomplete_value": true,
      "site": "00adc6b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00adc670",
      "incomplete_value": true,
      "site": "00adc670",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00adc694",
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
      "00adc694",
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

- 旧版 [`00adc648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc624.md#insn-00adc648) · [`00adc680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc624.md#insn-00adc680) · [`00adc690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc624.md#insn-00adc690)
- 新版 [`00adc68c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc668.md#insn-00adc68c) · [`00adc6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc668.md#insn-00adc6c4) · [`00adc6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc668.md#insn-00adc6d4)

~~~diff
- 00adc648 ["COPY", "tmp:0:8", ["const:a1:8"]]
- 00adc648 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00adc648 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00adc648 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00adc68c ["COPY", "tmp:0:8", ["const:13b:8"]]
+ 00adc68c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00adc68c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00adc68c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00adc648 bytes 4a850291
+ 00adc68c bytes 4aed0491
- 00adc680 ["INT_ADD", "register:40f0:8", ["const:adc680:8", "const:4:8"]]
- 00adc680 ["CALL", null, ["callee:00bdb550:8"]]
+ 00adc6c4 ["INT_ADD", "register:40f0:8", ["const:adc6c4:8", "const:4:8"]]
+ 00adc6c4 ["CALL", null, ["callee:00bdb550:8"]]
- 00adc680 bytes a0fb0394
+ 00adc6c4 bytes a3fb0394
- 00adc690 ["INT_ADD", "register:40f0:8", ["const:adc690:8", "const:4:8"]]
- 00adc690 ["CALL", null, ["callee:00bdb060:8"]]
+ 00adc6d4 ["INT_ADD", "register:40f0:8", ["const:adc6d4:8", "const:4:8"]]
+ 00adc6d4 ["CALL", null, ["callee:00bdb060:8"]]
- 00adc690 bytes 60fa0394
+ 00adc6d4 bytes 63fa0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b2203330672dc0ebbfa476677c18973"></a>

### [`00adcc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adcc94.md) → [`00adccd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adccd8.md) FUN_00adccd8

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 8件 [`0064b18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064b/0064b18c.md) [`00654084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00654/00654084.md) [`00829478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829478.md) [`0089d9f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089d/0089d9f4.md) [`008f2388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f2/008f2388.md) · 呼出先 16件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007f8ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8ecc.md)
- 新版 呼出元 8件 [`0064b18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064b/0064b18c.md) [`00654084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00654/00654084.md) [`00829478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829478.md) [`0089d9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089d/0089d9f4.md) [`008f2388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f2/008f2388.md) · 呼出先 16件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`007f8ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f8ecc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.23% / 新版 89.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_destination` 7件, `store_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00adcd04",
      "incomplete_value": false,
      "site": "00adcd28",
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
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00adccc0",
      "incomplete_value": false,
      "site": "00adcce4",
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
            "const:108:8"
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
      "definition_site": "00adcda4",
      "incomplete_value": true,
      "site": "00adcda4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f5c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00adcd60",
      "incomplete_value": true,
      "site": "00adcd60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed1:8"
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
      "definition_site": "00adcda8",
      "incomplete_value": true,
      "site": "00adcda8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00adcd64",
      "incomplete_value": true,
      "site": "00adcd64",
      "value": [
        "LOAD",
        "8",
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
      "00adcd28",
      "DATA",
      [
        "storage",
        "00bf7108",
        null,
        "pointer"
      ]
    ],
    [
      "00adcd5c",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00adcd98",
      "READ",
      [
        "storage",
        "0029fed1",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00adcd28",
      "DATA",
      [
        "storage",
        "00bf7158",
        null,
        "pointer"
      ]
    ],
    [
      "00adcd5c",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00adcd98",
      "READ",
      [
        "storage",
        "0029ff5c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adcd84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adcc94.md#insn-00adcd84) · [`00adcda4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adcc94.md#insn-00adcda4) · [`00adcff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adcc94.md#insn-00adcff0)
- 新版 [`00adcdc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adccd8.md#insn-00adcdc8) · [`00adcde8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adccd8.md#insn-00adcde8) · [`00add034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adccd8.md#insn-00add034)

~~~diff
- 00adcd84 ["INT_ADD", "register:40f0:8", ["const:adcd84:8", "const:4:8"]]
- 00adcd84 ["CALL", null, ["callee:0045b734:8"]]
+ 00adcdc8 ["INT_ADD", "register:40f0:8", ["const:adcdc8:8", "const:4:8"]]
+ 00adcdc8 ["CALL", null, ["callee:0045b734:8"]]
- 00adcd84 bytes 6cfae597
+ 00adcdc8 bytes 5bfae597
- 00adcda4 ["INT_ADD", "register:40f0:8", ["const:adcda4:8", "const:4:8"]]
- 00adcda4 ["CALL", null, ["callee:00bd6e90:8"]]
+ 00adcde8 ["INT_ADD", "register:40f0:8", ["const:adcde8:8", "const:4:8"]]
+ 00adcde8 ["CALL", null, ["callee:00bd6e90:8"]]
- 00adcda4 bytes 2be80394
+ 00adcde8 bytes 2ae80394
- 00adcff0 ["INT_ADD", "register:40f0:8", ["const:adcff0:8", "const:4:8"]]
- 00adcff0 ["CALL", null, ["callee:0045ba04:8"]]
+ 00add034 ["INT_ADD", "register:40f0:8", ["const:add034:8", "const:4:8"]]
+ 00add034 ["CALL", null, ["callee:0045ba04:8"]]
- 00adcff0 bytes 85fae597
+ 00add034 bytes 74fae597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc3fed9e3cbac54ffb03aaf11f5f9c8d"></a>

### [`00add2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00add/00add2e4.md) → [`00add328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00add/00add328.md) _INIT_267

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00add3a8",
      "incomplete_value": true,
      "site": "00add3c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00add364",
      "incomplete_value": true,
      "site": "00add380",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00add3c8",
      "incomplete_value": true,
      "site": "00add3e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00add384",
      "incomplete_value": true,
      "site": "00add39c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00add3e4",
      "incomplete_value": true,
      "site": "00add400",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00add3a0",
      "incomplete_value": true,
      "site": "00add3bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00add364",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00add388",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00add3a8",
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
      "00add364",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00add388",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00add3a8",
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

- 旧版 [`00add30c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00add/00add2e4.md#insn-00add30c) · [`00add310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00add/00add2e4.md#insn-00add310) · [`00add318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00add/00add2e4.md#insn-00add318)
- 新版 [`00add350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00add/00add328.md#insn-00add350) · [`00add354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00add/00add328.md#insn-00add354)

~~~diff
- 00add30c ["COPY", "register:4098:8", ["const:109f000:8"]]
+ 00add350 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00add30c bytes 132e00d0
+ 00add350 bytes 132e00f0
- 00add310 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 00add310 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00add310 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00add310 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00add354 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 00add354 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00add354 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00add354 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00add310 bytes 73623f91
+ 00add354 bytes 73620091
- 00add318 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00add318 bytes 49beffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-571e9d589fef8c74f6497de00c5ae9db"></a>

### [`00ade2f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade2f4.md) → [`00ade338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade338.md) FUN_00ade338

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00a37688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37688.md) [`00ade990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade990.md) [`00adf6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf6a0.md) · 呼出先 16件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`006c77bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c7/006c77bc.md) [`006fd890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fd890.md) [`006fdbdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fdbdc.md) [`007072cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/007072cc.md)
- 新版 呼出元 3件 [`00a376cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a37/00a376cc.md) [`00ade9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade9d4.md) [`00adf6e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adf6e4.md) · 呼出先 16件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`006c77bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c7/006c77bc.md) [`006fd890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd890.md) [`006fdbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdbdc.md) [`007072cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007072cc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ade388",
      "value": [
        "leaf",
        "ram:ade118:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ade344",
      "value": [
        "leaf",
        "ram:ade0d4:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ade388",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ade0d4"
      ]
    ],
    [
      "00ade468",
      "READ",
      [
        "storage",
        "00c1b838",
        null,
        "pointer"
      ]
    ],
    [
      "00ade468",
      "PARAM",
      [
        "storage",
        "0109e460",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ade388",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ade118"
      ]
    ],
    [
      "00ade468",
      "READ",
      [
        "storage",
        "00c1b888",
        null,
        "pointer"
      ]
    ],
    [
      "00ade468",
      "PARAM",
      [
        "storage",
        "0109e4a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ade344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade2f4.md#insn-00ade344) · [`00ade318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade2f4.md#insn-00ade318) · [`00ade320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade2f4.md#insn-00ade320)
- 新版 [`00ade388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade338.md#insn-00ade388) · [`00ade35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade338.md#insn-00ade35c) · [`00ade364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade338.md#insn-00ade364)

~~~diff
- 00ade344 ["INT_ADD", "register:40f0:8", ["const:ade344:8", "const:4:8"]]
- 00ade344 ["CALL", null, ["ram:ade0d4:8"]]
+ 00ade388 ["INT_ADD", "register:40f0:8", ["const:ade388:8", "const:4:8"]]
+ 00ade388 ["CALL", null, ["ram:ade118:8"]]
- 00ade344 bytes 64ffff97
+ 00ade388 bytes 64ffff97
- 00ade318 ["INT_ADD", "register:40f0:8", ["const:ade318:8", "const:4:8"]]
- 00ade318 ["CALL", null, ["callee:0081f580:8"]]
+ 00ade35c ["INT_ADD", "register:40f0:8", ["const:ade35c:8", "const:4:8"]]
+ 00ade35c ["CALL", null, ["callee:0081f580:8"]]
- 00ade318 bytes 9a04f597
+ 00ade35c bytes 8904f597
- 00ade320 ["INT_ADD", "register:40f0:8", ["const:ade320:8", "const:4:8"]]
- 00ade320 ["CALL", null, ["callee:00ade610:8"]]
+ 00ade364 ["INT_ADD", "register:40f0:8", ["const:ade364:8", "const:4:8"]]
+ 00ade364 ["CALL", null, ["callee:00ade610:8"]]
- 00ade320 bytes ab000094
+ 00ade364 bytes ab000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8ea893c5b1f4686af792ca979f8e586"></a>

### [`00ade6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade6f8.md) → [`00ade73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade73c.md) FUN_00ade73c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 88.51% / 新版 88.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ade77c",
      "incomplete_value": false,
      "site": "00ade788",
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
      "definition_site": "00ade738",
      "incomplete_value": false,
      "site": "00ade744",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ade7a0",
      "incomplete_value": true,
      "site": "00ade7a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:52d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ade75c",
      "incomplete_value": true,
      "site": "00ade75c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5ba:8"
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
      "definition_site": "00ade7a4",
      "incomplete_value": true,
      "site": "00ade7a4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ade760",
      "incomplete_value": true,
      "site": "00ade760",
      "value": [
        "LOAD",
        "8",
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
      "00ade788",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00ade790",
      "READ",
      [
        "storage",
        "002985ba",
        null,
        "string"
      ]
    ],
    [
      "00ade798",
      "READ",
      [
        "storage",
        "002985c1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ade788",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00ade790",
      "READ",
      [
        "storage",
        "0029852d",
        null,
        "string"
      ]
    ],
    [
      "00ade798",
      "READ",
      [
        "storage",
        "00298534",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ade788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade6f8.md#insn-00ade788) · [`00ade7a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade6f8.md#insn-00ade7a4) · [`00ade880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade6f8.md#insn-00ade880)
- 新版 [`00ade7cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade73c.md#insn-00ade7cc) · [`00ade7e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade73c.md#insn-00ade7e8) · [`00ade8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade73c.md#insn-00ade8c4)

~~~diff
- 00ade788 ["INT_ADD", "register:40f0:8", ["const:ade788:8", "const:4:8"]]
- 00ade788 ["CALL", null, ["callee:00bdb060:8"]]
+ 00ade7cc ["INT_ADD", "register:40f0:8", ["const:ade7cc:8", "const:4:8"]]
+ 00ade7cc ["CALL", null, ["callee:00bdb060:8"]]
- 00ade788 bytes 22f20394
+ 00ade7cc bytes 25f20394
- 00ade7a4 ["INT_ADD", "register:40f0:8", ["const:ade7a4:8", "const:4:8"]]
- 00ade7a4 ["CALL", null, ["callee:00419064:8"]]
+ 00ade7e8 ["INT_ADD", "register:40f0:8", ["const:ade7e8:8", "const:4:8"]]
+ 00ade7e8 ["CALL", null, ["callee:00419064:8"]]
- 00ade7a4 bytes 30eae497
+ 00ade7e8 bytes 1feae497
- 00ade880 ["INT_ADD", "register:40f0:8", ["const:ade880:8", "const:4:8"]]
- 00ade880 ["CALL", null, ["callee:00465780:8"]]
+ 00ade8c4 ["INT_ADD", "register:40f0:8", ["const:ade8c4:8", "const:4:8"]]
+ 00ade8c4 ["CALL", null, ["callee:00465780:8"]]
- 00ade880 bytes c01be697
+ 00ade8c4 bytes af1be697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-293d4ad0dbf61b0006fdc90267711491"></a>

### [`00ade990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade990.md) → [`00ade9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade9d4.md) FUN_00ade9d4

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`006525c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00652/006525c0.md) [`00695904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md) [`008f06a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f0/008f06a0.md) · 呼出先 22件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md)
- 新版 呼出元 3件 [`006525c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00652/006525c0.md) [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) [`008f06a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f0/008f06a0.md) · 呼出先 22件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.36% / 新版 99.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00adf484",
      "incomplete_value": false,
      "site": "00adf484",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00adf440",
      "incomplete_value": false,
      "site": "00adf440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "ordinal": 109,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00adf59c",
      "incomplete_value": false,
      "site": "00adf59c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00adf558",
      "incomplete_value": false,
      "site": "00adf558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "ordinal": 118,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00adea28",
      "incomplete_value": true,
      "site": "00adea30",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:890:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ade9e4",
      "incomplete_value": true,
      "site": "00ade9ec",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:840:8"
              ]
            ]
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
      "00adea28",
      "READ",
      [
        "storage",
        "00c1b840",
        null,
        "pointer"
      ]
    ],
    [
      "00adea28",
      "PARAM",
      [
        "storage",
        "0109e478",
        null,
        "undefined1"
      ]
    ],
    [
      "00adf484",
      "DATA",
      [
        "storage",
        "00c0f978",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00adea28",
      "READ",
      [
        "storage",
        "00c1b890",
        null,
        "pointer"
      ]
    ],
    [
      "00adea28",
      "PARAM",
      [
        "storage",
        "0109e4b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00adf484",
      "DATA",
      [
        "storage",
        "00c0f9c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ade9ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade990.md#insn-00ade9ec) · [`00ade9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade990.md#insn-00ade9d4) · [`00ade9e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade990.md#insn-00ade9e4)
- 新版 [`00adea30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade9d4.md#insn-00adea30) · [`00adea18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade9d4.md#insn-00adea18) · [`00adea28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade9d4.md#insn-00adea28)

~~~diff
- 00ade9ec ["INT_ADD", "register:40f0:8", ["const:ade9ec:8", "const:4:8"]]
- 00ade9ec ["CALL", null, ["callee:0084bae8:8"]]
+ 00adea30 ["INT_ADD", "register:40f0:8", ["const:adea30:8", "const:4:8"]]
+ 00adea30 ["CALL", null, ["callee:0084bae8:8"]]
- 00ade9ec bytes 3fb4f597
+ 00adea30 bytes 2eb4f597
- 00ade9d4 ["INT_ADD", "register:40f0:8", ["const:ade9d4:8", "const:4:8"]]
- 00ade9d4 ["CALL", null, ["callee:0081f580:8"]]
+ 00adea18 ["INT_ADD", "register:40f0:8", ["const:adea18:8", "const:4:8"]]
+ 00adea18 ["CALL", null, ["callee:0081f580:8"]]
- 00ade9d4 bytes eb02f597
+ 00adea18 bytes da02f597
- 00ade9e4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:840:8"]]
- 00ade9e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00adea28 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:890:8"]]
+ 00adea28 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ade9e4 bytes 212044f9
+ 00adea28 bytes 214844f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1136eea6a77bfddc2d8eaa7c3ed4a59"></a>

### [`00adf9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf9c0.md) → [`00adfa04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfa04.md) FUN_00adfa04

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00adfa18",
      "incomplete_value": false,
      "site": "00adfa1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00adf9d4",
      "incomplete_value": false,
      "site": "00adf9d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:978:8"
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
      "00adfa1c",
      "DATA",
      [
        "storage",
        "00c0f978",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00adfa1c",
      "DATA",
      [
        "storage",
        "00c0f9c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adf9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf9c0.md#insn-00adf9cc) · [`00adf9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf9c0.md#insn-00adf9d4)
- 新版 [`00adfa10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfa04.md#insn-00adfa10) · [`00adfa18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfa04.md#insn-00adfa18)

~~~diff
- 00adf9cc ["INT_ADD", "register:40f0:8", ["const:adf9cc:8", "const:4:8"]]
- 00adf9cc ["CALL", null, ["callee:00bdb040:8"]]
+ 00adfa10 ["INT_ADD", "register:40f0:8", ["const:adfa10:8", "const:4:8"]]
+ 00adfa10 ["CALL", null, ["callee:00bdb040:8"]]
- 00adf9cc bytes 89ed0394
+ 00adfa10 bytes 8ced0394
- 00adf9d4 ["COPY", "tmp:0:8", ["const:978:8"]]
- 00adf9d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00adf9d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00adf9d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00adfa18 ["COPY", "tmp:0:8", ["const:9c8:8"]]
+ 00adfa18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00adfa18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00adfa18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00adf9d4 bytes 08e12591
+ 00adfa18 bytes 08212791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffe0d41beeb32be7cf1bf7f791169f4d"></a>

### [`00adf9e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf9e4.md) → [`00adfa28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfa28.md) FUN_00adfa28

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00adfa2c",
      "incomplete_value": false,
      "site": "00adfa30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00adf9e8",
      "incomplete_value": false,
      "site": "00adf9ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:978:8"
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
      "00adfa30",
      "DATA",
      [
        "storage",
        "00c0f978",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00adfa30",
      "DATA",
      [
        "storage",
        "00c0f9c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adf9e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf9e4.md#insn-00adf9e8)
- 新版 [`00adfa2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfa28.md#insn-00adfa2c)

~~~diff
- 00adf9e8 ["COPY", "tmp:0:8", ["const:978:8"]]
- 00adf9e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00adf9e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00adf9e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00adfa2c ["COPY", "tmp:0:8", ["const:9c8:8"]]
+ 00adfa2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00adfa2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00adfa2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00adf9e8 bytes 08e12591
+ 00adfa2c bytes 08212791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b5d2977179fa747f0bc5b9ce2f2ff00"></a>

### [`00adfb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adfb44.md) → [`00adfb88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfb88.md) FUN_00adfb88

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00adfbac",
      "incomplete_value": false,
      "site": "00adfbac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00adfb68",
      "incomplete_value": false,
      "site": "00adfb68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
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
      "00adfbac",
      "DATA",
      [
        "storage",
        "00c0f9f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00adfbac",
      "DATA",
      [
        "storage",
        "00c0fa48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adfb58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adfb44.md#insn-00adfb58) · [`00adfb64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adfb44.md#insn-00adfb64)
- 新版 [`00adfb9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfb88.md#insn-00adfb9c) · [`00adfba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfb88.md#insn-00adfba8)

~~~diff
- 00adfb58 ["INT_ADD", "register:40f0:8", ["const:adfb58:8", "const:4:8"]]
- 00adfb58 ["CALL", null, ["callee:00bdb040:8"]]
+ 00adfb9c ["INT_ADD", "register:40f0:8", ["const:adfb9c:8", "const:4:8"]]
+ 00adfb9c ["CALL", null, ["callee:00bdb040:8"]]
- 00adfb58 bytes 26ed0394
+ 00adfb9c bytes 29ed0394
- 00adfb64 ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 00adfb64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00adfb64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00adfb64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00adfba8 ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 00adfba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00adfba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00adfba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00adfb64 bytes 08e12791
+ 00adfba8 bytes 08212991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f0a2f71abce49d1d27fd18df86d903f"></a>

### [`00adfb78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adfb78.md) → [`00adfbbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfbbc.md) FUN_00adfbbc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00adfbc8",
      "incomplete_value": false,
      "site": "00adfbc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00adfb84",
      "incomplete_value": false,
      "site": "00adfb84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
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
      "00adfbc8",
      "DATA",
      [
        "storage",
        "00c0f9f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00adfbc8",
      "DATA",
      [
        "storage",
        "00c0fa48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adfb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adfb78.md#insn-00adfb80)
- 新版 [`00adfbc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfbbc.md#insn-00adfbc4)

~~~diff
- 00adfb80 ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 00adfb80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00adfb80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00adfb80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00adfbc4 ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 00adfbc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00adfbc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00adfbc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00adfb80 bytes 29e12791
+ 00adfbc4 bytes 29212991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ccf8c57a8f54f4114aa86bcce16a9b4"></a>

### [`00adfc9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adfc9c.md) → [`00adfce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfce0.md) _INIT_268

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00adfd40",
      "incomplete_value": true,
      "site": "00adfd5c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00adfcfc",
      "incomplete_value": true,
      "site": "00adfd18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00adfd60",
      "incomplete_value": true,
      "site": "00adfd7c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00adfd1c",
      "incomplete_value": true,
      "site": "00adfd38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00adfd80",
      "incomplete_value": true,
      "site": "00adfd98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00adfd3c",
      "incomplete_value": true,
      "site": "00adfd54",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00adfd1c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00adfd40",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00adfd60",
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
      "00adfd1c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00adfd40",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00adfd60",
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

- 旧版 [`00adfcd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adfc9c.md#insn-00adfcd4) · [`00adfed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adfc9c.md#insn-00adfed0) · [`00adfcc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adfc9c.md#insn-00adfcc4)
- 新版 [`00adfd18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfce0.md#insn-00adfd18) · [`00adff14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfce0.md#insn-00adff14) · [`00adfd08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfce0.md#insn-00adfd08)

~~~diff
- 00adfcd4 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00adfcd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00adfcd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00adfcd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00adfd18 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00adfd18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00adfd18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00adfd18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00adfcd4 bytes 29750b91
+ 00adfd18 bytes 29dd0d91
- 00adfed0 ["INT_ADD", "register:40f0:8", ["const:adfed0:8", "const:4:8"]]
- 00adfed0 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00adff14 ["INT_ADD", "register:40f0:8", ["const:adff14:8", "const:4:8"]]
+ 00adff14 ["CALL", null, ["callee:00bdafe0:8"]]
- 00adfed0 bytes 30ec0394
+ 00adff14 bytes 33ec0394
- 00adfcc4 ["COPY", "register:4098:8", ["const:109f000:8"]]
+ 00adfd08 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00adfcc4 bytes 132e0090
+ 00adfd08 bytes 132e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d451fdeb0238b4db25fc1687af193e8b"></a>

### [`00ae0468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0468.md) → [`00ae04ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04ac.md) _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md) · 呼出先 1件 [`00ae047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md)
- 新版 呼出元 1件 [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md) · 呼出先 1件 [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md)

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
      "definition_site": "00ae04b8",
      "incomplete_value": false,
      "site": "00ae04bc",
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
      "definition_site": "00ae0474",
      "incomplete_value": false,
      "site": "00ae0478",
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
      "00ae04b8",
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
      "00ae04b8",
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

- 旧版 [`00ae0478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0468.md#insn-00ae0478) · [`00ae0474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0468.md#insn-00ae0474)
- 新版 [`00ae04bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04ac.md#insn-00ae04bc) · [`00ae04b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04ac.md#insn-00ae04b8)

~~~diff
- 00ae0478 ["INT_ADD", "register:40f0:8", ["const:ae0478:8", "const:4:8"]]
- 00ae0478 ["CALL", null, ["callee:00ae04c0:8"]]
+ 00ae04bc ["INT_ADD", "register:40f0:8", ["const:ae04bc:8", "const:4:8"]]
+ 00ae04bc ["CALL", null, ["callee:00ae04c0:8"]]
- 00ae0478 bytes 01000094
+ 00ae04bc bytes 01000094
- 00ae0474 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00ae0474 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0474 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0474 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae04b8 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00ae04b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae04b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae04b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae0474 bytes 000c0c91
+ 00ae04b8 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbd9ca2884dfc2880697646f20af1db3"></a>

### [`00ae047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md) → [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) FUN_00ae04c0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 11件 [`00ae0468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0468.md) [`00b4a204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a204.md) [`00b4a418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a418.md) [`00b4a558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a558.md) [`00b4a698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a698.md) · 呼出先 4件 [`00ae04cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae04cc.md) [`00bbae18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbae18.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 11件 [`00ae04ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04ac.md) [`00b4a248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a248.md) [`00b4a45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a45c.md) [`00b4a59c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a59c.md) [`00b4a6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a6dc.md) · 呼出先 4件 [`00ae0510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0510.md) [`00bbae5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbae5c.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae04ec",
      "incomplete_value": true,
      "site": "00ae04f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae04a8",
      "incomplete_value": true,
      "site": "00ae04b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
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
      "definition_site": "00ae04f0",
      "incomplete_value": true,
      "site": "00ae04f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae04ac",
      "incomplete_value": true,
      "site": "00ae04b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d58:8"
              ]
            ]
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
      "00ae04ec",
      "READ",
      [
        "storage",
        "00c1ad50",
        null,
        "pointer"
      ]
    ],
    [
      "00ae04ec",
      "PARAM",
      [
        "storage",
        "00c169e0",
        "_ZTISt12length_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00ae04f0",
      "READ",
      [
        "storage",
        "00c1ad58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ae04ec",
      "READ",
      [
        "storage",
        "00c1ada0",
        null,
        "pointer"
      ]
    ],
    [
      "00ae04ec",
      "PARAM",
      [
        "storage",
        "00c16a30",
        "_ZTISt12length_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00ae04f0",
      "READ",
      [
        "storage",
        "00c1ada8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae04b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md#insn-00ae04b4) · [`00ae0490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md#insn-00ae0490) · [`00ae049c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md#insn-00ae049c)
- 新版 [`00ae04f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md#insn-00ae04f8) · [`00ae04d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md#insn-00ae04d4) · [`00ae04e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md#insn-00ae04e0)

~~~diff
- 00ae04b4 ["INT_ADD", "register:40f0:8", ["const:ae04b4:8", "const:4:8"]]
- 00ae04b4 ["CALL", null, ["callee:00bdb0c0:8"]]
+ 00ae04f8 ["INT_ADD", "register:40f0:8", ["const:ae04f8:8", "const:4:8"]]
+ 00ae04f8 ["CALL", null, ["callee:00bdb0c0:8"]]
- 00ae04b4 bytes efea0394
+ 00ae04f8 bytes f2ea0394
- 00ae0490 ["INT_ADD", "register:40f0:8", ["const:ae0490:8", "const:4:8"]]
- 00ae0490 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00ae04d4 ["INT_ADD", "register:40f0:8", ["const:ae04d4:8", "const:4:8"]]
+ 00ae04d4 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00ae0490 bytes f0ea0394
+ 00ae04d4 bytes f3ea0394
- 00ae049c ["INT_ADD", "register:40f0:8", ["const:ae049c:8", "const:4:8"]]
- 00ae049c ["CALL", null, ["callee:00ae0510:8"]]
+ 00ae04e0 ["INT_ADD", "register:40f0:8", ["const:ae04e0:8", "const:4:8"]]
+ 00ae04e0 ["CALL", null, ["callee:00ae0510:8"]]
- 00ae049c bytes 0c000094
+ 00ae04e0 bytes 0c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c873e648e03da37c5b0258966e0bdf5"></a>

### [`00ae053c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae053c.md) → [`00ae0580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0580.md) FUN_00ae0580

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ae0130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0130.md) · 呼出先 3件 [`00bddaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddaa0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bdde30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde30.md)
- 新版 呼出元 1件 [`00ae0174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0174.md) · 呼出先 3件 [`00bddaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaf0.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bdde80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde80.md)

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
      "definition_site": "00ae058c",
      "incomplete_value": false,
      "site": "00ae0590",
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
            "const:24e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0548",
      "incomplete_value": false,
      "site": "00ae054c",
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
            "const:2db:8"
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
      "00ae058c",
      "PARAM",
      [
        "storage",
        "002952db",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae058c",
      "PARAM",
      [
        "storage",
        "0029524e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae054c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae053c.md#insn-00ae054c) · [`00ae0548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae053c.md#insn-00ae0548) · [`00ae0550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae053c.md#insn-00ae0550)
- 新版 [`00ae0590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0580.md#insn-00ae0590) · [`00ae058c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0580.md#insn-00ae058c) · [`00ae0594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0580.md#insn-00ae0594)

~~~diff
- 00ae054c ["INT_ADD", "register:40f0:8", ["const:ae054c:8", "const:4:8"]]
- 00ae054c ["CALL", null, ["callee:00bdde40:8"]]
+ 00ae0590 ["INT_ADD", "register:40f0:8", ["const:ae0590:8", "const:4:8"]]
+ 00ae0590 ["CALL", null, ["callee:00bdde40:8"]]
- 00ae054c bytes 29f60394
+ 00ae0590 bytes 2cf60394
- 00ae0548 ["COPY", "tmp:0:8", ["const:2db:8"]]
- 00ae0548 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0548 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0548 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae058c ["COPY", "tmp:0:8", ["const:24e:8"]]
+ 00ae058c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae058c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae058c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae0548 bytes 006c0b91
+ 00ae058c bytes 00380991
- 00ae0550 ["INT_ADD", "register:40f0:8", ["const:ae0550:8", "const:4:8"]]
- 00ae0550 ["CALL", null, ["callee:00bdde80:8"]]
+ 00ae0594 ["INT_ADD", "register:40f0:8", ["const:ae0594:8", "const:4:8"]]
+ 00ae0594 ["CALL", null, ["callee:00bdde80:8"]]
- 00ae0550 bytes 38f60394
+ 00ae0594 bytes 3bf60394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-954d3c42928a9766bcf25e772e65fa14"></a>

### [`00ae0568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0568.md) → [`00ae05ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae05ac.md) _INIT_269

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00ae002c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae002c.md) [`00ae0060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0060.md) [`00bddd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd10.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00ae0070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0070.md) [`00ae00a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae00a4.md) [`00bddd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd60.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 41.67% / 新版 41.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 4件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae05cc",
      "incomplete_value": false,
      "site": "00ae05cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0588",
      "incomplete_value": false,
      "site": "00ae0588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ae05cc",
      "incomplete_value": false,
      "site": "00ae05cc",
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
            "const:53d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0588",
      "incomplete_value": false,
      "site": "00ae0588",
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
            "const:5ca:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae05cc",
      "incomplete_value": false,
      "site": "00ae05cc",
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
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:48:8"
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
      "definition_site": "00ae0588",
      "incomplete_value": false,
      "site": "00ae0588",
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
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:8:8"
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
      "00ae05bc",
      "PARAM",
      [
        "storage",
        "010a0008",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae05cc",
      "WRITE",
      [
        "storage",
        "010a0008",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae05cc",
      "DATA",
      [
        "storage",
        "002985ca",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae05bc",
      "PARAM",
      [
        "storage",
        "010a0048",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae05cc",
      "WRITE",
      [
        "storage",
        "010a0048",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae05cc",
      "DATA",
      [
        "storage",
        "0029853d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0568.md#insn-00ae0578) · [`00ae057c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0568.md#insn-00ae057c) · [`00ae0580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0568.md#insn-00ae0580)
- 新版 [`00ae05bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae05ac.md#insn-00ae05bc) · [`00ae05c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae05ac.md#insn-00ae05c0) · [`00ae05c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae05ac.md#insn-00ae05c4)

~~~diff
- 00ae0578 ["COPY", "tmp:0:8", ["const:8:8"]]
- 00ae0578 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0578 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0578 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae05bc ["COPY", "tmp:0:8", ["const:48:8"]]
+ 00ae05bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae05bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae05bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae0578 bytes 00200091
+ 00ae05bc bytes 00200191
- 00ae057c ["COPY", "tmp:0:8", ["const:5ca:8"]]
- 00ae057c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae057c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae057c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae05c0 ["COPY", "tmp:0:8", ["const:53d:8"]]
+ 00ae05c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae05c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae05c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae057c bytes 08291791
+ 00ae05c0 bytes 08f51491
- 00ae0580 ["COPY", "tmp:0:8", ["const:2c:8"]]
- 00ae0580 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ae0580 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ae0580 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ae05c4 ["COPY", "tmp:0:8", ["const:70:8"]]
+ 00ae05c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ae05c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ae05c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ae0580 bytes 29b10091
+ 00ae05c4 bytes 29c10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff45b2ba13ef640d24246359ec37f085"></a>

### [`00ae0598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0598.md) → [`00ae05dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae05dc.md) _ZN8firebase9analytics9analytics19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae0608",
      "incomplete_value": true,
      "site": "00ae0608",
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
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae05c4",
      "incomplete_value": true,
      "site": "00ae05c4",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae05f0",
      "incomplete_value": true,
      "site": "00ae05f0",
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
      "definition_site": "00ae05ac",
      "incomplete_value": true,
      "site": "00ae05ac",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae05fc",
      "incomplete_value": false,
      "site": "00ae0600",
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
            "const:432:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae05b8",
      "incomplete_value": false,
      "site": "00ae05bc",
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
            "const:4bf:8"
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
      "00ae05ec",
      "READ",
      [
        "storage",
        "010a0030",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae05fc",
      "PARAM",
      [
        "storage",
        "002974bf",
        null,
        "string"
      ]
    ],
    [
      "00ae0608",
      "WRITE",
      [
        "storage",
        "010a0030",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae05ec",
      "READ",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae05fc",
      "PARAM",
      [
        "storage",
        "00297432",
        null,
        "string"
      ]
    ],
    [
      "00ae0608",
      "WRITE",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae05bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0598.md#insn-00ae05bc) · [`00ae05c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0598.md#insn-00ae05c4) · [`00ae05a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0598.md#insn-00ae05a8)
- 新版 [`00ae0600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae05dc.md#insn-00ae0600) · [`00ae0608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae05dc.md#insn-00ae0608) · [`00ae05ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae05dc.md#insn-00ae05ec)

~~~diff
- 00ae05bc ["INT_ADD", "register:40f0:8", ["const:ae05bc:8", "const:4:8"]]
- 00ae05bc ["CALL", null, ["callee:00bde090:8"]]
+ 00ae0600 ["INT_ADD", "register:40f0:8", ["const:ae0600:8", "const:4:8"]]
+ 00ae0600 ["CALL", null, ["callee:00bde090:8"]]
- 00ae05bc bytes a1f60394
+ 00ae0600 bytes a4f60394
- 00ae05c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:30:8"]]
- 00ae05c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae0608 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:70:8"]]
+ 00ae0608 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae05c4 bytes 601a00f9
+ 00ae0608 bytes 603a00f9
- 00ae05a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:30:8"]]
- 00ae05a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae05ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:70:8"]]
+ 00ae05ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae05a8 bytes 681a40f9
+ 00ae05ec bytes 683a40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f11f3081976b3ef4bb484ceaee457a2"></a>

### [`00ae05d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae05d8.md) → [`00ae061c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae061c.md) _ZN8firebase9analytics9analytics19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae0648",
      "incomplete_value": true,
      "site": "00ae0648",
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
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0604",
      "incomplete_value": true,
      "site": "00ae0604",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae0630",
      "incomplete_value": true,
      "site": "00ae0630",
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
      "definition_site": "00ae05ec",
      "incomplete_value": true,
      "site": "00ae05ec",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae0638",
      "incomplete_value": false,
      "site": "00ae0640",
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
            "const:432:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae05f4",
      "incomplete_value": false,
      "site": "00ae05fc",
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
            "const:4bf:8"
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
      "00ae062c",
      "READ",
      [
        "storage",
        "010a0030",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0638",
      "PARAM",
      [
        "storage",
        "002974bf",
        null,
        "string"
      ]
    ],
    [
      "00ae0648",
      "WRITE",
      [
        "storage",
        "010a0030",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae062c",
      "READ",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0638",
      "PARAM",
      [
        "storage",
        "00297432",
        null,
        "string"
      ]
    ],
    [
      "00ae0648",
      "WRITE",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae05fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae05d8.md#insn-00ae05fc) · [`00ae0604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae05d8.md#insn-00ae0604) · [`00ae05e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae05d8.md#insn-00ae05e8)
- 新版 [`00ae0640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae061c.md#insn-00ae0640) · [`00ae0648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae061c.md#insn-00ae0648) · [`00ae062c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae061c.md#insn-00ae062c)

~~~diff
- 00ae05fc ["INT_ADD", "register:40f0:8", ["const:ae05fc:8", "const:4:8"]]
- 00ae05fc ["CALL", null, ["callee:00bde090:8"]]
+ 00ae0640 ["INT_ADD", "register:40f0:8", ["const:ae0640:8", "const:4:8"]]
+ 00ae0640 ["CALL", null, ["callee:00bde090:8"]]
- 00ae05fc bytes 91f60394
+ 00ae0640 bytes 94f60394
- 00ae0604 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:30:8"]]
- 00ae0604 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae0648 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:70:8"]]
+ 00ae0648 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0604 bytes 601a00f9
+ 00ae0648 bytes 603a00f9
- 00ae05e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:30:8"]]
- 00ae05e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae062c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:70:8"]]
+ 00ae062c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae05e8 bytes 681a40f9
+ 00ae062c bytes 683a40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca314e9320eccc84259fedd3cfbda994"></a>

### [`00ae0618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0618.md) → [`00ae065c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae065c.md) _ZN8firebase9analytics9analytics10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae068c",
      "incomplete_value": true,
      "site": "00ae068c",
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
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0648",
      "incomplete_value": true,
      "site": "00ae0648",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae0670",
      "incomplete_value": true,
      "site": "00ae0670",
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
      "definition_site": "00ae062c",
      "incomplete_value": true,
      "site": "00ae062c",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae067c",
      "incomplete_value": false,
      "site": "00ae0684",
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
            "const:432:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0638",
      "incomplete_value": false,
      "site": "00ae0640",
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
            "const:4bf:8"
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
      "00ae066c",
      "READ",
      [
        "storage",
        "010a0030",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae067c",
      "PARAM",
      [
        "storage",
        "002974bf",
        null,
        "string"
      ]
    ],
    [
      "00ae068c",
      "WRITE",
      [
        "storage",
        "010a0030",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae066c",
      "READ",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae067c",
      "PARAM",
      [
        "storage",
        "00297432",
        null,
        "string"
      ]
    ],
    [
      "00ae068c",
      "WRITE",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0618.md#insn-00ae0640) · [`00ae0648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0618.md#insn-00ae0648) · [`00ae0628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0618.md#insn-00ae0628)
- 新版 [`00ae0684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae065c.md#insn-00ae0684) · [`00ae068c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae065c.md#insn-00ae068c) · [`00ae066c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae065c.md#insn-00ae066c)

~~~diff
- 00ae0640 ["INT_ADD", "register:40f0:8", ["const:ae0640:8", "const:4:8"]]
- 00ae0640 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae0684 ["INT_ADD", "register:40f0:8", ["const:ae0684:8", "const:4:8"]]
+ 00ae0684 ["CALL", null, ["callee:00bde090:8"]]
- 00ae0640 bytes 80f60394
+ 00ae0684 bytes 83f60394
- 00ae0648 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:30:8"]]
- 00ae0648 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae068c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:70:8"]]
+ 00ae068c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0648 bytes 601a00f9
+ 00ae068c bytes 603a00f9
- 00ae0628 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:30:8"]]
- 00ae0628 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae066c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:70:8"]]
+ 00ae066c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae0628 bytes 681a40f9
+ 00ae066c bytes 683a40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-119f413f0bb774066a3ab980c001baac"></a>

### [`00ae065c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae065c.md) → [`00ae06a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae06a0.md) _ZN8firebase9analytics9analytics10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae06d0",
      "incomplete_value": true,
      "site": "00ae06d0",
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
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae068c",
      "incomplete_value": true,
      "site": "00ae068c",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae06b4",
      "incomplete_value": true,
      "site": "00ae06b4",
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
      "definition_site": "00ae0670",
      "incomplete_value": true,
      "site": "00ae0670",
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
        "00ae0670"
      ],
      [
        "FALL_THROUGH",
        "00ae06b4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae06b4",
      "incomplete_value": true,
      "site": "00ae06d0",
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
      "definition_site": "00ae0670",
      "incomplete_value": true,
      "site": "00ae068c",
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
      "00ae06b0",
      "READ",
      [
        "storage",
        "010a0030",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae06bc",
      "PARAM",
      [
        "storage",
        "002974bf",
        null,
        "string"
      ]
    ],
    [
      "00ae06d0",
      "WRITE",
      [
        "storage",
        "010a0030",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae06b0",
      "READ",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae06bc",
      "PARAM",
      [
        "storage",
        "00297432",
        null,
        "string"
      ]
    ],
    [
      "00ae06d0",
      "WRITE",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae068c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae065c.md#insn-00ae068c) · [`00ae066c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae065c.md#insn-00ae066c) · [`00ae0678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae065c.md#insn-00ae0678)
- 新版 [`00ae06d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae06a0.md#insn-00ae06d0) · [`00ae06b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae06a0.md#insn-00ae06b0) · [`00ae06bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae06a0.md#insn-00ae06bc)

~~~diff
- 00ae068c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:30:8"]]
- 00ae068c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae06d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:70:8"]]
+ 00ae06d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae068c bytes 601a00f9
+ 00ae06d0 bytes 603a00f9
- 00ae066c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:30:8"]]
- 00ae066c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae06b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:70:8"]]
+ 00ae06b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae066c bytes 681a40f9
+ 00ae06b0 bytes 683a40f9
- 00ae0678 ["COPY", "tmp:0:8", ["const:4bf:8"]]
- 00ae0678 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00ae0678 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00ae0678 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00ae06bc ["COPY", "tmp:0:8", ["const:432:8"]]
+ 00ae06bc ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae06bc ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae06bc ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00ae0678 bytes 63fc1291
+ 00ae06bc bytes 63c81091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c6490de98d1bfd09b410009abd2129c"></a>

### [`00ae06ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae06ac.md) → [`00ae06f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae06f0.md) _ZN8firebase9analytics9analytics15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae0748",
      "incomplete_value": true,
      "site": "00ae0748",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0704",
      "incomplete_value": true,
      "site": "00ae0704",
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
            "const:38:8"
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
      "definition_site": "00ae0724",
      "incomplete_value": true,
      "site": "00ae0730",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae06e0",
      "incomplete_value": true,
      "site": "00ae06ec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:30:8"
              ]
            ]
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
      "00ae0704",
      "READ",
      [
        "storage",
        "010a0038",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae0724",
      "READ",
      [
        "storage",
        "010a0030",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0748",
      "WRITE",
      [
        "storage",
        "010a0038",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae0704",
      "READ",
      [
        "storage",
        "010a0078",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae0724",
      "READ",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0748",
      "WRITE",
      [
        "storage",
        "010a0078",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae06c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae06ac.md#insn-00ae06c0) · [`00ae06ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae06ac.md#insn-00ae06ec) · [`00ae0704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae06ac.md#insn-00ae0704)
- 新版 [`00ae0704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae06f0.md#insn-00ae0704) · [`00ae0730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae06f0.md#insn-00ae0730) · [`00ae0748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae06f0.md#insn-00ae0748)

~~~diff
- 00ae06c0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:38:8"]]
- 00ae06c0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae06c0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae0704 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:78:8"]]
+ 00ae0704 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae0704 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae06c0 bytes a8e24039
+ 00ae0704 bytes a8e24139
- 00ae06ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae06ec ["INT_ADD", "register:40f0:8", ["const:ae06ec:8", "const:4:8"]]
- 00ae06ec ["CALLIND", null, ["register:0:8"]]
+ 00ae0730 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae0730 ["INT_ADD", "register:40f0:8", ["const:ae0730:8", "const:4:8"]]
+ 00ae0730 ["CALLIND", null, ["register:0:8"]]
- 00ae06ec bytes 00013fd6
+ 00ae0730 bytes 00013fd6
- 00ae0704 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae0704 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:38:8"]]
- 00ae0704 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae0748 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae0748 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:78:8"]]
+ 00ae0748 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae0704 bytes a0e20039
+ 00ae0748 bytes a0e20139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42c5fdea7dc005179d2c64cf807d9bb3"></a>

### [`00ae0718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0718.md) → [`00ae075c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae075c.md) _ZN8firebase9analytics9analytics12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae0798",
      "incomplete_value": true,
      "site": "00ae0798",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0754",
      "incomplete_value": true,
      "site": "00ae0754",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae07b8",
      "incomplete_value": true,
      "site": "00ae07b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0774",
      "incomplete_value": true,
      "site": "00ae0774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:30:8"
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
      "definition_site": "00ae0774",
      "incomplete_value": true,
      "site": "00ae0774",
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
      "definition_site": "00ae0730",
      "incomplete_value": true,
      "site": "00ae0730",
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
      "00ae0770",
      "READ",
      [
        "storage",
        "010a0030",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae077c",
      "READ",
      [
        "storage",
        "010a0038",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae0798",
      "WRITE",
      [
        "storage",
        "010a0038",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae0770",
      "READ",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae077c",
      "READ",
      [
        "storage",
        "010a0078",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae0798",
      "WRITE",
      [
        "storage",
        "010a0078",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae072c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0718.md#insn-00ae072c) · [`00ae0754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0718.md#insn-00ae0754) · [`00ae0770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0718.md#insn-00ae0770)
- 新版 [`00ae0770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae075c.md#insn-00ae0770) · [`00ae0798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae075c.md#insn-00ae0798) · [`00ae07b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae075c.md#insn-00ae07b4)

~~~diff
- 00ae072c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:30:8"]]
- 00ae072c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae0770 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:70:8"]]
+ 00ae0770 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae072c bytes 811a40f9
+ 00ae0770 bytes 813a40f9
- 00ae0754 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae0754 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae0754 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:38:8"]]
- 00ae0754 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae0798 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae0798 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae0798 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:78:8"]]
+ 00ae0798 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae0754 bytes bfe20039
+ 00ae0798 bytes bfe20139
- 00ae0770 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae0770 ["INT_ADD", "register:40f0:8", ["const:ae0770:8", "const:4:8"]]
- 00ae0770 ["CALLIND", null, ["register:0:8"]]
+ 00ae07b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae07b4 ["INT_ADD", "register:40f0:8", ["const:ae07b4:8", "const:4:8"]]
+ 00ae07b4 ["CALLIND", null, ["register:0:8"]]
- 00ae0770 bytes 00013fd6
+ 00ae07b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fceb2fe1fa5b6611473179e30cd441b"></a>

### [`00ae0788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0788.md) → [`00ae07cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae07cc.md) _ZN8firebase9analytics9analytics14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae080c",
      "incomplete_value": true,
      "site": "00ae080c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae07c8",
      "incomplete_value": true,
      "site": "00ae07c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae07e8",
      "incomplete_value": true,
      "site": "00ae07e8",
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
      "definition_site": "00ae07a4",
      "incomplete_value": true,
      "site": "00ae07a4",
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
        "00ae07a4"
      ],
      [
        "FALL_THROUGH",
        "00ae07e8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae07e8",
      "incomplete_value": true,
      "site": "00ae080c",
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
      "definition_site": "00ae07a4",
      "incomplete_value": true,
      "site": "00ae07c8",
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
    "ordinal": 4,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae07e0",
      "READ",
      [
        "storage",
        "010a0030",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae07f0",
      "PARAM",
      [
        "storage",
        "002974bf",
        null,
        "string"
      ]
    ],
    [
      "00ae080c",
      "WRITE",
      [
        "storage",
        "010a0030",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae07e0",
      "READ",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae07f0",
      "PARAM",
      [
        "storage",
        "00297432",
        null,
        "string"
      ]
    ],
    [
      "00ae080c",
      "WRITE",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae07c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0788.md#insn-00ae07c8) · [`00ae079c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0788.md#insn-00ae079c) · [`00ae07ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0788.md#insn-00ae07ac)
- 新版 [`00ae080c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae07cc.md#insn-00ae080c) · [`00ae07e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae07cc.md#insn-00ae07e0) · [`00ae07f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae07cc.md#insn-00ae07f0)

~~~diff
- 00ae07c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:30:8"]]
- 00ae07c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae080c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:70:8"]]
+ 00ae080c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae07c8 bytes 801a00f9
+ 00ae080c bytes 803a00f9
- 00ae079c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:30:8"]]
- 00ae079c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae07e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:70:8"]]
+ 00ae07e0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae079c bytes 811a40f9
+ 00ae07e0 bytes 813a40f9
- 00ae07ac ["COPY", "tmp:0:8", ["const:4bf:8"]]
- 00ae07ac ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00ae07ac ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00ae07ac ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00ae07f0 ["COPY", "tmp:0:8", ["const:432:8"]]
+ 00ae07f0 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae07f0 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae07f0 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00ae07ac bytes 63fc1291
+ 00ae07f0 bytes 63c81091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcd2711009f50d649787ea36e137ce6a"></a>

### [`00ae07f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae07f8.md) → [`00ae083c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae083c.md) _ZN8firebase9analytics9analytics11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00ae0868",
      "incomplete_value": true,
      "site": "00ae0874",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0824",
      "incomplete_value": true,
      "site": "00ae0830",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
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
      "00ae0858",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae0868",
      "DATA",
      [
        "storage",
        "010a0040",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae0858",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae0868",
      "DATA",
      [
        "storage",
        "010a0080",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae07f8.md#insn-00ae0814) · [`00ae0818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae07f8.md#insn-00ae0818) · [`00ae0820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae07f8.md#insn-00ae0820)
- 新版 [`00ae0858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae083c.md#insn-00ae0858) · [`00ae085c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae083c.md#insn-00ae085c) · [`00ae0864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae083c.md#insn-00ae0864)

~~~diff
- 00ae0814 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae0814 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0814 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0814 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae0858 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae0858 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae0858 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae0858 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae0814 bytes 00501791
+ 00ae0858 bytes 001c1591
- 00ae0818 ["INT_ADD", "register:40f0:8", ["const:ae0818:8", "const:4:8"]]
- 00ae0818 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae085c ["INT_ADD", "register:40f0:8", ["const:ae085c:8", "const:4:8"]]
+ 00ae085c ["CALL", null, ["callee:00bde180:8"]]
- 00ae0818 bytes 46f60394
+ 00ae085c bytes 49f60394
- 00ae0820 ["COPY", "tmp:0:8", ["const:40:8"]]
- 00ae0820 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae0820 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae0820 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae0864 ["COPY", "tmp:0:8", ["const:80:8"]]
+ 00ae0864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae0864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae0864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae0820 bytes 08010191
+ 00ae0864 bytes 08010291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

