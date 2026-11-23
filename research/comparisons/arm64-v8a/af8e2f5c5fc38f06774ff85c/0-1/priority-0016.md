# v15.7.2 → v15.7.3 · 最優先の変更候補 (16)

[一覧の目次](README.md)

<a id="compare-5e8b7facd5da9ee99c7b7ebdd88de165"></a>

### [`0053fe04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053f/0053fe04.md) → [`0053fe04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053fe04.md) FUN_0053fe04

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0053feb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053f/0053feb8.md) [`005401c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/005401c0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`0053feb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053feb8.md) [`005401c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005401c0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0053fe10",
      "incomplete_value": false,
      "site": "0053fe14",
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
    "old": {
      "definition_site": "0053fe10",
      "incomplete_value": false,
      "site": "0053fe14",
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
      "0053fe10",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053fe10",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053fe10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053f/0053fe04.md#insn-0053fe10)
- 新版 `0053fe10`（命令位置の公開資料なし）

~~~diff
- 0053fe10 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0053fe10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053fe10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053fe10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053fe10 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0053fe10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053fe10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053fe10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053fe10 bytes 00280c91
+ 0053fe10 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18edf2cf61d35678d55468c2e673dc14"></a>

### [`0054050c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/0054050c.md) → [`0054050c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/0054050c.md) FUN_0054050c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)

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
      "definition_site": "00540510",
      "incomplete_value": false,
      "site": "00540514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00540510",
      "incomplete_value": false,
      "site": "00540514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:380:8"
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
      "00540514",
      "DATA",
      [
        "storage",
        "00bee380",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00540514",
      "DATA",
      [
        "storage",
        "00bee430",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00540510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/0054050c.md#insn-00540510)
- 新版 `00540510`（命令位置の公開資料なし）

~~~diff
- 00540510 ["COPY", "tmp:0:8", ["const:380:8"]]
- 00540510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00540510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00540510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00540510 ["COPY", "tmp:0:8", ["const:430:8"]]
+ 00540510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00540510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00540510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00540510 bytes 08010e91
+ 00540510 bytes 08c11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50f5d06e7e6f37ff56468899abeb7ab4"></a>

### [`0054051c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/0054051c.md) → [`0054051c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/0054051c.md) FUN_0054051c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0054052c",
      "incomplete_value": false,
      "site": "00540534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054052c",
      "incomplete_value": false,
      "site": "00540534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:380:8"
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
      "00540534",
      "DATA",
      [
        "storage",
        "00bee380",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00540534",
      "DATA",
      [
        "storage",
        "00bee430",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054052c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/0054051c.md#insn-0054052c)
- 新版 `0054052c`（命令位置の公開資料なし）

~~~diff
- 0054052c ["COPY", "tmp:0:8", ["const:380:8"]]
- 0054052c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054052c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054052c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0054052c ["COPY", "tmp:0:8", ["const:430:8"]]
+ 0054052c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0054052c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0054052c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054052c bytes 08010e91
+ 0054052c bytes 08c11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-323e4a6f6ab61f8a03d4f0980b34d55b"></a>

### [`005405bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/005405bc.md) → [`005405bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005405bc.md) FUN_005405bc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)

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
      "definition_site": "005405c0",
      "incomplete_value": false,
      "site": "005405c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005405c0",
      "incomplete_value": false,
      "site": "005405c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
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
      "005405c4",
      "DATA",
      [
        "storage",
        "00bee3d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005405c4",
      "DATA",
      [
        "storage",
        "00bee480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005405c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/005405bc.md#insn-005405c0)
- 新版 `005405c0`（命令位置の公開資料なし）

~~~diff
- 005405c0 ["COPY", "tmp:0:8", ["const:3d0:8"]]
- 005405c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005405c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005405c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005405c0 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 005405c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005405c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005405c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005405c0 bytes 08410f91
+ 005405c0 bytes 08011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21744dc83104c8d942291950d3bacde9"></a>

### [`005405cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/005405cc.md) → [`005405cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005405cc.md) FUN_005405cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "005405dc",
      "incomplete_value": false,
      "site": "005405e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005405dc",
      "incomplete_value": false,
      "site": "005405e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
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
      "005405e4",
      "DATA",
      [
        "storage",
        "00bee3d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005405e4",
      "DATA",
      [
        "storage",
        "00bee480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005405dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/005405cc.md#insn-005405dc)
- 新版 `005405dc`（命令位置の公開資料なし）

~~~diff
- 005405dc ["COPY", "tmp:0:8", ["const:3d0:8"]]
- 005405dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005405dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005405dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005405dc ["COPY", "tmp:0:8", ["const:480:8"]]
+ 005405dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005405dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005405dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005405dc bytes 08410f91
+ 005405dc bytes 08011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1fc04247682af9425d312bfdfaf48e5"></a>

### [`00540614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/00540614.md) → [`00540614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/00540614.md) FUN_00540614

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0054062c",
      "incomplete_value": false,
      "site": "00540630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054062c",
      "incomplete_value": false,
      "site": "00540630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
      "00540630",
      "DATA",
      [
        "storage",
        "00bee420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00540630",
      "DATA",
      [
        "storage",
        "00bee4d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054062c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/00540614.md#insn-0054062c)
- 新版 `0054062c`（命令位置の公開資料なし）

~~~diff
- 0054062c ["COPY", "tmp:0:8", ["const:420:8"]]
- 0054062c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0054062c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0054062c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0054062c ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 0054062c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0054062c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0054062c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0054062c bytes 29811091
+ 0054062c bytes 29411391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07ea27edc432c3e4466dce66d63fa41d"></a>

### [`00540664`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/00540664.md) → [`00540664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/00540664.md) FUN_00540664

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0054067c",
      "incomplete_value": false,
      "site": "00540680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054067c",
      "incomplete_value": false,
      "site": "00540680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
      "00540680",
      "DATA",
      [
        "storage",
        "00bee420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00540680",
      "DATA",
      [
        "storage",
        "00bee4d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054067c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/00540664.md#insn-0054067c)
- 新版 `0054067c`（命令位置の公開資料なし）

~~~diff
- 0054067c ["COPY", "tmp:0:8", ["const:420:8"]]
- 0054067c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0054067c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0054067c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0054067c ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 0054067c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0054067c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0054067c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0054067c bytes 29811091
+ 0054067c bytes 29411391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23c4c0930c0a10516bb378e87d6009af"></a>

### [`005406b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/005406b0.md) → [`005406b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005406b0.md) FUN_005406b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005406e4",
      "incomplete_value": false,
      "site": "005406e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005406e4",
      "incomplete_value": false,
      "site": "005406e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:420:8"
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
      "005406e4",
      "DATA",
      [
        "storage",
        "00bee420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005406e4",
      "DATA",
      [
        "storage",
        "00bee4d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005406d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/005406b0.md#insn-005406d8) · [`005406e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/005406b0.md#insn-005406e0)
- 新版 `005406d8`（命令位置の公開資料なし） · `005406e0`（命令位置の公開資料なし）

~~~diff
- 005406d8 ["COPY", "tmp:0:8", ["const:420:8"]]
- 005406d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005406d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005406d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005406d8 ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 005406d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005406d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005406d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005406d8 bytes 4a811091
+ 005406d8 bytes 4a411391
- 005406e0 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 005406e0 bytes f50300aa
+ 005406e0 ["COPY", "register:40a8:8", ["register:4000:8"]]
+ 005406e0 bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bf4f0e1829273512c9a49fa68d77606"></a>

### [`005408b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/005408b8.md) → [`005408b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005408b8.md) FUN_005408b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005408e4",
      "incomplete_value": true,
      "site": "005408e4",
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
      "definition_site": "005408e4",
      "incomplete_value": true,
      "site": "005408e4",
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
      "005408dc",
      "READ",
      [
        "storage",
        "00c25d00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005408dc",
      "READ",
      [
        "storage",
        "00c25dc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005408dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/005408b8.md#insn-005408dc)
- 新版 `005408dc`（命令位置の公開資料なし）

~~~diff
- 005408dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d00:8"]]
- 005408dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005408dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 005408dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005408dc bytes 088146f9
+ 005408dc bytes 08e146f9
~~~


<a id="compare-7813ce80e4794b39c9237af438f7a486"></a>

### [`00540964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/00540964.md) → [`00540964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/00540964.md) FUN_00540964

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)

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
      "definition_site": "00540968",
      "incomplete_value": false,
      "site": "0054096c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00540968",
      "incomplete_value": false,
      "site": "0054096c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
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
      "0054096c",
      "DATA",
      [
        "storage",
        "00bee4a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0054096c",
      "DATA",
      [
        "storage",
        "00bee550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00540968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/00540964.md#insn-00540968)
- 新版 `00540968`（命令位置の公開資料なし）

~~~diff
- 00540968 ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 00540968 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00540968 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00540968 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00540968 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00540968 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00540968 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00540968 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00540968 bytes 08811291
+ 00540968 bytes 08411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a7aea98b59ad7f25d31fbacfb055cb7"></a>

### [`00540974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/00540974.md) → [`00540974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/00540974.md) FUN_00540974

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00540984",
      "incomplete_value": false,
      "site": "0054098c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00540984",
      "incomplete_value": false,
      "site": "0054098c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
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
      "0054098c",
      "DATA",
      [
        "storage",
        "00bee4a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0054098c",
      "DATA",
      [
        "storage",
        "00bee550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00540984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/00540974.md#insn-00540984)
- 新版 `00540984`（命令位置の公開資料なし）

~~~diff
- 00540984 ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 00540984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00540984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00540984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00540984 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00540984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00540984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00540984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00540984 bytes 08811291
+ 00540984 bytes 08411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b48e51fccbe1550d8065dedd9d4956e2"></a>

### [`005409a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/005409a4.md) → [`005409a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005409a4.md) FUN_005409a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005409b4",
      "incomplete_value": false,
      "site": "005409b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005409b4",
      "incomplete_value": false,
      "site": "005409b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
      "005409b8",
      "DATA",
      [
        "storage",
        "00bee4f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005409b8",
      "DATA",
      [
        "storage",
        "00bee5a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005409b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/005409a4.md#insn-005409b4)
- 新版 `005409b4`（命令位置の公開資料なし）

~~~diff
- 005409b4 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 005409b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005409b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005409b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005409b4 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 005409b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005409b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005409b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005409b4 bytes 29c11391
+ 005409b4 bytes 29811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c51d605eb36fe70173ffda3a8ef06d5"></a>

### [`005409c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/005409c4.md) → [`005409c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005409c4.md) FUN_005409c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0054243c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00542/0054243c.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0053f81c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053f/0053f81c.md) [`00540c2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/00540c2c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`0054243c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00542/0054243c.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0053f81c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053f81c.md) [`00540c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/00540c2c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005409f0",
      "incomplete_value": false,
      "site": "00540a0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005409f0",
      "incomplete_value": false,
      "site": "00540a0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00540a0c",
      "DATA",
      [
        "storage",
        "00bee4f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00540abc",
      "READ",
      [
        "storage",
        "00bee4f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00540a0c",
      "DATA",
      [
        "storage",
        "00bee5a0",
        null,
        "undefined *"
      ]
    ],
    [
      "00540abc",
      "READ",
      [
        "storage",
        "00bee5a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005409f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/005409c4.md#insn-005409f0)
- 新版 `005409f0`（命令位置の公開資料なし）

~~~diff
- 005409f0 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 005409f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005409f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005409f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005409f0 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 005409f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005409f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005409f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005409f0 bytes 4ac11391
+ 005409f0 bytes 4a811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-149b41d6980d8ca45e88aa666f09f59f"></a>

### [`005416b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00541/005416b0.md) → [`005416b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00541/005416b0.md) FUN_005416b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00540f58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00540/00540f58.md) [`00832d28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00832/00832d28.md) [`0086b704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086b/0086b704.md) [`008e6014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e6/008e6014.md) [`009e6000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009e6/009e6000.md) · 呼出先 9件 [`004365f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/004365f8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb060.md)
- 新版 呼出元 5件 [`00540f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/00540f58.md) [`00832d28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00832/00832d28.md) [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) [`008e6014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e6/008e6014.md) [`009e6000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e6/009e6000.md) · 呼出先 9件 [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md) [`00bdb110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb110.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005416f8",
      "incomplete_value": true,
      "site": "00541708",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005416f8",
      "incomplete_value": true,
      "site": "00541708",
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
            "const:40:8"
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
      "definition_site": "00541700",
      "incomplete_value": true,
      "site": "0054170c",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00541700",
      "incomplete_value": true,
      "site": "0054170c",
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
                "const:8:8"
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
      "definition_site": "00541760",
      "incomplete_value": true,
      "site": "00541764",
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
      "definition_site": "00541760",
      "incomplete_value": true,
      "site": "00541764",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005416e4",
      "READ",
      [
        "storage",
        "00c1ad98",
        null,
        "pointer"
      ]
    ],
    [
      "005416e8",
      "READ",
      [
        "storage",
        "00c1acc8",
        null,
        "pointer"
      ]
    ],
    [
      "00541700",
      "READ",
      [
        "storage",
        "00c13360",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "005416e4",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "005416e8",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "00541700",
      "READ",
      [
        "storage",
        "00c13410",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005416e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00541/005416b0.md#insn-005416e4) · [`005416e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00541/005416b0.md#insn-005416e8) · [`00541758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00541/005416b0.md#insn-00541758)
- 新版 `005416e4`（命令位置の公開資料なし） · `005416e8`（命令位置の公開資料なし） · `00541758`（命令位置の公開資料なし）

~~~diff
- 005416e4 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:d98:8"]]
- 005416e4 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005416e4 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:e48:8"]]
+ 005416e4 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 005416e4 bytes 5acf46f9
+ 005416e4 bytes 5a2747f9
- 005416e8 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:cc8:8"]]
- 005416e8 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 005416e8 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:d78:8"]]
+ 005416e8 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 005416e8 bytes 396746f9
+ 005416e8 bytes 39bf46f9
- 00541758 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:cd0:8"]]
- 00541758 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00541758 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d80:8"]]
+ 00541758 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 00541758 bytes d66a46f9
+ 00541758 bytes d6c246f9
~~~


<a id="compare-12ee33fc518ef1bd3b490d009e8a52d5"></a>

### [`005418bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00541/005418bc.md) → [`005418bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00541/005418bc.md) FUN_005418bc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)

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
      "definition_site": "005418c0",
      "incomplete_value": false,
      "site": "005418c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005418c0",
      "incomplete_value": false,
      "site": "005418c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:560:8"
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
      "005418c4",
      "DATA",
      [
        "storage",
        "00bee560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005418c4",
      "DATA",
      [
        "storage",
        "00bee610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005418c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00541/005418bc.md#insn-005418c0)
- 新版 `005418c0`（命令位置の公開資料なし）

~~~diff
- 005418c0 ["COPY", "tmp:0:8", ["const:560:8"]]
- 005418c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005418c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005418c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005418c0 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 005418c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005418c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005418c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005418c0 bytes 08811591
+ 005418c0 bytes 08411891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a42f1eba5864d3c3a4ba98ed4d888f7b"></a>

### [`005418cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00541/005418cc.md) → [`005418cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00541/005418cc.md) FUN_005418cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "005418dc",
      "incomplete_value": false,
      "site": "005418e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005418dc",
      "incomplete_value": false,
      "site": "005418e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:560:8"
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
      "005418e4",
      "DATA",
      [
        "storage",
        "00bee560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005418e4",
      "DATA",
      [
        "storage",
        "00bee610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005418dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00541/005418cc.md#insn-005418dc)
- 新版 `005418dc`（命令位置の公開資料なし）

~~~diff
- 005418dc ["COPY", "tmp:0:8", ["const:560:8"]]
- 005418dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005418dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005418dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005418dc ["COPY", "tmp:0:8", ["const:610:8"]]
+ 005418dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005418dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005418dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005418dc bytes 08811591
+ 005418dc bytes 08411891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9129f3891a5d913ddc61eaa5fc251709"></a>

### [`00541908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00541/00541908.md) → [`00541908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00541/00541908.md) FUN_00541908

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0053f0f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053f/0053f0f8.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`0053f0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053f0f8.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0054192c",
      "incomplete_value": false,
      "site": "0054192c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054192c",
      "incomplete_value": false,
      "site": "0054192c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
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
      "0054192c",
      "DATA",
      [
        "storage",
        "00bee5b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0054192c",
      "DATA",
      [
        "storage",
        "00bee660",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00541924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00541/00541908.md#insn-00541924) · [`00541928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00541/00541908.md#insn-00541928)
- 新版 `00541924`（命令位置の公開資料なし） · `00541928`（命令位置の公開資料なし）

~~~diff
- 00541924 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 00541924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00541924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00541924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00541924 ["COPY", "tmp:0:8", ["const:660:8"]]
+ 00541924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00541924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00541924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00541924 bytes 08c11691
+ 00541924 bytes 08811991
- 00541928 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00541928 bytes f40300aa
+ 00541928 ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 00541928 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e71414be775e24e97826f58ad6c2405a"></a>

### [`00541e74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00541/00541e74.md) → [`00541e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00541/00541e74.md) FUN_00541e74

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb010.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00541ef4",
      "incomplete_value": false,
      "site": "00541efc",
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
            "const:541:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00541ef4",
      "incomplete_value": false,
      "site": "00541efc",
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
            "const:548:8"
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
      "definition_site": "005420cc",
      "incomplete_value": false,
      "site": "005420d8",
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
            "const:ca2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005420cc",
      "incomplete_value": false,
      "site": "005420d8",
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
            "const:c15:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00541ef4",
      "PARAM",
      [
        "storage",
        "002a2548",
        null,
        null
      ]
    ],
    [
      "00542030",
      "PARAM",
      [
        "storage",
        "002928f0",
        null,
        null
      ]
    ],
    [
      "005420cc",
      "PARAM",
      [
        "storage",
        "00297c15",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00541ef4",
      "PARAM",
      [
        "storage",
        "002a2541",
        null,
        null
      ]
    ],
    [
      "00542030",
      "PARAM",
      [
        "storage",
        "0029297d",
        null,
        null
      ]
    ],
    [
      "005420cc",
      "PARAM",
      [
        "storage",
        "00297ca2",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00541ef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00541/00541e74.md#insn-00541ef4) · [`00542030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00541/00541e74.md#insn-00542030) · [`005420cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00541/00541e74.md#insn-005420cc)
- 新版 `00541ef4`（命令位置の公開資料なし） · `00542030`（命令位置の公開資料なし） · `005420cc`（命令位置の公開資料なし）

~~~diff
- 00541ef4 ["COPY", "tmp:0:8", ["const:548:8"]]
- 00541ef4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00541ef4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00541ef4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00541ef4 ["COPY", "tmp:0:8", ["const:541:8"]]
+ 00541ef4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00541ef4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00541ef4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00541ef4 bytes 21201591
+ 00541ef4 bytes 21041591
- 00542030 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 00542030 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00542030 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00542030 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00542030 ["COPY", "tmp:0:8", ["const:97d:8"]]
+ 00542030 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00542030 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00542030 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00542030 bytes 42c02391
+ 00542030 bytes 42f42591
- 005420cc ["COPY", "tmp:0:8", ["const:c15:8"]]
- 005420cc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 005420cc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 005420cc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 005420cc ["COPY", "tmp:0:8", ["const:ca2:8"]]
+ 005420cc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 005420cc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 005420cc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 005420cc bytes 42543091
+ 005420cc bytes 42883291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d41f1ab1d4b0d85e5a52f7a6a04fbea"></a>

### [`0054250c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00542/0054250c.md) → [`0054250c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00542/0054250c.md) FUN_0054250c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005418fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00541/005418fc.md) · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`005418fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00541/005418fc.md) · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00542524",
      "incomplete_value": false,
      "site": "00542528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00542524",
      "incomplete_value": false,
      "site": "00542528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
      "00542528",
      "DATA",
      [
        "storage",
        "00bee5b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00542528",
      "DATA",
      [
        "storage",
        "00bee660",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00542524`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00542/0054250c.md#insn-00542524)
- 新版 `00542524`（命令位置の公開資料なし）

~~~diff
- 00542524 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 00542524 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00542524 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00542524 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00542524 ["COPY", "tmp:0:8", ["const:660:8"]]
+ 00542524 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00542524 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00542524 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00542524 bytes 08c11691
+ 00542524 bytes 08811991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81e342bd93cf385b81005424eeceeda4"></a>

### [`005425e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00542/005425e4.md) → [`005425e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00542/005425e4.md) _INIT_27

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053e10c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e10c.md) [`00b55550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55550.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053e10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e10c.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 52.00% / 新版 52.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 10件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054260c",
      "incomplete_value": false,
      "site": "0054260c",
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
                "const:da0:8"
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
      "definition_site": "0054260c",
      "incomplete_value": false,
      "site": "0054260c",
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
                "const:ce0:8"
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
      "definition_site": "0054262c",
      "incomplete_value": false,
      "site": "0054262c",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054262c",
      "incomplete_value": false,
      "site": "0054262c",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00542634",
      "incomplete_value": false,
      "site": "00542634",
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
                "const:dd0:8"
              ]
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
      "definition_site": "00542634",
      "incomplete_value": false,
      "site": "00542634",
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
                "const:d10:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:1:8"
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
      "005425fc",
      "PARAM",
      [
        "storage",
        "00c25ce0",
        null,
        null
      ]
    ],
    [
      "00542608",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ],
    [
      "0054260c",
      "WRITE",
      [
        "storage",
        "00c25d00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005425fc",
      "PARAM",
      [
        "storage",
        "00c25da0",
        null,
        null
      ]
    ],
    [
      "00542608",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ],
    [
      "0054260c",
      "WRITE",
      [
        "storage",
        "00c25dc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054266c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00542/005425e4.md#insn-0054266c) · [`005425f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00542/005425e4.md#insn-005425f4)
- 新版 `0054266c`（命令位置の公開資料なし） · `005425f4`（命令位置の公開資料なし）

~~~diff
- 0054266c ["INT_ADD", "register:40f0:8", ["const:54266c:8", "const:4:8"]]
- 0054266c ["CALL", null, ["callee:00bdaf90:8"]]
- 0054266c bytes 1d621a94
+ 0054266c ["INT_ADD", "register:40f0:8", ["const:54266c:8", "const:4:8"]]
+ 0054266c ["CALL", null, ["callee:00bdaf90:8"]]
+ 0054266c bytes 49621a94
- 005425f4 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 005425f4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005425f4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005425f4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005425f4 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 005425f4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005425f4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005425f4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005425f4 bytes 73423b91
+ 005425f4 bytes 73023e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0809f3168a6b4c7b3fd87bea9e592abe"></a>

### [`00547c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00547/00547c90.md) → [`00547c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00547/00547c90.md) FUN_00547c90

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004183ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004183ec.md) · 呼出先 11件 [`00548094`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00548/00548094.md) [`00548104`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00548/00548104.md) [`0054841c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00548/0054841c.md) [`0054df60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054d/0054df60.md) [`0054df6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054d/0054df6c.md)
- 新版 呼出元 1件 [`004183ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004183ec.md) · 呼出先 11件 [`00548094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/00548094.md) [`00548104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/00548104.md) [`0054841c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/0054841c.md) [`0054df60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054d/0054df60.md) [`0054df6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054d/0054df6c.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 82.63% / 新版 82.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 12件, `call_target` 4件, `store_condition` 5件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `store_destination` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00547dd8",
      "incomplete_value": false,
      "site": "00547de4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00547dd8",
      "incomplete_value": false,
      "site": "00547de4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:778:8"
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
      "definition_site": "00547e54",
      "incomplete_value": false,
      "site": "00547e54",
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
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00547e54",
      "incomplete_value": false,
      "site": "00547e54",
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
            "const:d78:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00547f08",
      "incomplete_value": false,
      "site": "00547f08",
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
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00547f08",
      "incomplete_value": false,
      "site": "00547f08",
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
            "const:d78:8"
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
      "00547cc0",
      "READ",
      [
        "storage",
        "00c25d88",
        null,
        "undefined8"
      ]
    ],
    [
      "00547cd8",
      "PARAM",
      [
        "storage",
        "00c25d88",
        null,
        "undefined8"
      ]
    ],
    [
      "00547cfc",
      "READ",
      [
        "storage",
        "00c25d88",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00547cc0",
      "READ",
      [
        "storage",
        "00c25e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00547cd8",
      "PARAM",
      [
        "storage",
        "00c25e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00547cfc",
      "READ",
      [
        "storage",
        "00c25e48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00547e54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00547/00547c90.md#insn-00547e54) · [`00547f08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00547/00547c90.md#insn-00547f08) · [`00547fd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00547/00547c90.md#insn-00547fd8)
- 新版 `00547e54`（命令位置の公開資料なし） · `00547f08`（命令位置の公開資料なし） · `00547fd8`（命令位置の公開資料なし）

~~~diff
- 00547e54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d78:8"]]
- 00547e54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00547e54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e38:8"]]
+ 00547e54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00547e54 bytes 00bd06f9
+ 00547e54 bytes 001d07f9
- 00547f08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d78:8"]]
- 00547f08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00547f08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e38:8"]]
+ 00547f08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00547f08 bytes 00bd06f9
+ 00547f08 bytes 001d07f9
- 00547fd8 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:d60:8"]]
- 00547fd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00547fd8 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:e20:8"]]
+ 00547fd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00547fd8 bytes 60b306f9
+ 00547fd8 bytes 601307f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71cc28f84d1bbb53092d9c89aa5a69e1"></a>

### [`00548364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00548/00548364.md) → [`00548364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/00548364.md) FUN_00548364

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00458f08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00458/00458f08.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00458f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00458/00458f08.md) · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00548380",
      "incomplete_value": true,
      "site": "00548384",
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
      "definition_site": "00548380",
      "incomplete_value": true,
      "site": "00548384",
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
      "0054837c",
      "READ",
      [
        "storage",
        "00c25d58",
        null,
        "undefined8"
      ]
    ],
    [
      "0054837c",
      "READ",
      [
        "storage",
        "00c25d60",
        null,
        "undefined8"
      ]
    ],
    [
      "005483c8",
      "READ",
      [
        "storage",
        "00c25d70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0054837c",
      "READ",
      [
        "storage",
        "00c25e18",
        null,
        "undefined8"
      ]
    ],
    [
      "0054837c",
      "READ",
      [
        "storage",
        "00c25e20",
        null,
        "undefined8"
      ]
    ],
    [
      "005483c8",
      "READ",
      [
        "storage",
        "00c25e30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00548378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00548/00548364.md#insn-00548378) · [`005483c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00548/00548364.md#insn-005483c4)
- 新版 `00548378`（命令位置の公開資料なし） · `005483c4`（命令位置の公開資料なし）

~~~diff
- 00548378 ["COPY", "tmp:0:8", ["const:d58:8"]]
- 00548378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00548378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00548378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00548378 ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 00548378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00548378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00548378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00548378 bytes 08613591
+ 00548378 bytes 08613891
- 005483c4 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 005483c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005483c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005483c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005483c4 ["COPY", "tmp:0:8", ["const:e30:8"]]
+ 005483c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005483c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005483c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005483c4 bytes 08c13591
+ 005483c4 bytes 08c13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f414be48594177c43dfe3b5fd6366ad"></a>

### [`0054841c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00548/0054841c.md) → [`0054841c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/0054841c.md) FUN_0054841c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00547c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00547/00547c90.md) · 呼出先 3件 [`0054873c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00548/0054873c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd170.md)
- 新版 呼出元 1件 [`00547c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00547/00547c90.md) · 呼出先 3件 [`0054873c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/0054873c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd220.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.44% / 新版 89.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 6件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00548458",
      "incomplete_value": false,
      "site": "0054845c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00548458",
      "incomplete_value": false,
      "site": "0054845c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:630:8"
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
      "definition_site": "00548488",
      "incomplete_value": true,
      "site": "00548510",
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
                "const:c25000:8"
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
    "old": {
      "definition_site": "00548488",
      "incomplete_value": true,
      "site": "00548510",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:d98:8"
              ]
            ]
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
      "definition_site": "0054854c",
      "incomplete_value": true,
      "site": "0054854c",
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
      "definition_site": "0054854c",
      "incomplete_value": true,
      "site": "0054854c",
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
    "ordinal": 42,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0054845c",
      "DATA",
      [
        "storage",
        "00bee630",
        null,
        "undefined *"
      ]
    ],
    [
      "00548488",
      "READ",
      [
        "storage",
        "00c25d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00548504",
      "READ",
      [
        "storage",
        "00c1b3b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0054845c",
      "DATA",
      [
        "storage",
        "00bee6e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00548488",
      "READ",
      [
        "storage",
        "00c25e58",
        null,
        "undefined8"
      ]
    ],
    [
      "00548504",
      "READ",
      [
        "storage",
        "00c1b460",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005486e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00548/0054841c.md#insn-005486e0) · [`00548458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00548/0054841c.md#insn-00548458) · [`00548488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00548/0054841c.md#insn-00548488)
- 新版 `005486e0`（命令位置の公開資料なし） · `00548458`（命令位置の公開資料なし） · `00548488`（命令位置の公開資料なし）

~~~diff
- 005486e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:da0:8"]]
- 005486e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 005486e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e60:8"]]
+ 005486e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 005486e0 bytes 09a10db9
+ 005486e0 bytes 09610eb9
- 00548458 ["COPY", "tmp:0:8", ["const:630:8"]]
- 00548458 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00548458 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00548458 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00548458 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 00548458 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00548458 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00548458 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00548458 bytes 08c11891
+ 00548458 bytes 08811b91
- 00548488 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d98:8"]]
- 00548488 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00548488 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e58:8"]]
+ 00548488 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00548488 bytes 4acd46f9
+ 00548488 bytes 4a2d47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff3897159a6ee33d728a9251b929b210"></a>

### [`005488c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00548/005488c4.md) → [`005488c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/005488c4.md) FUN_005488c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0054df60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054d/0054df60.md) · 呼出先 8件 [`005426ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00542/005426ac.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf10.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md)
- 新版 呼出元 1件 [`0054df60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054d/0054df60.md) · 呼出先 8件 [`005426ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00542/005426ac.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafc0.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005488dc",
      "incomplete_value": false,
      "site": "005488e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005488dc",
      "incomplete_value": false,
      "site": "005488e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00548930",
      "incomplete_value": false,
      "site": "00548930",
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
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00548930",
      "incomplete_value": false,
      "site": "00548930",
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
            "const:da0:8"
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
      "005488e0",
      "DATA",
      [
        "storage",
        "00bee630",
        null,
        "undefined *"
      ]
    ],
    [
      "00548928",
      "READ",
      [
        "storage",
        "00c25da0",
        null,
        "undefined4"
      ]
    ],
    [
      "00548930",
      "WRITE",
      [
        "storage",
        "00c25da0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "005488e0",
      "DATA",
      [
        "storage",
        "00bee6e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00548928",
      "READ",
      [
        "storage",
        "00c25e60",
        null,
        "undefined4"
      ]
    ],
    [
      "00548930",
      "WRITE",
      [
        "storage",
        "00c25e60",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00548930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00548/005488c4.md#insn-00548930) · [`005488dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00548/005488c4.md#insn-005488dc) · [`00548928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00548/005488c4.md#insn-00548928)
- 新版 `00548930`（命令位置の公開資料なし） · `005488dc`（命令位置の公開資料なし） · `00548928`（命令位置の公開資料なし）

~~~diff
- 00548930 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:da0:8"]]
- 00548930 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00548930 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e60:8"]]
+ 00548930 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00548930 bytes 09a10db9
+ 00548930 bytes 09610eb9
- 005488dc ["COPY", "tmp:0:8", ["const:630:8"]]
- 005488dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005488dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005488dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005488dc ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 005488dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005488dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005488dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005488dc bytes 29c11891
+ 005488dc bytes 29811b91
- 00548928 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:da0:8"]]
- 00548928 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00548928 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
+ 00548928 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e60:8"]]
+ 00548928 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 00548928 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
- 00548928 bytes 09a14db9
+ 00548928 bytes 09614eb9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1275ad375d394948c47deca28d41c8fb"></a>

### [`00549624`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00549/00549624.md) → [`00549624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549624.md) FUN_00549624

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00549864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00549/00549864.md) [`00549868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00549/00549868.md) · 呼出先 8件 [`00548e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00548/00548e1c.md) [`00bd6880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6880.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 2件 [`00549864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549864.md) [`00549868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549868.md) · 呼出先 8件 [`00548e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/00548e1c.md) [`00bd6940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6940.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.08% / 新版 92.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00549794",
      "incomplete_value": false,
      "site": "00549794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00549794",
      "incomplete_value": false,
      "site": "00549794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
      "definition_site": "00549660",
      "incomplete_value": true,
      "site": "00549664",
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
      "definition_site": "00549660",
      "incomplete_value": true,
      "site": "00549664",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005496c8",
      "incomplete_value": false,
      "site": "005496d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005496c8",
      "incomplete_value": false,
      "site": "005496d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
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
      "0054965c",
      "READ",
      [
        "storage",
        "00c25d58",
        null,
        "undefined8"
      ]
    ],
    [
      "0054965c",
      "READ",
      [
        "storage",
        "00c25d60",
        null,
        "undefined8"
      ]
    ],
    [
      "005496c8",
      "PARAM",
      [
        "storage",
        "00bee7b8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0054965c",
      "READ",
      [
        "storage",
        "00c25e18",
        null,
        "undefined8"
      ]
    ],
    [
      "0054965c",
      "READ",
      [
        "storage",
        "00c25e20",
        null,
        "undefined8"
      ]
    ],
    [
      "005496c8",
      "PARAM",
      [
        "storage",
        "00bee868",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00549658`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00549/00549624.md#insn-00549658) · [`005496c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00549/00549624.md#insn-005496c8) · [`005496cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00549/00549624.md#insn-005496cc)
- 新版 `00549658`（命令位置の公開資料なし） · `005496c8`（命令位置の公開資料なし） · `005496cc`（命令位置の公開資料なし）

~~~diff
- 00549658 ["COPY", "tmp:0:8", ["const:d58:8"]]
- 00549658 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00549658 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00549658 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00549658 ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 00549658 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00549658 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00549658 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00549658 bytes 08613591
+ 00549658 bytes 08613891
- 005496c8 ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 005496c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005496c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005496c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005496c8 ["COPY", "tmp:0:8", ["const:868:8"]]
+ 005496c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005496c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005496c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005496c8 bytes 21e01e91
+ 005496c8 bytes 21a02191
- 005496cc ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:3d8:8"]]
- 005496cc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005496cc ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:488:8"]]
+ 005496cc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005496cc bytes 42ec41f9
+ 005496cc bytes 424442f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55333f367643a7c6e9c9797b2b299776"></a>

### [`0054df20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054d/0054df20.md) → [`0054df20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054d/0054df20.md) FUN_0054df20

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)

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
      "definition_site": "0054df24",
      "incomplete_value": false,
      "site": "0054df28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054df24",
      "incomplete_value": false,
      "site": "0054df28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:778:8"
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
      "0054df28",
      "DATA",
      [
        "storage",
        "00bee778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0054df28",
      "DATA",
      [
        "storage",
        "00bee828",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054df24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054d/0054df20.md#insn-0054df24)
- 新版 `0054df24`（命令位置の公開資料なし）

~~~diff
- 0054df24 ["COPY", "tmp:0:8", ["const:778:8"]]
- 0054df24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054df24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054df24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0054df24 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 0054df24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0054df24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0054df24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054df24 bytes 08e11d91
+ 0054df24 bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8640f3ab04eb82e1792c103cd9f20e5"></a>

### [`0054df30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054d/0054df30.md) → [`0054df30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054d/0054df30.md) FUN_0054df30

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0054df40",
      "incomplete_value": false,
      "site": "0054df48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054df40",
      "incomplete_value": false,
      "site": "0054df48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:778:8"
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
      "0054df48",
      "DATA",
      [
        "storage",
        "00bee778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0054df48",
      "DATA",
      [
        "storage",
        "00bee828",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054df40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054d/0054df30.md#insn-0054df40)
- 新版 `0054df40`（命令位置の公開資料なし）

~~~diff
- 0054df40 ["COPY", "tmp:0:8", ["const:778:8"]]
- 0054df40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054df40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054df40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0054df40 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 0054df40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0054df40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0054df40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054df40 bytes 08e11d91
+ 0054df40 bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28d1751995c638d8e730180a23accd1d"></a>

### [`0054e0c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e0c8.md) → [`0054e0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e0c8.md) FUN_0054e0c8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0054df6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054d/0054df6c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0054df6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054d/0054df6c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0054e0d4",
      "incomplete_value": true,
      "site": "0054e0d8",
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
    "old": {
      "definition_site": "0054e0d4",
      "incomplete_value": true,
      "site": "0054e0d8",
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
            "const:30a:8"
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
      "0054e0d4",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0054e0d4",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054e0d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e0c8.md#insn-0054e0d4)
- 新版 `0054e0d4`（命令位置の公開資料なし）

~~~diff
- 0054e0d4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0054e0d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0054e0d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0054e0d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0054e0d4 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0054e0d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0054e0d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0054e0d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0054e0d4 bytes 00280c91
+ 0054e0d4 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf31b96b5916db89f9d344df43b153bb"></a>

### [`0054e0dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e0dc.md) → [`0054e0dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e0dc.md) FUN_0054e0dc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)

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
      "definition_site": "0054e0f4",
      "incomplete_value": false,
      "site": "0054e0f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054e0f4",
      "incomplete_value": false,
      "site": "0054e0f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
      "0054e0f8",
      "DATA",
      [
        "storage",
        "00bee7e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0054e0f8",
      "DATA",
      [
        "storage",
        "00bee890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054e0f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e0dc.md#insn-0054e0f4)
- 新版 `0054e0f4`（命令位置の公開資料なし）

~~~diff
- 0054e0f4 ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 0054e0f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054e0f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054e0f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0054e0f4 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 0054e0f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0054e0f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0054e0f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054e0f4 bytes 08811f91
+ 0054e0f4 bytes 08412291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-807ba9d973b289c32a7016a6b62bbc49"></a>

### [`0054e138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e138.md) → [`0054e138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e138.md) FUN_0054e138

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0054e150",
      "incomplete_value": false,
      "site": "0054e154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054e150",
      "incomplete_value": false,
      "site": "0054e154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
      "0054e154",
      "DATA",
      [
        "storage",
        "00bee7e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0054e154",
      "DATA",
      [
        "storage",
        "00bee890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054e150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e138.md#insn-0054e150)
- 新版 `0054e150`（命令位置の公開資料なし）

~~~diff
- 0054e150 ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 0054e150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054e150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054e150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0054e150 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 0054e150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0054e150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0054e150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054e150 bytes 08811f91
+ 0054e150 bytes 08412291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2207988bd8979d7a920045a401e3058e"></a>

### [`0054e21c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e21c.md) → [`0054e21c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e21c.md) FUN_0054e21c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)

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
      "definition_site": "0054e234",
      "incomplete_value": false,
      "site": "0054e238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054e234",
      "incomplete_value": false,
      "site": "0054e238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:830:8"
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
      "0054e238",
      "DATA",
      [
        "storage",
        "00bee830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0054e238",
      "DATA",
      [
        "storage",
        "00bee8e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054e234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e21c.md#insn-0054e234)
- 新版 `0054e234`（命令位置の公開資料なし）

~~~diff
- 0054e234 ["COPY", "tmp:0:8", ["const:830:8"]]
- 0054e234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054e234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054e234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0054e234 ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 0054e234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0054e234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0054e234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054e234 bytes 08c12091
+ 0054e234 bytes 08812391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-506fe70a5d880bf9156d1dd1998cb005"></a>

### [`0054e278`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e278.md) → [`0054e278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e278.md) FUN_0054e278

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0054e290",
      "incomplete_value": false,
      "site": "0054e294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054e290",
      "incomplete_value": false,
      "site": "0054e294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:830:8"
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
      "0054e294",
      "DATA",
      [
        "storage",
        "00bee830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0054e294",
      "DATA",
      [
        "storage",
        "00bee8e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054e290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e278.md#insn-0054e290)
- 新版 `0054e290`（命令位置の公開資料なし）

~~~diff
- 0054e290 ["COPY", "tmp:0:8", ["const:830:8"]]
- 0054e290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054e290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054e290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0054e290 ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 0054e290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0054e290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0054e290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054e290 bytes 08c12091
+ 0054e290 bytes 08812391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4184817d138a6004a6dbaf1c82e3919"></a>

### [`0054e35c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e35c.md) → [`0054e35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e35c.md) FUN_0054e35c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)

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
      "definition_site": "0054e360",
      "incomplete_value": false,
      "site": "0054e364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054e360",
      "incomplete_value": false,
      "site": "0054e364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:880:8"
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
      "0054e364",
      "DATA",
      [
        "storage",
        "00bee880",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0054e364",
      "DATA",
      [
        "storage",
        "00bee930",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054e360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e35c.md#insn-0054e360)
- 新版 `0054e360`（命令位置の公開資料なし）

~~~diff
- 0054e360 ["COPY", "tmp:0:8", ["const:880:8"]]
- 0054e360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054e360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054e360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0054e360 ["COPY", "tmp:0:8", ["const:930:8"]]
+ 0054e360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0054e360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0054e360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054e360 bytes 08012291
+ 0054e360 bytes 08c12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98c63675e29333766c3ae8ead06a296e"></a>

### [`0054e36c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e36c.md) → [`0054e36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e36c.md) FUN_0054e36c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0054e37c",
      "incomplete_value": false,
      "site": "0054e384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054e37c",
      "incomplete_value": false,
      "site": "0054e384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:880:8"
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
      "0054e384",
      "DATA",
      [
        "storage",
        "00bee880",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0054e384",
      "DATA",
      [
        "storage",
        "00bee930",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054e37c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e36c.md#insn-0054e37c)
- 新版 `0054e37c`（命令位置の公開資料なし）

~~~diff
- 0054e37c ["COPY", "tmp:0:8", ["const:880:8"]]
- 0054e37c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054e37c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054e37c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0054e37c ["COPY", "tmp:0:8", ["const:930:8"]]
+ 0054e37c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0054e37c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0054e37c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054e37c bytes 08012291
+ 0054e37c bytes 08c12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b30913d747395f3745edc2494add744"></a>

### [`0054e3ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e3ac.md) → [`0054e3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e3ac.md) _INIT_28

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00547bf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00547/00547bf8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00547bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00547/00547bf8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 56.52% / 新版 56.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054e3d8",
      "incomplete_value": false,
      "site": "0054e3d8",
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
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054e3d8",
      "incomplete_value": false,
      "site": "0054e3d8",
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
            "const:d58:8"
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
      "definition_site": "0054e3d8",
      "incomplete_value": false,
      "site": "0054e3d8",
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
                "const:e18:8"
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
      "definition_site": "0054e3d8",
      "incomplete_value": false,
      "site": "0054e3d8",
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
                "const:d58:8"
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054e3dc",
      "incomplete_value": false,
      "site": "0054e3dc",
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
                "const:e18:8"
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
      "definition_site": "0054e3dc",
      "incomplete_value": false,
      "site": "0054e3dc",
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
                "const:d58:8"
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
      "0054e3cc",
      "PARAM",
      [
        "storage",
        "00c25d58",
        null,
        "undefined8"
      ]
    ],
    [
      "0054e3d4",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ],
    [
      "0054e3d8",
      "WRITE",
      [
        "storage",
        "00c25d58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0054e3cc",
      "PARAM",
      [
        "storage",
        "00c25e18",
        null,
        "undefined8"
      ]
    ],
    [
      "0054e3d4",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ],
    [
      "0054e3d8",
      "WRITE",
      [
        "storage",
        "00c25e18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054e3c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e3ac.md#insn-0054e3c4) · [`0054e3c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e3ac.md#insn-0054e3c8)
- 新版 `0054e3c4`（命令位置の公開資料なし） · `0054e3c8`（命令位置の公開資料なし）

~~~diff
- 0054e3c4 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 0054e3c4 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 0054e3c4 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 0054e3c4 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 0054e3c4 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 0054e3c4 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 0054e3c4 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 0054e3c4 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 0054e3c4 bytes 94423b91
+ 0054e3c4 bytes 94023e91
- 0054e3c8 ["COPY", "register:4008:8", ["const:c25000:8"]]
- 0054e3c8 bytes a13600f0
+ 0054e3c8 ["COPY", "register:4008:8", ["const:c25000:8"]]
+ 0054e3c8 bytes a13600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2920f8cd370f583f32274b5c7ac559f2"></a>

### [`0054e408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e408.md) → [`0054e408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e408.md) FUN_0054e408

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00550c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00550/00550c88.md) [`00550fa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00550/00550fa8.md) [`00551208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551208.md) · 呼出先 10件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00551984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551984.md) [`00574054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574054.md) [`00574730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574730.md) [`00574810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574810.md)
- 新版 呼出元 3件 [`00550c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00550/00550c88.md) [`00550fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00550/00550fa8.md) [`00551208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551208.md) · 呼出先 10件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00551984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551984.md) [`00574054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574054.md) [`00574730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574730.md) [`00574810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574810.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.21% / 新版 94.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054e490",
      "incomplete_value": true,
      "site": "0054e490",
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
                "const:a64:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054e490",
      "incomplete_value": true,
      "site": "0054e490",
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
                "const:9d7:8"
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
      "definition_site": "0054e4f8",
      "incomplete_value": true,
      "site": "0054e4f8",
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
                "const:545:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054e4f8",
      "incomplete_value": true,
      "site": "0054e4f8",
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
                "const:54c:8"
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
      "definition_site": "0054e5c4",
      "incomplete_value": true,
      "site": "0054e5c4",
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
                "const:6d3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054e5c4",
      "incomplete_value": true,
      "site": "0054e5c4",
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
                "const:646:8"
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
      "0054e480",
      "READ",
      [
        "storage",
        "002939d7",
        null,
        "string"
      ]
    ],
    [
      "0054e4e0",
      "READ",
      [
        "storage",
        "002a254c",
        null,
        "string"
      ]
    ],
    [
      "0054e5b4",
      "READ",
      [
        "storage",
        "002a1646",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0054e480",
      "READ",
      [
        "storage",
        "00293a64",
        null,
        "string"
      ]
    ],
    [
      "0054e4e0",
      "READ",
      [
        "storage",
        "002a2545",
        null,
        "string"
      ]
    ],
    [
      "0054e5b4",
      "READ",
      [
        "storage",
        "002a16d3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054e478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e408.md#insn-0054e478) · [`0054e4d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e408.md#insn-0054e4d8) · [`0054e5ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e408.md#insn-0054e5ac)
- 新版 `0054e478`（命令位置の公開資料なし） · `0054e4d8`（命令位置の公開資料なし） · `0054e5ac`（命令位置の公開資料なし）

~~~diff
- 0054e478 ["COPY", "tmp:0:8", ["const:9d7:8"]]
- 0054e478 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0054e478 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0054e478 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0054e478 ["COPY", "tmp:0:8", ["const:a64:8"]]
+ 0054e478 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0054e478 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0054e478 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0054e478 bytes 295d2791
+ 0054e478 bytes 29912991
- 0054e4d8 ["COPY", "tmp:0:8", ["const:54c:8"]]
- 0054e4d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0054e4d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0054e4d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0054e4d8 ["COPY", "tmp:0:8", ["const:545:8"]]
+ 0054e4d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0054e4d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0054e4d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0054e4d8 bytes 29311591
+ 0054e4d8 bytes 29151591
- 0054e5ac ["COPY", "tmp:0:8", ["const:646:8"]]
- 0054e5ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0054e5ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0054e5ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0054e5ac ["COPY", "tmp:0:8", ["const:6d3:8"]]
+ 0054e5ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0054e5ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0054e5ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0054e5ac bytes 29191991
+ 0054e5ac bytes 294d1b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d91278a7fa815763874702e28ef45af"></a>

### [`0054ec1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054ec1c.md) → [`0054ec1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054ec1c.md) FUN_0054ec1c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052dab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dab8.md) · 呼出先 15件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md)
- 新版 呼出元 1件 [`0052dab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dab8.md) · 呼出先 15件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054edd4",
      "incomplete_value": true,
      "site": "0054edd4",
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
      "definition_site": "0054edd4",
      "incomplete_value": true,
      "site": "0054edd4",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "0054ee04",
      "incomplete_value": true,
      "site": "0054ee04",
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
      "definition_site": "0054ee04",
      "incomplete_value": true,
      "site": "0054ee04",
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
    "ordinal": 7,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0054ec98",
      "READ",
      [
        "storage",
        "002ac9cf",
        null,
        "string"
      ]
    ],
    [
      "0054ec98",
      "READ",
      [
        "storage",
        "002ac9df",
        null,
        "string"
      ]
    ],
    [
      "0054ecac",
      "READ",
      [
        "storage",
        "002ac9ef",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0054ec98",
      "READ",
      [
        "storage",
        "002ac9c6",
        null,
        "string"
      ]
    ],
    [
      "0054ec98",
      "READ",
      [
        "storage",
        "002ac9d6",
        null,
        "string"
      ]
    ],
    [
      "0054ecac",
      "READ",
      [
        "storage",
        "002ac9e6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054ec90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054ec1c.md#insn-0054ec90) · [`0054ec94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054ec1c.md#insn-0054ec94)
- 新版 `0054ec90`（命令位置の公開資料なし） · `0054ec94`（命令位置の公開資料なし）

~~~diff
- 0054ec90 ["COPY", "tmp:0:8", ["const:9cf:8"]]
- 0054ec90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054ec90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054ec90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0054ec90 ["COPY", "tmp:0:8", ["const:9c6:8"]]
+ 0054ec90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0054ec90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0054ec90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054ec90 bytes 083d2791
+ 0054ec90 bytes 08192791
- 0054ec94 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0054ec94 bytes 09ebffd0
+ 0054ec94 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0054ec94 bytes 09ebffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b456524f1de4850f5057d99beb597d2"></a>

### [`0054ef40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054ef40.md) → [`0054ef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054ef40.md) FUN_0054ef40

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052dabc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dabc.md) · 呼出先 15件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md)
- 新版 呼出元 1件 [`0052dabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dabc.md) · 呼出先 15件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.24% / 新版 93.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054efb8",
      "incomplete_value": true,
      "site": "0054efcc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ab000:8"
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
      "definition_site": "0054efb8",
      "incomplete_value": true,
      "site": "0054efcc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:7c4:8"
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
      "definition_site": "0054efb8",
      "incomplete_value": true,
      "site": "0054efcc",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0054efb8",
      "incomplete_value": true,
      "site": "0054efcc",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0054efd0",
      "incomplete_value": true,
      "site": "0054efd0",
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
                "const:1f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054efd0",
      "incomplete_value": true,
      "site": "0054efd0",
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
                "const:1f:8"
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
      "0054efb8",
      "READ",
      [
        "storage",
        "002ab7c4",
        null,
        "string"
      ]
    ],
    [
      "0054efb8",
      "READ",
      [
        "storage",
        "002ab7d4",
        null,
        "string"
      ]
    ],
    [
      "0054efc0",
      "READ",
      [
        "storage",
        "002ab7e3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0054efb8",
      "READ",
      [
        "storage",
        "002ab7ca",
        null,
        "string"
      ]
    ],
    [
      "0054efb8",
      "READ",
      [
        "storage",
        "002ab7da",
        null,
        "string"
      ]
    ],
    [
      "0054efc0",
      "READ",
      [
        "storage",
        "002ab7e9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054efb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054ef40.md#insn-0054efb0) · [`0054efb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054ef40.md#insn-0054efb4)
- 新版 `0054efb0`（命令位置の公開資料なし） · `0054efb4`（命令位置の公開資料なし）

~~~diff
- 0054efb0 ["COPY", "tmp:0:8", ["const:7c4:8"]]
- 0054efb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054efb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054efb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0054efb0 ["COPY", "tmp:0:8", ["const:7ca:8"]]
+ 0054efb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0054efb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0054efb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054efb0 bytes 08111f91
+ 0054efb0 bytes 08291f91
- 0054efb4 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0054efb4 bytes 09ebffd0
+ 0054efb4 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0054efb4 bytes 09ebffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9232986baf7a7f26638839bfe65e69a0"></a>

### [`0054f220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054f220.md) → [`0054f220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054f/0054f220.md) FUN_0054f220

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052dac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dac0.md) · 呼出先 11件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0052dac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dac0.md) · 呼出先 11件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.05% / 新版 94.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054f284",
      "incomplete_value": true,
      "site": "0054f294",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:99c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054f284",
      "incomplete_value": true,
      "site": "0054f294",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:90f:8"
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
      "definition_site": "0054f298",
      "incomplete_value": true,
      "site": "0054f298",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054f298",
      "incomplete_value": true,
      "site": "0054f298",
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
                "const:e:8"
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
      "0054f284",
      "READ",
      [
        "storage",
        "0029290f",
        null,
        "string"
      ]
    ],
    [
      "0054f28c",
      "READ",
      [
        "storage",
        "0029291d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0054f284",
      "READ",
      [
        "storage",
        "0029299c",
        null,
        "string"
      ]
    ],
    [
      "0054f28c",
      "READ",
      [
        "storage",
        "002929aa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054f280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054f220.md#insn-0054f280)
- 新版 `0054f280`（命令位置の公開資料なし）

~~~diff
- 0054f280 ["COPY", "tmp:0:8", ["const:90f:8"]]
- 0054f280 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0054f280 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0054f280 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0054f280 ["COPY", "tmp:0:8", ["const:99c:8"]]
+ 0054f280 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0054f280 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0054f280 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0054f280 bytes 293d2491
+ 0054f280 bytes 29712691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe36eee8c60f38672d22d66fc4791ab6"></a>

### [`0054f3d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054f3d4.md) → [`0054f3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054f/0054f3d4.md) FUN_0054f3d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052dac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dac4.md) · 呼出先 11件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0052dac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dac4.md) · 呼出先 11件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.05% / 新版 94.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054f438",
      "incomplete_value": true,
      "site": "0054f448",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:99c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054f438",
      "incomplete_value": true,
      "site": "0054f448",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:90f:8"
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
      "definition_site": "0054f44c",
      "incomplete_value": true,
      "site": "0054f44c",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054f44c",
      "incomplete_value": true,
      "site": "0054f44c",
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
                "const:e:8"
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
      "0054f438",
      "READ",
      [
        "storage",
        "0029290f",
        null,
        "string"
      ]
    ],
    [
      "0054f440",
      "READ",
      [
        "storage",
        "0029291d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0054f438",
      "READ",
      [
        "storage",
        "0029299c",
        null,
        "string"
      ]
    ],
    [
      "0054f440",
      "READ",
      [
        "storage",
        "002929aa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054f434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054f3d4.md#insn-0054f434)
- 新版 `0054f434`（命令位置の公開資料なし）

~~~diff
- 0054f434 ["COPY", "tmp:0:8", ["const:90f:8"]]
- 0054f434 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0054f434 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0054f434 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0054f434 ["COPY", "tmp:0:8", ["const:99c:8"]]
+ 0054f434 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0054f434 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0054f434 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0054f434 bytes 293d2491
+ 0054f434 bytes 29712691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cba6b65b1e23e28d432151e2e76083e3"></a>

### [`0054f588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054f588.md) → [`0054f588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054f/0054f588.md) FUN_0054f588

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052dac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dac8.md) · 呼出先 19件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00551eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551eb0.md)
- 新版 呼出元 1件 [`0052dac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dac8.md) · 呼出先 19件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00551eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551eb0.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054f604",
      "incomplete_value": true,
      "site": "0054f614",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:30e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054f604",
      "incomplete_value": true,
      "site": "0054f614",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3a2:8"
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
      "definition_site": "0054f618",
      "incomplete_value": true,
      "site": "0054f618",
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
      "definition_site": "0054f618",
      "incomplete_value": true,
      "site": "0054f618",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054f680",
      "incomplete_value": false,
      "site": "0054f680",
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
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054f680",
      "incomplete_value": false,
      "site": "0054f680",
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
            "const:1f8:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0054f604",
      "READ",
      [
        "storage",
        "002a83a2",
        null,
        "string"
      ]
    ],
    [
      "0054f608",
      "READ",
      [
        "storage",
        "002a83b1",
        null,
        "string"
      ]
    ],
    [
      "0054f674",
      "READ",
      [
        "storage",
        "00c261f8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0054f604",
      "READ",
      [
        "storage",
        "002a830e",
        null,
        "string"
      ]
    ],
    [
      "0054f608",
      "READ",
      [
        "storage",
        "002a831d",
        null,
        "string"
      ]
    ],
    [
      "0054f674",
      "READ",
      [
        "storage",
        "00c262b8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054f680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054f588.md#insn-0054f680) · [`0054f6fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054f588.md#insn-0054f6fc) · [`0054f5fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054f588.md#insn-0054f5fc)
- 新版 `0054f680`（命令位置の公開資料なし） · `0054f6fc`（命令位置の公開資料なし） · `0054f5fc`（命令位置の公開資料なし）

~~~diff
- 0054f680 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:1f8:8"]]
- 0054f680 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
+ 0054f680 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:2b8:8"]]
+ 0054f680 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
- 0054f680 bytes 54f901b9
+ 0054f680 bytes 54b902b9
- 0054f6fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e0:8"]]
- 0054f6fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0054f6fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
+ 0054f6fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0054f6fc bytes 09f100f9
+ 0054f6fc bytes 095101f9
- 0054f5fc ["COPY", "tmp:0:8", ["const:3a2:8"]]
- 0054f5fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054f5fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054f5fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0054f5fc ["COPY", "tmp:0:8", ["const:30e:8"]]
+ 0054f5fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0054f5fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0054f5fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054f5fc bytes 08890e91
+ 0054f5fc bytes 08390c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92697c69c57c4b9f0e0b62e41992a6a7"></a>

### [`0054f9dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054f9dc.md) → [`0054f9dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054f/0054f9dc.md) FUN_0054f9dc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052dacc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dacc.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0052dacc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dacc.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

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
      "definition_site": "0054fa28",
      "incomplete_value": true,
      "site": "0054fa28",
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
                "const:dc5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054fa28",
      "incomplete_value": true,
      "site": "0054fa28",
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
                "const:d38:8"
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
      "0054fa18",
      "READ",
      [
        "storage",
        "00299d38",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0054fa18",
      "READ",
      [
        "storage",
        "00299dc5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054fa10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054f9dc.md#insn-0054fa10)
- 新版 `0054fa10`（命令位置の公開資料なし）

~~~diff
- 0054fa10 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 0054fa10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0054fa10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0054fa10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0054fa10 ["COPY", "tmp:0:8", ["const:dc5:8"]]
+ 0054fa10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0054fa10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0054fa10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0054fa10 bytes 29e13491
+ 0054fa10 bytes 29153791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dde7a918b1c3947f9e2fc6969131e5c2"></a>

### [`0054fb0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054fb0c.md) → [`0054fb0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054f/0054fb0c.md) FUN_0054fb0c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052dad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dad0.md) · 呼出先 11件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0052dad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dad0.md) · 呼出先 11件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.57% / 新版 94.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054fb64",
      "incomplete_value": true,
      "site": "0054fb70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0054fb64",
      "incomplete_value": true,
      "site": "0054fb70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4f6:8"
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
      "definition_site": "0054fb74",
      "incomplete_value": true,
      "site": "0054fb74",
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
      "definition_site": "0054fb74",
      "incomplete_value": true,
      "site": "0054fb74",
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
      "0054fb64",
      "READ",
      [
        "storage",
        "002a34f6",
        null,
        "string"
      ]
    ],
    [
      "0054fb68",
      "READ",
      [
        "storage",
        "002a3503",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0054fb64",
      "READ",
      [
        "storage",
        "002a34ef",
        null,
        "string"
      ]
    ],
    [
      "0054fb68",
      "READ",
      [
        "storage",
        "002a34fc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054fb5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054fb0c.md#insn-0054fb5c)
- 新版 `0054fb5c`（命令位置の公開資料なし）

~~~diff
- 0054fb5c ["COPY", "tmp:0:8", ["const:4f6:8"]]
- 0054fb5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054fb5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054fb5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0054fb5c ["COPY", "tmp:0:8", ["const:4ef:8"]]
+ 0054fb5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0054fb5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0054fb5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054fb5c bytes 08d91391
+ 0054fb5c bytes 08bd1391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa29286c82d182a30b5f11db186704a9"></a>

### [`0054fcc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054fcc8.md) → [`0054fcc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054f/0054fcc8.md) FUN_0054fcc8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052dad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dad4.md) · 呼出先 2件 [`00552018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/00552018.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`0052dad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dad4.md) · 呼出先 2件 [`00552018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/00552018.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
      "definition_site": "0054fd30",
      "incomplete_value": false,
      "site": "0054fd3c",
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
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054fd30",
      "incomplete_value": false,
      "site": "0054fd3c",
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
            "const:1b0:8"
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
      "0054fd30",
      "PARAM",
      [
        "storage",
        "00c261b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0054fd30",
      "PARAM",
      [
        "storage",
        "00c26270",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054fd30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054fcc8.md#insn-0054fd30)
- 新版 `0054fd30`（命令位置の公開資料なし）

~~~diff
- 0054fd30 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 0054fd30 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0054fd30 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0054fd30 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0054fd30 ["COPY", "tmp:0:8", ["const:270:8"]]
+ 0054fd30 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0054fd30 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0054fd30 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0054fd30 bytes 21c00691
+ 0054fd30 bytes 21c00991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a667fee4c1d5e266ebdfebb9d40b5f84"></a>

### [`0054fd90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054fd90.md) → [`0054fd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054f/0054fd90.md) Java_jp_co_ponos_battlecats_MyActivity_onIapList

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`0054ea94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054ea94.md) [`005515a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/005515a0.md) [`0055224c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/0055224c.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0054ea94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054ea94.md) [`005515a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/005515a0.md) [`0055224c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/0055224c.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.58% / 新版 95.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_value` 10件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0054fe64",
      "incomplete_value": false,
      "site": "0054fe64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054fe64",
      "incomplete_value": false,
      "site": "0054fe64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:a50:8"
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
      "definition_site": "0054ffa0",
      "incomplete_value": true,
      "site": "0054ffac",
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
                "const:a64:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054ffa0",
      "incomplete_value": true,
      "site": "0054ffac",
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
                "const:9d7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00550064",
      "incomplete_value": true,
      "site": "00550074",
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
                "const:9b3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00550064",
      "incomplete_value": true,
      "site": "00550074",
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
                "const:926:8"
              ]
            ]
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
      "0054fdcc",
      "READ",
      [
        "storage",
        "00c261e8",
        null,
        "undefined8"
      ]
    ],
    [
      "0054fe64",
      "DATA",
      [
        "storage",
        "00beea50",
        null,
        "pointer"
      ]
    ],
    [
      "0054ffa0",
      "READ",
      [
        "storage",
        "002939d7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0054fdcc",
      "READ",
      [
        "storage",
        "00c262a8",
        null,
        "undefined8"
      ]
    ],
    [
      "0054fe64",
      "DATA",
      [
        "storage",
        "00beeb00",
        null,
        "pointer"
      ]
    ],
    [
      "0054ffa0",
      "READ",
      [
        "storage",
        "00293a64",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054fdc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054fd90.md#insn-0054fdc8) · [`0054fdd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054fd90.md#insn-0054fdd8) · [`0054fe5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054fd90.md#insn-0054fe5c)
- 新版 `0054fdc8`（命令位置の公開資料なし） · `0054fdd8`（命令位置の公開資料なし） · `0054fe5c`（命令位置の公開資料なし）

~~~diff
- 0054fdc8 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 0054fdc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054fdc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054fdc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0054fdc8 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 0054fdc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0054fdc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0054fdc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054fdc8 bytes 08a10791
+ 0054fdc8 bytes 08a10a91
- 0054fdd8 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 0054fdd8 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
- 0054fdd8 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
- 0054fdd8 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
+ 0054fdd8 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 0054fdd8 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
+ 0054fdd8 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
+ 0054fdd8 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
- 0054fdd8 bytes 5aa30791
+ 0054fdd8 bytes 5aa30a91
- 0054fe5c ["COPY", "tmp:0:8", ["const:a50:8"]]
- 0054fe5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054fe5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054fe5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0054fe5c ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 0054fe5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0054fe5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0054fe5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054fe5c bytes 08412991
+ 0054fe5c bytes 08012c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df43b80730b44a60c5a6ba67e48cf2c6"></a>

### [`00550fa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00550/00550fa8.md) → [`00550fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00550/00550fa8.md) Java_jp_co_ponos_battlecats_MyActivity_onIapPurchases

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0054e408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e408.md) [`0056774c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/0056774c.md) [`00567848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567848.md) [`00567900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567900.md) [`005679e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/005679e4.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0054e408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e408.md) [`0056774c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/0056774c.md) [`00567848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567848.md) [`00567900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567900.md) [`005679e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/005679e4.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 98.37% / 新版 98.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005510e4",
      "incomplete_value": true,
      "site": "005510e4",
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
      "definition_site": "005510e4",
      "incomplete_value": true,
      "site": "005510e4",
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
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "005510e4"
      ],
      [
        "FALL_THROUGH",
        "005510e4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "005510e4",
      "incomplete_value": true,
      "site": "005510e8",
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
      "definition_site": "005510e4",
      "incomplete_value": true,
      "site": "005510e8",
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
    "ordinal": 15,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005510e0",
      "READ",
      [
        "storage",
        "00c261d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005510e0",
      "READ",
      [
        "storage",
        "00c26290",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005510e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00550/00550fa8.md#insn-005510e0)
- 新版 `005510e0`（命令位置の公開資料なし）

~~~diff
- 005510e0 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:1d0:8"]]
- 005510e0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005510e0 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:290:8"]]
+ 005510e0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005510e0 bytes 00eb40f9
+ 005510e0 bytes 004b41f9
~~~


<a id="compare-5090c84c2fc5a637686a9fd6524eb647"></a>

### [`00551208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551208.md) → [`00551208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551208.md) Java_jp_co_ponos_battlecats_MyActivity_onIapPurchases2

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0054e408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e408.md) [`0056774c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/0056774c.md) [`00567848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567848.md) [`00567900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567900.md) [`005679e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/005679e4.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0054e408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e408.md) [`0056774c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/0056774c.md) [`00567848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567848.md) [`00567900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567900.md) [`005679e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/005679e4.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 98.74% / 新版 98.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005513a0",
      "incomplete_value": true,
      "site": "005513a0",
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
      "definition_site": "005513a0",
      "incomplete_value": true,
      "site": "005513a0",
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
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "005513a0"
      ],
      [
        "FALL_THROUGH",
        "005513a0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "005513a0",
      "incomplete_value": true,
      "site": "005513a4",
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
      "definition_site": "005513a0",
      "incomplete_value": true,
      "site": "005513a4",
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
    "ordinal": 17,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0055139c",
      "READ",
      [
        "storage",
        "00c261d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0055139c",
      "READ",
      [
        "storage",
        "00c26290",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055139c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551208.md#insn-0055139c)
- 新版 `0055139c`（命令位置の公開資料なし）

~~~diff
- 0055139c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:1d0:8"]]
- 0055139c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0055139c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:290:8"]]
+ 0055139c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0055139c bytes 40eb40f9
+ 0055139c bytes 404b41f9
~~~


<a id="compare-8e1d07ca72aff8959be676decff8a9f6"></a>

### [`0055150c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/0055150c.md) → [`0055150c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/0055150c.md) FUN_0055150c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)

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
      "definition_site": "00551510",
      "incomplete_value": false,
      "site": "00551514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00551510",
      "incomplete_value": false,
      "site": "00551514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
      "00551514",
      "DATA",
      [
        "storage",
        "00bee8d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00551514",
      "DATA",
      [
        "storage",
        "00bee980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00551510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/0055150c.md#insn-00551510)
- 新版 `00551510`（命令位置の公開資料なし）

~~~diff
- 00551510 ["COPY", "tmp:0:8", ["const:8d0:8"]]
- 00551510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00551510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00551510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00551510 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 00551510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00551510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00551510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00551510 bytes 08412391
+ 00551510 bytes 08012691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1fe0c65f1b53a94e07d995ad823c61b"></a>

### [`0055151c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/0055151c.md) → [`0055151c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/0055151c.md) FUN_0055151c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0055152c",
      "incomplete_value": false,
      "site": "00551534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055152c",
      "incomplete_value": false,
      "site": "00551534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
      "00551534",
      "DATA",
      [
        "storage",
        "00bee8d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00551534",
      "DATA",
      [
        "storage",
        "00bee980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055152c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/0055151c.md#insn-0055152c)
- 新版 `0055152c`（命令位置の公開資料なし）

~~~diff
- 0055152c ["COPY", "tmp:0:8", ["const:8d0:8"]]
- 0055152c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055152c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055152c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055152c ["COPY", "tmp:0:8", ["const:980:8"]]
+ 0055152c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055152c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055152c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055152c bytes 08412391
+ 0055152c bytes 08012691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b43f3b412988da2e5a4f748c438d6d2"></a>

### [`005515a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/005515a0.md) → [`005515a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/005515a0.md) FUN_005515a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0054fd90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054fd90.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`0054fd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054f/0054fd90.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005515d0",
      "incomplete_value": true,
      "site": "005515d0",
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
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005515d0",
      "incomplete_value": true,
      "site": "005515d0",
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
            "const:920:8"
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
      "005515d0",
      "DATA",
      [
        "storage",
        "00bee920",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005515d0",
      "DATA",
      [
        "storage",
        "00bee9d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005515c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/005515a0.md#insn-005515c0)
- 新版 `005515c0`（命令位置の公開資料なし）

~~~diff
- 005515c0 ["COPY", "tmp:0:8", ["const:920:8"]]
- 005515c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005515c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005515c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005515c0 ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 005515c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005515c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005515c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005515c0 bytes 08812491
+ 005515c0 bytes 08412791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce56df3c3c2cd3c9f0d7ba6052a0a417"></a>

### [`00551850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551850.md) → [`00551850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551850.md) FUN_00551850

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0055154c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/0055154c.md) · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`0055154c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/0055154c.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00551868",
      "incomplete_value": false,
      "site": "0055186c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00551868",
      "incomplete_value": false,
      "site": "0055186c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:920:8"
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
      "0055186c",
      "DATA",
      [
        "storage",
        "00bee920",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055186c",
      "DATA",
      [
        "storage",
        "00bee9d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00551868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551850.md#insn-00551868)
- 新版 `00551868`（命令位置の公開資料なし）

~~~diff
- 00551868 ["COPY", "tmp:0:8", ["const:920:8"]]
- 00551868 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00551868 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00551868 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00551868 ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 00551868 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00551868 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00551868 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00551868 bytes 29812491
+ 00551868 bytes 29412791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f28f41db0834ded0afad062bb52ac1d"></a>

### [`005518f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/005518f0.md) → [`005518f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/005518f0.md) FUN_005518f0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)

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
      "definition_site": "005518f4",
      "incomplete_value": true,
      "site": "005518f8",
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
      "definition_site": "005518f4",
      "incomplete_value": true,
      "site": "005518f8",
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
            "const:988:8"
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
      "005518f8",
      "DATA",
      [
        "storage",
        "00bee988",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005518f8",
      "DATA",
      [
        "storage",
        "00beea38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005518f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/005518f0.md#insn-005518f4)
- 新版 `005518f4`（命令位置の公開資料なし）

~~~diff
- 005518f4 ["COPY", "tmp:0:8", ["const:988:8"]]
- 005518f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005518f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005518f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005518f4 ["COPY", "tmp:0:8", ["const:a38:8"]]
+ 005518f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005518f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005518f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005518f4 bytes 08212691
+ 005518f4 bytes 08e12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44fb1d5f201fd22ac50683d8ddd5f2b6"></a>

### [`00551900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551900.md) → [`00551900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551900.md) FUN_00551900

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00551910",
      "incomplete_value": false,
      "site": "00551918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00551910",
      "incomplete_value": false,
      "site": "00551918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:988:8"
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
      "00551918",
      "DATA",
      [
        "storage",
        "00bee988",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00551918",
      "DATA",
      [
        "storage",
        "00beea38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00551910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551900.md#insn-00551910)
- 新版 `00551910`（命令位置の公開資料なし）

~~~diff
- 00551910 ["COPY", "tmp:0:8", ["const:988:8"]]
- 00551910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00551910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00551910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00551910 ["COPY", "tmp:0:8", ["const:a38:8"]]
+ 00551910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00551910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00551910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00551910 bytes 08212691
+ 00551910 bytes 08e12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f536d511d68fcbf180d2d227f44bd1e1"></a>

### [`00551984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551984.md) → [`00551984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551984.md) FUN_00551984

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0054e408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e408.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 1件 [`0054e408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e408.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005519a8",
      "incomplete_value": false,
      "site": "005519a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005519a8",
      "incomplete_value": false,
      "site": "005519a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "005519a8",
      "DATA",
      [
        "storage",
        "00bee9d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005519a8",
      "DATA",
      [
        "storage",
        "00beea88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005519a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551984.md#insn-005519a0) · [`005519a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551984.md#insn-005519a4)
- 新版 `005519a0`（命令位置の公開資料なし） · `005519a4`（命令位置の公開資料なし）

~~~diff
- 005519a0 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 005519a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005519a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005519a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005519a0 ["COPY", "tmp:0:8", ["const:a88:8"]]
+ 005519a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005519a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005519a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005519a0 bytes 08612791
+ 005519a0 bytes 08212a91
- 005519a4 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 005519a4 bytes f50300aa
+ 005519a4 ["COPY", "register:40a8:8", ["register:4000:8"]]
+ 005519a4 bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27a30785504072882f49f3d74e4b425d"></a>

### [`00551bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551bf4.md) → [`00551bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551bf4.md) FUN_00551bf4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00551930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551930.md) · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00551930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551930.md) · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00551c0c",
      "incomplete_value": false,
      "site": "00551c10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00551c0c",
      "incomplete_value": false,
      "site": "00551c10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "00551c10",
      "DATA",
      [
        "storage",
        "00bee9d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00551c10",
      "DATA",
      [
        "storage",
        "00beea88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00551c0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551bf4.md#insn-00551c0c)
- 新版 `00551c0c`（命令位置の公開資料なし）

~~~diff
- 00551c0c ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 00551c0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00551c0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00551c0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00551c0c ["COPY", "tmp:0:8", ["const:a88:8"]]
+ 00551c0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00551c0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00551c0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00551c0c bytes 08612791
+ 00551c0c bytes 08212a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acfaae9522aafc4d4e3ada165da2c785"></a>

### [`00551ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551ccc.md) → [`00551ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551ccc.md) FUN_00551ccc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00550/00550c88.md) · 呼出先 2件 [`00574784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574784.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`00550c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00550/00550c88.md) · 呼出先 2件 [`00574784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574784.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00551cf4",
      "incomplete_value": false,
      "site": "00551cfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00551cf4",
      "incomplete_value": false,
      "site": "00551cfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:988:8"
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
      "definition_site": "00551d08",
      "incomplete_value": false,
      "site": "00551d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00551d08",
      "incomplete_value": false,
      "site": "00551d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "00551cfc",
      "DATA",
      [
        "storage",
        "00bee988",
        null,
        "undefined *"
      ]
    ],
    [
      "00551d08",
      "DATA",
      [
        "storage",
        "00bee9d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00551cfc",
      "DATA",
      [
        "storage",
        "00beea38",
        null,
        "undefined *"
      ]
    ],
    [
      "00551d08",
      "DATA",
      [
        "storage",
        "00beea88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00551cf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551ccc.md#insn-00551cf4) · [`00551cf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551ccc.md#insn-00551cf8)
- 新版 `00551cf4`（命令位置の公開資料なし） · `00551cf8`（命令位置の公開資料なし）

~~~diff
- 00551cf4 ["COPY", "tmp:0:8", ["const:988:8"]]
- 00551cf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00551cf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00551cf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00551cf4 ["COPY", "tmp:0:8", ["const:a38:8"]]
+ 00551cf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00551cf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00551cf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00551cf4 bytes 08212691
+ 00551cf4 bytes 08e12891
- 00551cf8 ["COPY", "register:40b8:8", ["register:4000:8"]]
- 00551cf8 bytes f70300aa
+ 00551cf8 ["COPY", "register:40b8:8", ["register:4000:8"]]
+ 00551cf8 bytes f70300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-994c0505cacb8af4413f95d67df9b1c6"></a>

### [`0055246c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/0055246c.md) → [`0055246c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/0055246c.md) FUN_0055246c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00552310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/00552310.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00552310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/00552310.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00552478",
      "incomplete_value": false,
      "site": "0055247c",
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
    "old": {
      "definition_site": "00552478",
      "incomplete_value": false,
      "site": "0055247c",
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
      "00552478",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00552478",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00552478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/0055246c.md#insn-00552478)
- 新版 `00552478`（命令位置の公開資料なし）

~~~diff
- 00552478 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00552478 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00552478 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00552478 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00552478 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00552478 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00552478 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00552478 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00552478 bytes 00280c91
+ 00552478 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9f1fea2f404dbffd0c2d49f68f262c2"></a>

### [`00552480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/00552480.md) → [`00552480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/00552480.md) _INIT_29

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0054e8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e8f0.md) [`0054e920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e920.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0054e8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e8f0.md) [`0054e920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e920.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 45.83% / 新版 45.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005524a8",
      "incomplete_value": false,
      "site": "005524a8",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:270:8"
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
      "definition_site": "005524a8",
      "incomplete_value": false,
      "site": "005524a8",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:1b0:8"
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
      "definition_site": "005524c4",
      "incomplete_value": false,
      "site": "005524c4",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:2a0:8"
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
      "definition_site": "005524c4",
      "incomplete_value": false,
      "site": "005524c4",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:1e0:8"
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
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005524c8",
      "incomplete_value": false,
      "site": "005524c8",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:2a0:8"
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
      "definition_site": "005524c8",
      "incomplete_value": false,
      "site": "005524c8",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:1e0:8"
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
      "00552498",
      "PARAM",
      [
        "storage",
        "00c261b0",
        null,
        null
      ]
    ],
    [
      "005524a4",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ],
    [
      "005524a8",
      "WRITE",
      [
        "storage",
        "00c261d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00552498",
      "PARAM",
      [
        "storage",
        "00c26270",
        null,
        null
      ]
    ],
    [
      "005524a4",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ],
    [
      "005524a8",
      "WRITE",
      [
        "storage",
        "00c26290",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00552490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/00552480.md#insn-00552490) · [`00552494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/00552480.md#insn-00552494)
- 新版 `00552490`（命令位置の公開資料なし） · `00552494`（命令位置の公開資料なし）

~~~diff
- 00552490 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 00552490 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00552490 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00552490 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00552490 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 00552490 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00552490 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00552490 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00552490 bytes 73423b91
+ 00552490 bytes 73023e91
- 00552494 ["COPY", "register:4008:8", ["const:c26000:8"]]
- 00552494 bytes a1360090
+ 00552494 ["COPY", "register:4008:8", ["const:c26000:8"]]
+ 00552494 bytes a1360090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1390828d815fecce1ef4645b871a3f6"></a>

### [`00552540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/00552540.md) → [`00552540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/00552540.md) FUN_00552540

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dad8.md) · 呼出先 11件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0052dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dad8.md) · 呼出先 11件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.04% / 新版 89.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00552584",
      "incomplete_value": true,
      "site": "0055259c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c19:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00552584",
      "incomplete_value": true,
      "site": "0055259c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b8c:8"
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
      "definition_site": "005525a0",
      "incomplete_value": true,
      "site": "005525ac",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:725:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005525a0",
      "incomplete_value": true,
      "site": "005525ac",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:71f:8"
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
      "definition_site": "005525b0",
      "incomplete_value": true,
      "site": "005525b0",
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
      "definition_site": "005525b0",
      "incomplete_value": true,
      "site": "005525b0",
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
      "00552584",
      "READ",
      [
        "storage",
        "00295b8c",
        null,
        "string"
      ]
    ],
    [
      "005525a0",
      "READ",
      [
        "storage",
        "002aa71f",
        null,
        "string"
      ]
    ],
    [
      "005525a4",
      "READ",
      [
        "storage",
        "002aa72c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00552584",
      "READ",
      [
        "storage",
        "00295c19",
        null,
        "string"
      ]
    ],
    [
      "005525a0",
      "READ",
      [
        "storage",
        "002aa725",
        null,
        "string"
      ]
    ],
    [
      "005525a4",
      "READ",
      [
        "storage",
        "002aa732",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00552578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/00552540.md#insn-00552578) · [`00552598`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/00552540.md#insn-00552598)
- 新版 `00552578`（命令位置の公開資料なし） · `00552598`（命令位置の公開資料なし）

~~~diff
- 00552578 ["COPY", "tmp:0:8", ["const:b8c:8"]]
- 00552578 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00552578 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00552578 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00552578 ["COPY", "tmp:0:8", ["const:c19:8"]]
+ 00552578 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00552578 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00552578 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00552578 bytes 29312e91
+ 00552578 bytes 29653091
- 00552598 ["COPY", "tmp:0:8", ["const:71f:8"]]
- 00552598 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00552598 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00552598 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00552598 ["COPY", "tmp:0:8", ["const:725:8"]]
+ 00552598 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00552598 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00552598 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00552598 bytes 087d1c91
+ 00552598 bytes 08951c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61cd0651c2472adcc9c3bb879e28dac2"></a>

### [`005526b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/005526b0.md) → [`005526b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/005526b0.md) FUN_005526b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052dadc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dadc.md) · 呼出先 14件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00552eb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/00552eb4.md) [`005530c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005530c0.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md)
- 新版 呼出元 1件 [`0052dadc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dadc.md) · 呼出先 14件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00552eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/00552eb4.md) [`005530c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005530c0.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00552700",
      "incomplete_value": true,
      "site": "00552710",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9f1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00552700",
      "incomplete_value": true,
      "site": "00552710",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:964:8"
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
      "definition_site": "00552720",
      "incomplete_value": true,
      "site": "00552720",
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
      "definition_site": "00552720",
      "incomplete_value": true,
      "site": "00552720",
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055272c",
      "incomplete_value": true,
      "site": "00552738",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0055272c",
      "incomplete_value": true,
      "site": "00552738",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4f6:8"
              ]
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
      "00552700",
      "READ",
      [
        "storage",
        "00294964",
        null,
        "string"
      ]
    ],
    [
      "00552704",
      "READ",
      [
        "storage",
        "00294973",
        null,
        "string"
      ]
    ],
    [
      "0055272c",
      "READ",
      [
        "storage",
        "002a34f6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00552700",
      "READ",
      [
        "storage",
        "002949f1",
        null,
        "string"
      ]
    ],
    [
      "00552704",
      "READ",
      [
        "storage",
        "00294a00",
        null,
        "string"
      ]
    ],
    [
      "0055272c",
      "READ",
      [
        "storage",
        "002a34ef",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005526f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/005526b0.md#insn-005526f8) · [`005526fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/005526b0.md#insn-005526fc)
- 新版 `005526f8`（命令位置の公開資料なし） · `005526fc`（命令位置の公開資料なし）

~~~diff
- 005526f8 ["COPY", "tmp:0:8", ["const:964:8"]]
- 005526f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005526f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005526f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005526f8 ["COPY", "tmp:0:8", ["const:9f1:8"]]
+ 005526f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005526f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005526f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005526f8 bytes 08912591
+ 005526f8 bytes 08c52791
- 005526fc ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 005526fc bytes e9eaffd0
+ 005526fc ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 005526fc bytes e9eaffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccafafc5402885b053745f28295c4f7b"></a>

### [`005528f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/005528f8.md) → [`005528f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/005528f8.md) FUN_005528f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052dae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dae0.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00553278`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/00553278.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md)
- 新版 呼出元 1件 [`0052dae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dae0.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00553278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/00553278.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.78% / 新版 92.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00552940",
      "incomplete_value": true,
      "site": "00552950",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2aa000:8"
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
    "old": {
      "definition_site": "00552940",
      "incomplete_value": true,
      "site": "00552950",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:735:8"
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
      "definition_site": "00552944",
      "incomplete_value": true,
      "site": "00552968",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00552944",
      "incomplete_value": true,
      "site": "00552968",
      "value": [
        "LOAD",
        "16",
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
      "00552940",
      "READ",
      [
        "storage",
        "002aa735",
        null,
        "string"
      ]
    ],
    [
      "00552944",
      "READ",
      [
        "storage",
        "002aa742",
        null,
        "string"
      ]
    ],
    [
      "00552a18",
      "PARAM",
      [
        "storage",
        "00c26200",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00552940",
      "READ",
      [
        "storage",
        "002aa73b",
        null,
        "string"
      ]
    ],
    [
      "00552944",
      "READ",
      [
        "storage",
        "002aa748",
        null,
        "string"
      ]
    ],
    [
      "00552a18",
      "PARAM",
      [
        "storage",
        "00c262c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00552938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/005528f8.md#insn-00552938) · [`00552948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/005528f8.md#insn-00552948)
- 新版 `00552938`（命令位置の公開資料なし） · `00552948`（命令位置の公開資料なし）

~~~diff
- 00552938 ["COPY", "tmp:0:8", ["const:735:8"]]
- 00552938 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00552938 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00552938 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00552938 ["COPY", "tmp:0:8", ["const:73b:8"]]
+ 00552938 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00552938 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00552938 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00552938 bytes 08d51c91
+ 00552938 bytes 08ed1c91
- 00552948 ["COPY", "register:4040:8", ["const:2b1000:8"]]
- 00552948 bytes e8eafff0
+ 00552948 ["COPY", "register:4040:8", ["const:2b1000:8"]]
+ 00552948 bytes e8eafff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f053fa54bae35f4a04587e6c6c3dfa65"></a>

### [`00552ab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/00552ab8.md) → [`00552ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/00552ab8.md) FUN_00552ab8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052dae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dae4.md) · 呼出先 13件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md)
- 新版 呼出元 1件 [`0052dae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dae4.md) · 呼出先 13件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.09% / 新版 98.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00552b1c",
      "incomplete_value": true,
      "site": "00552b34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a09:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00552b1c",
      "incomplete_value": true,
      "site": "00552b34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:97c:8"
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
      "00552b1c",
      "READ",
      [
        "storage",
        "0029497c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00552b1c",
      "READ",
      [
        "storage",
        "00294a09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00552b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/00552ab8.md#insn-00552b14)
- 新版 `00552b14`（命令位置の公開資料なし）

~~~diff
- 00552b14 ["COPY", "tmp:0:8", ["const:97c:8"]]
- 00552b14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00552b14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00552b14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00552b14 ["COPY", "tmp:0:8", ["const:a09:8"]]
+ 00552b14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00552b14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00552b14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00552b14 bytes 29f12591
+ 00552b14 bytes 29252891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-017b37461542ea95e689b26bd0a2d5d6"></a>

### [`0055347c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/0055347c.md) → [`0055347c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/0055347c.md) _INIT_30

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`005524e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/005524e0.md) [`00552510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00552/00552510.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005524e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/005524e0.md) [`00552510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/00552510.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005534a4",
      "incomplete_value": false,
      "site": "005534a4",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:2c0:8"
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
      "definition_site": "005534a4",
      "incomplete_value": false,
      "site": "005534a4",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:200:8"
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
      "definition_site": "005534c0",
      "incomplete_value": false,
      "site": "005534c0",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:2f0:8"
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
      "definition_site": "005534c0",
      "incomplete_value": false,
      "site": "005534c0",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:230:8"
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
      "definition_site": "00553494",
      "incomplete_value": false,
      "site": "005534a8",
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
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00553494",
      "incomplete_value": false,
      "site": "005534a8",
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
            "const:200:8"
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
      "00553494",
      "PARAM",
      [
        "storage",
        "00c26200",
        null,
        null
      ]
    ],
    [
      "005534a0",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ],
    [
      "005534a4",
      "WRITE",
      [
        "storage",
        "00c26220",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00553494",
      "PARAM",
      [
        "storage",
        "00c262c0",
        null,
        null
      ]
    ],
    [
      "005534a0",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ],
    [
      "005534a4",
      "WRITE",
      [
        "storage",
        "00c262e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055348c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/0055347c.md#insn-0055348c) · [`00553490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/0055347c.md#insn-00553490)
- 新版 `0055348c`（命令位置の公開資料なし） · `00553490`（命令位置の公開資料なし）

~~~diff
- 0055348c ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 0055348c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0055348c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0055348c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0055348c ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 0055348c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0055348c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0055348c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0055348c bytes 73423b91
+ 0055348c bytes 73023e91
- 00553490 ["COPY", "register:4008:8", ["const:c26000:8"]]
- 00553490 bytes 813600f0
+ 00553490 ["COPY", "register:4008:8", ["const:c26000:8"]]
+ 00553490 bytes 813600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65505f5d4285a7261573e0ee12257872"></a>

### [`005534d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005534d4.md) → [`005534d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005534d4.md) FUN_005534d4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052daf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052daf0.md) · 呼出先 4件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566978.md)
- 新版 呼出元 1件 [`0052daf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052daf0.md) · 呼出先 4件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00553518",
      "incomplete_value": false,
      "site": "00553530",
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
            "const:a6e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00553518",
      "incomplete_value": false,
      "site": "00553530",
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
            "const:9e1:8"
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
      "definition_site": "00553520",
      "incomplete_value": false,
      "site": "00553530",
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
            "const:a7e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00553520",
      "incomplete_value": false,
      "site": "00553530",
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
            "const:9f1:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00553518",
      "PARAM",
      [
        "storage",
        "002939e1",
        null,
        "string"
      ]
    ],
    [
      "00553520",
      "PARAM",
      [
        "storage",
        "002939f1",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00553518",
      "PARAM",
      [
        "storage",
        "00293a6e",
        null,
        "string"
      ]
    ],
    [
      "00553520",
      "PARAM",
      [
        "storage",
        "00293a7e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00553518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005534d4.md#insn-00553518) · [`00553520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005534d4.md#insn-00553520)
- 新版 `00553518`（命令位置の公開資料なし） · `00553520`（命令位置の公開資料なし）

~~~diff
- 00553518 ["COPY", "tmp:0:8", ["const:9e1:8"]]
- 00553518 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00553518 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00553518 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00553518 ["COPY", "tmp:0:8", ["const:a6e:8"]]
+ 00553518 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00553518 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00553518 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00553518 bytes 42842791
+ 00553518 bytes 42b82991
- 00553520 ["COPY", "tmp:0:8", ["const:9f1:8"]]
- 00553520 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00553520 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00553520 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00553520 ["COPY", "tmp:0:8", ["const:a7e:8"]]
+ 00553520 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00553520 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00553520 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00553520 bytes 63c42791
+ 00553520 bytes 63f82991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f5cc83f7db3af5ef57bdc0908feb248"></a>

### [`00553568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/00553568.md) → [`00553568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/00553568.md) FUN_00553568

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052daf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052daf4.md) · 呼出先 4件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566978.md)
- 新版 呼出元 1件 [`0052daf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052daf4.md) · 呼出先 4件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005535b8",
      "incomplete_value": false,
      "site": "005535d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:6cd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005535b8",
      "incomplete_value": false,
      "site": "005535d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "definition_site": "005535c0",
      "incomplete_value": false,
      "site": "005535d0",
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
            "const:55b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005535c0",
      "incomplete_value": false,
      "site": "005535d0",
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
            "const:4ce:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005535b8",
      "PARAM",
      [
        "storage",
        "002a0640",
        null,
        "string"
      ]
    ],
    [
      "005535c0",
      "PARAM",
      [
        "storage",
        "0029d4ce",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005535b8",
      "PARAM",
      [
        "storage",
        "002a06cd",
        null,
        "string"
      ]
    ],
    [
      "005535c0",
      "PARAM",
      [
        "storage",
        "0029d55b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005535b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/00553568.md#insn-005535b8) · [`005535c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/00553568.md#insn-005535c0)
- 新版 `005535b8`（命令位置の公開資料なし） · `005535c0`（命令位置の公開資料なし）

~~~diff
- 005535b8 ["COPY", "tmp:0:8", ["const:640:8"]]
- 005535b8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 005535b8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 005535b8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 005535b8 ["COPY", "tmp:0:8", ["const:6cd:8"]]
+ 005535b8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 005535b8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 005535b8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 005535b8 bytes 42001991
+ 005535b8 bytes 42341b91
- 005535c0 ["COPY", "tmp:0:8", ["const:4ce:8"]]
- 005535c0 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 005535c0 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 005535c0 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 005535c0 ["COPY", "tmp:0:8", ["const:55b:8"]]
+ 005535c0 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 005535c0 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 005535c0 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 005535c0 bytes 63381391
+ 005535c0 bytes 636c1591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30e506e10fd23c807095294508dbf0e0"></a>

### [`00553628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/00553628.md) → [`00553628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/00553628.md) FUN_00553628

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052db20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db20.md) · 呼出先 4件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566978.md)
- 新版 呼出元 1件 [`0052db20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db20.md) · 呼出先 4件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055366c",
      "incomplete_value": false,
      "site": "00553684",
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
            "const:739:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055366c",
      "incomplete_value": false,
      "site": "00553684",
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
            "const:742:8"
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
      "definition_site": "00553674",
      "incomplete_value": false,
      "site": "00553684",
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
            "const:63f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00553674",
      "incomplete_value": false,
      "site": "00553684",
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
            "const:5b2:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0055366c",
      "PARAM",
      [
        "storage",
        "002a9742",
        null,
        "string"
      ]
    ],
    [
      "00553674",
      "PARAM",
      [
        "storage",
        "0029e5b2",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0055366c",
      "PARAM",
      [
        "storage",
        "002a9739",
        null,
        "string"
      ]
    ],
    [
      "00553674",
      "PARAM",
      [
        "storage",
        "0029e63f",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055366c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/00553628.md#insn-0055366c) · [`00553674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/00553628.md#insn-00553674)
- 新版 `0055366c`（命令位置の公開資料なし） · `00553674`（命令位置の公開資料なし）

~~~diff
- 0055366c ["COPY", "tmp:0:8", ["const:742:8"]]
- 0055366c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0055366c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0055366c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0055366c ["COPY", "tmp:0:8", ["const:739:8"]]
+ 0055366c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0055366c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0055366c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0055366c bytes 42081d91
+ 0055366c bytes 42e41c91
- 00553674 ["COPY", "tmp:0:8", ["const:5b2:8"]]
- 00553674 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00553674 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00553674 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00553674 ["COPY", "tmp:0:8", ["const:63f:8"]]
+ 00553674 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00553674 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00553674 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00553674 bytes 63c81691
+ 00553674 bytes 63fc1891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6746603b34aa9935b6235ca553e6f32d"></a>

### [`005536e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005536e4.md) → [`005536e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005536e4.md) FUN_005536e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052db24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db24.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0052db24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db24.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00553720",
      "incomplete_value": true,
      "site": "00553738",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5d3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00553720",
      "incomplete_value": true,
      "site": "00553738",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5da:8"
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
      "00553720",
      "READ",
      [
        "storage",
        "002a45da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00553720",
      "READ",
      [
        "storage",
        "002a45d3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00553714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005536e4.md#insn-00553714)
- 新版 `00553714`（命令位置の公開資料なし）

~~~diff
- 00553714 ["COPY", "tmp:0:8", ["const:5da:8"]]
- 00553714 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00553714 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00553714 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00553714 ["COPY", "tmp:0:8", ["const:5d3:8"]]
+ 00553714 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00553714 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00553714 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00553714 bytes 29691791
+ 00553714 bytes 294d1791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b45370e9473eceff7fc9db79445fa792"></a>

### [`00553828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/00553828.md) → [`00553828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/00553828.md) FUN_00553828

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00553950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/00553950.md) · 呼出先 7件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566978.md)
- 新版 呼出元 1件 [`00553950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/00553950.md) · 呼出先 7件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.89% / 新版 95.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00553850",
      "incomplete_value": true,
      "site": "00553854",
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
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00553850",
      "incomplete_value": true,
      "site": "00553854",
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
            "const:aa0:8"
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
      "00553854",
      "DATA",
      [
        "storage",
        "00beeaa0",
        null,
        "undefined *"
      ]
    ],
    [
      "00553878",
      "READ",
      [
        "storage",
        "002939f5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00553854",
      "DATA",
      [
        "storage",
        "00beeb50",
        null,
        "undefined *"
      ]
    ],
    [
      "00553878",
      "READ",
      [
        "storage",
        "00293a82",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00553850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/00553828.md#insn-00553850) · [`0055386c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/00553828.md#insn-0055386c)
- 新版 `00553850`（命令位置の公開資料なし） · `0055386c`（命令位置の公開資料なし）

~~~diff
- 00553850 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 00553850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00553850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00553850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00553850 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 00553850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00553850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00553850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00553850 bytes 08812a91
+ 00553850 bytes 08412d91
- 0055386c ["COPY", "tmp:0:8", ["const:9f5:8"]]
- 0055386c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055386c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055386c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055386c ["COPY", "tmp:0:8", ["const:a82:8"]]
+ 0055386c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055386c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055386c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055386c bytes 29d52791
+ 0055386c bytes 29092a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8efa5c94fdb23ebfca2b0886067d041a"></a>

### [`00553ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/00553ac4.md) → [`00553ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/00553ac4.md) FUN_00553ac4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00554440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554440.md) [`00554a08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554a08.md) [`00554da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554da8.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`00558f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md)
- 新版 呼出元 3件 [`00554440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/00554440.md) [`00554a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/00554a08.md) [`00554da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/00554da8.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00558f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.21% / 新版 97.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00553b38",
      "incomplete_value": true,
      "site": "00553b38",
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
                "const:759:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00553b38",
      "incomplete_value": true,
      "site": "00553b38",
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
                "const:753:8"
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
      "definition_site": "00553b3c",
      "incomplete_value": true,
      "site": "00553b3c",
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
      "definition_site": "00553b3c",
      "incomplete_value": true,
      "site": "00553b3c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00553b28",
      "READ",
      [
        "storage",
        "002aa753",
        null,
        "string"
      ]
    ],
    [
      "00553b30",
      "READ",
      [
        "storage",
        "002aa759",
        null,
        "string"
      ]
    ],
    [
      "00553c08",
      "READ",
      [
        "storage",
        "00291bb7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00553b28",
      "READ",
      [
        "storage",
        "002aa759",
        null,
        "string"
      ]
    ],
    [
      "00553b30",
      "READ",
      [
        "storage",
        "002aa75f",
        null,
        "string"
      ]
    ],
    [
      "00553c08",
      "READ",
      [
        "storage",
        "00291c44",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00553b24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/00553ac4.md#insn-00553b24) · [`00553bfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/00553ac4.md#insn-00553bfc) · [`00553dd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/00553ac4.md#insn-00553dd4)
- 新版 `00553b24`（命令位置の公開資料なし） · `00553bfc`（命令位置の公開資料なし） · `00553dd4`（命令位置の公開資料なし）

~~~diff
- 00553b24 ["COPY", "tmp:0:8", ["const:753:8"]]
- 00553b24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00553b24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00553b24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00553b24 ["COPY", "tmp:0:8", ["const:759:8"]]
+ 00553b24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00553b24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00553b24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00553b24 bytes 294d1d91
+ 00553b24 bytes 29651d91
- 00553bfc ["COPY", "tmp:0:8", ["const:bb7:8"]]
- 00553bfc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00553bfc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00553bfc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00553bfc ["COPY", "tmp:0:8", ["const:c44:8"]]
+ 00553bfc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00553bfc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00553bfc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00553bfc bytes 29dd2e91
+ 00553bfc bytes 29113191
- 00553dd4 ["COPY", "tmp:0:8", ["const:a09:8"]]
- 00553dd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00553dd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00553dd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00553dd4 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00553dd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00553dd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00553dd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00553dd4 bytes 29252891
+ 00553dd4 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b8655bc01f50d08ccd978288370d68a"></a>

### [`00554030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554030.md) → [`00554030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/00554030.md) FUN_00554030

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00554440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554440.md) [`00554da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554da8.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566978.md)
- 新版 呼出元 2件 [`00554440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/00554440.md) [`00554da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/00554da8.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00554090",
      "incomplete_value": true,
      "site": "005540a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c3f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00554090",
      "incomplete_value": true,
      "site": "005540a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bb2:8"
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
      "definition_site": "005540a8",
      "incomplete_value": true,
      "site": "005540a8",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005540a8",
      "incomplete_value": true,
      "site": "005540a8",
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
                "const:e:8"
              ]
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
      "00554074",
      "READ",
      [
        "storage",
        "00294991",
        null,
        "string"
      ]
    ],
    [
      "0055407c",
      "READ",
      [
        "storage",
        "00294997",
        null,
        "string"
      ]
    ],
    [
      "00554090",
      "READ",
      [
        "storage",
        "00296bb2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00554074",
      "READ",
      [
        "storage",
        "00294a1e",
        null,
        "string"
      ]
    ],
    [
      "0055407c",
      "READ",
      [
        "storage",
        "00294a24",
        null,
        "string"
      ]
    ],
    [
      "00554090",
      "READ",
      [
        "storage",
        "00296c3f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00554070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554030.md#insn-00554070) · [`00554084`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554030.md#insn-00554084)
- 新版 `00554070`（命令位置の公開資料なし） · `00554084`（命令位置の公開資料なし）

~~~diff
- 00554070 ["COPY", "tmp:0:8", ["const:991:8"]]
- 00554070 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00554070 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00554070 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00554070 ["COPY", "tmp:0:8", ["const:a1e:8"]]
+ 00554070 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00554070 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00554070 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00554070 bytes 29452691
+ 00554070 bytes 29792891
- 00554084 ["COPY", "tmp:0:8", ["const:bb2:8"]]
- 00554084 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00554084 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00554084 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00554084 ["COPY", "tmp:0:8", ["const:c3f:8"]]
+ 00554084 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00554084 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00554084 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00554084 bytes 29c92e91
+ 00554084 bytes 29fd3091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1e65639d4b8af1b19e36f5559418345"></a>

### [`00554274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554274.md) → [`00554274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/00554274.md) FUN_00554274

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00554a08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554a08.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566978.md)
- 新版 呼出元 1件 [`00554a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/00554a08.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.33% / 新版 89.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005542d0",
      "incomplete_value": true,
      "site": "005542d0",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:7f2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005542d0",
      "incomplete_value": true,
      "site": "005542d0",
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
                "const:2ab000:8"
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005542d8",
      "incomplete_value": true,
      "site": "005542d8",
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
      "definition_site": "005542d8",
      "incomplete_value": true,
      "site": "005542d8",
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
      "005542b8",
      "READ",
      [
        "storage",
        "002ab7ec",
        null,
        "string"
      ]
    ],
    [
      "005542c0",
      "READ",
      [
        "storage",
        "002ab7f1",
        null,
        "string"
      ]
    ],
    [
      "005542d4",
      "READ",
      [
        "storage",
        "00296bb2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005542b8",
      "READ",
      [
        "storage",
        "002ab7f2",
        null,
        "string"
      ]
    ],
    [
      "005542c0",
      "READ",
      [
        "storage",
        "002ab7f7",
        null,
        "string"
      ]
    ],
    [
      "005542d4",
      "READ",
      [
        "storage",
        "00296c3f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005542b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554274.md#insn-005542b4) · [`005542c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554274.md#insn-005542c4)
- 新版 `005542b4`（命令位置の公開資料なし） · `005542c4`（命令位置の公開資料なし）

~~~diff
- 005542b4 ["COPY", "tmp:0:8", ["const:7ec:8"]]
- 005542b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005542b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005542b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005542b4 ["COPY", "tmp:0:8", ["const:7f2:8"]]
+ 005542b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005542b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005542b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005542b4 bytes 29b11f91
+ 005542b4 bytes 29c91f91
- 005542c4 ["COPY", "register:4048:8", ["const:296000:8"]]
- 005542c4 bytes 09eaffd0
+ 005542c4 ["COPY", "register:4048:8", ["const:296000:8"]]
+ 005542c4 bytes 09eaffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a915b6bc5f33ef2debaa6540d8754e32"></a>

### [`00554440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554440.md) → [`00554440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/00554440.md) FUN_00554440

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052db2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db2c.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`00553ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/00553ac4.md) [`00554030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554030.md) [`005541a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/005541a8.md)
- 新版 呼出元 1件 [`0052db2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db2c.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00553ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/00553ac4.md) [`00554030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/00554030.md) [`005541a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/005541a8.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055457c",
      "incomplete_value": false,
      "site": "00554584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055457c",
      "incomplete_value": false,
      "site": "00554584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
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
      "definition_site": "00554594",
      "incomplete_value": false,
      "site": "00554594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00554594",
      "incomplete_value": false,
      "site": "00554594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00554640",
      "incomplete_value": true,
      "site": "00554640",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00554640",
      "incomplete_value": true,
      "site": "00554640",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005544a8",
      "READ",
      [
        "storage",
        "002a974e",
        null,
        "string"
      ]
    ],
    [
      "00554584",
      "DATA",
      [
        "storage",
        "00beedc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00554594",
      "DATA",
      [
        "storage",
        "00beeaa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005544a8",
      "READ",
      [
        "storage",
        "002a9745",
        null,
        "string"
      ]
    ],
    [
      "00554584",
      "DATA",
      [
        "storage",
        "00beee70",
        null,
        "undefined *"
      ]
    ],
    [
      "00554594",
      "DATA",
      [
        "storage",
        "00beeb50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00554640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554440.md#insn-00554640) · [`0055449c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554440.md#insn-0055449c) · [`0055457c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554440.md#insn-0055457c)
- 新版 `00554640`（命令位置の公開資料なし） · `0055449c`（命令位置の公開資料なし） · `0055457c`（命令位置の公開資料なし）

~~~diff
- 00554640 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b0:8"]]
- 00554640 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00554640 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
+ 00554640 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00554640 bytes 095901f9
+ 00554640 bytes 09b901f9
- 0055449c ["COPY", "tmp:0:8", ["const:74e:8"]]
- 0055449c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055449c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055449c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055449c ["COPY", "tmp:0:8", ["const:745:8"]]
+ 0055449c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055449c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055449c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055449c bytes 29391d91
+ 0055449c bytes 29151d91
- 0055457c ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 0055457c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055457c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055457c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055457c ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 0055457c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055457c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055457c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055457c bytes 08013791
+ 0055457c bytes 08c13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44c4531aabb5e9eb737e368a793ed176"></a>

### [`005547a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/005547a0.md) → [`005547a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/005547a0.md) FUN_005547a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00554914`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554914.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`00554914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/00554914.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.31% / 新版 95.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005547c0",
      "incomplete_value": false,
      "site": "005547c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005547c0",
      "incomplete_value": false,
      "site": "005547c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:b28:8"
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
      "005547c0",
      "DATA",
      [
        "storage",
        "00beeb28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005547c0",
      "DATA",
      [
        "storage",
        "00beebd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005547b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/005547a0.md#insn-005547b8) · [`005547bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/005547a0.md#insn-005547bc)
- 新版 `005547b8`（命令位置の公開資料なし） · `005547bc`（命令位置の公開資料なし）

~~~diff
- 005547b8 ["COPY", "tmp:0:8", ["const:b28:8"]]
- 005547b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005547b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005547b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005547b8 ["COPY", "tmp:0:8", ["const:bd8:8"]]
+ 005547b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005547b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005547b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005547b8 bytes 08a12c91
+ 005547b8 bytes 08612f91
- 005547bc ["COPY", "register:40a0:8", ["register:4000:8"]]
- 005547bc bytes f40300aa
+ 005547bc ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 005547bc bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5aa4a46e98e9a36577469a968eaca28f"></a>

### [`00554a08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554a08.md) → [`00554a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/00554a08.md) FUN_00554a08

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`00553ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/00553ac4.md) [`005541a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/005541a8.md) [`00554274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554274.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00553ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/00553ac4.md) [`005541a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/005541a8.md) [`00554274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/00554274.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 95.67% / 新版 95.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00554b48",
      "incomplete_value": false,
      "site": "00554b50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00554b48",
      "incomplete_value": false,
      "site": "00554b50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00554c0c",
      "incomplete_value": true,
      "site": "00554c0c",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00554c0c",
      "incomplete_value": true,
      "site": "00554c0c",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00554c08",
      "incomplete_value": true,
      "site": "00554c08",
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
      "definition_site": "00554c08",
      "incomplete_value": true,
      "site": "00554c08",
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
    "ordinal": 10,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00554a74",
      "READ",
      [
        "storage",
        "002a974e",
        null,
        "string"
      ]
    ],
    [
      "00554b50",
      "DATA",
      [
        "storage",
        "00beedc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00554b60",
      "DATA",
      [
        "storage",
        "00beeaa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00554a74",
      "READ",
      [
        "storage",
        "002a9745",
        null,
        "string"
      ]
    ],
    [
      "00554b50",
      "DATA",
      [
        "storage",
        "00beee70",
        null,
        "undefined *"
      ]
    ],
    [
      "00554b60",
      "DATA",
      [
        "storage",
        "00beeb50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00554c0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554a08.md#insn-00554c0c) · [`00554a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554a08.md#insn-00554a68) · [`00554b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554a08.md#insn-00554b48)
- 新版 `00554c0c`（命令位置の公開資料なし） · `00554a68`（命令位置の公開資料なし） · `00554b48`（命令位置の公開資料なし）

~~~diff
- 00554c0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b0:8"]]
- 00554c0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00554c0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
+ 00554c0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00554c0c bytes 095901f9
+ 00554c0c bytes 09b901f9
- 00554a68 ["COPY", "tmp:0:8", ["const:74e:8"]]
- 00554a68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00554a68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00554a68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00554a68 ["COPY", "tmp:0:8", ["const:745:8"]]
+ 00554a68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00554a68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00554a68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00554a68 bytes 29391d91
+ 00554a68 bytes 29151d91
- 00554b48 ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 00554b48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00554b48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00554b48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00554b48 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 00554b48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00554b48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00554b48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00554b48 bytes 08013791
+ 00554b48 bytes 08c13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53b4660b70e2304e7418eedbc4ea0ae8"></a>

### [`00554da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554da8.md) → [`00554da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/00554da8.md) FUN_00554da8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 16件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`00553ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/00553ac4.md) [`00554030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554030.md) [`005541a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/005541a8.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00553ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/00553ac4.md) [`00554030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/00554030.md) [`005541a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/005541a8.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 94.71% / 新版 94.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00554f00",
      "incomplete_value": false,
      "site": "00554f00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00554f00",
      "incomplete_value": false,
      "site": "00554f00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00554fac",
      "incomplete_value": true,
      "site": "00554fac",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00554fac",
      "incomplete_value": true,
      "site": "00554fac",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00554fa8",
      "incomplete_value": true,
      "site": "00554fa8",
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
      "definition_site": "00554fa8",
      "incomplete_value": true,
      "site": "00554fa8",
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
    "ordinal": 10,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00554e14",
      "READ",
      [
        "storage",
        "002a974e",
        null,
        "string"
      ]
    ],
    [
      "00554ef0",
      "DATA",
      [
        "storage",
        "00beedc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00554f00",
      "DATA",
      [
        "storage",
        "00beeaa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00554e14",
      "READ",
      [
        "storage",
        "002a9745",
        null,
        "string"
      ]
    ],
    [
      "00554ef0",
      "DATA",
      [
        "storage",
        "00beee70",
        null,
        "undefined *"
      ]
    ],
    [
      "00554f00",
      "DATA",
      [
        "storage",
        "00beeb50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00554fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554da8.md#insn-00554fac) · [`00554e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554da8.md#insn-00554e08) · [`00554ee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00554/00554da8.md#insn-00554ee8)
- 新版 `00554fac`（命令位置の公開資料なし） · `00554e08`（命令位置の公開資料なし） · `00554ee8`（命令位置の公開資料なし）

~~~diff
- 00554fac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b0:8"]]
- 00554fac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00554fac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
+ 00554fac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00554fac bytes 095901f9
+ 00554fac bytes 09b901f9
- 00554e08 ["COPY", "tmp:0:8", ["const:74e:8"]]
- 00554e08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00554e08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00554e08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00554e08 ["COPY", "tmp:0:8", ["const:745:8"]]
+ 00554e08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00554e08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00554e08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00554e08 bytes 29391d91
+ 00554e08 bytes 29151d91
- 00554ee8 ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 00554ee8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00554ee8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00554ee8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00554ee8 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 00554ee8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00554ee8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00554ee8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00554ee8 bytes 08013791
+ 00554ee8 bytes 08c13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfca4c6f9824d74f20426e4616198104"></a>

### [`00555148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555148.md) → [`00555148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00555/00555148.md) FUN_00555148

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005552ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/005552ec.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00559348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559348.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`005552ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00555/005552ec.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00559348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559348.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.15% / 新版 95.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00555174",
      "incomplete_value": false,
      "site": "00555178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00555174",
      "incomplete_value": false,
      "site": "00555178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:b48:8"
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
      "00555178",
      "DATA",
      [
        "storage",
        "00beeb48",
        null,
        "undefined *"
      ]
    ],
    [
      "0055519c",
      "READ",
      [
        "storage",
        "002939f5",
        null,
        "string"
      ]
    ],
    [
      "0055523c",
      "PARAM",
      [
        "storage",
        "00c262b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00555178",
      "DATA",
      [
        "storage",
        "00beebf8",
        null,
        "undefined *"
      ]
    ],
    [
      "0055519c",
      "READ",
      [
        "storage",
        "00293a82",
        null,
        "string"
      ]
    ],
    [
      "0055523c",
      "PARAM",
      [
        "storage",
        "00c26370",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00555174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555148.md#insn-00555174) · [`00555190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555148.md#insn-00555190) · [`00555228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555148.md#insn-00555228)
- 新版 `00555174`（命令位置の公開資料なし） · `00555190`（命令位置の公開資料なし） · `00555228`（命令位置の公開資料なし）

~~~diff
- 00555174 ["COPY", "tmp:0:8", ["const:b48:8"]]
- 00555174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00555174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00555174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00555174 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00555174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00555174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00555174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00555174 bytes 08212d91
+ 00555174 bytes 08e12f91
- 00555190 ["COPY", "tmp:0:8", ["const:9f5:8"]]
- 00555190 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00555190 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00555190 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00555190 ["COPY", "tmp:0:8", ["const:a82:8"]]
+ 00555190 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00555190 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00555190 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00555190 bytes 29d52791
+ 00555190 bytes 29092a91
- 00555228 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 00555228 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00555228 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00555228 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00555228 ["COPY", "tmp:0:8", ["const:370:8"]]
+ 00555228 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00555228 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00555228 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00555228 bytes 94c20a91
+ 00555228 bytes 94c20d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3aef2b3c96a07a04a24ebe46d88fb85"></a>

### [`00555484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555484.md) → [`00555484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00555/00555484.md) FUN_00555484

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.54% / 新版 92.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005554f0",
      "incomplete_value": true,
      "site": "005554f0",
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
                "const:561:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005554f0",
      "incomplete_value": true,
      "site": "005554f0",
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
                "const:4d4:8"
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
      "definition_site": "00555508",
      "incomplete_value": true,
      "site": "00555518",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6df:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00555508",
      "incomplete_value": true,
      "site": "00555518",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6e6:8"
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
      "definition_site": "0055551c",
      "incomplete_value": true,
      "site": "0055551c",
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
      "definition_site": "0055551c",
      "incomplete_value": true,
      "site": "0055551c",
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
      "005554dc",
      "READ",
      [
        "storage",
        "0029d4d4",
        null,
        "string"
      ]
    ],
    [
      "00555508",
      "READ",
      [
        "storage",
        "002a56e6",
        null,
        "string"
      ]
    ],
    [
      "0055550c",
      "READ",
      [
        "storage",
        "002a56f5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005554dc",
      "READ",
      [
        "storage",
        "0029d561",
        null,
        "string"
      ]
    ],
    [
      "00555508",
      "READ",
      [
        "storage",
        "002a56df",
        null,
        "string"
      ]
    ],
    [
      "0055550c",
      "READ",
      [
        "storage",
        "002a56ee",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055557c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555484.md#insn-0055557c) · [`005556ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555484.md#insn-005556ac) · [`005554d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555484.md#insn-005554d0)
- 新版 `0055557c`（命令位置の公開資料なし） · `005556ac`（命令位置の公開資料なし） · `005554d0`（命令位置の公開資料なし）

~~~diff
- 0055557c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a8:8"]]
- 0055557c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:4"]]
+ 0055557c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
+ 0055557c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:4"]]
- 0055557c bytes 16a902b9
+ 0055557c bytes 166903b9
- 005556ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
- 005556ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 005556ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:350:8"]]
+ 005556ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 005556ac bytes 094901f9
+ 005556ac bytes 09a901f9
- 005554d0 ["COPY", "tmp:0:8", ["const:4d4:8"]]
- 005554d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005554d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005554d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005554d0 ["COPY", "tmp:0:8", ["const:561:8"]]
+ 005554d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005554d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005554d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005554d0 bytes 29511391
+ 005554d0 bytes 29851591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bab05850725460fe3e97f69925eaf8f"></a>

### [`005558b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/005558b8.md) → [`005558b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00555/005558b8.md) FUN_005558b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.61% / 新版 89.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00555914",
      "incomplete_value": true,
      "site": "00555914",
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
                "const:561:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00555914",
      "incomplete_value": true,
      "site": "00555914",
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
                "const:4d4:8"
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
      "definition_site": "00555928",
      "incomplete_value": true,
      "site": "00555930",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c3f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00555928",
      "incomplete_value": true,
      "site": "00555930",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bb2:8"
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
      "definition_site": "00555934",
      "incomplete_value": true,
      "site": "00555934",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00555934",
      "incomplete_value": true,
      "site": "00555934",
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
                "const:e:8"
              ]
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
      "00555904",
      "READ",
      [
        "storage",
        "0029d4d4",
        null,
        "string"
      ]
    ],
    [
      "00555928",
      "READ",
      [
        "storage",
        "00296bb2",
        null,
        "string"
      ]
    ],
    [
      "0055592c",
      "READ",
      [
        "storage",
        "00296bc0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00555904",
      "READ",
      [
        "storage",
        "0029d561",
        null,
        "string"
      ]
    ],
    [
      "00555928",
      "READ",
      [
        "storage",
        "00296c3f",
        null,
        "string"
      ]
    ],
    [
      "0055592c",
      "READ",
      [
        "storage",
        "00296c4d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00555900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/005558b8.md#insn-00555900) · [`00555924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/005558b8.md#insn-00555924)
- 新版 `00555900`（命令位置の公開資料なし） · `00555924`（命令位置の公開資料なし）

~~~diff
- 00555900 ["COPY", "tmp:0:8", ["const:4d4:8"]]
- 00555900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00555900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00555900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00555900 ["COPY", "tmp:0:8", ["const:561:8"]]
+ 00555900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00555900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00555900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00555900 bytes 08511391
+ 00555900 bytes 08851591
- 00555924 ["COPY", "tmp:0:8", ["const:bb2:8"]]
- 00555924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00555924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00555924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00555924 ["COPY", "tmp:0:8", ["const:c3f:8"]]
+ 00555924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00555924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00555924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00555924 bytes 08c92e91
+ 00555924 bytes 08fd3091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d896731ac2c0a55b9a5f970503b7ecc"></a>

### [`00555a38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555a38.md) → [`00555a38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00555/00555a38.md) FUN_00555a38

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00555a90",
      "incomplete_value": true,
      "site": "00555a90",
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
                "const:528:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00555a90",
      "incomplete_value": true,
      "site": "00555a90",
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
                "const:49b:8"
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
      "definition_site": "00555a98",
      "incomplete_value": true,
      "site": "00555a98",
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
      "definition_site": "00555a98",
      "incomplete_value": true,
      "site": "00555a98",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00555a94",
      "incomplete_value": true,
      "site": "00555aa8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6f7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00555a94",
      "incomplete_value": true,
      "site": "00555aa8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6fe:8"
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
      "00555a78",
      "READ",
      [
        "storage",
        "0029b49b",
        null,
        "string"
      ]
    ],
    [
      "00555a80",
      "READ",
      [
        "storage",
        "0029b4a0",
        null,
        "string"
      ]
    ],
    [
      "00555a94",
      "READ",
      [
        "storage",
        "002a56fe",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00555a78",
      "READ",
      [
        "storage",
        "0029b528",
        null,
        "string"
      ]
    ],
    [
      "00555a80",
      "READ",
      [
        "storage",
        "0029b52d",
        null,
        "string"
      ]
    ],
    [
      "00555a94",
      "READ",
      [
        "storage",
        "002a56f7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00555a74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555a38.md#insn-00555a74) · [`00555a84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555a38.md#insn-00555a84)
- 新版 `00555a74`（命令位置の公開資料なし） · `00555a84`（命令位置の公開資料なし）

~~~diff
- 00555a74 ["COPY", "tmp:0:8", ["const:49b:8"]]
- 00555a74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00555a74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00555a74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00555a74 ["COPY", "tmp:0:8", ["const:528:8"]]
+ 00555a74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00555a74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00555a74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00555a74 bytes 296d1291
+ 00555a74 bytes 29a11491
- 00555a84 ["COPY", "register:4048:8", ["const:2a5000:8"]]
- 00555a84 bytes 89eaff90
+ 00555a84 ["COPY", "register:4048:8", ["const:2a5000:8"]]
+ 00555a84 bytes 89eaff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf369bb16684eac4019c5a1aeacadce2"></a>

### [`00555bd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555bd4.md) → [`00555bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00555/00555bd4.md) FUN_00555bd4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

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
      "definition_site": "00555c20",
      "incomplete_value": true,
      "site": "00555c20",
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
                "const:f84:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00555c20",
      "incomplete_value": true,
      "site": "00555c20",
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
                "const:ef7:8"
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
      "definition_site": "00555c24",
      "incomplete_value": true,
      "site": "00555c24",
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
      "definition_site": "00555c24",
      "incomplete_value": true,
      "site": "00555c24",
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
      "00555c10",
      "READ",
      [
        "storage",
        "00298ef7",
        null,
        "string"
      ]
    ],
    [
      "00555c18",
      "READ",
      [
        "storage",
        "00298efc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00555c10",
      "READ",
      [
        "storage",
        "00298f84",
        null,
        "string"
      ]
    ],
    [
      "00555c18",
      "READ",
      [
        "storage",
        "00298f89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00555c0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555bd4.md#insn-00555c0c)
- 新版 `00555c0c`（命令位置の公開資料なし）

~~~diff
- 00555c0c ["COPY", "tmp:0:8", ["const:ef7:8"]]
- 00555c0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00555c0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00555c0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00555c0c ["COPY", "tmp:0:8", ["const:f84:8"]]
+ 00555c0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00555c0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00555c0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00555c0c bytes 29dd3b91
+ 00555c0c bytes 29113e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a681aade34ec1a5e89c3f820bd9a140e"></a>

### [`00555d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555d04.md) → [`00555d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00555/00555d04.md) FUN_00555d04

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)

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
      "definition_site": "00555d50",
      "incomplete_value": true,
      "site": "00555d50",
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
                "const:6db:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00555d50",
      "incomplete_value": true,
      "site": "00555d50",
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
                "const:64e:8"
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
      "definition_site": "00555d54",
      "incomplete_value": true,
      "site": "00555d54",
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
      "definition_site": "00555d54",
      "incomplete_value": true,
      "site": "00555d54",
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
      "00555d40",
      "READ",
      [
        "storage",
        "002a064e",
        null,
        "string"
      ]
    ],
    [
      "00555d48",
      "READ",
      [
        "storage",
        "002a0653",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00555d40",
      "READ",
      [
        "storage",
        "002a06db",
        null,
        "string"
      ]
    ],
    [
      "00555d48",
      "READ",
      [
        "storage",
        "002a06e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00555d3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555d04.md#insn-00555d3c)
- 新版 `00555d3c`（命令位置の公開資料なし）

~~~diff
- 00555d3c ["COPY", "tmp:0:8", ["const:64e:8"]]
- 00555d3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00555d3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00555d3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00555d3c ["COPY", "tmp:0:8", ["const:6db:8"]]
+ 00555d3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00555d3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00555d3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00555d3c bytes 29391991
+ 00555d3c bytes 296d1b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a1bef43bef24d2467955b12b5b80c1d"></a>

### [`00555e74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555e74.md) → [`00555e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00555/00555e74.md) FUN_00555e74

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)

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
      "definition_site": "00555ec0",
      "incomplete_value": true,
      "site": "00555ec0",
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
                "const:539:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00555ec0",
      "incomplete_value": true,
      "site": "00555ec0",
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
                "const:540:8"
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
      "definition_site": "00555ec4",
      "incomplete_value": true,
      "site": "00555ec4",
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
      "definition_site": "00555ec4",
      "incomplete_value": true,
      "site": "00555ec4",
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
      "00555eb0",
      "READ",
      [
        "storage",
        "002a3540",
        null,
        "string"
      ]
    ],
    [
      "00555eb8",
      "READ",
      [
        "storage",
        "002a3545",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00555eb0",
      "READ",
      [
        "storage",
        "002a3539",
        null,
        "string"
      ]
    ],
    [
      "00555eb8",
      "READ",
      [
        "storage",
        "002a353e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00555eac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555e74.md#insn-00555eac)
- 新版 `00555eac`（命令位置の公開資料なし）

~~~diff
- 00555eac ["COPY", "tmp:0:8", ["const:540:8"]]
- 00555eac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00555eac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00555eac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00555eac ["COPY", "tmp:0:8", ["const:539:8"]]
+ 00555eac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00555eac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00555eac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00555eac bytes 29011591
+ 00555eac bytes 29e51491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29d744e41133abf0ed79d05d69422b80"></a>

### [`00555fe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555fe4.md) → [`00555fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00555/00555fe4.md) FUN_00555fe4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 19件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`0055664c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00556/0055664c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`0055664c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00556/0055664c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 93.12% / 新版 93.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00556144",
      "incomplete_value": true,
      "site": "00556144",
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
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00556144",
      "incomplete_value": true,
      "site": "00556144",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005563b8",
      "incomplete_value": true,
      "site": "005563b8",
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
                "const:56d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005563b8",
      "incomplete_value": true,
      "site": "005563b8",
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
                "const:4e0:8"
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
      "definition_site": "005563bc",
      "incomplete_value": true,
      "site": "005563bc",
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
      "definition_site": "005563bc",
      "incomplete_value": true,
      "site": "005563bc",
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
      "005560c0",
      "READ",
      [
        "storage",
        "00c26280",
        null,
        "undefined8"
      ]
    ],
    [
      "00556124",
      "DATA",
      [
        "storage",
        "00c26280",
        null,
        "undefined8"
      ]
    ],
    [
      "00556134",
      "WRITE",
      [
        "storage",
        "00c26280",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005560c0",
      "READ",
      [
        "storage",
        "00c26340",
        null,
        "undefined8"
      ]
    ],
    [
      "00556124",
      "DATA",
      [
        "storage",
        "00c26340",
        null,
        "undefined8"
      ]
    ],
    [
      "00556134",
      "WRITE",
      [
        "storage",
        "00c26340",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00556144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555fe4.md#insn-00556144) · [`005560b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555fe4.md#insn-005560b8) · [`00556138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555fe4.md#insn-00556138)
- 新版 `00556144`（命令位置の公開資料なし） · `005560b8`（命令位置の公開資料なし） · `00556138`（命令位置の公開資料なし）

~~~diff
- 00556144 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:278:8"]]
- 00556144 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00556144 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:338:8"]]
+ 00556144 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00556144 bytes 093d01f9
+ 00556144 bytes 099d01f9
- 005560b8 ["COPY", "tmp:0:8", ["const:280:8"]]
- 005560b8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005560b8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005560b8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005560b8 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 005560b8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005560b8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005560b8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005560b8 bytes 73020a91
+ 005560b8 bytes 73020d91
- 00556138 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:278:8"]]
- 00556138 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00556138 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:338:8"]]
+ 00556138 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00556138 bytes 093d41f9
+ 00556138 bytes 099d41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2f5f54d0ea06854bf6d99480ad60110"></a>

### [`0055664c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00556/0055664c.md) → [`0055664c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00556/0055664c.md) FUN_0055664c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00555fe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555fe4.md) · 呼出先 11件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00574784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574784.md) [`00574810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574810.md) [`00574bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574bb4.md) [`00574bbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574bbc.md)
- 新版 呼出元 1件 [`00555fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00555/00555fe4.md) · 呼出先 11件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00574784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574784.md) [`00574810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574810.md) [`00574bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574bb4.md) [`00574bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574bbc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005567ec",
      "incomplete_value": false,
      "site": "005567f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:6e9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005567ec",
      "incomplete_value": false,
      "site": "005567f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:65c:8"
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
      "definition_site": "00556850",
      "incomplete_value": false,
      "site": "00556858",
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
            "const:536:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00556850",
      "incomplete_value": false,
      "site": "00556858",
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
            "const:4a9:8"
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
      "definition_site": "005568b0",
      "incomplete_value": false,
      "site": "005568c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:a2d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005568b0",
      "incomplete_value": false,
      "site": "005568c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
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
      "005567ec",
      "PARAM",
      [
        "storage",
        "002a065c",
        null,
        "string"
      ]
    ],
    [
      "00556850",
      "PARAM",
      [
        "storage",
        "0029b4a9",
        null,
        "string"
      ]
    ],
    [
      "005568b0",
      "PARAM",
      [
        "storage",
        "002949a0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005567ec",
      "PARAM",
      [
        "storage",
        "002a06e9",
        null,
        "string"
      ]
    ],
    [
      "00556850",
      "PARAM",
      [
        "storage",
        "0029b536",
        null,
        "string"
      ]
    ],
    [
      "005568b0",
      "PARAM",
      [
        "storage",
        "00294a2d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005567ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00556/0055664c.md#insn-005567ec) · [`00556850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00556/0055664c.md#insn-00556850) · [`005568b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00556/0055664c.md#insn-005568b0)
- 新版 `005567ec`（命令位置の公開資料なし） · `00556850`（命令位置の公開資料なし） · `005568b0`（命令位置の公開資料なし）

~~~diff
- 005567ec ["COPY", "tmp:0:8", ["const:65c:8"]]
- 005567ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005567ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005567ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005567ec ["COPY", "tmp:0:8", ["const:6e9:8"]]
+ 005567ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005567ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005567ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005567ec bytes 21701991
+ 005567ec bytes 21a41b91
- 00556850 ["COPY", "tmp:0:8", ["const:4a9:8"]]
- 00556850 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00556850 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00556850 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00556850 ["COPY", "tmp:0:8", ["const:536:8"]]
+ 00556850 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00556850 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00556850 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00556850 bytes 21a41291
+ 00556850 bytes 21d81491
- 005568b0 ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 005568b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005568b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005568b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005568b0 ["COPY", "tmp:0:8", ["const:a2d:8"]]
+ 005568b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005568b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005568b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005568b0 bytes 21802691
+ 005568b0 bytes 21b42891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10566fe88dce5cb6eabf55cb0fdedc4b"></a>

### [`00556bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00556/00556bf4.md) → [`00556bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00556/00556bf4.md) FUN_00556bf4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 94.49% / 新版 94.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00556d50",
      "incomplete_value": true,
      "site": "00556d50",
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
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00556d50",
      "incomplete_value": true,
      "site": "00556d50",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00556ef0",
      "incomplete_value": true,
      "site": "00556ef0",
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
                "const:56d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00556ef0",
      "incomplete_value": true,
      "site": "00556ef0",
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
                "const:4e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00556ef8",
      "incomplete_value": true,
      "site": "00556ef8",
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
      "definition_site": "00556ef8",
      "incomplete_value": true,
      "site": "00556ef8",
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
    "ordinal": 42,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00556ccc",
      "READ",
      [
        "storage",
        "00c26280",
        null,
        "undefined8"
      ]
    ],
    [
      "00556d30",
      "DATA",
      [
        "storage",
        "00c26280",
        null,
        "undefined8"
      ]
    ],
    [
      "00556d40",
      "WRITE",
      [
        "storage",
        "00c26280",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00556ccc",
      "READ",
      [
        "storage",
        "00c26340",
        null,
        "undefined8"
      ]
    ],
    [
      "00556d30",
      "DATA",
      [
        "storage",
        "00c26340",
        null,
        "undefined8"
      ]
    ],
    [
      "00556d40",
      "WRITE",
      [
        "storage",
        "00c26340",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00556d50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00556/00556bf4.md#insn-00556d50) · [`00556cc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00556/00556bf4.md#insn-00556cc4) · [`00556d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00556/00556bf4.md#insn-00556d44)
- 新版 `00556d50`（命令位置の公開資料なし） · `00556cc4`（命令位置の公開資料なし） · `00556d44`（命令位置の公開資料なし）

~~~diff
- 00556d50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:278:8"]]
- 00556d50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00556d50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:338:8"]]
+ 00556d50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00556d50 bytes 093d01f9
+ 00556d50 bytes 099d01f9
- 00556cc4 ["COPY", "tmp:0:8", ["const:280:8"]]
- 00556cc4 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 00556cc4 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 00556cc4 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 00556cc4 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 00556cc4 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 00556cc4 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 00556cc4 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 00556cc4 bytes 18030a91
+ 00556cc4 bytes 18030d91
- 00556d44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:278:8"]]
- 00556d44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00556d44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:338:8"]]
+ 00556d44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00556d44 bytes 093d41f9
+ 00556d44 bytes 099d41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3a9e92a6769d260b0346170d9f7b100"></a>

### [`00557264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557264.md) → [`00557264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557264.md) FUN_00557264

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005572c8",
      "incomplete_value": true,
      "site": "005572c8",
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
                "const:547:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005572c8",
      "incomplete_value": true,
      "site": "005572c8",
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
                "const:54e:8"
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
      "definition_site": "005572cc",
      "incomplete_value": true,
      "site": "005572cc",
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
      "definition_site": "005572cc",
      "incomplete_value": true,
      "site": "005572cc",
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
      "005572b8",
      "READ",
      [
        "storage",
        "002a354e",
        null,
        "string"
      ]
    ],
    [
      "005572c0",
      "READ",
      [
        "storage",
        "002a3553",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005572b8",
      "READ",
      [
        "storage",
        "002a3547",
        null,
        "string"
      ]
    ],
    [
      "005572c0",
      "READ",
      [
        "storage",
        "002a354c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005572b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557264.md#insn-005572b4)
- 新版 `005572b4`（命令位置の公開資料なし）

~~~diff
- 005572b4 ["COPY", "tmp:0:8", ["const:54e:8"]]
- 005572b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005572b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005572b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005572b4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 005572b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005572b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005572b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005572b4 bytes 29391591
+ 005572b4 bytes 291d1591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f45b7ac78d5603dee7e8189f60c9aa76"></a>

### [`005574b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/005574b4.md) → [`005574b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/005574b4.md) FUN_005574b4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00557508",
      "incomplete_value": true,
      "site": "00557508",
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
                "const:74f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00557508",
      "incomplete_value": true,
      "site": "00557508",
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
                "const:758:8"
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
      "definition_site": "0055750c",
      "incomplete_value": true,
      "site": "0055750c",
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
      "definition_site": "0055750c",
      "incomplete_value": true,
      "site": "0055750c",
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
      "005574f8",
      "READ",
      [
        "storage",
        "002a9758",
        null,
        "string"
      ]
    ],
    [
      "00557500",
      "READ",
      [
        "storage",
        "002a975e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005574f8",
      "READ",
      [
        "storage",
        "002a974f",
        null,
        "string"
      ]
    ],
    [
      "00557500",
      "READ",
      [
        "storage",
        "002a9755",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005574f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/005574b4.md#insn-005574f4)
- 新版 `005574f4`（命令位置の公開資料なし）

~~~diff
- 005574f4 ["COPY", "tmp:0:8", ["const:758:8"]]
- 005574f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005574f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005574f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005574f4 ["COPY", "tmp:0:8", ["const:74f:8"]]
+ 005574f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005574f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005574f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005574f4 bytes 29611d91
+ 005574f4 bytes 293d1d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0800527c194753c26a65e6e095c4be1b"></a>

### [`005575ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/005575ec.md) → [`005575ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/005575ec.md) FUN_005575ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00557640",
      "incomplete_value": true,
      "site": "00557640",
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
                "const:890:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00557640",
      "incomplete_value": true,
      "site": "00557640",
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
                "const:897:8"
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
      "definition_site": "00557644",
      "incomplete_value": true,
      "site": "00557644",
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
      "definition_site": "00557644",
      "incomplete_value": true,
      "site": "00557644",
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
      "00557630",
      "READ",
      [
        "storage",
        "002a6897",
        null,
        "string"
      ]
    ],
    [
      "00557638",
      "READ",
      [
        "storage",
        "002a689d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00557630",
      "READ",
      [
        "storage",
        "002a6890",
        null,
        "string"
      ]
    ],
    [
      "00557638",
      "READ",
      [
        "storage",
        "002a6896",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055762c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/005575ec.md#insn-0055762c)
- 新版 `0055762c`（命令位置の公開資料なし）

~~~diff
- 0055762c ["COPY", "tmp:0:8", ["const:897:8"]]
- 0055762c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055762c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055762c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055762c ["COPY", "tmp:0:8", ["const:890:8"]]
+ 0055762c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055762c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055762c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055762c bytes 295d2291
+ 0055762c bytes 29412291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-222a934b5290e85d50289dc574f92355"></a>

### [`00557724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557724.md) → [`00557724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557724.md) FUN_00557724

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00559458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559458.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00559458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559458.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.18% / 新版 97.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055775c",
      "incomplete_value": false,
      "site": "00557770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055775c",
      "incomplete_value": false,
      "site": "00557770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00557764",
      "incomplete_value": false,
      "site": "00557770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00557764",
      "incomplete_value": false,
      "site": "00557770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "0055775c",
      "PARAM",
      [
        "storage",
        "00beecc8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00557764",
      "PARAM",
      [
        "storage",
        "00beece0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0055775c",
      "PARAM",
      [
        "storage",
        "00beed78",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00557764",
      "PARAM",
      [
        "storage",
        "00beed90",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055775c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557724.md#insn-0055775c) · [`00557764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557724.md#insn-00557764)
- 新版 `0055775c`（命令位置の公開資料なし） · `00557764`（命令位置の公開資料なし）

~~~diff
- 0055775c ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 0055775c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0055775c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0055775c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0055775c ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 0055775c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0055775c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0055775c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0055775c bytes 21203391
+ 0055775c bytes 21e03591
- 00557764 ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 00557764 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00557764 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00557764 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00557764 ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 00557764 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00557764 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00557764 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00557764 bytes 42803391
+ 00557764 bytes 42403691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95d0045567d3b89082420bee01f4123d"></a>

### [`00557864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557864.md) → [`00557864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557864.md) FUN_00557864

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052db34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db34.md) · 呼出先 8件 [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566978.md)
- 新版 呼出元 1件 [`0052db34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db34.md) · 呼出先 8件 [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.35% / 新版 90.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005578e0",
      "incomplete_value": true,
      "site": "005578e0",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:768:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005578e0",
      "incomplete_value": true,
      "site": "005578e0",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:762:8"
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
      "definition_site": "00557904",
      "incomplete_value": true,
      "site": "00557904",
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
                "const:6e1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00557904",
      "incomplete_value": true,
      "site": "00557904",
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
                "const:654:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005579c4",
      "incomplete_value": false,
      "site": "005579cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005579c4",
      "incomplete_value": false,
      "site": "005579cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:e60:8"
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
      "005578d4",
      "READ",
      [
        "storage",
        "002aa762",
        null,
        "string"
      ]
    ],
    [
      "00557900",
      "READ",
      [
        "storage",
        "002a1654",
        null,
        "string"
      ]
    ],
    [
      "005579cc",
      "DATA",
      [
        "storage",
        "00beee60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005578d4",
      "READ",
      [
        "storage",
        "002aa768",
        null,
        "string"
      ]
    ],
    [
      "00557900",
      "READ",
      [
        "storage",
        "002a16e1",
        null,
        "string"
      ]
    ],
    [
      "005579cc",
      "DATA",
      [
        "storage",
        "00beef10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005578d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557864.md#insn-005578d0) · [`005578fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557864.md#insn-005578fc) · [`005579c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557864.md#insn-005579c4)
- 新版 `005578d0`（命令位置の公開資料なし） · `005578fc`（命令位置の公開資料なし） · `005579c4`（命令位置の公開資料なし）

~~~diff
- 005578d0 ["COPY", "tmp:0:8", ["const:762:8"]]
- 005578d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005578d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005578d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005578d0 ["COPY", "tmp:0:8", ["const:768:8"]]
+ 005578d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005578d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005578d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005578d0 bytes 08891d91
+ 005578d0 bytes 08a11d91
- 005578fc ["COPY", "tmp:0:8", ["const:654:8"]]
- 005578fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005578fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005578fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005578fc ["COPY", "tmp:0:8", ["const:6e1:8"]]
+ 005578fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005578fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005578fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005578fc bytes 08511991
+ 005578fc bytes 08851b91
- 005579c4 ["COPY", "tmp:0:8", ["const:e60:8"]]
- 005579c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005579c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005579c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005579c4 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 005579c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005579c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005579c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005579c4 bytes 08813991
+ 005579c4 bytes 08413c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f0cb15e9d3499aa52c6c7f1877db77e"></a>

### [`00557a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557a90.md) → [`00557a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557a90.md) FUN_00557a90

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 73.68% / 新版 73.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00557aac",
      "incomplete_value": false,
      "site": "00557ab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00557aac",
      "incomplete_value": false,
      "site": "00557ab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "definition_site": "00557ac8",
      "incomplete_value": false,
      "site": "00557ac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00557ac8",
      "incomplete_value": false,
      "site": "00557ac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:c18:8"
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
      "00557ab4",
      "DATA",
      [
        "storage",
        "00beeeb0",
        null,
        "undefined *"
      ]
    ],
    [
      "00557ac8",
      "DATA",
      [
        "storage",
        "00beec18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00557ab4",
      "DATA",
      [
        "storage",
        "00beef60",
        null,
        "undefined *"
      ]
    ],
    [
      "00557ac8",
      "DATA",
      [
        "storage",
        "00beecc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00557aac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557a90.md#insn-00557aac) · [`00557ab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557a90.md#insn-00557ab8)
- 新版 `00557aac`（命令位置の公開資料なし） · `00557ab8`（命令位置の公開資料なし）

~~~diff
- 00557aac ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 00557aac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00557aac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00557aac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00557aac ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00557aac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00557aac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00557aac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00557aac bytes 08c13a91
+ 00557aac bytes 08813d91
- 00557ab8 ["COPY", "register:4040:8", ["const:bee000:8"]]
- 00557ab8 bytes a83400f0
+ 00557ab8 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 00557ab8 bytes a83400f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dbaad3e7accfc0664fc700d83f2a5d2"></a>

### [`00557adc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557adc.md) → [`00557adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557adc.md) FUN_00557adc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00558fd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558fd0.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00558fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558fd0.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00557b54",
      "incomplete_value": true,
      "site": "00557b68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c3f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00557b54",
      "incomplete_value": true,
      "site": "00557b68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bb2:8"
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
      "definition_site": "00557b6c",
      "incomplete_value": true,
      "site": "00557b6c",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00557b6c",
      "incomplete_value": true,
      "site": "00557b6c",
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
                "const:e:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00557c60",
      "incomplete_value": true,
      "site": "00557c60",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00557c60",
      "incomplete_value": true,
      "site": "00557c60",
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
            "const:2e0:8"
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
      "00557b54",
      "READ",
      [
        "storage",
        "00296bb2",
        null,
        "string"
      ]
    ],
    [
      "00557b64",
      "READ",
      [
        "storage",
        "00296bc0",
        null,
        "string"
      ]
    ],
    [
      "00557be8",
      "READ",
      [
        "storage",
        "00c262e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00557b54",
      "READ",
      [
        "storage",
        "00296c3f",
        null,
        "string"
      ]
    ],
    [
      "00557b64",
      "READ",
      [
        "storage",
        "00296c4d",
        null,
        "string"
      ]
    ],
    [
      "00557be8",
      "READ",
      [
        "storage",
        "00c263a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00557c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557adc.md#insn-00557c60) · [`00557b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557adc.md#insn-00557b48) · [`00557be0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557adc.md#insn-00557be0)
- 新版 `00557c60`（命令位置の公開資料なし） · `00557b48`（命令位置の公開資料なし） · `00557be0`（命令位置の公開資料なし）

~~~diff
- 00557c60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
- 00557c60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00557c60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a0:8"]]
+ 00557c60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00557c60 bytes 097101f9
+ 00557c60 bytes 09d101f9
- 00557b48 ["COPY", "tmp:0:8", ["const:bb2:8"]]
- 00557b48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00557b48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00557b48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00557b48 ["COPY", "tmp:0:8", ["const:c3f:8"]]
+ 00557b48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00557b48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00557b48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00557b48 bytes 29c92e91
+ 00557b48 bytes 29fd3091
- 00557be0 ["COPY", "tmp:0:8", ["const:2e8:8"]]
- 00557be0 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00557be0 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00557be0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00557be0 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 00557be0 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00557be0 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00557be0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00557be0 bytes b5a20b91
+ 00557be0 bytes b5a20e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12b169f50ea07fa6485c262282e1818c"></a>

### [`00557d8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557d8c.md) → [`00557d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557d8c.md) FUN_00557d8c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00557dec",
      "incomplete_value": true,
      "site": "00557dec",
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
                "const:cce:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00557dec",
      "incomplete_value": true,
      "site": "00557dec",
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
                "const:c41:8"
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
      "definition_site": "00557e68",
      "incomplete_value": true,
      "site": "00557e68",
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
      "definition_site": "00557e68",
      "incomplete_value": true,
      "site": "00557e68",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00557ddc",
      "READ",
      [
        "storage",
        "00297c41",
        null,
        "string"
      ]
    ],
    [
      "00557e64",
      "READ",
      [
        "storage",
        "00c262d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00557ec0",
      "READ",
      [
        "storage",
        "00c26320",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00557ddc",
      "READ",
      [
        "storage",
        "00297cce",
        null,
        "string"
      ]
    ],
    [
      "00557e64",
      "READ",
      [
        "storage",
        "00c26390",
        null,
        "undefined8"
      ]
    ],
    [
      "00557ec0",
      "READ",
      [
        "storage",
        "00c263e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00557dd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557d8c.md#insn-00557dd0) · [`00557e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557d8c.md#insn-00557e60) · [`00557e74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557d8c.md#insn-00557e74)
- 新版 `00557dd0`（命令位置の公開資料なし） · `00557e60`（命令位置の公開資料なし） · `00557e74`（命令位置の公開資料なし）

~~~diff
- 00557dd0 ["COPY", "tmp:0:8", ["const:c41:8"]]
- 00557dd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00557dd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00557dd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00557dd0 ["COPY", "tmp:0:8", ["const:cce:8"]]
+ 00557dd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00557dd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00557dd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00557dd0 bytes 29053191
+ 00557dd0 bytes 29393391
- 00557e60 ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 00557e60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00557e60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00557e60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00557e60 ["COPY", "tmp:0:8", ["const:390:8"]]
+ 00557e60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00557e60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00557e60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00557e60 bytes 08410b91
+ 00557e60 bytes 08410e91
- 00557e74 ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 00557e74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00557e74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00557e74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00557e74 ["COPY", "tmp:0:8", ["const:390:8"]]
+ 00557e74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00557e74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00557e74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00557e74 bytes 29410b91
+ 00557e74 bytes 29410e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed52f26a69edde6a0eaea2c554d08462"></a>

### [`00557f84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557f84.md) → [`00557f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557f84.md) FUN_00557f84

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)

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
      "definition_site": "00557fe0",
      "incomplete_value": true,
      "site": "00557fe0",
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
                "const:89f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00557fe0",
      "incomplete_value": true,
      "site": "00557fe0",
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
                "const:8a6:8"
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
      "00557fc8",
      "READ",
      [
        "storage",
        "002a68a6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00557fc8",
      "READ",
      [
        "storage",
        "002a689f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00557fbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557f84.md#insn-00557fbc)
- 新版 `00557fbc`（命令位置の公開資料なし）

~~~diff
- 00557fbc ["COPY", "tmp:0:8", ["const:8a6:8"]]
- 00557fbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00557fbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00557fbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00557fbc ["COPY", "tmp:0:8", ["const:89f:8"]]
+ 00557fbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00557fbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00557fbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00557fbc bytes 29992291
+ 00557fbc bytes 297d2291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96e868dd9c32fb6ff08f078031357a6c"></a>

### [`005580a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/005580a4.md) → [`005580a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/005580a4.md) FUN_005580a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052db3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db3c.md) · 呼出先 11件 [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566978.md)
- 新版 呼出元 1件 [`0052db3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db3c.md) · 呼出先 11件 [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.20% / 新版 90.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00558110",
      "incomplete_value": true,
      "site": "00558118",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9d1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00558110",
      "incomplete_value": true,
      "site": "00558118",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:944:8"
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
      "definition_site": "0055811c",
      "incomplete_value": true,
      "site": "0055811c",
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
      "definition_site": "0055811c",
      "incomplete_value": true,
      "site": "0055811c",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005581dc",
      "incomplete_value": false,
      "site": "005581e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005581dc",
      "incomplete_value": false,
      "site": "005581e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:f00:8"
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
      "00558110",
      "READ",
      [
        "storage",
        "00292944",
        null,
        "string"
      ]
    ],
    [
      "00558114",
      "READ",
      [
        "storage",
        "00292951",
        null,
        "string"
      ]
    ],
    [
      "005581e4",
      "DATA",
      [
        "storage",
        "00beef00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00558110",
      "READ",
      [
        "storage",
        "002929d1",
        null,
        "string"
      ]
    ],
    [
      "00558114",
      "READ",
      [
        "storage",
        "002929de",
        null,
        "string"
      ]
    ],
    [
      "005581e4",
      "DATA",
      [
        "storage",
        "00beefb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055810c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/005580a4.md#insn-0055810c) · [`005581dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/005580a4.md#insn-005581dc) · [`005581e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/005580a4.md#insn-005581e8)
- 新版 `0055810c`（命令位置の公開資料なし） · `005581dc`（命令位置の公開資料なし）

~~~diff
- 0055810c ["COPY", "tmp:0:8", ["const:944:8"]]
- 0055810c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055810c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055810c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055810c ["COPY", "tmp:0:8", ["const:9d1:8"]]
+ 0055810c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055810c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055810c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055810c bytes 29112591
+ 0055810c bytes 29452791
- 005581dc ["COPY", "tmp:0:8", ["const:f00:8"]]
- 005581dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005581dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005581dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005581dc ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 005581dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005581dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005581dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005581dc bytes 08013c91
+ 005581dc bytes 08c13e91
- 005581e8 ["COPY", "register:4040:8", ["const:bee000:8"]]
- 005581e8 bytes a83400d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e99d3b449007c260ae32e76ddf135054"></a>

### [`0055828c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/0055828c.md) → [`0055828c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/0055828c.md) FUN_0055828c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052db38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db38.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`0055977c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/0055977c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md)
- 新版 呼出元 1件 [`0052db38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db38.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`0055977c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/0055977c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 92.38% / 新版 92.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005584b4",
      "incomplete_value": true,
      "site": "005584b4",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005584b4",
      "incomplete_value": true,
      "site": "005584b4",
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
            "const:2c8:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00558570",
      "incomplete_value": false,
      "site": "00558578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00558570",
      "incomplete_value": false,
      "site": "00558578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00558588",
      "incomplete_value": false,
      "site": "00558588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00558588",
      "incomplete_value": false,
      "site": "00558588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "0055830c",
      "READ",
      [
        "storage",
        "00299d60",
        null,
        "string"
      ]
    ],
    [
      "0055830c",
      "READ",
      [
        "storage",
        "00299d70",
        null,
        "string"
      ]
    ],
    [
      "00558314",
      "READ",
      [
        "storage",
        "00299d80",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055830c",
      "READ",
      [
        "storage",
        "00299ded",
        null,
        "string"
      ]
    ],
    [
      "0055830c",
      "READ",
      [
        "storage",
        "00299dfd",
        null,
        "string"
      ]
    ],
    [
      "00558314",
      "READ",
      [
        "storage",
        "00299e0d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005584b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/0055828c.md#insn-005584b4) · [`00558304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/0055828c.md#insn-00558304) · [`00558308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/0055828c.md#insn-00558308)
- 新版 `005584b4`（命令位置の公開資料なし） · `00558304`（命令位置の公開資料なし）

~~~diff
- 005584b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2c8:8"]]
- 005584b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 005584b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:388:8"]]
+ 005584b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 005584b4 bytes 096501f9
+ 005584b4 bytes 09c501f9
- 00558304 ["COPY", "tmp:0:8", ["const:d60:8"]]
- 00558304 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00558304 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00558304 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00558304 ["COPY", "tmp:0:8", ["const:ded:8"]]
+ 00558304 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00558304 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00558304 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00558304 bytes 08813591
+ 00558304 bytes 08b53791
- 00558308 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00558308 bytes c9eaffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-671fbaebe818d2d79da08fa55854b1ee"></a>

### [`00558640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558640.md) → [`00558640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558640.md) Java_jp_co_ponos_battlecats_MyActivity_onAlertClick

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00471738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471738.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00471738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471738.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 92.56% / 新版 92.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005587b0",
      "incomplete_value": true,
      "site": "005587b0",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005587b0",
      "incomplete_value": true,
      "site": "005587b0",
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
            "const:2e0:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0055866c",
      "incomplete_value": true,
      "site": "0055866c",
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
      "definition_site": "0055866c",
      "incomplete_value": true,
      "site": "0055866c",
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
      "definition_site": "005587ac",
      "incomplete_value": true,
      "site": "005587ac",
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
      "definition_site": "005587ac",
      "incomplete_value": true,
      "site": "005587ac",
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
    "ordinal": 20,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00558668",
      "READ",
      [
        "storage",
        "00c262d0",
        null,
        "undefined8"
      ]
    ],
    [
      "005586b0",
      "READ",
      [
        "storage",
        "00c26320",
        null,
        "undefined8"
      ]
    ],
    [
      "005586e4",
      "READ",
      [
        "storage",
        "00c262e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00558668",
      "READ",
      [
        "storage",
        "00c26390",
        null,
        "undefined8"
      ]
    ],
    [
      "005586b0",
      "READ",
      [
        "storage",
        "00c263e0",
        null,
        "undefined8"
      ]
    ],
    [
      "005586e4",
      "READ",
      [
        "storage",
        "00c263a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005587b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558640.md#insn-005587b0) · [`00558664`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558640.md#insn-00558664) · [`00558674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558640.md#insn-00558674)
- 新版 `005587b0`（命令位置の公開資料なし） · `00558664`（命令位置の公開資料なし） · `00558674`（命令位置の公開資料なし）

~~~diff
- 005587b0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2e0:8"]]
- 005587b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 005587b0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3a0:8"]]
+ 005587b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005587b0 bytes 287101f9
+ 005587b0 bytes 28d101f9
- 00558664 ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 00558664 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00558664 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00558664 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00558664 ["COPY", "tmp:0:8", ["const:390:8"]]
+ 00558664 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00558664 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00558664 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00558664 bytes 08410b91
+ 00558664 bytes 08410e91
- 00558674 ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 00558674 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00558674 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00558674 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00558674 ["COPY", "tmp:0:8", ["const:390:8"]]
+ 00558674 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00558674 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00558674 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00558674 bytes 29410b91
+ 00558674 bytes 29410e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1441b97317ffc70b1164553370725b97"></a>

### [`00558824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558824.md) → [`00558824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558824.md) Java_jp_co_ponos_battlecats_MyActivity_onButtonClick

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00558830",
      "incomplete_value": true,
      "site": "00558830",
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
      "definition_site": "00558830",
      "incomplete_value": true,
      "site": "00558830",
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
      "0055882c",
      "READ",
      [
        "storage",
        "00c262b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00558884",
      "READ",
      [
        "storage",
        "00c262e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0055882c",
      "READ",
      [
        "storage",
        "00c26378",
        null,
        "undefined8"
      ]
    ],
    [
      "00558884",
      "READ",
      [
        "storage",
        "00c263a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00558828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558824.md#insn-00558828) · [`00558838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558824.md#insn-00558838)
- 新版 `00558828`（命令位置の公開資料なし） · `00558838`（命令位置の公開資料なし）

~~~diff
- 00558828 ["COPY", "tmp:0:8", ["const:2b8:8"]]
- 00558828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00558828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00558828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00558828 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 00558828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00558828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00558828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00558828 bytes 08e10a91
+ 00558828 bytes 08e10d91
- 00558838 ["COPY", "tmp:0:8", ["const:2b8:8"]]
- 00558838 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00558838 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00558838 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00558838 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 00558838 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00558838 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00558838 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00558838 bytes 29e10a91
+ 00558838 bytes 29e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca3466f78979f81dc3ec3a25c49f6400"></a>

### [`005588a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/005588a0.md) → [`005588a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/005588a0.md) Java_jp_co_ponos_battlecats_MyActivity_onWebViewFilter

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566a7c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 92.54% / 新版 92.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005588c8",
      "incomplete_value": true,
      "site": "005588c8",
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
      "definition_site": "005588c8",
      "incomplete_value": true,
      "site": "005588c8",
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
      "005588c4",
      "READ",
      [
        "storage",
        "00c26280",
        null,
        "undefined8"
      ]
    ],
    [
      "0055891c",
      "READ",
      [
        "storage",
        "00c26300",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005588c4",
      "READ",
      [
        "storage",
        "00c26340",
        null,
        "undefined8"
      ]
    ],
    [
      "0055891c",
      "READ",
      [
        "storage",
        "00c263c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005588c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/005588a0.md#insn-005588c0) · [`005588d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/005588a0.md#insn-005588d0)
- 新版 `005588c0`（命令位置の公開資料なし） · `005588d0`（命令位置の公開資料なし）

~~~diff
- 005588c0 ["COPY", "tmp:0:8", ["const:280:8"]]
- 005588c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005588c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005588c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005588c0 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 005588c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005588c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005588c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005588c0 bytes 08010a91
+ 005588c0 bytes 08010d91
- 005588d0 ["COPY", "tmp:0:8", ["const:280:8"]]
- 005588d0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005588d0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005588d0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005588d0 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 005588d0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005588d0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005588d0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005588d0 bytes 73020a91
+ 005588d0 bytes 73020d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-362e7b222917293c073f3c6fd7d4f7ac"></a>

### [`005589d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/005589d8.md) → [`005589d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/005589d8.md) Java_jp_co_ponos_battlecats_MyActivity_onWebViewResult

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566a7c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 92.54% / 新版 92.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00558a08",
      "incomplete_value": true,
      "site": "00558a08",
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
      "definition_site": "00558a08",
      "incomplete_value": true,
      "site": "00558a08",
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
      "00558a04",
      "READ",
      [
        "storage",
        "00c26280",
        null,
        "undefined8"
      ]
    ],
    [
      "00558a5c",
      "READ",
      [
        "storage",
        "00c262d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00558a04",
      "READ",
      [
        "storage",
        "00c26340",
        null,
        "undefined8"
      ]
    ],
    [
      "00558a5c",
      "READ",
      [
        "storage",
        "00c26390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00558a00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/005589d8.md#insn-00558a00) · [`00558a10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/005589d8.md#insn-00558a10)
- 新版 `00558a00`（命令位置の公開資料なし） · `00558a10`（命令位置の公開資料なし）

~~~diff
- 00558a00 ["COPY", "tmp:0:8", ["const:280:8"]]
- 00558a00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00558a00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00558a00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00558a00 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 00558a00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00558a00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00558a00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00558a00 bytes 08010a91
+ 00558a00 bytes 08010d91
- 00558a10 ["COPY", "tmp:0:8", ["const:280:8"]]
- 00558a10 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00558a10 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00558a10 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00558a10 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 00558a10 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00558a10 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00558a10 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00558a10 bytes b5020a91
+ 00558a10 bytes b5020d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

