# v15.7.3 → v15.7.4 · 最優先の変更候補 (79)

[一覧の目次](README.md)

<a id="compare-9c09ed87c74d11f6c3f6c2d4ef994e85"></a>

### [`00bc65c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc65c0.md) → [`00bc6604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6604.md) FUN_00bc6604

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

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
      "definition_site": "00bc666c",
      "incomplete_value": false,
      "site": "00bc666c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc6628",
      "incomplete_value": false,
      "site": "00bc6628",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "00bc666c",
      "DATA",
      [
        "storage",
        "00c18be8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc666c",
      "DATA",
      [
        "storage",
        "00c18c38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc65f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc65c0.md#insn-00bc65f8) · [`00bc661c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc65c0.md#insn-00bc661c) · [`00bc6668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc65c0.md#insn-00bc6668)
- 新版 [`00bc663c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6604.md#insn-00bc663c) · [`00bc6660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6604.md#insn-00bc6660) · [`00bc66ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6604.md#insn-00bc66ac)

~~~diff
- 00bc65f8 ["INT_ADD", "register:40f0:8", ["const:bc65f8:8", "const:4:8"]]
- 00bc65f8 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc663c ["INT_ADD", "register:40f0:8", ["const:bc663c:8", "const:4:8"]]
+ 00bc663c ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc65f8 bytes e25a0094
+ 00bc663c bytes e55a0094
- 00bc661c ["COPY", "tmp:0:8", ["const:be8:8"]]
- 00bc661c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc661c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc661c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc6660 ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 00bc6660 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc6660 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc6660 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc661c bytes 08a12f91
+ 00bc6660 bytes 08e13091
- 00bc6668 ["INT_ADD", "register:40f0:8", ["const:bc6668:8", "const:4:8"]]
- 00bc6668 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc66ac ["INT_ADD", "register:40f0:8", ["const:bc66ac:8", "const:4:8"]]
+ 00bc66ac ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc6668 bytes c6520094
+ 00bc66ac bytes c9520094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d8fcdf4565859e0673ddafdc6f94991"></a>

### [`00bc666c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc666c.md) → [`00bc66b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc66b0.md) FUN_00bc66b0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 3件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

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
      "definition_site": "00bc671c",
      "incomplete_value": false,
      "site": "00bc671c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc66d8",
      "incomplete_value": false,
      "site": "00bc66d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "00bc671c",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc671c",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc66a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc666c.md#insn-00bc66a0) · [`00bc66c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc666c.md#insn-00bc66c8) · [`00bc66d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc666c.md#insn-00bc66d0)
- 新版 [`00bc66e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc66b0.md#insn-00bc66e4) · [`00bc670c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc66b0.md#insn-00bc670c) · [`00bc6714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc66b0.md#insn-00bc6714)

~~~diff
- 00bc66a0 ["INT_ADD", "register:40f0:8", ["const:bc66a0:8", "const:4:8"]]
- 00bc66a0 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc66e4 ["INT_ADD", "register:40f0:8", ["const:bc66e4:8", "const:4:8"]]
+ 00bc66e4 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc66a0 bytes b85a0094
+ 00bc66e4 bytes bb5a0094
- 00bc66c8 ["INT_ADD", "register:40f0:8", ["const:bc66c8:8", "const:4:8"]]
- 00bc66c8 ["CALL", null, ["callee:00bdb190:8"]]
+ 00bc670c ["INT_ADD", "register:40f0:8", ["const:bc670c:8", "const:4:8"]]
+ 00bc670c ["CALL", null, ["callee:00bdb190:8"]]
- 00bc66c8 bytes 9e520094
+ 00bc670c bytes a1520094
- 00bc66d0 ["COPY", "tmp:0:8", ["const:848:8"]]
- 00bc66d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bc66d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bc66d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bc6714 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00bc6714 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc6714 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc6714 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bc66d0 bytes 29212191
+ 00bc6714 bytes 29612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff6072735a4ed99de2481124dc2cf32f"></a>

### [`00bc6718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6718.md) → [`00bc675c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc675c.md) FUN_00bc675c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc67c0",
      "incomplete_value": true,
      "site": "00bc67c0",
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
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc677c",
      "incomplete_value": true,
      "site": "00bc677c",
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
            "const:fd8:8"
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
      "00bc67c0",
      "DATA",
      [
        "storage",
        "00c18fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc67c0",
      "DATA",
      [
        "storage",
        "00c19028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc674c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6718.md#insn-00bc674c) · [`00bc676c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6718.md#insn-00bc676c) · [`00bc6770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6718.md#insn-00bc6770)
- 新版 [`00bc6790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc675c.md#insn-00bc6790) · [`00bc67b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc675c.md#insn-00bc67b0) · [`00bc67b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc675c.md#insn-00bc67b4)

~~~diff
- 00bc674c ["INT_ADD", "register:40f0:8", ["const:bc674c:8", "const:4:8"]]
- 00bc674c ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc6790 ["INT_ADD", "register:40f0:8", ["const:bc6790:8", "const:4:8"]]
+ 00bc6790 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc674c bytes 8d5a0094
+ 00bc6790 bytes 905a0094
- 00bc676c ["COPY", "register:4040:8", ["const:c18000:8"]]
+ 00bc67b0 ["COPY", "register:4040:8", ["const:c19000:8"]]
- 00bc676c bytes 880200d0
+ 00bc67b0 bytes 880200f0
- 00bc6770 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 00bc6770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc6770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc6770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc67b4 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 00bc67b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc67b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc67b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc6770 bytes 08613f91
+ 00bc67b4 bytes 08a10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18f7911902fe1d0eca8842c1b0cd78bb"></a>

### [`00bc67b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc67b8.md) → [`00bc67fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc67fc.md) FUN_00bc67fc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 7件 [`00bc10fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc10fc.md) [`00bc1710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1710.md) [`00bc1be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1be0.md) [`00bce774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce774.md) [`00bce8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce8f8.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 7件 [`00bc1140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1140.md) [`00bc1754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1754.md) [`00bc1c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1c24.md) [`00bce7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce7b8.md) [`00bce93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce93c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.58% / 新版 97.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc68d0",
      "incomplete_value": false,
      "site": "00bc68d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc688c",
      "incomplete_value": false,
      "site": "00bc688c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "definition_site": "00bc6bd0",
      "incomplete_value": false,
      "site": "00bc6bd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc6b8c",
      "incomplete_value": false,
      "site": "00bc6b8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc6ca0",
      "incomplete_value": false,
      "site": "00bc6ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc6c5c",
      "incomplete_value": false,
      "site": "00bc6c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "ordinal": 71,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc68d0",
      "DATA",
      [
        "storage",
        "00c19208",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc6a04",
      "DATA",
      [
        "storage",
        "00c19748",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc6a48",
      "DATA",
      [
        "storage",
        "00c19048",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc68d0",
      "DATA",
      [
        "storage",
        "00c19258",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc6a04",
      "DATA",
      [
        "storage",
        "00c19798",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc6a48",
      "DATA",
      [
        "storage",
        "00c19098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc6830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc67b8.md#insn-00bc6830) · [`00bc6858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc67b8.md#insn-00bc6858) · [`00bc6880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc67b8.md#insn-00bc6880)
- 新版 [`00bc6874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc67fc.md#insn-00bc6874) · [`00bc689c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc67fc.md#insn-00bc689c) · [`00bc68c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc67fc.md#insn-00bc68c4)

~~~diff
- 00bc6830 ["INT_ADD", "register:40f0:8", ["const:bc6830:8", "const:4:8"]]
- 00bc6830 ["CALL", null, ["callee:00bce93c:8"]]
+ 00bc6874 ["INT_ADD", "register:40f0:8", ["const:bc6874:8", "const:4:8"]]
+ 00bc6874 ["CALL", null, ["callee:00bce93c:8"]]
- 00bc6830 bytes 32200094
+ 00bc6874 bytes 32200094
- 00bc6858 ["INT_ADD", "register:40f0:8", ["const:bc6858:8", "const:4:8"]]
- 00bc6858 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc689c ["INT_ADD", "register:40f0:8", ["const:bc689c:8", "const:4:8"]]
+ 00bc689c ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc6858 bytes 4a5a0094
+ 00bc689c bytes 4d5a0094
- 00bc6880 ["COPY", "tmp:0:8", ["const:208:8"]]
- 00bc6880 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bc6880 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bc6880 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bc68c4 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 00bc68c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00bc68c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00bc68c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bc6880 bytes 4a210891
+ 00bc68c4 bytes 4a610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e2b28f311af22fb47c0619a6db8264a"></a>

### [`00bc6e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6e2c.md) → [`00bc6e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6e70.md) FUN_00bc6e70

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc6ee4",
      "incomplete_value": false,
      "site": "00bc6ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc6ea0",
      "incomplete_value": false,
      "site": "00bc6ea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc6ee4",
      "DATA",
      [
        "storage",
        "00c17d78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc6ee4",
      "DATA",
      [
        "storage",
        "00c17dc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc6e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6e2c.md#insn-00bc6e70) · [`00bc6e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6e2c.md#insn-00bc6e94) · [`00bc6ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6e2c.md#insn-00bc6ef4)
- 新版 [`00bc6eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6e70.md#insn-00bc6eb4) · [`00bc6ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6e70.md#insn-00bc6ed8) · [`00bc6f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6e70.md#insn-00bc6f38)

~~~diff
- 00bc6e70 ["INT_ADD", "register:40f0:8", ["const:bc6e70:8", "const:4:8"]]
- 00bc6e70 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc6eb4 ["INT_ADD", "register:40f0:8", ["const:bc6eb4:8", "const:4:8"]]
+ 00bc6eb4 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc6e70 bytes c4580094
+ 00bc6eb4 bytes c7580094
- 00bc6e94 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 00bc6e94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc6e94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc6e94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc6ed8 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 00bc6ed8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc6ed8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc6ed8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc6e94 bytes 08e13591
+ 00bc6ed8 bytes 08213791
- 00bc6ef4 ["INT_ADD", "register:40f0:8", ["const:bc6ef4:8", "const:4:8"]]
- 00bc6ef4 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc6f38 ["INT_ADD", "register:40f0:8", ["const:bc6f38:8", "const:4:8"]]
+ 00bc6f38 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc6ef4 bytes a3500094
+ 00bc6f38 bytes a6500094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6472a7a702e85094b4701d435fa96c5"></a>

### [`00bc740c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc740c.md) → [`00bc7450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7450.md) FUN_00bc7450

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc74c0",
      "incomplete_value": false,
      "site": "00bc74c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc747c",
      "incomplete_value": false,
      "site": "00bc747c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:de8:8"
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
      "00bc74c0",
      "DATA",
      [
        "storage",
        "00c17de8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc74c0",
      "DATA",
      [
        "storage",
        "00c17e38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc744c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc740c.md#insn-00bc744c) · [`00bc7470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc740c.md#insn-00bc7470) · [`00bc74c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc740c.md#insn-00bc74c8)
- 新版 [`00bc7490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7450.md#insn-00bc7490) · [`00bc74b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7450.md#insn-00bc74b4) · [`00bc750c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7450.md#insn-00bc750c)

~~~diff
- 00bc744c ["INT_ADD", "register:40f0:8", ["const:bc744c:8", "const:4:8"]]
- 00bc744c ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc7490 ["INT_ADD", "register:40f0:8", ["const:bc7490:8", "const:4:8"]]
+ 00bc7490 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc744c bytes 4d570094
+ 00bc7490 bytes 50570094
- 00bc7470 ["COPY", "tmp:0:8", ["const:de8:8"]]
- 00bc7470 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc7470 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc7470 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc74b4 ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 00bc74b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc74b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc74b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc7470 bytes 08a13791
+ 00bc74b4 bytes 08e13891
- 00bc74c8 ["INT_ADD", "register:40f0:8", ["const:bc74c8:8", "const:4:8"]]
- 00bc74c8 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc750c ["INT_ADD", "register:40f0:8", ["const:bc750c:8", "const:4:8"]]
+ 00bc750c ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc74c8 bytes 2e4f0094
+ 00bc750c bytes 314f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05c1f07b4a9d3d3444b62213672b99be"></a>

### [`00bc9384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9384.md) → [`00bc93c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc93c8.md) FUN_00bc93c8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md) · 呼出先 3件 [`00bbdcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdcd8.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) · 呼出先 3件 [`00bbdd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdd1c.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc9470",
      "incomplete_value": false,
      "site": "00bc9470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc942c",
      "incomplete_value": false,
      "site": "00bc942c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:2b8:8"
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
      "00bc9470",
      "DATA",
      [
        "storage",
        "00c182b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc9470",
      "DATA",
      [
        "storage",
        "00c18308",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc93ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9384.md#insn-00bc93ac) · [`00bc93f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9384.md#insn-00bc93f4) · [`00bc9428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9384.md#insn-00bc9428)
- 新版 [`00bc93f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc93c8.md#insn-00bc93f0) · [`00bc9438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc93c8.md#insn-00bc9438) · [`00bc946c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc93c8.md#insn-00bc946c)

~~~diff
- 00bc93ac ["INT_ADD", "register:40f0:8", ["const:bc93ac:8", "const:4:8"]]
- 00bc93ac ["CALL", null, ["callee:00bbdd1c:8"]]
+ 00bc93f0 ["INT_ADD", "register:40f0:8", ["const:bc93f0:8", "const:4:8"]]
+ 00bc93f0 ["CALL", null, ["callee:00bbdd1c:8"]]
- 00bc93ac bytes 4bd2ff97
+ 00bc93f0 bytes 4bd2ff97
- 00bc93f4 ["INT_ADD", "register:40f0:8", ["const:bc93f4:8", "const:4:8"]]
- 00bc93f4 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc9438 ["INT_ADD", "register:40f0:8", ["const:bc9438:8", "const:4:8"]]
+ 00bc9438 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc93f4 bytes 634f0094
+ 00bc9438 bytes 664f0094
- 00bc9428 ["COPY", "tmp:0:8", ["const:2b8:8"]]
- 00bc9428 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bc9428 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bc9428 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bc946c ["COPY", "tmp:0:8", ["const:308:8"]]
+ 00bc946c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc946c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc946c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bc9428 bytes 29e10a91
+ 00bc946c bytes 29210c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b715ba93112b130ac4f35e569c277ab3"></a>

### [`00bc9478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9478.md) → [`00bc94bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc94bc.md) FUN_00bc94bc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc952c",
      "incomplete_value": false,
      "site": "00bc9538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc94e8",
      "incomplete_value": false,
      "site": "00bc94f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "00bc9538",
      "DATA",
      [
        "storage",
        "00c18328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc9538",
      "DATA",
      [
        "storage",
        "00c18378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc94ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9478.md#insn-00bc94ac) · [`00bc94e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9478.md#insn-00bc94e8) · [`00bc951c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9478.md#insn-00bc951c)
- 新版 [`00bc94f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc94bc.md#insn-00bc94f0) · [`00bc952c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc94bc.md#insn-00bc952c) · [`00bc9560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc94bc.md#insn-00bc9560)

~~~diff
- 00bc94ac ["INT_ADD", "register:40f0:8", ["const:bc94ac:8", "const:4:8"]]
- 00bc94ac ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc94f0 ["INT_ADD", "register:40f0:8", ["const:bc94f0:8", "const:4:8"]]
+ 00bc94f0 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc94ac bytes 354f0094
+ 00bc94f0 bytes 384f0094
- 00bc94e8 ["COPY", "tmp:0:8", ["const:328:8"]]
- 00bc94e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc94e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc94e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc952c ["COPY", "tmp:0:8", ["const:378:8"]]
+ 00bc952c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc952c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc952c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc94e8 bytes 08a10c91
+ 00bc952c bytes 08e10d91
- 00bc951c ["INT_ADD", "register:40f0:8", ["const:bc951c:8", "const:4:8"]]
- 00bc951c ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc9560 ["INT_ADD", "register:40f0:8", ["const:bc9560:8", "const:4:8"]]
+ 00bc9560 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc951c bytes 19470094
+ 00bc9560 bytes 1c470094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c13e2911c4ff660b805db581528a7420"></a>

### [`00bc9520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9520.md) → [`00bc9564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9564.md) FUN_00bc9564

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc95c8",
      "incomplete_value": false,
      "site": "00bc95c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9584",
      "incomplete_value": false,
      "site": "00bc9584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:4e8:8"
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
      "00bc95c8",
      "DATA",
      [
        "storage",
        "00c184e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc95c8",
      "DATA",
      [
        "storage",
        "00c18538",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9520.md#insn-00bc9554) · [`00bc9578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9520.md#insn-00bc9578) · [`00bc95bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9520.md#insn-00bc95bc)
- 新版 [`00bc9598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9564.md#insn-00bc9598) · [`00bc95bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9564.md#insn-00bc95bc) · [`00bc9600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9564.md#insn-00bc9600)

~~~diff
- 00bc9554 ["INT_ADD", "register:40f0:8", ["const:bc9554:8", "const:4:8"]]
- 00bc9554 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc9598 ["INT_ADD", "register:40f0:8", ["const:bc9598:8", "const:4:8"]]
+ 00bc9598 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc9554 bytes 0b4f0094
+ 00bc9598 bytes 0e4f0094
- 00bc9578 ["COPY", "tmp:0:8", ["const:4e8:8"]]
- 00bc9578 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc9578 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc9578 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc95bc ["COPY", "tmp:0:8", ["const:538:8"]]
+ 00bc95bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc95bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc95bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc9578 bytes 08a11391
+ 00bc95bc bytes 08e11491
- 00bc95bc ["INT_ADD", "register:40f0:8", ["const:bc95bc:8", "const:4:8"]]
- 00bc95bc ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc9600 ["INT_ADD", "register:40f0:8", ["const:bc9600:8", "const:4:8"]]
+ 00bc9600 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc95bc bytes f1460094
+ 00bc9600 bytes f4460094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e241125f5803223e26ed11923f81c993"></a>

### [`00bc95c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc95c0.md) → [`00bc9604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9604.md) FUN_00bc9604

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bc489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md) · 呼出先 3件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 2件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

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
      "definition_site": "00bc9670",
      "incomplete_value": false,
      "site": "00bc9670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc962c",
      "incomplete_value": false,
      "site": "00bc962c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "00bc9670",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc9670",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc95f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc95c0.md#insn-00bc95f4) · [`00bc961c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc95c0.md#insn-00bc961c) · [`00bc9624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc95c0.md#insn-00bc9624)
- 新版 [`00bc9638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9604.md#insn-00bc9638) · [`00bc9660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9604.md#insn-00bc9660) · [`00bc9668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9604.md#insn-00bc9668)

~~~diff
- 00bc95f4 ["INT_ADD", "register:40f0:8", ["const:bc95f4:8", "const:4:8"]]
- 00bc95f4 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc9638 ["INT_ADD", "register:40f0:8", ["const:bc9638:8", "const:4:8"]]
+ 00bc9638 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc95f4 bytes e34e0094
+ 00bc9638 bytes e64e0094
- 00bc961c ["INT_ADD", "register:40f0:8", ["const:bc961c:8", "const:4:8"]]
- 00bc961c ["CALL", null, ["callee:00bdb190:8"]]
+ 00bc9660 ["INT_ADD", "register:40f0:8", ["const:bc9660:8", "const:4:8"]]
+ 00bc9660 ["CALL", null, ["callee:00bdb190:8"]]
- 00bc961c bytes c9460094
+ 00bc9660 bytes cc460094
- 00bc9624 ["COPY", "tmp:0:8", ["const:848:8"]]
- 00bc9624 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bc9624 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bc9624 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bc9668 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00bc9668 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc9668 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc9668 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bc9624 bytes 29212191
+ 00bc9668 bytes 29612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87ba8ad4af9365d31c413d3ef06a0d4c"></a>

### [`00bc966c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc966c.md) → [`00bc96b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc96b0.md) FUN_00bc96b0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00bc245c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc245c.md) [`00bc489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md) · 呼出先 14件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bca980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca980.md)
- 新版 呼出元 2件 [`00bc24a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md) [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) · 呼出先 14件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bca9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca9c4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.63% / 新版 97.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc97d0",
      "incomplete_value": false,
      "site": "00bc97d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc978c",
      "incomplete_value": false,
      "site": "00bc978c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "definition_site": "00bc97f8",
      "incomplete_value": false,
      "site": "00bc97f8",
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
            "const:a6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc97b4",
      "incomplete_value": false,
      "site": "00bc97b4",
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
            "const:c:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc9984",
      "incomplete_value": false,
      "site": "00bc9984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9940",
      "incomplete_value": false,
      "site": "00bc9940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:558:8"
          ]
        ]
      ]
    },
    "ordinal": 45,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc97d0",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc97f8",
      "DATA",
      [
        "storage",
        "002a800c",
        null,
        "string"
      ]
    ],
    [
      "00bc9984",
      "DATA",
      [
        "storage",
        "00c18558",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc97d0",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc97f8",
      "DATA",
      [
        "storage",
        "002a80a6",
        null,
        "string"
      ]
    ],
    [
      "00bc9984",
      "DATA",
      [
        "storage",
        "00c185a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc966c.md#insn-00bc9984) · [`00bc9d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc966c.md#insn-00bc9d60) · [`00bc9d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc966c.md#insn-00bc9d80)
- 新版 [`00bc99c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc96b0.md#insn-00bc99c8) · [`00bc9da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc96b0.md#insn-00bc9da4) · [`00bc9dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc96b0.md#insn-00bc9dc4)

~~~diff
- 00bc9984 ["INT_ADD", "register:40f0:8", ["const:bc9984:8", "const:4:8"]]
- 00bc9984 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00bc99c8 ["INT_ADD", "register:40f0:8", ["const:bc99c8:8", "const:4:8"]]
+ 00bc99c8 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00bc9984 bytes c7450094
+ 00bc99c8 bytes ca450094
- 00bc9d60 ["INT_ADD", "register:40f0:8", ["const:bc9d60:8", "const:4:8"]]
- 00bc9d60 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bc9da4 ["INT_ADD", "register:40f0:8", ["const:bc9da4:8", "const:4:8"]]
+ 00bc9da4 ["CALL", null, ["callee:00bde2c0:8"]]
- 00bc9d60 bytes 44510094
+ 00bc9da4 bytes 47510094
- 00bc9d80 ["INT_ADD", "register:40f0:8", ["const:bc9d80:8", "const:4:8"]]
- 00bc9d80 ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bc9dc4 ["INT_ADD", "register:40f0:8", ["const:bc9dc4:8", "const:4:8"]]
+ 00bc9dc4 ["CALL", null, ["callee:00bbb19c:8"]]
- 00bc9d80 bytes f6c4ff97
+ 00bc9dc4 bytes f6c4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-066100ce168db2cabbeebfffe86a50d6"></a>

### [`00bc9dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9dec.md) → [`00bc9e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9e30.md) FUN_00bc9e30

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc9e94",
      "incomplete_value": false,
      "site": "00bc9e94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9e50",
      "incomplete_value": false,
      "site": "00bc9e50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "00bc9e94",
      "DATA",
      [
        "storage",
        "00c188d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc9e94",
      "DATA",
      [
        "storage",
        "00c18928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9dec.md#insn-00bc9e20) · [`00bc9e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9dec.md#insn-00bc9e44) · [`00bc9e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9dec.md#insn-00bc9e88)
- 新版 [`00bc9e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9e30.md#insn-00bc9e64) · [`00bc9e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9e30.md#insn-00bc9e88) · [`00bc9ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9e30.md#insn-00bc9ecc)

~~~diff
- 00bc9e20 ["INT_ADD", "register:40f0:8", ["const:bc9e20:8", "const:4:8"]]
- 00bc9e20 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc9e64 ["INT_ADD", "register:40f0:8", ["const:bc9e64:8", "const:4:8"]]
+ 00bc9e64 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc9e20 bytes d84c0094
+ 00bc9e64 bytes db4c0094
- 00bc9e44 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 00bc9e44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc9e44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc9e44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc9e88 ["COPY", "tmp:0:8", ["const:928:8"]]
+ 00bc9e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc9e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc9e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc9e44 bytes 08612391
+ 00bc9e88 bytes 08a12491
- 00bc9e88 ["INT_ADD", "register:40f0:8", ["const:bc9e88:8", "const:4:8"]]
- 00bc9e88 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc9ecc ["INT_ADD", "register:40f0:8", ["const:bc9ecc:8", "const:4:8"]]
+ 00bc9ecc ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc9e88 bytes be440094
+ 00bc9ecc bytes c1440094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-762b5d975bd70b6f23627083b73e080d"></a>

### [`00bc9e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9e8c.md) → [`00bc9ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9ed0.md) FUN_00bc9ed0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

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
      "definition_site": "00bc9f38",
      "incomplete_value": false,
      "site": "00bc9f38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9ef4",
      "incomplete_value": false,
      "site": "00bc9ef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "00bc9f38",
      "DATA",
      [
        "storage",
        "00c18948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc9f38",
      "DATA",
      [
        "storage",
        "00c18998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9e8c.md#insn-00bc9ec4) · [`00bc9ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9e8c.md#insn-00bc9ee8) · [`00bc9f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9e8c.md#insn-00bc9f34)
- 新版 [`00bc9f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9ed0.md#insn-00bc9f08) · [`00bc9f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9ed0.md#insn-00bc9f2c) · [`00bc9f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9ed0.md#insn-00bc9f78)

~~~diff
- 00bc9ec4 ["INT_ADD", "register:40f0:8", ["const:bc9ec4:8", "const:4:8"]]
- 00bc9ec4 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bc9f08 ["INT_ADD", "register:40f0:8", ["const:bc9f08:8", "const:4:8"]]
+ 00bc9f08 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bc9ec4 bytes af4c0094
+ 00bc9f08 bytes b24c0094
- 00bc9ee8 ["COPY", "tmp:0:8", ["const:948:8"]]
- 00bc9ee8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc9ee8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc9ee8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc9f2c ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00bc9f2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc9f2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc9f2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc9ee8 bytes 08212591
+ 00bc9f2c bytes 08612691
- 00bc9f34 ["INT_ADD", "register:40f0:8", ["const:bc9f34:8", "const:4:8"]]
- 00bc9f34 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bc9f78 ["INT_ADD", "register:40f0:8", ["const:bc9f78:8", "const:4:8"]]
+ 00bc9f78 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bc9f34 bytes 93440094
+ 00bc9f78 bytes 96440094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab9af762a80990b5d61dc6904aac6fbf"></a>

### [`00bca2dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca2dc.md) → [`00bca320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca320.md) FUN_00bca320

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be10b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1100.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.08% / 新版 99.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bca444",
      "incomplete_value": false,
      "site": "00bca45c",
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
            "const:9e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bca400",
      "incomplete_value": false,
      "site": "00bca418",
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
            "const:4:8"
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
      "00bca444",
      "PARAM",
      [
        "storage",
        "002a8004",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bca444",
      "PARAM",
      [
        "storage",
        "002a809e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca2dc.md#insn-00bca418) · [`00bca400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca2dc.md#insn-00bca400) · [`00bca44c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca2dc.md#insn-00bca44c)
- 新版 [`00bca45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca320.md#insn-00bca45c) · [`00bca444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca320.md#insn-00bca444) · [`00bca490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca320.md#insn-00bca490)

~~~diff
- 00bca418 ["INT_ADD", "register:40f0:8", ["const:bca418:8", "const:4:8"]]
- 00bca418 ["CALL", null, ["callee:00be1100:8"]]
+ 00bca45c ["INT_ADD", "register:40f0:8", ["const:bca45c:8", "const:4:8"]]
+ 00bca45c ["CALL", null, ["callee:00be1100:8"]]
- 00bca418 bytes 265b0094
+ 00bca45c bytes 295b0094
- 00bca400 ["COPY", "tmp:0:8", ["const:4:8"]]
- 00bca400 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00bca400 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00bca400 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00bca444 ["COPY", "tmp:0:8", ["const:9e:8"]]
+ 00bca444 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00bca444 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00bca444 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00bca400 bytes 42100091
+ 00bca444 bytes 42780291
- 00bca44c ["INT_ADD", "register:40f0:8", ["const:bca44c:8", "const:4:8"]]
- 00bca44c ["CALL", null, ["callee:00bdd250:8"]]
+ 00bca490 ["INT_ADD", "register:40f0:8", ["const:bca490:8", "const:4:8"]]
+ 00bca490 ["CALL", null, ["callee:00bdd250:8"]]
- 00bca44c bytes 6d4b0094
+ 00bca490 bytes 704b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c482040a41c3b739b7afe0ca4deb17f3"></a>

### [`00bca498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca498.md) → [`00bca4dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca4dc.md) FUN_00bca4dc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be10b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1100.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.12% / 新版 99.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bca618",
      "incomplete_value": false,
      "site": "00bca628",
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
            "const:2b7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bca5d4",
      "incomplete_value": false,
      "site": "00bca5e4",
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
            "const:2b9:8"
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
      "00bca618",
      "PARAM",
      [
        "storage",
        "0029c2b9",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bca618",
      "PARAM",
      [
        "storage",
        "0029c2b7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca5e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca498.md#insn-00bca5e4) · [`00bca5d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca498.md#insn-00bca5d4) · [`00bca618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca498.md#insn-00bca618)
- 新版 [`00bca628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca4dc.md#insn-00bca628) · [`00bca618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca4dc.md#insn-00bca618) · [`00bca65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca4dc.md#insn-00bca65c)

~~~diff
- 00bca5e4 ["INT_ADD", "register:40f0:8", ["const:bca5e4:8", "const:4:8"]]
- 00bca5e4 ["CALL", null, ["callee:00be1100:8"]]
+ 00bca628 ["INT_ADD", "register:40f0:8", ["const:bca628:8", "const:4:8"]]
+ 00bca628 ["CALL", null, ["callee:00be1100:8"]]
- 00bca5e4 bytes b35a0094
+ 00bca628 bytes b65a0094
- 00bca5d4 ["COPY", "tmp:0:8", ["const:2b9:8"]]
- 00bca5d4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00bca5d4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00bca5d4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00bca618 ["COPY", "tmp:0:8", ["const:2b7:8"]]
+ 00bca618 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00bca618 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00bca618 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00bca5d4 bytes 42e40a91
+ 00bca618 bytes 42dc0a91
- 00bca618 ["INT_ADD", "register:40f0:8", ["const:bca618:8", "const:4:8"]]
- 00bca618 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bca65c ["INT_ADD", "register:40f0:8", ["const:bca65c:8", "const:4:8"]]
+ 00bca65c ["CALL", null, ["callee:00bdd250:8"]]
- 00bca618 bytes fa4a0094
+ 00bca65c bytes fd4a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f5a9dbcc56ed13f69fe9a3a9487a18f"></a>

### [`00bca664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca664.md) → [`00bca6a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca6a8.md) FUN_00bca6a8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be10b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1100.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.22% / 新版 99.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bca81c",
      "incomplete_value": false,
      "site": "00bca830",
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
            "const:177:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bca7d8",
      "incomplete_value": false,
      "site": "00bca7ec",
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
            "const:dd:8"
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
      "00bca81c",
      "PARAM",
      [
        "storage",
        "002a90dd",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bca81c",
      "PARAM",
      [
        "storage",
        "002a9177",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca7ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca664.md#insn-00bca7ec) · [`00bca7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca664.md#insn-00bca7d8) · [`00bca820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca664.md#insn-00bca820)
- 新版 [`00bca830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca6a8.md#insn-00bca830) · [`00bca81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca6a8.md#insn-00bca81c) · [`00bca864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca6a8.md#insn-00bca864)

~~~diff
- 00bca7ec ["INT_ADD", "register:40f0:8", ["const:bca7ec:8", "const:4:8"]]
- 00bca7ec ["CALL", null, ["callee:00be1100:8"]]
+ 00bca830 ["INT_ADD", "register:40f0:8", ["const:bca830:8", "const:4:8"]]
+ 00bca830 ["CALL", null, ["callee:00be1100:8"]]
- 00bca7ec bytes 315a0094
+ 00bca830 bytes 345a0094
- 00bca7d8 ["COPY", "tmp:0:8", ["const:dd:8"]]
- 00bca7d8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00bca7d8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00bca7d8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00bca81c ["COPY", "tmp:0:8", ["const:177:8"]]
+ 00bca81c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00bca81c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00bca81c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00bca7d8 bytes 42740391
+ 00bca81c bytes 42dc0591
- 00bca820 ["INT_ADD", "register:40f0:8", ["const:bca820:8", "const:4:8"]]
- 00bca820 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bca864 ["INT_ADD", "register:40f0:8", ["const:bca864:8", "const:4:8"]]
+ 00bca864 ["CALL", null, ["callee:00bdd250:8"]]
- 00bca820 bytes 784a0094
+ 00bca864 bytes 7b4a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-611532c4a4a6ec3d1182108ab032c174"></a>

### [`00bca980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca980.md) → [`00bca9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca9c4.md) FUN_00bca9c4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bc966c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc966c.md) [`00bca980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca980.md) · 呼出先 14件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bbff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md)
- 新版 呼出元 3件 [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) [`00bc96b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc96b0.md) [`00bca9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca9c4.md) · 呼出先 14件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bbff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.96% / 新版 96.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcaae0",
      "incomplete_value": false,
      "site": "00bcaae0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcaa9c",
      "incomplete_value": false,
      "site": "00bcaa9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "definition_site": "00bcabb8",
      "incomplete_value": false,
      "site": "00bcabb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcab74",
      "incomplete_value": false,
      "site": "00bcab74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcac78",
      "incomplete_value": false,
      "site": "00bcac78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcac34",
      "incomplete_value": false,
      "site": "00bcac34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "00bcaae0",
      "DATA",
      [
        "storage",
        "00c185c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bcabb8",
      "DATA",
      [
        "storage",
        "00c185c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bcac78",
      "DATA",
      [
        "storage",
        "00c185c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bcaae0",
      "DATA",
      [
        "storage",
        "00c18618",
        null,
        "undefined *"
      ]
    ],
    [
      "00bcabb8",
      "DATA",
      [
        "storage",
        "00c18618",
        null,
        "undefined *"
      ]
    ],
    [
      "00bcac78",
      "DATA",
      [
        "storage",
        "00c18618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca980.md#insn-00bcb2ac) · [`00bcaa1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca980.md#insn-00bcaa1c) · [`00bcaa30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca980.md#insn-00bcaa30)
- 新版 [`00bcb2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca9c4.md#insn-00bcb2f0) · [`00bcaa60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca9c4.md#insn-00bcaa60) · [`00bcaa74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca9c4.md#insn-00bcaa74)

~~~diff
- 00bcb2ac ["INT_ADD", "register:40f0:8", ["const:bcb2ac:8", "const:4:8"]]
- 00bcb2ac ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bcb2f0 ["INT_ADD", "register:40f0:8", ["const:bcb2f0:8", "const:4:8"]]
+ 00bcb2f0 ["CALL", null, ["callee:00bbb19c:8"]]
- 00bcb2ac bytes abbfff97
+ 00bcb2f0 bytes abbfff97
- 00bcaa1c ["INT_ADD", "register:40f0:8", ["const:bcaa1c:8", "const:4:8"]]
- 00bcaa1c ["CALL", null, ["local:b0:8"]]
+ 00bcaa60 ["INT_ADD", "register:40f0:8", ["const:bcaa60:8", "const:4:8"]]
+ 00bcaa60 ["CALL", null, ["local:b0:8"]]
- 00bcaa1c bytes d9ffff97
+ 00bcaa60 bytes d9ffff97
- 00bcaa30 ["INT_ADD", "register:40f0:8", ["const:bcaa30:8", "const:4:8"]]
- 00bcaa30 ["CALL", null, ["callee:00bcb5dc:8"]]
+ 00bcaa74 ["INT_ADD", "register:40f0:8", ["const:bcaa74:8", "const:4:8"]]
+ 00bcaa74 ["CALL", null, ["callee:00bcb5dc:8"]]
- 00bcaa30 bytes da020094
+ 00bcaa74 bytes da020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6299d918dcca427cdc7ceb11cd251c98"></a>

### [`00bcb2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb2ec.md) → [`00bcb330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb330.md) FUN_00bcb330

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc966c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc966c.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc96b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc96b0.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

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
      "definition_site": "00bcb3ac",
      "incomplete_value": false,
      "site": "00bcb3ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb368",
      "incomplete_value": false,
      "site": "00bcb368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:868:8"
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
      "00bcb3ac",
      "DATA",
      [
        "storage",
        "00c18868",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bcb3ac",
      "DATA",
      [
        "storage",
        "00c188b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb2ec.md#insn-00bcb338) · [`00bcb35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb2ec.md#insn-00bcb35c) · [`00bcb3c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb2ec.md#insn-00bcb3c8)
- 新版 [`00bcb37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb330.md#insn-00bcb37c) · [`00bcb3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb330.md#insn-00bcb3a0) · [`00bcb40c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb330.md#insn-00bcb40c)

~~~diff
- 00bcb338 ["INT_ADD", "register:40f0:8", ["const:bcb338:8", "const:4:8"]]
- 00bcb338 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bcb37c ["INT_ADD", "register:40f0:8", ["const:bcb37c:8", "const:4:8"]]
+ 00bcb37c ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bcb338 bytes 92470094
+ 00bcb37c bytes 95470094
- 00bcb35c ["COPY", "tmp:0:8", ["const:868:8"]]
- 00bcb35c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bcb35c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bcb35c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bcb3a0 ["COPY", "tmp:0:8", ["const:8b8:8"]]
+ 00bcb3a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcb3a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcb3a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bcb35c bytes 08a12191
+ 00bcb3a0 bytes 08e12291
- 00bcb3c8 ["INT_ADD", "register:40f0:8", ["const:bcb3c8:8", "const:4:8"]]
- 00bcb3c8 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bcb40c ["INT_ADD", "register:40f0:8", ["const:bcb40c:8", "const:4:8"]]
+ 00bcb40c ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bcb3c8 bytes 6e3f0094
+ 00bcb40c bytes 713f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32d004b1e70c3c21b4e6a22fb2f0072d"></a>

### [`00bcb3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb3cc.md) → [`00bcb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb410.md) FUN_00bcb410

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcb474",
      "incomplete_value": false,
      "site": "00bcb484",
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
            "const:195:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb430",
      "incomplete_value": false,
      "site": "00bcb440",
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
            "const:10a:8"
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
      "definition_site": "00bcb47c",
      "incomplete_value": false,
      "site": "00bcb484",
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
      "definition_site": "00bcb438",
      "incomplete_value": false,
      "site": "00bcb440",
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
      "00bcb474",
      "PARAM",
      [
        "storage",
        "002a210a",
        null,
        "string"
      ]
    ],
    [
      "00bcb47c",
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
      "00bcb474",
      "PARAM",
      [
        "storage",
        "002a2195",
        null,
        "string"
      ]
    ],
    [
      "00bcb47c",
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

- 旧版 [`00bcb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb3cc.md#insn-00bcb440) · [`00bcb430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb3cc.md#insn-00bcb430) · [`00bcb438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb3cc.md#insn-00bcb438)
- 新版 [`00bcb484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb410.md#insn-00bcb484) · [`00bcb474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb410.md#insn-00bcb474) · [`00bcb47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb410.md#insn-00bcb47c)

~~~diff
- 00bcb440 ["INT_ADD", "register:40f0:8", ["const:bcb440:8", "const:4:8"]]
- 00bcb440 ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bcb484 ["INT_ADD", "register:40f0:8", ["const:bcb484:8", "const:4:8"]]
+ 00bcb484 ["CALL", null, ["callee:00bbb19c:8"]]
- 00bcb440 bytes 46bfff97
+ 00bcb484 bytes 46bfff97
- 00bcb430 ["COPY", "tmp:0:8", ["const:10a:8"]]
- 00bcb430 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bcb430 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bcb430 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bcb474 ["COPY", "tmp:0:8", ["const:195:8"]]
+ 00bcb474 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bcb474 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bcb474 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bcb430 bytes 21280491
+ 00bcb474 bytes 21540691
- 00bcb438 ["COPY", "tmp:0:8", ["const:866:8"]]
- 00bcb438 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00bcb438 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00bcb438 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00bcb47c ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 00bcb47c ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00bcb47c ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00bcb47c ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00bcb438 bytes 63982191
+ 00bcb47c bytes 63641f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36eb09af9b418a4072a3ada756305b2b"></a>

### [`00bcb598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb598.md) → [`00bcb5dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb5dc.md) FUN_00bcb5dc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bca980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca980.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bca9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca9c4.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcb640",
      "incomplete_value": false,
      "site": "00bcb640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb5fc",
      "incomplete_value": false,
      "site": "00bcb5fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "00bcb640",
      "DATA",
      [
        "storage",
        "00c187f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bcb640",
      "DATA",
      [
        "storage",
        "00c18848",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb5cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb598.md#insn-00bcb5cc) · [`00bcb5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb598.md#insn-00bcb5f0) · [`00bcb634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb598.md#insn-00bcb634)
- 新版 [`00bcb610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb5dc.md#insn-00bcb610) · [`00bcb634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb5dc.md#insn-00bcb634) · [`00bcb678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb5dc.md#insn-00bcb678)

~~~diff
- 00bcb5cc ["INT_ADD", "register:40f0:8", ["const:bcb5cc:8", "const:4:8"]]
- 00bcb5cc ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bcb610 ["INT_ADD", "register:40f0:8", ["const:bcb610:8", "const:4:8"]]
+ 00bcb610 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bcb5cc bytes ed460094
+ 00bcb610 bytes f0460094
- 00bcb5f0 ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 00bcb5f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bcb5f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bcb5f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bcb634 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00bcb634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcb634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcb634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bcb5f0 bytes 08e11f91
+ 00bcb634 bytes 08212191
- 00bcb634 ["INT_ADD", "register:40f0:8", ["const:bcb634:8", "const:4:8"]]
- 00bcb634 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bcb678 ["INT_ADD", "register:40f0:8", ["const:bcb678:8", "const:4:8"]]
+ 00bcb678 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bcb634 bytes d33e0094
+ 00bcb678 bytes d63e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96f9e86827cdcad54eabcf9bdd3798dc"></a>

### [`00bcb86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb86c.md) → [`00bcb8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb8b0.md) FUN_00bcb8b0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

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
      "definition_site": "00bcb908",
      "incomplete_value": true,
      "site": "00bcb914",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb8c4",
      "incomplete_value": true,
      "site": "00bcb8d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:64e:8"
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
      "00bcb908",
      "READ",
      [
        "storage",
        "0029264e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcb908",
      "READ",
      [
        "storage",
        "002925c1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb86c.md#insn-00bcb8a8) · [`00bcb8bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb86c.md#insn-00bcb8bc) · [`00bcb8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb86c.md#insn-00bcb8f0)
- 新版 [`00bcb8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb8b0.md#insn-00bcb8ec) · [`00bcb900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb8b0.md#insn-00bcb900) · [`00bcb934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb8b0.md#insn-00bcb934)

~~~diff
- 00bcb8a8 ["INT_ADD", "register:40f0:8", ["const:bcb8a8:8", "const:4:8"]]
- 00bcb8a8 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcb8ec ["INT_ADD", "register:40f0:8", ["const:bcb8ec:8", "const:4:8"]]
+ 00bcb8ec ["CALL", null, ["callee:00bdd250:8"]]
- 00bcb8a8 bytes 56460094
+ 00bcb8ec bytes 59460094
- 00bcb8bc ["COPY", "tmp:0:8", ["const:64e:8"]]
- 00bcb8bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bcb8bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bcb8bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bcb900 ["COPY", "tmp:0:8", ["const:5c1:8"]]
+ 00bcb900 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bcb900 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bcb900 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bcb8bc bytes 29391991
+ 00bcb900 bytes 29051791
- 00bcb8f0 ["INT_ADD", "register:40f0:8", ["const:bcb8f0:8", "const:4:8"]]
- 00bcb8f0 ["CALL", null, ["callee:00bde2c0:8"]]
+ 00bcb934 ["INT_ADD", "register:40f0:8", ["const:bcb934:8", "const:4:8"]]
+ 00bcb934 ["CALL", null, ["callee:00bde2c0:8"]]
- 00bcb8f0 bytes 604a0094
+ 00bcb934 bytes 634a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ce073aa81d1f35360106603af9cbc6d"></a>

### [`00bcbbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbbbc.md) → [`00bcbc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbc00.md) FUN_00bcbc00

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcbcd4",
      "incomplete_value": true,
      "site": "00bcbce0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:35c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbc90",
      "incomplete_value": true,
      "site": "00bcbc9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2d1:8"
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
      "00bcbcd4",
      "READ",
      [
        "storage",
        "002a02d1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcbcd4",
      "READ",
      [
        "storage",
        "002a035c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbbbc.md#insn-00bcbc08) · [`00bcbc48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbbbc.md#insn-00bcbc48) · [`00bcbc74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbbbc.md#insn-00bcbc74)
- 新版 [`00bcbc4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbc00.md#insn-00bcbc4c) · [`00bcbc8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbc00.md#insn-00bcbc8c) · [`00bcbcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbc00.md#insn-00bcbcb8)

~~~diff
- 00bcbc08 ["INT_ADD", "register:40f0:8", ["const:bcbc08:8", "const:4:8"]]
- 00bcbc08 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcbc4c ["INT_ADD", "register:40f0:8", ["const:bcbc4c:8", "const:4:8"]]
+ 00bcbc4c ["CALL", null, ["callee:00bdd250:8"]]
- 00bcbc08 bytes 7e450094
+ 00bcbc4c bytes 81450094
- 00bcbc48 ["INT_ADD", "register:40f0:8", ["const:bcbc48:8", "const:4:8"]]
- 00bcbc48 ["CALL", null, ["callee:00bc82d4:8"]]
+ 00bcbc8c ["INT_ADD", "register:40f0:8", ["const:bcbc8c:8", "const:4:8"]]
+ 00bcbc8c ["CALL", null, ["callee:00bc82d4:8"]]
- 00bcbc48 bytes 92f1ff97
+ 00bcbc8c bytes 92f1ff97
- 00bcbc74 ["INT_ADD", "register:40f0:8", ["const:bcbc74:8", "const:4:8"]]
- 00bcbc74 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcbcb8 ["INT_ADD", "register:40f0:8", ["const:bcbcb8:8", "const:4:8"]]
+ 00bcbcb8 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcbc74 bytes 63450094
+ 00bcbcb8 bytes 66450094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5e156ded9141c1f83c8b558cb59839c"></a>

### [`00bcbcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbcd8.md) → [`00bcbd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbd1c.md) FUN_00bcbd1c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcbdbc",
      "incomplete_value": true,
      "site": "00bcbdcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7ec:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbd78",
      "incomplete_value": true,
      "site": "00bcbd88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:880:8"
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
      "00bcbdbc",
      "READ",
      [
        "storage",
        "002af880",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcbdbc",
      "READ",
      [
        "storage",
        "002af7ec",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbd04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbcd8.md#insn-00bcbd04) · [`00bcbd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbcd8.md#insn-00bcbd28) · [`00bcbd5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbcd8.md#insn-00bcbd5c)
- 新版 [`00bcbd48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbd1c.md#insn-00bcbd48) · [`00bcbd6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbd1c.md#insn-00bcbd6c) · [`00bcbda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbd1c.md#insn-00bcbda0)

~~~diff
- 00bcbd04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbd04 ["INT_ADD", "register:40f0:8", ["const:bcbd04:8", "const:4:8"]]
- 00bcbd04 ["CALLIND", null, ["register:0:8"]]
+ 00bcbd48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcbd48 ["INT_ADD", "register:40f0:8", ["const:bcbd48:8", "const:4:8"]]
+ 00bcbd48 ["CALLIND", null, ["register:0:8"]]
- 00bcbd04 bytes 00013fd6
+ 00bcbd48 bytes 00013fd6
- 00bcbd28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbd28 ["INT_ADD", "register:40f0:8", ["const:bcbd28:8", "const:4:8"]]
- 00bcbd28 ["CALLIND", null, ["register:0:8"]]
+ 00bcbd6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcbd6c ["INT_ADD", "register:40f0:8", ["const:bcbd6c:8", "const:4:8"]]
+ 00bcbd6c ["CALLIND", null, ["register:0:8"]]
- 00bcbd28 bytes 00013fd6
+ 00bcbd6c bytes 00013fd6
- 00bcbd5c ["INT_ADD", "register:40f0:8", ["const:bcbd5c:8", "const:4:8"]]
- 00bcbd5c ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcbda0 ["INT_ADD", "register:40f0:8", ["const:bcbda0:8", "const:4:8"]]
+ 00bcbda0 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcbd5c bytes 29450094
+ 00bcbda0 bytes 2c450094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-164d5ad5c89d3b6309a4f3f49fae2e43"></a>

### [`00bcc6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc6a8.md) → [`00bcc6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc6ec.md) FUN_00bcc6ec

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc521c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc521c.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc5260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5260.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcc750",
      "incomplete_value": false,
      "site": "00bcc750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc70c",
      "incomplete_value": false,
      "site": "00bcc70c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "00bcc750",
      "DATA",
      [
        "storage",
        "00c189b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bcc750",
      "DATA",
      [
        "storage",
        "00c18a08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc6a8.md#insn-00bcc6dc) · [`00bcc700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc6a8.md#insn-00bcc700) · [`00bcc744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc6a8.md#insn-00bcc744)
- 新版 [`00bcc720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc6ec.md#insn-00bcc720) · [`00bcc744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc6ec.md#insn-00bcc744) · [`00bcc788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc6ec.md#insn-00bcc788)

~~~diff
- 00bcc6dc ["INT_ADD", "register:40f0:8", ["const:bcc6dc:8", "const:4:8"]]
- 00bcc6dc ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bcc720 ["INT_ADD", "register:40f0:8", ["const:bcc720:8", "const:4:8"]]
+ 00bcc720 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bcc6dc bytes a9420094
+ 00bcc720 bytes ac420094
- 00bcc700 ["COPY", "tmp:0:8", ["const:9b8:8"]]
- 00bcc700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bcc700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bcc700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bcc744 ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 00bcc744 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcc744 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcc744 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bcc700 bytes 08e12691
+ 00bcc744 bytes 08212891
- 00bcc744 ["INT_ADD", "register:40f0:8", ["const:bcc744:8", "const:4:8"]]
- 00bcc744 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bcc788 ["INT_ADD", "register:40f0:8", ["const:bcc788:8", "const:4:8"]]
+ 00bcc788 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bcc744 bytes 8f3a0094
+ 00bcc788 bytes 923a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61746c42c9b80380f66d82d1ffebab2e"></a>

### [`00bcc83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc83c.md) → [`00bcc880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc880.md) FUN_00bcc880

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bccfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bccfc0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bcd004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd004.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.16% / 新版 99.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcca60",
      "incomplete_value": false,
      "site": "00bcca64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcca1c",
      "incomplete_value": false,
      "site": "00bcca20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "definition_site": "00bccd98",
      "incomplete_value": false,
      "site": "00bccd9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bccd54",
      "incomplete_value": false,
      "site": "00bccd58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "ordinal": 67,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcca64",
      "DATA",
      [
        "storage",
        "00c18a98",
        null,
        "undefined *"
      ]
    ],
    [
      "00bccd9c",
      "DATA",
      [
        "storage",
        "00c18a98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bcca64",
      "DATA",
      [
        "storage",
        "00c18ae8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bccd9c",
      "DATA",
      [
        "storage",
        "00c18ae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc9dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc83c.md#insn-00bcc9dc) · [`00bccd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc83c.md#insn-00bccd14) · [`00bcc890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc83c.md#insn-00bcc890)
- 新版 [`00bcca20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc880.md#insn-00bcca20) · [`00bccd58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc880.md#insn-00bccd58) · [`00bcc8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc880.md#insn-00bcc8d4)

~~~diff
- 00bcc9dc ["INT_ADD", "register:40f0:8", ["const:bcc9dc:8", "const:4:8"]]
- 00bcc9dc ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcca20 ["INT_ADD", "register:40f0:8", ["const:bcca20:8", "const:4:8"]]
+ 00bcca20 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcc9dc bytes 09420094
+ 00bcca20 bytes 0c420094
- 00bccd14 ["INT_ADD", "register:40f0:8", ["const:bccd14:8", "const:4:8"]]
- 00bccd14 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bccd58 ["INT_ADD", "register:40f0:8", ["const:bccd58:8", "const:4:8"]]
+ 00bccd58 ["CALL", null, ["callee:00bdd250:8"]]
- 00bccd14 bytes 3b410094
+ 00bccd58 bytes 3e410094
- 00bcc890 ["INT_ADD", "register:40f0:8", ["const:bcc890:8", "const:4:8"]]
- 00bcc890 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcc8d4 ["INT_ADD", "register:40f0:8", ["const:bcc8d4:8", "const:4:8"]]
+ 00bcc8d4 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcc890 bytes 5c420094
+ 00bcc8d4 bytes 5f420094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d00028c440ff45c321a52d9446037a9e"></a>

### [`00bcd964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd964.md) → [`00bcd9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd9a8.md) FUN_00bcd9a8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.38% / 新版 98.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcdb68",
      "incomplete_value": true,
      "site": "00bcdb74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:264:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcdb24",
      "incomplete_value": true,
      "site": "00bcdb30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1d9:8"
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
      "00bcdb68",
      "READ",
      [
        "storage",
        "002a11d9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcdb68",
      "READ",
      [
        "storage",
        "002a1264",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd9ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd964.md#insn-00bcd9ac) · [`00bcda18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd964.md#insn-00bcda18) · [`00bcda4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd964.md#insn-00bcda4c)
- 新版 [`00bcd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd9a8.md#insn-00bcd9f0) · [`00bcda5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd9a8.md#insn-00bcda5c) · [`00bcda90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd9a8.md#insn-00bcda90)

~~~diff
- 00bcd9ac ["INT_ADD", "register:40f0:8", ["const:bcd9ac:8", "const:4:8"]]
- 00bcd9ac ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcd9f0 ["INT_ADD", "register:40f0:8", ["const:bcd9f0:8", "const:4:8"]]
+ 00bcd9f0 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcd9ac bytes 153e0094
+ 00bcd9f0 bytes 183e0094
- 00bcda18 ["INT_ADD", "register:40f0:8", ["const:bcda18:8", "const:4:8"]]
- 00bcda18 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcda5c ["INT_ADD", "register:40f0:8", ["const:bcda5c:8", "const:4:8"]]
+ 00bcda5c ["CALL", null, ["callee:00bdd250:8"]]
- 00bcda18 bytes fa3d0094
+ 00bcda5c bytes fd3d0094
- 00bcda4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcda4c ["INT_ADD", "register:40f0:8", ["const:bcda4c:8", "const:4:8"]]
- 00bcda4c ["CALLIND", null, ["register:0:8"]]
+ 00bcda90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcda90 ["INT_ADD", "register:40f0:8", ["const:bcda90:8", "const:4:8"]]
+ 00bcda90 ["CALLIND", null, ["register:0:8"]]
- 00bcda4c bytes 00013fd6
+ 00bcda90 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4cd245190a7576bf36f1d201e5a1b92"></a>

### [`00bcdd74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcdd74.md) → [`00bcddb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcddb8.md) FUN_00bcddb8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcde1c",
      "incomplete_value": true,
      "site": "00bcde2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7ec:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcddd8",
      "incomplete_value": true,
      "site": "00bcdde8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:880:8"
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
      "00bcde1c",
      "READ",
      [
        "storage",
        "002af880",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcde1c",
      "READ",
      [
        "storage",
        "002af7ec",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcde2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcdd74.md#insn-00bcde2c) · [`00bcddb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcdd74.md#insn-00bcddb8) · [`00bcddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcdd74.md#insn-00bcddd0)
- 新版 [`00bcde70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcddb8.md#insn-00bcde70) · [`00bcddfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcddb8.md#insn-00bcddfc) · [`00bcde14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcddb8.md#insn-00bcde14)

~~~diff
- 00bcde2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcde2c ["INT_ADD", "register:40f0:8", ["const:bcde2c:8", "const:4:8"]]
- 00bcde2c ["CALLIND", null, ["register:0:8"]]
+ 00bcde70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcde70 ["INT_ADD", "register:40f0:8", ["const:bcde70:8", "const:4:8"]]
+ 00bcde70 ["CALLIND", null, ["register:0:8"]]
- 00bcde2c bytes 00013fd6
+ 00bcde70 bytes 00013fd6
- 00bcddb8 ["INT_ADD", "register:40f0:8", ["const:bcddb8:8", "const:4:8"]]
- 00bcddb8 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcddfc ["INT_ADD", "register:40f0:8", ["const:bcddfc:8", "const:4:8"]]
+ 00bcddfc ["CALL", null, ["callee:00bdd250:8"]]
- 00bcddb8 bytes 123d0094
+ 00bcddfc bytes 153d0094
- 00bcddd0 ["COPY", "tmp:0:8", ["const:880:8"]]
- 00bcddd0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bcddd0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bcddd0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bcde14 ["COPY", "tmp:0:8", ["const:7ec:8"]]
+ 00bcde14 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00bcde14 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00bcde14 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bcddd0 bytes 4a012291
+ 00bcde14 bytes 4ab11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-411797d73b8221fc6c4205bd65b472fd"></a>

### [`00bce1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce1f0.md) → [`00bce234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce234.md) FUN_00bce234

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.45% / 新版 98.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bce354",
      "incomplete_value": true,
      "site": "00bce360",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bce310",
      "incomplete_value": true,
      "site": "00bce31c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:25b:8"
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
      "00bce354",
      "READ",
      [
        "storage",
        "002a725b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bce354",
      "READ",
      [
        "storage",
        "002a72f5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bce21c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce1f0.md#insn-00bce21c) · [`00bce240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce1f0.md#insn-00bce240) · [`00bce26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce1f0.md#insn-00bce26c)
- 新版 [`00bce260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce234.md#insn-00bce260) · [`00bce284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce234.md#insn-00bce284) · [`00bce2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce234.md#insn-00bce2b0)

~~~diff
- 00bce21c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bce21c ["INT_ADD", "register:40f0:8", ["const:bce21c:8", "const:4:8"]]
- 00bce21c ["CALLIND", null, ["register:0:8"]]
+ 00bce260 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bce260 ["INT_ADD", "register:40f0:8", ["const:bce260:8", "const:4:8"]]
+ 00bce260 ["CALLIND", null, ["register:0:8"]]
- 00bce21c bytes 00013fd6
+ 00bce260 bytes 00013fd6
- 00bce240 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bce240 ["INT_ADD", "register:40f0:8", ["const:bce240:8", "const:4:8"]]
- 00bce240 ["CALLIND", null, ["register:0:8"]]
+ 00bce284 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bce284 ["INT_ADD", "register:40f0:8", ["const:bce284:8", "const:4:8"]]
+ 00bce284 ["CALLIND", null, ["register:0:8"]]
- 00bce240 bytes 00013fd6
+ 00bce284 bytes 00013fd6
- 00bce26c ["INT_ADD", "register:40f0:8", ["const:bce26c:8", "const:4:8"]]
- 00bce26c ["CALL", null, ["callee:00bdd250:8"]]
+ 00bce2b0 ["INT_ADD", "register:40f0:8", ["const:bce2b0:8", "const:4:8"]]
+ 00bce2b0 ["CALL", null, ["callee:00bdd250:8"]]
- 00bce26c bytes e53b0094
+ 00bce2b0 bytes e83b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e0e380df2cf16b69480b5205e5d0fda"></a>

### [`00bce500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce500.md) → [`00bce544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce544.md) FUN_00bce544

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bccfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bccfc0.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bcd004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd004.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.68% / 新版 94.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bce5ac",
      "incomplete_value": true,
      "site": "00bce5b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:31a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bce568",
      "incomplete_value": true,
      "site": "00bce574",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:31c:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bce638",
      "incomplete_value": false,
      "site": "00bce63c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bce5f4",
      "incomplete_value": false,
      "site": "00bce5f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "00bce5ac",
      "READ",
      [
        "storage",
        "0029c31c",
        null,
        "string"
      ]
    ],
    [
      "00bce63c",
      "DATA",
      [
        "storage",
        "00c18a98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bce5ac",
      "READ",
      [
        "storage",
        "0029c31a",
        null,
        "string"
      ]
    ],
    [
      "00bce63c",
      "DATA",
      [
        "storage",
        "00c18ae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bce5b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce500.md#insn-00bce5b4) · [`00bce548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce500.md#insn-00bce548) · [`00bce560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce500.md#insn-00bce560)
- 新版 [`00bce5f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce544.md#insn-00bce5f8) · [`00bce58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce544.md#insn-00bce58c) · [`00bce5a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce544.md#insn-00bce5a4)

~~~diff
- 00bce5b4 ["INT_ADD", "register:40f0:8", ["const:bce5b4:8", "const:4:8"]]
- 00bce5b4 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bce5f8 ["INT_ADD", "register:40f0:8", ["const:bce5f8:8", "const:4:8"]]
+ 00bce5f8 ["CALL", null, ["callee:00bdd250:8"]]
- 00bce5b4 bytes 133b0094
+ 00bce5f8 bytes 163b0094
- 00bce548 ["INT_ADD", "register:40f0:8", ["const:bce548:8", "const:4:8"]]
- 00bce548 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bce58c ["INT_ADD", "register:40f0:8", ["const:bce58c:8", "const:4:8"]]
+ 00bce58c ["CALL", null, ["callee:00bdd250:8"]]
- 00bce548 bytes 2e3b0094
+ 00bce58c bytes 313b0094
- 00bce560 ["COPY", "tmp:0:8", ["const:31c:8"]]
- 00bce560 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bce560 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bce560 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bce5a4 ["COPY", "tmp:0:8", ["const:31a:8"]]
+ 00bce5a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00bce5a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00bce5a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bce560 bytes 4a710c91
+ 00bce5a4 bytes 4a690c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f288d9ef7e161cfafd89df4b59578edf"></a>

### [`00bce8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce8f8.md) → [`00bce93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce93c.md) FUN_00bce93c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc67b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc67b8.md) · 呼出先 6件 [`00bc10fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc10fc.md) [`00bc1710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1710.md) [`00bce774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce774.md) [`00bceca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bceca8.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md)
- 新版 呼出元 1件 [`00bc67fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc67fc.md) · 呼出先 6件 [`00bc1140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1140.md) [`00bc1754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1754.md) [`00bce7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce7b8.md) [`00bcecec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bcecec.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.95% / 新版 96.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bceae4",
      "incomplete_value": false,
      "site": "00bceae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bceaa0",
      "incomplete_value": false,
      "site": "00bceaa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:b8:8"
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
      "definition_site": "00bceba4",
      "incomplete_value": false,
      "site": "00bceba4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bceb60",
      "incomplete_value": false,
      "site": "00bceb60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:748:8"
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
      "00bcea3c",
      "DATA",
      [
        "storage",
        "00c19748",
        null,
        "undefined *"
      ]
    ],
    [
      "00bceae4",
      "DATA",
      [
        "storage",
        "00c190b8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bceba4",
      "DATA",
      [
        "storage",
        "00c19748",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bcea3c",
      "DATA",
      [
        "storage",
        "00c19798",
        null,
        "undefined *"
      ]
    ],
    [
      "00bceae4",
      "DATA",
      [
        "storage",
        "00c19108",
        null,
        "undefined *"
      ]
    ],
    [
      "00bceba4",
      "DATA",
      [
        "storage",
        "00c19798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bce964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce8f8.md#insn-00bce964) · [`00bce974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce8f8.md#insn-00bce974) · [`00bce9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce8f8.md#insn-00bce9a0)
- 新版 [`00bce9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce93c.md#insn-00bce9a8) · [`00bce9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce93c.md#insn-00bce9b8) · [`00bce9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce93c.md#insn-00bce9e4)

~~~diff
- 00bce964 ["INT_ADD", "register:40f0:8", ["const:bce964:8", "const:4:8"]]
- 00bce964 ["CALL", null, ["callee:00bcecec:8"]]
+ 00bce9a8 ["INT_ADD", "register:40f0:8", ["const:bce9a8:8", "const:4:8"]]
+ 00bce9a8 ["CALL", null, ["callee:00bcecec:8"]]
- 00bce964 bytes d1000094
+ 00bce9a8 bytes d1000094
- 00bce974 ["INT_ADD", "register:40f0:8", ["const:bce974:8", "const:4:8"]]
- 00bce974 ["CALL", null, ["callee:00bc1140:8"]]
+ 00bce9b8 ["INT_ADD", "register:40f0:8", ["const:bce9b8:8", "const:4:8"]]
+ 00bce9b8 ["CALL", null, ["callee:00bc1140:8"]]
- 00bce974 bytes e2c9ff97
+ 00bce9b8 bytes e2c9ff97
- 00bce9a0 ["INT_ADD", "register:40f0:8", ["const:bce9a0:8", "const:4:8"]]
- 00bce9a0 ["CALL", null, ["callee:00bc1754:8"]]
+ 00bce9e4 ["INT_ADD", "register:40f0:8", ["const:bce9e4:8", "const:4:8"]]
+ 00bce9e4 ["CALL", null, ["callee:00bc1754:8"]]
- 00bce9a0 bytes 5ccbff97
+ 00bce9e4 bytes 5ccbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18bcaf574d2a033c0351fd5ef31e0ffc"></a>

### [`00bceca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bceca8.md) → [`00bcecec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bcecec.md) FUN_00bcecec

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00bc245c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc245c.md) [`00bce8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce8f8.md) · 呼出先 5件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bc10fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc10fc.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 2件 [`00bc24a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md) [`00bce93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce93c.md) · 呼出先 5件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bc1140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1140.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.74% / 新版 97.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcee38",
      "incomplete_value": false,
      "site": "00bcee38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcedf4",
      "incomplete_value": false,
      "site": "00bcedf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:128:8"
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
      "00bced44",
      "READ",
      [
        "storage",
        "00c17b68",
        null,
        "undefined1"
      ]
    ],
    [
      "00bced54",
      "READ",
      [
        "storage",
        "00c17b69",
        null,
        "undefined1"
      ]
    ],
    [
      "00bced80",
      "READ",
      [
        "storage",
        "00c17b78",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bced44",
      "READ",
      [
        "storage",
        "00c17bb8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bced54",
      "READ",
      [
        "storage",
        "00c17bb9",
        null,
        "undefined1"
      ]
    ],
    [
      "00bced80",
      "READ",
      [
        "storage",
        "00c17bc8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcece0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bceca8.md#insn-00bcece0) · [`00bced8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bceca8.md#insn-00bced8c) · [`00bcedc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bceca8.md#insn-00bcedc0)
- 新版 [`00bced24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bcecec.md#insn-00bced24) · [`00bcedd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bcecec.md#insn-00bcedd0) · [`00bcee04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bcecec.md#insn-00bcee04)

~~~diff
- 00bcece0 ["COPY", "register:4060:8", ["const:c17988:8"]]
+ 00bced24 ["COPY", "register:4060:8", ["const:c179d8:8"]]
- 00bcece0 bytes 4c652410
+ 00bced24 bytes ac652410
- 00bced8c ["INT_ADD", "register:40f0:8", ["const:bced8c:8", "const:4:8"]]
- 00bced8c ["CALL", null, ["callee:00bbde5c:8"]]
+ 00bcedd0 ["INT_ADD", "register:40f0:8", ["const:bcedd0:8", "const:4:8"]]
+ 00bcedd0 ["CALL", null, ["callee:00bbde5c:8"]]
- 00bced8c bytes 23bcff97
+ 00bcedd0 bytes 23bcff97
- 00bcedc0 ["INT_ADD", "register:40f0:8", ["const:bcedc0:8", "const:4:8"]]
- 00bcedc0 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bcee04 ["INT_ADD", "register:40f0:8", ["const:bcee04:8", "const:4:8"]]
+ 00bcee04 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bcedc0 bytes f0380094
+ 00bcee04 bytes f3380094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cabd5b75834356b5d6e9b6969d5254a4"></a>

### [`00bcf484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf484.md) → [`00bcf4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf4c8.md) FUN_00bcf4c8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf664",
      "incomplete_value": false,
      "site": "00bcf674",
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
            "const:195:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf620",
      "incomplete_value": false,
      "site": "00bcf630",
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
            "const:10a:8"
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
      "definition_site": "00bcf66c",
      "incomplete_value": false,
      "site": "00bcf674",
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
      "definition_site": "00bcf628",
      "incomplete_value": false,
      "site": "00bcf630",
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
      "00bcf5cc",
      "READ",
      [
        "storage",
        "002a91b2",
        null,
        "string"
      ]
    ],
    [
      "00bcf5cc",
      "READ",
      [
        "storage",
        "002a801c",
        null,
        "string"
      ]
    ],
    [
      "00bcf5d4",
      "READ",
      [
        "storage",
        "002a91b6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcf5cc",
      "READ",
      [
        "storage",
        "002a924c",
        null,
        "string"
      ]
    ],
    [
      "00bcf5cc",
      "READ",
      [
        "storage",
        "002a80b6",
        null,
        "string"
      ]
    ],
    [
      "00bcf5d4",
      "READ",
      [
        "storage",
        "002a9250",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf484.md#insn-00bcf630) · [`00bcf4cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf484.md#insn-00bcf4cc) · [`00bcf520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf484.md#insn-00bcf520)
- 新版 [`00bcf674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf4c8.md#insn-00bcf674) · [`00bcf510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf4c8.md#insn-00bcf510) · [`00bcf564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf4c8.md#insn-00bcf564)

~~~diff
- 00bcf630 ["INT_ADD", "register:40f0:8", ["const:bcf630:8", "const:4:8"]]
- 00bcf630 ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bcf674 ["INT_ADD", "register:40f0:8", ["const:bcf674:8", "const:4:8"]]
+ 00bcf674 ["CALL", null, ["callee:00bbb19c:8"]]
- 00bcf630 bytes caaeff97
+ 00bcf674 bytes caaeff97
- 00bcf4cc ["INT_ADD", "register:40f0:8", ["const:bcf4cc:8", "const:4:8"]]
- 00bcf4cc ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcf510 ["INT_ADD", "register:40f0:8", ["const:bcf510:8", "const:4:8"]]
+ 00bcf510 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcf4cc bytes 4d370094
+ 00bcf510 bytes 50370094
- 00bcf520 ["COPY", "tmp:0:8", ["const:1b2:8"]]
- 00bcf520 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00bcf520 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00bcf520 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00bcf564 ["COPY", "tmp:0:8", ["const:24c:8"]]
+ 00bcf564 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00bcf564 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00bcf564 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00bcf520 bytes b5ca0691
+ 00bcf564 bytes b5320991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-701be9648d9516c5d6c6ad8e40ae4f7e"></a>

### [`00bcf63c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf63c.md) → [`00bcf680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf680.md) FUN_00bcf680

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 89.09% / 新版 89.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf748",
      "incomplete_value": false,
      "site": "00bcf758",
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
            "const:195:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf704",
      "incomplete_value": false,
      "site": "00bcf714",
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
            "const:10a:8"
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
      "definition_site": "00bcf750",
      "incomplete_value": false,
      "site": "00bcf758",
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
      "definition_site": "00bcf70c",
      "incomplete_value": false,
      "site": "00bcf714",
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
    "ordinal": 0,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bcf6a0",
      "incomplete_value": false,
      "site": "00bcf6a8",
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
            "const:24c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf65c",
      "incomplete_value": false,
      "site": "00bcf664",
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
            "const:1b2:8"
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
      "00bcf6a0",
      "DATA",
      [
        "storage",
        "002a91b2",
        null,
        "string"
      ]
    ],
    [
      "00bcf6d0",
      "DATA",
      [
        "storage",
        "002a7267",
        null,
        "string"
      ]
    ],
    [
      "00bcf708",
      "READ",
      [
        "storage",
        "002a91b2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcf6a0",
      "DATA",
      [
        "storage",
        "002a924c",
        null,
        "string"
      ]
    ],
    [
      "00bcf6d0",
      "DATA",
      [
        "storage",
        "002a7301",
        null,
        "string"
      ]
    ],
    [
      "00bcf708",
      "READ",
      [
        "storage",
        "002a924c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf63c.md#insn-00bcf714) · [`00bcf65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf63c.md#insn-00bcf65c) · [`00bcf68c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf63c.md#insn-00bcf68c)
- 新版 [`00bcf758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf680.md#insn-00bcf758) · [`00bcf6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf680.md#insn-00bcf6a0) · [`00bcf6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf680.md#insn-00bcf6d0)

~~~diff
- 00bcf714 ["INT_ADD", "register:40f0:8", ["const:bcf714:8", "const:4:8"]]
- 00bcf714 ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bcf758 ["INT_ADD", "register:40f0:8", ["const:bcf758:8", "const:4:8"]]
+ 00bcf758 ["CALL", null, ["callee:00bbb19c:8"]]
- 00bcf714 bytes 91aeff97
+ 00bcf758 bytes 91aeff97
- 00bcf65c ["COPY", "tmp:0:8", ["const:1b2:8"]]
- 00bcf65c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bcf65c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bcf65c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcf6a0 ["COPY", "tmp:0:8", ["const:24c:8"]]
+ 00bcf6a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcf6a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcf6a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bcf65c bytes 00c80691
+ 00bcf6a0 bytes 00300991
- 00bcf68c ["COPY", "tmp:0:8", ["const:267:8"]]
- 00bcf68c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bcf68c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bcf68c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcf6d0 ["COPY", "tmp:0:8", ["const:301:8"]]
+ 00bcf6d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcf6d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcf6d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bcf68c bytes 009c0991
+ 00bcf6d0 bytes 00040c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bee54d1e9498e96239f4274255e2a7c"></a>

### [`00bcf720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf720.md) → [`00bcf764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf764.md) FUN_00bcf764

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.50% / 新版 96.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcf8a4",
      "incomplete_value": true,
      "site": "00bcf8ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:203:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf860",
      "incomplete_value": true,
      "site": "00bcf868",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:178:8"
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
      "definition_site": "00bcf8a8",
      "incomplete_value": true,
      "site": "00bcf8b0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00bcf864",
      "incomplete_value": true,
      "site": "00bcf86c",
      "value": [
        "LOAD",
        "16",
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
      "00bcf8a4",
      "READ",
      [
        "storage",
        "002a4178",
        null,
        "string"
      ]
    ],
    [
      "00bcf8a8",
      "READ",
      [
        "storage",
        "002a4185",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcf8a4",
      "READ",
      [
        "storage",
        "002a4203",
        null,
        "string"
      ]
    ],
    [
      "00bcf8a8",
      "READ",
      [
        "storage",
        "002a4210",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf720.md#insn-00bcf8b0) · [`00bcf768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf720.md#insn-00bcf768) · [`00bcf7ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf720.md#insn-00bcf7ac)
- 新版 [`00bcf8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf764.md#insn-00bcf8f4) · [`00bcf7ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf764.md#insn-00bcf7ac) · [`00bcf7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf764.md#insn-00bcf7f0)

~~~diff
- 00bcf8b0 ["INT_ADD", "register:40f0:8", ["const:bcf8b0:8", "const:4:8"]]
- 00bcf8b0 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcf8f4 ["INT_ADD", "register:40f0:8", ["const:bcf8f4:8", "const:4:8"]]
+ 00bcf8f4 ["CALL", null, ["callee:00bdd250:8"]]
- 00bcf8b0 bytes 54360094
+ 00bcf8f4 bytes 57360094
- 00bcf768 ["INT_ADD", "register:40f0:8", ["const:bcf768:8", "const:4:8"]]
- 00bcf768 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bcf7ac ["INT_ADD", "register:40f0:8", ["const:bcf7ac:8", "const:4:8"]]
+ 00bcf7ac ["CALL", null, ["callee:00bdd250:8"]]
- 00bcf768 bytes a6360094
+ 00bcf7ac bytes a9360094
- 00bcf7ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcf7ac ["INT_ADD", "register:40f0:8", ["const:bcf7ac:8", "const:4:8"]]
- 00bcf7ac ["CALLIND", null, ["register:0:8"]]
+ 00bcf7f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcf7f0 ["INT_ADD", "register:40f0:8", ["const:bcf7f0:8", "const:4:8"]]
+ 00bcf7f0 ["CALLIND", null, ["register:0:8"]]
- 00bcf7ac bytes 00013fd6
+ 00bcf7f0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c20eaa0031cff52ff9085e42f740761"></a>

### [`00bcfc50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfc50.md) → [`00bcfc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfc94.md) FUN_00bcfc94

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc245c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc245c.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bc24a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcfd04",
      "incomplete_value": false,
      "site": "00bcfd04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcfcc0",
      "incomplete_value": false,
      "site": "00bcfcc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:438:8"
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
      "00bcfd04",
      "DATA",
      [
        "storage",
        "00c19438",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bcfd04",
      "DATA",
      [
        "storage",
        "00c19488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcfc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfc50.md#insn-00bcfc90) · [`00bcfcbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfc50.md#insn-00bcfcbc) · [`00bcfd0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfc50.md#insn-00bcfd0c)
- 新版 [`00bcfcd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfc94.md#insn-00bcfcd4) · [`00bcfd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfc94.md#insn-00bcfd00) · [`00bcfd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfc94.md#insn-00bcfd50)

~~~diff
- 00bcfc90 ["INT_ADD", "register:40f0:8", ["const:bcfc90:8", "const:4:8"]]
- 00bcfc90 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bcfcd4 ["INT_ADD", "register:40f0:8", ["const:bcfcd4:8", "const:4:8"]]
+ 00bcfcd4 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bcfc90 bytes 3c350094
+ 00bcfcd4 bytes 3f350094
- 00bcfcbc ["COPY", "tmp:0:8", ["const:438:8"]]
- 00bcfcbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bcfcbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bcfcbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bcfd00 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00bcfd00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bcfd00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bcfd00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bcfcbc bytes 29e11091
+ 00bcfd00 bytes 29211291
- 00bcfd0c ["INT_ADD", "register:40f0:8", ["const:bcfd0c:8", "const:4:8"]]
- 00bcfd0c ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bcfd50 ["INT_ADD", "register:40f0:8", ["const:bcfd50:8", "const:4:8"]]
+ 00bcfd50 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bcfd0c bytes 1d2d0094
+ 00bcfd50 bytes 202d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d62a1c30a1571d23fd71af89a03c287"></a>

### [`00bd023c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd023c.md) → [`00bd0280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0280.md) FUN_00bd0280

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) · 呼出先 3件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 2件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd02ec",
      "incomplete_value": true,
      "site": "00bd02ec",
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
      "definition_site": "00bd02a8",
      "incomplete_value": true,
      "site": "00bd02a8",
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
      "00bd02ec",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd02ec",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd023c.md#insn-00bd0270) · [`00bd0298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd023c.md#insn-00bd0298) · [`00bd02a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd023c.md#insn-00bd02a0)
- 新版 [`00bd02b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0280.md#insn-00bd02b4) · [`00bd02dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0280.md#insn-00bd02dc) · [`00bd02e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0280.md#insn-00bd02e4)

~~~diff
- 00bd0270 ["INT_ADD", "register:40f0:8", ["const:bd0270:8", "const:4:8"]]
- 00bd0270 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bd02b4 ["INT_ADD", "register:40f0:8", ["const:bd02b4:8", "const:4:8"]]
+ 00bd02b4 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bd0270 bytes c4330094
+ 00bd02b4 bytes c7330094
- 00bd0298 ["INT_ADD", "register:40f0:8", ["const:bd0298:8", "const:4:8"]]
- 00bd0298 ["CALL", null, ["callee:00bdb190:8"]]
+ 00bd02dc ["INT_ADD", "register:40f0:8", ["const:bd02dc:8", "const:4:8"]]
+ 00bd02dc ["CALL", null, ["callee:00bdb190:8"]]
- 00bd0298 bytes aa2b0094
+ 00bd02dc bytes ad2b0094
- 00bd02a0 ["COPY", "tmp:0:8", ["const:848:8"]]
- 00bd02a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bd02a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bd02a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bd02e4 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00bd02e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd02e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd02e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bd02a0 bytes 29212191
+ 00bd02e4 bytes 29612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59ce475fb4b4359c8c8d3097741af441"></a>

### [`00bd02e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd02e8.md) → [`00bd032c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd032c.md) FUN_00bd032c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd0394",
      "incomplete_value": false,
      "site": "00bd0394",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0350",
      "incomplete_value": false,
      "site": "00bd0350",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
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
      "00bd0394",
      "DATA",
      [
        "storage",
        "00c195f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd0394",
      "DATA",
      [
        "storage",
        "00c19648",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd02e8.md#insn-00bd0320) · [`00bd0344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd02e8.md#insn-00bd0344) · [`00bd038c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd02e8.md#insn-00bd038c)
- 新版 [`00bd0364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd032c.md#insn-00bd0364) · [`00bd0388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd032c.md#insn-00bd0388) · [`00bd03d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd032c.md#insn-00bd03d0)

~~~diff
- 00bd0320 ["INT_ADD", "register:40f0:8", ["const:bd0320:8", "const:4:8"]]
- 00bd0320 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bd0364 ["INT_ADD", "register:40f0:8", ["const:bd0364:8", "const:4:8"]]
+ 00bd0364 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bd0320 bytes 98330094
+ 00bd0364 bytes 9b330094
- 00bd0344 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 00bd0344 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd0344 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd0344 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd0388 ["COPY", "tmp:0:8", ["const:648:8"]]
+ 00bd0388 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd0388 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd0388 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd0344 bytes 08e11791
+ 00bd0388 bytes 08211991
- 00bd038c ["INT_ADD", "register:40f0:8", ["const:bd038c:8", "const:4:8"]]
- 00bd038c ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bd03d0 ["INT_ADD", "register:40f0:8", ["const:bd03d0:8", "const:4:8"]]
+ 00bd03d0 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bd038c bytes 7d2b0094
+ 00bd03d0 bytes 802b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-273a8f1aa0da8c66b430317879250bd6"></a>

### [`00bd0918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0918.md) → [`00bd095c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd095c.md) FUN_00bd095c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd09c0",
      "incomplete_value": true,
      "site": "00bd09d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:499:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd097c",
      "incomplete_value": true,
      "site": "00bd0990",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00bd09c0",
      "READ",
      [
        "storage",
        "00294526",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd09c0",
      "READ",
      [
        "storage",
        "00294499",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd095c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0918.md#insn-00bd095c) · [`00bd0974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0918.md#insn-00bd0974) · [`00bd09a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0918.md#insn-00bd09a4)
- 新版 [`00bd09a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd095c.md#insn-00bd09a0) · [`00bd09b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd095c.md#insn-00bd09b8) · [`00bd09e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd095c.md#insn-00bd09e8)

~~~diff
- 00bd095c ["INT_ADD", "register:40f0:8", ["const:bd095c:8", "const:4:8"]]
- 00bd095c ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd09a0 ["INT_ADD", "register:40f0:8", ["const:bd09a0:8", "const:4:8"]]
+ 00bd09a0 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd095c bytes 29320094
+ 00bd09a0 bytes 2c320094
- 00bd0974 ["COPY", "tmp:0:8", ["const:526:8"]]
- 00bd0974 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bd0974 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bd0974 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bd09b8 ["COPY", "tmp:0:8", ["const:499:8"]]
+ 00bd09b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00bd09b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00bd09b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bd0974 bytes 4a991491
+ 00bd09b8 bytes 4a651291
- 00bd09a4 ["INT_ADD", "register:40f0:8", ["const:bd09a4:8", "const:4:8"]]
- 00bd09a4 ["CALL", null, ["callee:00bc82d4:8"]]
+ 00bd09e8 ["INT_ADD", "register:40f0:8", ["const:bd09e8:8", "const:4:8"]]
+ 00bd09e8 ["CALL", null, ["callee:00bc82d4:8"]]
- 00bd09a4 bytes 3bdeff97
+ 00bd09e8 bytes 3bdeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bf8606caf6f1747ef2d38000cb771bb"></a>

### [`00bd118c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd118c.md) → [`00bd11d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd11d0.md) FUN_00bd11d0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 8件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md)
- 新版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 8件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.24% / 新版 97.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd13c8",
      "incomplete_value": false,
      "site": "00bd13c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1384",
      "incomplete_value": false,
      "site": "00bd1384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "definition_site": "00bd13ec",
      "incomplete_value": false,
      "site": "00bd13ec",
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
            "const:b64:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd13a8",
      "incomplete_value": false,
      "site": "00bd13a8",
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
            "const:bf1:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd1478",
      "incomplete_value": false,
      "site": "00bd1478",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1434",
      "incomplete_value": false,
      "site": "00bd1434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "00bd13c8",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd13ec",
      "DATA",
      [
        "storage",
        "00298bf1",
        null,
        "string"
      ]
    ],
    [
      "00bd1478",
      "DATA",
      [
        "storage",
        "00c19a58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd13c8",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd13ec",
      "DATA",
      [
        "storage",
        "00298b64",
        null,
        "string"
      ]
    ],
    [
      "00bd1478",
      "DATA",
      [
        "storage",
        "00c19aa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd118c.md#insn-00bd1730) · [`00bd1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd118c.md#insn-00bd1290) · [`00bd12d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd118c.md#insn-00bd12d8)
- 新版 [`00bd1774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd11d0.md#insn-00bd1774) · [`00bd12d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd11d0.md#insn-00bd12d4) · [`00bd131c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd11d0.md#insn-00bd131c)

~~~diff
- 00bd1730 ["INT_ADD", "register:40f0:8", ["const:bd1730:8", "const:4:8"]]
- 00bd1730 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bd1774 ["INT_ADD", "register:40f0:8", ["const:bd1774:8", "const:4:8"]]
+ 00bd1774 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bd1730 bytes 94260094
+ 00bd1774 bytes 97260094
- 00bd1290 ["INT_ADD", "register:40f0:8", ["const:bd1290:8", "const:4:8"]]
- 00bd1290 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd12d4 ["INT_ADD", "register:40f0:8", ["const:bd12d4:8", "const:4:8"]]
+ 00bd12d4 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd1290 bytes dc2f0094
+ 00bd12d4 bytes df2f0094
- 00bd12d8 ["INT_ADD", "register:40f0:8", ["const:bd12d8:8", "const:4:8"]]
- 00bd12d8 ["CALL", null, ["callee:00bbde5c:8"]]
+ 00bd131c ["INT_ADD", "register:40f0:8", ["const:bd131c:8", "const:4:8"]]
+ 00bd131c ["CALL", null, ["callee:00bbde5c:8"]]
- 00bd12d8 bytes d0b2ff97
+ 00bd131c bytes d0b2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4086220dbd4676802af8c86c42ebd761"></a>

### [`00bd1734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1734.md) → [`00bd1778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1778.md) FUN_00bd1778

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bd1734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1734.md) · 呼出先 5件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bc1710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1710.md) [`00bd1734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1734.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 2件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bd1778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1778.md) · 呼出先 5件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bc1754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1754.md) [`00bd1778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1778.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.97% / 新版 97.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd19f8",
      "incomplete_value": false,
      "site": "00bd19f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd19b4",
      "incomplete_value": false,
      "site": "00bd19b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd1b08",
      "incomplete_value": false,
      "site": "00bd1b08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1ac4",
      "incomplete_value": false,
      "site": "00bd1ac4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "ordinal": 45,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd1970",
      "DATA",
      [
        "storage",
        "00c19c88",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd19f8",
      "DATA",
      [
        "storage",
        "00c19c18",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd1b08",
      "DATA",
      [
        "storage",
        "00c19ba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd1970",
      "DATA",
      [
        "storage",
        "00c19cd8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd19f8",
      "DATA",
      [
        "storage",
        "00c19c68",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd1b08",
      "DATA",
      [
        "storage",
        "00c19bf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1734.md#insn-00bd1b08) · [`00bd1850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1734.md#insn-00bd1850) · [`00bd18cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1734.md#insn-00bd18cc)
- 新版 [`00bd1b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1778.md#insn-00bd1b4c) · [`00bd1894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1778.md#insn-00bd1894) · [`00bd1910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1778.md#insn-00bd1910)

~~~diff
- 00bd1b08 ["INT_ADD", "register:40f0:8", ["const:bd1b08:8", "const:4:8"]]
- 00bd1b08 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bd1b4c ["INT_ADD", "register:40f0:8", ["const:bd1b4c:8", "const:4:8"]]
+ 00bd1b4c ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bd1b08 bytes 9e250094
+ 00bd1b4c bytes a1250094
- 00bd1850 ["INT_ADD", "register:40f0:8", ["const:bd1850:8", "const:4:8"]]
- 00bd1850 ["CALL", null, ["callee:00bc1754:8"]]
+ 00bd1894 ["INT_ADD", "register:40f0:8", ["const:bd1894:8", "const:4:8"]]
+ 00bd1894 ["CALL", null, ["callee:00bc1754:8"]]
- 00bd1850 bytes b0bfff97
+ 00bd1894 bytes b0bfff97
- 00bd18cc ["INT_ADD", "register:40f0:8", ["const:bd18cc:8", "const:4:8"]]
- 00bd18cc ["CALL", null, ["callee:00bbde5c:8"]]
+ 00bd1910 ["INT_ADD", "register:40f0:8", ["const:bd1910:8", "const:4:8"]]
+ 00bd1910 ["CALL", null, ["callee:00bbde5c:8"]]
- 00bd18cc bytes 53b1ff97
+ 00bd1910 bytes 53b1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73fefaf673cd3b0200afee22a5dcdc25"></a>

### [`00bd1b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1b0c.md) → [`00bd1b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1b50.md) FUN_00bd1b50

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 3件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

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
      "definition_site": "00bd1bbc",
      "incomplete_value": false,
      "site": "00bd1bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1b78",
      "incomplete_value": false,
      "site": "00bd1b78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "00bd1bbc",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd1bbc",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1b0c.md#insn-00bd1b40) · [`00bd1b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1b0c.md#insn-00bd1b68) · [`00bd1b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1b0c.md#insn-00bd1b70)
- 新版 [`00bd1b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1b50.md#insn-00bd1b84) · [`00bd1bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1b50.md#insn-00bd1bac) · [`00bd1bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1b50.md#insn-00bd1bb4)

~~~diff
- 00bd1b40 ["INT_ADD", "register:40f0:8", ["const:bd1b40:8", "const:4:8"]]
- 00bd1b40 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bd1b84 ["INT_ADD", "register:40f0:8", ["const:bd1b84:8", "const:4:8"]]
+ 00bd1b84 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bd1b40 bytes 902d0094
+ 00bd1b84 bytes 932d0094
- 00bd1b68 ["INT_ADD", "register:40f0:8", ["const:bd1b68:8", "const:4:8"]]
- 00bd1b68 ["CALL", null, ["callee:00bdb190:8"]]
+ 00bd1bac ["INT_ADD", "register:40f0:8", ["const:bd1bac:8", "const:4:8"]]
+ 00bd1bac ["CALL", null, ["callee:00bdb190:8"]]
- 00bd1b68 bytes 76250094
+ 00bd1bac bytes 79250094
- 00bd1b70 ["COPY", "tmp:0:8", ["const:848:8"]]
- 00bd1b70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bd1b70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bd1b70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bd1bb4 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00bd1bb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd1bb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd1bb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bd1b70 bytes 29212191
+ 00bd1bb4 bytes 29612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3affa9e1ce54f057b222e6f1c0ce54c"></a>

### [`00bd1bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1bb8.md) → [`00bd1bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1bfc.md) FUN_00bd1bfc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 3件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

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
      "definition_site": "00bd1c68",
      "incomplete_value": false,
      "site": "00bd1c68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1c24",
      "incomplete_value": false,
      "site": "00bd1c24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "00bd1c68",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd1c68",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1bec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1bb8.md#insn-00bd1bec) · [`00bd1c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1bb8.md#insn-00bd1c14) · [`00bd1c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1bb8.md#insn-00bd1c1c)
- 新版 [`00bd1c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1bfc.md#insn-00bd1c30) · [`00bd1c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1bfc.md#insn-00bd1c58) · [`00bd1c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1bfc.md#insn-00bd1c60)

~~~diff
- 00bd1bec ["INT_ADD", "register:40f0:8", ["const:bd1bec:8", "const:4:8"]]
- 00bd1bec ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bd1c30 ["INT_ADD", "register:40f0:8", ["const:bd1c30:8", "const:4:8"]]
+ 00bd1c30 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bd1bec bytes 652d0094
+ 00bd1c30 bytes 682d0094
- 00bd1c14 ["INT_ADD", "register:40f0:8", ["const:bd1c14:8", "const:4:8"]]
- 00bd1c14 ["CALL", null, ["callee:00bdb190:8"]]
+ 00bd1c58 ["INT_ADD", "register:40f0:8", ["const:bd1c58:8", "const:4:8"]]
+ 00bd1c58 ["CALL", null, ["callee:00bdb190:8"]]
- 00bd1c14 bytes 4b250094
+ 00bd1c58 bytes 4e250094
- 00bd1c1c ["COPY", "tmp:0:8", ["const:848:8"]]
- 00bd1c1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bd1c1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bd1c1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bd1c60 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00bd1c60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd1c60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd1c60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bd1c1c bytes 29212191
+ 00bd1c60 bytes 29612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3c852c381f370c727ffd8ed71242b9d"></a>

### [`00bd1c64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1c64.md) → [`00bd1ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ca8.md) FUN_00bd1ca8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 3件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

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
      "definition_site": "00bd1d14",
      "incomplete_value": false,
      "site": "00bd1d14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1cd0",
      "incomplete_value": false,
      "site": "00bd1cd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "00bd1d14",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd1d14",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1c64.md#insn-00bd1c98) · [`00bd1cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1c64.md#insn-00bd1cc0) · [`00bd1cc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1c64.md#insn-00bd1cc8)
- 新版 [`00bd1cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ca8.md#insn-00bd1cdc) · [`00bd1d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ca8.md#insn-00bd1d04) · [`00bd1d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ca8.md#insn-00bd1d0c)

~~~diff
- 00bd1c98 ["INT_ADD", "register:40f0:8", ["const:bd1c98:8", "const:4:8"]]
- 00bd1c98 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bd1cdc ["INT_ADD", "register:40f0:8", ["const:bd1cdc:8", "const:4:8"]]
+ 00bd1cdc ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bd1c98 bytes 3a2d0094
+ 00bd1cdc bytes 3d2d0094
- 00bd1cc0 ["INT_ADD", "register:40f0:8", ["const:bd1cc0:8", "const:4:8"]]
- 00bd1cc0 ["CALL", null, ["callee:00bdb190:8"]]
+ 00bd1d04 ["INT_ADD", "register:40f0:8", ["const:bd1d04:8", "const:4:8"]]
+ 00bd1d04 ["CALL", null, ["callee:00bdb190:8"]]
- 00bd1cc0 bytes 20250094
+ 00bd1d04 bytes 23250094
- 00bd1cc8 ["COPY", "tmp:0:8", ["const:848:8"]]
- 00bd1cc8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bd1cc8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bd1cc8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bd1d0c ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00bd1d0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd1d0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd1d0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bd1cc8 bytes 29212191
+ 00bd1d0c bytes 29612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fbacaf36095092a067e45959223f6fc"></a>

### [`00bd1d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1d10.md) → [`00bd1d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1d54.md) FUN_00bd1d54

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

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
      "definition_site": "00bd1dbc",
      "incomplete_value": false,
      "site": "00bd1dbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1d78",
      "incomplete_value": false,
      "site": "00bd1d78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
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
      "00bd1dbc",
      "DATA",
      [
        "storage",
        "00c19cf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd1dbc",
      "DATA",
      [
        "storage",
        "00c19d48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1d10.md#insn-00bd1d48) · [`00bd1d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1d10.md#insn-00bd1d6c) · [`00bd1db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1d10.md#insn-00bd1db8)
- 新版 [`00bd1d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1d54.md#insn-00bd1d8c) · [`00bd1db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1d54.md#insn-00bd1db0) · [`00bd1dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1d54.md#insn-00bd1dfc)

~~~diff
- 00bd1d48 ["INT_ADD", "register:40f0:8", ["const:bd1d48:8", "const:4:8"]]
- 00bd1d48 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bd1d8c ["INT_ADD", "register:40f0:8", ["const:bd1d8c:8", "const:4:8"]]
+ 00bd1d8c ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bd1d48 bytes 0e2d0094
+ 00bd1d8c bytes 112d0094
- 00bd1d6c ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 00bd1d6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1d6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1d6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd1db0 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 00bd1db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd1d6c bytes 08e13391
+ 00bd1db0 bytes 08213591
- 00bd1db8 ["INT_ADD", "register:40f0:8", ["const:bd1db8:8", "const:4:8"]]
- 00bd1db8 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bd1dfc ["INT_ADD", "register:40f0:8", ["const:bd1dfc:8", "const:4:8"]]
+ 00bd1dfc ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bd1db8 bytes f2240094
+ 00bd1dfc bytes f5240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35a23f9b715bb71aa1fcc10caccb2c25"></a>

### [`00bd1dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1dbc.md) → [`00bd1e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1e00.md) FUN_00bd1e00

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd1e64",
      "incomplete_value": true,
      "site": "00bd1e64",
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
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1e20",
      "incomplete_value": true,
      "site": "00bd1e20",
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
            "const:d68:8"
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
      "00bd1e64",
      "DATA",
      [
        "storage",
        "00c19d68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd1e64",
      "DATA",
      [
        "storage",
        "00c19db8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1dbc.md#insn-00bd1df0) · [`00bd1e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1dbc.md#insn-00bd1e14) · [`00bd1e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1dbc.md#insn-00bd1e58)
- 新版 [`00bd1e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1e00.md#insn-00bd1e34) · [`00bd1e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1e00.md#insn-00bd1e58) · [`00bd1e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1e00.md#insn-00bd1e9c)

~~~diff
- 00bd1df0 ["INT_ADD", "register:40f0:8", ["const:bd1df0:8", "const:4:8"]]
- 00bd1df0 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bd1e34 ["INT_ADD", "register:40f0:8", ["const:bd1e34:8", "const:4:8"]]
+ 00bd1e34 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bd1df0 bytes e42c0094
+ 00bd1e34 bytes e72c0094
- 00bd1e14 ["COPY", "tmp:0:8", ["const:d68:8"]]
- 00bd1e14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1e14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1e14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd1e58 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 00bd1e58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1e58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1e58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd1e14 bytes 08a13591
+ 00bd1e58 bytes 08e13691
- 00bd1e58 ["INT_ADD", "register:40f0:8", ["const:bd1e58:8", "const:4:8"]]
- 00bd1e58 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bd1e9c ["INT_ADD", "register:40f0:8", ["const:bd1e9c:8", "const:4:8"]]
+ 00bd1e9c ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bd1e58 bytes ca240094
+ 00bd1e9c bytes cd240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ef92c32fe15284b45aee2c4882fa98b"></a>

### [`00bd1e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1e5c.md) → [`00bd1ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ea0.md) FUN_00bd1ea0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

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
      "definition_site": "00bd1f08",
      "incomplete_value": false,
      "site": "00bd1f08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1ec4",
      "incomplete_value": false,
      "site": "00bd1ec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
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
      "00bd1f08",
      "DATA",
      [
        "storage",
        "00c19dd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd1f08",
      "DATA",
      [
        "storage",
        "00c19e28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1e5c.md#insn-00bd1e94) · [`00bd1eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1e5c.md#insn-00bd1eb8) · [`00bd1f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1e5c.md#insn-00bd1f04)
- 新版 [`00bd1ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ea0.md#insn-00bd1ed8) · [`00bd1efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ea0.md#insn-00bd1efc) · [`00bd1f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ea0.md#insn-00bd1f48)

~~~diff
- 00bd1e94 ["INT_ADD", "register:40f0:8", ["const:bd1e94:8", "const:4:8"]]
- 00bd1e94 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bd1ed8 ["INT_ADD", "register:40f0:8", ["const:bd1ed8:8", "const:4:8"]]
+ 00bd1ed8 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bd1e94 bytes bb2c0094
+ 00bd1ed8 bytes be2c0094
- 00bd1eb8 ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 00bd1eb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1eb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1eb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd1efc ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 00bd1efc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1efc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1efc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd1eb8 bytes 08613791
+ 00bd1efc bytes 08a13891
- 00bd1f04 ["INT_ADD", "register:40f0:8", ["const:bd1f04:8", "const:4:8"]]
- 00bd1f04 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bd1f48 ["INT_ADD", "register:40f0:8", ["const:bd1f48:8", "const:4:8"]]
+ 00bd1f48 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bd1f04 bytes 9f240094
+ 00bd1f48 bytes a2240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2f84f710a20f4b47857a50381460f7a"></a>

### [`00bd1f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1f08.md) → [`00bd1f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1f4c.md) FUN_00bd1f4c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd1fb4",
      "incomplete_value": true,
      "site": "00bd1fb4",
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
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1f70",
      "incomplete_value": true,
      "site": "00bd1f70",
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
            "const:e48:8"
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
      "00bd1fb4",
      "DATA",
      [
        "storage",
        "00c19e48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd1fb4",
      "DATA",
      [
        "storage",
        "00c19e98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1f08.md#insn-00bd1f40) · [`00bd1f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1f08.md#insn-00bd1f64) · [`00bd1fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1f08.md#insn-00bd1fb0)
- 新版 [`00bd1f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1f4c.md#insn-00bd1f84) · [`00bd1fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1f4c.md#insn-00bd1fa8) · [`00bd1ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1f4c.md#insn-00bd1ff4)

~~~diff
- 00bd1f40 ["INT_ADD", "register:40f0:8", ["const:bd1f40:8", "const:4:8"]]
- 00bd1f40 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bd1f84 ["INT_ADD", "register:40f0:8", ["const:bd1f84:8", "const:4:8"]]
+ 00bd1f84 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bd1f40 bytes 902c0094
+ 00bd1f84 bytes 932c0094
- 00bd1f64 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00bd1f64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1f64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1f64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd1fa8 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00bd1fa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1fa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1fa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd1f64 bytes 08213991
+ 00bd1fa8 bytes 08613a91
- 00bd1fb0 ["INT_ADD", "register:40f0:8", ["const:bd1fb0:8", "const:4:8"]]
- 00bd1fb0 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bd1ff4 ["INT_ADD", "register:40f0:8", ["const:bd1ff4:8", "const:4:8"]]
+ 00bd1ff4 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bd1fb0 bytes 74240094
+ 00bd1ff4 bytes 77240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1054e44071a706e257718a2bee8cf16"></a>

### [`00bd1fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1fb4.md) → [`00bd1ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ff8.md) FUN_00bd1ff8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 6件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bd397c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd397c.md) [`00bd3a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3a1c.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md)
- 新版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 6件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bd39c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd39c0.md) [`00bd3a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3a60.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.57% / 新版 96.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd20f4",
      "incomplete_value": false,
      "site": "00bd20f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd20b0",
      "incomplete_value": false,
      "site": "00bd20b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "definition_site": "00bd21d0",
      "incomplete_value": false,
      "site": "00bd21d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd218c",
      "incomplete_value": false,
      "site": "00bd218c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "definition_site": "00bd226c",
      "incomplete_value": false,
      "site": "00bd226c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2228",
      "incomplete_value": false,
      "site": "00bd2228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "00bd20f4",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd21d0",
      "DATA",
      [
        "storage",
        "00c19f28",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd226c",
      "DATA",
      [
        "storage",
        "00c19f28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd20f4",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd21d0",
      "DATA",
      [
        "storage",
        "00c19f78",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd226c",
      "DATA",
      [
        "storage",
        "00c19f78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd21d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1fb4.md#insn-00bd21d0) · [`00bd226c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1fb4.md#insn-00bd226c) · [`00bd2078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1fb4.md#insn-00bd2078)
- 新版 [`00bd2214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ff8.md#insn-00bd2214) · [`00bd22b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ff8.md#insn-00bd22b0) · [`00bd20bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ff8.md#insn-00bd20bc)

~~~diff
- 00bd21d0 ["INT_ADD", "register:40f0:8", ["const:bd21d0:8", "const:4:8"]]
- 00bd21d0 ["CALL", null, ["callee:00bbde5c:8"]]
+ 00bd2214 ["INT_ADD", "register:40f0:8", ["const:bd2214:8", "const:4:8"]]
+ 00bd2214 ["CALL", null, ["callee:00bbde5c:8"]]
- 00bd21d0 bytes 12afff97
+ 00bd2214 bytes 12afff97
- 00bd226c ["INT_ADD", "register:40f0:8", ["const:bd226c:8", "const:4:8"]]
- 00bd226c ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bd22b0 ["INT_ADD", "register:40f0:8", ["const:bd22b0:8", "const:4:8"]]
+ 00bd22b0 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bd226c bytes c5230094
+ 00bd22b0 bytes c8230094
- 00bd2078 ["INT_ADD", "register:40f0:8", ["const:bd2078:8", "const:4:8"]]
- 00bd2078 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bd20bc ["INT_ADD", "register:40f0:8", ["const:bd20bc:8", "const:4:8"]]
+ 00bd20bc ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bd2078 bytes 422c0094
+ 00bd20bc bytes 452c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84910765f533c91326989fc419c08795"></a>

### [`00bd2270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2270.md) → [`00bd22b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd22b4.md) FUN_00bd22b4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 3件 [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 3件 [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd23c0",
      "incomplete_value": false,
      "site": "00bd23c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c1a000:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd237c",
      "incomplete_value": false,
      "site": "00bd237c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c1a000:8"
          ],
          [
            "leaf",
            "const:78:8"
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
      "00bd23c0",
      "DATA",
      [
        "storage",
        "00c1a078",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd23e0",
      "DATA",
      [
        "storage",
        "002a3069",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd23c0",
      "DATA",
      [
        "storage",
        "00c1a0c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd23e0",
      "DATA",
      [
        "storage",
        "002a30f4",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd22e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2270.md#insn-00bd22e8) · [`00bd2308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2270.md#insn-00bd2308) · [`00bd2320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2270.md#insn-00bd2320)
- 新版 [`00bd232c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd22b4.md#insn-00bd232c) · [`00bd234c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd22b4.md#insn-00bd234c) · [`00bd2364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd22b4.md#insn-00bd2364)

~~~diff
- 00bd22e8 ["COPY", "tmp:0:8", ["const:69:8"]]
- 00bd22e8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00bd22e8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00bd22e8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00bd232c ["COPY", "tmp:0:8", ["const:f4:8"]]
+ 00bd232c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00bd232c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00bd232c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00bd22e8 bytes 73a60191
+ 00bd232c bytes 73d20391
- 00bd2308 ["COPY", "tmp:0:8", ["const:7e8:8"]]
- 00bd2308 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00bd2308 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00bd2308 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00bd234c ["COPY", "tmp:0:8", ["const:7e6:8"]]
+ 00bd234c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00bd234c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00bd234c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00bd2308 bytes 73a21f91
+ 00bd234c bytes 739a1f91
- 00bd2320 ["INT_ADD", "register:40f0:8", ["const:bd2320:8", "const:4:8"]]
- 00bd2320 ["CALL", null, ["callee:00bbf39c:8"]]
+ 00bd2364 ["INT_ADD", "register:40f0:8", ["const:bd2364:8", "const:4:8"]]
+ 00bd2364 ["CALL", null, ["callee:00bbf39c:8"]]
- 00bd2320 bytes 0eb4ff97
+ 00bd2364 bytes 0eb4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4e13dcef4060fdbfe611d66d2ee8371"></a>

### [`00bd23c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd23c0.md) → [`00bd2404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2404.md) FUN_00bd2404

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

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
      "definition_site": "00bd246c",
      "incomplete_value": false,
      "site": "00bd246c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c1a000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2428",
      "incomplete_value": false,
      "site": "00bd2428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c1a000:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "00bd246c",
      "DATA",
      [
        "storage",
        "00c1a0e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd246c",
      "DATA",
      [
        "storage",
        "00c1a138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd23f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd23c0.md#insn-00bd23f4) · [`00bd2420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd23c0.md#insn-00bd2420) · [`00bd2468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd23c0.md#insn-00bd2468)
- 新版 [`00bd2438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2404.md#insn-00bd2438) · [`00bd2464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2404.md#insn-00bd2464) · [`00bd24ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2404.md#insn-00bd24ac)

~~~diff
- 00bd23f4 ["INT_ADD", "register:40f0:8", ["const:bd23f4:8", "const:4:8"]]
- 00bd23f4 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bd2438 ["INT_ADD", "register:40f0:8", ["const:bd2438:8", "const:4:8"]]
+ 00bd2438 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bd23f4 bytes 632b0094
+ 00bd2438 bytes 662b0094
- 00bd2420 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 00bd2420 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2420 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2420 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd2464 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 00bd2464 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd2464 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd2464 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd2420 bytes 08a10391
+ 00bd2464 bytes 08e10491
- 00bd2468 ["INT_ADD", "register:40f0:8", ["const:bd2468:8", "const:4:8"]]
- 00bd2468 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bd24ac ["INT_ADD", "register:40f0:8", ["const:bd24ac:8", "const:4:8"]]
+ 00bd24ac ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bd2468 bytes 46230094
+ 00bd24ac bytes 49230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ed8232c5747c578d36d6fdab1941291"></a>

### [`00bd246c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd246c.md) → [`00bd24b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd24b0.md) FUN_00bd24b0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd2524",
      "incomplete_value": false,
      "site": "00bd2524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c1a000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd24e0",
      "incomplete_value": false,
      "site": "00bd24e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c1a000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "00bd2524",
      "DATA",
      [
        "storage",
        "00c1a158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd2524",
      "DATA",
      [
        "storage",
        "00c1a1a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd246c.md#insn-00bd2524) · [`00bd24a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd246c.md#insn-00bd24a4) · [`00bd24d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd246c.md#insn-00bd24d0)
- 新版 [`00bd2568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd24b0.md#insn-00bd2568) · [`00bd24e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd24b0.md#insn-00bd24e8) · [`00bd2514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd24b0.md#insn-00bd2514)

~~~diff
- 00bd2524 ["INT_ADD", "register:40f0:8", ["const:bd2524:8", "const:4:8"]]
- 00bd2524 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bd2568 ["INT_ADD", "register:40f0:8", ["const:bd2568:8", "const:4:8"]]
+ 00bd2568 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bd2524 bytes 17230094
+ 00bd2568 bytes 1a230094
- 00bd24a4 ["INT_ADD", "register:40f0:8", ["const:bd24a4:8", "const:4:8"]]
- 00bd24a4 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bd24e8 ["INT_ADD", "register:40f0:8", ["const:bd24e8:8", "const:4:8"]]
+ 00bd24e8 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bd24a4 bytes 372b0094
+ 00bd24e8 bytes 3a2b0094
- 00bd24d0 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00bd24d0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bd24d0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bd24d0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bd2514 ["COPY", "tmp:0:8", ["const:1a8:8"]]
+ 00bd2514 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00bd2514 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00bd2514 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bd24d0 bytes 4a610591
+ 00bd2514 bytes 4aa10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c227d92091fe744712ccd9b79a7fba0"></a>

### [`00bd2528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2528.md) → [`00bd256c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd256c.md) FUN_00bd256c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd25f0",
      "incomplete_value": false,
      "site": "00bd25f0",
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
            "const:854:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd25ac",
      "incomplete_value": false,
      "site": "00bd25ac",
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
            "const:8e1:8"
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
      "00bd25d0",
      "DATA",
      [
        "storage",
        "00c19e48",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd25f0",
      "DATA",
      [
        "storage",
        "002978e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd25d0",
      "DATA",
      [
        "storage",
        "00c19e98",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd25f0",
      "DATA",
      [
        "storage",
        "00297854",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd255c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2528.md#insn-00bd255c) · [`00bd2580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2528.md#insn-00bd2580) · [`00bd25a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2528.md#insn-00bd25a4)
- 新版 [`00bd25a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd256c.md#insn-00bd25a0) · [`00bd25c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd256c.md#insn-00bd25c4) · [`00bd25e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd256c.md#insn-00bd25e8)

~~~diff
- 00bd255c ["INT_ADD", "register:40f0:8", ["const:bd255c:8", "const:4:8"]]
- 00bd255c ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bd25a0 ["INT_ADD", "register:40f0:8", ["const:bd25a0:8", "const:4:8"]]
+ 00bd25a0 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bd255c bytes 092b0094
+ 00bd25a0 bytes 0c2b0094
- 00bd2580 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00bd2580 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2580 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2580 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd25c4 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00bd25c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd25c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd25c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd2580 bytes 08213991
+ 00bd25c4 bytes 08613a91
- 00bd25a4 ["COPY", "tmp:0:8", ["const:8e1:8"]]
- 00bd25a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bd25a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bd25a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bd25e8 ["COPY", "tmp:0:8", ["const:854:8"]]
+ 00bd25e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd25e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd25e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bd25a4 bytes 29852391
+ 00bd25e8 bytes 29512191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6276d0d7106b5f47e26976964cc4165"></a>

### [`00bd25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd25d8.md) → [`00bd261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd261c.md) FUN_00bd261c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd2680",
      "incomplete_value": false,
      "site": "00bd2680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd263c",
      "incomplete_value": false,
      "site": "00bd263c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "00bd2680",
      "DATA",
      [
        "storage",
        "00c19e48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd2680",
      "DATA",
      [
        "storage",
        "00c19e98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd260c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd25d8.md#insn-00bd260c) · [`00bd2630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd25d8.md#insn-00bd2630) · [`00bd2684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd25d8.md#insn-00bd2684)
- 新版 [`00bd2650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd261c.md#insn-00bd2650) · [`00bd2674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd261c.md#insn-00bd2674) · [`00bd26c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd261c.md#insn-00bd26c8)

~~~diff
- 00bd260c ["INT_ADD", "register:40f0:8", ["const:bd260c:8", "const:4:8"]]
- 00bd260c ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bd2650 ["INT_ADD", "register:40f0:8", ["const:bd2650:8", "const:4:8"]]
+ 00bd2650 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bd260c bytes dd2a0094
+ 00bd2650 bytes e02a0094
- 00bd2630 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00bd2630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd2674 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00bd2674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd2674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd2674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd2630 bytes 08213991
+ 00bd2674 bytes 08613a91
- 00bd2684 ["INT_ADD", "register:40f0:8", ["const:bd2684:8", "const:4:8"]]
- 00bd2684 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bd26c8 ["INT_ADD", "register:40f0:8", ["const:bd26c8:8", "const:4:8"]]
+ 00bd26c8 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bd2684 bytes bf220094
+ 00bd26c8 bytes c2220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5564bd4cffc093ed7d821f5bc6a3d8d"></a>

### [`00bd35e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd35e8.md) → [`00bd362c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd362c.md) FUN_00bd362c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.37% / 新版 98.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd3694",
      "incomplete_value": true,
      "site": "00bd36a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:85d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd3650",
      "incomplete_value": true,
      "site": "00bd365c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8ea:8"
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
      "00bd3694",
      "READ",
      [
        "storage",
        "002978ea",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd3694",
      "READ",
      [
        "storage",
        "0029785d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd3634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd35e8.md#insn-00bd3634) · [`00bd3648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd35e8.md#insn-00bd3648) · [`00bd3694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd35e8.md#insn-00bd3694)
- 新版 [`00bd3678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd362c.md#insn-00bd3678) · [`00bd368c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd362c.md#insn-00bd368c) · [`00bd36d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd362c.md#insn-00bd36d8)

~~~diff
- 00bd3634 ["INT_ADD", "register:40f0:8", ["const:bd3634:8", "const:4:8"]]
- 00bd3634 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd3678 ["INT_ADD", "register:40f0:8", ["const:bd3678:8", "const:4:8"]]
+ 00bd3678 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd3634 bytes f3260094
+ 00bd3678 bytes f6260094
- 00bd3648 ["COPY", "tmp:0:8", ["const:8ea:8"]]
- 00bd3648 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bd3648 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bd3648 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bd368c ["COPY", "tmp:0:8", ["const:85d:8"]]
+ 00bd368c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd368c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd368c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bd3648 bytes 29a92391
+ 00bd368c bytes 29752191
- 00bd3694 ["INT_ADD", "register:40f0:8", ["const:bd3694:8", "const:4:8"]]
- 00bd3694 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd36d8 ["INT_ADD", "register:40f0:8", ["const:bd36d8:8", "const:4:8"]]
+ 00bd36d8 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd3694 bytes db260094
+ 00bd36d8 bytes de260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ace92e6ccb397101f086c52df5c67fb2"></a>

### [`00bd397c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd397c.md) → [`00bd39c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd39c0.md) FUN_00bd39c0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bd1fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1fb4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bd1ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ff8.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd3a24",
      "incomplete_value": false,
      "site": "00bd3a24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd39e0",
      "incomplete_value": false,
      "site": "00bd39e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
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
      "00bd3a24",
      "DATA",
      [
        "storage",
        "00c19eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd3a24",
      "DATA",
      [
        "storage",
        "00c19f08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd39b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd397c.md#insn-00bd39b0) · [`00bd39d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd397c.md#insn-00bd39d4) · [`00bd3a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd397c.md#insn-00bd3a18)
- 新版 [`00bd39f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd39c0.md#insn-00bd39f4) · [`00bd3a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd39c0.md#insn-00bd3a18) · [`00bd3a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd39c0.md#insn-00bd3a5c)

~~~diff
- 00bd39b0 ["INT_ADD", "register:40f0:8", ["const:bd39b0:8", "const:4:8"]]
- 00bd39b0 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bd39f4 ["INT_ADD", "register:40f0:8", ["const:bd39f4:8", "const:4:8"]]
+ 00bd39f4 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bd39b0 bytes f4250094
+ 00bd39f4 bytes f7250094
- 00bd39d4 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 00bd39d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd39d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd39d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd3a18 ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 00bd3a18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd3a18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd3a18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd39d4 bytes 08e13a91
+ 00bd3a18 bytes 08213c91
- 00bd3a18 ["INT_ADD", "register:40f0:8", ["const:bd3a18:8", "const:4:8"]]
- 00bd3a18 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bd3a5c ["INT_ADD", "register:40f0:8", ["const:bd3a5c:8", "const:4:8"]]
+ 00bd3a5c ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bd3a18 bytes da1d0094
+ 00bd3a5c bytes dd1d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c429365ecae16cc054cf9e663bf012c"></a>

### [`00bd3a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3a1c.md) → [`00bd3a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3a60.md) FUN_00bd3a60

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bd1fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1fb4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bd1ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ff8.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd3ac8",
      "incomplete_value": false,
      "site": "00bd3ac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd3a84",
      "incomplete_value": false,
      "site": "00bd3a84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "00bd3ac8",
      "DATA",
      [
        "storage",
        "00c19f28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd3ac8",
      "DATA",
      [
        "storage",
        "00c19f78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd3a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3a1c.md#insn-00bd3a54) · [`00bd3a78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3a1c.md#insn-00bd3a78) · [`00bd3ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3a1c.md#insn-00bd3ac0)
- 新版 [`00bd3a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3a60.md#insn-00bd3a98) · [`00bd3abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3a60.md#insn-00bd3abc) · [`00bd3b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3a60.md#insn-00bd3b04)

~~~diff
- 00bd3a54 ["INT_ADD", "register:40f0:8", ["const:bd3a54:8", "const:4:8"]]
- 00bd3a54 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bd3a98 ["INT_ADD", "register:40f0:8", ["const:bd3a98:8", "const:4:8"]]
+ 00bd3a98 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bd3a54 bytes cb250094
+ 00bd3a98 bytes ce250094
- 00bd3a78 ["COPY", "tmp:0:8", ["const:f28:8"]]
- 00bd3a78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd3a78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd3a78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd3abc ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 00bd3abc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd3abc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd3abc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd3a78 bytes 08a13c91
+ 00bd3abc bytes 08e13d91
- 00bd3ac0 ["INT_ADD", "register:40f0:8", ["const:bd3ac0:8", "const:4:8"]]
- 00bd3ac0 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bd3b04 ["INT_ADD", "register:40f0:8", ["const:bd3b04:8", "const:4:8"]]
+ 00bd3b04 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bd3ac0 bytes b01d0094
+ 00bd3b04 bytes b31d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e551a69b8b8a7987de75060569fe2c3"></a>

### [`00bd3d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3d48.md) → [`00bd3d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3d8c.md) FUN_00bd3d8c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd3df4",
      "incomplete_value": false,
      "site": "00bd3df4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd3db0",
      "incomplete_value": false,
      "site": "00bd3db0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:f98:8"
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
      "00bd3df4",
      "DATA",
      [
        "storage",
        "00c19f98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd3df4",
      "DATA",
      [
        "storage",
        "00c19fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd3d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3d48.md#insn-00bd3d80) · [`00bd3da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3d48.md#insn-00bd3da4) · [`00bd3de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3d48.md#insn-00bd3de8)
- 新版 [`00bd3dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3d8c.md#insn-00bd3dc4) · [`00bd3de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3d8c.md#insn-00bd3de8) · [`00bd3e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3d8c.md#insn-00bd3e2c)

~~~diff
- 00bd3d80 ["INT_ADD", "register:40f0:8", ["const:bd3d80:8", "const:4:8"]]
- 00bd3d80 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bd3dc4 ["INT_ADD", "register:40f0:8", ["const:bd3dc4:8", "const:4:8"]]
+ 00bd3dc4 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bd3d80 bytes 00250094
+ 00bd3dc4 bytes 03250094
- 00bd3da4 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 00bd3da4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd3da4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd3da4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd3de8 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 00bd3de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd3de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd3de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd3da4 bytes 08613e91
+ 00bd3de8 bytes 08a13f91
- 00bd3de8 ["INT_ADD", "register:40f0:8", ["const:bd3de8:8", "const:4:8"]]
- 00bd3de8 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bd3e2c ["INT_ADD", "register:40f0:8", ["const:bd3e2c:8", "const:4:8"]]
+ 00bd3e2c ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bd3de8 bytes e61c0094
+ 00bd3e2c bytes e91c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dedd8b49e57f511cd1eae75d37bcc0ca"></a>

### [`00bd3e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3e18.md) → [`00bd3e5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3e5c.md) FUN_00bd3e5c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.10% / 新版 98.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd3fe0",
      "incomplete_value": false,
      "site": "00bd3ff0",
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
            "const:324:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd3f9c",
      "incomplete_value": false,
      "site": "00bd3fac",
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
            "const:326:8"
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
      "definition_site": "00bd3fe8",
      "incomplete_value": false,
      "site": "00bd3ff0",
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
      "definition_site": "00bd3fa4",
      "incomplete_value": false,
      "site": "00bd3fac",
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
    "ordinal": 5,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd3fe0",
      "PARAM",
      [
        "storage",
        "0029c326",
        null,
        "string"
      ]
    ],
    [
      "00bd3fe8",
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
      "00bd3fe0",
      "PARAM",
      [
        "storage",
        "0029c324",
        null,
        "string"
      ]
    ],
    [
      "00bd3fe8",
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

- 旧版 [`00bd3fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3e18.md#insn-00bd3fac) · [`00bd3e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3e18.md#insn-00bd3e74) · [`00bd3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3e18.md#insn-00bd3ebc)
- 新版 [`00bd3ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3e5c.md#insn-00bd3ff0) · [`00bd3eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3e5c.md#insn-00bd3eb8) · [`00bd3f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3e5c.md#insn-00bd3f00)

~~~diff
- 00bd3fac ["INT_ADD", "register:40f0:8", ["const:bd3fac:8", "const:4:8"]]
- 00bd3fac ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bd3ff0 ["INT_ADD", "register:40f0:8", ["const:bd3ff0:8", "const:4:8"]]
+ 00bd3ff0 ["CALL", null, ["callee:00bbb19c:8"]]
- 00bd3fac bytes 6b9cff97
+ 00bd3ff0 bytes 6b9cff97
- 00bd3e74 ["INT_ADD", "register:40f0:8", ["const:bd3e74:8", "const:4:8"]]
- 00bd3e74 ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd3eb8 ["INT_ADD", "register:40f0:8", ["const:bd3eb8:8", "const:4:8"]]
+ 00bd3eb8 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd3e74 bytes e3240094
+ 00bd3eb8 bytes e6240094
- 00bd3ebc ["INT_ADD", "register:40f0:8", ["const:bd3ebc:8", "const:4:8"]]
- 00bd3ebc ["CALL", null, ["callee:00bdd250:8"]]
+ 00bd3f00 ["INT_ADD", "register:40f0:8", ["const:bd3f00:8", "const:4:8"]]
+ 00bd3f00 ["CALL", null, ["callee:00bdd250:8"]]
- 00bd3ebc bytes d1240094
+ 00bd3f00 bytes d4240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a630f47419814a98f61cddc40d95b887"></a>

### [`00bd3fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3fc4.md) → [`00bd4008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4008.md) FUN_00bd4008

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd4074",
      "incomplete_value": false,
      "site": "00bd4074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c1a000:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd4030",
      "incomplete_value": false,
      "site": "00bd4030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c1a000:8"
          ],
          [
            "leaf",
            "const:8:8"
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
      "00bd4074",
      "DATA",
      [
        "storage",
        "00c1a008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd4074",
      "DATA",
      [
        "storage",
        "00c1a058",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3fc4.md#insn-00bd4074) · [`00bd3ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3fc4.md#insn-00bd3ffc) · [`00bd4028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3fc4.md#insn-00bd4028)
- 新版 [`00bd40b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4008.md#insn-00bd40b8) · [`00bd4040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4008.md#insn-00bd4040) · [`00bd406c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4008.md#insn-00bd406c)

~~~diff
- 00bd4074 ["INT_ADD", "register:40f0:8", ["const:bd4074:8", "const:4:8"]]
- 00bd4074 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00bd40b8 ["INT_ADD", "register:40f0:8", ["const:bd40b8:8", "const:4:8"]]
+ 00bd40b8 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00bd4074 bytes 431c0094
+ 00bd40b8 bytes 461c0094
- 00bd3ffc ["INT_ADD", "register:40f0:8", ["const:bd3ffc:8", "const:4:8"]]
- 00bd3ffc ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bd4040 ["INT_ADD", "register:40f0:8", ["const:bd4040:8", "const:4:8"]]
+ 00bd4040 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bd3ffc bytes 61240094
+ 00bd4040 bytes 64240094
- 00bd4028 ["COPY", "tmp:0:8", ["const:8:8"]]
- 00bd4028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd4028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd4028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd406c ["COPY", "tmp:0:8", ["const:58:8"]]
+ 00bd406c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd406c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd406c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd4028 bytes 08210091
+ 00bd406c bytes 08610191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3995332ce3227f55360cfed325697dc2"></a>

### [`00bd4cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4cc0.md) → [`00bd4d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4d04.md) FUN_00bd4d04

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bd4988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4988.md) [`00bd4b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4b98.md) · 呼出先 6件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md)
- 新版 呼出元 2件 [`00bd49cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd49cc.md) [`00bd4bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4bdc.md) · 呼出先 6件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.98% / 新版 97.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd4e74",
      "incomplete_value": false,
      "site": "00bd4e84",
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
            "const:195:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd4e30",
      "incomplete_value": false,
      "site": "00bd4e40",
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
            "const:10a:8"
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
      "definition_site": "00bd4e7c",
      "incomplete_value": false,
      "site": "00bd4e84",
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
            "const:b26:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd4e38",
      "incomplete_value": false,
      "site": "00bd4e40",
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
            "const:bb3:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd4e74",
      "PARAM",
      [
        "storage",
        "002a210a",
        null,
        "string"
      ]
    ],
    [
      "00bd4e7c",
      "PARAM",
      [
        "storage",
        "00298bb3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd4e74",
      "PARAM",
      [
        "storage",
        "002a2195",
        null,
        "string"
      ]
    ],
    [
      "00bd4e7c",
      "PARAM",
      [
        "storage",
        "00298b26",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4cc0.md#insn-00bd4dfc) · [`00bd4e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4cc0.md#insn-00bd4e40) · [`00bd4d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4cc0.md#insn-00bd4d18)
- 新版 [`00bd4e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4d04.md#insn-00bd4e40) · [`00bd4e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4d04.md#insn-00bd4e84) · [`00bd4d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4d04.md#insn-00bd4d5c)

~~~diff
- 00bd4dfc ["INT_ADD", "register:40f0:8", ["const:bd4dfc:8", "const:4:8"]]
- 00bd4dfc ["CALL", null, ["callee:00bdb810:8"]]
+ 00bd4e40 ["INT_ADD", "register:40f0:8", ["const:bd4e40:8", "const:4:8"]]
+ 00bd4e40 ["CALL", null, ["callee:00bdb810:8"]]
- 00bd4dfc bytes 711a0094
+ 00bd4e40 bytes 741a0094
- 00bd4e40 ["INT_ADD", "register:40f0:8", ["const:bd4e40:8", "const:4:8"]]
- 00bd4e40 ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bd4e84 ["INT_ADD", "register:40f0:8", ["const:bd4e84:8", "const:4:8"]]
+ 00bd4e84 ["CALL", null, ["callee:00bbb19c:8"]]
- 00bd4e40 bytes c698ff97
+ 00bd4e84 bytes c698ff97
- 00bd4d18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4d18 ["INT_ADD", "register:40f0:8", ["const:bd4d18:8", "const:4:8"]]
- 00bd4d18 ["CALLIND", null, ["register:0:8"]]
+ 00bd4d5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd4d5c ["INT_ADD", "register:40f0:8", ["const:bd4d5c:8", "const:4:8"]]
+ 00bd4d5c ["CALLIND", null, ["register:0:8"]]
- 00bd4d18 bytes 00013fd6
+ 00bd4d5c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c3b624d72aa43d2ac326fecb59f0c45"></a>

### [`00bd57dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd57dc.md) → [`00bd5820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5820.md) FUN_00bd5820

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bd5790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5790.md) · 呼出先 3件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)
- 新版 呼出元 1件 [`00bd57d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd57d4.md) · 呼出先 3件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 84.27% / 新版 84.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 6件, `store_destination` 3件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd5870",
      "incomplete_value": true,
      "site": "00bd5870",
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
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd582c",
      "incomplete_value": true,
      "site": "00bd582c",
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
            "const:748:8"
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
      "definition_site": "00bd5868",
      "incomplete_value": false,
      "site": "00bd5870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:79c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5824",
      "incomplete_value": false,
      "site": "00bd582c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:75c:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd5874",
      "incomplete_value": false,
      "site": "00bd5874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:79c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5830",
      "incomplete_value": false,
      "site": "00bd5830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:75c:8"
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
      "00bd5838",
      "PARAM",
      [
        "storage",
        "010a3720",
        null,
        null
      ]
    ],
    [
      "00bd5844",
      "READ",
      [
        "storage",
        "010a3748",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5870",
      "WRITE",
      [
        "storage",
        "010a3748",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5838",
      "PARAM",
      [
        "storage",
        "010a3760",
        null,
        null
      ]
    ],
    [
      "00bd5844",
      "READ",
      [
        "storage",
        "010a3788",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5870",
      "WRITE",
      [
        "storage",
        "010a3788",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd57f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd57dc.md#insn-00bd57f8) · [`00bd582c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd57dc.md#insn-00bd582c) · [`00bd58dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd57dc.md#insn-00bd58dc)
- 新版 [`00bd583c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5820.md#insn-00bd583c) · [`00bd5870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5820.md#insn-00bd5870) · [`00bd5920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5820.md#insn-00bd5920)

~~~diff
- 00bd57f8 ["INT_ADD", "register:40f0:8", ["const:bd57f8:8", "const:4:8"]]
- 00bd57f8 ["CALL", null, ["callee:00bde820:8"]]
+ 00bd583c ["INT_ADD", "register:40f0:8", ["const:bd583c:8", "const:4:8"]]
+ 00bd583c ["CALL", null, ["callee:00bde820:8"]]
- 00bd57f8 bytes f6230094
+ 00bd583c bytes f9230094
- 00bd582c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:748:8"]]
- 00bd582c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4070:8"]]
+ 00bd5870 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:788:8"]]
+ 00bd5870 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4070:8"]]
- 00bd582c bytes 0ea503f9
+ 00bd5870 bytes 0ec503f9
- 00bd58dc ["INT_ADD", "register:40f0:8", ["const:bd58dc:8", "const:4:8"]]
- 00bd58dc ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bd5920 ["INT_ADD", "register:40f0:8", ["const:bd5920:8", "const:4:8"]]
+ 00bd5920 ["CALL", null, ["callee:00bbb19c:8"]]
- 00bd58dc bytes 1f96ff97
+ 00bd5920 bytes 1f96ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7631adf747d9a439a2ff675e5391435"></a>

### [`00bd5964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5964.md) → [`00bd59a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd59a8.md) FUN_00bd59a8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 6件 [`00bd50b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd50b0.md) [`00bd5144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5144.md) [`00bd51e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51e8.md) [`00bd527c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd527c.md) [`00bd5368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5368.md) · 呼出先 2件 [`00bd5990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5990.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 6件 [`00bd50f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd50f4.md) [`00bd5188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5188.md) [`00bd522c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd522c.md) [`00bd52c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd52c0.md) [`00bd53ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd53ac.md) · 呼出先 2件 [`00bd59d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd59d4.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 45.45% / 新版 45.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd59b8",
      "incomplete_value": true,
      "site": "00bd59b8",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_LESSEQUAL",
            "1",
            [
              "INT_ADD",
              [
                "live",
                "register:4000:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5974",
      "incomplete_value": true,
      "site": "00bd5974",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_LESSEQUAL",
            "1",
            [
              "INT_ADD",
              [
                "live",
                "register:4000:8"
              ]
            ]
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
      "definition_site": "00bd59c4",
      "incomplete_value": true,
      "site": "00bd59c8",
      "value": [
        "INT_LESSEQUAL",
        "1",
        [
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
                "const:990:8"
              ]
            ]
          ],
          [
            "live",
            "register:4000:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5980",
      "incomplete_value": true,
      "site": "00bd5984",
      "value": [
        "INT_LESSEQUAL",
        "1",
        [
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
                "const:950:8"
              ]
            ]
          ],
          [
            "live",
            "register:4000:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bd596c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5964.md#insn-00bd596c) · [`00bd597c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5964.md#insn-00bd597c)
- 新版 [`00bd59b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd59a8.md#insn-00bd59b0) · [`00bd59c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd59a8.md#insn-00bd59c0)

~~~diff
- 00bd596c ["COPY", "tmp:0:8", ["const:750:8"]]
- 00bd596c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd596c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd596c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd59b0 ["COPY", "tmp:0:8", ["const:790:8"]]
+ 00bd59b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd59b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd59b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd596c bytes 08411d91
+ 00bd59b0 bytes 08411e91
- 00bd597c ["COPY", "tmp:0:8", ["const:950:8"]]
- 00bd597c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd597c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd597c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd59c0 ["COPY", "tmp:0:8", ["const:990:8"]]
+ 00bd59c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd59c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd59c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd597c bytes 08412591
+ 00bd59c0 bytes 08412691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aaf99eab5a8def9b061725e0a061afc3"></a>

### [`00bd5990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5990.md) → [`00bd59d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd59d4.md) FUN_00bd59d4

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bd5964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5964.md) · 呼出先 2件 [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)
- 新版 呼出元 1件 [`00bd59a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd59a8.md) · 呼出先 2件 [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd5a64",
      "incomplete_value": true,
      "site": "00bd5a64",
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
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5a20",
      "incomplete_value": true,
      "site": "00bd5a20",
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
            "const:748:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd5ab0",
      "incomplete_value": true,
      "site": "00bd5ab0",
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
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5a6c",
      "incomplete_value": true,
      "site": "00bd5a6c",
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
            "const:748:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd5a00",
      "incomplete_value": true,
      "site": "00bd5a00",
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
      "definition_site": "00bd59bc",
      "incomplete_value": true,
      "site": "00bd59bc",
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
      "00bd59f0",
      "PARAM",
      [
        "storage",
        "010a3720",
        null,
        null
      ]
    ],
    [
      "00bd59fc",
      "READ",
      [
        "storage",
        "010a3748",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5a24",
      "DATA",
      [
        "storage",
        "010a3752",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd59f0",
      "PARAM",
      [
        "storage",
        "010a3760",
        null,
        null
      ]
    ],
    [
      "00bd59fc",
      "READ",
      [
        "storage",
        "010a3788",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5a24",
      "DATA",
      [
        "storage",
        "010a3792",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd59b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5990.md#insn-00bd59b0) · [`00bd5a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5990.md#insn-00bd5a20) · [`00bd5a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5990.md#insn-00bd5a6c)
- 新版 [`00bd59f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd59d4.md#insn-00bd59f4) · [`00bd5a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd59d4.md#insn-00bd5a64) · [`00bd5ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd59d4.md#insn-00bd5ab0)

~~~diff
- 00bd59b0 ["INT_ADD", "register:40f0:8", ["const:bd59b0:8", "const:4:8"]]
- 00bd59b0 ["CALL", null, ["callee:00bde820:8"]]
+ 00bd59f4 ["INT_ADD", "register:40f0:8", ["const:bd59f4:8", "const:4:8"]]
+ 00bd59f4 ["CALL", null, ["callee:00bde820:8"]]
- 00bd59b0 bytes 88230094
+ 00bd59f4 bytes 8b230094
- 00bd5a20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:748:8"]]
- 00bd5a20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 00bd5a64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:788:8"]]
+ 00bd5a64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00bd5a20 bytes 14a503f9
+ 00bd5a64 bytes 14c503f9
- 00bd5a6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:748:8"]]
- 00bd5a6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 00bd5ab0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:788:8"]]
+ 00bd5ab0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00bd5a6c bytes 14a503f9
+ 00bd5ab0 bytes 14c503f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-753750fadd7d5e42dab48fd42087a9ac"></a>

### [`00bd6030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6030.md) → [`00bd6074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6074.md) __cxa_call_unexpected

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 18件 [`00bba9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9e0.md) [`00bbaa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md) [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bd4f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4f94.md) [`00bd4fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4fa0.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00bbaa24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa24.md) [`00bbaa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bd4fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4fd8.md) [`00bd4fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4fe4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.69% / 新版 97.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd61c8",
      "incomplete_value": true,
      "site": "00bd61cc",
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
      "definition_site": "00bd6184",
      "incomplete_value": true,
      "site": "00bd6188",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd61dc",
      "incomplete_value": true,
      "site": "00bd61f0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1c000:8"
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
    "old": {
      "definition_site": "00bd6198",
      "incomplete_value": true,
      "site": "00bd61ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6228",
      "incomplete_value": true,
      "site": "00bd6230",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd61e4",
      "incomplete_value": true,
      "site": "00bd61ec",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:fe0:8"
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
      "00bd61c4",
      "READ",
      [
        "storage",
        "00c1bfd8",
        null,
        "pointer"
      ]
    ],
    [
      "00bd61cc",
      "DATA",
      [
        "storage",
        "00c16870",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00bd61dc",
      "READ",
      [
        "storage",
        "00c1bfe0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bd61c4",
      "READ",
      [
        "storage",
        "00c1c028",
        null,
        "pointer"
      ]
    ],
    [
      "00bd61cc",
      "DATA",
      [
        "storage",
        "00c168c0",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00bd61dc",
      "READ",
      [
        "storage",
        "00c1c030",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd61ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6030.md#insn-00bd61ac) · [`00bd61ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6030.md#insn-00bd61ec) · [`00bd6058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6030.md#insn-00bd6058)
- 新版 [`00bd61f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6074.md#insn-00bd61f0) · [`00bd6230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6074.md#insn-00bd6230) · [`00bd609c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6074.md#insn-00bd609c)

~~~diff
- 00bd61ac ["INT_ADD", "register:40f0:8", ["const:bd61ac:8", "const:4:8"]]
- 00bd61ac ["CALL", null, ["callee:00bd6438:8"]]
+ 00bd61f0 ["INT_ADD", "register:40f0:8", ["const:bd61f0:8", "const:4:8"]]
+ 00bd61f0 ["CALL", null, ["callee:00bd6438:8"]]
- 00bd61ac bytes 92000094
+ 00bd61f0 bytes 92000094
- 00bd61ec ["INT_ADD", "register:40f0:8", ["const:bd61ec:8", "const:4:8"]]
- 00bd61ec ["CALL", null, ["callee:00bdb0c0:8"]]
+ 00bd6230 ["INT_ADD", "register:40f0:8", ["const:bd6230:8", "const:4:8"]]
+ 00bd6230 ["CALL", null, ["callee:00bdb0c0:8"]]
- 00bd61ec bytes a1130094
+ 00bd6230 bytes a4130094
- 00bd6058 ["INT_ADD", "register:40f0:8", ["const:bd6058:8", "const:4:8"]]
- 00bd6058 ["CALL", null, ["callee:00bdb1c0:8"]]
+ 00bd609c ["INT_ADD", "register:40f0:8", ["const:bd609c:8", "const:4:8"]]
+ 00bd609c ["CALL", null, ["callee:00bdb1c0:8"]]
- 00bd6058 bytes 46140094
+ 00bd609c bytes 49140094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8c92ea687c2d4d7bdf82caa9b06a7b2"></a>

### [`00bd6650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6650.md) → [`00bd6694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6694.md) __emutls_get_address

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdd450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd450.md) · 呼出先 11件 [`00bd6878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6878.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00bdb2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2a0.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)
- 新版 呼出元 1件 [`00bdd4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4a0.md) · 呼出先 11件 [`00bd68bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd68bc.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bdb2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2f0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.50% / 新版 93.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd6750",
      "incomplete_value": true,
      "site": "00bd6750",
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
            "const:9a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd670c",
      "incomplete_value": true,
      "site": "00bd670c",
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
            "const:960:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd6748",
      "incomplete_value": true,
      "site": "00bd6750",
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
            "const:1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6704",
      "incomplete_value": true,
      "site": "00bd670c",
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
            "const:1:8"
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
      "definition_site": "00bd6748",
      "incomplete_value": true,
      "site": "00bd6754",
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
            "const:1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6704",
      "incomplete_value": true,
      "site": "00bd6710",
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
            "const:1:8"
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
      "00bd66bc",
      "READ",
      [
        "storage",
        "010a3954",
        null,
        "undefined4"
      ]
    ],
    [
      "00bd6724",
      "PARAM",
      [
        "storage",
        "00bd6878",
        null,
        null
      ]
    ],
    [
      "00bd6728",
      "PARAM",
      [
        "storage",
        "010a3958",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd66bc",
      "READ",
      [
        "storage",
        "010a3994",
        null,
        "undefined4"
      ]
    ],
    [
      "00bd6724",
      "PARAM",
      [
        "storage",
        "00bd68bc",
        null,
        null
      ]
    ],
    [
      "00bd6728",
      "PARAM",
      [
        "storage",
        "010a3998",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd667c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6650.md#insn-00bd667c) · [`00bd66cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6650.md#insn-00bd66cc) · [`00bd66d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6650.md#insn-00bd66d8)
- 新版 [`00bd66c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6694.md#insn-00bd66c0) · [`00bd6710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6694.md#insn-00bd6710) · [`00bd671c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6694.md#insn-00bd671c)

~~~diff
- 00bd667c ["INT_ADD", "register:40f0:8", ["const:bd667c:8", "const:4:8"]]
- 00bd667c ["CALL", null, ["callee:00be11f0:8"]]
+ 00bd66c0 ["INT_ADD", "register:40f0:8", ["const:bd66c0:8", "const:4:8"]]
+ 00bd66c0 ["CALL", null, ["callee:00be11f0:8"]]
- 00bd667c bytes c92a0094
+ 00bd66c0 bytes cc2a0094
- 00bd66cc ["INT_ADD", "register:40f0:8", ["const:bd66cc:8", "const:4:8"]]
- 00bd66cc ["CALL", null, ["callee:00bdb240:8"]]
+ 00bd6710 ["INT_ADD", "register:40f0:8", ["const:bd6710:8", "const:4:8"]]
+ 00bd6710 ["CALL", null, ["callee:00bdb240:8"]]
- 00bd66cc bytes c9120094
+ 00bd6710 bytes cc120094
- 00bd66d8 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00bd66d8 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00bd66d8 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00bd66d8 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00bd671c ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00bd671c ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00bd671c ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00bd671c ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00bd66d8 bytes 94622591
+ 00bd671c bytes 94622691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b82853deb28f85a58c85d9f3b17f87ee"></a>

### [`00bd683c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd683c.md) → [`00bd6880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6880.md) FUN_00bd6880

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004182e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004182e8.md) · 呼出先 1件 [`00be1f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f00.md)
- 新版 呼出元 1件 [`004182e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004182e8.md) · 呼出先 1件 [`00be1f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd68a4",
      "incomplete_value": true,
      "site": "00bd68a8",
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
      "definition_site": "00bd6860",
      "incomplete_value": true,
      "site": "00bd6864",
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
      "00bd6888",
      "READ",
      [
        "storage",
        "010a3950",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd68a4",
      "READ",
      [
        "storage",
        "010a3954",
        null,
        "undefined4"
      ]
    ],
    [
      "00bd68ac",
      "WRITE",
      [
        "storage",
        "010a3950",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd6888",
      "READ",
      [
        "storage",
        "010a3990",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd68a4",
      "READ",
      [
        "storage",
        "010a3994",
        null,
        "undefined4"
      ]
    ],
    [
      "00bd68ac",
      "WRITE",
      [
        "storage",
        "010a3990",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd683c.md#insn-00bd6864) · [`00bd6844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd683c.md#insn-00bd6844) · [`00bd685c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd683c.md#insn-00bd685c)
- 新版 [`00bd68a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6880.md#insn-00bd68a8) · [`00bd6888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6880.md#insn-00bd6888) · [`00bd68a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6880.md#insn-00bd68a0)

~~~diff
- 00bd6864 ["INT_ADD", "register:40f0:8", ["const:bd6864:8", "const:4:8"]]
- 00bd6864 ["CALL", null, ["callee:00be1f50:8"]]
+ 00bd68a8 ["INT_ADD", "register:40f0:8", ["const:bd68a8:8", "const:4:8"]]
+ 00bd68a8 ["CALL", null, ["callee:00be1f50:8"]]
- 00bd6864 bytes a72d0094
+ 00bd68a8 bytes aa2d0094
- 00bd6844 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:950:8"]]
- 00bd6844 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd6844 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bd6888 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:990:8"]]
+ 00bd6888 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6888 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bd6844 bytes 08416539
+ 00bd6888 bytes 08416639
- 00bd685c ["COPY", "tmp:0:8", ["const:950:8"]]
- 00bd685c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00bd685c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00bd685c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00bd68a0 ["COPY", "tmp:0:8", ["const:990:8"]]
+ 00bd68a0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00bd68a0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00bd68a0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00bd685c bytes 73422591
+ 00bd68a0 bytes 73422691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55bdc297366dfaff2543b6e7865ecd83"></a>

### [`00bd6878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6878.md) → [`00bd68bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd68bc.md) FUN_00bd68bc

採用 · 移動量 `+0x44` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bd6650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6650.md) · 呼出先 3件 [`00bd68b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd68b4.md) [`00bdd460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd460.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bd6694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6694.md) · 呼出先 3件 [`00bd68f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd68f8.md) [`00bdd4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd68e4",
      "incomplete_value": false,
      "site": "00bd68e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd68a0",
      "incomplete_value": false,
      "site": "00bd68a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:950:8"
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
      "definition_site": "00bd68c8",
      "incomplete_value": false,
      "site": "00bd68d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:994:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6884",
      "incomplete_value": false,
      "site": "00bd6890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:954:8"
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
      "definition_site": "00bd68d0",
      "incomplete_value": false,
      "site": "00bd68d4",
      "value": [
        "leaf",
        "const:bd68f8:8"
      ]
    },
    "old": {
      "definition_site": "00bd688c",
      "incomplete_value": false,
      "site": "00bd6890",
      "value": [
        "leaf",
        "const:bd68b4:8"
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
      "00bd68c8",
      "PARAM",
      [
        "storage",
        "010a3954",
        null,
        "undefined4"
      ]
    ],
    [
      "00bd68d0",
      "PARAM",
      [
        "storage",
        "00bd68b4",
        null,
        null
      ]
    ],
    [
      "00bd68e4",
      "WRITE",
      [
        "storage",
        "010a3950",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd68c8",
      "PARAM",
      [
        "storage",
        "010a3994",
        null,
        "undefined4"
      ]
    ],
    [
      "00bd68d0",
      "PARAM",
      [
        "storage",
        "00bd68f8",
        null,
        null
      ]
    ],
    [
      "00bd68e4",
      "WRITE",
      [
        "storage",
        "010a3990",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6878.md#insn-00bd6890) · [`00bd68a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6878.md#insn-00bd68a0) · [`00bd6884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6878.md#insn-00bd6884)
- 新版 [`00bd68d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd68bc.md#insn-00bd68d4) · [`00bd68e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd68bc.md#insn-00bd68e4) · [`00bd68c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd68bc.md#insn-00bd68c8)

~~~diff
- 00bd6890 ["INT_ADD", "register:40f0:8", ["const:bd6890:8", "const:4:8"]]
- 00bd6890 ["CALL", null, ["callee:00bdd4b0:8"]]
+ 00bd68d4 ["INT_ADD", "register:40f0:8", ["const:bd68d4:8", "const:4:8"]]
+ 00bd68d4 ["CALL", null, ["callee:00bdd4b0:8"]]
- 00bd6890 bytes f41a0094
+ 00bd68d4 bytes f71a0094
- 00bd68a0 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bd68a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:950:8"]]
- 00bd68a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd68e4 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00bd68e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:990:8"]]
+ 00bd68e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd68a0 bytes 09412539
+ 00bd68e4 bytes 09412639
- 00bd6884 ["COPY", "tmp:0:8", ["const:954:8"]]
- 00bd6884 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd6884 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd6884 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd68c8 ["COPY", "tmp:0:8", ["const:994:8"]]
+ 00bd68c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd68c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd68c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd6884 bytes 00502591
+ 00bd68c8 bytes 00502691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4c31646c56a43ce32d1e5bee1a04e87"></a>

### [`00bd6974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6974.md) → [`00bd69b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd69b4.md) _INIT_0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00be01e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01e0.md) [`00be1f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f10.md) [`00be1f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00be0230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0230.md) [`00be1f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f60.md) [`00be1f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f70.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd69d4",
      "incomplete_value": false,
      "site": "00bd69d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6994",
      "incomplete_value": false,
      "site": "00bd6994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:990:8"
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
      "definition_site": "00bd6a20",
      "incomplete_value": false,
      "site": "00bd6a20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd69e0",
      "incomplete_value": false,
      "site": "00bd69e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:990:8"
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
      "definition_site": "00bd6a3c",
      "incomplete_value": false,
      "site": "00bd6a3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd69fc",
      "incomplete_value": false,
      "site": "00bd69fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd69d4",
      "WRITE",
      [
        "storage",
        "010a3990",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd69e8",
      "PARAM",
      [
        "storage",
        "0029684d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd69c0",
      "PARAM",
      [
        "storage",
        "00299acc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd69d4",
      "WRITE",
      [
        "storage",
        "010a39d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd69e8",
      "PARAM",
      [
        "storage",
        "002967c0",
        null,
        "string"
      ]
    ],
    [
      "00bd6a00",
      "PARAM",
      [
        "storage",
        "00299a3f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6974.md#insn-00bd6994) · [`00bd69b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6974.md#insn-00bd69b0) · [`00bd69cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6974.md#insn-00bd69cc)
- 新版 [`00bd69d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd69b4.md#insn-00bd69d4) · [`00bd69f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd69b4.md#insn-00bd69f0) · [`00bd6a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd69b4.md#insn-00bd6a0c)

~~~diff
- 00bd6994 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd6994 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd6994 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:990:8"]]
- 00bd6994 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd69d4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd69d4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd69d4 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:9d0:8"]]
+ 00bd69d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd6994 bytes 3f412639
+ 00bd69d4 bytes 3f412739
- 00bd69b0 ["INT_ADD", "register:40f0:8", ["const:bd69b0:8", "const:4:8"]]
- 00bd69b0 ["CALL", null, ["callee:00be1f70:8"]]
+ 00bd69f0 ["INT_ADD", "register:40f0:8", ["const:bd69f0:8", "const:4:8"]]
+ 00bd69f0 ["CALL", null, ["callee:00be1f70:8"]]
- 00bd69b0 bytes 5c2d0094
+ 00bd69f0 bytes 602d0094
- 00bd69cc ["INT_ADD", "register:40f0:8", ["const:bd69cc:8", "const:4:8"]]
- 00bd69cc ["CALL", null, ["callee:00be0230:8"]]
+ 00bd6a0c ["INT_ADD", "register:40f0:8", ["const:bd6a0c:8", "const:4:8"]]
+ 00bd6a0c ["CALL", null, ["callee:00be0230:8"]]
- 00bd69cc bytes 05260094
+ 00bd6a0c bytes 09260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19eebeb66f9f41a63c7197f378dc290f"></a>

### [`00bd6a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6a0c.md) → [`00bd6a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6a4c.md) FUN_00bd6a4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bd6cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6cb8.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bd6cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6cf8.md) · 呼出先 0件 

変更の種類 constant, local_def_use, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 92.40% / 新版 92.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd6cf0",
      "incomplete_value": false,
      "site": "00bd6cf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6cb0",
      "incomplete_value": false,
      "site": "00bd6cb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "00bd6cf0",
      "WRITE",
      [
        "storage",
        "010a3998",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6cf0",
      "WRITE",
      [
        "storage",
        "010a39d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6a0c.md#insn-00bd6cb0) · [`00bd6b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6a0c.md#insn-00bd6b30) · [`00bd6b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6a0c.md#insn-00bd6b70)
- 新版 [`00bd6cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6a4c.md#insn-00bd6cf0)

~~~diff
- 00bd6cb0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:998:8"]]
- 00bd6cb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00bd6cf0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9d8:8"]]
+ 00bd6cf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bd6cb0 bytes 28cd04f9
+ 00bd6cf0 bytes 28ed04f9
- 00bd6b30 ["INT_OR", "register:4060:8", ["register:4060:8", "register:4068:8"]]
- 00bd6b30 bytes 8c010daa
- 00bd6b70 ["INT_OR", "register:4050:8", ["register:4050:8", "register:4058:8"]]
- 00bd6b70 bytes 4a010baa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be174bb9baff0ad84eda6a010b1ee008"></a>

### [`00bd6cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6cb8.md) → [`00bd6cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6cf8.md) _INIT_1

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd6a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6a0c.md) [`00be01e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01e0.md) [`00be1f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f10.md) [`00be1f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f20.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bd6a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6a4c.md) [`00be0230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0230.md) [`00be1f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f60.md) [`00be1f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f70.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_return_alignment

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd6d04",
      "incomplete_value": true,
      "site": "00bd6d04",
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
      "definition_site": "00bd6cc4",
      "incomplete_value": true,
      "site": "00bd6cc4",
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
      "definition_site": "00bd6d1c",
      "incomplete_value": false,
      "site": "00bd6d24",
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
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6cdc",
      "incomplete_value": false,
      "site": "00bd6ce4",
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
            "const:84d:8"
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
      "definition_site": "00bd6d34",
      "incomplete_value": false,
      "site": "00bd6d40",
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
            "const:a3f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6cf4",
      "incomplete_value": false,
      "site": "00bd6d00",
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
            "const:acc:8"
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
      "00bd6d00",
      "READ",
      [
        "storage",
        "010a3998",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd6cdc",
      "PARAM",
      [
        "storage",
        "0029684d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd6cf4",
      "PARAM",
      [
        "storage",
        "00299acc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd6d00",
      "READ",
      [
        "storage",
        "010a39d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6d1c",
      "PARAM",
      [
        "storage",
        "002967c0",
        null,
        "string"
      ]
    ],
    [
      "00bd6d34",
      "PARAM",
      [
        "storage",
        "00299a3f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6cb8.md#insn-00bd6cc0) · [`00bd6ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6cb8.md#insn-00bd6ce4) · [`00bd6d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6cb8.md#insn-00bd6d00)
- 新版 [`00bd6d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6cf8.md#insn-00bd6d00) · [`00bd6d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6cf8.md#insn-00bd6d24) · [`00bd6d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6cf8.md#insn-00bd6d40)

~~~diff
- 00bd6cc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:998:8"]]
- 00bd6cc0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6d00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d8:8"]]
+ 00bd6d00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd6cc0 bytes 08cd44f9
+ 00bd6d00 bytes 08ed44f9
- 00bd6ce4 ["INT_ADD", "register:40f0:8", ["const:bd6ce4:8", "const:4:8"]]
- 00bd6ce4 ["CALL", null, ["callee:00be1f70:8"]]
+ 00bd6d24 ["INT_ADD", "register:40f0:8", ["const:bd6d24:8", "const:4:8"]]
+ 00bd6d24 ["CALL", null, ["callee:00be1f70:8"]]
- 00bd6ce4 bytes 8f2c0094
+ 00bd6d24 bytes 932c0094
- 00bd6d00 ["INT_ADD", "register:40f0:8", ["const:bd6d00:8", "const:4:8"]]
- 00bd6d00 ["CALL", null, ["callee:00be0230:8"]]
+ 00bd6d40 ["INT_ADD", "register:40f0:8", ["const:bd6d40:8", "const:4:8"]]
+ 00bd6d40 ["CALL", null, ["callee:00be0230:8"]]
- 00bd6d00 bytes 38250094
+ 00bd6d40 bytes 3c250094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79646ac1693574a5565ad4f61e1eb838"></a>

### [`00bd6d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6d50.md) → [`00bd6d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6d90.md) FUN_00bd6d90

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b7354c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b7354c.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00b73590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73590.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 37.50% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6d74"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd6db4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00bd6d74"
      ],
      [
        "FALL_THROUGH",
        "00bd6db4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bd6db4",
      "incomplete_value": true,
      "site": "00bd6db8",
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
      "definition_site": "00bd6d74",
      "incomplete_value": true,
      "site": "00bd6d78",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "live",
            "register:101:1"
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
      "00bd6d98",
      "READ",
      [
        "storage",
        "010a3990",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bd6d74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6dc0"
      ]
    ]
  ],
  "added": [
    [
      "00bd6d98",
      "READ",
      [
        "storage",
        "010a39d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6db4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6dc0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6d50.md#insn-00bd6d74) · [`00bd6d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6d50.md#insn-00bd6d58)
- 新版 [`00bd6db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6d90.md#insn-00bd6db4) · [`00bd6d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6d90.md#insn-00bd6d98)

~~~diff
- 00bd6d74 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd6d74 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00bd6d74 bytes 61000054
+ 00bd6db4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00bd6db4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bd6db4 bytes 61000054
- 00bd6d58 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:990:8"]]
- 00bd6d58 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd6d58 ["INT_ZEXT", "register:4080:8", ["tmp:1:1"]]
+ 00bd6d98 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9d0:8"]]
+ 00bd6d98 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6d98 ["INT_ZEXT", "register:4080:8", ["tmp:1:1"]]
- 00bd6d58 bytes 10426639
+ 00bd6d98 bytes 10426739
~~~


<a id="compare-f1714740aa6cef8aadc1851f0355438e"></a>

### [`00bd6df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6df0.md) → [`00bd6e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e30.md) FUN_00bd6e30

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 8件 [`00b737f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b737f8.md) [`00b73830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73830.md) [`00b739a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b739a8.md) [`00b739e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b739e0.md) [`00b7e240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e240.md) · 呼出先 0件 
- 新版 呼出元 8件 [`00b7383c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b7383c.md) [`00b73874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73874.md) [`00b739ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b739ec.md) [`00b73a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73a24.md) [`00b7e284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e284.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 80.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00bd6e00",
      "incomplete_value": true,
      "site": "00bd6e04",
      "value": [
        "LOAD",
        "4",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:4008:8"
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
      "00bd6e38",
      "READ",
      [
        "storage",
        "010a3990",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd6e38",
      "READ",
      [
        "storage",
        "010a39d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6df0.md#insn-00bd6df8) · [`00bd6dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6df0.md#insn-00bd6dfc) · [`00bd6e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6df0.md#insn-00bd6e18)
- 新版 [`00bd6e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e30.md#insn-00bd6e38) · [`00bd6e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e30.md#insn-00bd6e3c) · [`00bd6e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e30.md#insn-00bd6e58)

~~~diff
- 00bd6df8 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:990:8"]]
- 00bd6df8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd6df8 ["INT_ZEXT", "register:4080:8", ["tmp:1:1"]]
+ 00bd6e38 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9d0:8"]]
+ 00bd6e38 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6e38 ["INT_ZEXT", "register:4080:8", ["tmp:1:1"]]
- 00bd6df8 bytes 10426639
+ 00bd6e38 bytes 10426739
- 00bd6dfc ["INT_EQUAL", "tmp:0:1", ["register:4080:4", "const:0:4"]]
- 00bd6dfc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd6e3c ["INT_EQUAL", "tmp:0:1", ["register:4080:4", "const:0:4"]]
+ 00bd6e3c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd6dfc bytes 70000034
+ 00bd6e3c bytes 70000034
- 00bd6e18 ["INT_NOTEQUAL", "tmp:0:1", ["register:4078:4", "const:0:4"]]
- 00bd6e18 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd6e58 ["INT_NOTEQUAL", "tmp:0:1", ["register:4078:4", "const:0:4"]]
+ 00bd6e58 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd6e18 bytes afffff35
+ 00bd6e58 bytes afffff35
~~~


<a id="compare-ecd8fd1ad3ede3338bbbc1f99e392070"></a>

### [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) → [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) FUN_00bd6e90

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1479件 [`00418394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418394.md) [`004183ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004183ec.md) [`004185a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004185a8.md) [`004186bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004186bc.md) [`00418b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418b18.md) · 呼出先 0件 
- 新版 呼出元 1480件 [`00418394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418394.md) [`004183ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004183ec.md) [`004185a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004185a8.md) [`004186bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004186bc.md) [`00418b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418b18.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 14.29% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6e74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd6eb4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6e74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6e98",
      "READ",
      [
        "storage",
        "010a3990",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bd6e78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6eac"
      ]
    ]
  ],
  "added": [
    [
      "00bd6e98",
      "READ",
      [
        "storage",
        "010a39d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6eb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6eac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md#insn-00bd6e74) · [`00bd6e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md#insn-00bd6e78) · [`00bd6e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md#insn-00bd6e7c)

~~~diff
- 00bd6e74 ["COPY", "tmp:0:1", ["const:1:1"]]
- 00bd6e74 ["CALLOTHER", "tmp:1:1", ["const:3f:4", "register:4008:8", "const:10:1"]]
- 00bd6e74 ["BOOL_NEGATE", "tmp:2:1", ["tmp:1:1"]]
- 00bd6e74 ["CBRANCH", null, ["const:3:4", "tmp:2:1"]]
- 00bd6e74 bytes 31fc0fc8
- 00bd6e78 ["INT_NOTEQUAL", "tmp:0:1", ["register:4078:4", "const:0:4"]]
- 00bd6e78 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd6e78 bytes afffff35
- 00bd6e7c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd6e7c ["RETURN", null, ["register:0:8"]]
- 00bd6e7c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d15579e529d4fc69169f7bf50827ed8"></a>

### [`00bd6e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e80.md) → [`00bd6ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6ec0.md) FUN_00bd6ec0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bd51f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51f0.md) [`00bd5414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5414.md) [`00bd55a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd55a4.md) · 呼出先 6件 [`00bd6f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6f78.md) [`00bd72f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72f0.md) [`00bd7398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7398.md) [`00bd7500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7500.md) [`00bd7528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7528.md)
- 新版 呼出元 3件 [`00bd5234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5234.md) [`00bd5458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5458.md) [`00bd55e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd55e8.md) · 呼出先 6件 [`00bd6fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6fb8.md) [`00bd7330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7330.md) [`00bd73d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd73d8.md) [`00bd7540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7540.md) [`00bd7568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7568.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 91.94% / 新版 91.94%

CFGの説明率　旧版 23.53% / 新版 23.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6f20"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd6f60"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6f24",
      "incomplete_value": true,
      "site": "00bd6f2c",
      "value": [
        "live",
        "register:8:8"
      ]
    },
    "old": null,
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
      "unmatched:00bd6f20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6fa0"
      ]
    ],
    [
      "unmatched:00bd6f50",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6f54",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd6f60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6fa0"
      ]
    ],
    [
      "00bd6f90",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6f94",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e80.md#insn-00bd6eec) · [`00bd6f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e80.md#insn-00bd6f20) · [`00bd6f5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e80.md#insn-00bd6f5c)
- 新版 [`00bd6f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6ec0.md#insn-00bd6f2c)

~~~diff
- 00bd6eec ["INT_ADD", "register:40f0:8", ["const:bd6eec:8", "const:4:8"]]
- 00bd6eec ["CALL", null, ["callee:00bd7568:8"]]
+ 00bd6f2c ["INT_ADD", "register:40f0:8", ["const:bd6f2c:8", "const:4:8"]]
+ 00bd6f2c ["CALL", null, ["callee:00bd7568:8"]]
- 00bd6eec bytes 8f010094
+ 00bd6f2c bytes 8f010094
- 00bd6f20 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd6f20 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00bd6f20 bytes 01020054
- 00bd6f5c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd6f5c ["RETURN", null, ["register:0:8"]]
- 00bd6f5c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68f19c9d9e252b98be76a2955828e21c"></a>

### [`00bd6f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6f78.md) → [`00bd6fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6fb8.md) FUN_00bd6fb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bd6e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e80.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) · 呼出先 9件 [`00bd72f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72f0.md) [`00bd7398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7398.md) [`00bd7514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7514.md) [`00bd7528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7528.md) [`00bd7568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7568.md)
- 新版 呼出元 2件 [`00bd6ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6ec0.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) · 呼出先 9件 [`00bd7330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7330.md) [`00bd73d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd73d8.md) [`00bd7554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7554.md) [`00bd7568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7568.md) [`00bd75a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75a8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 89.61% / 新版 89.61%

CFGの説明率　旧版 60.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7010"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd7050"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7090",
      "incomplete_value": true,
      "site": "00bd7094",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7050",
      "incomplete_value": true,
      "site": "00bd7054",
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
            "const:130:8"
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
      "unmatched:00bd703c",
      "READ",
      [
        "storage",
        "00c1bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bd7044",
      "PARAM",
      [
        "storage",
        "0029d229",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd704c",
      "PARAM",
      [
        "storage",
        "002a4196",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd707c",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ],
    [
      "00bd7084",
      "PARAM",
      [
        "storage",
        "0029d2b4",
        null,
        "string"
      ]
    ],
    [
      "00bd708c",
      "PARAM",
      [
        "storage",
        "002a4221",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6f78.md#insn-00bd7010) · [`00bd7014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6f78.md#insn-00bd7014) · [`00bd7050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6f78.md#insn-00bd7050)
- 新版 [`00bd7054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6fb8.md#insn-00bd7054)

~~~diff
- 00bd7010 ["COPY", "tmp:0:4", ["register:40b0:4"]]
- 00bd7010 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bd7010 ["COPY", "tmp:0:4", ["register:40a8:4"]]
- 00bd7010 ["INT_ZEXT", "register:4008:8", ["tmp:0:4"]]
- 00bd7010 bytes c102951a
- 00bd7014 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd7014 ["INT_ADD", "register:40f0:8", ["const:bd7014:8", "const:4:8"]]
- 00bd7014 ["CALLIND", null, ["register:0:8"]]
+ 00bd7054 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7054 ["INT_ADD", "register:40f0:8", ["const:bd7054:8", "const:4:8"]]
+ 00bd7054 ["CALLIND", null, ["register:0:8"]]
- 00bd7014 bytes 00013fd6
+ 00bd7054 bytes 00013fd6
- 00bd7050 ["COPY", "tmp:0:8", ["const:130:8"]]
- 00bd7050 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00bd7050 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00bd7050 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00bd7050 bytes 60c20491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4be4c7584325b7f2f9c6759919ba9f5b"></a>

### [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) → [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) FUN_00bd70ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 253件 [`0043e5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043e5d8.md) [`0043e940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043e940.md) [`00445124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445124.md) [`00450668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450668.md) [`00455270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00455/00455270.md) · 呼出先 7件 [`00bd6f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6f78.md) [`00bd7130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7130.md) [`00bdad98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdad98.md) [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 256件 [`0043e5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043e5d8.md) [`0043e940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043e940.md) [`00445124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445124.md) [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`00455270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455270.md) · 呼出先 7件 [`00bd6fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6fb8.md) [`00bd7170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7170.md) [`00bdadd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdadd8.md) [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd715c",
      "incomplete_value": true,
      "site": "00bd7160",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd711c",
      "incomplete_value": true,
      "site": "00bd7120",
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
            "const:130:8"
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
      "definition_site": "00bd7158",
      "incomplete_value": false,
      "site": "00bd7160",
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
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7118",
      "incomplete_value": false,
      "site": "00bd7120",
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
            "const:82d:8"
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
      "00bd7148",
      "READ",
      [
        "storage",
        "00c1bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "00bd7158",
      "PARAM",
      [
        "storage",
        "0029582d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd7148",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ],
    [
      "00bd7158",
      "PARAM",
      [
        "storage",
        "002957a0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd70e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md#insn-00bd70e0) · [`00bd7120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md#insn-00bd7120) · [`00bd70c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md#insn-00bd70c8)
- 新版 [`00bd7120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md#insn-00bd7120) · [`00bd7160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md#insn-00bd7160) · [`00bd7108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md#insn-00bd7108)

~~~diff
- 00bd70e0 ["INT_ADD", "register:40f0:8", ["const:bd70e0:8", "const:4:8"]]
- 00bd70e0 ["CALL", null, ["callee:00bd6fb8:8"]]
+ 00bd7120 ["INT_ADD", "register:40f0:8", ["const:bd7120:8", "const:4:8"]]
+ 00bd7120 ["CALL", null, ["callee:00bd6fb8:8"]]
- 00bd70e0 bytes a6ffff97
+ 00bd7120 bytes a6ffff97
- 00bd7120 ["INT_ADD", "register:40f0:8", ["const:bd7120:8", "const:4:8"]]
- 00bd7120 ["CALL", null, ["callee:00be1f80:8"]]
+ 00bd7160 ["INT_ADD", "register:40f0:8", ["const:bd7160:8", "const:4:8"]]
+ 00bd7160 ["CALL", null, ["callee:00be1f80:8"]]
- 00bd7120 bytes 842b0094
+ 00bd7160 bytes 882b0094
- 00bd70c8 ["INT_ADD", "register:40f0:8", ["const:bd70c8:8", "const:4:8"]]
- 00bd70c8 ["CALL", null, ["callee:00bdadd8:8"]]
+ 00bd7108 ["INT_ADD", "register:40f0:8", ["const:bd7108:8", "const:4:8"]]
+ 00bd7108 ["CALL", null, ["callee:00bdadd8:8"]]
- 00bd70c8 bytes 340f0094
+ 00bd7108 bytes 340f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2311e6d6b29c8f28669e5bb5f6c052e"></a>

### [`00bd7130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7130.md) → [`00bd7170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7170.md) FUN_00bd7170

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) · 呼出先 4件 [`00bd72f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72f0.md) [`00bd7514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7514.md) [`00bd7528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7528.md) [`00bd7568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7568.md)
- 新版 呼出元 1件 [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) · 呼出先 4件 [`00bd7330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7330.md) [`00bd7554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7554.md) [`00bd7568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7568.md) [`00bd75a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75a8.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 55.56% / 新版 58.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd720c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd724c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bd7184",
      "incomplete_value": true,
      "site": "00bd718c",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "ordinal": 2,
    "slot": 5
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd720c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd71e8"
      ]
    ]
  ],
  "added": [
    [
      "00bd724c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd71e8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd718c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7130.md#insn-00bd718c) · [`00bd720c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7130.md#insn-00bd720c)
- 新版 [`00bd71cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7170.md#insn-00bd71cc) · [`00bd724c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7170.md#insn-00bd724c)

~~~diff
- 00bd718c ["COPY", "register:0:8", ["register:4098:8"]]
- 00bd718c ["INT_ADD", "register:40f0:8", ["const:bd718c:8", "const:4:8"]]
- 00bd718c ["CALLIND", null, ["register:0:8"]]
+ 00bd71cc ["COPY", "register:0:8", ["register:4098:8"]]
+ 00bd71cc ["INT_ADD", "register:40f0:8", ["const:bd71cc:8", "const:4:8"]]
+ 00bd71cc ["CALLIND", null, ["register:0:8"]]
- 00bd718c bytes 60023fd6
+ 00bd71cc bytes 60023fd6
- 00bd720c ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00bd720c bytes e0fcff54
+ 00bd724c ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 00bd724c bytes e0fcff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01ec78fc5a5a7ad480c382811b5d6dfe"></a>

### [`00bd72f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72f0.md) → [`00bd7330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7330.md) FUN_00bd7330

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00bd6e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e80.md) [`00bd6f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6f78.md) [`00bd7130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7130.md) · 呼出先 2件 [`00bd7db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7db8.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 3件 [`00bd6ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6ec0.md) [`00bd6fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6fb8.md) [`00bd7170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7170.md) · 呼出先 2件 [`00bd7df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7df8.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, local_def_use, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd735c",
      "incomplete_value": false,
      "site": "00bd735c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c1a000:8"
          ],
          [
            "leaf",
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd731c",
      "incomplete_value": false,
      "site": "00bd731c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c1a000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
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
      "definition_site": "00bd735c",
      "incomplete_value": false,
      "site": "00bd735c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd731c",
      "incomplete_value": false,
      "site": "00bd731c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bd737c",
      "value": [
        "live",
        "register:5060:16"
      ]
    },
    "old": {
      "definition_site": "00bd732c",
      "incomplete_value": true,
      "site": "00bd733c",
      "value": [
        "LOAD",
        "16",
        [
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:110:8"
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
      "00bd735c",
      "DATA",
      [
        "storage",
        "00c1a1c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd735c",
      "DATA",
      [
        "storage",
        "010a39a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd735c",
      "DATA",
      [
        "storage",
        "00c1a218",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd735c",
      "DATA",
      [
        "storage",
        "010a39e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72f0.md#insn-00bd7304) · [`00bd7308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72f0.md#insn-00bd7308) · [`00bd730c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72f0.md#insn-00bd730c)
- 新版 [`00bd7344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7330.md#insn-00bd7344) · [`00bd734c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7330.md#insn-00bd734c)

~~~diff
- 00bd7304 ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 00bd7304 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd7304 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd7304 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd7344 ["COPY", "tmp:0:8", ["const:218:8"]]
+ 00bd7344 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd7344 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd7344 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd7304 bytes 08210791
+ 00bd7344 bytes 08610891
- 00bd7308 ["COPY", "register:4048:8", ["const:10a3000:8"]]
- 00bd7308 bytes 69260090
- 00bd730c ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 00bd730c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bd730c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bd730c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bd734c ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 00bd734c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd734c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd734c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bd730c bytes 29812691
+ 00bd734c bytes 29812791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49180739d1baf55e76ad32e13d139458"></a>

### [`00bd7590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7590.md) → [`00bd75d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75d0.md) FUN_00bd75d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00bd7db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7db8.md) [`00bd8120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd8120.md) [`00bdaa74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaa74.md) · 呼出先 3件 [`00bd7720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7720.md) [`00bd9470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9470.md) [`00bd97fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd97fc.md)
- 新版 呼出元 3件 [`00bd7df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7df8.md) [`00bd8160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd8160.md) [`00bdaab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaab4.md) · 呼出先 3件 [`00bd7760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7760.md) [`00bd94b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md) [`00bd983c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd983c.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7598"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd75d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bd7648",
      "incomplete_value": false,
      "site": "00bd7650",
      "value": [
        "leaf",
        "const:0:8"
      ]
    },
    "ordinal": 1,
    "slot": 5
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd7598",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bd764c",
      "DATA",
      [
        "storage",
        "0029793e",
        null,
        "string"
      ]
    ],
    [
      "00bd7658",
      "DATA",
      [
        "storage",
        "0029f2c0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd75d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bd764c",
      "DATA",
      [
        "storage",
        "002978b1",
        null,
        "string"
      ]
    ],
    [
      "00bd7658",
      "DATA",
      [
        "storage",
        "0029f34b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7590.md#insn-00bd7598) · [`00bd7650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7590.md#insn-00bd7650)
- 新版 [`00bd75d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75d0.md#insn-00bd75d8) · [`00bd7690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75d0.md#insn-00bd7690)

~~~diff
- 00bd7598 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bd7598 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00bd7598 bytes fb0b00f9
+ 00bd75d8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 00bd75d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
+ 00bd75d8 bytes fb0b00f9
- 00bd7650 ["INT_ADD", "register:40f0:8", ["const:bd7650:8", "const:4:8"]]
- 00bd7650 ["CALL", null, ["callee:00bd94b0:8"]]
+ 00bd7690 ["INT_ADD", "register:40f0:8", ["const:bd7690:8", "const:4:8"]]
+ 00bd7690 ["CALL", null, ["callee:00bd94b0:8"]]
- 00bd7650 bytes 88070094
+ 00bd7690 bytes 88070094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b2eedad842d3dacada27043d838a8ce"></a>

### [`00bd7720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7720.md) → [`00bd7760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7760.md) FUN_00bd7760

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bd7590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7590.md) [`00bda8ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda8ac.md) · 呼出先 6件 [`00bd9470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9470.md) [`00bd97fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd97fc.md) [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f30.md)
- 新版 呼出元 2件 [`00bd75d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75d0.md) [`00bda8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda8ec.md) · 呼出先 6件 [`00bd94b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md) [`00bd983c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd983c.md) [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.57% / 新版 91.57%

CFGの説明率　旧版 37.50% / 新版 39.13%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_condition` 4件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd78d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd7910"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd77ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd77ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd79f4"
      ]
    ],
    [
      "00bd7848",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd77e8"
      ]
    ],
    [
      "00bd78a0",
      "DATA",
      [
        "storage",
        "00294599",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd782c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd79f4"
      ]
    ],
    [
      "00bd7848",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7828"
      ]
    ],
    [
      "00bd78a0",
      "DATA",
      [
        "storage",
        "0029450c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd77ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7720.md#insn-00bd77ec) · [`00bd7858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7720.md#insn-00bd7858)
- 新版 [`00bd782c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7760.md#insn-00bd782c) · [`00bd7898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7760.md#insn-00bd7898)

~~~diff
- 00bd77ec ["CBRANCH", null, ["local:b50:8", "register:101:1"]]
- 00bd77ec bytes 400e0054
+ 00bd782c ["CBRANCH", null, ["local:b47:8", "register:101:1"]]
+ 00bd782c bytes 400e0054
- 00bd7858 ["BRANCH", null, ["local:b48:8"]]
+ 00bd7898 ["BRANCH", null, ["local:b45:8"]]
- 00bd7858 bytes 4b000014
+ 00bd7898 bytes 4b000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0707b525c8fd24ded5b5febcd4feae73"></a>

### [`00bd7a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7a3c.md) → [`00bd7a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7a7c.md) FUN_00bd7a7c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f30.md) [`010a58b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a58b8.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f80.md) [`010a58b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a58b8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 86.21% / 新版 86.21%

CFGの説明率　旧版 69.57% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7a68"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd7aa8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bd7b10",
      "incomplete_value": true,
      "site": "00bd7b14",
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
            "const:130:8"
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
      "unmatched:00bd7a68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7ae4"
      ]
    ],
    [
      "unmatched:00bd7afc",
      "READ",
      [
        "storage",
        "00c1bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bd7b04",
      "PARAM",
      [
        "storage",
        "0029f2ac",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd7aa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7ae4"
      ]
    ],
    [
      "00bd7b3c",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ],
    [
      "00bd7b44",
      "PARAM",
      [
        "storage",
        "0029f337",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7a3c.md#insn-00bd7a68) · [`00bd7aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7a3c.md#insn-00bd7aa8)
- 新版 [`00bd7aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7a7c.md#insn-00bd7aa8)

~~~diff
- 00bd7a68 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 00bd7a68 bytes e0010054
- 00bd7aa8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bd7aa8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd7aa8 bytes 000140f9
+ 00bd7aa8 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
+ 00bd7aa8 bytes e0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36e51ec41d3c2c8b04f23103d7731afe"></a>

### [`00bd7b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7b24.md) → [`00bd7b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7b64.md) FUN_00bd7b64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f30.md) [`010a58b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a58b8.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f80.md) [`010a58b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a58b8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 78.26% / 新版 81.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7c38",
      "incomplete_value": true,
      "site": "00bd7c3c",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7bf8",
      "incomplete_value": true,
      "site": "00bd7bfc",
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
            "const:130:8"
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
      "definition_site": "00bd7c2c",
      "incomplete_value": false,
      "site": "00bd7c3c",
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
            "const:369:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7bec",
      "incomplete_value": false,
      "site": "00bd7bfc",
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
            "const:2de:8"
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
      "definition_site": "00bd7c34",
      "incomplete_value": false,
      "site": "00bd7c3c",
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
            "const:a4a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7bf4",
      "incomplete_value": false,
      "site": "00bd7bfc",
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
            "const:ad7:8"
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
      "unmatched:00bd7be0",
      "PARAM",
      [
        "storage",
        "0029182b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd7be4",
      "READ",
      [
        "storage",
        "00c1bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bd7bec",
      "PARAM",
      [
        "storage",
        "002a52de",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd7c20",
      "PARAM",
      [
        "storage",
        "0029182b",
        null,
        "string"
      ]
    ],
    [
      "00bd7c24",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ],
    [
      "00bd7c2c",
      "PARAM",
      [
        "storage",
        "002a5369",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7b24.md#insn-00bd7bfc) · [`00bd7b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7b24.md#insn-00bd7b3c) · [`00bd7b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7b24.md#insn-00bd7b48)
- 新版 [`00bd7c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7b64.md#insn-00bd7c3c) · [`00bd7b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7b64.md#insn-00bd7b7c) · [`00bd7b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7b64.md#insn-00bd7b88)

~~~diff
- 00bd7bfc ["INT_ADD", "register:40f0:8", ["const:bd7bfc:8", "const:4:8"]]
- 00bd7bfc ["CALL", null, ["callee:00be1f80:8"]]
+ 00bd7c3c ["INT_ADD", "register:40f0:8", ["const:bd7c3c:8", "const:4:8"]]
+ 00bd7c3c ["CALL", null, ["callee:00be1f80:8"]]
- 00bd7bfc bytes cd280094
+ 00bd7c3c bytes d1280094
- 00bd7b3c ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
+ 00bd7b7c ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00bd7b3c bytes a0030054
+ 00bd7b7c bytes a0030054
- 00bd7b48 ["BRANCH", null, ["local:b14:8"]]
+ 00bd7b88 ["BRANCH", null, ["local:b13:8"]]
- 00bd7b48 bytes 14000014
+ 00bd7b88 bytes 14000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44a349a14c7f3ebdd88750c548cb77c2"></a>

### [`00bd7db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7db8.md) → [`00bd7df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7df8.md) FUN_00bd7df8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00bd72f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72f0.md) · 呼出先 10件 [`00bd7590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7590.md) [`00bd85b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd85b4.md) [`00bda388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda388.md) [`00bda65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda65c.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)
- 新版 呼出元 1件 [`00bd7330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7330.md) · 呼出先 10件 [`00bd75d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75d0.md) [`00bd85f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd85f4.md) [`00bda3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda3c8.md) [`00bda69c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda69c.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 96.50% / 新版 96.50%

CFGの説明率　旧版 60.53% / 新版 62.16%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7e48",
      "incomplete_value": false,
      "site": "00bd7e58",
      "value": [
        "leaf",
        "const:bda69c:8"
      ]
    },
    "old": {
      "definition_site": "00bd7e08",
      "incomplete_value": false,
      "site": "00bd7e18",
      "value": [
        "leaf",
        "const:bda65c:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7e84",
      "incomplete_value": false,
      "site": "00bd7e88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:9e4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7e44",
      "incomplete_value": false,
      "site": "00bd7e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:9a4:8"
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
      "definition_site": "00bd7ecc",
      "incomplete_value": false,
      "site": "00bd7ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:9e4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7e8c",
      "incomplete_value": false,
      "site": "00bd7e90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:9a4:8"
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
      "00bd7e48",
      "PARAM",
      [
        "storage",
        "00bda65c",
        null,
        null
      ]
    ],
    [
      "00bd7e84",
      "PARAM",
      [
        "storage",
        "010a39a4",
        null,
        null
      ]
    ],
    [
      "00bd7e94",
      "READ",
      [
        "storage",
        "00c24978",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bd7e48",
      "PARAM",
      [
        "storage",
        "00bda69c",
        null,
        null
      ]
    ],
    [
      "00bd7e84",
      "PARAM",
      [
        "storage",
        "010a39e4",
        null,
        null
      ]
    ],
    [
      "00bd7e94",
      "READ",
      [
        "storage",
        "00c249c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7db8.md#insn-00bd7e08) · [`00bd7e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7db8.md#insn-00bd7e18) · [`00bd7e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7db8.md#insn-00bd7e48)
- 新版 [`00bd7e48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7df8.md#insn-00bd7e48) · [`00bd7e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7df8.md#insn-00bd7e58) · [`00bd7e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7df8.md#insn-00bd7e88)

~~~diff
- 00bd7e08 ["COPY", "register:4000:8", ["const:bda65c:8"]]
+ 00bd7e48 ["COPY", "register:4000:8", ["const:bda69c:8"]]
- 00bd7e08 bytes a0420110
+ 00bd7e48 bytes a0420110
- 00bd7e18 ["INT_ADD", "register:40f0:8", ["const:bd7e18:8", "const:4:8"]]
- 00bd7e18 ["CALL", null, ["callee:00be1fb0:8"]]
+ 00bd7e58 ["INT_ADD", "register:40f0:8", ["const:bd7e58:8", "const:4:8"]]
+ 00bd7e58 ["CALL", null, ["callee:00be1fb0:8"]]
- 00bd7e18 bytes 52280094
+ 00bd7e58 bytes 56280094
- 00bd7e48 ["INT_ADD", "register:40f0:8", ["const:bd7e48:8", "const:4:8"]]
- 00bd7e48 ["CALL", null, ["callee:00be1fc0:8"]]
+ 00bd7e88 ["INT_ADD", "register:40f0:8", ["const:bd7e88:8", "const:4:8"]]
+ 00bd7e88 ["CALL", null, ["callee:00be1fc0:8"]]
- 00bd7e48 bytes 4a280094
+ 00bd7e88 bytes 4e280094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d20f252ef130dd6e09aa708279a9b2e7"></a>

### [`00bd8120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd8120.md) → [`00bd8160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd8160.md) FUN_00bd8160

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bd7c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7c40.md) · 呼出先 11件 [`00bd7590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7590.md) [`00bd85b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd85b4.md) [`00bd912c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd912c.md) [`00bd9260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9260.md) [`00bd99c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd99c4.md)
- 新版 呼出元 1件 [`00bd7c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7c80.md) · 呼出先 11件 [`00bd75d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75d0.md) [`00bd85f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd85f4.md) [`00bd916c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd916c.md) [`00bd92a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd92a0.md) [`00bd9a04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd9a04.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.74% / 新版 88.74%

CFGの説明率　旧版 51.85% / 新版 50.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_condition` 3件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8434"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8458"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd8474"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd82b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd84b4"
      ]
    ],
    [
      "unmatched:00bd8300",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd8434"
      ]
    ],
    [
      "unmatched:00bd8384",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd83e8"
      ]
    ]
  ],
  "added": [
    [
      "00bd82f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd84b4"
      ]
    ],
    [
      "00bd8340",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd8434"
      ]
    ],
    [
      "00bd83c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd83e8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd82b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd8120.md#insn-00bd82b0) · [`00bd8300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd8120.md#insn-00bd8300)
- 新版 [`00bd82f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd8160.md#insn-00bd82f0)

~~~diff
- 00bd82b0 ["CBRANCH", null, ["local:b58:8", "register:101:1"]]
- 00bd82b0 bytes 200e0054
+ 00bd82f0 ["CBRANCH", null, ["local:b59:8", "register:101:1"]]
+ 00bd82f0 bytes 200e0054
- 00bd8300 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd8300 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 00bd8300 ["CBRANCH", null, ["local:b43:8", "tmp:1:1"]]
- 00bd8300 bytes ad070054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1eafaffd6c6f24cc75bab7d0695ee502"></a>

### [`00bd85b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd85b4.md) → [`00bd85f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd85f4.md) FUN_00bd85f4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bd7db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7db8.md) [`00bd8120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd8120.md) [`00bda388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda388.md) · 呼出先 8件 [`00bd9470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9470.md) [`00bd97fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd97fc.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bdd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd380.md)
- 新版 呼出元 3件 [`00bd7df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7df8.md) [`00bd8160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd8160.md) [`00bda3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda3c8.md) · 呼出先 8件 [`00bd94b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md) [`00bd983c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd983c.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.84% / 新版 73.84%

CFGの説明率　旧版 37.41% / 新版 35.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_condition` 2件, `unresolved_branch_alignment` 27件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8614"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8618"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8638"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd8614",
      "WRITE",
      [
        "storage",
        "Stack[-0x6cc]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd8618",
      "WRITE",
      [
        "storage",
        "Stack[-0x6d8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd8638",
      "WRITE",
      [
        "storage",
        "Stack[-0x6c8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd8654",
      "WRITE",
      [
        "storage",
        "Stack[-0x6cc]",
        null,
        null
      ]
    ],
    [
      "00bd8658",
      "WRITE",
      [
        "storage",
        "Stack[-0x6d8]",
        null,
        null
      ]
    ],
    [
      "00bd8678",
      "WRITE",
      [
        "storage",
        "Stack[-0x6c8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd8614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd85b4.md#insn-00bd8614) · [`00bd8618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd85b4.md#insn-00bd8618)
- 新版 [`00bd8614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd85f4.md#insn-00bd8614)

~~~diff
- 00bd8614 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:24:8"]]
- 00bd8614 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4020:4"]]
- 00bd8614 bytes 642600b9
+ 00bd8614 ["INT_SUB", "register:8:8", ["register:8:8", "const:690:8"]]
+ 00bd8614 bytes ff431ad1
- 00bd8618 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:18:8"]]
- 00bd8618 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd8618 bytes 600e00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d607996b9b947e81f02e3d47e71b7d93"></a>

### [`00bd912c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd912c.md) → [`00bd916c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd916c.md) FUN_00bd916c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bd8120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd8120.md) · 呼出先 5件 [`00bd99c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd99c4.md) [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f30.md) [`010a58b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a58b8.md)
- 新版 呼出元 1件 [`00bd8160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd8160.md) · 呼出先 5件 [`00bd9a04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd9a04.md) [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f80.md) [`010a58b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a58b8.md)

変更の種類 call_argument_candidate, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.21% / 新版 92.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd928c",
      "incomplete_value": true,
      "site": "00bd9290",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd924c",
      "incomplete_value": true,
      "site": "00bd9250",
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
            "const:130:8"
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
      "definition_site": "00bd9280",
      "incomplete_value": false,
      "site": "00bd9290",
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
            "const:337:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9240",
      "incomplete_value": false,
      "site": "00bd9250",
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
            "const:2ac:8"
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
      "definition_site": "00bd9288",
      "incomplete_value": false,
      "site": "00bd9290",
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
            "const:a4a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9248",
      "incomplete_value": false,
      "site": "00bd9250",
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
            "const:ad7:8"
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
      "00bd9278",
      "READ",
      [
        "storage",
        "00c1bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "00bd9280",
      "PARAM",
      [
        "storage",
        "0029f2ac",
        null,
        "string"
      ]
    ],
    [
      "00bd9288",
      "PARAM",
      [
        "storage",
        "00299ad7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd9278",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ],
    [
      "00bd9280",
      "PARAM",
      [
        "storage",
        "0029f337",
        null,
        "string"
      ]
    ],
    [
      "00bd9288",
      "PARAM",
      [
        "storage",
        "00299a4a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd912c.md#insn-00bd9250) · [`00bd9258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd912c.md#insn-00bd9258) · [`00bd91e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd912c.md#insn-00bd91e4)
- 新版 [`00bd9290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd916c.md#insn-00bd9290) · [`00bd9298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd916c.md#insn-00bd9298)

~~~diff
- 00bd9250 ["INT_ADD", "register:40f0:8", ["const:bd9250:8", "const:4:8"]]
- 00bd9250 ["CALL", null, ["callee:00be1f80:8"]]
+ 00bd9290 ["INT_ADD", "register:40f0:8", ["const:bd9290:8", "const:4:8"]]
+ 00bd9290 ["CALL", null, ["callee:00be1f80:8"]]
- 00bd9250 bytes 38230094
+ 00bd9290 bytes 3c230094
- 00bd9258 ["INT_ADD", "register:40f0:8", ["const:bd9258:8", "const:4:8"]]
- 00bd9258 ["CALL", null, ["callee:00bdd360:8"]]
+ 00bd9298 ["INT_ADD", "register:40f0:8", ["const:bd9298:8", "const:4:8"]]
+ 00bd9298 ["CALL", null, ["callee:00bdd360:8"]]
- 00bd9258 bytes 2e100094
+ 00bd9298 bytes 32100094
- 00bd91e4 ["COPY", "register:4000:8", ["register:4040:8"]]
- 00bd91e4 bytes e00308aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2c490354bbc662a7f1c44578454efd2"></a>

### [`00bd9470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9470.md) → [`00bd94b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md) FUN_00bd94b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`00bd7590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7590.md) [`00bd7720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7720.md) [`00bd85b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd85b4.md) [`00bda78c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda78c.md) [`00bda8ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda8ac.md) · 呼出先 5件 [`00bd97fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd97fc.md) [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f30.md) [`010a58b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a58b8.md)
- 新版 呼出元 6件 [`00bd75d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75d0.md) [`00bd7760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7760.md) [`00bd85f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd85f4.md) [`00bda7cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda7cc.md) [`00bda8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda8ec.md) · 呼出先 5件 [`00bd983c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd983c.md) [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f80.md) [`010a58b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a58b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 75.77% / 新版 75.77%

CFGの説明率　旧版 58.97% / 新版 60.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 8件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd94bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd9530"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd94e8"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd9570",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd965c"
      ]
    ],
    [
      "00bd94f4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd97c8"
      ]
    ],
    [
      "unmatched:00bd94bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd953c"
      ]
    ]
  ],
  "added": [
    [
      "00bd94e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd965c"
      ]
    ],
    [
      "00bd94f4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd9808"
      ]
    ],
    [
      "00bd94fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd953c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd94bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9470.md#insn-00bd94bc)
- 新版 [`00bd94e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md#insn-00bd94e8) · [`00bd94fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md#insn-00bd94fc)

~~~diff
- 00bd94bc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd94bc ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00bd94bc ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00bd94bc ["CBRANCH", null, ["local:b12:8", "tmp:2:1"]]
- 00bd94bc bytes 0c020054
+ 00bd94e8 ["CBRANCH", null, ["local:b34:8", "register:101:1"]]
+ 00bd94e8 bytes a00b0054
+ 00bd94fc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00bd94fc ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
+ 00bd94fc ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
+ 00bd94fc ["CBRANCH", null, ["local:b12:8", "tmp:2:1"]]
+ 00bd94fc bytes 0c020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b922b1383464f1af57b73d1df034d19"></a>

### [`00bd97fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd97fc.md) → [`00bd983c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd983c.md) FUN_00bd983c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`00bd7590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7590.md) [`00bd7720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7720.md) [`00bd85b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd85b4.md) [`00bd9470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9470.md) [`00bd99c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd99c4.md) · 呼出先 4件 [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f30.md) [`010a58b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a58b8.md)
- 新版 呼出元 6件 [`00bd75d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75d0.md) [`00bd7760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7760.md) [`00bd85f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd85f4.md) [`00bd94b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md) [`00bd9a04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd9a04.md) · 呼出先 4件 [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f80.md) [`010a58b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a58b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 85.96% / 新版 85.96%

CFGの説明率　旧版 43.75% / 新版 42.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd9860"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd9874"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd98b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd9860",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd999c"
      ]
    ],
    [
      "unmatched:00bd9874",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd986c"
      ]
    ],
    [
      "unmatched:00bd98b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd999c"
      ]
    ]
  ],
  "added": [
    [
      "00bd98a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd999c"
      ]
    ],
    [
      "00bd98f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd999c"
      ]
    ],
    [
      "00bd995c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd986c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd97fc.md#insn-00bd9860) · [`00bd9874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd97fc.md#insn-00bd9874)
- 新版 [`00bd98a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd983c.md#insn-00bd98a0)

~~~diff
- 00bd9860 ["CBRANCH", null, ["local:b26:8", "register:101:1"]]
- 00bd9860 bytes e0070054
- 00bd9874 ["INT_RIGHT", "tmp:0:4", ["register:4058:4", "const:1f:4"]]
- 00bd9874 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00bd9874 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00bd9874 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00bd9874 bytes cbfdff36
+ 00bd98a0 ["CBRANCH", null, ["local:b27:8", "register:101:1"]]
+ 00bd98a0 bytes e0070054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe27c752ccff2a1d84abb3d9ea77c145"></a>

### [`00bd99c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd99c4.md) → [`00bd9a04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd9a04.md) FUN_00bd9a04

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bd8120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd8120.md) [`00bd912c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd912c.md) [`00bd9260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9260.md) · 呼出先 5件 [`00bd97fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd97fc.md) [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f30.md) [`010a58b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a58b8.md)
- 新版 呼出元 3件 [`00bd8160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd8160.md) [`00bd916c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd916c.md) [`00bd92a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd92a0.md) · 呼出先 5件 [`00bd983c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd983c.md) [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f80.md) [`010a58b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a58b8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.72% / 新版 74.72%

CFGの説明率　旧版 53.63% / 新版 53.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 24件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd9cd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd9e58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd9e90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd9aa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bda244"
      ]
    ],
    [
      "00bd9ab0",
      "DATA",
      [
        "storage",
        "002fdff8",
        "switchD_00bd9a78::switchdataD_002fdff8",
        "ushort"
      ]
    ],
    [
      "00bd9ab8",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:00bda244"
      ]
    ]
  ],
  "added": [
    [
      "00bd9aa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bda284"
      ]
    ],
    [
      "00bd9ab0",
      "DATA",
      [
        "storage",
        "002fdff8",
        "switchD_00bd9ab8::switchdataD_002fdff8",
        "ushort"
      ]
    ],
    [
      "00bd9ab8",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "00bda284"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd99c4.md#insn-00bd9af8)
- 新版 [`00bd9af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd9a04.md#insn-00bd9af8) · [`00bd9b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd9a04.md#insn-00bd9b38)

~~~diff
- 00bd9af8 ["CBRANCH", null, ["local:b34:8", "register:101:1"]]
- 00bd9af8 bytes a0040054
+ 00bd9af8 ["INT_OR", "register:4050:8", ["register:4078:8", "register:4050:8"]]
+ 00bd9af8 bytes ea010aaa
+ 00bd9b38 ["CBRANCH", null, ["local:b34:8", "register:101:1"]]
+ 00bd9b38 bytes a0040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90f17e78733b2c3f141413c1a06a2715"></a>

### [`00bda388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda388.md) → [`00bda3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda3c8.md) FUN_00bda3c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bd7db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7db8.md) · 呼出先 10件 [`00bd85b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd85b4.md) [`00bda8ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda8ac.md) [`00bdaa74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaa74.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)
- 新版 呼出元 1件 [`00bd7df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7df8.md) · 呼出先 10件 [`00bd85f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd85f4.md) [`00bda8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda8ec.md) [`00bdaab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaab4.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.53% / 新版 84.53%

CFGの説明率　旧版 49.15% / 新版 48.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 9件, `store_destination` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bda640",
      "incomplete_value": true,
      "site": "00bda640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:9c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda600",
      "incomplete_value": true,
      "site": "00bda600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:978:8"
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
      "definition_site": "00bda644",
      "incomplete_value": true,
      "site": "00bda644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda604",
      "incomplete_value": true,
      "site": "00bda604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bda60c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bda44c",
      "PARAM",
      [
        "storage",
        "010a39a4",
        null,
        null
      ]
    ],
    [
      "00bda45c",
      "READ",
      [
        "storage",
        "00c24978",
        null,
        "pointer"
      ]
    ],
    [
      "00bda460",
      "READ",
      [
        "storage",
        "00c24980",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bda44c",
      "PARAM",
      [
        "storage",
        "010a39e4",
        null,
        null
      ]
    ],
    [
      "00bda45c",
      "READ",
      [
        "storage",
        "00c249c8",
        null,
        "pointer"
      ]
    ],
    [
      "00bda460",
      "READ",
      [
        "storage",
        "00c249d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda388.md#insn-00bda3fc) · [`00bda410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda388.md#insn-00bda410) · [`00bda458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda388.md#insn-00bda458)
- 新版 [`00bda43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda3c8.md#insn-00bda43c) · [`00bda450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda3c8.md#insn-00bda450)

~~~diff
- 00bda3fc ["INT_ADD", "register:40f0:8", ["const:bda3fc:8", "const:4:8"]]
- 00bda3fc ["CALL", null, ["callee:00bdaab4:8"]]
+ 00bda43c ["INT_ADD", "register:40f0:8", ["const:bda43c:8", "const:4:8"]]
+ 00bda43c ["CALL", null, ["callee:00bdaab4:8"]]
- 00bda3fc bytes 9e010094
+ 00bda43c bytes 9e010094
- 00bda410 ["INT_ADD", "register:40f0:8", ["const:bda410:8", "const:4:8"]]
- 00bda410 ["CALL", null, ["callee:00be1fc0:8"]]
+ 00bda450 ["INT_ADD", "register:40f0:8", ["const:bda450:8", "const:4:8"]]
+ 00bda450 ["CALL", null, ["callee:00be1fc0:8"]]
- 00bda410 bytes d81e0094
+ 00bda450 bytes dc1e0094
- 00bda458 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bda458 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bda458 ["CBRANCH", null, ["local:b8:8", "tmp:1:1"]]
- 00bda458 bytes 08ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-caa223135fc52a1dc5557d162e14eb4c"></a>

### [`00bda78c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda78c.md) → [`00bda7cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda7cc.md) FUN_00bda7cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bda65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda65c.md) [`00bdaa74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaa74.md) · 呼出先 4件 [`00bd9470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9470.md) [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00be1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f30.md) [`010a58b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a58b8.md)
- 新版 呼出元 2件 [`00bda69c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda69c.md) [`00bdaab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaab4.md) · 呼出先 4件 [`00bd94b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md) [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00be1f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f80.md) [`010a58b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a58b8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.72% / 新版 84.72%

CFGの説明率　旧版 53.33% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bda7f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bda838"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bda7e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bda808",
      "PARAM",
      [
        "storage",
        "002a41f9",
        null,
        "string"
      ]
    ],
    [
      "00bda80c",
      "READ",
      [
        "storage",
        "00c1bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bda7e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bda880"
      ]
    ]
  ],
  "added": [
    [
      "00bda808",
      "PARAM",
      [
        "storage",
        "002a4284",
        null,
        "string"
      ]
    ],
    [
      "00bda80c",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ],
    [
      "00bda828",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bda880"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda78c.md#insn-00bda7d8) · [`00bda7dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda78c.md#insn-00bda7dc) · [`00bda7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda78c.md#insn-00bda7e8)
- 新版 [`00bda818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda7cc.md#insn-00bda818) · [`00bda81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda7cc.md#insn-00bda81c)

~~~diff
- 00bda7d8 ["INT_ADD", "register:40f0:8", ["const:bda7d8:8", "const:4:8"]]
- 00bda7d8 ["CALL", null, ["callee:00be1f80:8"]]
+ 00bda818 ["INT_ADD", "register:40f0:8", ["const:bda818:8", "const:4:8"]]
+ 00bda818 ["CALL", null, ["callee:00be1f80:8"]]
- 00bda7d8 bytes d61d0094
+ 00bda818 bytes da1d0094
- 00bda7dc ["BRANCH", null, ["local:b9:8"]]
+ 00bda81c ["BRANCH", null, ["local:b8:8"]]
- 00bda7dc bytes 21000014
+ 00bda81c bytes 21000014
- 00bda7e8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bda7e8 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00bda7e8 bytes c1020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abb5b0dfc5ac87f271bb06272a1a25f0"></a>

### [`00bda8ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda8ac.md) → [`00bda8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda8ec.md) FUN_00bda8ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bda388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda388.md) · 呼出先 3件 [`00bd7720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7720.md) [`00bd9470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9470.md) [`00bd97fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd97fc.md)
- 新版 呼出元 1件 [`00bda3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda3c8.md) · 呼出先 3件 [`00bd7760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7760.md) [`00bd94b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md) [`00bd983c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd983c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 63.89% / 新版 65.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bda934"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bda974"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bda9c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bda934",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bda9c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bda948"
      ]
    ]
  ],
  "added": [
    [
      "00bda974",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00bdaa00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bda948"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda8ac.md#insn-00bda934) · [`00bda9ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda8ac.md#insn-00bda9ac)
- 新版 [`00bda974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda8ec.md#insn-00bda974) · [`00bda9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda8ec.md#insn-00bda9ec)

~~~diff
- 00bda934 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00bda934 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bda934 bytes e80700f9
+ 00bda974 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
+ 00bda974 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00bda974 bytes e80700f9
- 00bda9ac ["INT_ADD", "register:40f0:8", ["const:bda9ac:8", "const:4:8"]]
- 00bda9ac ["CALL", null, ["callee:00bd94b0:8"]]
+ 00bda9ec ["INT_ADD", "register:40f0:8", ["const:bda9ec:8", "const:4:8"]]
+ 00bda9ec ["CALL", null, ["callee:00bd94b0:8"]]
- 00bda9ac bytes b1faff97
+ 00bda9ec bytes b1faff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f3ec2a6deacec6eb30d56ce07a970bc"></a>

### [`00bdabdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdabdc.md) → [`00bdac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdac1c.md) FUN_00bdac1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdaa74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaa74.md) · 呼出先 4件 [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f30.md) [`010a58b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a58b8.md)
- 新版 呼出元 1件 [`00bdaab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaab4.md) · 呼出先 4件 [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f80.md) [`010a58b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a58b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 69.23% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdabf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bdac38"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdacc4",
      "incomplete_value": true,
      "site": "00bdacc8",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdac84",
      "incomplete_value": true,
      "site": "00bdac88",
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
            "const:130:8"
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
      "unmatched:00bdabf8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdac58"
      ]
    ],
    [
      "00bdacb0",
      "READ",
      [
        "storage",
        "00c1bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdacb8",
      "PARAM",
      [
        "storage",
        "00299b1c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdac38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdac58"
      ]
    ],
    [
      "00bdacb0",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ],
    [
      "00bdacb8",
      "PARAM",
      [
        "storage",
        "00299a8f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdabf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdabdc.md#insn-00bdabf8) · [`00bdac14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdabdc.md#insn-00bdac14)
- 新版 [`00bdac54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdac1c.md#insn-00bdac54) · [`00bdac38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdac1c.md#insn-00bdac38)

~~~diff
- 00bdabf8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bdabf8 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00bdabf8 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00bdabf8 ["CBRANCH", null, ["local:b6:8", "tmp:2:1"]]
- 00bdabf8 bytes 0c010054
- 00bdac14 ["BRANCH", null, ["local:b14:8"]]
+ 00bdac54 ["BRANCH", null, ["local:b15:8"]]
- 00bdac14 bytes 14000014
+ 00bdac54 bytes 14000014
+ 00bdac38 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00bdac38 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
+ 00bdac38 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
+ 00bdac38 ["CBRANCH", null, ["local:b6:8", "tmp:2:1"]]
+ 00bdac38 bytes 0c010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed42dd44f451501dc4c6682e6875ba25"></a>

### [`00bdaec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaec8.md) → [`00bdaf18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaf18.md) _ZnwmSt11align_val_t

採用 · 移動量 `+0x50` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1eb0.md) · 呼出先 6件 [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdbba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbba0.md) [`00be1dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1dd0.md)
- 新版 呼出元 1件 [`00be1f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f00.md) · 呼出先 6件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbf0.md) [`00be1e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 86.11% / 新版 86.11%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdaeec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bdaf3c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdaf40",
      "incomplete_value": true,
      "site": "00bdaf50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": null,
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
      "unmatched:00bdaf4c",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdaf4c",
      "PARAM",
      [
        "storage",
        "00c168a0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:00bdaf50",
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
      "00bdaf9c",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdaf9c",
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bdafa0",
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

- 旧版 [`00bdaeec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaec8.md#insn-00bdaeec) · [`00bdaf00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaec8.md#insn-00bdaf00) · [`00bdaf2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaec8.md#insn-00bdaf2c)
- 新版 [`00bdaf50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaf18.md#insn-00bdaf50)

~~~diff
- 00bdaeec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bdaeec ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bdaeec ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00bdaeec ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bdaeec bytes 3480889a
- 00bdaf00 ["INT_ADD", "register:40f0:8", ["const:bdaf00:8", "const:4:8"]]
- 00bdaf00 ["CALL", null, ["callee:00be1f10:8"]]
+ 00bdaf50 ["INT_ADD", "register:40f0:8", ["const:bdaf50:8", "const:4:8"]]
+ 00bdaf50 ["CALL", null, ["callee:00be1f10:8"]]
- 00bdaf00 bytes f01b0094
+ 00bdaf50 bytes f01b0094
- 00bdaf2c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bdaf2c ["RETURN", null, ["register:0:8"]]
- 00bdaf2c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

