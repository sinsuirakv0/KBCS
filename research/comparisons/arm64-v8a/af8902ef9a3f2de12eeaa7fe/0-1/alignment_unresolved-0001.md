# v15.7.3 → v15.7.4 · 命令位置の検査未完了 (1)

[一覧の目次](README.md)

<a id="compare-d43b8a761c2ea776aced056c1456d7be"></a>

### [`0044a8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8e8.md) → [`0044a8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8e8.md) FUN_0044a8e8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`009a6228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a6/009a6228.md) [`009a6234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a6/009a6234.md) [`009a6240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a6/009a6240.md) [`009a9ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a9/009a9ce0.md) · 呼出先 7件 [`0044ac28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac28.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb500.md) [`00bdb510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb510.md)
- 新版 呼出元 5件 [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`009a6228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a6/009a6228.md) [`009a6234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a6/009a6234.md) [`009a6240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a6/009a6240.md) [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 7件 [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md) [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0044a940",
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
      "0044a940",
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

- 旧版 [`0044a934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8e8.md#insn-0044a934) · [`0044a938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8e8.md#insn-0044a938)
- 新版 [`0044a934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8e8.md#insn-0044a934) · [`0044a938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8e8.md#insn-0044a938)

~~~diff
- 0044a934 ["COPY", "tmp:0:8", ["const:a1:8"]]
- 0044a934 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044a934 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044a934 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044a934 ["COPY", "tmp:0:8", ["const:13b:8"]]
+ 0044a934 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044a934 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044a934 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044a934 bytes 08850291
+ 0044a934 bytes 08ed0491
- 0044a938 ["COPY", "register:4048:8", ["const:2b2000:8"]]
- 0044a938 bytes 49f3ff90
+ 0044a938 ["COPY", "register:4048:8", ["const:2b2000:8"]]
+ 0044a938 bytes 49f3ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dca40919948b551aa3537e675865cb9"></a>

### [`004532cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00453/004532cc.md) → [`004532cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004532cc.md) FUN_004532cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00452ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00452/00452ec8.md) · 呼出先 11件 [`004512c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00451/004512c0.md) [`004537f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00453/004537f0.md) [`00453c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00453/00453c78.md) [`00454af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00454/00454af4.md) [`00454f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00454/00454f34.md)
- 新版 呼出元 1件 [`00452ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452ec8.md) · 呼出先 11件 [`004512c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/004512c0.md) [`004537f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004537f0.md) [`00453c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/00453c78.md) [`00454af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454af4.md) [`00454f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454f34.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.57% / 新版 98.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00453410",
      "READ",
      [
        "storage",
        "0029f355",
        null,
        "string"
      ]
    ],
    [
      "00453420",
      "READ",
      [
        "storage",
        "0029f35f",
        null,
        "string"
      ]
    ],
    [
      "00453438",
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
      "00453410",
      "READ",
      [
        "storage",
        "0029f3e0",
        null,
        "string"
      ]
    ],
    [
      "00453420",
      "READ",
      [
        "storage",
        "0029f3ea",
        null,
        "string"
      ]
    ],
    [
      "00453438",
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

- 旧版 [`00453338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00453/004532cc.md#insn-00453338) · [`0045333c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00453/004532cc.md#insn-0045333c)
- 新版 [`00453338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004532cc.md#insn-00453338) · [`0045333c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004532cc.md#insn-0045333c)

~~~diff
- 00453338 ["COPY", "tmp:0:8", ["const:355:8"]]
- 00453338 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 00453338 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 00453338 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 00453338 ["COPY", "tmp:0:8", ["const:3e0:8"]]
+ 00453338 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 00453338 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 00453338 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 00453338 bytes 39570d91
+ 00453338 bytes 39830f91
- 0045333c ["COPY", "register:40a0:8", ["const:297000:8"]]
- 0045333c bytes 34f2ff90
+ 0045333c ["COPY", "register:40a0:8", ["const:297000:8"]]
+ 0045333c bytes 34f2ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad0b933ea775889497bee6e4719f8b5b"></a>

### [`0046a3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046a3a8.md) → [`0046a3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a3a8.md) FUN_0046a3a8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00829180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829180.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00829180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829180.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0046a3b4",
      "READ",
      [
        "storage",
        "00c24d88",
        null,
        "undefined4"
      ]
    ],
    [
      "0046a3bc",
      "READ",
      [
        "storage",
        "00c24d78",
        null,
        "undefined4"
      ]
    ],
    [
      "0046a3c8",
      "READ",
      [
        "storage",
        "00c24d8c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0046a3b4",
      "READ",
      [
        "storage",
        "00c24dc8",
        null,
        "undefined4"
      ]
    ],
    [
      "0046a3bc",
      "READ",
      [
        "storage",
        "00c24db8",
        null,
        "undefined4"
      ]
    ],
    [
      "0046a3c8",
      "READ",
      [
        "storage",
        "00c24dcc",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046a3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046a3a8.md#insn-0046a3ac) · [`0046a3b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046a3a8.md#insn-0046a3b8)
- 新版 [`0046a3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a3a8.md#insn-0046a3ac) · [`0046a3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a3a8.md#insn-0046a3b8)

~~~diff
- 0046a3ac ["COPY", "tmp:0:8", ["const:d70:8"]]
- 0046a3ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046a3ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046a3ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046a3ac ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 0046a3ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046a3ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046a3ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046a3ac bytes 08c13591
+ 0046a3ac bytes 08c13691
- 0046a3b8 ["INT_MULT", "tmp:0:4", ["register:4050:4", "register:4048:4"]]
- 0046a3b8 ["INT_ZEXT", "register:4048:8", ["tmp:0:4"]]
- 0046a3b8 bytes 497d091b
+ 0046a3b8 ["INT_MULT", "tmp:0:4", ["register:4050:4", "register:4048:4"]]
+ 0046a3b8 ["INT_ZEXT", "register:4048:8", ["tmp:0:4"]]
+ 0046a3b8 bytes 497d091b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f39cadb7d2b20473af44787eae993e72"></a>

### [`00470c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470c54.md) → [`00470c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470c54.md) FUN_00470c54

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00906b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md) · 呼出先 3件 [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb750.md) [`00bdb760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb760.md)
- 新版 呼出元 1件 [`00906b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906b9c.md) · 呼出先 3件 [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7a0.md) [`00bdb7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00470cf0",
      "PARAM",
      [
        "storage",
        "0029f37f",
        null,
        null
      ]
    ],
    [
      "00470cf8",
      "PARAM",
      [
        "storage",
        "00298cdd",
        null,
        null
      ]
    ],
    [
      "00470cf8",
      "PARAM",
      [
        "storage",
        "0029f37c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00470cf0",
      "PARAM",
      [
        "storage",
        "0029f40a",
        null,
        null
      ]
    ],
    [
      "00470cf8",
      "PARAM",
      [
        "storage",
        "00298c50",
        null,
        null
      ]
    ],
    [
      "00470cf8",
      "PARAM",
      [
        "storage",
        "0029f407",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00470cc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470c54.md#insn-00470cc8) · [`00470cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470c54.md#insn-00470cd8) · [`00470cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470c54.md#insn-00470cdc)
- 新版 [`00470cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470c54.md#insn-00470cc8) · [`00470cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470c54.md#insn-00470cd8)

~~~diff
- 00470cc8 ["COPY", "tmp:0:8", ["const:37c:8"]]
- 00470cc8 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00470cc8 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00470cc8 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00470cc8 ["COPY", "tmp:0:8", ["const:407:8"]]
+ 00470cc8 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00470cc8 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00470cc8 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00470cc8 bytes d6f20d91
+ 00470cc8 bytes d61e1091
- 00470cd8 ["COPY", "tmp:0:8", ["const:331:8"]]
- 00470cd8 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 00470cd8 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 00470cd8 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 00470cd8 ["COPY", "tmp:0:8", ["const:3bc:8"]]
+ 00470cd8 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 00470cd8 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 00470cd8 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 00470cd8 bytes 18c70c91
+ 00470cd8 bytes 18f30e91
- 00470cdc ["COPY", "register:40c8:8", ["const:29f000:8"]]
- 00470cdc bytes 79f1fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-122873c53a8ade35032c1ba07e00e818"></a>

### [`00474c0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474c0c.md) → [`00474c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474c0c.md) FUN_00474c0c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0060f9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060f9b8.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`0060f9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060f9b8.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call, call_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.31% / 新版 67.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00474c50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00474c58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00474c58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00474c40",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb040"
      ]
    ],
    [
      "unmatched:00474c50",
      "DATA",
      [
        "storage",
        "00be8f68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00474c88",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb040"
      ]
    ],
    [
      "00474c98",
      "DATA",
      [
        "storage",
        "00be9008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474c0c.md#insn-00474c40) · [`00474c50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474c0c.md#insn-00474c50) · [`00474c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474c0c.md#insn-00474c58)

~~~diff
- 00474c40 ["INT_ADD", "register:40f0:8", ["const:474c40:8", "const:4:8"]]
- 00474c40 ["CALL", null, ["callee:00bdb040:8"]]
- 00474c40 bytes ec981d94
- 00474c50 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00474c50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00474c50 bytes 080000f9
- 00474c58 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00474c58 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00474c58 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00474c58 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00474c58 bytes 1ffc00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19a9a60118c8d73ff286125affeeadf4"></a>

### [`0053980c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053980c.md) → [`0053980c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053980c.md) FUN_0053980c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0052e39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e39c.md) [`005385e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/005385e0.md) [`00a3b374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b374.md) · 呼出先 2件 [`005399b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005399b0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 3件 [`0052e39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e39c.md) [`005385e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005385e0.md) [`00a3b3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b3b8.md) · 呼出先 2件 [`005399b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005399b0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.29% / 新版 85.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00539840"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0053984c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00539840"
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
      "unmatched:00539840",
      "DATA",
      [
        "storage",
        "00bedef0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0053984c",
      "DATA",
      [
        "storage",
        "00bedea0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00539840",
      "DATA",
      [
        "storage",
        "00bedf40",
        null,
        "undefined *"
      ]
    ],
    [
      "0053984c",
      "DATA",
      [
        "storage",
        "00bedef0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053980c.md#insn-00539840) · [`0053984c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053980c.md#insn-0053984c)
- 新版 [`00539840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053980c.md#insn-00539840)

~~~diff
- 00539840 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00539840 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00539840 bytes 080000f9
+ 00539840 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00539840 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00539840 bytes 080000f9
- 0053984c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0053984c ["INT_ADD", "register:40c0:8", ["register:40c0:8", "const:18:8"]]
- 0053984c ["STORE", null, ["const:1b1:8", "register:40c0:8", "tmp:0:8"]]
- 0053984c bytes 088f01f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c07f37f099ac47084beccdf92c087b21"></a>

### [`005537fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005537fc.md) → [`005537fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005537fc.md) FUN_005537fc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052db28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db28.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0052db28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db28.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 11.11% / 新版 11.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00553804",
      "READ",
      [
        "storage",
        "00c1ad30",
        null,
        "pointer"
      ]
    ],
    [
      "00553808",
      "READ",
      [
        "storage",
        "00c1ad38",
        null,
        "pointer"
      ]
    ],
    [
      "0055380c",
      "READ",
      [
        "storage",
        "00c2655c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00553804",
      "READ",
      [
        "storage",
        "00c1ad80",
        null,
        "pointer"
      ]
    ],
    [
      "00553808",
      "READ",
      [
        "storage",
        "00c1ad88",
        null,
        "pointer"
      ]
    ],
    [
      "0055380c",
      "READ",
      [
        "storage",
        "00c2659c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005537fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005537fc.md#insn-005537fc) · [`00553800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005537fc.md#insn-00553800)
- 新版 [`005537fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005537fc.md#insn-005537fc)

~~~diff
- 005537fc ["COPY", "register:4040:8", ["const:c1a000:8"]]
- 005537fc bytes 283600f0
+ 005537fc ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005537fc bytes 283600f0
- 00553800 ["COPY", "register:4048:8", ["const:c1a000:8"]]
- 00553800 bytes 293600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-944df17291c336a97834f4f59f6e85a6"></a>

### [`00562188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/00562188.md) → [`00562188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562188.md) FUN_00562188

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`0056233c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/0056233c.md) [`00564d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564d7c.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0056233c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/0056233c.md) [`00564d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564d7c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.94% / 新版 96.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005621e8",
      "PARAM",
      [
        "storage",
        "00bef9c0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005621ec",
      "PARAM",
      [
        "storage",
        "00bef9d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005621e8",
      "PARAM",
      [
        "storage",
        "00befa10",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005621ec",
      "PARAM",
      [
        "storage",
        "00befa20",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005621c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/00562188.md#insn-005621c0) · [`005621c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/00562188.md#insn-005621c8)
- 新版 [`005621c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562188.md#insn-005621c0) · [`005621c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562188.md#insn-005621c8)

~~~diff
- 005621c0 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 005621c0 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 005621c0 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 005621c0 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 005621c0 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005621c0 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 005621c0 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 005621c0 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 005621c0 bytes 94022791
+ 005621c0 bytes 94422891
- 005621c8 ["COPY", "register:40a8:8", ["const:bef000:8"]]
- 005621c8 bytes 753400b0
+ 005621c8 ["COPY", "register:40a8:8", ["const:bef000:8"]]
+ 005621c8 bytes 753400b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a766633206e4e9149958681653f7b93"></a>

### [`0056b688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056b688.md) → [`0056b688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b688.md) FUN_0056b688

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566968.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.03% / 新版 97.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0056b704",
      "READ",
      [
        "storage",
        "00299e4b",
        null,
        "string"
      ]
    ],
    [
      "0056b704",
      "READ",
      [
        "storage",
        "00299e5b",
        null,
        "string"
      ]
    ],
    [
      "0056b718",
      "READ",
      [
        "storage",
        "00299e6b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056b704",
      "READ",
      [
        "storage",
        "00299e49",
        null,
        "string"
      ]
    ],
    [
      "0056b704",
      "READ",
      [
        "storage",
        "00299e59",
        null,
        "string"
      ]
    ],
    [
      "0056b718",
      "READ",
      [
        "storage",
        "00299e69",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056b688.md#insn-0056b6fc) · [`0056b700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056b688.md#insn-0056b700)
- 新版 [`0056b6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b688.md#insn-0056b6fc) · [`0056b700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b688.md#insn-0056b700)

~~~diff
- 0056b6fc ["COPY", "tmp:0:8", ["const:e4b:8"]]
- 0056b6fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056b6fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056b6fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056b6fc ["COPY", "tmp:0:8", ["const:e49:8"]]
+ 0056b6fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b6fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b6fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056b6fc bytes 082d3991
+ 0056b6fc bytes 08253991
- 0056b700 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0056b700 bytes 29eaffb0
+ 0056b700 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0056b700 bytes 29eaffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83cd1f1fa25ac5d9764a5db6fc287164"></a>

### [`005bc0ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bc0ac.md) → [`005bc0ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc0ac.md) FUN_005bc0ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`006f5fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f5/006f5fe8.md) [`006f8ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f8/006f8ac0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006f5fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f5/006f5fe8.md) [`006f8ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f8/006f8ac0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 76.27% / 新版 76.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005bc0d0",
      "DATA",
      [
        "storage",
        "0109c602",
        null,
        "undefined4"
      ]
    ],
    [
      "005bc0d4",
      "DATA",
      [
        "storage",
        "0109c605",
        null,
        "undefined1"
      ]
    ],
    [
      "005bc0d8",
      "DATA",
      [
        "storage",
        "0109c604",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "005bc0d0",
      "DATA",
      [
        "storage",
        "0109c642",
        null,
        "undefined4"
      ]
    ],
    [
      "005bc0d4",
      "DATA",
      [
        "storage",
        "0109c645",
        null,
        "undefined1"
      ]
    ],
    [
      "005bc0d8",
      "DATA",
      [
        "storage",
        "0109c644",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bc0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bc0ac.md#insn-005bc0c8) · [`005bc0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bc0ac.md#insn-005bc0e0)
- 新版 [`005bc0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc0ac.md#insn-005bc0c8) · [`005bc0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc0ac.md#insn-005bc0e0)

~~~diff
- 005bc0c8 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005bc0c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005bc0c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005bc0c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005bc0c8 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 005bc0c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005bc0c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005bc0c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005bc0c8 bytes 08011891
+ 005bc0c8 bytes 08011991
- 005bc0e0 ["INT_XOR", "tmp:0:4", ["register:4050:4", "register:4048:4"]]
- 005bc0e0 ["INT_ZEXT", "register:4048:8", ["tmp:0:4"]]
- 005bc0e0 bytes 4901094a
+ 005bc0e0 ["INT_XOR", "tmp:0:4", ["register:4050:4", "register:4048:4"]]
+ 005bc0e0 ["INT_ZEXT", "register:4048:8", ["tmp:0:4"]]
+ 005bc0e0 bytes 4901094a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76eb2481a42a07c025c63c456e357cd2"></a>

### [`005c2f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2f88.md) → [`005c2f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2f88.md) FUN_005c2f88

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`005c2ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2ec0.md) [`005c2f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2f30.md) [`005c3330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c3/005c3330.md) [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) [`009f4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f4/009f4a74.md) · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`005bce08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bce08.md) [`0063e4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e4a8.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`009019f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/009019f4.md)
- 新版 呼出元 5件 [`005c2ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2ec0.md) [`005c2f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2f30.md) [`005c3330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c3/005c3330.md) [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`009f4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f4ab8.md) · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`005bce08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bce08.md) [`0063e4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e4a8.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`009019f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/009019f4.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.79% / 新版 97.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005c3030",
      "READ",
      [
        "storage",
        "002a170d",
        null,
        "string"
      ]
    ],
    [
      "005c3030",
      "READ",
      [
        "storage",
        "002a171d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005c3030",
      "READ",
      [
        "storage",
        "002a1798",
        null,
        "string"
      ]
    ],
    [
      "005c3030",
      "READ",
      [
        "storage",
        "002a17a8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c3028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2f88.md#insn-005c3028) · [`005c302c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2f88.md#insn-005c302c)
- 新版 [`005c3028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2f88.md#insn-005c3028) · [`005c302c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2f88.md#insn-005c302c)

~~~diff
- 005c3028 ["COPY", "tmp:0:8", ["const:70d:8"]]
- 005c3028 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005c3028 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005c3028 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005c3028 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 005c3028 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005c3028 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005c3028 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005c3028 bytes 4a351c91
+ 005c3028 bytes 4a611e91
- 005c302c ["COPY", "register:4040:8", ["const:2b1000:8"]]
- 005c302c bytes 68e7ffd0
+ 005c302c ["COPY", "register:4040:8", ["const:2b1000:8"]]
+ 005c302c bytes 68e7ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-255214537c5681cba12b203a91cbc88f"></a>

### [`005c8a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c8/005c8a6c.md) → [`005c8a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c8/005c8a6c.md) FUN_005c8a6c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`005c8548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c8/005c8548.md) [`005cb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cb/005cb0e0.md) [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) · 呼出先 4件 [`009019f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/009019f4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 4件 [`005c8548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c8/005c8548.md) [`005cb0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cb/005cb0e0.md) [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 4件 [`009019f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/009019f4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.94% / 新版 94.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005c8b14",
      "READ",
      [
        "storage",
        "002a7683",
        null,
        "string"
      ]
    ],
    [
      "005c8b78",
      "READ",
      [
        "storage",
        "00c24070",
        null,
        "undefined4"
      ]
    ],
    [
      "005c8b9c",
      "READ",
      [
        "storage",
        "00296d04",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005c8b14",
      "READ",
      [
        "storage",
        "002a771d",
        null,
        "string"
      ]
    ],
    [
      "005c8b78",
      "READ",
      [
        "storage",
        "00c240c0",
        null,
        "undefined4"
      ]
    ],
    [
      "005c8b9c",
      "READ",
      [
        "storage",
        "00296c77",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c8b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c8/005c8a6c.md#insn-005c8b00) · [`005c8b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c8/005c8a6c.md#insn-005c8b68) · [`005c8b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c8/005c8a6c.md#insn-005c8b94)
- 新版 [`005c8b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c8/005c8a6c.md#insn-005c8b00) · [`005c8b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c8/005c8a6c.md#insn-005c8b68) · [`005c8b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c8/005c8a6c.md#insn-005c8b94)

~~~diff
- 005c8b00 ["COPY", "tmp:0:8", ["const:683:8"]]
- 005c8b00 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005c8b00 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005c8b00 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005c8b00 ["COPY", "tmp:0:8", ["const:71d:8"]]
+ 005c8b00 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005c8b00 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005c8b00 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005c8b00 bytes 4a0d1a91
+ 005c8b00 bytes 4a751c91
- 005c8b68 ["COPY", "tmp:0:8", ["const:70:8"]]
- 005c8b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005c8b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005c8b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005c8b68 ["COPY", "tmp:0:8", ["const:c0:8"]]
+ 005c8b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005c8b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005c8b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005c8b68 bytes 08c10191
+ 005c8b68 bytes 08010391
- 005c8b94 ["COPY", "tmp:0:8", ["const:d04:8"]]
- 005c8b94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005c8b94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005c8b94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005c8b94 ["COPY", "tmp:0:8", ["const:c77:8"]]
+ 005c8b94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005c8b94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005c8b94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005c8b94 bytes 08113491
+ 005c8b94 bytes 08dd3191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6164e22621452405e863a4cde2a3912"></a>

### [`005d18a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d1/005d18a4.md) → [`005d18a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d1/005d18a4.md) FUN_005d18a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005d0a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d0/005d0a68.md) · 呼出先 10件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0058c05c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058c/0058c05c.md) [`005c2d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2d18.md)
- 新版 呼出元 1件 [`005d0a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d0/005d0a68.md) · 呼出先 10件 [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0058c05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058c05c.md) [`005c2d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2d18.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.28% / 新版 97.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d19b0",
      "READ",
      [
        "storage",
        "00296d04",
        null,
        "string"
      ]
    ],
    [
      "005d19b4",
      "READ",
      [
        "storage",
        "00296d13",
        null,
        "string"
      ]
    ],
    [
      "005d1a14",
      "READ",
      [
        "storage",
        "00c1b668",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d19b0",
      "READ",
      [
        "storage",
        "00296c77",
        null,
        "string"
      ]
    ],
    [
      "005d19b4",
      "READ",
      [
        "storage",
        "00296c86",
        null,
        "string"
      ]
    ],
    [
      "005d1a14",
      "READ",
      [
        "storage",
        "00c1b6b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d19a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d1/005d18a4.md#insn-005d19a8) · [`005d19ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d1/005d18a4.md#insn-005d19ac)
- 新版 [`005d19a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d1/005d18a4.md#insn-005d19a8) · [`005d19ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d1/005d18a4.md#insn-005d19ac)

~~~diff
- 005d19a8 ["COPY", "tmp:0:8", ["const:d04:8"]]
- 005d19a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005d19a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005d19a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005d19a8 ["COPY", "tmp:0:8", ["const:c77:8"]]
+ 005d19a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005d19a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005d19a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005d19a8 bytes 08113491
+ 005d19a8 bytes 08dd3191
- 005d19ac ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 005d19ac bytes e9e6fff0
+ 005d19ac ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 005d19ac bytes e9e6fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2d2e7bcad2beb080df7b0f467a64af7"></a>

### [`006f4518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f4/006f4518.md) → [`006f4518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f4518.md) FUN_006f4518

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006f3154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f3/006f3154.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00670f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670f08.md) [`00adc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc050.md) [`00adc0dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc0dc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`006f3154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f3154.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00670f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670f08.md) [`00adc094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc094.md) [`00adc120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc120.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.86% / 新版 93.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006f45e8",
      "PARAM",
      [
        "storage",
        "00294cef",
        null,
        "string"
      ]
    ],
    [
      "006f45e8",
      "PARAM",
      [
        "storage",
        "00293c5a",
        null,
        "string"
      ]
    ],
    [
      "006f45e8",
      "PARAM",
      [
        "storage",
        "002aedf6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006f45e8",
      "PARAM",
      [
        "storage",
        "00294c62",
        null,
        "string"
      ]
    ],
    [
      "006f45e8",
      "PARAM",
      [
        "storage",
        "00293bcd",
        null,
        "string"
      ]
    ],
    [
      "006f45e8",
      "PARAM",
      [
        "storage",
        "002aed62",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006f45b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f4/006f4518.md#insn-006f45b8) · [`006f45c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f4/006f4518.md#insn-006f45c8) · [`006f45dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f4/006f4518.md#insn-006f45dc)
- 新版 [`006f45b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f4518.md#insn-006f45b8) · [`006f45c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f4518.md#insn-006f45c8)

~~~diff
- 006f45b8 ["COPY", "tmp:0:8", ["const:cef:8"]]
- 006f45b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 006f45b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 006f45b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006f45b8 ["COPY", "tmp:0:8", ["const:c62:8"]]
+ 006f45b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006f45b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006f45b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 006f45b8 bytes 4abd3391
+ 006f45b8 bytes 4a893191
- 006f45c8 ["COPY", "tmp:0:8", ["const:df6:8"]]
- 006f45c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006f45c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006f45c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006f45c8 ["COPY", "tmp:0:8", ["const:d62:8"]]
+ 006f45c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006f45c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006f45c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006f45c8 bytes 08d93791
+ 006f45c8 bytes 08893591
- 006f45dc ["COPY", "register:4048:8", ["const:293000:8"]]
- 006f45dc bytes e9dcfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-321a6891c16ed4b0e8caed8307aaad33"></a>

### [`007cfd34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfd34.md) → [`007cfd34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfd34.md) FUN_007cfd34

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e0/005e02b0.md) [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`0099697c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00996/0099697c.md) [`009969b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00996/009969b8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 6件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e0/005e02b0.md) [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0099697c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/0099697c.md) [`009969b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/009969b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call, call_count, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.68% / 新版 95.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "007cfdfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "007cfdfc"
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
      "007cfdf4",
      "READ",
      [
        "storage",
        "00c1b788",
        null,
        "pointer"
      ]
    ],
    [
      "007cfdf8",
      "DATA",
      [
        "storage",
        "00c245dc",
        null,
        null
      ]
    ],
    [
      "unmatched:007cfdfc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0081f580"
      ]
    ]
  ],
  "added": [
    [
      "007cfdf4",
      "READ",
      [
        "storage",
        "00c1b7d8",
        null,
        "pointer"
      ]
    ],
    [
      "007cfdf8",
      "DATA",
      [
        "storage",
        "00c2462c",
        null,
        null
      ]
    ],
    [
      "007cfdfc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0081f580"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cfdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfd34.md#insn-007cfdfc) · [`007cfdf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfd34.md#insn-007cfdf4)
- 新版 [`007cfdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfd34.md#insn-007cfdfc) · [`007cfdf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfd34.md#insn-007cfdf4)

~~~diff
- 007cfdfc ["INT_ADD", "register:40f0:8", ["const:7cfdfc:8", "const:4:8"]]
- 007cfdfc ["CALL", null, ["callee:0081f580:8"]]
- 007cfdfc bytes e13d0194
+ 007cfdfc ["INT_ADD", "register:40f0:8", ["const:7cfdfc:8", "const:4:8"]]
+ 007cfdfc ["CALL", null, ["callee:0081f580:8"]]
+ 007cfdfc bytes e13d0194
- 007cfdf4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:788:8"]]
- 007cfdf4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 007cfdf4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7d8:8"]]
+ 007cfdf4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 007cfdf4 bytes 29c543f9
+ 007cfdf4 bytes 29ed43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cce5c617b23fe97ffc5dc1bb864413c"></a>

### [`007d1164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d1/007d1164.md) → [`007d1164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d1/007d1164.md) FUN_007d1164

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0075f8cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075f/0075f8cc.md) [`00a3e5b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3e/00a3e5b4.md) · 呼出先 3件 [`007cd2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd2ac.md) [`007d0e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d0/007d0e6c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`0075f8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md) [`00a3e5f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3e/00a3e5f8.md) · 呼出先 3件 [`007cd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd2ac.md) [`007d0e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d0/007d0e6c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007d12c0",
      "READ",
      [
        "storage",
        "00c28058",
        null,
        "undefined8"
      ]
    ],
    [
      "007d12c0",
      "READ",
      [
        "storage",
        "00c28060",
        null,
        "undefined8"
      ]
    ],
    [
      "007d1310",
      "READ",
      [
        "storage",
        "00c28070",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "007d12c0",
      "READ",
      [
        "storage",
        "00c28098",
        null,
        "undefined8"
      ]
    ],
    [
      "007d12c0",
      "READ",
      [
        "storage",
        "00c280a0",
        null,
        "undefined8"
      ]
    ],
    [
      "007d1310",
      "READ",
      [
        "storage",
        "00c280b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007d11bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d1/007d1164.md#insn-007d11bc) · [`007d11c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d1/007d1164.md#insn-007d11c0)
- 新版 [`007d11bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d1/007d1164.md#insn-007d11bc) · [`007d11c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d1/007d1164.md#insn-007d11c0)

~~~diff
- 007d11bc ["COPY", "tmp:0:8", ["const:58:8"]]
- 007d11bc ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 007d11bc ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 007d11bc ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 007d11bc ["COPY", "tmp:0:8", ["const:98:8"]]
+ 007d11bc ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 007d11bc ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 007d11bc ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 007d11bc bytes f7620191
+ 007d11bc bytes f7620291
- 007d11c0 ["COPY", "register:40c0:8", ["const:1:8"]]
- 007d11c0 bytes 38008052
+ 007d11c0 ["COPY", "register:40c0:8", ["const:1:8"]]
+ 007d11c0 bytes 38008052
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c7fc24425c6af43afbbc7221c855384"></a>

### [`0087308c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/0087308c.md) → [`0087308c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/0087308c.md) FUN_0087308c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0051d884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d884.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md) [`0051d884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d884.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.85% / 新版 94.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00873130",
      "PARAM",
      [
        "storage",
        "0029fc00",
        null,
        "string"
      ]
    ],
    [
      "00873130",
      "PARAM",
      [
        "storage",
        "0029506b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00873130",
      "PARAM",
      [
        "storage",
        "0029fc8b",
        null,
        "string"
      ]
    ],
    [
      "00873130",
      "PARAM",
      [
        "storage",
        "00294fde",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087311c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/0087308c.md#insn-0087311c) · [`00873120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/0087308c.md#insn-00873120)
- 新版 [`0087311c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/0087308c.md#insn-0087311c) · [`00873120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/0087308c.md#insn-00873120)

~~~diff
- 0087311c ["COPY", "tmp:0:8", ["const:c00:8"]]
- 0087311c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087311c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087311c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087311c ["COPY", "tmp:0:8", ["const:c8b:8"]]
+ 0087311c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087311c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087311c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087311c bytes 08013091
+ 0087311c bytes 082d3291
- 00873120 ["COPY", "register:4048:8", ["const:295000:8"]]
- 00873120 bytes 09d1ffd0
+ 00873120 ["COPY", "register:4048:8", ["const:294000:8"]]
+ 00873120 bytes 09d1ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa6c87b3c8f2809f540b5f227727324d"></a>

### [`009d5268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d5268.md) → [`009d52ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d52ac.md) FUN_009d52ac

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00644b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00644/00644b38.md) · 呼出先 2件 [`006ef68c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ef/006ef68c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00644b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00644/00644b38.md) · 呼出先 2件 [`006ef68c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ef/006ef68c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 98.15% / 新版 98.15%

CFGの説明率　旧版 61.54% / 新版 64.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "009d5338"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "009d537c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`009d5338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d5268.md#insn-009d5338) · [`009d5288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d5268.md#insn-009d5288)
- 新版 [`009d537c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d52ac.md#insn-009d537c) · [`009d52cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d52ac.md#insn-009d52cc)

~~~diff
- 009d5338 ["COPY", "register:0:8", ["register:40f0:8"]]
- 009d5338 ["RETURN", null, ["register:0:8"]]
- 009d5338 bytes c0035fd6
+ 009d537c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 009d537c ["RETURN", null, ["register:0:8"]]
+ 009d537c bytes c0035fd6
- 009d5288 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 009d5288 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 009d52cc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 009d52cc ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 009d5288 bytes 880400b4
+ 009d52cc bytes 880400b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-420af0257af81e4bdd156673cb64cf28"></a>

### [`009d53c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d53c8.md) → [`009d540c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d540c.md) FUN_009d540c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.19% / 新版 74.19%

CFGの説明率　旧版 70.21% / 新版 70.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d53d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d53d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d53dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009d53d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:009d53dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009d53e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009d541c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "009d5420",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009d5424",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009d53d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d53c8.md#insn-009d53d8) · [`009d53dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d53c8.md#insn-009d53dc) · [`009d53e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d53c8.md#insn-009d53e0)

~~~diff
- 009d53d8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 009d53d8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 009d53d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1b0:8"]]
- 009d53d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009d53d8 bytes f85f1ba9
- 009d53dc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 009d53dc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 009d53dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1c0:8"]]
- 009d53dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009d53dc bytes f6571ca9
- 009d53e0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 009d53e0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 009d53e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1d0:8"]]
- 009d53e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009d53e0 bytes f44f1da9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-743455f3b029412b95ea7b8b09507799"></a>

### [`009d58cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d58cc.md) → [`009d5910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d5910.md) FUN_009d5910

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 12件 [`006989b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00698/006989b8.md) [`00749514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00749/00749514.md) [`0079a4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079a/0079a4e4.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfaa0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5b0.md)
- 新版 呼出元 12件 [`006989b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00698/006989b8.md) [`00749514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/00749514.md) [`0079a4e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079a/0079a4e4.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`007cf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfaa0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 96.05% / 新版 96.05%

CFGの説明率　旧版 93.94% / 新版 87.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d5c28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d5c40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009d5c6c"
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
      "009d5c68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:009d5c30"
      ]
    ],
    [
      "unmatched:009d5c34",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00419064"
      ]
    ],
    [
      "unmatched:009d5c58",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "009d5c1c"
      ]
    ]
  ],
  "added": [
    [
      "009d5c68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009d5c74"
      ]
    ],
    [
      "009d5c78",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00419064"
      ]
    ],
    [
      "009d5c9c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "009d5c1c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009d5c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d58cc.md#insn-009d5c28) · [`009d5c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d58cc.md#insn-009d5c34) · [`009d5c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d58cc.md#insn-009d5c40)

~~~diff
- 009d5c28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:18:8"]]
- 009d5c28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009d5c28 bytes 680e00f9
- 009d5c34 ["INT_ADD", "register:40f0:8", ["const:9d5c34:8", "const:4:8"]]
- 009d5c34 ["CALL", null, ["callee:00419064:8"]]
- 009d5c34 bytes 0c0de997
- 009d5c40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:28:8"]]
- 009d5c40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009d5c40 bytes 681600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b9715e1c20f7de39c4c4333be805bbc"></a>

### [`009d5c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d5c5c.md) → [`009d5ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d5ca0.md) FUN_009d5ca0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) · 呼出先 1件 [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md)
- 新版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 1件 [`007cf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf950.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 37.93% / 新版 37.93%

CFGの説明率　旧版 4.00% / 新版 3.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d5c5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d5c5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d5c60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009d5c5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009d5c60",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009d5c70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009d5cc4"
      ]
    ]
  ],
  "added": [
    [
      "009d5ca0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009d5ca4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009d5cb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009d5cc4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009d5c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d5c5c.md#insn-009d5c5c) · [`009d5c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d5c5c.md#insn-009d5c60) · [`009d5c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d5c5c.md#insn-009d5c70)

~~~diff
- 009d5c5c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009d5c5c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009d5c5c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009d5c5c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009d5c5c bytes fd7bbea9
- 009d5c60 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009d5c60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 009d5c60 bytes f30b00f9
- 009d5c70 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 009d5c70 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a7ede52c7ac103aee681c64a2197b8a"></a>

### [`009d5cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d5cd0.md) → [`009d5d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d5d14.md) FUN_009d5d14

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005ec96c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ec/005ec96c.md) [`007bda04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bda04.md) [`008ff4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff4a8.md) [`009eadc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009ea/009eadc8.md) · 呼出先 1件 [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md)
- 新版 呼出元 7件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005ec96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ec/005ec96c.md) [`007bda04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bd/007bda04.md) [`008ff4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff4a8.md) [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) · 呼出先 1件 [`007cf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf950.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 28.57% / 新版 42.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d5cd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d5cd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d5cd4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009d5cd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009d5cd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009d5cf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009d5d8c"
      ]
    ]
  ],
  "added": [
    [
      "009d5d14",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009d5d18",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009d5d34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009d5d8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009d5cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d5cd0.md#insn-009d5cd0) · [`009d5cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d5cd0.md#insn-009d5cd4) · [`009d5cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d5cd0.md#insn-009d5cf0)

~~~diff
- 009d5cd0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009d5cd0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009d5cd0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009d5cd0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009d5cd0 bytes fd7bbea9
- 009d5cd4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009d5cd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 009d5cd4 bytes f30b00f9
- 009d5cf0 ["CBRANCH", null, ["local:b20:8", "register:101:1"]]
- 009d5cf0 bytes c0020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-047c63535c523081093a04988cf9a4ed"></a>

### [`009d5d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d5d60.md) → [`009d5da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d5da4.md) FUN_009d5da4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`0079a4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079a/0079a4e4.md) [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) [`007bd4d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bd4d8.md) [`007cfb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfb70.md) [`009a3a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a3/009a3a30.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 8件 [`0079a4e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079a/0079a4e4.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) [`007bd4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bd/007bd4d8.md) [`007cfb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfb70.md) [`009a3a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a3/009a3a30.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.06% / 新版 92.06%

CFGの説明率　旧版 44.83% / 新版 43.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009d5d88"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009d5d94"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009d5dc4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009d5dc4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:009d5d8c"
      ]
    ],
    [
      "unmatched:009d5d88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009d5e1c"
      ]
    ],
    [
      "unmatched:009d5d94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009d5dc8"
      ]
    ]
  ],
  "added": [
    [
      "009d5dc4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "009d5dd0"
      ]
    ],
    [
      "009d5dcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009d5e1c"
      ]
    ],
    [
      "009d5dd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009d5dc8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009d5d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d5d60.md#insn-009d5d80) · [`009d5d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d5d60.md#insn-009d5d88) · [`009d5d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d5/009d5d60.md#insn-009d5d94)
- 新版 [`009d5dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d5da4.md#insn-009d5dc4)

~~~diff
- 009d5d80 ["BRANCH", null, ["local:b4:8"]]
+ 009d5dc4 ["BRANCH", null, ["local:b3:8"]]
- 009d5d80 bytes 03000014
+ 009d5dc4 bytes 03000014
- 009d5d88 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 009d5d88 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 009d5d88 bytes 890200b4
- 009d5d94 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 009d5d94 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 009d5d94 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 009d5d94 ["CBRANCH", null, ["local:b2:8", "tmp:2:1"]]
- 009d5d94 bytes 8cffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fe2c705fa42369641fd7f50b9cb7663"></a>

### [`009d6ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d6/009d6ae4.md) → [`009d6b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d6/009d6b28.md) FUN_009d6b28

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 12件 [`00606588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00606/00606588.md) [`0067417c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00674/0067417c.md) [`00708bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00708/00708bb8.md) [`0071b744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071b/0071b744.md) [`0071d1f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071d/0071d1f4.md) · 呼出先 3件 [`005748a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/005748a0.md) [`00574bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574bb4.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 12件 [`00606588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00606/00606588.md) [`0067417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067417c.md) [`00708bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00708/00708bb8.md) [`0071b744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071b/0071b744.md) [`0071d1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071d1f4.md) · 呼出先 3件 [`005748a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/005748a0.md) [`00574bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574bb4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 73.08% / 新版 73.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d6ae8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d6ae8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d6aec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009d6ae8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009d6aec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009d6b04",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009d6b2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009d6b30",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009d6b48",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009d6ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d6/009d6ae4.md#insn-009d6ae8) · [`009d6aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d6/009d6ae4.md#insn-009d6aec) · [`009d6b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d6/009d6ae4.md#insn-009d6b04)

~~~diff
- 009d6ae8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009d6ae8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009d6ae8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 009d6ae8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009d6ae8 bytes fd7b05a9
- 009d6aec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 009d6aec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 009d6aec bytes f33300f9
- 009d6b04 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009d6b04 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009d6b04 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009d6b04 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acfd5a900102035758f00128b90749a1"></a>

### [`009d6e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d6/009d6e44.md) → [`009d6e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d6/009d6e88.md) FUN_009d6e88

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`009d845c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d8/009d845c.md) [`009d8fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d8/009d8fe4.md) [`009d99e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d9/009d99e0.md) · 呼出先 4件 [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`009d6b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d6/009d6b74.md) [`009dbd20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009db/009dbd20.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 3件 [`009d84a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d8/009d84a0.md) [`009d9028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d9/009d9028.md) [`009d9a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d9/009d9a24.md) · 呼出先 4件 [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`009d6bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d6/009d6bb8.md) [`009dbd64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009db/009dbd64.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.01% / 新版 97.01%

CFGの説明率　旧版 51.35% / 新版 52.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009d6ff0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009d703c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009d7034"
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
      "unmatched:009d6ff0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009d705c"
      ]
    ],
    [
      "unmatched:009d703c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009d7090"
      ]
    ]
  ],
  "added": [
    [
      "009d7034",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009d705c"
      ]
    ],
    [
      "009d7080",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009d7090"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009d6ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d6/009d6e44.md#insn-009d6ff0) · [`009d6ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d6/009d6e44.md#insn-009d6ff8) · [`009d7034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d6/009d6e44.md#insn-009d7034)
- 新版 [`009d703c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d6/009d6e88.md#insn-009d703c)

~~~diff
- 009d6ff0 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 009d6ff0 bytes 40010054
- 009d6ff8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 009d6ff8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 009d703c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 009d703c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 009d6ff8 bytes 600000b4
+ 009d703c bytes 600000b4
- 009d7034 ["INT_SEXT", "register:4040:8", ["register:40a8:4"]]
- 009d7034 bytes a87e4093
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-941b1f998a4ee17600b4ea4e78a07316"></a>

### [`009d8a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d8/009d8a6c.md) → [`009d8ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d8/009d8ab0.md) FUN_009d8ab0

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0099dc74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0099d/0099dc74.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0044a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0099dc74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099d/0099dc74.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.80% / 新版 90.80%

CFGの説明率　旧版 75.51% / 新版 72.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d8aa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d8abc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d8ac0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009d8aa0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:009d8aa4",
      "READ",
      [
        "storage",
        "0109eb58",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:009d8ab0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009d8b0c"
      ]
    ]
  ],
  "added": [
    [
      "009d8ae4",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "009d8ae8",
      "READ",
      [
        "storage",
        "0109eb98",
        null,
        "undefined8"
      ]
    ],
    [
      "009d8af4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009d8b0c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009d8aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d8/009d8a6c.md#insn-009d8aa0) · [`009d8ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d8/009d8a6c.md#insn-009d8ab0) · [`009d8abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d8/009d8a6c.md#insn-009d8abc)

~~~diff
- 009d8aa0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 009d8aa0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009d8aa0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009d8aa0 bytes a9831ff8
- 009d8ab0 ["INT_RIGHT", "tmp:0:4", ["register:4058:4", "const:0:4"]]
- 009d8ab0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 009d8ab0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 009d8ab0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 009d8ab0 bytes cb000037
- 009d8abc ["COPY", "tmp:0:8", ["register:8:8"]]
- 009d8abc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 009d8abc bytes e003803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56b6a5ac9666178285b9062f39832bfa"></a>

### [`009d9f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d9/009d9f2c.md) → [`009d9f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d9/009d9f70.md) FUN_009d9f70

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`00606588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00606/00606588.md) [`006fb324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fb/006fb324.md) [`0070b570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070b/0070b570.md) [`0070ba4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070b/0070ba4c.md) [`0070f364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070f/0070f364.md) · 呼出先 8件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`006fd890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fd890.md) [`006fdbdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fdbdc.md) [`006fdd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fdd28.md) [`006fde74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fde74.md)
- 新版 呼出元 10件 [`00606588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00606/00606588.md) [`006fb324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fb/006fb324.md) [`0070b570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070b/0070b570.md) [`0070ba4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070b/0070ba4c.md) [`0070f364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070f/0070f364.md) · 呼出先 8件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`006fd890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd890.md) [`006fdbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdbdc.md) [`006fdd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdd28.md) [`006fde74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fde74.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 58.28% / 新版 58.28%

CFGの説明率　旧版 33.83% / 新版 33.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 33件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 44件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d9f44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d9f44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d9f48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009d9f44",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009d9f48",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009d9f64",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0081f580"
      ]
    ]
  ],
  "added": [
    [
      "009d9f88",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009d9f8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009d9fb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009da0b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009d9f44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d9/009d9f2c.md#insn-009d9f44) · [`009d9f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d9/009d9f2c.md#insn-009d9f48) · [`009d9ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d9/009d9f2c.md#insn-009d9ff8)

~~~diff
- 009d9f44 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 009d9f44 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 009d9f44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 009d9f44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009d9f44 bytes f65707a9
- 009d9f48 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 009d9f48 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 009d9f48 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 009d9f48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009d9f48 bytes f44f08a9
- 009d9ff8 ["COPY", "tmp:0:8", ["const:0:8"]]
- 009d9ff8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 009d9ff8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 009d9ff8 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 009d9ff8 bytes 1ffc02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c5060b40821e4621d8c8a3a071aa4cc"></a>

### [`009dbf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009db/009dbf40.md) → [`009dbf84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009db/009dbf84.md) FUN_009dbf84

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009dbd20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009db/009dbd20.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`009dbd64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009db/009dbd64.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.14% / 新版 85.14%

CFGの説明率　旧版 47.06% / 新版 47.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009dbf40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009dbf40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009dbf44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009dbf40",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:009dbf44",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:009dbf48",
      "WRITE",
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
      "009dbf84",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "009dbf88",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "009dbf8c",
      "WRITE",
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

- 旧版 [`009dbf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009db/009dbf40.md#insn-009dbf40) · [`009dbf44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009db/009dbf40.md#insn-009dbf44) · [`009dbf48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009db/009dbf40.md#insn-009dbf48)

~~~diff
- 009dbf40 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009dbf40 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009dbf40 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 009dbf40 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009dbf40 bytes fd7bbca9
- 009dbf44 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009dbf44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 009dbf44 bytes f70b00f9
- 009dbf48 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 009dbf48 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 009dbf48 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 009dbf48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009dbf48 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8b4b4dab05935534f9aa966c6d16b4f"></a>

### [`009dca10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dca10.md) → [`009dca54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dca54.md) FUN_009dca54

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`009dcbe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dcbe4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`009dcc28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dcc28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "009dca44"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "009dca88"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`009dca44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dca10.md#insn-009dca44) · [`009dca24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dca10.md#insn-009dca24)
- 新版 [`009dca88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dca54.md#insn-009dca88) · [`009dca68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dca54.md#insn-009dca68)

~~~diff
- 009dca44 ["COPY", "register:0:8", ["register:40f0:8"]]
- 009dca44 ["RETURN", null, ["register:0:8"]]
- 009dca44 bytes c0035fd6
+ 009dca88 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 009dca88 ["RETURN", null, ["register:0:8"]]
+ 009dca88 bytes c0035fd6
- 009dca24 ["INT_ADD", "register:40f0:8", ["const:9dca24:8", "const:4:8"]]
- 009dca24 ["CALL", null, ["callee:009dcc28:8"]]
+ 009dca68 ["INT_ADD", "register:40f0:8", ["const:9dca68:8", "const:4:8"]]
+ 009dca68 ["CALL", null, ["callee:009dcc28:8"]]
- 009dca24 bytes 70000094
+ 009dca68 bytes 70000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d9e640cb1349541afe3ad5dbd1db4a7"></a>

### [`009dca48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dca48.md) → [`009dca8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dca8c.md) FUN_009dca8c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009dc708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dc708.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`009dc74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dc74c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009dca48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009dca48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009dca8c"
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
      "unmatched:009dca48",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009dca54",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ],
    [
      "unmatched:009dca58",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "009dca8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009dca98",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "009dca9c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00418c38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009dca48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dca48.md#insn-009dca48) · [`009dca58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dca48.md#insn-009dca58)
- 新版 [`009dca8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dca8c.md#insn-009dca8c)

~~~diff
- 009dca48 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009dca48 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009dca48 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 009dca48 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009dca48 bytes fd7bbfa9
- 009dca58 ["INT_ADD", "register:40f0:8", ["const:9dca58:8", "const:4:8"]]
- 009dca58 ["CALL", null, ["callee:00418c38:8"]]
- 009dca58 bytes 78f0e897
+ 009dca8c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 009dca8c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 009dca8c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 009dca8c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 009dca8c bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f128cacbc9f3fcabc16c9aa2de1b1ef0"></a>

### [`009dca5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dca5c.md) → [`009dcaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dcaa0.md) FUN_009dcaa0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009dc898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dc898.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`009dc8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dc8dc.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 40.74% / 新版 42.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009dcabc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009dcacc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009dcb00"
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
      "unmatched:009dcabc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009dcb14"
      ]
    ],
    [
      "unmatched:009dcacc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009dcac4"
      ]
    ],
    [
      "009dcb28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:009dcac4"
      ]
    ]
  ],
  "added": [
    [
      "009dcb00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009dcb14"
      ]
    ],
    [
      "009dcb10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009dcac4"
      ]
    ],
    [
      "009dcb28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009dcb08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009dca88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dca5c.md#insn-009dca88) · [`009dcabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dca5c.md#insn-009dcabc) · [`009dcacc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dca5c.md#insn-009dcacc)
- 新版 [`009dcacc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dcaa0.md#insn-009dcacc)

~~~diff
- 009dca88 ["INT_ADD", "register:40f0:8", ["const:9dca88:8", "const:4:8"]]
- 009dca88 ["CALL", null, ["callee:00bdb060:8"]]
+ 009dcacc ["INT_ADD", "register:40f0:8", ["const:9dcacc:8", "const:4:8"]]
+ 009dcacc ["CALL", null, ["callee:00bdb060:8"]]
- 009dca88 bytes 62f90794
+ 009dcacc bytes 65f90794
- 009dcabc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 009dcabc ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 009dcabc bytes a1000054
- 009dcacc ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 009dcacc bytes a0fdff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2d973f8a605130c7b4c3515840cc587"></a>

### [`009dcb3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dcb3c.md) → [`009dcb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dcb80.md) FUN_009dcb80

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009dcb04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dcb04.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`009dcb48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dcb48.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 84.62% / 新版 91.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009dcb44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009dcb44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009dcb48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009dcb44",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:009dcb48",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009dcb4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009dcb88",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "009dcb8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009dcb90",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009dcb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dcb3c.md#insn-009dcb44) · [`009dcb48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dcb3c.md#insn-009dcb48) · [`009dcb4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dcb3c.md#insn-009dcb4c)

~~~diff
- 009dcb44 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009dcb44 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009dcb44 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 009dcb44 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009dcb44 bytes fd7bbda9
- 009dcb48 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 009dcb48 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 009dcb48 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 009dcb48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009dcb48 bytes f65701a9
- 009dcb4c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 009dcb4c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 009dcb4c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 009dcb4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009dcb4c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8773a8877e2595cae60573cf7fe459f"></a>

### [`009dcecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dcecc.md) → [`009dcf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dcf10.md) FUN_009dcf10

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009dcca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dcca0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`009dcce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dcce4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009dcecc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009dcecc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009dcf10"
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
      "unmatched:009dcecc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009dced8",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ],
    [
      "unmatched:009dcedc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "009dcf10",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009dcf1c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "009dcf20",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00418c38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009dcecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dcecc.md#insn-009dcecc) · [`009dcedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dcecc.md#insn-009dcedc)
- 新版 [`009dcf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dcf10.md#insn-009dcf10)

~~~diff
- 009dcecc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009dcecc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009dcecc ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 009dcecc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009dcecc bytes fd7bbfa9
- 009dcedc ["INT_ADD", "register:40f0:8", ["const:9dcedc:8", "const:4:8"]]
- 009dcedc ["CALL", null, ["callee:00418c38:8"]]
- 009dcedc bytes 57efe897
+ 009dcf10 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 009dcf10 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 009dcf10 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 009dcf10 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 009dcf10 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5ded50766fb9ef05e2dac78addcc43d"></a>

### [`009dd800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dd/009dd800.md) → [`009dd844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dd/009dd844.md) FUN_009dd844

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009dd6cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dd/009dd6cc.md) · 呼出先 3件 [`00471738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471738.md) [`0059d12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d12c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`009dd710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dd/009dd710.md) · 呼出先 3件 [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 33.33% / 新版 34.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009dd800"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009dd800"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009dd804"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009dd800",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:009dd804",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009dd808",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009dd844",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "009dd848",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009dd84c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009dd800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dd/009dd800.md#insn-009dd800) · [`009dd804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dd/009dd800.md#insn-009dd804) · [`009dd808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dd/009dd800.md#insn-009dd808)

~~~diff
- 009dd800 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009dd800 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009dd800 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 009dd800 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009dd800 bytes fd7bbda9
- 009dd804 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009dd804 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 009dd804 bytes f50b00f9
- 009dd808 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 009dd808 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 009dd808 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 009dd808 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009dd808 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5262d02d63c625b4cd12a09720b3fd48"></a>

### [`009de78c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009de/009de78c.md) → [`009de7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009de/009de7d0.md) FUN_009de7d0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009dd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dd/009dd990.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`009dd9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dd/009dd9d4.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 79.01% / 新版 79.01%

CFGの説明率　旧版 35.00% / 新版 35.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009de78c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009de78c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009de790"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009de78c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:009de790",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:009de794",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009de7d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "009de7d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "009de7d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009de78c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009de/009de78c.md#insn-009de78c) · [`009de790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009de/009de78c.md#insn-009de790) · [`009de794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009de/009de78c.md#insn-009de794)

~~~diff
- 009de78c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009de78c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009de78c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 009de78c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009de78c bytes fd7bbaa9
- 009de790 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009de790 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 009de790 bytes fb0b00f9
- 009de794 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 009de794 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 009de794 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 009de794 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009de794 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94759e6312f50e5280fd0bf03a463f75"></a>

### [`009e08bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e0/009e08bc.md) → [`009e0900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e0/009e0900.md) FUN_009e0900

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009dfce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009df/009dfce0.md) · 呼出先 2件 [`00878784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/00878784.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`009dfd24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009df/009dfd24.md) · 呼出先 2件 [`00878784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878784.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.83% / 新版 70.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e08c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e08c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e08c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009e08c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009e08c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009e08d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e0904",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009e0908",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009e0918",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e08c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e0/009e08bc.md#insn-009e08c0) · [`009e08c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e0/009e08bc.md#insn-009e08c4) · [`009e08d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e0/009e08bc.md#insn-009e08d4)

~~~diff
- 009e08c0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009e08c0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009e08c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 009e08c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009e08c0 bytes fd7b03a9
- 009e08c4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 009e08c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 009e08c4 bytes f32300f9
- 009e08d4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009e08d4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009e08d4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009e08d4 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e3d90b31c5bf71bfd60d76abd5f09ff"></a>

### [`009e16f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e1/009e16f0.md) → [`009e1734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1734.md) FUN_009e1734

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d12c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e170c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009e1750"
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
      "unmatched:009e170c",
      "DATA",
      [
        "storage",
        "00c0b9c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e1750",
      "DATA",
      [
        "storage",
        "00c0ba18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e170c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e1/009e16f0.md#insn-009e170c) · [`009e1704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e1/009e16f0.md#insn-009e1704)
- 新版 [`009e1750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1734.md#insn-009e1750)

~~~diff
- 009e170c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009e170c ["COPY", "tmp:1:8", ["register:4000:8"]]
- 009e170c ["INT_ADD", "register:4000:8", ["register:4000:8", "const:40:8"]]
- 009e170c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009e170c bytes 080404f8
+ 009e1750 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 009e1750 ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 009e1750 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:40:8"]]
+ 009e1750 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 009e1750 bytes 080404f8
- 009e1704 ["COPY", "tmp:0:8", ["const:9c8:8"]]
- 009e1704 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e1704 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e1704 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e1704 bytes 08212791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7cb00353b367ae7a634f92e0584267a"></a>

### [`009e3b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e3/009e3b7c.md) → [`009e3bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3bc0.md) FUN_009e3bc0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e3b94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009e3bd8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "009e3b9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009e3b94",
      "DATA",
      [
        "storage",
        "00c0bb68",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009e3b98",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e3bd8",
      "DATA",
      [
        "storage",
        "00c0bbb8",
        null,
        "undefined *"
      ]
    ],
    [
      "009e3bdc",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e3b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e3/009e3b7c.md#insn-009e3b94) · [`009e3b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e3/009e3b7c.md#insn-009e3b9c)
- 新版 [`009e3bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3bc0.md#insn-009e3bd8)

~~~diff
- 009e3b94 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 009e3b94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009e3b94 bytes 080000f9
- 009e3b9c ["COPY", "register:0:8", ["register:40f0:8"]]
- 009e3b9c ["RETURN", null, ["register:0:8"]]
- 009e3b9c bytes c0035fd6
+ 009e3bd8 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 009e3bd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009e3bd8 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ff1264bbb70da4ff6d3072292efa0b7"></a>

### [`009e3ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e3/009e3ba0.md) → [`009e3be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3be4.md) FUN_009e3be4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e3ba8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009e3bec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "009e3bac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009e3ba8",
      "DATA",
      [
        "storage",
        "00c0bb68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e3bec",
      "DATA",
      [
        "storage",
        "00c0bbb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e3ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e3/009e3ba0.md#insn-009e3ba8) · [`009e3bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e3/009e3ba0.md#insn-009e3bac)
- 新版 [`009e3bec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3be4.md#insn-009e3bec)

~~~diff
- 009e3ba8 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 009e3ba8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009e3ba8 bytes 280000f9
- 009e3bac ["COPY", "register:0:8", ["register:40f0:8"]]
- 009e3bac ["RETURN", null, ["register:0:8"]]
- 009e3bac bytes c0035fd6
+ 009e3bec ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 009e3bec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009e3bec bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f92eb61a2790d487912484311aadbd06"></a>

### [`009e3bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e3/009e3bb8.md) → [`009e3bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3bfc.md) FUN_009e3bfc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e3bd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009e3c14"
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
      "unmatched:009e3bd0",
      "DATA",
      [
        "storage",
        "00397054",
        "fde_00397054",
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "009e3c14",
      "DATA",
      [
        "storage",
        "00397054",
        "fde_00397054",
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e3bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e3/009e3bb8.md#insn-009e3bd0) · [`009e3bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e3/009e3bb8.md#insn-009e3bc0)
- 新版 [`009e3c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3bfc.md#insn-009e3c14) · [`009e3c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3bfc.md#insn-009e3c04)

~~~diff
- 009e3bd0 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 009e3bd0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 009e3bd0 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 009e3bd0 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 009e3bd0 bytes 096828b8
+ 009e3c14 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 009e3c14 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 009e3c14 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 009e3c14 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 009e3c14 bytes 096828b8
- 009e3bc0 ["INT_ADD", "register:40f0:8", ["const:9e3bc0:8", "const:4:8"]]
- 009e3bc0 ["CALL", null, ["callee:0081f580:8"]]
+ 009e3c04 ["INT_ADD", "register:40f0:8", ["const:9e3c04:8", "const:4:8"]]
+ 009e3c04 ["CALL", null, ["callee:0081f580:8"]]
- 009e3bc0 bytes 70eef897
+ 009e3c04 bytes 5feef897
~~~


<a id="compare-fdfa6b3af65b4f7522a10af8067e2455"></a>

### [`009e3c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e3/009e3c08.md) → [`009e3c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3c4c.md) FUN_009e3c4c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e3c2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e3c2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009e3c70"
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
      "unmatched:009e3c2c",
      "DATA",
      [
        "storage",
        "00c0bbe8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009e3c30",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009e3c34",
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
      "009e3c70",
      "DATA",
      [
        "storage",
        "00c0bc38",
        null,
        "undefined *"
      ]
    ],
    [
      "009e3c74",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009e3c78",
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

- 旧版 [`009e3c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e3/009e3c08.md#insn-009e3c2c) · [`009e3c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e3/009e3c08.md#insn-009e3c38)
- 新版 [`009e3c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3c4c.md#insn-009e3c70)

~~~diff
- 009e3c2c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009e3c2c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 009e3c2c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 009e3c2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009e3c2c bytes 082400a9
- 009e3c38 ["COPY", "register:0:8", ["register:40f0:8"]]
- 009e3c38 ["RETURN", null, ["register:0:8"]]
- 009e3c38 bytes c0035fd6
+ 009e3c70 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 009e3c70 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 009e3c70 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 009e3c70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 009e3c70 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ccd4b9b187509720e47524e3e89ab24"></a>

### [`009e583c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e5/009e583c.md) → [`009e5880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e5880.md) FUN_009e5880

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005d0a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d0/005d0a68.md) [`006ee6c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ee/006ee6c8.md) [`009f4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f4/009f4a74.md) · 呼出先 8件 [`0047c518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c518.md) [`005bce08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bce08.md) [`005be130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005be/005be130.md) [`005c2720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2720.md) [`0063e4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e4a8.md)
- 新版 呼出元 3件 [`005d0a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d0/005d0a68.md) [`006ee6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ee/006ee6c8.md) [`009f4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f4ab8.md) · 呼出先 8件 [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`005bce08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bce08.md) [`005be130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005be/005be130.md) [`005c2720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2720.md) [`0063e4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e4a8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 55.56% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "009e5960"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "009e59a4"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`009e5960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e5/009e583c.md#insn-009e5960) · [`009e5854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e5/009e583c.md#insn-009e5854)
- 新版 [`009e59a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e5880.md#insn-009e59a4) · [`009e5898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e5880.md#insn-009e5898)

~~~diff
- 009e5960 ["COPY", "register:0:8", ["register:40f0:8"]]
- 009e5960 ["RETURN", null, ["register:0:8"]]
- 009e5960 bytes c0035fd6
+ 009e59a4 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 009e59a4 ["RETURN", null, ["register:0:8"]]
+ 009e59a4 bytes c0035fd6
- 009e5854 ["INT_ADD", "register:40f0:8", ["const:9e5854:8", "const:4:8"]]
- 009e5854 ["CALL", null, ["callee:0081f580:8"]]
+ 009e5898 ["INT_ADD", "register:40f0:8", ["const:9e5898:8", "const:4:8"]]
+ 009e5898 ["CALL", null, ["callee:0081f580:8"]]
- 009e5854 bytes 4be7f897
+ 009e5898 bytes 3ae7f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5847f7577a1422101280091c04c36226"></a>

### [`009e5f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e5/009e5f20.md) → [`009e5f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e5f64.md) FUN_009e5f64

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005bc910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bc910.md) [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 5件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00821cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821cb4.md) [`009e4ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e4/009e4ef8.md) [`009e4f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e4/009e4f84.md) [`00a93f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93f08.md)
- 新版 呼出元 2件 [`005bc910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc910.md) [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 5件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00821cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cb4.md) [`009e4f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4f3c.md) [`009e4fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4fc8.md) [`00a93f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a93f4c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.64% / 新版 94.64%

CFGの説明率　旧版 33.33% / 新版 34.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009e5f58"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009e5f78"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009e5fbc"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`009e5f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e5/009e5f20.md#insn-009e5f34) · [`009e5f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e5/009e5f20.md#insn-009e5f58) · [`009e5f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e5/009e5f20.md#insn-009e5f78)
- 新版 [`009e5f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e5f64.md#insn-009e5f78)

~~~diff
- 009e5f34 ["INT_ADD", "register:40f0:8", ["const:9e5f34:8", "const:4:8"]]
- 009e5f34 ["CALL", null, ["callee:009e4f3c:8"]]
+ 009e5f78 ["INT_ADD", "register:40f0:8", ["const:9e5f78:8", "const:4:8"]]
+ 009e5f78 ["CALL", null, ["callee:009e4f3c:8"]]
- 009e5f34 bytes f1fbff97
+ 009e5f78 bytes f1fbff97
- 009e5f58 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 009e5f58 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 009e5f58 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 009e5f58 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 009e5f58 bytes 08b1899a
- 009e5f78 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 009e5f78 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 009e5f78 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 009e5f78 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 009e5f78 bytes b4b2889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a605d87bd4519e924418bf10bb0c86a"></a>

### [`009e9afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e9afc.md) → [`009e9b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9b40.md) FUN_009e9b40

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 30件 [`005a02e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a0/005a02e8.md) [`005a2308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a2/005a2308.md) [`005a3eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a3/005a3eb8.md) [`005a45f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a4/005a45f4.md) [`0062da7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062da7c.md) · 呼出先 2件 [`009e9afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e9afc.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)
- 新版 呼出元 30件 [`005a02e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a0/005a02e8.md) [`005a2308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a2/005a2308.md) [`005a3eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a3/005a3eb8.md) [`005a45f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md) [`0062da7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062da7c.md) · 呼出先 2件 [`009e9b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9b40.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009e9b90",
      "PARAM",
      [
        "storage",
        "00c0bd08",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009e9b94",
      "PARAM",
      [
        "storage",
        "00c0bd18",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009e9b90",
      "PARAM",
      [
        "storage",
        "00c0bd58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009e9b94",
      "PARAM",
      [
        "storage",
        "00c0bd68",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e9b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e9afc.md#insn-009e9b3c) · [`009e9b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e9afc.md#insn-009e9b40) · [`009e9b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e9afc.md#insn-009e9b44)
- 新版 [`009e9b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9b40.md#insn-009e9b80) · [`009e9b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9b40.md#insn-009e9b88)

~~~diff
- 009e9b3c ["COPY", "tmp:0:8", ["const:d08:8"]]
- 009e9b3c ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 009e9b3c ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 009e9b3c ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 009e9b80 ["COPY", "tmp:0:8", ["const:d58:8"]]
+ 009e9b80 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 009e9b80 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 009e9b80 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 009e9b3c bytes f7223491
+ 009e9b80 bytes f7623591
- 009e9b40 ["COPY", "register:40c0:8", ["const:c0b000:8"]]
- 009e9b40 bytes 181100d0
- 009e9b44 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 009e9b44 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 009e9b44 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 009e9b44 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 009e9b88 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 009e9b88 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 009e9b88 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 009e9b88 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 009e9b44 bytes 18633491
+ 009e9b88 bytes 18a33591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0907814e7ce1008c742bb33780c7ca4b"></a>

### [`00a01fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a01/00a01fd8.md) → [`00a0201c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a0201c.md) FUN_00a0201c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a010f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a01/00a010f0.md) [`00a01fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a01/00a01fd8.md) · 呼出先 4件 [`00a01fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a01/00a01fd8.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 2件 [`00a01134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01134.md) [`00a0201c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a0201c.md) · 呼出先 4件 [`00a0201c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a0201c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 69.23% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a01fdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a01fdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a01fe0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a01fdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a01fe0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a02020",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a02024",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a01fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a01/00a01fd8.md#insn-00a01fdc) · [`00a01fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a01/00a01fd8.md#insn-00a01fe0) · [`00a02020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a01/00a01fd8.md#insn-00a02020)
- 新版 [`00a02064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a0201c.md#insn-00a02064)

~~~diff
- 00a01fdc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a01fdc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a01fdc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a01fdc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a01fdc bytes fd7bbea9
- 00a01fe0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a01fe0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a01fe0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a01fe0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a01fe0 bytes f44f01a9
- 00a02020 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00a02020 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00a02020 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00a02020 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00a02064 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00a02064 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00a02064 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00a02064 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00a02020 bytes 68000036
+ 00a02064 bytes 68000036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c19efb6ceb934ee209d73fb8718e1cb5"></a>

### [`00a02120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a02120.md) → [`00a02164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02164.md) FUN_00a02164

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f4/009f4a74.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`009f4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f4ab8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a02120"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a02120"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a02164"
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
      "unmatched:00a02120",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0212c",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a02130",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00a02164",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a02170",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00a02174",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00418c38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a02120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a02120.md#insn-00a02120) · [`00a02130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a02120.md#insn-00a02130)
- 新版 [`00a02164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02164.md#insn-00a02164)

~~~diff
- 00a02120 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a02120 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a02120 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00a02120 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a02120 bytes fd7bbfa9
- 00a02130 ["INT_ADD", "register:40f0:8", ["const:a02130:8", "const:4:8"]]
- 00a02130 ["CALL", null, ["callee:00418c38:8"]]
- 00a02130 bytes c25ae897
+ 00a02164 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00a02164 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00a02164 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00a02164 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00a02164 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97beb303d2242d6bf8c24db8eaaa4d1b"></a>

### [`00a02a8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a02a8c.md) → [`00a02ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02ad0.md) FUN_00a02ad0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a02d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a02d90.md) · 呼出先 3件 [`007cd2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd2ac.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a08564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a08/00a08564.md)
- 新版 呼出元 1件 [`00a02dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02dd4.md) · 呼出先 3件 [`007cd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd2ac.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a085a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a085a8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 99.05% / 新版 99.05%

CFGの説明率　旧版 70.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a02b18"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a02b5c"
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
      "unmatched:00a02b18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a02b90"
      ]
    ]
  ],
  "added": [
    [
      "00a02b5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a02b90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a02b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a02a8c.md#insn-00a02b18) · [`00a02a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a02a8c.md#insn-00a02a94)
- 新版 [`00a02b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02ad0.md#insn-00a02b5c) · [`00a02ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02ad0.md#insn-00a02ad8)

~~~diff
- 00a02b18 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a02b18 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00a02b18 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00a02b18 bytes a8010054
+ 00a02b5c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a02b5c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00a02b5c ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
+ 00a02b5c bytes a8010054
- 00a02a94 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 00a02ad8 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00a02a94 bytes 80050054
+ 00a02ad8 bytes 80050054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d89795fe9a71993a40047e20fcd1bc86"></a>

### [`00a02c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a02c30.md) → [`00a02c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02c74.md) FUN_00a02c74

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a02d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a02d90.md) · 呼出先 3件 [`006fe610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fe/006fe610.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00ade5cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade5cc.md)
- 新版 呼出元 1件 [`00a02dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02dd4.md) · 呼出先 3件 [`006fe610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fe610.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00ade610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade610.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 82.95% / 新版 82.95%

CFGの説明率　旧版 15.38% / 新版 13.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a02c4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a02c90"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a02c90"
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
      "unmatched:00a02c4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a02cac"
      ]
    ],
    [
      "unmatched:00a02c90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a02d3c"
      ]
    ],
    [
      "unmatched:00a02d6c",
      "DATA",
      [
        "storage",
        "003b1d70",
        null,
        "byte[23]"
      ]
    ]
  ],
  "added": [
    [
      "00a02c90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a02cac"
      ]
    ],
    [
      "00a02cd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a02d0c"
      ]
    ],
    [
      "00a02db0",
      "DATA",
      [
        "storage",
        "003b1d70",
        null,
        "byte[23]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a02c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a02c30.md#insn-00a02c4c) · [`00a02c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a02c30.md#insn-00a02c90)
- 新版 [`00a02c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02c74.md#insn-00a02c90)

~~~diff
- 00a02c4c ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00a02c4c bytes e0000054
- 00a02c90 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a02c90 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00a02c90 ["CBRANCH", null, ["local:b8:8", "tmp:1:1"]]
- 00a02c90 bytes c8010054
+ 00a02c90 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 00a02c90 bytes e0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87c6c8b1dd9d1e7bf232b519152e98f0"></a>

### [`00a02d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a02d90.md) → [`00a02dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02dd4.md) FUN_00a02dd4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`00695904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md) [`00a30514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a30/00a30514.md) [`00a33510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a33510.md) [`00a3371c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a3371c.md) [`00a3ce88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3ce88.md) · 呼出先 3件 [`00a028b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a028b8.md) [`00a02a8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a02a8c.md) [`00a02c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a02c30.md)
- 新版 呼出元 6件 [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) [`00a30558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a30/00a30558.md) [`00a33554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a33554.md) [`00a33760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a33760.md) [`00a3cecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cecc.md) · 呼出先 3件 [`00a028fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a028fc.md) [`00a02ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02ad0.md) [`00a02c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02c74.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.80% / 新版 89.80%

CFGの説明率　旧版 80.95% / 新版 89.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a02d90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a02d90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a02d94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a02d90",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a02d94",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a02d98",
      "WRITE",
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
      "00a02dd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00a02dd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a02ddc",
      "WRITE",
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

- 旧版 [`00a02d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a02d90.md#insn-00a02d90) · [`00a02d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a02d90.md#insn-00a02d94) · [`00a02d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a02d90.md#insn-00a02d98)

~~~diff
- 00a02d90 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a02d90 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a02d90 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00a02d90 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a02d90 bytes fd7bbca9
- 00a02d94 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a02d94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00a02d94 bytes f70b00f9
- 00a02d98 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a02d98 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a02d98 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a02d98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a02d98 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fee021a36346228bc9777cdd41fbcb88"></a>

### [`00a04a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a04/00a04a10.md) → [`00a04a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a04/00a04a54.md) FUN_00a04a54

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a024c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a02/00a024c4.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00a04bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a04/00a04bc0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00a02508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02508.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00a04c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a04/00a04c04.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.11% / 新版 86.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a04acc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a04acc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a04ad4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a04afc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a04bcc"
      ]
    ]
  ],
  "added": [
    [
      "00a04b40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a04bcc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a04acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a04/00a04a10.md#insn-00a04acc) · [`00a04ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a04/00a04a10.md#insn-00a04ad4) · [`00a04ad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a04/00a04a10.md#insn-00a04ad8)

~~~diff
- 00a04acc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a04acc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00a04acc ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00a04acc ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5040:16"]]
- 00a04acc bytes 210900ad
- 00a04ad4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00a04ad4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00a04ad4 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00a04ad4 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00a04ad4 bytes 9f7e03a9
- 00a04ad8 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00a04ad8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00a04ad8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00a04ad8 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00a04ad8 bytes 9f7e04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dcdad59cc4d6e75384bcf3b202c4a36"></a>

### [`00a05218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a05/00a05218.md) → [`00a0525c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a0525c.md) FUN_00a0525c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0523c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0523c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a05280"
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
      "unmatched:00a0523c",
      "DATA",
      [
        "storage",
        "00c0be10",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a05240",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a05244",
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
      "00a05280",
      "DATA",
      [
        "storage",
        "00c0be60",
        null,
        "undefined *"
      ]
    ],
    [
      "00a05284",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a05288",
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

- 旧版 [`00a0523c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a05/00a05218.md#insn-00a0523c) · [`00a05248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a05/00a05218.md#insn-00a05248)
- 新版 [`00a05280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a0525c.md#insn-00a05280)

~~~diff
- 00a0523c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a0523c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a0523c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a0523c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a0523c bytes 082400a9
- 00a05248 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a05248 ["RETURN", null, ["register:0:8"]]
- 00a05248 bytes c0035fd6
+ 00a05280 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a05280 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a05280 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00a05280 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a05280 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ab859524501314727daf945ff94b376"></a>

### [`00a06b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a06/00a06b6c.md) → [`00a06bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06bb0.md) FUN_00a06bb0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009bd6b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009bd/009bd6b8.md) · 呼出先 1件 [`0045d518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d518.md)
- 新版 呼出元 1件 [`009bd6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd6c4.md) · 呼出先 1件 [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a06bb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a06bfc"
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
      "unmatched:00a06bb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a06bec"
      ]
    ]
  ],
  "added": [
    [
      "00a06bfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a06bec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a06bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a06/00a06b6c.md#insn-00a06bb8) · [`00a06b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a06/00a06b6c.md#insn-00a06b98)
- 新版 [`00a06bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06bb0.md#insn-00a06bfc) · [`00a06bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06bb0.md#insn-00a06bdc)

~~~diff
- 00a06bb8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a06bb8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00a06bb8 bytes 81ffff54
+ 00a06bfc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a06bfc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00a06bfc bytes 81ffff54
- 00a06b98 ["INT_ADD", "register:40f0:8", ["const:a06b98:8", "const:4:8"]]
- 00a06b98 ["CALL", null, ["callee:0045d518:8"]]
+ 00a06bdc ["INT_ADD", "register:40f0:8", ["const:a06bdc:8", "const:4:8"]]
+ 00a06bdc ["CALL", null, ["callee:0045d518:8"]]
- 00a06b98 bytes 605ae997
+ 00a06bdc bytes 4f5ae997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e9b4147580f9723b858d44eb528ebeb"></a>

### [`00a07fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a07/00a07fd8.md) → [`00a0801c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a0801c.md) FUN_00a0801c

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`007ab6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ab/007ab6a0.md) [`00a081d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a08/00a081d8.md) [`00a083e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a08/00a083e4.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 3件 [`007ab6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ab/007ab6a0.md) [`00a0821c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a0821c.md) [`00a08428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a08428.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 55.56% / 新版 52.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a080a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a08184"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0818c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a07ff8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0807c"
      ]
    ],
    [
      "unmatched:00a080ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a08144"
      ]
    ]
  ],
  "added": [
    [
      "00a0803c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0807c"
      ]
    ],
    [
      "00a08130",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a08144"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a07ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a07/00a07fd8.md#insn-00a07ff8) · [`00a08018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a07/00a07fd8.md#insn-00a08018)
- 新版 [`00a0803c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a0801c.md#insn-00a0803c)

~~~diff
- 00a07ff8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a07ff8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00a07ff8 bytes 080200b4
- 00a08018 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a08018 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a08018 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00a08018 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00a08018 bytes 29b18a9a
+ 00a0803c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00a0803c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00a0803c bytes 080200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84aa6ea7b08a5575bb004a2fe8a08dab"></a>

### [`00a092a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a09/00a092a0.md) → [`00a092e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a092e4.md) FUN_00a092e4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`0079a4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079a/0079a4e4.md) [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) [`007c5e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5e34.md) [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 5件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`0079a4e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079a/0079a4e4.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) [`007c5e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5e34.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 60.34% / 新版 60.34%

CFGの説明率　旧版 12.24% / 新版 11.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 15件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 25件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a092a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a092a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a092a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a092a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a092a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a092a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a092e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a092e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00a092ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a092a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a09/00a092a0.md#insn-00a092a0) · [`00a092a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a09/00a092a0.md#insn-00a092a4) · [`00a092a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a09/00a092a0.md#insn-00a092a8)

~~~diff
- 00a092a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a092a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a092a0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00a092a0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a092a0 bytes fd7bbba9
- 00a092a4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a092a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00a092a4 bytes f90b00f9
- 00a092a8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00a092a8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00a092a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a092a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a092a8 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf5be7e2e933e1549b6d5a3101020e55"></a>

### [`00a098d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a09/00a098d8.md) → [`00a0991c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a0991c.md) FUN_00a0991c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`007e9118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e9/007e9118.md) [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`007e9118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e9/007e9118.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 68.42% / 新版 68.42%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a098d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a098d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a098dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a098d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a098dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a098e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a0991c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a09920",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a09924",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a098d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a09/00a098d8.md#insn-00a098d8) · [`00a098dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a09/00a098d8.md#insn-00a098dc) · [`00a098e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a09/00a098d8.md#insn-00a098e0)

~~~diff
- 00a098d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a098d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a098d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00a098d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a098d8 bytes fd7bbda9
- 00a098dc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a098dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00a098dc bytes f50b00f9
- 00a098e0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a098e0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a098e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a098e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a098e0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d37f681dd4363f3d086ff1ab2aa67f1"></a>

### [`00a09be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a09/00a09be4.md) → [`00a09c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09c28.md) FUN_00a09c28

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) · 呼出先 4件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`005bafb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005bafb8.md) [`007cd120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd120.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 4件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`005bafb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005bafb8.md) [`007cd120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd120.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 26.67% / 新版 26.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a09c24"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a09c84"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a09ca8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a09c84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a09cb8"
      ]
    ],
    [
      "unmatched:00a09ca8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a09d38"
      ]
    ],
    [
      "unmatched:00a09cac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0081f580"
      ]
    ]
  ],
  "added": [
    [
      "00a09cc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a09cb8"
      ]
    ],
    [
      "00a09cec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a09d38"
      ]
    ],
    [
      "00a09cf0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0081f580"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a09c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a09/00a09be4.md#insn-00a09c24) · [`00a09c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a09/00a09be4.md#insn-00a09c68)
- 新版 [`00a09cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09c28.md#insn-00a09cac) · [`00a09c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09c28.md#insn-00a09c68)

~~~diff
- 00a09c24 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a09c24 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a09c24 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00a09c24 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a09c24 bytes 08b1899a
- 00a09c68 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a09c68 ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
+ 00a09cac ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00a09cac ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
- 00a09c68 bytes 080400b4
+ 00a09cac bytes 080400b4
+ 00a09c68 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00a09c68 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00a09c68 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00a09c68 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a09c68 bytes 08b1899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32bf4ca897c0f11f55e98cd0e8217ca7"></a>

### [`00a09d28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a09/00a09d28.md) → [`00a09d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09d6c.md) FUN_00a09d6c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a0a488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0a/00a0a488.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00a0a4cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a4cc.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 68.42% / 新版 68.42%

CFGの説明率　旧版 55.56% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a09d28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a09d28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a09d2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a09d28",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a09d2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a09d3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a09dac"
      ]
    ]
  ],
  "added": [
    [
      "00a09d6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a09d70",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a09d80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a09dac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a09d28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a09/00a09d28.md#insn-00a09d28) · [`00a09d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a09/00a09d28.md#insn-00a09d2c) · [`00a09d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a09/00a09d28.md#insn-00a09d38)

~~~diff
- 00a09d28 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a09d28 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a09d28 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a09d28 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a09d28 bytes fd7bbea9
- 00a09d2c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a09d2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00a09d2c bytes f30b00f9
- 00a09d38 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00a09d38 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00a09d38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00a09d38 bytes 1f0000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-278924b64301dc5b7601ae8763a4d082"></a>

### [`00a0a160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0a/00a0a160.md) → [`00a0a1a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a1a4.md) FUN_00a0a1a4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a09d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a09/00a09d74.md) · 呼出先 4件 [`006928b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00692/006928b0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00a09db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09db8.md) · 呼出先 4件 [`006928b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00692/006928b0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 99.50% / 新版 99.50%

CFGの説明率　旧版 95.65% / 新版 94.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0a2d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a0a31c"
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
      "unmatched:00a0a2d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0a308"
      ]
    ]
  ],
  "added": [
    [
      "00a0a31c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0a308"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0a2d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0a/00a0a160.md#insn-00a0a2d8) · [`00a0a1a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0a/00a0a160.md#insn-00a0a1a4)
- 新版 [`00a0a31c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a1a4.md#insn-00a0a31c) · [`00a0a1e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a1a4.md#insn-00a0a1e8)

~~~diff
- 00a0a2d8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a0a2d8 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00a0a2d8 bytes 61ffff54
+ 00a0a31c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a0a31c ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
+ 00a0a31c bytes 61ffff54
- 00a0a1a4 ["INT_ADD", "register:40f0:8", ["const:a0a1a4:8", "const:4:8"]]
- 00a0a1a4 ["CALL", null, ["callee:00bdb060:8"]]
+ 00a0a1e8 ["INT_ADD", "register:40f0:8", ["const:a0a1e8:8", "const:4:8"]]
+ 00a0a1e8 ["CALL", null, ["callee:00bdb060:8"]]
- 00a0a1a4 bytes 9b430794
+ 00a0a1e8 bytes 9e430794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd86619c66dd3b9e02ea200757941f59"></a>

### [`00a0a488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0a/00a0a488.md) → [`00a0a4cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a4cc.md) FUN_00a0a4cc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a09d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a09/00a09d74.md) · 呼出先 6件 [`006928b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00692/006928b0.md) [`00a09d28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a09/00a09d28.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00a09db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09db8.md) · 呼出先 6件 [`006928b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00692/006928b0.md) [`00a09d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09d6c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 60.00% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0a528"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00a0a56c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a0a4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0a/00a0a488.md#insn-00a0a4e4) · [`00a0a528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0a/00a0a488.md#insn-00a0a528)
- 新版 [`00a0a528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a4cc.md#insn-00a0a528) · [`00a0a56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a4cc.md#insn-00a0a56c)

~~~diff
- 00a0a4e4 ["INT_ADD", "register:40f0:8", ["const:a0a4e4:8", "const:4:8"]]
- 00a0a4e4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a0a528 ["INT_ADD", "register:40f0:8", ["const:a0a528:8", "const:4:8"]]
+ 00a0a528 ["CALL", null, ["callee:00bdb040:8"]]
- 00a0a4e4 bytes c3420794
+ 00a0a528 bytes c6420794
- 00a0a528 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a0a528 ["RETURN", null, ["register:0:8"]]
- 00a0a528 bytes c0035fd6
+ 00a0a56c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00a0a56c ["RETURN", null, ["register:0:8"]]
+ 00a0a56c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b69c01e743285209f0b94652336db4e"></a>

### [`00a0addc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0a/00a0addc.md) → [`00a0ae20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0ae20.md) FUN_00a0ae20

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a0bbd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0b/00a0bbd8.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00a0bc1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0bc1c.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.39% / 新版 95.39%

CFGの説明率　旧版 51.76% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0b01c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a0b060"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0ae4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a0ae4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0aeac"
      ]
    ],
    [
      "unmatched:00a0ae78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0aed0"
      ]
    ],
    [
      "unmatched:00a0aea8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0aeac"
      ]
    ]
  ],
  "added": [
    [
      "00a0ae90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0aeac"
      ]
    ],
    [
      "00a0aebc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0aed0"
      ]
    ],
    [
      "00a0aeec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0aeac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0ae4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0a/00a0addc.md#insn-00a0ae4c) · [`00a0ae78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0a/00a0addc.md#insn-00a0ae78)
- 新版 [`00a0ae90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0ae20.md#insn-00a0ae90)

~~~diff
- 00a0ae4c ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00a0ae4c ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00a0ae4c bytes e90000b4
- 00a0ae78 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00a0ae78 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00a0ae78 bytes a90000b5
+ 00a0ae90 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00a0ae90 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 00a0ae90 bytes e90000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-346f5278c1a843fb30dbe73061318be6"></a>

### [`00a0b048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0b/00a0b048.md) → [`00a0b08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b08c.md) FUN_00a0b08c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009ce1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009ce/009ce1d0.md) · 呼出先 6件 [`0045df50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045df50.md) [`00a0a900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0a/00a0a900.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 6件 [`0045df50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045df50.md) [`00a0a944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a944.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.14% / 新版 85.14%

CFGの説明率　旧版 42.31% / 新版 42.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0b05c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0b05c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0b0dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a0b05c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0b094",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0b114"
      ]
    ],
    [
      "unmatched:00a0b09c",
      "READ",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a0b0a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a0b0d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0b114"
      ]
    ],
    [
      "00a0b0e0",
      "READ",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0b05c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0b/00a0b048.md#insn-00a0b05c) · [`00a0b094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0b/00a0b048.md#insn-00a0b094) · [`00a0b0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0b/00a0b048.md#insn-00a0b0a0)

~~~diff
- 00a0b05c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a0b05c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a0b05c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00a0b05c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a0b05c bytes f44f06a9
- 00a0b094 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a0b094 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00a0b094 bytes e1010054
- 00a0b0a0 ["INT_LESSEQUAL", "register:105:1", ["register:4048:8", "register:4040:8"]]
- 00a0b0a0 ["INT_SBORROW", "register:106:1", ["register:4040:8", "register:4048:8"]]
- 00a0b0a0 ["INT_SUB", "tmp:0:8", ["register:4040:8", "register:4048:8"]]
- 00a0b0a0 ["INT_SLESS", "register:107:1", ["tmp:0:8", "const:0:8"]]
- 00a0b0a0 bytes 1f0109eb
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46ab0f7730c73afa8ef9226fd0bfc2b5"></a>

### [`00a0b5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0b/00a0b5b8.md) → [`00a0b5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b5fc.md) FUN_00a0b5fc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e0/005e02b0.md) [`0079942c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00799/0079942c.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 3件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e0/005e02b0.md) [`0079942c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00799/0079942c.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 67.50% / 新版 69.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0b608"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0b618"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a0b64c"
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
      "unmatched:00a0b608",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0b63c"
      ]
    ],
    [
      "unmatched:00a0b618",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0b644"
      ]
    ]
  ],
  "added": [
    [
      "00a0b64c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0b63c"
      ]
    ],
    [
      "00a0b65c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0b644"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0b5c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0b/00a0b5b8.md#insn-00a0b5c4) · [`00a0b608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0b/00a0b5b8.md#insn-00a0b608) · [`00a0b618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0b/00a0b5b8.md#insn-00a0b618)
- 新版 [`00a0b608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b5fc.md#insn-00a0b608)

~~~diff
- 00a0b5c4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a0b5c4 ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
+ 00a0b608 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00a0b608 ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
- 00a0b5c4 bytes e80500b4
+ 00a0b608 bytes e80500b4
- 00a0b608 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a0b608 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00a0b608 bytes 8bffff54
- 00a0b618 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a0b618 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00a0b618 bytes 48ffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea3aaff9e051482e480b355f451dd520"></a>

### [`00a0baf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0b/00a0baf4.md) → [`00a0bb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0bb38.md) FUN_00a0bb38

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e0/005e02b0.md) [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00a0acdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0a/00a0acdc.md)
- 新版 呼出元 3件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e0/005e02b0.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00a0ad20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0ad20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 91.23% / 新版 91.23%

CFGの説明率　旧版 60.98% / 新版 64.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0bb18"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0bb48"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0bb50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a0bb18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0bc04"
      ]
    ],
    [
      "unmatched:00a0bb48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0bb7c"
      ]
    ],
    [
      "unmatched:00a0bb50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0bbac"
      ]
    ]
  ],
  "added": [
    [
      "00a0bb5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0bc04"
      ]
    ],
    [
      "00a0bb8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0bb7c"
      ]
    ],
    [
      "00a0bb94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0bbac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0bb18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0b/00a0baf4.md#insn-00a0bb18) · [`00a0bb48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0b/00a0baf4.md#insn-00a0bb48) · [`00a0bb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0b/00a0baf4.md#insn-00a0bb50)

~~~diff
- 00a0bb18 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00a0bb18 ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
- 00a0bb18 bytes 490500b4
- 00a0bb48 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a0bb48 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00a0bb48 bytes 8bffff54
- 00a0bb50 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a0bb50 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00a0bb50 bytes ca000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa25c90056d18e5d0dd7d434f7b54d74"></a>

### [`00a0c798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0c/00a0c798.md) → [`00a0c7dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0c7dc.md) FUN_00a0c7dc

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0073465c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073465c.md) [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`009a1cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a1/009a1cd4.md) · 呼出先 6件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 3件 [`0073465c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073465c.md) [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`009a1cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a1/009a1cd4.md) · 呼出先 6件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.44% / 新版 93.44%

CFGの説明率　旧版 78.85% / 新版 82.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0c7c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0c7c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a0c804"
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
      "unmatched:00a0c7c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0c7c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0c7d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0c970"
      ]
    ]
  ],
  "added": [
    [
      "00a0c804",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ],
    [
      "00a0c80c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00a0c818",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0c970"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0c7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0c/00a0c798.md#insn-00a0c7c0) · [`00a0c7c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0c/00a0c798.md#insn-00a0c7c8) · [`00a0c7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0c/00a0c798.md#insn-00a0c7d4)

~~~diff
- 00a0c7c0 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00a0c7c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a0c7c0 bytes e80300f9
- 00a0c7c8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a0c7c8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a0c7c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a0c7c8 bytes a8831ff8
- 00a0c7d4 ["CBRANCH", null, ["local:b31:8", "register:101:1"]]
- 00a0c7d4 bytes c00a0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c383f11d9049610460aea631d28510f9"></a>

### [`00a0ca58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0c/00a0ca58.md) → [`00a0ca9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0ca9c.md) FUN_00a0ca9c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e0/005e02b0.md) [`0079942c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00799/0079942c.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`007ab264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ab/007ab264.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 6件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e0/005e02b0.md) [`0079942c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00799/0079942c.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`007ab264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ab/007ab264.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 76.19% / 新版 76.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0ca70"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a0cab4"
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
      "unmatched:00a0ca70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0cb0c"
      ]
    ]
  ],
  "added": [
    [
      "00a0cab4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0cb0c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0ca70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0c/00a0ca58.md#insn-00a0ca70) · [`00a0cac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0c/00a0ca58.md#insn-00a0cac4)
- 新版 [`00a0cab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0ca9c.md#insn-00a0cab4) · [`00a0cb08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0ca9c.md#insn-00a0cb08)

~~~diff
- 00a0ca70 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00a0ca70 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00a0ca70 bytes c90200b4
+ 00a0cab4 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00a0cab4 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 00a0cab4 bytes c90200b4
- 00a0cac4 ["INT_ADD", "register:40f0:8", ["const:a0cac4:8", "const:4:8"]]
- 00a0cac4 ["CALL", null, ["callee:0041fdf0:8"]]
+ 00a0cb08 ["INT_ADD", "register:40f0:8", ["const:a0cb08:8", "const:4:8"]]
+ 00a0cb08 ["CALL", null, ["callee:0041fdf0:8"]]
- 00a0cac4 bytes cb4ce897
+ 00a0cb08 bytes ba4ce897
~~~


<a id="compare-1a0f66ba56de69c6a3b55de9e5ada7f5"></a>

### [`00a0cb5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0c/00a0cb5c.md) → [`00a0cba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0cba0.md) FUN_00a0cba0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00906b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md) · 呼出先 6件 [`00a0e090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0e/00a0e090.md) [`00a0e0bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0e/00a0e0bc.md) [`00a0e0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0e/00a0e0e4.md) [`00a0e10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0e/00a0e10c.md) [`00a0e40c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0e/00a0e40c.md)
- 新版 呼出元 1件 [`00906b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906b9c.md) · 呼出先 6件 [`00a0e0d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e0d4.md) [`00a0e100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e100.md) [`00a0e128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e128.md) [`00a0e150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e150.md) [`00a0e450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e450.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 44.44% / 新版 36.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0cb88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0cb88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0cb8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a0cb94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0cc58"
      ]
    ]
  ],
  "added": [
    [
      "00a0cbd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0cc58"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0cb88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0c/00a0cb5c.md#insn-00a0cb88) · [`00a0cb8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0c/00a0cb5c.md#insn-00a0cb8c) · [`00a0cb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0c/00a0cb5c.md#insn-00a0cb90)

~~~diff
- 00a0cb88 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00a0cb88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a0cb88 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00a0cb88 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00a0cb88 bytes 600200ad
- 00a0cb8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:20:8"]]
- 00a0cb8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a0cb8c ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00a0cb8c ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00a0cb8c bytes 600201ad
- 00a0cb90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:40:8"]]
- 00a0cb90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a0cb90 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00a0cb90 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00a0cb90 bytes 600202ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36c3ffb088c5142e0a56f93b9ebdaae2"></a>

### [`00a0cdf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0c/00a0cdf4.md) → [`00a0ce38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0ce38.md) FUN_00a0ce38

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a0cfec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0c/00a0cfec.md) · 呼出先 9件 [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00a0d86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0d/00a0d86c.md) [`00a0d874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0d/00a0d874.md) [`00a0e194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0e/00a0e194.md) [`00a0e40c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0e/00a0e40c.md)
- 新版 呼出元 1件 [`00a0d030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d030.md) · 呼出先 9件 [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00a0d8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d8b0.md) [`00a0d8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d8b8.md) [`00a0e1d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e1d8.md) [`00a0e450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e450.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 93.58% / 新版 93.58%

CFGの説明率　旧版 57.14% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0ce28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a0ce6c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0cf98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a0ce28",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0cf98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0d02c"
      ]
    ],
    [
      "unmatched:00a0cfa0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0044d968"
      ]
    ]
  ],
  "added": [
    [
      "00a0ce6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00a0cfdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0d02c"
      ]
    ],
    [
      "00a0cfe4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0044d968"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0ce28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0c/00a0cdf4.md#insn-00a0ce28) · [`00a0cf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0c/00a0cdf4.md#insn-00a0cf98)
- 新版 [`00a0ce6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0ce38.md#insn-00a0ce6c)

~~~diff
- 00a0ce28 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a0ce28 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a0ce28 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a0ce28 bytes a8831ff8
+ 00a0ce6c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a0ce6c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
+ 00a0ce6c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00a0ce6c bytes a8831ff8
- 00a0cf98 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a0cf98 ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
- 00a0cf98 bytes 81020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c44183a5b2ab9095ffa59ca4b91783d"></a>

### [`00a0d13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0d/00a0d13c.md) → [`00a0d180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d180.md) FUN_00a0d180

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 41.67% / 新版 41.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0d13c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0d13c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0d140"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a0d13c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0d140",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0d154",
      "DATA",
      [
        "storage",
        "00c0be90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a0d180",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a0d184",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a0d198",
      "DATA",
      [
        "storage",
        "00c0bee0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0d13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0d/00a0d13c.md#insn-00a0d13c) · [`00a0d140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0d/00a0d13c.md#insn-00a0d140) · [`00a0d154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0d/00a0d13c.md#insn-00a0d154)

~~~diff
- 00a0d13c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a0d13c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a0d13c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a0d13c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a0d13c bytes fd7bbea9
- 00a0d140 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a0d140 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00a0d140 bytes f30b00f9
- 00a0d154 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00a0d154 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a0d154 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8771c64d3f71b0f909497694ebc58ae"></a>

### [`00a0d70c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0d/00a0d70c.md) → [`00a0d750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d750.md) FUN_00a0d750

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a0d964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0d/00a0d964.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00a0d9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d9a8.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 66.67% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0d7e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a0d82c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0d7a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a0d7e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0d850"
      ]
    ],
    [
      "unmatched:00a0d7a8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00a0d82c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0d850"
      ]
    ],
    [
      "00a0d7ec",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0d7a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0d/00a0d70c.md#insn-00a0d7a8) · [`00a0d7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0d/00a0d70c.md#insn-00a0d7e8)
- 新版 [`00a0d7e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d750.md#insn-00a0d7e8)

~~~diff
- 00a0d7a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a0d7a8 ["INT_ADD", "register:40f0:8", ["const:a0d7a8:8", "const:4:8"]]
- 00a0d7a8 ["CALLIND", null, ["register:0:8"]]
- 00a0d7a8 bytes 00013fd6
- 00a0d7e8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a0d7e8 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00a0d7e8 bytes 280100b4
+ 00a0d7e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:18:8"]]
+ 00a0d7e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a0d7e8 bytes 080d40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ead2d58d3a0ffbb1031663207e06bad8"></a>

### [`00a0d874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0d/00a0d874.md) → [`00a0d8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d8b8.md) FUN_00a0d8b8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a0cdf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0c/00a0cdf4.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00a0ce38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0ce38.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 48.15% / 新版 52.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0d8d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0d908"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a0d91c"
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
      "unmatched:00a0d8d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0d90c"
      ]
    ],
    [
      "unmatched:00a0d908",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0d93c"
      ]
    ]
  ],
  "added": [
    [
      "00a0d91c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0d90c"
      ]
    ],
    [
      "00a0d94c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a0d93c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0d8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0d/00a0d874.md#insn-00a0d8d8) · [`00a0d908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0d/00a0d874.md#insn-00a0d908)
- 新版 [`00a0d91c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d8b8.md#insn-00a0d91c)

~~~diff
- 00a0d8d8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a0d8d8 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00a0d8d8 bytes 81ffff54
- 00a0d908 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00a0d908 bytes 80ffff54
+ 00a0d91c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a0d91c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00a0d91c bytes 81ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1afe5ac830cc4fb47d85565cd5f19b3"></a>

### [`00a0e19c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0e/00a0e19c.md) → [`00a0e1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e1e0.md) FUN_00a0e1e0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a0c330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0c/00a0c330.md) · 呼出先 8件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00470c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470c48.md) [`00839974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00839/00839974.md) [`00a0d964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0d/00a0d964.md)
- 新版 呼出元 1件 [`00a0c374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0c374.md) · 呼出先 8件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00470c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470c48.md) [`00839974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839974.md) [`00a0d9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d9a8.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.73% / 新版 84.73%

CFGの説明率　旧版 68.09% / 新版 69.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0e1a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0e1a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0e1a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a0e1a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0e1a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0e1a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a0e1e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a0e1e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a0e1ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0e1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0e/00a0e19c.md#insn-00a0e1a0) · [`00a0e1a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0e/00a0e19c.md#insn-00a0e1a4) · [`00a0e1a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0e/00a0e19c.md#insn-00a0e1a8)

~~~diff
- 00a0e1a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a0e1a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a0e1a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a0e1a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a0e1a0 bytes fd7b02a9
- 00a0e1a4 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a0e1a4 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a0e1a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00a0e1a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a0e1a4 bytes fc6f03a9
- 00a0e1a8 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a0e1a8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a0e1a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00a0e1a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a0e1a8 bytes fa6704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6b3e7a94db6fcbcd403cfe615e1e669"></a>

### [`00a0e4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0e/00a0e4f8.md) → [`00a0e53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e53c.md) FUN_00a0e53c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d12c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0e51c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a0e560"
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
      "unmatched:00a0e51c",
      "DATA",
      [
        "storage",
        "00c0bee0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00a0e560",
      "DATA",
      [
        "storage",
        "00c0bf30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0e51c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0e/00a0e4f8.md#insn-00a0e51c) · [`00a0e508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0e/00a0e4f8.md#insn-00a0e508)
- 新版 [`00a0e560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e53c.md#insn-00a0e560) · [`00a0e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e53c.md#insn-00a0e54c)

~~~diff
- 00a0e51c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00a0e51c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a0e51c bytes 680200f9
+ 00a0e560 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 00a0e560 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00a0e560 bytes 680200f9
- 00a0e508 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00a0e508 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00a0e54c ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00a0e54c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00a0e508 bytes 730100b4
+ 00a0e54c bytes 730100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90e2bcd4dbbc23a7c4090e86730b77e6"></a>

### [`00a1da58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1d/00a1da58.md) → [`00a1da9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1d/00a1da9c.md) FUN_00a1da9c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1da7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1da7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a1dac0"
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
      "unmatched:00a1da7c",
      "DATA",
      [
        "storage",
        "00c0bf90",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a1da80",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a1da84",
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
      "00a1dac0",
      "DATA",
      [
        "storage",
        "00c0bfe0",
        null,
        "undefined *"
      ]
    ],
    [
      "00a1dac4",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a1dac8",
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

- 旧版 [`00a1da7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1d/00a1da58.md#insn-00a1da7c) · [`00a1da88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1d/00a1da58.md#insn-00a1da88)
- 新版 [`00a1dac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1d/00a1da9c.md#insn-00a1dac0)

~~~diff
- 00a1da7c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a1da7c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a1da7c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a1da7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a1da7c bytes 082400a9
- 00a1da88 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a1da88 ["RETURN", null, ["register:0:8"]]
- 00a1da88 bytes c0035fd6
+ 00a1dac0 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a1dac0 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a1dac0 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00a1dac0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a1dac0 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9afd6c30ea06ea3ad2538043261a309"></a>

### [`00a1dd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1d/00a1dd30.md) → [`00a1dd74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1d/00a1dd74.md) FUN_00a1dd74

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1dd48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a1dd8c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1dd50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a1dd48",
      "DATA",
      [
        "storage",
        "00c0c000",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a1dd4c",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a1dd8c",
      "DATA",
      [
        "storage",
        "00c0c050",
        null,
        "undefined *"
      ]
    ],
    [
      "00a1dd90",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a1dd48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1d/00a1dd30.md#insn-00a1dd48) · [`00a1dd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1d/00a1dd30.md#insn-00a1dd50)
- 新版 [`00a1dd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1d/00a1dd74.md#insn-00a1dd8c)

~~~diff
- 00a1dd48 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00a1dd48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a1dd48 bytes 080000f9
- 00a1dd50 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a1dd50 ["RETURN", null, ["register:0:8"]]
- 00a1dd50 bytes c0035fd6
+ 00a1dd8c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00a1dd8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00a1dd8c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c90ab9e92f0b7b9504266349cedc5426"></a>

### [`00a1ddb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1d/00a1ddb0.md) → [`00a1ddf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1d/00a1ddf4.md) FUN_00a1ddf4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1ddd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1ddd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a1de18"
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
      "unmatched:00a1ddd4",
      "DATA",
      [
        "storage",
        "00c0c090",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a1ddd8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a1dddc",
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
      "00a1de18",
      "DATA",
      [
        "storage",
        "00c0c0e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00a1de1c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a1de20",
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

- 旧版 [`00a1ddd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1d/00a1ddb0.md#insn-00a1ddd4) · [`00a1dde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1d/00a1ddb0.md#insn-00a1dde0)
- 新版 [`00a1de18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1d/00a1ddf4.md#insn-00a1de18)

~~~diff
- 00a1ddd4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a1ddd4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a1ddd4 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a1ddd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a1ddd4 bytes 082400a9
- 00a1dde0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a1dde0 ["RETURN", null, ["register:0:8"]]
- 00a1dde0 bytes c0035fd6
+ 00a1de18 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a1de18 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a1de18 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00a1de18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a1de18 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a768844de872cd750a7a8c3b21400da6"></a>

### [`00a1dde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1d/00a1dde4.md) → [`00a1de28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1d/00a1de28.md) FUN_00a1de28

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1ddf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1ddf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a1de34"
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
      "unmatched:00a1ddf0",
      "DATA",
      [
        "storage",
        "00c0c090",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a1de34",
      "DATA",
      [
        "storage",
        "00c0c0e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a1ddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1d/00a1dde4.md#insn-00a1ddf0) · [`00a1ddf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1d/00a1dde4.md#insn-00a1ddf4)
- 新版 [`00a1de34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1d/00a1de28.md#insn-00a1de34)

~~~diff
- 00a1ddf0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a1ddf0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a1ddf0 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00a1ddf0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a1ddf0 bytes 292000a9
- 00a1ddf4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a1ddf4 ["RETURN", null, ["register:0:8"]]
- 00a1ddf4 bytes c0035fd6
+ 00a1de34 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00a1de34 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00a1de34 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00a1de34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a1de34 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de80cb275b448c82da65a8da43556b61"></a>

### [`00a1e088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e088.md) → [`00a1e0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1e/00a1e0cc.md) FUN_00a1e0cc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1e088"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1e088"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1e0a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a1e088",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a1e094",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb040"
      ]
    ],
    [
      "unmatched:00a1e0a0",
      "DATA",
      [
        "storage",
        "00c0c100",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a1e0cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a1e0d8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb040"
      ]
    ],
    [
      "00a1e0e4",
      "DATA",
      [
        "storage",
        "00c0c150",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a1e088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e088.md#insn-00a1e088) · [`00a1e094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e088.md#insn-00a1e094) · [`00a1e0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e088.md#insn-00a1e0a0)

~~~diff
- 00a1e088 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a1e088 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a1e088 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00a1e088 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a1e088 bytes fd7bbfa9
- 00a1e094 ["INT_ADD", "register:40f0:8", ["const:a1e094:8", "const:4:8"]]
- 00a1e094 ["CALL", null, ["callee:00bdb040:8"]]
- 00a1e094 bytes d7f30694
- 00a1e0a0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00a1e0a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a1e0a0 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dbc9bf9a5f4b3831db820ceac1b1df3"></a>

### [`00a1e108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e108.md) → [`00a1e14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1e/00a1e14c.md) FUN_00a1e14c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1e12c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1e12c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a1e170"
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
      "unmatched:00a1e12c",
      "DATA",
      [
        "storage",
        "00c0c190",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a1e130",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a1e134",
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
      "00a1e170",
      "DATA",
      [
        "storage",
        "00c0c1e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00a1e174",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a1e178",
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

- 旧版 [`00a1e12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e108.md#insn-00a1e12c) · [`00a1e138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e108.md#insn-00a1e138)
- 新版 [`00a1e170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1e/00a1e14c.md#insn-00a1e170)

~~~diff
- 00a1e12c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a1e12c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a1e12c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a1e12c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a1e12c bytes 082400a9
- 00a1e138 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a1e138 ["RETURN", null, ["register:0:8"]]
- 00a1e138 bytes c0035fd6
+ 00a1e170 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a1e170 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a1e170 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00a1e170 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a1e170 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c639b3ec12bbabf19909ca8bb6e2dd4b"></a>

### [`00a1e13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e13c.md) → [`00a1e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1e/00a1e180.md) FUN_00a1e180

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1e148"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1e148"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a1e18c"
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
      "unmatched:00a1e148",
      "DATA",
      [
        "storage",
        "00c0c190",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a1e18c",
      "DATA",
      [
        "storage",
        "00c0c1e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a1e148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e13c.md#insn-00a1e148) · [`00a1e14c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e13c.md#insn-00a1e14c)
- 新版 [`00a1e18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1e/00a1e180.md#insn-00a1e18c)

~~~diff
- 00a1e148 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a1e148 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a1e148 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00a1e148 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a1e148 bytes 292000a9
- 00a1e14c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a1e14c ["RETURN", null, ["register:0:8"]]
- 00a1e14c bytes c0035fd6
+ 00a1e18c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00a1e18c ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00a1e18c ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00a1e18c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a1e18c bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ac065cf598f488498ae36356a60339c"></a>

### [`00a1e158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e158.md) → [`00a1e19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1e/00a1e19c.md) FUN_00a1e19c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00883cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883cc0.md) [`009e97a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e97a0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00883cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883cc0.md) [`009e97e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e97e4.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a1e170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e158.md#insn-00a1e170) · [`00a1e18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e158.md#insn-00a1e18c) · [`00a1e1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e158.md#insn-00a1e1b0)
- 新版 [`00a1e1b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1e/00a1e19c.md#insn-00a1e1b4) · [`00a1e1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1e/00a1e19c.md#insn-00a1e1d0) · [`00a1e1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1e/00a1e19c.md#insn-00a1e1f4)

~~~diff
- 00a1e170 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 00a1e1b4 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00a1e170 bytes 40040054
+ 00a1e1b4 bytes 40040054
- 00a1e18c ["INT_ADD", "register:40f0:8", ["const:a1e18c:8", "const:4:8"]]
- 00a1e18c ["CALL", null, ["ram:457e1c:8"]]
+ 00a1e1d0 ["INT_ADD", "register:40f0:8", ["const:a1e1d0:8", "const:4:8"]]
+ 00a1e1d0 ["CALL", null, ["ram:457e1c:8"]]
- 00a1e18c bytes 24e7e897
+ 00a1e1d0 bytes 13e7e897
- 00a1e1b0 ["INT_ADD", "register:40f0:8", ["const:a1e1b0:8", "const:4:8"]]
- 00a1e1b0 ["CALL", null, ["ram:457e1c:8"]]
+ 00a1e1f4 ["INT_ADD", "register:40f0:8", ["const:a1e1f4:8", "const:4:8"]]
+ 00a1e1f4 ["CALL", null, ["ram:457e1c:8"]]
- 00a1e1b0 bytes 1be7e897
+ 00a1e1f4 bytes 0ae7e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9156029bccb8a6be62c80c781fedb724"></a>

### [`00a1e250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e250.md) → [`00a1e294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1e/00a1e294.md) FUN_00a1e294

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.85% / 新版 53.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1e274"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1e274"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a1e2b8"
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
      "unmatched:00a1e274",
      "DATA",
      [
        "storage",
        "00c0c210",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a1e278",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a1e27c",
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
      "00a1e2b8",
      "DATA",
      [
        "storage",
        "00c0c260",
        null,
        "undefined *"
      ]
    ],
    [
      "00a1e2bc",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a1e2c0",
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

- 旧版 [`00a1e274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e250.md#insn-00a1e274) · [`00a1e280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e250.md#insn-00a1e280)
- 新版 [`00a1e2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1e/00a1e294.md#insn-00a1e2b8)

~~~diff
- 00a1e274 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a1e274 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a1e274 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a1e274 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a1e274 bytes 082400a9
- 00a1e280 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a1e280 ["RETURN", null, ["register:0:8"]]
- 00a1e280 bytes c0035fd6
+ 00a1e2b8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a1e2b8 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a1e2b8 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00a1e2b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a1e2b8 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f06bad23dcf5768d762871f6c7d8823d"></a>

### [`00a1e284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e284.md) → [`00a1e2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1e/00a1e2c8.md) FUN_00a1e2c8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1e290"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1e290"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a1e2d4"
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
      "unmatched:00a1e290",
      "DATA",
      [
        "storage",
        "00c0c210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a1e2d4",
      "DATA",
      [
        "storage",
        "00c0c260",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a1e290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e284.md#insn-00a1e290) · [`00a1e294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e284.md#insn-00a1e294)
- 新版 [`00a1e2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1e/00a1e2c8.md#insn-00a1e2d4)

~~~diff
- 00a1e290 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a1e290 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a1e290 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00a1e290 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a1e290 bytes 292000a9
- 00a1e294 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a1e294 ["RETURN", null, ["register:0:8"]]
- 00a1e294 bytes c0035fd6
+ 00a1e2d4 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00a1e2d4 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00a1e2d4 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00a1e2d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a1e2d4 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fecad9e9c4048313cdd4b3debafdf1aa"></a>

### [`00a1fcf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fcf4.md) → [`00a1fd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1f/00a1fd38.md) FUN_00a1fd38

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1fd18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1fd18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a1fd5c"
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
      "unmatched:00a1fd18",
      "DATA",
      [
        "storage",
        "00c0c330",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a1fd1c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a1fd20",
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
      "00a1fd5c",
      "DATA",
      [
        "storage",
        "00c0c380",
        null,
        "undefined *"
      ]
    ],
    [
      "00a1fd60",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a1fd64",
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

- 旧版 [`00a1fd18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fcf4.md#insn-00a1fd18) · [`00a1fd24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fcf4.md#insn-00a1fd24)
- 新版 [`00a1fd5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1f/00a1fd38.md#insn-00a1fd5c)

~~~diff
- 00a1fd18 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a1fd18 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a1fd18 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a1fd18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a1fd18 bytes 082400a9
- 00a1fd24 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a1fd24 ["RETURN", null, ["register:0:8"]]
- 00a1fd24 bytes c0035fd6
+ 00a1fd5c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a1fd5c ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a1fd5c ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00a1fd5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a1fd5c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c21350ae15f5eef8987a012fd0f813f"></a>

### [`00a1fda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fda8.md) → [`00a1fdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1f/00a1fdec.md) FUN_00a1fdec

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1fda8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1fda8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1fdac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a1fda8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a1fdac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a1fdcc",
      "DATA",
      [
        "storage",
        "00c0c3b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a1fdec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a1fdf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a1fe10",
      "DATA",
      [
        "storage",
        "00c0c400",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a1fda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fda8.md#insn-00a1fda8) · [`00a1fdac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fda8.md#insn-00a1fdac) · [`00a1fdcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fda8.md#insn-00a1fdcc)

~~~diff
- 00a1fda8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a1fda8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a1fda8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a1fda8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a1fda8 bytes fd7bbea9
- 00a1fdac ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a1fdac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00a1fdac bytes f30b00f9
- 00a1fdcc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a1fdcc ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a1fdcc ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a1fdcc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a1fdcc bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30ca7e14f0344ebc6c17a718b5639d0f"></a>

### [`00a203c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a203c8.md) → [`00a2040c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a2040c.md) FUN_00a2040c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a203e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a20424"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00a203e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a203e0",
      "DATA",
      [
        "storage",
        "00c0c520",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a203e4",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a20424",
      "DATA",
      [
        "storage",
        "00c0c570",
        null,
        "undefined *"
      ]
    ],
    [
      "00a20428",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a203e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a203c8.md#insn-00a203e0) · [`00a203e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a203c8.md#insn-00a203e8)
- 新版 [`00a20424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a2040c.md#insn-00a20424)

~~~diff
- 00a203e0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00a203e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a203e0 bytes 080000f9
- 00a203e8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a203e8 ["RETURN", null, ["register:0:8"]]
- 00a203e8 bytes c0035fd6
+ 00a20424 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00a20424 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00a20424 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fed839c56e4608a26dfb16ef4177a01"></a>

### [`00a20448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20448.md) → [`00a2048c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a2048c.md) FUN_00a2048c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a20448"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a20448"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2044c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a20448",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2044c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2046c",
      "DATA",
      [
        "storage",
        "00c0c5b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a2048c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a20490",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a204b0",
      "DATA",
      [
        "storage",
        "00c0c600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a20448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20448.md#insn-00a20448) · [`00a2044c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20448.md#insn-00a2044c) · [`00a2046c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20448.md#insn-00a2046c)

~~~diff
- 00a20448 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a20448 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a20448 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a20448 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a20448 bytes fd7bbea9
- 00a2044c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a2044c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00a2044c bytes f30b00f9
- 00a2046c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a2046c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a2046c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a2046c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a2046c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c05f53ede6d2b1c03252bd1a1259711"></a>

### [`00a2047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a2047c.md) → [`00a204c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a204c0.md) FUN_00a204c0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a20488"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a20488"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a204cc"
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
      "unmatched:00a20488",
      "DATA",
      [
        "storage",
        "00c0c5b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a204cc",
      "DATA",
      [
        "storage",
        "00c0c600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a20488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a2047c.md#insn-00a20488) · [`00a2048c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a2047c.md#insn-00a2048c)
- 新版 [`00a204cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a204c0.md#insn-00a204cc)

~~~diff
- 00a20488 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a20488 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a20488 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00a20488 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a20488 bytes 292000a9
- 00a2048c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a2048c ["RETURN", null, ["register:0:8"]]
- 00a2048c bytes c0035fd6
+ 00a204cc ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00a204cc ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00a204cc ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00a204cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a204cc bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e1ad8baef1ea021dd6740facdde68b7"></a>

### [`00a20590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20590.md) → [`00a205d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a205d4.md) FUN_00a205d4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a205b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a205b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a205f8"
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
      "unmatched:00a205b4",
      "DATA",
      [
        "storage",
        "00c0c630",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a205b8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a205bc",
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
      "00a205f8",
      "DATA",
      [
        "storage",
        "00c0c680",
        null,
        "undefined *"
      ]
    ],
    [
      "00a205fc",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a20600",
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

- 旧版 [`00a205b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20590.md#insn-00a205b4) · [`00a205c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20590.md#insn-00a205c0)
- 新版 [`00a205f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a205d4.md#insn-00a205f8)

~~~diff
- 00a205b4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a205b4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a205b4 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a205b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a205b4 bytes 082400a9
- 00a205c0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a205c0 ["RETURN", null, ["register:0:8"]]
- 00a205c0 bytes c0035fd6
+ 00a205f8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a205f8 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a205f8 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00a205f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a205f8 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18b76f7c9ef1e8785730bd3475cabdfc"></a>

### [`00a20a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20a54.md) → [`00a20a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20a98.md) FUN_00a20a98

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00a144c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a14/00a144c8.md) [`00a20a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20a54.md) [`00a20d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20d94.md) · 呼出先 4件 [`007dcb28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dc/007dcb28.md) [`00a20a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20a54.md) [`00a20d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20d94.md) [`00a21094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21094.md)
- 新版 呼出元 3件 [`00a1450c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a14/00a1450c.md) [`00a20a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20a98.md) [`00a20dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20dd8.md) · 呼出先 4件 [`007dcb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dc/007dcb28.md) [`00a20a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20a98.md) [`00a20dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20dd8.md) [`00a210d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a210d8.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 90.62% / 新版 90.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a20d80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a20d80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a20dc4"
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
      "unmatched:00a20d84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a20db0"
      ]
    ],
    [
      "unmatched:00a20d8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a20d7c"
      ]
    ]
  ],
  "added": [
    [
      "00a20dc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a20db0"
      ]
    ],
    [
      "00a20dd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a20d7c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a20d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20a54.md#insn-00a20d80) · [`00a20d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20a54.md#insn-00a20d84) · [`00a20d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20a54.md#insn-00a20d8c)

~~~diff
- 00a20d80 ["COPY", "tmp:0:8", ["register:4078:8"]]
- 00a20d80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a20d80 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00a20d80 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00a20d80 bytes e00500ad
- 00a20d84 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a20d84 ["CBRANCH", null, ["local:b37:8", "tmp:0:1"]]
- 00a20d84 bytes 41ffff54
- 00a20d8c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a20d8c ["CBRANCH", null, ["local:b34:8", "tmp:0:1"]]
- 00a20d8c bytes 61fdff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-239a1ad06dec20327cbecb9f8bfa7417"></a>

### [`00a21720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21720.md) → [`00a21764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a21764.md) FUN_00a21764

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2172c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2172c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a21770"
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
      "unmatched:00a2172c",
      "DATA",
      [
        "storage",
        "00c0c7b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a21770",
      "DATA",
      [
        "storage",
        "00c0c800",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a2172c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21720.md#insn-00a2172c) · [`00a21730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21720.md#insn-00a21730)
- 新版 [`00a21770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a21764.md#insn-00a21770)

~~~diff
- 00a2172c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a2172c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a2172c ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00a2172c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a2172c bytes 292000a9
- 00a21730 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a21730 ["RETURN", null, ["register:0:8"]]
- 00a21730 bytes c0035fd6
+ 00a21770 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00a21770 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00a21770 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00a21770 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a21770 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61c10a3aa9cd3d0450da8ff98f28cb32"></a>

### [`00a21bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21bc4.md) → [`00a21c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a21c08.md) FUN_00a21c08

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a21768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21768.md) · 呼出先 2件 [`00a21768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21768.md) [`00a21ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21ae4.md)
- 新版 呼出元 1件 [`00a217ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a217ac.md) · 呼出先 2件 [`00a217ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a217ac.md) [`00a21b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a21b28.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.02% / 新版 92.02%

CFGの説明率　旧版 72.06% / 新版 72.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a21e00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a21e00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a21e44"
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
      "unmatched:00a21d98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a21d98"
      ]
    ],
    [
      "unmatched:00a21db4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a21e58"
      ]
    ],
    [
      "unmatched:00a21dc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a21e58"
      ]
    ]
  ],
  "added": [
    [
      "00a21ddc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a21d98"
      ]
    ],
    [
      "00a21df8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a21e58"
      ]
    ],
    [
      "00a21e08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a21e58"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a21d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21bc4.md#insn-00a21d98) · [`00a21db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21bc4.md#insn-00a21db4) · [`00a21dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21bc4.md#insn-00a21dc4)

~~~diff
- 00a21d98 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a21d98 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 00a21d98 bytes e1fdff54
- 00a21db4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00a21db4 ["CBRANCH", null, ["local:b31:8", "tmp:0:1"]]
- 00a21db4 bytes 03030054
- 00a21dc4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00a21dc4 ["CBRANCH", null, ["local:b31:8", "tmp:0:1"]]
- 00a21dc4 bytes 83020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02777346468bffa3cb60c3127c9c2c4d"></a>

### [`00a22848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a22/00a22848.md) → [`00a2288c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a22/00a2288c.md) FUN_00a2288c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a22568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a22/00a22568.md) · 呼出先 1件 [`00a22568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a22/00a22568.md)
- 新版 呼出元 1件 [`00a225ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a22/00a225ac.md) · 呼出先 1件 [`00a225ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a22/00a225ac.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.71% / 新版 94.71%

CFGの説明率　旧版 81.54% / 新版 79.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a22adc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a22adc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a22b20"
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
      "unmatched:00a22aa0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a22ad8"
      ]
    ],
    [
      "unmatched:00a22ae0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a22b0c"
      ]
    ],
    [
      "unmatched:00a22aec",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00a228d8"
      ]
    ]
  ],
  "added": [
    [
      "00a22ae4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a22ad8"
      ]
    ],
    [
      "00a22b24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a22b0c"
      ]
    ],
    [
      "00a22b30",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00a228d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a22aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a22/00a22848.md#insn-00a22aa0) · [`00a22adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a22/00a22848.md#insn-00a22adc) · [`00a22ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a22/00a22848.md#insn-00a22ae0)

~~~diff
- 00a22aa0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a22aa0 ["CBRANCH", null, ["local:b34:8", "tmp:0:1"]]
- 00a22aa0 bytes a1ffff54
- 00a22adc ["COPY", "tmp:0:8", ["register:4080:8"]]
- 00a22adc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a22adc ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00a22adc ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00a22adc bytes 000600ad
- 00a22ae0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a22ae0 ["CBRANCH", null, ["local:b38:8", "tmp:0:1"]]
- 00a22ae0 bytes 41ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c6ef3a0aab64fcaa44f14250359c07b"></a>

### [`00a230d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a230d0.md) → [`00a23114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a23/00a23114.md) FUN_00a23114

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a230f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a230f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a23138"
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
      "unmatched:00a230f4",
      "DATA",
      [
        "storage",
        "00c0c830",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a230f8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a230fc",
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
      "00a23138",
      "DATA",
      [
        "storage",
        "00c0c880",
        null,
        "undefined *"
      ]
    ],
    [
      "00a2313c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a23140",
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

- 旧版 [`00a230f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a230d0.md#insn-00a230f4) · [`00a23100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a230d0.md#insn-00a23100)
- 新版 [`00a23138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a23/00a23114.md#insn-00a23138)

~~~diff
- 00a230f4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a230f4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a230f4 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a230f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a230f4 bytes 082400a9
- 00a23100 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a23100 ["RETURN", null, ["register:0:8"]]
- 00a23100 bytes c0035fd6
+ 00a23138 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a23138 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a23138 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00a23138 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a23138 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc3db9c41edfd92ac1f82e7ad9e9a329"></a>

### [`00a23104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a23104.md) → [`00a23148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a23/00a23148.md) FUN_00a23148

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a23110"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a23110"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a23154"
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
      "unmatched:00a23110",
      "DATA",
      [
        "storage",
        "00c0c830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a23154",
      "DATA",
      [
        "storage",
        "00c0c880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a23110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a23104.md#insn-00a23110) · [`00a23114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a23104.md#insn-00a23114)
- 新版 [`00a23154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a23/00a23148.md#insn-00a23154)

~~~diff
- 00a23110 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a23110 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a23110 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00a23110 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a23110 bytes 292000a9
- 00a23114 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a23114 ["RETURN", null, ["register:0:8"]]
- 00a23114 bytes c0035fd6
+ 00a23154 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00a23154 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00a23154 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00a23154 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a23154 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c097ca60f0b672221d97767afb691e0"></a>

### [`00a25380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a25380.md) → [`00a253c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a25/00a253c4.md) FUN_00a253c4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 56件 [`005a2308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a2/005a2308.md) [`005a45f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a4/005a45f4.md) [`005e1a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md) [`00604cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/00604cfc.md) [`006062a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00606/006062a4.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00a2386c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a2386c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 56件 [`005a2308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a2/005a2308.md) [`005a45f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md) [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`00604cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604cfc.md) [`006062a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00606/006062a4.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00a238b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a23/00a238b0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 82.28% / 新版 82.28%

CFGの説明率　旧版 17.86% / 新版 18.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a253b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a253cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a253d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a253b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a25478"
      ]
    ],
    [
      "unmatched:00a253d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a25404"
      ]
    ],
    [
      "unmatched:00a2540c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2547c"
      ]
    ]
  ],
  "added": [
    [
      "00a253f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a25478"
      ]
    ],
    [
      "00a25418",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a25404"
      ]
    ],
    [
      "00a25450",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2547c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a25380.md#insn-00a253b4) · [`00a253cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a25380.md#insn-00a253cc) · [`00a253d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a25380.md#insn-00a253d4)

~~~diff
- 00a253b4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a253b4 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 00a253b4 bytes 080400b4
- 00a253cc ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a253cc ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a253cc ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00a253cc ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00a253cc bytes 29b18a9a
- 00a253d4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00a253d4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00a253d4 bytes 6affffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2413f2b153b4ad338eb870317b5838c2"></a>

### [`00a25630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a25630.md) → [`00a25674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a25/00a25674.md) FUN_00a25674

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006369bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00636/006369bc.md) [`00637320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00637/00637320.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 2件 [`006369bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00636/006369bc.md) [`00637320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00637/00637320.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 40.74% / 新版 40.74%

CFGの説明率　旧版 14.61% / 新版 14.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 74件, `unresolved_call_alignment` 25件, `unresolved_store_alignment` 123件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a25644"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a25644"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a25648"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a25644",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a25648",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2564c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a25688",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a2568c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a25690",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a25644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a25630.md#insn-00a25644) · [`00a25648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a25630.md#insn-00a25648) · [`00a2564c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a25630.md#insn-00a2564c)

~~~diff
- 00a25644 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00a25644 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00a25644 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00a25644 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a25644 bytes f85f05a9
- 00a25648 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a25648 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a25648 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00a25648 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a25648 bytes f65706a9
- 00a2564c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a2564c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a2564c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00a2564c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a2564c bytes f44f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2baf32c909f3d8526ffc2dc0c6c2749c"></a>

### [`00a26c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26c9c.md) → [`00a26ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26ce0.md) FUN_00a26ce0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 62.50% / 新版 62.50%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00a26cb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00a26cfc"
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
      "unmatched:00a26cb0",
      "DATA",
      [
        "storage",
        "00334010",
        null,
        "byte[39]"
      ]
    ],
    [
      "unmatched:00a26cb4",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a26cf4",
      "DATA",
      [
        "storage",
        "00334010",
        null,
        "byte[39]"
      ]
    ],
    [
      "00a26cf8",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a26cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26c9c.md#insn-00a26cb8) · [`00a26ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26c9c.md#insn-00a26ca4)
- 新版 [`00a26cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26ce0.md#insn-00a26cfc) · [`00a26ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26ce0.md#insn-00a26ce8)

~~~diff
- 00a26cb8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a26cb8 ["RETURN", null, ["register:0:8"]]
- 00a26cb8 bytes c0035fd6
+ 00a26cfc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00a26cfc ["RETURN", null, ["register:0:8"]]
+ 00a26cfc bytes c0035fd6
- 00a26ca4 ["INT_ADD", "register:40f0:8", ["const:a26ca4:8", "const:4:8"]]
- 00a26ca4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a26ce8 ["INT_ADD", "register:40f0:8", ["const:a26ce8:8", "const:4:8"]]
+ 00a26ce8 ["CALL", null, ["callee:0081f580:8"]]
- 00a26ca4 bytes 37e2f797
+ 00a26ce8 bytes 26e2f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40ddcbf033ad8d99d4b22637d699a314"></a>

### [`00a26d14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26d14.md) → [`00a26d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26d58.md) FUN_00a26d58

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md) · 呼出先 1件 [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md)
- 新版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) · 呼出先 1件 [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_store_alignment

命令の説明率　旧版 78.12% / 新版 78.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_destination` 3件, `store_value` 3件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a26d18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a26d1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a26d1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a26d18",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a26d1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a26d5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a26d60",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a26d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26d14.md#insn-00a26d18) · [`00a26d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26d14.md#insn-00a26d1c) · [`00a26d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26d14.md#insn-00a26d38)

~~~diff
- 00a26d18 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a26d18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00a26d18 bytes f50b00f9
- 00a26d1c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a26d1c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a26d1c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a26d1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a26d1c bytes f44f02a9
- 00a26d38 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00a26d38 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00a26d38 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:88:8"]]
- 00a26d38 ["STORE", null, ["const:1b1:8", "register:4040:8", "tmp:1:8"]]
- 00a26d38 bytes 1f8d08f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-febaedcd227345cc6bbf15425716853d"></a>

### [`00a28640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28640.md) → [`00a28684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28684.md) FUN_00a28684

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a28744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28744.md) · 呼出先 4件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a5b084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b084.md) [`00a5cd84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5cd84.md) [`00acfa94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfa94.md)
- 新版 呼出元 1件 [`00a28788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28788.md) · 呼出先 4件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a5b0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b0c8.md) [`00a5cdc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5cdc8.md) [`00acfad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfad8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 89.23% / 新版 89.23%

CFGの説明率　旧版 25.00% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00a28740"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00a28784"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a28740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28640.md#insn-00a28740) · [`00a28654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28640.md#insn-00a28654)
- 新版 [`00a28784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28684.md#insn-00a28784) · [`00a28698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28684.md#insn-00a28698)

~~~diff
- 00a28740 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a28740 ["RETURN", null, ["register:0:8"]]
- 00a28740 bytes c0035fd6
+ 00a28784 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00a28784 ["RETURN", null, ["register:0:8"]]
+ 00a28784 bytes c0035fd6
- 00a28654 ["INT_ADD", "register:40f0:8", ["const:a28654:8", "const:4:8"]]
- 00a28654 ["CALL", null, ["callee:0081f580:8"]]
+ 00a28698 ["INT_ADD", "register:40f0:8", ["const:a28698:8", "const:4:8"]]
+ 00a28698 ["CALL", null, ["callee:0081f580:8"]]
- 00a28654 bytes cbdbf797
+ 00a28698 bytes badbf797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1e9aa90ef11fbcfbe53d36a201fc29b"></a>

### [`00a294a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a294a0.md) → [`00a294e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a294e4.md) FUN_00a294e4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a293b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a293b0.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00a293f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a293f4.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 14.29% / 新版 8.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a294b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a294f8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00a294e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a294b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a29524"
      ]
    ]
  ],
  "added": [
    [
      "00a294f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a29524"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a294b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a294a0.md#insn-00a294b4) · [`00a294e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a294a0.md#insn-00a294e8)
- 新版 [`00a294f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a294e4.md#insn-00a294f8)

~~~diff
- 00a294b4 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00a294b4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00a294b4 bytes 730100b4
- 00a294e8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a294e8 ["RETURN", null, ["register:0:8"]]
- 00a294e8 bytes c0035fd6
+ 00a294f8 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00a294f8 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00a294f8 bytes 730100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

