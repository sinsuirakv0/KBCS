# v15.7.2 → v15.7.3 · 命令位置の検査未完了 (1)

[一覧の目次](README.md)

<a id="compare-5c1fc13abbd0ec834d77b4cbf5bf0bfb"></a>

### [`0044a8e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a8e8.md) → [`0044a8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8e8.md) FUN_0044a8e8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`0044a8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a8d8.md) [`009a6228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009a6/009a6228.md) [`009a6234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009a6/009a6234.md) [`009a6240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009a6/009a6240.md) [`009a9ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009a9/009a9ce0.md) · 呼出先 7件 [`0044ac28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044ac28.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb460.md)
- 新版 呼出元 5件 [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`009a6228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a6/009a6228.md) [`009a6234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a6/009a6234.md) [`009a6240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a6/009a6240.md) [`009a9ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a9/009a9ce0.md) · 呼出先 7件 [`0044ac28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac28.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb500.md) [`00bdb510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb510.md)

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
        "002a8135",
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
        "002a80a1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044a934`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a8e8.md#insn-0044a934) · [`0044a938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a8e8.md#insn-0044a938)
- 新版 `0044a934`（命令位置の公開資料なし） · `0044a938`（命令位置の公開資料なし）

~~~diff
- 0044a934 ["COPY", "tmp:0:8", ["const:135:8"]]
- 0044a934 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044a934 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044a934 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044a934 ["COPY", "tmp:0:8", ["const:a1:8"]]
+ 0044a934 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044a934 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044a934 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044a934 bytes 08d50491
+ 0044a934 bytes 08850291
- 0044a938 ["COPY", "register:4048:8", ["const:2b2000:8"]]
- 0044a938 bytes 49f3ff90
+ 0044a938 ["COPY", "register:4048:8", ["const:2b2000:8"]]
+ 0044a938 bytes 49f3ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf47e6777f54e369d2c7887d74a13a34"></a>

### [`004532cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00453/004532cc.md) → [`004532cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00453/004532cc.md) FUN_004532cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00452ec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00452/00452ec8.md) · 呼出先 11件 [`004512c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00451/004512c0.md) [`004537f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00453/004537f0.md) [`00453c78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00453/00453c78.md) [`00454af4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00454/00454af4.md) [`00454f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00454/00454f34.md)
- 新版 呼出元 1件 [`00452ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00452/00452ec8.md) · 呼出先 11件 [`004512c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00451/004512c0.md) [`004537f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00453/004537f0.md) [`00453c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00453/00453c78.md) [`00454af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00454/00454af4.md) [`00454f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00454/00454f34.md)

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
        "0029f2c8",
        null,
        "string"
      ]
    ],
    [
      "00453420",
      "READ",
      [
        "storage",
        "0029f2d2",
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
  ],
  "added": [
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00453338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00453/004532cc.md#insn-00453338) · [`0045333c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00453/004532cc.md#insn-0045333c)
- 新版 `00453338`（命令位置の公開資料なし） · `0045333c`（命令位置の公開資料なし）

~~~diff
- 00453338 ["COPY", "tmp:0:8", ["const:2c8:8"]]
- 00453338 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 00453338 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 00453338 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 00453338 ["COPY", "tmp:0:8", ["const:355:8"]]
+ 00453338 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 00453338 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 00453338 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 00453338 bytes 39230b91
+ 00453338 bytes 39570d91
- 0045333c ["COPY", "register:40a0:8", ["const:297000:8"]]
- 0045333c bytes 34f2ff90
+ 0045333c ["COPY", "register:40a0:8", ["const:297000:8"]]
+ 0045333c bytes 34f2ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bde0628df98735d53e0f676608fac78"></a>

### [`0046a3a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046a/0046a3a8.md) → [`0046a3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046a3a8.md) FUN_0046a3a8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00829180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00829/00829180.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00829180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829180.md) · 呼出先 0件 

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
        "00c24cc8",
        null,
        "undefined4"
      ]
    ],
    [
      "0046a3bc",
      "READ",
      [
        "storage",
        "00c24cb8",
        null,
        "undefined4"
      ]
    ],
    [
      "0046a3c8",
      "READ",
      [
        "storage",
        "00c24ccc",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046a3ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046a/0046a3a8.md#insn-0046a3ac) · [`0046a3b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046a/0046a3a8.md#insn-0046a3b8)
- 新版 `0046a3ac`（命令位置の公開資料なし） · `0046a3b8`（命令位置の公開資料なし）

~~~diff
- 0046a3ac ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 0046a3ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046a3ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046a3ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046a3ac ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 0046a3ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046a3ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046a3ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046a3ac bytes 08c13291
+ 0046a3ac bytes 08c13591
- 0046a3b8 ["INT_MULT", "tmp:0:4", ["register:4050:4", "register:4048:4"]]
- 0046a3b8 ["INT_ZEXT", "register:4048:8", ["tmp:0:4"]]
- 0046a3b8 bytes 497d091b
+ 0046a3b8 ["INT_MULT", "tmp:0:4", ["register:4050:4", "register:4048:4"]]
+ 0046a3b8 ["INT_ZEXT", "register:4048:8", ["tmp:0:4"]]
+ 0046a3b8 bytes 497d091b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c2490d44a2e3424b34ee1d1bed0020e"></a>

### [`00470c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470c54.md) → [`00470c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470c54.md) FUN_00470c54

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00906b9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00906/00906b9c.md) · 呼出先 3件 [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6a0.md) [`00bdb6b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6b0.md)
- 新版 呼出元 1件 [`00906b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md) · 呼出先 3件 [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb750.md) [`00bdb760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb760.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 88.00% / 新版 88.00%

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
        "0029f2f2",
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
        "0029f2ef",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00470cc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470c54.md#insn-00470cc8) · [`00470ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470c54.md#insn-00470ccc)
- 新版 `00470cc8`（命令位置の公開資料なし） · `00470ccc`（命令位置の公開資料なし）

~~~diff
- 00470cc8 ["COPY", "tmp:0:8", ["const:2ef:8"]]
- 00470cc8 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00470cc8 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00470cc8 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00470cc8 ["COPY", "tmp:0:8", ["const:37c:8"]]
+ 00470cc8 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00470cc8 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00470cc8 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00470cc8 bytes d6be0b91
+ 00470cc8 bytes d6f20d91
- 00470ccc ["COPY", "register:40b8:8", ["const:2ad000:8"]]
- 00470ccc bytes f7f1ffb0
+ 00470ccc ["COPY", "register:40b8:8", ["const:2ad000:8"]]
+ 00470ccc bytes f7f1ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52255c1ee6f8f25f149d2daede62c4ed"></a>

### [`005537fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005537fc.md) → [`005537fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005537fc.md) FUN_005537fc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052db28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db28.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0052db28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db28.md) · 呼出先 0件 

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
        "00c1ac80",
        null,
        "pointer"
      ]
    ],
    [
      "00553808",
      "READ",
      [
        "storage",
        "00c1ac88",
        null,
        "pointer"
      ]
    ],
    [
      "0055380c",
      "READ",
      [
        "storage",
        "00c2649c",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005537fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005537fc.md#insn-005537fc) · [`00553800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005537fc.md#insn-00553800)
- 新版 `005537fc`（命令位置の公開資料なし）

~~~diff
- 005537fc ["COPY", "register:4040:8", ["const:c1a000:8"]]
- 005537fc bytes 283600f0
+ 005537fc ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005537fc bytes 283600f0
- 00553800 ["COPY", "register:4048:8", ["const:c1a000:8"]]
- 00553800 bytes 293600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af87156be2279328bb106648661a5f31"></a>

### [`00562188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/00562188.md) → [`00562188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/00562188.md) FUN_00562188

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`0056233c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/0056233c.md) [`00564d7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564d7c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0056233c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/0056233c.md) [`00564d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564d7c.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

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
        "00bef910",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005621ec",
      "PARAM",
      [
        "storage",
        "00bef920",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005621c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/00562188.md#insn-005621c0) · [`005621c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/00562188.md#insn-005621c8)
- 新版 `005621c0`（命令位置の公開資料なし） · `005621c8`（命令位置の公開資料なし）

~~~diff
- 005621c0 ["COPY", "tmp:0:8", ["const:910:8"]]
- 005621c0 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 005621c0 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 005621c0 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 005621c0 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 005621c0 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 005621c0 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 005621c0 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 005621c0 bytes 94422491
+ 005621c0 bytes 94022791
- 005621c8 ["COPY", "register:40a8:8", ["const:bef000:8"]]
- 005621c8 bytes 753400b0
+ 005621c8 ["COPY", "register:40a8:8", ["const:bef000:8"]]
+ 005621c8 bytes 753400b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21273430dbed2f4f27aa74fcd3fff6c1"></a>

### [`0056b688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056b688.md) → [`0056b688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056b688.md) FUN_0056b688

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566968.md)

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
        "00299dbe",
        null,
        "string"
      ]
    ],
    [
      "0056b704",
      "READ",
      [
        "storage",
        "00299dce",
        null,
        "string"
      ]
    ],
    [
      "0056b718",
      "READ",
      [
        "storage",
        "00299dde",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b6fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056b688.md#insn-0056b6fc) · [`0056b700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056b688.md#insn-0056b700)
- 新版 `0056b6fc`（命令位置の公開資料なし） · `0056b700`（命令位置の公開資料なし）

~~~diff
- 0056b6fc ["COPY", "tmp:0:8", ["const:dbe:8"]]
- 0056b6fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056b6fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056b6fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056b6fc ["COPY", "tmp:0:8", ["const:e4b:8"]]
+ 0056b6fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b6fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b6fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056b6fc bytes 08f93691
+ 0056b6fc bytes 082d3991
- 0056b700 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0056b700 bytes 29eaffb0
+ 0056b700 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0056b700 bytes 29eaffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b2c881ee889312ec5334c3f05b6f9ac"></a>

### [`005bc0ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005bc/005bc0ac.md) → [`005bc0ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bc0ac.md) FUN_005bc0ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`006f5fe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006f5/006f5fe8.md) [`006f8ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006f8/006f8ac0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006f5fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f5/006f5fe8.md) [`006f8ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f8/006f8ac0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

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
        "0109c542",
        null,
        "undefined4"
      ]
    ],
    [
      "005bc0d4",
      "DATA",
      [
        "storage",
        "0109c545",
        null,
        "undefined1"
      ]
    ],
    [
      "005bc0d8",
      "DATA",
      [
        "storage",
        "0109c544",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bc0c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005bc/005bc0ac.md#insn-005bc0c8) · [`005bc0e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005bc/005bc0ac.md#insn-005bc0e0)
- 新版 `005bc0c8`（命令位置の公開資料なし） · `005bc0e0`（命令位置の公開資料なし）

~~~diff
- 005bc0c8 ["COPY", "tmp:0:8", ["const:540:8"]]
- 005bc0c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005bc0c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005bc0c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005bc0c8 ["COPY", "tmp:0:8", ["const:600:8"]]
+ 005bc0c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005bc0c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005bc0c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005bc0c8 bytes 08011591
+ 005bc0c8 bytes 08011891
- 005bc0e0 ["INT_XOR", "tmp:0:4", ["register:4050:4", "register:4048:4"]]
- 005bc0e0 ["INT_ZEXT", "register:4048:8", ["tmp:0:4"]]
- 005bc0e0 bytes 4901094a
+ 005bc0e0 ["INT_XOR", "tmp:0:4", ["register:4050:4", "register:4048:4"]]
+ 005bc0e0 ["INT_ZEXT", "register:4048:8", ["tmp:0:4"]]
+ 005bc0e0 bytes 4901094a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9d8b8a106e854f9f3dd21d2af5e107b"></a>

### [`005c2f88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005c2/005c2f88.md) → [`005c2f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2f88.md) FUN_005c2f88

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`005c2ec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005c2/005c2ec0.md) [`005c2f30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005c2/005c2f30.md) [`005c3330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005c3/005c3330.md) [`006d6d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d6/006d6d04.md) [`009f4a74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009f4/009f4a74.md) · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`005bce08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005bc/005bce08.md) [`0063e4a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063e/0063e4a8.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`009019f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/009019f4.md)
- 新版 呼出元 5件 [`005c2ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2ec0.md) [`005c2f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2f30.md) [`005c3330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c3/005c3330.md) [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) [`009f4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f4/009f4a74.md) · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`005bce08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bce08.md) [`0063e4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e4a8.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`009019f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/009019f4.md)

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
        "002a1680",
        null,
        "string"
      ]
    ],
    [
      "005c3030",
      "READ",
      [
        "storage",
        "002a1690",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c3028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005c2/005c2f88.md#insn-005c3028) · [`005c302c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005c2/005c2f88.md#insn-005c302c)
- 新版 `005c3028`（命令位置の公開資料なし） · `005c302c`（命令位置の公開資料なし）

~~~diff
- 005c3028 ["COPY", "tmp:0:8", ["const:680:8"]]
- 005c3028 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005c3028 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005c3028 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005c3028 ["COPY", "tmp:0:8", ["const:70d:8"]]
+ 005c3028 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005c3028 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005c3028 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005c3028 bytes 4a011a91
+ 005c3028 bytes 4a351c91
- 005c302c ["COPY", "register:4040:8", ["const:2b1000:8"]]
- 005c302c bytes 68e7ffd0
+ 005c302c ["COPY", "register:4040:8", ["const:2b1000:8"]]
+ 005c302c bytes 68e7ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81d02dd669805631a7ca5dbbdcccddfd"></a>

### [`005c8a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005c8/005c8a6c.md) → [`005c8a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c8/005c8a6c.md) FUN_005c8a6c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`005c8548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005c8/005c8548.md) [`005cb0e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005cb/005cb0e0.md) [`006d6d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d6/006d6d04.md) [`006ddfb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006dd/006ddfb8.md) · 呼出先 4件 [`009019f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/009019f4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 4件 [`005c8548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c8/005c8548.md) [`005cb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cb/005cb0e0.md) [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) · 呼出先 4件 [`009019f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/009019f4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.67% / 新版 93.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005c8a9c",
      "READ",
      [
        "storage",
        "002aa7fb",
        null,
        "string"
      ]
    ],
    [
      "005c8b14",
      "READ",
      [
        "storage",
        "002a7717",
        null,
        "string"
      ]
    ],
    [
      "005c8b78",
      "READ",
      [
        "storage",
        "00c23fc0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "005c8a9c",
      "READ",
      [
        "storage",
        "002aa801",
        null,
        "string"
      ]
    ],
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
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c8a94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005c8/005c8a6c.md#insn-005c8a94) · [`005c8b00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005c8/005c8a6c.md#insn-005c8b00) · [`005c8b64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005c8/005c8a6c.md#insn-005c8b64)
- 新版 `005c8a94`（命令位置の公開資料なし） · `005c8b00`（命令位置の公開資料なし） · `005c8b64`（命令位置の公開資料なし）

~~~diff
- 005c8a94 ["COPY", "tmp:0:8", ["const:7fb:8"]]
- 005c8a94 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005c8a94 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005c8a94 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005c8a94 ["COPY", "tmp:0:8", ["const:801:8"]]
+ 005c8a94 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005c8a94 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005c8a94 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005c8a94 bytes 4aed1f91
+ 005c8a94 bytes 4a052091
- 005c8b00 ["COPY", "tmp:0:8", ["const:717:8"]]
- 005c8b00 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005c8b00 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005c8b00 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005c8b00 ["COPY", "tmp:0:8", ["const:683:8"]]
+ 005c8b00 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005c8b00 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005c8b00 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005c8b00 bytes 4a5d1c91
+ 005c8b00 bytes 4a0d1a91
- 005c8b64 ["COPY", "register:4040:8", ["const:c23000:8"]]
+ 005c8b64 ["COPY", "register:4040:8", ["const:c24000:8"]]
- 005c8b64 bytes c83200f0
+ 005c8b64 bytes e8320090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfa8634bb2f6c3abadd46798a582e4c9"></a>

### [`005d18a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005d1/005d18a4.md) → [`005d18a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d1/005d18a4.md) FUN_005d18a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005d0a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005d0/005d0a68.md) · 呼出先 10件 [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0058c05c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058c/0058c05c.md) [`005c2d18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005c2/005c2d18.md)
- 新版 呼出元 1件 [`005d0a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d0/005d0a68.md) · 呼出先 10件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0058c05c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058c/0058c05c.md) [`005c2d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2d18.md)

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
        "00c1b5b8",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d19a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005d1/005d18a4.md#insn-005d19a8) · [`005d19ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005d1/005d18a4.md#insn-005d19ac)
- 新版 `005d19a8`（命令位置の公開資料なし） · `005d19ac`（命令位置の公開資料なし）

~~~diff
- 005d19a8 ["COPY", "tmp:0:8", ["const:c77:8"]]
- 005d19a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005d19a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005d19a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005d19a8 ["COPY", "tmp:0:8", ["const:d04:8"]]
+ 005d19a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005d19a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005d19a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005d19a8 bytes 08dd3191
+ 005d19a8 bytes 08113491
- 005d19ac ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 005d19ac bytes e9e6fff0
+ 005d19ac ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 005d19ac bytes e9e6fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa9d3312a4535cea47bdf54dbbcaeece"></a>

### [`006f4518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006f4/006f4518.md) → [`006f4518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f4/006f4518.md) FUN_006f4518

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006f3154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006f3/006f3154.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00670f08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00670/00670f08.md) [`00adbf88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adbf88.md) [`00adc014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adc/00adc014.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`006f3154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f3/006f3154.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00670f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670f08.md) [`00adc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc050.md) [`00adc0dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc0dc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.74% / 新版 94.74%

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
      "006f4650",
      "PARAM",
      [
        "storage",
        "00294c62",
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
      "006f4650",
      "PARAM",
      [
        "storage",
        "00294cef",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006f45b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006f4/006f4518.md#insn-006f45b8) · [`006f45dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006f4/006f4518.md#insn-006f45dc)
- 新版 `006f45b8`（命令位置の公開資料なし） · `006f45dc`（命令位置の公開資料なし）

~~~diff
- 006f45b8 ["COPY", "tmp:0:8", ["const:c62:8"]]
- 006f45b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 006f45b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 006f45b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006f45b8 ["COPY", "tmp:0:8", ["const:cef:8"]]
+ 006f45b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006f45b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006f45b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 006f45b8 bytes 4a893191
+ 006f45b8 bytes 4abd3391
- 006f45dc ["COPY", "register:4048:8", ["const:293000:8"]]
- 006f45dc bytes e9dcfff0
+ 006f45dc ["COPY", "register:4048:8", ["const:293000:8"]]
+ 006f45dc bytes e9dcfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dcd8e382871ee713527dabf28f88535"></a>

### [`007cfd34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cfd34.md) → [`007cfd34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfd34.md) FUN_007cfd34

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`005d996c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005e0/005e02b0.md) [`006d6d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d6/006d6d04.md) [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) [`007acf88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ac/007acf88.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`0099697c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00996/0099697c.md) [`009969b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00996/009969b8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 6件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e0/005e02b0.md) [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`0099697c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00996/0099697c.md) [`009969b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00996/009969b8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
        "00c1b6d8",
        null,
        "pointer"
      ]
    ],
    [
      "007cfdf8",
      "DATA",
      [
        "storage",
        "00c2452c",
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

- 旧版 [`007cfdfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cfd34.md#insn-007cfdfc) · [`007cfdf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cfd34.md#insn-007cfdf4)
- 新版 `007cfdfc`（命令位置の公開資料なし） · `007cfdf4`（命令位置の公開資料なし）

~~~diff
- 007cfdfc ["INT_ADD", "register:40f0:8", ["const:7cfdfc:8", "const:4:8"]]
- 007cfdfc ["CALL", null, ["callee:0081f580:8"]]
- 007cfdfc bytes e13d0194
+ 007cfdfc ["INT_ADD", "register:40f0:8", ["const:7cfdfc:8", "const:4:8"]]
+ 007cfdfc ["CALL", null, ["callee:0081f580:8"]]
+ 007cfdfc bytes e13d0194
- 007cfdf4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6d8:8"]]
- 007cfdf4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 007cfdf4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:788:8"]]
+ 007cfdf4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 007cfdf4 bytes 296d43f9
+ 007cfdf4 bytes 29c543f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ee2124d2954faaa02becb4bdf149c1f"></a>

### [`007d1164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d1/007d1164.md) → [`007d1164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d1/007d1164.md) FUN_007d1164

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0075f8cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0075f/0075f8cc.md) [`00a3e5b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a3e/00a3e5b4.md) · 呼出先 3件 [`007cd2ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cd/007cd2ac.md) [`007d0e6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d0/007d0e6c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`0075f8cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075f/0075f8cc.md) [`00a3e5b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3e/00a3e5b4.md) · 呼出先 3件 [`007cd2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd2ac.md) [`007d0e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d0/007d0e6c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

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
        "00c27f98",
        null,
        "undefined8"
      ]
    ],
    [
      "007d12c0",
      "READ",
      [
        "storage",
        "00c27fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "007d1310",
      "READ",
      [
        "storage",
        "00c27fb0",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007d11b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d1/007d1164.md#insn-007d11b8) · [`007d11bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d1/007d1164.md#insn-007d11bc) · [`007d11c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d1/007d1164.md#insn-007d11c0)
- 新版 `007d11b8`（命令位置の公開資料なし） · `007d11bc`（命令位置の公開資料なし）

~~~diff
- 007d11b8 ["COPY", "register:40b8:8", ["const:c27000:8"]]
+ 007d11b8 ["COPY", "register:40b8:8", ["const:c28000:8"]]
- 007d11b8 bytes b72200d0
+ 007d11b8 bytes b72200f0
- 007d11bc ["COPY", "tmp:0:8", ["const:f98:8"]]
- 007d11bc ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 007d11bc ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 007d11bc ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 007d11bc ["COPY", "tmp:0:8", ["const:58:8"]]
+ 007d11bc ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 007d11bc ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 007d11bc ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 007d11bc bytes f7623e91
+ 007d11bc bytes f7620191
- 007d11c0 ["COPY", "register:40c0:8", ["const:1:8"]]
- 007d11c0 bytes 38008052
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb49f5bdd6a2317b01be0d73d6a6fd03"></a>

### [`0087308c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/0087308c.md) → [`0087308c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/0087308c.md) FUN_0087308c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fe2c.md) [`0051d884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d884.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0051d884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d884.md)

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
        "0029fb73",
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
  ],
  "added": [
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087311c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/0087308c.md#insn-0087311c) · [`00873120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/0087308c.md#insn-00873120)
- 新版 `0087311c`（命令位置の公開資料なし） · `00873120`（命令位置の公開資料なし）

~~~diff
- 0087311c ["COPY", "tmp:0:8", ["const:b73:8"]]
- 0087311c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087311c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087311c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087311c ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 0087311c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087311c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087311c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087311c bytes 08cd2d91
+ 0087311c bytes 08013091
- 00873120 ["COPY", "register:4048:8", ["const:294000:8"]]
- 00873120 bytes 09d1ffb0
+ 00873120 ["COPY", "register:4048:8", ["const:295000:8"]]
+ 00873120 bytes 09d1ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-083835292e8b1acd86e7fda29821c0a4"></a>

### [`009e9afc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009e9/009e9afc.md) → [`009e9afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e9afc.md) FUN_009e9afc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 30件 [`005a02e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a0/005a02e8.md) [`005a2308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a2/005a2308.md) [`005a3eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a3/005a3eb8.md) [`005a45f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a4/005a45f4.md) [`0062da7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0062d/0062da7c.md) · 呼出先 2件 [`009e9afc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009e9/009e9afc.md) [`00bdb6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6c0.md)
- 新版 呼出元 30件 [`005a02e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a0/005a02e8.md) [`005a2308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a2/005a2308.md) [`005a3eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a3/005a3eb8.md) [`005a45f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a4/005a45f4.md) [`0062da7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062da7c.md) · 呼出先 2件 [`009e9afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e9afc.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009e9b4c",
      "PARAM",
      [
        "storage",
        "00c0bc58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009e9b50",
      "PARAM",
      [
        "storage",
        "00c0bc68",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009e9b4c",
      "PARAM",
      [
        "storage",
        "00c0bd08",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009e9b50",
      "PARAM",
      [
        "storage",
        "00c0bd18",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e9b3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009e9/009e9afc.md#insn-009e9b3c) · [`009e9b40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009e9/009e9afc.md#insn-009e9b40)
- 新版 `009e9b3c`（命令位置の公開資料なし） · `009e9b40`（命令位置の公開資料なし）

~~~diff
- 009e9b3c ["COPY", "tmp:0:8", ["const:c58:8"]]
- 009e9b3c ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 009e9b3c ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 009e9b3c ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 009e9b3c ["COPY", "tmp:0:8", ["const:d08:8"]]
+ 009e9b3c ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 009e9b3c ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 009e9b3c ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 009e9b3c bytes f7623191
+ 009e9b3c bytes f7223491
- 009e9b40 ["COPY", "register:40c0:8", ["const:c0b000:8"]]
- 009e9b40 bytes 181100d0
+ 009e9b40 ["COPY", "register:40c0:8", ["const:c0b000:8"]]
+ 009e9b40 bytes 181100d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e604891c40ab06e41f81d7dc6e4676b0"></a>

### [`00abeec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00abe/00abeec0.md) → [`00abef88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abe/00abef88.md) FUN_00abef88

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00abe0c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00abe/00abe0c4.md) · 呼出先 3件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00abe18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abe/00abe18c.md) · 呼出先 3件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 84.85% / 新版 84.85%

CFGの説明率　旧版 42.86% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00abeee8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00abef18"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00abefb0"
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
      "unmatched:00abeee8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abf084"
      ]
    ],
    [
      "unmatched:00abef18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abf078"
      ]
    ]
  ],
  "added": [
    [
      "00abefb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abf084"
      ]
    ],
    [
      "00abefe0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abf078"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00abeee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00abe/00abeec0.md#insn-00abeee8) · [`00abef18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00abe/00abeec0.md#insn-00abef18) · [`00abefb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00abe/00abeec0.md#insn-00abefb0)
- 新版 `00abf078`（命令位置の公開資料なし）

~~~diff
- 00abeee8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00abeee8 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00abeee8 ["CBRANCH", null, ["local:b15:8", "tmp:1:1"]]
- 00abeee8 bytes a9060054
- 00abef18 ["CBRANCH", null, ["local:b14:8", "register:102:1"]]
- 00abef18 bytes c2040054
- 00abefb0 ["INT_ADD", "register:40f0:8", ["const:abefb0:8", "const:4:8"]]
- 00abefb0 ["CALL", null, ["callee:0041e380:8"]]
+ 00abf078 ["INT_ADD", "register:40f0:8", ["const:abf078:8", "const:4:8"]]
+ 00abf078 ["CALL", null, ["callee:0041e380:8"]]
- 00abefb0 bytes f47ce597
+ 00abf078 bytes c27ce597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fec073a58d33505ac858bbb3d588de6f"></a>

### [`00acfe8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acfe8c.md) → [`00acff54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acff54.md) FUN_00acff54

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00acfa20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acfa20.md) · 呼出先 12件 [`0053d580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d580.md) [`00574730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574730.md) [`00574744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574744.md) [`0057474c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/0057474c.md) [`00574fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574fec.md)
- 新版 呼出元 1件 [`00acfae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfae8.md) · 呼出先 12件 [`0053d580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d580.md) [`00574730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574730.md) [`00574744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574744.md) [`0057474c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/0057474c.md) [`00574fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574fec.md)

変更の種類 constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acfee4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acfee4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acfee8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00acffa0",
      "READ",
      [
        "storage",
        "0029a56b",
        null,
        "string"
      ]
    ],
    [
      "00acffa0",
      "READ",
      [
        "storage",
        "0029a57b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00acfee0",
      "READ",
      [
        "storage",
        "0029a58b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00acffa0",
      "READ",
      [
        "storage",
        "0029a5f8",
        null,
        "string"
      ]
    ],
    [
      "00acffa0",
      "READ",
      [
        "storage",
        "0029a608",
        null,
        "string"
      ]
    ],
    [
      "00acffa8",
      "READ",
      [
        "storage",
        "0029a618",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acfee4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acfe8c.md#insn-00acfee4) · [`00acfee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acfe8c.md#insn-00acfee8) · [`00acfef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acfe8c.md#insn-00acfef0)

~~~diff
- 00acfee4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:60:8"]]
- 00acfee4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00acfee4 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00acfee4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5040:16"]]
- 00acfee4 bytes 010803ad
- 00acfee8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:80:8"]]
- 00acfee8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00acfee8 bytes 0020803d
- 00acfef0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:20:8"]]
- 00acfef0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00acfef0 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00acfef0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00acfef0 bytes 010001ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbdacf553db0c3de18ccafbdd7615ba1"></a>

### [`00ad0154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad0/00ad0154.md) → [`00ad021c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad021c.md) FUN_00ad021c

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0042fd7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042fd7c.md) [`004349a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/004349a0.md) [`00435358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00435/00435358.md) · 呼出先 11件 [`0042e8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e8c4.md) [`00436bf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436bf8.md) [`00438f20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438f20.md) [`00574744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574744.md) [`0057474c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/0057474c.md)
- 新版 呼出元 3件 [`0042fd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fd7c.md) [`004349a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/004349a0.md) [`00435358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/00435358.md) · 呼出先 11件 [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md) [`00436bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436bf8.md) [`00438f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438f20.md) [`00574744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574744.md) [`0057474c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/0057474c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.35% / 新版 67.35%

CFGの説明率　旧版 3.70% / 新版 3.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 14件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad01c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad01f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad01f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ad01c4",
      "DATA",
      [
        "storage",
        "00be6a20",
        null,
        "pointer"
      ]
    ],
    [
      "00ad02b4",
      "DATA",
      [
        "storage",
        "00be6a20",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ad01fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad028c",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ],
    [
      "00ad02b4",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ],
    [
      "00ad02c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad01c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad0/00ad0154.md#insn-00ad01c4) · [`00ad01f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad0/00ad0154.md#insn-00ad01f4) · [`00ad01f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad0/00ad0154.md#insn-00ad01f8)

~~~diff
- 00ad01c4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00ad01c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c0:8"]]
- 00ad01c4 bytes 180000f9
- 00ad01f4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00ad01f4 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00ad01f4 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:18:8"]]
- 00ad01f4 ["STORE", null, ["const:1b1:8", "register:4040:8", "tmp:1:8"]]
- 00ad01f4 bytes 1f8d01f8
- 00ad01f8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 00ad01f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ad01f8 bytes 080800f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34c26d5e28519c23262d123c630a2e27"></a>

### [`00ad05f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad0/00ad05f0.md) → [`00ad06b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad06b8.md) FUN_00ad06b8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00acfe8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acfe8c.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00ad192c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad1/00ad192c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00acff54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acff54.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00ad19f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad19f4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 62.16% / 新版 63.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad062c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ad06f4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad0748"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ad062c",
      "WRITE",
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
      "00ad06f4",
      "WRITE",
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

- 旧版 [`00ad062c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad0/00ad05f0.md#insn-00ad062c) · [`00ad0680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad0/00ad05f0.md#insn-00ad0680) · [`00ad06f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad0/00ad05f0.md#insn-00ad06f4)
- 新版 `00ad0748`（命令位置の公開資料なし） · `00ad07bc`（命令位置の公開資料なし）

~~~diff
- 00ad062c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00ad062c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00ad062c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ad062c bytes a9831ff8
- 00ad0680 ["INT_ADD", "register:40f0:8", ["const:ad0680:8", "const:4:8"]]
- 00ad0680 ["CALL", null, ["callee:00418fe0:8"]]
+ 00ad0748 ["INT_ADD", "register:40f0:8", ["const:ad0748:8", "const:4:8"]]
+ 00ad0748 ["CALL", null, ["callee:00418fe0:8"]]
- 00ad0680 bytes 5822e597
+ 00ad0748 bytes 2622e597
- 00ad06f4 ["INT_ADD", "register:40f0:8", ["const:ad06f4:8", "const:4:8"]]
- 00ad06f4 ["CALL", null, ["callee:00ad19f4:8"]]
+ 00ad07bc ["INT_ADD", "register:40f0:8", ["const:ad07bc:8", "const:4:8"]]
+ 00ad07bc ["CALL", null, ["callee:00ad19f4:8"]]
- 00ad06f4 bytes 8e040094
+ 00ad07bc bytes 8e040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39371888c0de1d5f0c0ce9b7cdd87de4"></a>

### [`00ad4820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad4/00ad4820.md) → [`00ad48e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad48e8.md) FUN_00ad48e8

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ad4294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad4/00ad4294.md) [`00ad6ae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad6/00ad6ae8.md) · 呼出先 1件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 2件 [`00ad435c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad435c.md) [`00ad6bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6bb0.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.53% / 新版 77.53%

CFGの説明率　旧版 9.68% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad4840"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ad4908"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad485c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ad4840",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ad485c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ad493c"
      ]
    ],
    [
      "unmatched:00ad488c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad4908",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00ad4924",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ad493c"
      ]
    ],
    [
      "00ad4954",
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

- 旧版 [`00ad4840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad4/00ad4820.md#insn-00ad4840) · [`00ad485c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad4/00ad4820.md#insn-00ad485c) · [`00ad488c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad4/00ad4820.md#insn-00ad488c)

~~~diff
- 00ad4840 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ad4840 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00ad4840 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ad4840 bytes a8831ff8
- 00ad485c ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00ad485c bytes c0000054
- 00ad488c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad488c ["INT_ADD", "register:40f0:8", ["const:ad488c:8", "const:4:8"]]
- 00ad488c ["CALLIND", null, ["register:0:8"]]
- 00ad488c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11bf6b7db45870b385e186c149b44753"></a>

### [`00ad4cec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad4/00ad4cec.md) → [`00ad4db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4db4.md) FUN_00ad4db4

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ad4424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad4/00ad4424.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e41c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00ad44ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad44ec.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.31% / 新版 98.31%

CFGの説明率　旧版 83.33% / 新版 86.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad4ea0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ad4f68"
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
      "unmatched:00ad4ea0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ad4fac"
      ]
    ]
  ],
  "added": [
    [
      "00ad4f68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ad4fac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad4ea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad4/00ad4cec.md#insn-00ad4ea0) · [`00ad4d80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad4/00ad4cec.md#insn-00ad4d80)
- 新版 `00ad4f68`（命令位置の公開資料なし） · `00ad4e48`（命令位置の公開資料なし）

~~~diff
- 00ad4ea0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00ad4ea0 ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 00ad4ea0 bytes 21020054
+ 00ad4f68 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00ad4f68 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
+ 00ad4f68 bytes 21020054
- 00ad4d80 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00ad4d80 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00ad4d80 ["CBRANCH", null, ["local:b20:8", "tmp:1:1"]]
+ 00ad4e48 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00ad4e48 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00ad4e48 ["CBRANCH", null, ["local:b19:8", "tmp:1:1"]]
- 00ad4d80 bytes 68090054
+ 00ad4e48 bytes 68090054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ca31cb5747235febe1d516e61a5af5b"></a>

### [`00ad5474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad5/00ad5474.md) → [`00ad553c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad553c.md) FUN_00ad553c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad548c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ad5554"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad5494"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ad548c",
      "DATA",
      [
        "storage",
        "00c0f838",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00ad5490",
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
      "00ad5554",
      "DATA",
      [
        "storage",
        "00c0f8e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00ad5558",
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

- 旧版 [`00ad548c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad5/00ad5474.md#insn-00ad548c) · [`00ad5494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad5/00ad5474.md#insn-00ad5494)
- 新版 `00ad5554`（命令位置の公開資料なし）

~~~diff
- 00ad548c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00ad548c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ad548c bytes 080000f9
- 00ad5494 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ad5494 ["RETURN", null, ["register:0:8"]]
- 00ad5494 bytes c0035fd6
+ 00ad5554 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00ad5554 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00ad5554 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-932fd1fd7cf87060031da3cc24d8bf9b"></a>

### [`00ad85b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad8/00ad85b4.md) → [`00ad867c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad867c.md) FUN_00ad867c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00855df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/00855df0.md) · 呼出先 15件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md)
- 新版 呼出元 1件 [`00855df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855df0.md) · 呼出先 15件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.12% / 新版 85.12%

CFGの説明率　旧版 82.14% / 新版 79.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad8610"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad8614"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad8620"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ad8604",
      "READ",
      [
        "storage",
        "002a0dae",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ad8608",
      "READ",
      [
        "storage",
        "002a0dbd",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ad8610",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad86cc",
      "READ",
      [
        "storage",
        "002a0e3b",
        null,
        "string"
      ]
    ],
    [
      "00ad86d0",
      "READ",
      [
        "storage",
        "002a0e4a",
        null,
        "string"
      ]
    ],
    [
      "00ad86d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad8610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad8/00ad85b4.md#insn-00ad8610) · [`00ad8614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad8/00ad85b4.md#insn-00ad8614) · [`00ad8620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad8/00ad85b4.md#insn-00ad8620)

~~~diff
- 00ad8610 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00ad8610 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ad8610 bytes e00b00f9
- 00ad8614 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00ad8614 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00ad8614 bytes 0000803d
- 00ad8620 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00ad8620 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00ad8620 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ad8620 bytes a8831d38
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e9b1c4ebd87c627be33eb86a7fe28cb"></a>

### [`00ad8cec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad8/00ad8cec.md) → [`00ad8db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8db4.md) Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdRewarded

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566a7c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 64.44% / 新版 64.44%

CFGの説明率　旧版 50.00% / 新版 63.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad8cf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad8cf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad8cf4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ad8cf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ad8cf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ad8cf8",
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
      "00ad8db8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ad8dbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ad8dc0",
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

- 旧版 [`00ad8cf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad8/00ad8cec.md#insn-00ad8cf0) · [`00ad8cf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad8/00ad8cec.md#insn-00ad8cf4) · [`00ad8cf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad8/00ad8cec.md#insn-00ad8cf8)

~~~diff
- 00ad8cf0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ad8cf0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ad8cf0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00ad8cf0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ad8cf0 bytes fd7b03a9
- 00ad8cf4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00ad8cf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00ad8cf4 bytes f52300f9
- 00ad8cf8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ad8cf8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ad8cf8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00ad8cf8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ad8cf8 bytes f44f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-106667ad7f24f47e7f03f1b4f7fdf6d3"></a>

### [`00ad8f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad8/00ad8f7c.md) → [`00ad9044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad9044.md) _INIT_264

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00ad7338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad7/00ad7338.md) [`00ad7368`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad7/00ad7368.md) [`00ad73ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad7/00ad73ec.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00ad7400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7400.md) [`00ad7430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7430.md) [`00ad74b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad74b4.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 12.50% / 新版 12.50%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad8fa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad8fc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad8fc4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ad8f94",
      "PARAM",
      [
        "storage",
        "0109fcd0",
        null,
        null
      ]
    ],
    [
      "unmatched:00ad8f9c",
      "PARAM",
      [
        "storage",
        "00ad7338",
        null,
        null
      ]
    ],
    [
      "unmatched:00ad8fa0",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ad905c",
      "PARAM",
      [
        "storage",
        "0109fd90",
        null,
        null
      ]
    ],
    [
      "00ad9064",
      "PARAM",
      [
        "storage",
        "00ad7400",
        null,
        null
      ]
    ],
    [
      "00ad9068",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad8fa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad8/00ad8f7c.md#insn-00ad8fa4) · [`00ad8fa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad8/00ad8f7c.md#insn-00ad8fa8) · [`00ad8fc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad8/00ad8f7c.md#insn-00ad8fc0)

~~~diff
- 00ad8fa4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:20:8"]]
- 00ad8fa4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ad8fa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ad8fa4 bytes 3f1000f9
- 00ad8fa8 ["INT_ADD", "register:40f0:8", ["const:ad8fa8:8", "const:4:8"]]
- 00ad8fa8 ["CALL", null, ["callee:00bdaf90:8"]]
- 00ad8fa8 bytes ce070494
- 00ad8fc0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:20:8"]]
- 00ad8fc0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ad8fc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ad8fc0 bytes 3f1000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6483ecf9b1eab425717824c4f8e83cd5"></a>

### [`00ad9208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad9/00ad9208.md) → [`00ad92d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad92d0.md) FUN_00ad92d0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0085e130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085e130.md) [`0085e328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085e328.md) [`0085ea30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085ea30.md) · 呼出先 8件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 3件 [`0085e130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e130.md) [`0085e328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e328.md) [`0085ea30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085ea30.md) · 呼出先 8件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 72.22% / 新版 68.42%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad9224"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad9240"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad9260"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ad9224",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ad9240",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ad9248",
      "READ",
      [
        "storage",
        "0029ed2f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ad92ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00ad9308",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00ad9310",
      "READ",
      [
        "storage",
        "0029edbc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad9224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad9/00ad9208.md#insn-00ad9224) · [`00ad9228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad9/00ad9208.md#insn-00ad9228) · [`00ad9240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad9/00ad9208.md#insn-00ad9240)
- 新版 `00ad92f0`（命令位置の公開資料なし）

~~~diff
- 00ad9224 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ad9224 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00ad9224 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ad9224 bytes a8831ff8
- 00ad9228 ["INT_ADD", "register:40f0:8", ["const:ad9228:8", "const:4:8"]]
- 00ad9228 ["CALL", null, ["callee:00565f94:8"]]
+ 00ad92f0 ["INT_ADD", "register:40f0:8", ["const:ad92f0:8", "const:4:8"]]
+ 00ad92f0 ["CALL", null, ["callee:00565f94:8"]]
- 00ad9228 bytes 5b33ea97
+ 00ad92f0 bytes 2933ea97
- 00ad9240 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00ad9240 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:18:8"]]
- 00ad9240 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ad9240 bytes e8630039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d02a4b6601114dee5e61ab74bef5b51a"></a>

### [`00ad9708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad9/00ad9708.md) → [`00ad97d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad97d0.md) FUN_00ad97d0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00860170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/00860170.md) · 呼出先 12件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00860170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860170.md) · 呼出先 12件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.00% / 新版 72.00%

CFGの説明率　旧版 45.45% / 新版 38.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad9760"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad9764"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad9770"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ad9754",
      "READ",
      [
        "storage",
        "002973dc",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ad9758",
      "READ",
      [
        "storage",
        "002973e6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ad9760",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad981c",
      "READ",
      [
        "storage",
        "00297469",
        null,
        "string"
      ]
    ],
    [
      "00ad9820",
      "READ",
      [
        "storage",
        "00297473",
        null,
        "string"
      ]
    ],
    [
      "00ad9828",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad9760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad9/00ad9708.md#insn-00ad9760) · [`00ad9764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad9/00ad9708.md#insn-00ad9764) · [`00ad9770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad9/00ad9708.md#insn-00ad9770)

~~~diff
- 00ad9760 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00ad9760 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ad9760 bytes e00b00f9
- 00ad9764 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00ad9764 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00ad9764 bytes 0000803d
- 00ad9770 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00ad9770 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00ad9770 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ad9770 bytes a8831d38
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e62b86351db585331f253732675edd9a"></a>

### [`00adab2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00adab2c.md) → [`00adabf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adabf4.md) Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoySpendCurrency

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566a7c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 25.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adab6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00adac34"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adab54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00adab50",
      "READ",
      [
        "storage",
        "0109fef0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00adab54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00adac60"
      ]
    ],
    [
      "unmatched:00adab68",
      "READ",
      [
        "storage",
        "0109fef0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00adac18",
      "READ",
      [
        "storage",
        "0109ffb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00adac1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00adac60"
      ]
    ],
    [
      "00adac30",
      "READ",
      [
        "storage",
        "0109ffb0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adab54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00adab2c.md#insn-00adab54) · [`00adab6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00adab2c.md#insn-00adab6c) · [`00adab70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00adab2c.md#insn-00adab70)

~~~diff
- 00adab54 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00adab54 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00adab54 bytes 280200b4
- 00adab6c ["COPY", "tmp:0:4", ["register:4098:4"]]
- 00adab6c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff4:8"]]
- 00adab6c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 00adab6c bytes b3431fb8
- 00adab70 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00adab70 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00adab70 bytes 600200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1bf2d2cef0dc35954fd39d6a152ba35"></a>

### [`00adac00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00adac00.md) → [`00adacc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adacc8.md) Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestSuccess

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00566a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566a7c.md) [`00adb914`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb914.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md) [`00adb9dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb9dc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 37.84% / 新版 37.84%

CFGの説明率　旧版 45.45% / 新版 38.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adac04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adac04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adac08"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00adac04",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00adac08",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00adac1c",
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
      "00adaccc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00adacd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00adace4",
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

- 旧版 [`00adac04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00adac00.md#insn-00adac04) · [`00adac08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00adac00.md#insn-00adac08) · [`00adac1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00adac00.md#insn-00adac1c)

~~~diff
- 00adac04 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00adac04 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00adac04 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00adac04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00adac04 bytes fd7b02a9
- 00adac08 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00adac08 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00adac08 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00adac08 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00adac08 bytes f44f03a9
- 00adac1c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00adac1c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00adac1c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00adac1c bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5962fb40c05d743cca68eecf14bc2778"></a>

### [`00adb2e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb2e4.md) → [`00adb3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb3ac.md) FUN_00adb3ac

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00adb1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb1a0.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00adb268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb268.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 57.14% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adb308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb2e4.md#insn-00adb308) · [`00adb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb2e4.md#insn-00adb330) · [`00adb364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb2e4.md#insn-00adb364)
- 新版 `00adb3d0`（命令位置の公開資料なし） · `00adb3f8`（命令位置の公開資料なし）

~~~diff
- 00adb308 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00adb308 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00adb3d0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00adb3d0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00adb308 bytes e80500b4
+ 00adb3d0 bytes e80500b4
- 00adb330 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00adb330 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00adb3f8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00adb3f8 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00adb330 bytes c80400b4
+ 00adb3f8 bytes c80400b4
- 00adb364 ["COPY", "register:4010:8", ["register:40b8:8"]]
- 00adb364 bytes e20317aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47cc8c165cb05c36ea5a1b25db1247fd"></a>

### [`00adb5fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb5fc.md) → [`00adb6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb6c4.md) FUN_00adb6c4

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00adb4c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb4c4.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00adb58c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb58c.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 87.69% / 新版 87.69%

CFGの説明率　旧版 35.29% / 新版 46.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb668"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb66c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb678"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00adb668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb5fc.md#insn-00adb668) · [`00adb66c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb5fc.md#insn-00adb66c) · [`00adb678`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb5fc.md#insn-00adb678)

~~~diff
- 00adb668 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00adb668 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00adb668 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00adb668 ["COPY", "register:40d0:8", ["tmp:0:8"]]
- 00adb668 bytes 5a01899a
- 00adb66c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00adb66c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00adb66c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00adb66c ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 00adb66c bytes 16018b9a
- 00adb678 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00adb678 ["COPY", "tmp:1:8", ["register:40d0:8"]]
- 00adb678 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00adb678 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00adb678 bytes 5733999a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-193ef5575f7590fbd1813f085c148a22"></a>

### [`00adb914`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb914.md) → [`00adb9dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb9dc.md) FUN_00adb9dc

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00adac00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00adac00.md) [`00adacc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00adacc0.md) [`00adadcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00adadcc.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 3件 [`00adacc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adacc8.md) [`00adad88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adad88.md) [`00adae94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adae94.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb914"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb914"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb918"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00adb914",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00adb918",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00adb91c",
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
      "00adb9dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00adb9e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00adb9e4",
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

- 旧版 [`00adb914`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb914.md#insn-00adb914) · [`00adb918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb914.md#insn-00adb918) · [`00adb91c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb914.md#insn-00adb91c)

~~~diff
- 00adb914 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00adb914 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00adb914 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00adb914 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00adb914 bytes fd7bbba9
- 00adb918 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00adb918 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00adb918 bytes f90b00f9
- 00adb91c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00adb91c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00adb91c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00adb91c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00adb91c bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba12a59971c886c52d19e239df3a977e"></a>

### [`00adc9d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adc/00adc9d0.md) → [`00adca98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adca98.md) FUN_00adca98

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 20件 [`004222e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00422/004222e0.md) [`00453c78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00453/00453c78.md) [`0046aa44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046a/0046aa44.md) [`0046c588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c588.md) [`0073496c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00734/0073496c.md) · 呼出先 3件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md)
- 新版 呼出元 20件 [`004222e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) [`00453c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00453/00453c78.md) [`0046aa44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046aa44.md) [`0046c588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c588.md) [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) · 呼出先 3件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.90% / 新版 95.90%

CFGの説明率　旧版 72.50% / 新版 76.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adc9f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adcb38"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00adcabc"
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
      "unmatched:00adc9f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00adcc78"
      ]
    ],
    [
      "unmatched:00adcb38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00adcbcc"
      ]
    ]
  ],
  "added": [
    [
      "00adcabc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00adcc78"
      ]
    ],
    [
      "00adcc00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00adcbcc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adc9f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adc/00adc9d0.md#insn-00adc9f4) · [`00adcb38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adc/00adc9d0.md#insn-00adcb38)
- 新版 `00adcabc`（命令位置の公開資料なし）

~~~diff
- 00adc9f4 ["CBRANCH", null, ["local:b27:8", "register:102:1"]]
- 00adc9f4 bytes e20d0054
+ 00adcabc ["CBRANCH", null, ["local:b25:8", "register:102:1"]]
+ 00adcabc bytes e20d0054
- 00adcb38 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00adcb38 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00adcb38 bytes 61feff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45dd123942f4eede9b4777b2d34466de"></a>

### [`00adf5d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adf5d8.md) → [`00adf6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf6a0.md) FUN_00adf6a0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009a9/009a9ce0.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00ade22c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ade/00ade22c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a9/009a9ce0.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00ade2f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade2f4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 78.18% / 新版 75.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adf744"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adf7d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00adf80c"
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
      "unmatched:00adf744",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00adf7f4"
      ]
    ],
    [
      "unmatched:00adf7d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00adf890"
      ]
    ]
  ],
  "added": [
    [
      "00adf80c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00adf7f4"
      ]
    ],
    [
      "00adf8a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00adf890"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adf744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adf5d8.md#insn-00adf744) · [`00adf7d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adf5d8.md#insn-00adf7d8)
- 新版 `00adf80c`（命令位置の公開資料なし）

~~~diff
- 00adf744 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00adf744 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00adf744 bytes 4bffff54
- 00adf7d8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00adf7d8 ["CBRANCH", null, ["local:b30:8", "tmp:0:1"]]
- 00adf7d8 bytes 81ffff54
+ 00adf80c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00adf80c ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
+ 00adf80c bytes 4bffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4148242c5905089de082ac46b9b35729"></a>

### [`00adf818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adf818.md) → [`00adf8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf8e0.md) FUN_00adf8e0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`006aef04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006aef04.md) [`00730204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00730/00730204.md) [`0094f64c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094f/0094f64c.md) [`0094f7d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094f/0094f7d0.md) [`00957f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00957/00957f9c.md) · 呼出先 1件 [`00ade504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ade/00ade504.md)
- 新版 呼出元 6件 [`006aef04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006aef04.md) [`00730204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00730/00730204.md) [`0094f64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f64c.md) [`0094f7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f7d0.md) [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) · 呼出先 1件 [`00ade5cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade5cc.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 64.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adf84c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adf894"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00adf914"
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
      "unmatched:00adf84c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00adf9a4"
      ]
    ],
    [
      "unmatched:00adf894",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00adf96c"
      ]
    ]
  ],
  "added": [
    [
      "00adf914",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00adf9a4"
      ]
    ],
    [
      "00adf95c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00adf96c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adf84c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adf818.md#insn-00adf84c) · [`00adf894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adf818.md#insn-00adf894)
- 新版 `00adf914`（命令位置の公開資料なし）

~~~diff
- 00adf84c ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00adf84c bytes 80040054
- 00adf894 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00adf894 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00adf894 bytes 81000054
+ 00adf914 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
+ 00adf914 bytes 80040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c78b279ca2b7ef1a2cdfc22c05a29a26"></a>

### [`00adf8f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adf8f8.md) → [`00adf9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf9c0.md) FUN_00adf9c0

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adf910"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00adf9d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00adf918"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00adf910",
      "DATA",
      [
        "storage",
        "00c0f8c8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00adf914",
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
      "00adf9d8",
      "DATA",
      [
        "storage",
        "00c0f978",
        null,
        "undefined *"
      ]
    ],
    [
      "00adf9dc",
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

- 旧版 [`00adf910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adf8f8.md#insn-00adf910) · [`00adf918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adf8f8.md#insn-00adf918)
- 新版 `00adf9d8`（命令位置の公開資料なし）

~~~diff
- 00adf910 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00adf910 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00adf910 bytes 080000f9
- 00adf918 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00adf918 ["RETURN", null, ["register:0:8"]]
- 00adf918 bytes c0035fd6
+ 00adf9d8 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00adf9d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00adf9d8 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-156d2b024fda5a2c015821086c152f3e"></a>

### [`00adfa7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adfa7c.md) → [`00adfb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adfb44.md) FUN_00adfb44

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adfa80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adfaa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adfaa0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00adfa80",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00adfaa0",
      "DATA",
      [
        "storage",
        "00c0f948",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00adfaa4",
      "READ",
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
      "00adfb48",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00adfb68",
      "DATA",
      [
        "storage",
        "00c0f9f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00adfb6c",
      "READ",
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

- 旧版 [`00adfa80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adfa7c.md#insn-00adfa80) · [`00adfaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adfa7c.md#insn-00adfaa0)
- 新版 `00adfb48`（命令位置の公開資料なし）

~~~diff
- 00adfa80 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00adfa80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00adfa80 bytes f30b00f9
- 00adfaa0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00adfaa0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00adfaa0 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00adfaa0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00adfaa0 bytes 082400a9
+ 00adfb48 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 00adfb48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00adfb48 bytes f30b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54174f37994589093d8227328d44b4b9"></a>

### [`00adfab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adfab0.md) → [`00adfb78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adfb78.md) FUN_00adfb78

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00adfabc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adfabc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00adfb84"
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
      "unmatched:00adfabc",
      "DATA",
      [
        "storage",
        "00c0f948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00adfb84",
      "DATA",
      [
        "storage",
        "00c0f9f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adfabc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adfab0.md#insn-00adfabc) · [`00adfac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adfab0.md#insn-00adfac0)
- 新版 `00adfb84`（命令位置の公開資料なし）

~~~diff
- 00adfabc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00adfabc ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00adfabc ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00adfabc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00adfabc bytes 292000a9
- 00adfac0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00adfac0 ["RETURN", null, ["register:0:8"]]
- 00adfac0 bytes c0035fd6
+ 00adfb84 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00adfb84 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00adfb84 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00adfb84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00adfb84 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-144faf4fb6501390337d9b002f88de10"></a>

### [`00ae001c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae001c.md) → [`00ae00e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae00e4.md) _ZN8firebase9analytics8internal10FutureData7DestroyEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddd70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd70.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddcf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcf0.md)
- 新版 呼出元 1件 [`00bdde20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde20.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddda0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 53.33% / 新版 53.33%

CFGの説明率　旧版 33.33% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae001c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae001c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae0020"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae001c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae0020",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae002c",
      "READ",
      [
        "storage",
        "00c1b7a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ae00e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae00e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae00f4",
      "READ",
      [
        "storage",
        "00c1b850",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae001c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae001c.md#insn-00ae001c) · [`00ae0020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae001c.md#insn-00ae0020) · [`00ae0034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae001c.md#insn-00ae0034)

~~~diff
- 00ae001c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae001c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae001c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae001c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae001c bytes f44fbea9
- 00ae0020 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae0020 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae0020 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae0020 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae0020 bytes fd7b01a9
- 00ae0034 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00ae0034 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae0034 bytes b30000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea427052973f215ba38e8c9252e0a06c"></a>

### [`00ae00b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae00b4.md) → [`00ae017c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae017c.md) _ZN8firebase9analytics8internal38UnregisterTerminateOnDefaultAppDestroyEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bddda0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddda0.md) · 呼出先 5件 [`00bddc70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc70.md) [`00bddc90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc90.md) [`00bddcb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcb0.md) [`00bddd00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd00.md) [`00bddd80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd80.md)
- 新版 呼出元 1件 [`00bdde50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde50.md) · 呼出先 5件 [`00bddd20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd20.md) [`00bddd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd40.md) [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md) [`00bdddb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddb0.md) [`00bdde30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde30.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae0190",
      "incomplete_value": true,
      "site": "00ae0194",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:4098:8"
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
      "00ae018c",
      "READ",
      [
        "storage",
        "00c1b7a8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ae00c8",
      "READ",
      [
        "storage",
        "00c24648",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ],
    [
      "unmatched:00ae00c8",
      "PARAM",
      [
        "storage",
        "0029853d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae018c",
      "READ",
      [
        "storage",
        "00c1b858",
        null,
        "pointer"
      ]
    ],
    [
      "00ae0190",
      "READ",
      [
        "storage",
        "00c246f8",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ],
    [
      "00ae0190",
      "PARAM",
      [
        "storage",
        "002985ca",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae00cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae00b4.md#insn-00ae00cc) · [`00ae00c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae00b4.md#insn-00ae00c4) · [`00ae00c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae00b4.md#insn-00ae00c8)
- 新版 `00ae0194`（命令位置の公開資料なし） · `00ae018c`（命令位置の公開資料なし）

~~~diff
- 00ae00cc ["INT_ADD", "register:40f0:8", ["const:ae00cc:8", "const:4:8"]]
- 00ae00cc ["CALL", null, ["callee:00bddd20:8"]]
+ 00ae0194 ["INT_ADD", "register:40f0:8", ["const:ae0194:8", "const:4:8"]]
+ 00ae0194 ["CALL", null, ["callee:00bddd20:8"]]
- 00ae00cc bytes e9f60394
+ 00ae0194 bytes e3f60394
- 00ae00c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
- 00ae00c4 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae018c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:858:8"]]
+ 00ae018c ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae00c4 bytes 73d643f9
+ 00ae018c bytes 732e44f9
- 00ae00c8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae00c8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae00c8 bytes 600240f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44d2626ed5916bee7ea01ddec4a67b3e"></a>

### [`00ae0100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae0100.md) → [`00ae01c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae01c8.md) _ZN8firebase26ReferenceCountedFutureImplC2Em

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bddce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddce0.md) · 呼出先 3件 [`00bddcc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcc0.md) [`00bddd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd20.md) [`00bddde0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddde0.md)
- 新版 呼出元 1件 [`00bddd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd90.md) · 呼出先 3件 [`00bddd70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd70.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md) [`00bdde90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde90.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae012c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae01f4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae01fc",
      "incomplete_value": true,
      "site": "00ae0200",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0134",
      "incomplete_value": true,
      "site": "00ae0138",
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
            "const:8:8"
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
      "00ae01e0",
      "READ",
      [
        "storage",
        "00c1b7b0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ae012c",
      "DATA",
      [
        "storage",
        "00c107a0",
        null,
        "undefined1[120]"
      ]
    ]
  ],
  "added": [
    [
      "00ae01e0",
      "READ",
      [
        "storage",
        "00c1b860",
        null,
        "pointer"
      ]
    ],
    [
      "00ae01f4",
      "DATA",
      [
        "storage",
        "00c10850",
        null,
        "undefined1[120]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae012c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae0100.md#insn-00ae012c) · [`00ae0138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae0100.md#insn-00ae0138)
- 新版 `00ae0200`（命令位置の公開資料なし） · `00ae01f4`（命令位置の公開資料なし）

~~~diff
- 00ae012c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ae012c ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 00ae012c ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:8:8"]]
- 00ae012c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ae012c bytes 888600f8
- 00ae0138 ["INT_ADD", "register:40f0:8", ["const:ae0138:8", "const:4:8"]]
- 00ae0138 ["CALL", null, ["callee:00bdddd0:8"]]
+ 00ae0200 ["INT_ADD", "register:40f0:8", ["const:ae0200:8", "const:4:8"]]
+ 00ae0200 ["CALL", null, ["callee:00bdddd0:8"]]
- 00ae0138 bytes faf60394
+ 00ae0200 bytes f4f60394
+ 00ae01f4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00ae01f4 ["COPY", "tmp:1:8", ["register:40a0:8"]]
+ 00ae01f4 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:8:8"]]
+ 00ae01f4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00ae01f4 bytes 888600f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-459aabdfecfdea9fff8b2fea2e390fc4"></a>

### [`00ae0650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae0650.md) → [`00ae0718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0718.md) _ZN8firebase9analytics9analytics12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 39.29% / 新版 39.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae068c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae06ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae0754"
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
      "unmatched:00ae0664",
      "READ",
      [
        "storage",
        "0109ff70",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae0668",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae06b0"
      ]
    ],
    [
      "00ae0738",
      "READ",
      [
        "storage",
        "0109ff78",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae072c",
      "READ",
      [
        "storage",
        "010a0030",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0730",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae0778"
      ]
    ],
    [
      "00ae0738",
      "READ",
      [
        "storage",
        "010a0038",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae0650.md#insn-00ae0668) · [`00ae0688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae0650.md#insn-00ae0688) · [`00ae068c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae0650.md#insn-00ae068c)

~~~diff
- 00ae0668 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae0668 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00ae0668 bytes 410200b4
- 00ae0688 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae0688 ["INT_ADD", "register:40f0:8", ["const:ae0688:8", "const:4:8"]]
- 00ae0688 ["CALLIND", null, ["register:0:8"]]
- 00ae0688 bytes 00013fd6
- 00ae068c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae068c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae068c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:f78:8"]]
- 00ae068c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae068c bytes bfe23d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3cc802e93969423d33b19a1e282d8eb0"></a>

### [`00ae0730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae0730.md) → [`00ae07f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae07f8.md) _ZN8firebase9analytics9analytics11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 33.33% / 新版 33.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae0744"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ae080c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae0750"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae0744",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae0754"
      ]
    ],
    [
      "unmatched:00ae074c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae0750",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae080c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae081c"
      ]
    ],
    [
      "00ae0814",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae0818",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae0730.md#insn-00ae0744) · [`00ae0750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae0730.md#insn-00ae0750) · [`00ae0768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae0730.md#insn-00ae0768)

~~~diff
- 00ae0744 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00ae0744 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae0744 bytes 8b000054
- 00ae0750 ["INT_ADD", "register:40f0:8", ["const:ae0750:8", "const:4:8"]]
- 00ae0750 ["CALL", null, ["callee:00bde130:8"]]
- 00ae0750 bytes 4cf60394
- 00ae0768 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae0768 ["RETURN", null, ["register:0:8"]]
- 00ae0768 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-176fa98184d0f8c5917c21b4bcfa9316"></a>

### [`00ae07dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae07dc.md) → [`00ae08a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae08a4.md) _ZN8firebase9analytics9analytics10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae07fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00ae08c4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae0814"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae08b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae0800"
      ]
    ],
    [
      "unmatched:00ae07f8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae07fc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae08b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae08c8"
      ]
    ],
    [
      "00ae08c0",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae08c4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae07fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae07dc.md#insn-00ae07fc) · [`00ae0814`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae07dc.md#insn-00ae0814)
- 新版 `00ae08c4`（命令位置の公開資料なし）

~~~diff
- 00ae07fc ["INT_ADD", "register:40f0:8", ["const:ae07fc:8", "const:4:8"]]
- 00ae07fc ["CALL", null, ["callee:00bde130:8"]]
- 00ae07fc bytes 21f60394
- 00ae0814 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae0814 ["RETURN", null, ["register:0:8"]]
- 00ae0814 bytes c0035fd6
+ 00ae08c4 ["INT_ADD", "register:40f0:8", ["const:ae08c4:8", "const:4:8"]]
+ 00ae08c4 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae08c4 bytes 1bf60394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28de7056bf425ffaa5d24d9d9cf7a9d0"></a>

### [`00ae119c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae119c.md) → [`00ae1264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1264.md) _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc40.md) · 呼出先 1件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 56.41% / 新版 56.41%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae11a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae11a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae11a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae11a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae11a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae11ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae1268",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae126c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae1274",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae11a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae119c.md#insn-00ae11a0) · [`00ae11a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae119c.md#insn-00ae11a4) · [`00ae11ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae119c.md#insn-00ae11ac)

~~~diff
- 00ae11a0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00ae11a0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae11a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00ae11a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae11a0 bytes fc4f10a9
- 00ae11a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae11a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae11a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00ae11a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae11a4 bytes fd7b11a9
- 00ae11ac ["COPY", "tmp:0:8", ["register:4018:8"]]
- 00ae11ac ["COPY", "tmp:1:8", ["register:4020:8"]]
- 00ae11ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:88:8"]]
- 00ae11ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae11ac bytes e39308a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddb327aef1fa06aa3a71450c6df062c0"></a>

### [`00ae17c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae17c8.md) → [`00ae1890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1890.md) _ZN8firebase9analytics11AddToBundleEP7_JNIEnvP8_jobjectPKcS6_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae17d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae17d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae1898"
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
      "unmatched:00ae17d0",
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
      "00ae1898",
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

- 旧版 [`00ae17d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae17c8.md#insn-00ae17d0) · [`00ae17f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae17c8.md#insn-00ae17f0)
- 新版 `00ae1898`（命令位置の公開資料なし） · `00ae18b8`（命令位置の公開資料なし）

~~~diff
- 00ae17d0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae17d0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae17d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae17d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae17d0 bytes fd7b02a9
+ 00ae1898 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00ae1898 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00ae1898 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
+ 00ae1898 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00ae1898 bytes fd7b02a9
- 00ae17f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae17f0 ["INT_ADD", "register:40f0:8", ["const:ae17f0:8", "const:4:8"]]
- 00ae17f0 ["CALLIND", null, ["register:0:8"]]
+ 00ae18b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae18b8 ["INT_ADD", "register:40f0:8", ["const:ae18b8:8", "const:4:8"]]
+ 00ae18b8 ["CALLIND", null, ["register:0:8"]]
- 00ae17f0 bytes 00013fd6
+ 00ae18b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b86587ae92256e4f275d3e3dac72f0e6"></a>

### [`00ae186c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae186c.md) → [`00ae1934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1934.md) _ZN8firebase9analytics11AddToBundleEP7_JNIEnvP8_jobjectPKcd

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae187c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae186c.md#insn-00ae187c) · [`00ae1898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae186c.md#insn-00ae1898) · [`00ae18a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae186c.md#insn-00ae18a4)
- 新版 `00ae1960`（命令位置の公開資料なし） · `00ae196c`（命令位置の公開資料なし）

~~~diff
- 00ae187c ["COPY", "tmp:0:8", ["const:20:8"]]
- 00ae187c ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 00ae187c ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 00ae187c ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 00ae187c bytes fd830091
- 00ae1898 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae1898 ["INT_ADD", "register:40f0:8", ["const:ae1898:8", "const:4:8"]]
- 00ae1898 ["CALLIND", null, ["register:0:8"]]
+ 00ae1960 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae1960 ["INT_ADD", "register:40f0:8", ["const:ae1960:8", "const:4:8"]]
+ 00ae1960 ["CALLIND", null, ["register:0:8"]]
- 00ae1898 bytes 00013fd6
+ 00ae1960 bytes 00013fd6
- 00ae18a4 ["INT_ADD", "register:40f0:8", ["const:ae18a4:8", "const:4:8"]]
- 00ae18a4 ["CALL", null, ["callee:00bde0c0:8"]]
+ 00ae196c ["INT_ADD", "register:40f0:8", ["const:ae196c:8", "const:4:8"]]
+ 00ae196c ["CALL", null, ["callee:00bde0c0:8"]]
- 00ae18a4 bytes dbf10394
+ 00ae196c bytes d5f10394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0239bf77a84da5cfc147729348d32ac4"></a>

### [`00ae18ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae18ec.md) → [`00ae19b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae19b4.md) _ZN8firebase9analytics11AddToBundleEP7_JNIEnvP8_jobjectPKcl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)

変更の種類 constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae1914`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae18ec.md#insn-00ae1914) · [`00ae1920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae18ec.md#insn-00ae1920) · [`00ae1938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae18ec.md#insn-00ae1938)
- 新版 `00ae19dc`（命令位置の公開資料なし） · `00ae19e8`（命令位置の公開資料なし） · `00ae1a00`（命令位置の公開資料なし）

~~~diff
- 00ae1914 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae1914 ["INT_ADD", "register:40f0:8", ["const:ae1914:8", "const:4:8"]]
- 00ae1914 ["CALLIND", null, ["register:0:8"]]
+ 00ae19dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae19dc ["INT_ADD", "register:40f0:8", ["const:ae19dc:8", "const:4:8"]]
+ 00ae19dc ["CALLIND", null, ["register:0:8"]]
- 00ae1914 bytes 00013fd6
+ 00ae19dc bytes 00013fd6
- 00ae1920 ["INT_ADD", "register:40f0:8", ["const:ae1920:8", "const:4:8"]]
- 00ae1920 ["CALL", null, ["callee:00bde0c0:8"]]
+ 00ae19e8 ["INT_ADD", "register:40f0:8", ["const:ae19e8:8", "const:4:8"]]
+ 00ae19e8 ["CALL", null, ["callee:00bde0c0:8"]]
- 00ae1920 bytes bcf10394
+ 00ae19e8 bytes b6f10394
- 00ae1938 ["INT_ADD", "register:40f0:8", ["const:ae1938:8", "const:4:8"]]
- 00ae1938 ["CALL", null, ["callee:00551e14:8"]]
+ 00ae1a00 ["INT_ADD", "register:40f0:8", ["const:ae1a00:8", "const:4:8"]]
+ 00ae1a00 ["CALL", null, ["callee:00551e14:8"]]
- 00ae1938 bytes 37c1e997
+ 00ae1a00 bytes 05c1e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebf2ae29735176a65a23ecd8094c3ce7"></a>

### [`00ae1964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1964.md) → [`00ae1a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1a2c.md) _ZN8firebase9analytics20AddArrayListToBundleEP7_JNIEnvP8_jobjectPKcS4_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae19a0",
      "incomplete_value": true,
      "site": "00ae19b0",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae19a4",
      "incomplete_value": true,
      "site": "00ae19b0",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae199c",
      "incomplete_value": true,
      "site": "00ae19b0",
      "value": [
        "live",
        "register:4000:8"
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ae19b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1964.md#insn-00ae19b0) · [`00ae1970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1964.md#insn-00ae1970) · [`00ae198c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1964.md#insn-00ae198c)
- 新版 `00ae1a78`（命令位置の公開資料なし） · `00ae1a54`（命令位置の公開資料なし）

~~~diff
- 00ae19b0 ["INT_ADD", "register:40f0:8", ["const:ae19b0:8", "const:4:8"]]
- 00ae19b0 ["CALL", null, ["callee:00551e14:8"]]
+ 00ae1a78 ["INT_ADD", "register:40f0:8", ["const:ae1a78:8", "const:4:8"]]
+ 00ae1a78 ["CALL", null, ["callee:00551e14:8"]]
- 00ae19b0 bytes 19c1e997
+ 00ae1a78 bytes e7c0e997
- 00ae1970 ["COPY", "tmp:0:8", ["const:20:8"]]
- 00ae1970 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 00ae1970 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 00ae1970 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 00ae1970 bytes fd830091
- 00ae198c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae198c ["INT_ADD", "register:40f0:8", ["const:ae198c:8", "const:4:8"]]
- 00ae198c ["CALLIND", null, ["register:0:8"]]
+ 00ae1a54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae1a54 ["INT_ADD", "register:40f0:8", ["const:ae1a54:8", "const:4:8"]]
+ 00ae1a54 ["CALLIND", null, ["register:0:8"]]
- 00ae198c bytes 00013fd6
+ 00ae1a54 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0c46a329d68ce10e7f71bef8e1dcea9"></a>

### [`00ae1b58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1b58.md) → [`00ae1c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1c20.md) _ZN8firebase9analytics11MapToBundleEP7_JNIEnvRKNSt6__ndk13mapINS_7VariantES5_NS3_4lessIS5_EENS3_9allocatorINS3_4pairIKS5_S5_EEEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde090.md) · 呼出先 8件 [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bddbd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddbd0.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde010.md)
- 新版 呼出元 1件 [`00bde140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde140.md) · 呼出先 8件 [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bddc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc80.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 74.77% / 新版 74.77%

CFGの説明率　旧版 18.37% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1bcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1bfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1c08"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae1bc0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae1c98"
      ]
    ],
    [
      "unmatched:00ae1bcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae1dbc"
      ]
    ],
    [
      "unmatched:00ae1bfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae1c14"
      ]
    ]
  ],
  "added": [
    [
      "00ae1c88",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae1c98"
      ]
    ],
    [
      "00ae1c94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae1dbc"
      ]
    ],
    [
      "00ae1cc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae1cdc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae1bcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1b58.md#insn-00ae1bcc) · [`00ae1bfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1b58.md#insn-00ae1bfc) · [`00ae1c08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1b58.md#insn-00ae1c08)

~~~diff
- 00ae1bcc ["CBRANCH", null, ["local:b33:8", "register:101:1"]]
- 00ae1bcc bytes 40090054
- 00ae1bfc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00ae1bfc ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00ae1bfc bytes c1000054
- 00ae1c08 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00ae1c08 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00ae1c08 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00ae1c08 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00ae1c08 bytes 09010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d40cf433b3a6a23d0255a4218d8cc3f3"></a>

### [`00ae30f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae30f0.md) → [`00ae31b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae31b8.md) _ZN8firebase6FutureIlEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdde50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde50.md) · 呼出先 3件 [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdde70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde70.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md)
- 新版 呼出元 1件 [`00bddf00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf00.md) · 呼出先 3件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 20.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3168"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00ae3230"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ae3168`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae30f0.md#insn-00ae3168) · [`00ae3110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae30f0.md#insn-00ae3110)
- 新版 `00ae3230`（命令位置の公開資料なし） · `00ae31d8`（命令位置の公開資料なし）

~~~diff
- 00ae3168 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae3168 ["RETURN", null, ["register:0:8"]]
- 00ae3168 bytes c0035fd6
+ 00ae3230 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00ae3230 ["RETURN", null, ["register:0:8"]]
+ 00ae3230 bytes c0035fd6
- 00ae3110 ["INT_ADD", "register:40f0:8", ["const:ae3110:8", "const:4:8"]]
- 00ae3110 ["CALL", null, ["callee:00bdddc0:8"]]
+ 00ae31d8 ["INT_ADD", "register:40f0:8", ["const:ae31d8:8", "const:4:8"]]
+ 00ae31d8 ["CALL", null, ["callee:00bdddc0:8"]]
- 00ae3110 bytes 00eb0394
+ 00ae31d8 bytes faea0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adab28b6a6854c980686bec203c42498"></a>

### [`00ae3fcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3fcc.md) → [`00ae4094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4094.md) _ZN8firebase8LogDebugEPKcz

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bde1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1b0.md) · 呼出先 2件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1a0.md)
- 新版 呼出元 1件 [`00bde260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde260.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde250.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_store_alignment

命令の説明率　旧版 34.15% / 新版 34.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 2件, `store_value` 2件, `unresolved_store_alignment` 24件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3fd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3fd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3fd4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae3fd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae3fd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae3fdc",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae4098",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae409c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae40a4",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae3fd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3fcc.md#insn-00ae3fd0) · [`00ae3fd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3fcc.md#insn-00ae3fd4) · [`00ae3fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3fcc.md#insn-00ae3fdc)

~~~diff
- 00ae3fd0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00ae3fd0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae3fd0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00ae3fd0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae3fd0 bytes fc4f11a9
- 00ae3fd4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae3fd4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae3fd4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00ae3fd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae3fd4 bytes fd7b12a9
- 00ae3fdc ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00ae3fdc ["COPY", "tmp:1:8", ["register:4010:8"]]
- 00ae3fdc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:88:8"]]
- 00ae3fdc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae3fdc bytes e18b08a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12df602d51f980401588ff34520d5a94"></a>

### [`00ae4070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4070.md) → [`00ae4138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4138.md) _ZN8firebase7LogInfoEPKcz

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bde060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde060.md) · 呼出先 2件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1a0.md)
- 新版 呼出元 1件 [`00bde110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde110.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde250.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 68.29% / 新版 68.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_value` 4件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4098"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4098"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae409c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae4098",
      "WRITE",
      [
        "storage",
        "Stack[-0xf0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae409c",
      "WRITE",
      [
        "storage",
        "Stack[-0xd0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae4160",
      "WRITE",
      [
        "storage",
        "Stack[-0xf0]",
        null,
        null
      ]
    ],
    [
      "00ae4164",
      "WRITE",
      [
        "storage",
        "Stack[-0xd0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4098`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4070.md#insn-00ae4098) · [`00ae409c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4070.md#insn-00ae409c)
- 新版 `00ae4160`（命令位置の公開資料なし）

~~~diff
- 00ae4098 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00ae4098 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5080:16"]]
- 00ae4098 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00ae4098 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:50a0:16"]]
- 00ae4098 bytes e41702ad
- 00ae409c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00ae409c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:50c0:16"]]
- 00ae409c ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00ae409c ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:50e0:16"]]
- 00ae409c bytes e61f03ad
+ 00ae4160 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
+ 00ae4160 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5080:16"]]
+ 00ae4160 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
+ 00ae4160 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:50a0:16"]]
+ 00ae4160 bytes e41702ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad55b852b8ce8d252e51125895ab1739"></a>

### [`00ae4114`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4114.md) → [`00ae41dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae41dc.md) _ZN8firebase10LogWarningEPKcz

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdde60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde60.md) · 呼出先 2件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1a0.md)
- 新版 呼出元 1件 [`00bddf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf10.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde250.md)

変更の種類 call_argument_candidate, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae4250",
      "incomplete_value": true,
      "site": "00ae4258",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": {
      "definition_site": "00ae4188",
      "incomplete_value": true,
      "site": "00ae4190",
      "value": [
        "live",
        "register:4000:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae4180",
      "incomplete_value": true,
      "site": "00ae4190",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "live",
            "register:40e8:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4114.md#insn-00ae4190) · [`00ae4180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4114.md#insn-00ae4180) · [`00ae41b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4114.md#insn-00ae41b4)
- 新版 `00ae4258`（命令位置の公開資料なし） · `00ae427c`（命令位置の公開資料なし）

~~~diff
- 00ae4190 ["INT_ADD", "register:40f0:8", ["const:ae4190:8", "const:4:8"]]
- 00ae4190 ["CALL", null, ["callee:00bde250:8"]]
+ 00ae4258 ["INT_ADD", "register:40f0:8", ["const:ae4258:8", "const:4:8"]]
+ 00ae4258 ["CALL", null, ["callee:00bde250:8"]]
- 00ae4190 bytes 04e80394
+ 00ae4258 bytes fee70394
- 00ae4180 ["INT_SUB", "register:4010:8", ["register:40e8:8", "const:60:8"]]
- 00ae4180 bytes a28301d1
- 00ae41b4 ["INT_ADD", "register:40f0:8", ["const:ae41b4:8", "const:4:8"]]
- 00ae41b4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ae427c ["INT_ADD", "register:40f0:8", ["const:ae427c:8", "const:4:8"]]
+ 00ae427c ["CALL", null, ["callee:00bdb040:8"]]
- 00ae41b4 bytes 77db0394
+ 00ae427c bytes 71db0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99fb5c9163e789fe9279d80ea8c7c097"></a>

### [`00ae4300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4300.md) → [`00ae43c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae43c8.md) _ZN8firebase10LogMessageENS_8LogLevelEPKcz

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde140.md) · 呼出先 2件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1a0.md)
- 新版 呼出元 1件 [`00bde1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1f0.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde250.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 27.03% / 新版 27.03%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 25件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4304"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4304"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4308"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae4304",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae4308",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae4310",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae43cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae43d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae43d8",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4300.md#insn-00ae4304) · [`00ae4308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4300.md#insn-00ae4308) · [`00ae4310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4300.md#insn-00ae4310)

~~~diff
- 00ae4304 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00ae4304 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae4304 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00ae4304 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4304 bytes fc4f10a9
- 00ae4308 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae4308 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae4308 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00ae4308 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4308 bytes fd7b11a9
- 00ae4310 ["COPY", "tmp:0:8", ["register:4010:8"]]
- 00ae4310 ["COPY", "tmp:1:8", ["register:4018:8"]]
- 00ae4310 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00ae4310 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4310 bytes e20f08a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-faf9a68e1cb2f909953319e5724a72aa"></a>

### [`00ae4394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4394.md) → [`00ae445c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae445c.md) _ZN8firebase14LogSetCallbackEPFvNS_8LogLevelEPKcPvES3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00ae3e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3e68.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00ae3f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae43b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae43b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae447c"
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
      "unmatched:00ae439c",
      "READ",
      [
        "storage",
        "00c1b7e0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ae43a0",
      "READ",
      [
        "storage",
        "00c1b7e8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ae43b4",
      "WRITE",
      [
        "storage",
        "00c24660",
        "_ZN8firebase14g_log_callbackE",
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ae4464",
      "READ",
      [
        "storage",
        "00c1b890",
        null,
        "pointer"
      ]
    ],
    [
      "00ae4468",
      "READ",
      [
        "storage",
        "00c1b898",
        null,
        "pointer"
      ]
    ],
    [
      "00ae447c",
      "WRITE",
      [
        "storage",
        "00c24710",
        "_ZN8firebase14g_log_callbackE",
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae43b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4394.md#insn-00ae43b0) · [`00ae43b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4394.md#insn-00ae43b4) · [`00ae43b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4394.md#insn-00ae43b8)

~~~diff
- 00ae43b0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ae43b0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00ae43b0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00ae43b0 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00ae43b0 bytes 0801809a
- 00ae43b4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00ae43b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ae43b4 bytes 280100f9
- 00ae43b8 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00ae43b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00ae43b8 bytes 410100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-493f529ada11bbee49c06f6668dd4894"></a>

### [`00ae44e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae44e8.md) → [`00ae45b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae45b0.md) _ZN8firebase18AndroidLogMessageVEiPKcS1_St9__va_list

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde320.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae450c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae450c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae45d4"
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
      "unmatched:00ae450c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae4510",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde320"
      ]
    ],
    [
      "unmatched:00ae4518",
      "READ",
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
      "00ae45d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00ae45d8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde320"
      ]
    ],
    [
      "00ae45e0",
      "READ",
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

- 旧版 [`00ae450c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae44e8.md#insn-00ae450c) · [`00ae4510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae44e8.md#insn-00ae4510) · [`00ae4520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae44e8.md#insn-00ae4520)

~~~diff
- 00ae450c ["COPY", "tmp:0:8", ["register:8:8"]]
- 00ae450c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00ae450c ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00ae450c ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00ae450c bytes e10300ad
- 00ae4510 ["INT_ADD", "register:40f0:8", ["const:ae4510:8", "const:4:8"]]
- 00ae4510 ["CALL", null, ["callee:00bde320:8"]]
- 00ae4510 bytes 58e70394
- 00ae4520 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00ae4520 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00ae4520 bytes a1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa7d67a7007f2d00bfdee2888aaf55be"></a>

### [`00ae453c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae453c.md) → [`00ae4604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4604.md) _ZN8firebase11LogMessageVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde160.md) · 呼出先 2件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bde210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde210.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde320.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.77% / 新版 90.77%

CFGの説明率　旧版 27.78% / 新版 21.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae4638",
      "DATA",
      [
        "storage",
        "002f5a44",
        "switchD_00ae457c::switchdataD_002f5a44",
        "byte"
      ]
    ],
    [
      "unmatched:00ae4588",
      "READ",
      [
        "storage",
        "00c1b800",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ae45a0",
      "READ",
      [
        "storage",
        "00c1b800",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ae4638",
      "DATA",
      [
        "storage",
        "002f5a44",
        "switchD_00ae4644::switchdataD_002f5a44",
        "byte"
      ]
    ],
    [
      "00ae4650",
      "READ",
      [
        "storage",
        "00c1b8b0",
        null,
        "pointer"
      ]
    ],
    [
      "00ae4668",
      "READ",
      [
        "storage",
        "00c1b8b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae455c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae453c.md#insn-00ae455c) · [`00ae456c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae453c.md#insn-00ae456c) · [`00ae4588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae453c.md#insn-00ae4588)
- 新版 `00ae4624`（命令位置の公開資料なし） · `00ae4634`（命令位置の公開資料なし）

~~~diff
- 00ae455c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00ae455c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00ae455c ["CBRANCH", null, ["local:b10:8", "tmp:1:1"]]
+ 00ae4624 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00ae4624 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00ae4624 ["CBRANCH", null, ["local:b15:8", "tmp:1:1"]]
- 00ae455c bytes 08060054
+ 00ae4624 bytes 08060054
- 00ae456c ["COPY", "register:4058:8", ["const:ae4580:8"]]
+ 00ae4634 ["COPY", "register:4058:8", ["const:ae4648:8"]]
- 00ae456c bytes ab000010
+ 00ae4634 bytes ab000010
- 00ae4588 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:800:8"]]
- 00ae4588 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae4588 bytes 290144f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90491bae115afec8c2dfebc8764f5a3a"></a>

### [`00ae4920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4920.md) → [`00ae49e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae49e8.md) _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) · 呼出先 0件 

変更の種類 call, call_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4960"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00ae4a28"
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
      "unmatched:00ae4960",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae4a28",
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

- 旧版 [`00ae4960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4920.md#insn-00ae4960) · [`00ae4938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4920.md#insn-00ae4938)
- 新版 `00ae4a28`（命令位置の公開資料なし） · `00ae4a00`（命令位置の公開資料なし）

~~~diff
- 00ae4960 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae4960 ["INT_ADD", "register:40f0:8", ["const:ae4960:8", "const:4:8"]]
- 00ae4960 ["CALLIND", null, ["register:0:8"]]
- 00ae4960 bytes 00013fd6
+ 00ae4a28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae4a28 ["INT_ADD", "register:40f0:8", ["const:ae4a28:8", "const:4:8"]]
+ 00ae4a28 ["CALLIND", null, ["register:0:8"]]
+ 00ae4a28 bytes 00013fd6
- 00ae4938 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae4938 ["INT_ADD", "register:40f0:8", ["const:ae4938:8", "const:4:8"]]
- 00ae4938 ["CALLIND", null, ["register:0:8"]]
+ 00ae4a00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae4a00 ["INT_ADD", "register:40f0:8", ["const:ae4a00:8", "const:4:8"]]
+ 00ae4a00 ["CALLIND", null, ["register:0:8"]]
- 00ae4938 bytes 00013fd6
+ 00ae4a00 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbd5aa940ed4ca18caa903576e4ce2f9"></a>

### [`00ae4cf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4cf8.md) → [`00ae4dc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4dc0.md) _ZN8firebase4util12class_loader11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 26.67% / 新版 26.67%

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
      "site": "00ae4cf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4cfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4cfc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae4cf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae4cfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae4dd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae4d1c"
      ]
    ]
  ],
  "added": [
    [
      "00ae4dc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae4dc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae4dd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae4de4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4cf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4cf8.md#insn-00ae4cf8) · [`00ae4cfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4cf8.md#insn-00ae4cfc) · [`00ae4d18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4cf8.md#insn-00ae4d18)

~~~diff
- 00ae4cf8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae4cf8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae4cf8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae4cf8 bytes f30f1ef8
- 00ae4cfc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae4cfc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae4cfc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae4cfc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4cfc bytes fd7b01a9
- 00ae4d18 ["INT_ADD", "register:40f0:8", ["const:ae4d18:8", "const:4:8"]]
- 00ae4d18 ["CALL", null, ["callee:00bde130:8"]]
- 00ae4d18 bytes dae40394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebc0c6bf7324b3282edce6e395ccb2ce"></a>

### [`00ae504c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae504c.md) → [`00ae5114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5114.md) _ZN8firebase4util17jniresultcallback19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5078"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae5140"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5060"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae505c",
      "READ",
      [
        "storage",
        "010a0290",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae5060",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae5144"
      ]
    ],
    [
      "unmatched:00ae506c",
      "PARAM",
      [
        "storage",
        "0029fea8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae5124",
      "READ",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5128",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae5144"
      ]
    ],
    [
      "00ae5134",
      "PARAM",
      [
        "storage",
        "0029ff35",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae504c.md#insn-00ae5060) · [`00ae5070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae504c.md#insn-00ae5070) · [`00ae5078`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae504c.md#insn-00ae5078)

~~~diff
- 00ae5060 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae5060 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae5060 bytes e80000b5
- 00ae5070 ["INT_ADD", "register:40f0:8", ["const:ae5070:8", "const:4:8"]]
- 00ae5070 ["CALL", null, ["callee:00bde040:8"]]
- 00ae5070 bytes c8e30394
- 00ae5078 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00ae5078 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5078 bytes 604a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbe882b2ea36194d32ada6f14cd1154a"></a>

### [`00ae530c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae530c.md) → [`00ae53d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae53d4.md) _ZN8firebase4util17jniresultcallback11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae532c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00ae53f4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5344"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae53e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae5330"
      ]
    ],
    [
      "unmatched:00ae5328",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae532c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae53e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae53f8"
      ]
    ],
    [
      "00ae53f0",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae53f4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae532c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae530c.md#insn-00ae532c) · [`00ae5344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae530c.md#insn-00ae5344)
- 新版 `00ae53f4`（命令位置の公開資料なし）

~~~diff
- 00ae532c ["INT_ADD", "register:40f0:8", ["const:ae532c:8", "const:4:8"]]
- 00ae532c ["CALL", null, ["callee:00bde130:8"]]
- 00ae532c bytes 55e30394
- 00ae5344 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae5344 ["RETURN", null, ["register:0:8"]]
- 00ae5344 bytes c0035fd6
+ 00ae53f4 ["INT_ADD", "register:40f0:8", ["const:ae53f4:8", "const:4:8"]]
+ 00ae53f4 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae53f4 bytes 4fe30394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b87b9b985f873ab251427c6fd269bb7"></a>

### [`00ae56b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae56b4.md) → [`00ae577c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae577c.md) _ZN8firebase4util26cppthreaddispatchercontext11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 26.67% / 新版 26.67%

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
      "site": "00ae56b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae56b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae56b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae56b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae56b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae5790",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae56d8"
      ]
    ]
  ],
  "added": [
    [
      "00ae577c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae5780",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae5790",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae57a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae56b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae56b4.md#insn-00ae56b4) · [`00ae56b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae56b4.md#insn-00ae56b8) · [`00ae56d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae56b4.md#insn-00ae56d4)

~~~diff
- 00ae56b4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae56b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae56b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae56b4 bytes f30f1ef8
- 00ae56b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae56b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae56b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae56b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae56b8 bytes fd7b01a9
- 00ae56d4 ["INT_ADD", "register:40f0:8", ["const:ae56d4:8", "const:4:8"]]
- 00ae56d4 ["CALL", null, ["callee:00bde130:8"]]
- 00ae56d4 bytes 6be20394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1f5ea1689406593853d5589fc300b9d"></a>

### [`00ae5760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5760.md) → [`00ae5828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5828.md) _ZN8firebase4util26cppthreaddispatchercontext10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5780"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00ae5848"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5798"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae583c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae5784"
      ]
    ],
    [
      "unmatched:00ae577c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae5780",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae583c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae584c"
      ]
    ],
    [
      "00ae5844",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae5848",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5760.md#insn-00ae5780) · [`00ae5798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5760.md#insn-00ae5798)
- 新版 `00ae5848`（命令位置の公開資料なし）

~~~diff
- 00ae5780 ["INT_ADD", "register:40f0:8", ["const:ae5780:8", "const:4:8"]]
- 00ae5780 ["CALL", null, ["callee:00bde130:8"]]
- 00ae5780 bytes 40e20394
- 00ae5798 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae5798 ["RETURN", null, ["register:0:8"]]
- 00ae5798 bytes c0035fd6
+ 00ae5848 ["INT_ADD", "register:40f0:8", ["const:ae5848:8", "const:4:8"]]
+ 00ae5848 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae5848 bytes 3ae20394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7718e265920e6192631092f2e19f7a8"></a>

### [`00ae5b08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5b08.md) → [`00ae5bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5bd0.md) _ZN8firebase4util19cppthreaddispatcher10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5b28"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00ae5bf0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5b40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae5be4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae5b2c"
      ]
    ],
    [
      "unmatched:00ae5b24",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae5b28",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae5be4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae5bf4"
      ]
    ],
    [
      "00ae5bec",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae5bf0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5b28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5b08.md#insn-00ae5b28) · [`00ae5b40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5b08.md#insn-00ae5b40)
- 新版 `00ae5bf0`（命令位置の公開資料なし）

~~~diff
- 00ae5b28 ["INT_ADD", "register:40f0:8", ["const:ae5b28:8", "const:4:8"]]
- 00ae5b28 ["CALL", null, ["callee:00bde130:8"]]
- 00ae5b28 bytes 56e10394
- 00ae5b40 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae5b40 ["RETURN", null, ["register:0:8"]]
- 00ae5b40 bytes c0035fd6
+ 00ae5bf0 ["INT_ADD", "register:40f0:8", ["const:ae5bf0:8", "const:4:8"]]
+ 00ae5bf0 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae5bf0 bytes 50e10394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9377384ca33fc35111724d9ca228c58a"></a>

### [`00ae5e04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5e04.md) → [`00ae5ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5ecc.md) _ZN8firebase4util3log11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5e24"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00ae5eec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5e3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae5ee0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae5e28"
      ]
    ],
    [
      "unmatched:00ae5e20",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae5e24",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae5ee0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae5ef0"
      ]
    ],
    [
      "00ae5ee8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae5eec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5e24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5e04.md#insn-00ae5e24) · [`00ae5e3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5e04.md#insn-00ae5e3c)
- 新版 `00ae5eec`（命令位置の公開資料なし）

~~~diff
- 00ae5e24 ["INT_ADD", "register:40f0:8", ["const:ae5e24:8", "const:4:8"]]
- 00ae5e24 ["CALL", null, ["callee:00bde130:8"]]
- 00ae5e24 bytes 97e00394
- 00ae5e3c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae5e3c ["RETURN", null, ["register:0:8"]]
- 00ae5e3c bytes c0035fd6
+ 00ae5eec ["INT_ADD", "register:40f0:8", ["const:ae5eec:8", "const:4:8"]]
+ 00ae5eec ["CALL", null, ["callee:00bde130:8"]]
+ 00ae5eec bytes 91e00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed0d80d7bdcf31be17fc6feb1742e2b4"></a>

### [`00ae5eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5eb0.md) → [`00ae5f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5f78.md) _ZN8firebase4util3log10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5ed0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00ae5f98"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5ee8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae5f8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae5ed4"
      ]
    ],
    [
      "unmatched:00ae5ecc",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae5ed0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae5f8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae5f9c"
      ]
    ],
    [
      "00ae5f94",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae5f98",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5ed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5eb0.md#insn-00ae5ed0) · [`00ae5ee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5eb0.md#insn-00ae5ee8)
- 新版 `00ae5f98`（命令位置の公開資料なし）

~~~diff
- 00ae5ed0 ["INT_ADD", "register:40f0:8", ["const:ae5ed0:8", "const:4:8"]]
- 00ae5ed0 ["CALL", null, ["callee:00bde130:8"]]
- 00ae5ed0 bytes 6ce00394
- 00ae5ee8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae5ee8 ["RETURN", null, ["register:0:8"]]
- 00ae5ee8 bytes c0035fd6
+ 00ae5f98 ["INT_ADD", "register:40f0:8", ["const:ae5f98:8", "const:4:8"]]
+ 00ae5f98 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae5f98 bytes 66e00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-770d541f0bc2698763d77be22c3aa1d5"></a>

### [`00ae609c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae609c.md) → [`00ae6164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6164.md) _ZN8firebase4util10uribuilder12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.50% / 新版 57.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae609c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae60a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae60a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae609c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae60a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae60a4",
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
      "00ae6164",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ae6168",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae616c",
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

- 旧版 [`00ae609c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae609c.md#insn-00ae609c) · [`00ae60a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae609c.md#insn-00ae60a0) · [`00ae60a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae609c.md#insn-00ae60a4)

~~~diff
- 00ae609c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae609c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae609c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae609c bytes f50f1df8
- 00ae60a0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae60a0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae60a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae60a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae60a0 bytes f44f01a9
- 00ae60a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae60a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae60a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae60a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae60a4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a2e52d3b351d108fba730c0321f0068"></a>

### [`00ae6258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6258.md) → [`00ae6320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6320.md) _ZN8firebase4util10uribuilder10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 33.33% / 新版 33.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae626c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ae6334"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6278"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae626c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae627c"
      ]
    ],
    [
      "unmatched:00ae6274",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae6278",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae6334",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6344"
      ]
    ],
    [
      "00ae633c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae6340",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6258.md#insn-00ae626c) · [`00ae6278`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6258.md#insn-00ae6278) · [`00ae6290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6258.md#insn-00ae6290)

~~~diff
- 00ae626c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00ae626c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae626c bytes 8b000054
- 00ae6278 ["INT_ADD", "register:40f0:8", ["const:ae6278:8", "const:4:8"]]
- 00ae6278 ["CALL", null, ["callee:00bde130:8"]]
- 00ae6278 bytes 82df0394
- 00ae6290 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae6290 ["RETURN", null, ["register:0:8"]]
- 00ae6290 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b50a5b1b924d23578d250f6472acf676"></a>

### [`00ae639c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae639c.md) → [`00ae6464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6464.md) _ZN8firebase4util3url8GetClassEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00ae63a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00ae646c"
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
      "unmatched:00ae63a0",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6468",
      "READ",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae63a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae639c.md#insn-00ae63a4) · [`00ae639c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae639c.md#insn-00ae639c)
- 新版 `00ae646c`（命令位置の公開資料なし）

~~~diff
- 00ae63a4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae63a4 ["RETURN", null, ["register:0:8"]]
- 00ae63a4 bytes c0035fd6
+ 00ae646c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00ae646c ["RETURN", null, ["register:0:8"]]
+ 00ae646c bytes c0035fd6
- 00ae639c ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae639c bytes c82d00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3394b5c81b78e40f0272188f67e6009"></a>

### [`00ae6444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6444.md) → [`00ae650c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae650c.md) _ZN8firebase4util3url12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6480"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae64d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae6548"
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
      "00ae6520",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae645c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae659c"
      ]
    ],
    [
      "00ae652c",
      "READ",
      [
        "storage",
        "010a0370",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae6520",
      "READ",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6524",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae659c"
      ]
    ],
    [
      "00ae652c",
      "READ",
      [
        "storage",
        "010a0430",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae645c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6444.md#insn-00ae645c) · [`00ae647c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6444.md#insn-00ae647c) · [`00ae6480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6444.md#insn-00ae6480)

~~~diff
- 00ae645c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae645c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00ae645c bytes c10300b4
- 00ae647c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae647c ["INT_ADD", "register:40f0:8", ["const:ae647c:8", "const:4:8"]]
- 00ae647c ["CALLIND", null, ["register:0:8"]]
- 00ae647c bytes 00013fd6
- 00ae6480 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae6480 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae6480 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:370:8"]]
- 00ae6480 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae6480 bytes bfc20d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e9e58ae92aa773809f2b7adb6ce3bbb"></a>

### [`00ae6554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6554.md) → [`00ae661c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae661c.md) _ZN8firebase4util3url11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6554"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6558"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6558"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae6554",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae6558",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae6568",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae6578"
      ]
    ]
  ],
  "added": [
    [
      "00ae661c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae6620",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae6630",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6640"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6554.md#insn-00ae6554) · [`00ae6558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6554.md#insn-00ae6558) · [`00ae6568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6554.md#insn-00ae6568)

~~~diff
- 00ae6554 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae6554 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae6554 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae6554 bytes f30f1ef8
- 00ae6558 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae6558 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae6558 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae6558 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae6558 bytes fd7b01a9
- 00ae6568 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00ae6568 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae6568 bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3805dc6969a4a9ed7eb2391d47f1ce8d"></a>

### [`00ae6600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6600.md) → [`00ae66c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae66c8.md) _ZN8firebase4util3url10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6620"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00ae66e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6638"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae66dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae6624"
      ]
    ],
    [
      "unmatched:00ae661c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae6620",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae66dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae66ec"
      ]
    ],
    [
      "00ae66e4",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae66e8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6600.md#insn-00ae6620) · [`00ae6638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6600.md#insn-00ae6638)
- 新版 `00ae66e8`（命令位置の公開資料なし）

~~~diff
- 00ae6620 ["INT_ADD", "register:40f0:8", ["const:ae6620:8", "const:4:8"]]
- 00ae6620 ["CALL", null, ["callee:00bde130:8"]]
- 00ae6620 bytes 98de0394
- 00ae6638 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae6638 ["RETURN", null, ["register:0:8"]]
- 00ae6638 bytes c0035fd6
+ 00ae66e8 ["INT_ADD", "register:40f0:8", ["const:ae66e8:8", "const:4:8"]]
+ 00ae66e8 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae66e8 bytes 92de0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91c1636a43c480a7a216ecabf9d1420d"></a>

### [`00ae6aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6aec.md) → [`00ae6bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6bb4.md) _ZN8firebase4util16dex_class_loader8GetClassEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00ae6af4"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00ae6bbc"
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
      "unmatched:00ae6af0",
      "READ",
      [
        "storage",
        "010a03c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6bb8",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6af4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6aec.md#insn-00ae6af4) · [`00ae6aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6aec.md#insn-00ae6aec)
- 新版 `00ae6bbc`（命令位置の公開資料なし）

~~~diff
- 00ae6af4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae6af4 ["RETURN", null, ["register:0:8"]]
- 00ae6af4 bytes c0035fd6
+ 00ae6bbc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00ae6bbc ["RETURN", null, ["register:0:8"]]
+ 00ae6bbc bytes c0035fd6
- 00ae6aec ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae6aec bytes c82d00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-643645580b073204084fbef1aab72f8e"></a>

### [`00ae6af8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6af8.md) → [`00ae6bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6bc0.md) _ZN8firebase4util16dex_class_loader15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 20.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 4件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6b80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae6c48"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6b38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae6bd4",
      "READ",
      [
        "storage",
        "010a03c8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae6b2c",
      "READ",
      [
        "storage",
        "010a03c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6c1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae6b78"
      ]
    ]
  ],
  "added": [
    [
      "00ae6bd4",
      "READ",
      [
        "storage",
        "010a0488",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae6bf4",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6c1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6c40"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6b38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6af8.md#insn-00ae6b38) · [`00ae6b4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6af8.md#insn-00ae6b4c) · [`00ae6b64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6af8.md#insn-00ae6b64)

~~~diff
- 00ae6b38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae6b38 ["INT_ADD", "register:40f0:8", ["const:ae6b38:8", "const:4:8"]]
- 00ae6b38 ["CALLIND", null, ["register:0:8"]]
- 00ae6b38 bytes 00013fd6
- 00ae6b4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae6b4c ["INT_ADD", "register:40f0:8", ["const:ae6b4c:8", "const:4:8"]]
- 00ae6b4c ["CALLIND", null, ["register:0:8"]]
- 00ae6b4c bytes 00013fd6
- 00ae6b64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae6b64 ["INT_ADD", "register:40f0:8", ["const:ae6b64:8", "const:4:8"]]
- 00ae6b64 ["CALLIND", null, ["register:0:8"]]
- 00ae6b64 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e09d27ce7b69c6a3a20735bfe5535848"></a>

### [`00ae6ca4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6ca4.md) → [`00ae6d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6d6c.md) _ZN8firebase4util16dex_class_loader11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6cc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00ae6d8c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6cdc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae6d80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae6cc8"
      ]
    ],
    [
      "unmatched:00ae6cc0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae6cc4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae6d80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6d90"
      ]
    ],
    [
      "00ae6d88",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae6d8c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6cc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6ca4.md#insn-00ae6cc4) · [`00ae6cdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6ca4.md#insn-00ae6cdc)
- 新版 `00ae6d8c`（命令位置の公開資料なし）

~~~diff
- 00ae6cc4 ["INT_ADD", "register:40f0:8", ["const:ae6cc4:8", "const:4:8"]]
- 00ae6cc4 ["CALL", null, ["callee:00bde130:8"]]
- 00ae6cc4 bytes efdc0394
- 00ae6cdc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae6cdc ["RETURN", null, ["register:0:8"]]
- 00ae6cdc bytes c0035fd6
+ 00ae6d8c ["INT_ADD", "register:40f0:8", ["const:ae6d8c:8", "const:4:8"]]
+ 00ae6d8c ["CALL", null, ["callee:00bde130:8"]]
+ 00ae6d8c bytes e9dc0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10d7446cb417fc553a8e7c9a6ac507ed"></a>

### [`00ae6d50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6d50.md) → [`00ae6e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6e18.md) _ZN8firebase4util16dex_class_loader10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6d70"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00ae6e38"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6d88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae6e2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae6d74"
      ]
    ],
    [
      "unmatched:00ae6d6c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae6d70",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae6e2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6e3c"
      ]
    ],
    [
      "00ae6e34",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae6e38",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6d70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6d50.md#insn-00ae6d70) · [`00ae6d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6d50.md#insn-00ae6d88)
- 新版 `00ae6e38`（命令位置の公開資料なし）

~~~diff
- 00ae6d70 ["INT_ADD", "register:40f0:8", ["const:ae6d70:8", "const:4:8"]]
- 00ae6d70 ["CALL", null, ["callee:00bde130:8"]]
- 00ae6d70 bytes c4dc0394
- 00ae6d88 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae6d88 ["RETURN", null, ["register:0:8"]]
- 00ae6d88 bytes c0035fd6
+ 00ae6e38 ["INT_ADD", "register:40f0:8", ["const:ae6e38:8", "const:4:8"]]
+ 00ae6e38 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae6e38 bytes bedc0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-156f8aaebc222383a9ea2c337e64022d"></a>

### [`00ae704c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae704c.md) → [`00ae7114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7114.md) _ZN8firebase4util9resources11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae706c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00ae7134"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7084"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae7128",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae7070"
      ]
    ],
    [
      "unmatched:00ae7068",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae706c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae7128",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae7138"
      ]
    ],
    [
      "00ae7130",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae7134",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae706c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae704c.md#insn-00ae706c) · [`00ae7084`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae704c.md#insn-00ae7084)
- 新版 `00ae7134`（命令位置の公開資料なし）

~~~diff
- 00ae706c ["INT_ADD", "register:40f0:8", ["const:ae706c:8", "const:4:8"]]
- 00ae706c ["CALL", null, ["callee:00bde130:8"]]
- 00ae706c bytes 05dc0394
- 00ae7084 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae7084 ["RETURN", null, ["register:0:8"]]
- 00ae7084 bytes c0035fd6
+ 00ae7134 ["INT_ADD", "register:40f0:8", ["const:ae7134:8", "const:4:8"]]
+ 00ae7134 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae7134 bytes ffdb0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afbc09086d126922eb9f093be042f1cc"></a>

### [`00ae70f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae70f8.md) → [`00ae71c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae71c0.md) _ZN8firebase4util9resources10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 26.67% / 新版 26.67%

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
      "site": "00ae70f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae70fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae70fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae70f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae70fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae71d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae711c"
      ]
    ]
  ],
  "added": [
    [
      "00ae71c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae71c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae71d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae71e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae70f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae70f8.md#insn-00ae70f8) · [`00ae70fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae70f8.md#insn-00ae70fc) · [`00ae7118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae70f8.md#insn-00ae7118)

~~~diff
- 00ae70f8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae70f8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae70f8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae70f8 bytes f30f1ef8
- 00ae70fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae70fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae70fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae70fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae70fc bytes fd7b01a9
- 00ae7118 ["INT_ADD", "register:40f0:8", ["const:ae7118:8", "const:4:8"]]
- 00ae7118 ["CALL", null, ["callee:00bde130:8"]]
- 00ae7118 bytes dadb0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67cde1a6efcc44d241a074e2eba20284"></a>

### [`00ae7174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7174.md) → [`00ae723c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae723c.md) _ZN8firebase4util8activity19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae71a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae7268"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7188"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae7184",
      "READ",
      [
        "storage",
        "010a0408",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae7188",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae71a4"
      ]
    ],
    [
      "unmatched:00ae7190",
      "PARAM",
      [
        "storage",
        "002ad342",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae724c",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7250",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae726c"
      ]
    ],
    [
      "00ae7258",
      "PARAM",
      [
        "storage",
        "002ad339",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7174.md#insn-00ae7188) · [`00ae7198`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7174.md#insn-00ae7198) · [`00ae71a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7174.md#insn-00ae71a0)

~~~diff
- 00ae7188 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae7188 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae7188 bytes e80000b5
- 00ae7198 ["INT_ADD", "register:40f0:8", ["const:ae7198:8", "const:4:8"]]
- 00ae7198 ["CALL", null, ["callee:00bde040:8"]]
- 00ae7198 bytes 7edb0394
- 00ae71a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:408:8"]]
- 00ae71a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae71a0 bytes 600602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e19d2caf63cea1af7499cde8fb03afb4"></a>

### [`00ae73f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae73f4.md) → [`00ae74bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae74bc.md) _ZN8firebase4util8activity11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde5d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde5d0.md) · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde680.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7414"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00ae74dc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae742c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae74d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae7418"
      ]
    ],
    [
      "unmatched:00ae7410",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae7414",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae74d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae74e0"
      ]
    ],
    [
      "00ae74d8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae74dc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7414`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae73f4.md#insn-00ae7414) · [`00ae742c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae73f4.md#insn-00ae742c)
- 新版 `00ae74dc`（命令位置の公開資料なし）

~~~diff
- 00ae7414 ["INT_ADD", "register:40f0:8", ["const:ae7414:8", "const:4:8"]]
- 00ae7414 ["CALL", null, ["callee:00bde130:8"]]
- 00ae7414 bytes 1bdb0394
- 00ae742c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae742c ["RETURN", null, ["register:0:8"]]
- 00ae742c bytes c0035fd6
+ 00ae74dc ["INT_ADD", "register:40f0:8", ["const:ae74dc:8", "const:4:8"]]
+ 00ae74dc ["CALL", null, ["callee:00bde130:8"]]
+ 00ae74dc bytes 15db0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1edcb4b5ca67df335cd3eb92be136ed4"></a>

### [`00ae74a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae74a0.md) → [`00ae7568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7568.md) _ZN8firebase4util8activity10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae74c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00ae7588"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae74d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae757c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae74c4"
      ]
    ],
    [
      "unmatched:00ae74bc",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae74c0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae757c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae758c"
      ]
    ],
    [
      "00ae7584",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae7588",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae74c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae74a0.md#insn-00ae74c0) · [`00ae74d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae74a0.md#insn-00ae74d8)
- 新版 `00ae7588`（命令位置の公開資料なし）

~~~diff
- 00ae74c0 ["INT_ADD", "register:40f0:8", ["const:ae74c0:8", "const:4:8"]]
- 00ae74c0 ["CALL", null, ["callee:00bde130:8"]]
- 00ae74c0 bytes f0da0394
- 00ae74d8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae74d8 ["RETURN", null, ["register:0:8"]]
- 00ae74d8 bytes c0035fd6
+ 00ae7588 ["INT_ADD", "register:40f0:8", ["const:ae7588:8", "const:4:8"]]
+ 00ae7588 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae7588 bytes eada0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62d491d1788048ba8c86ae2f8d26e137"></a>

### [`00ae751c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae751c.md) → [`00ae75e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae75e4.md) _ZN8firebase4util10array_list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae751c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7520"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7520"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae751c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae7520",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae752c",
      "READ",
      [
        "storage",
        "010a0470",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae75e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae75e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae75f4",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae751c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae751c.md#insn-00ae751c) · [`00ae7520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae751c.md#insn-00ae7520) · [`00ae7530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae751c.md#insn-00ae7530)

~~~diff
- 00ae751c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae751c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae751c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae751c bytes f30f1ef8
- 00ae7520 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae7520 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae7520 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae7520 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae7520 bytes fd7b01a9
- 00ae7530 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae7530 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae7530 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f69e6b4ae5ee76067819db704a171eda"></a>

### [`00ae779c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae779c.md) → [`00ae7864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7864.md) _ZN8firebase4util10array_list11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf30.md) · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bddfe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddfe0.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae77bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00ae7884"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae77d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae7878",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae77c0"
      ]
    ],
    [
      "unmatched:00ae77b8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae77bc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae7878",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae7888"
      ]
    ],
    [
      "00ae7880",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae7884",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae77bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae779c.md#insn-00ae77bc) · [`00ae77d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae779c.md#insn-00ae77d4)
- 新版 `00ae7884`（命令位置の公開資料なし）

~~~diff
- 00ae77bc ["INT_ADD", "register:40f0:8", ["const:ae77bc:8", "const:4:8"]]
- 00ae77bc ["CALL", null, ["callee:00bde130:8"]]
- 00ae77bc bytes 31da0394
- 00ae77d4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae77d4 ["RETURN", null, ["register:0:8"]]
- 00ae77d4 bytes c0035fd6
+ 00ae7884 ["INT_ADD", "register:40f0:8", ["const:ae7884:8", "const:4:8"]]
+ 00ae7884 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae7884 bytes 2bda0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5a0a0e141b217c66fdbf4d3b198d311"></a>

### [`00ae7904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7904.md) → [`00ae79cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae79cc.md) _ZN8firebase4util21asset_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7934"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae79fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7918"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae7914",
      "READ",
      [
        "storage",
        "010a04a0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae7918",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae7a00"
      ]
    ],
    [
      "unmatched:00ae7924",
      "PARAM",
      [
        "storage",
        "002ae3cd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae79dc",
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae79e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae7a00"
      ]
    ],
    [
      "00ae79ec",
      "PARAM",
      [
        "storage",
        "002ae339",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7904.md#insn-00ae7918) · [`00ae792c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7904.md#insn-00ae792c) · [`00ae7934`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7904.md#insn-00ae7934)

~~~diff
- 00ae7918 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae7918 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae7918 bytes 080100b5
- 00ae792c ["INT_ADD", "register:40f0:8", ["const:ae792c:8", "const:4:8"]]
- 00ae792c ["CALL", null, ["callee:00bde040:8"]]
- 00ae792c bytes 99d90394
- 00ae7934 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
- 00ae7934 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7934 bytes 605202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-719dd30efae073e0578feb3bd55b21a0"></a>

### [`00ae7b44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7b44.md) → [`00ae7c0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7c0c.md) _ZN8firebase4util21asset_file_descriptor11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7b64"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00ae7c2c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7b7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae7c20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae7b68"
      ]
    ],
    [
      "unmatched:00ae7b60",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae7b64",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae7c20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae7c30"
      ]
    ],
    [
      "00ae7c28",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae7c2c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7b64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7b44.md#insn-00ae7b64) · [`00ae7b7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7b44.md#insn-00ae7b7c)
- 新版 `00ae7c2c`（命令位置の公開資料なし）

~~~diff
- 00ae7b64 ["INT_ADD", "register:40f0:8", ["const:ae7b64:8", "const:4:8"]]
- 00ae7b64 ["CALL", null, ["callee:00bde130:8"]]
- 00ae7b64 bytes 47d90394
- 00ae7b7c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae7b7c ["RETURN", null, ["register:0:8"]]
- 00ae7b7c bytes c0035fd6
+ 00ae7c2c ["INT_ADD", "register:40f0:8", ["const:ae7c2c:8", "const:4:8"]]
+ 00ae7c2c ["CALL", null, ["callee:00bde130:8"]]
+ 00ae7c2c bytes 41d90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a0ca92b83e8fa5290ad0adffa71a0c0"></a>

### [`00ae7c6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7c6c.md) → [`00ae7d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7d34.md) _ZN8firebase4util13boolean_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7c98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae7d60"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7c80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae7c7c",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae7c80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae7d64"
      ]
    ],
    [
      "unmatched:00ae7c88",
      "PARAM",
      [
        "storage",
        "002985dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae7d44",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7d48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae7d64"
      ]
    ],
    [
      "00ae7d50",
      "PARAM",
      [
        "storage",
        "00298669",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7c6c.md#insn-00ae7c80) · [`00ae7c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7c6c.md#insn-00ae7c90) · [`00ae7c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7c6c.md#insn-00ae7c98)

~~~diff
- 00ae7c80 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae7c80 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae7c80 bytes e80000b5
- 00ae7c90 ["INT_ADD", "register:40f0:8", ["const:ae7c90:8", "const:4:8"]]
- 00ae7c90 ["CALL", null, ["callee:00bde040:8"]]
- 00ae7c90 bytes c0d80394
- 00ae7c98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
- 00ae7c98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7c98 bytes 606202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-141a725d7bf888fae506c1566416aa62"></a>

### [`00ae7eec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7eec.md) → [`00ae7fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7fb4.md) _ZN8firebase4util13boolean_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde340.md) · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde3f0.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7f0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00ae7fd4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7f24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae7fc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae7f10"
      ]
    ],
    [
      "unmatched:00ae7f08",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae7f0c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae7fc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae7fd8"
      ]
    ],
    [
      "00ae7fd0",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae7fd4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7f0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7eec.md#insn-00ae7f0c) · [`00ae7f24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7eec.md#insn-00ae7f24)
- 新版 `00ae7fd4`（命令位置の公開資料なし）

~~~diff
- 00ae7f0c ["INT_ADD", "register:40f0:8", ["const:ae7f0c:8", "const:4:8"]]
- 00ae7f0c ["CALL", null, ["callee:00bde130:8"]]
- 00ae7f0c bytes 5dd80394
- 00ae7f24 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae7f24 ["RETURN", null, ["register:0:8"]]
- 00ae7f24 bytes c0035fd6
+ 00ae7fd4 ["INT_ADD", "register:40f0:8", ["const:ae7fd4:8", "const:4:8"]]
+ 00ae7fd4 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae7fd4 bytes 57d80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5601c7fe6f0d7169e08748294477ad16"></a>

### [`00ae7f98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7f98.md) → [`00ae8060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8060.md) _ZN8firebase4util13boolean_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7fb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00ae8080"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7fd0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae8074",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae7fbc"
      ]
    ],
    [
      "unmatched:00ae7fb4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae7fb8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae8074",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae8084"
      ]
    ],
    [
      "00ae807c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae8080",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7fb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7f98.md#insn-00ae7fb8) · [`00ae7fd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7f98.md#insn-00ae7fd0)
- 新版 `00ae8080`（命令位置の公開資料なし）

~~~diff
- 00ae7fb8 ["INT_ADD", "register:40f0:8", ["const:ae7fb8:8", "const:4:8"]]
- 00ae7fb8 ["CALL", null, ["callee:00bde130:8"]]
- 00ae7fb8 bytes 32d80394
- 00ae7fd0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae7fd0 ["RETURN", null, ["register:0:8"]]
- 00ae7fd0 bytes c0035fd6
+ 00ae8080 ["INT_ADD", "register:40f0:8", ["const:ae8080:8", "const:4:8"]]
+ 00ae8080 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae8080 bytes 2cd80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75074733cc5d84a2fb95053fc6ba1626"></a>

### [`00ae7fd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7fd4.md) → [`00ae809c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae809c.md) _ZN8firebase4util6bundle19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7fd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7fd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7fd8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae7fd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae7fd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae7fe4",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae809c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae80a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae80ac",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7fd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7fd4.md#insn-00ae7fd4) · [`00ae7fd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7fd4.md#insn-00ae7fd8) · [`00ae7fe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7fd4.md#insn-00ae7fe8)

~~~diff
- 00ae7fd4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae7fd4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae7fd4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae7fd4 bytes f30f1ef8
- 00ae7fd8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae7fd8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae7fd8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae7fd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae7fd8 bytes fd7b01a9
- 00ae7fe8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae7fe8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae7fe8 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f6094040a88dda095e7bbfb3b87fe88"></a>

### [`00ae8294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8294.md) → [`00ae835c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae835c.md) _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde010.md) · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae82b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00ae837c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae82cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae8370",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae82b8"
      ]
    ],
    [
      "unmatched:00ae82b0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae82b4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae8370",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae8380"
      ]
    ],
    [
      "00ae8378",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae837c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae82b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8294.md#insn-00ae82b4) · [`00ae82cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8294.md#insn-00ae82cc)
- 新版 `00ae837c`（命令位置の公開資料なし）

~~~diff
- 00ae82b4 ["INT_ADD", "register:40f0:8", ["const:ae82b4:8", "const:4:8"]]
- 00ae82b4 ["CALL", null, ["callee:00bde130:8"]]
- 00ae82b4 bytes 73d70394
- 00ae82cc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae82cc ["RETURN", null, ["register:0:8"]]
- 00ae82cc bytes c0035fd6
+ 00ae837c ["INT_ADD", "register:40f0:8", ["const:ae837c:8", "const:4:8"]]
+ 00ae837c ["CALL", null, ["callee:00bde130:8"]]
+ 00ae837c bytes 6dd70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c17c1e51e84506146ad2f867929c4d5"></a>

### [`00ae837c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae837c.md) → [`00ae8444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8444.md) _ZN8firebase4util10byte_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae837c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8380"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8380"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae837c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae8380",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae838c",
      "READ",
      [
        "storage",
        "010a0548",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8444",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae8448",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae8454",
      "READ",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae837c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae837c.md#insn-00ae837c) · [`00ae8380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae837c.md#insn-00ae8380) · [`00ae8390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae837c.md#insn-00ae8390)

~~~diff
- 00ae837c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae837c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae837c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae837c bytes f30f1ef8
- 00ae8380 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae8380 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae8380 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae8380 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae8380 bytes fd7b01a9
- 00ae8390 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae8390 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00ae8390 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d433ae704fd9d75b57ede2812e558e54"></a>

### [`00ae8490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8490.md) → [`00ae8558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8558.md) _ZN8firebase4util10byte_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.85% / 新版 53.85%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8518"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae85e0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae84d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae856c",
      "READ",
      [
        "storage",
        "010a0550",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae8578",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae851c"
      ]
    ],
    [
      "unmatched:00ae84c4",
      "READ",
      [
        "storage",
        "010a0548",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae856c",
      "READ",
      [
        "storage",
        "010a0610",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae8578",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae85e4"
      ]
    ],
    [
      "00ae858c",
      "READ",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae84d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8490.md#insn-00ae84d0) · [`00ae84e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8490.md#insn-00ae84e4) · [`00ae850c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8490.md#insn-00ae850c)

~~~diff
- 00ae84d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae84d0 ["INT_ADD", "register:40f0:8", ["const:ae84d0:8", "const:4:8"]]
- 00ae84d0 ["CALLIND", null, ["register:0:8"]]
- 00ae84d0 bytes 00013fd6
- 00ae84e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae84e4 ["INT_ADD", "register:40f0:8", ["const:ae84e4:8", "const:4:8"]]
- 00ae84e4 ["CALLIND", null, ["register:0:8"]]
- 00ae84e4 bytes 00013fd6
- 00ae850c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae850c ["INT_ADD", "register:40f0:8", ["const:ae850c:8", "const:4:8"]]
- 00ae850c ["CALLIND", null, ["register:0:8"]]
- 00ae850c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9079860abb7e31167f9cea85b313f66c"></a>

### [`00ae863c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae863c.md) → [`00ae8704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8704.md) _ZN8firebase4util10byte_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 13.33% / 新版 13.33%

CFGの説明率　旧版 14.29% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae863c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8640"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8640"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae863c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae8640",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae8650",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae8660"
      ]
    ]
  ],
  "added": [
    [
      "00ae8704",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae8708",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae8718",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae8728"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae863c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae863c.md#insn-00ae863c) · [`00ae8640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae863c.md#insn-00ae8640) · [`00ae8650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae863c.md#insn-00ae8650)

~~~diff
- 00ae863c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae863c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae863c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae863c bytes f30f1ef8
- 00ae8640 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae8640 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae8640 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae8640 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae8640 bytes fd7b01a9
- 00ae8650 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00ae8650 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae8650 bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0545cf1b4c09313952a7b79732ee9dfa"></a>

### [`00ae86e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae86e8.md) → [`00ae87b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae87b0.md) _ZN8firebase4util10byte_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 40.00% / 新版 40.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae86e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae86ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae86ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae86e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae86ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae87c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae870c"
      ]
    ]
  ],
  "added": [
    [
      "00ae87b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae87b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae87c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae87d4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae86e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae86e8.md#insn-00ae86e8) · [`00ae86ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae86e8.md#insn-00ae86ec)
- 新版 `00ae87b0`（命令位置の公開資料なし）

~~~diff
- 00ae86e8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae86e8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae86e8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae86e8 bytes f30f1ef8
- 00ae86ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae86ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae86ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae86ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae86ec bytes fd7b01a9
+ 00ae87b0 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 00ae87b0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00ae87b0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00ae87b0 bytes f30f1ef8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12cad9ff7dc6ea91138ec8fb149ab9c4"></a>

### [`00ae8724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8724.md) → [`00ae87ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae87ec.md) _ZN8firebase4util15character_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8724"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8728"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8728"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae8724",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae8728",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae8734",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae87ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae87f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae87fc",
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8724.md#insn-00ae8724) · [`00ae8728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8724.md#insn-00ae8728) · [`00ae8738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8724.md#insn-00ae8738)

~~~diff
- 00ae8724 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae8724 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae8724 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae8724 bytes f30f1ef8
- 00ae8728 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae8728 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae8728 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae8728 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae8728 bytes fd7b01a9
- 00ae8738 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae8738 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae8738 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4e8070d48b46c2b67e0a9b162f1e52e"></a>

### [`00ae8764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8764.md) → [`00ae882c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae882c.md) _ZN8firebase4util15character_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8764"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8768"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8768"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae8764",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae8768",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae8774",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae882c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae8830",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae883c",
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8764.md#insn-00ae8764) · [`00ae8768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8764.md#insn-00ae8768) · [`00ae8778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8764.md#insn-00ae8778)

~~~diff
- 00ae8764 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae8764 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae8764 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae8764 bytes f30f1ef8
- 00ae8768 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae8768 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae8768 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae8768 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae8768 bytes fd7b01a9
- 00ae8778 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae8778 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00ae8778 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b18892c69d33d4f2edde0abf9b863a04"></a>

### [`00ae87a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae87a4.md) → [`00ae886c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae886c.md) _ZN8firebase4util15character_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 29.41% / 新版 29.41%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae87d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae889c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae87cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae87b4",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8880",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae87d8"
      ]
    ],
    [
      "unmatched:00ae87c4",
      "PARAM",
      [
        "storage",
        "002aafea",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae887c",
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8880",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae88a0"
      ]
    ],
    [
      "00ae888c",
      "PARAM",
      [
        "storage",
        "002aaff0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae87cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae87a4.md#insn-00ae87cc) · [`00ae87d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae87a4.md#insn-00ae87d4) · [`00ae87e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae87a4.md#insn-00ae87e4)

~~~diff
- 00ae87cc ["INT_ADD", "register:40f0:8", ["const:ae87cc:8", "const:4:8"]]
- 00ae87cc ["CALL", null, ["callee:00bde040:8"]]
- 00ae87cc bytes f1d50394
- 00ae87d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
- 00ae87d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae87d4 bytes 60ba02f9
- 00ae87e4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae87e4 ["RETURN", null, ["register:0:8"]]
- 00ae87e4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dd9a0277d19380bff9e1094f809f98a"></a>

### [`00ae882c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae882c.md) → [`00ae88f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae88f4.md) _ZN8firebase4util15character_class8GetClassEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8834"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00ae88fc"
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
      "unmatched:00ae8830",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae88f8",
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae882c.md#insn-00ae8834) · [`00ae882c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae882c.md#insn-00ae882c)
- 新版 `00ae88fc`（命令位置の公開資料なし）

~~~diff
- 00ae8834 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae8834 ["RETURN", null, ["register:0:8"]]
- 00ae8834 bytes c0035fd6
+ 00ae88fc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00ae88fc ["RETURN", null, ["register:0:8"]]
+ 00ae88fc bytes c0035fd6
- 00ae882c ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae882c bytes c82d0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

