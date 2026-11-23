# v15.7.2 → v15.7.3 · 最優先の変更候補 (35)

[一覧の目次](README.md)

<a id="compare-b70516482b9703861303de12650b3faf"></a>

### [`007735b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/007735b0.md) → [`007735b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007735b0.md) FUN_007735b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
            "const:970:8"
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
            "const:8c0:8"
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
        "00bfc8c0",
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
        "00bfc970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007735d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/007735b0.md#insn-007735d0)
- 新版 `007735d0`（命令位置の公開資料なし）

~~~diff
- 007735d0 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 007735d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007735d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007735d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007735d0 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 007735d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007735d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007735d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007735d0 bytes 08012391
+ 007735d0 bytes 08c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62345e5bd9942f114f3097101662ff69"></a>

### [`007735e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/007735e4.md) → [`007735e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007735e4.md) FUN_007735e4

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
            "const:970:8"
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
            "const:8c0:8"
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
        "00bfc8c0",
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
        "00bfc970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007735ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/007735e4.md#insn-007735ec)
- 新版 `007735ec`（命令位置の公開資料なし）

~~~diff
- 007735ec ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 007735ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007735ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007735ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007735ec ["COPY", "tmp:0:8", ["const:970:8"]]
+ 007735ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007735ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007735ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007735ec bytes 29012391
+ 007735ec bytes 29c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ff0e0c8b5f5804ee2b0b0515e8d8d11"></a>

### [`00773634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/00773634.md) → [`00773634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773634.md) FUN_00773634

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
            "const:a00:8"
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
            "const:950:8"
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
        "00bfc950",
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
        "00bfca00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00773654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/00773634.md#insn-00773654)
- 新版 `00773654`（命令位置の公開資料なし）

~~~diff
- 00773654 ["COPY", "tmp:0:8", ["const:950:8"]]
- 00773654 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00773654 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00773654 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00773654 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00773654 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00773654 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00773654 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00773654 bytes 08412591
+ 00773654 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6574c4c15889d878a39bd5de88e2498"></a>

### [`00773668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/00773668.md) → [`00773668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773668.md) FUN_00773668

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
      "definition_site": "00773674",
      "incomplete_value": false,
      "site": "00773674",
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
    "old": {
      "definition_site": "00773674",
      "incomplete_value": false,
      "site": "00773674",
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
            "const:950:8"
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
      "00773674",
      "DATA",
      [
        "storage",
        "00bfc950",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00773674",
      "DATA",
      [
        "storage",
        "00bfca00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00773670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/00773668.md#insn-00773670)
- 新版 `00773670`（命令位置の公開資料なし）

~~~diff
- 00773670 ["COPY", "tmp:0:8", ["const:950:8"]]
- 00773670 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00773670 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00773670 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00773670 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00773670 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00773670 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00773670 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00773670 bytes 29412591
+ 00773670 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f6d9d6239d2f26cd69f132f24317fb4"></a>

### [`0077372c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/0077372c.md) → [`0077372c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/0077372c.md) FUN_0077372c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00773750",
      "incomplete_value": false,
      "site": "00773750",
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
    "old": {
      "definition_site": "00773750",
      "incomplete_value": false,
      "site": "00773750",
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
            "const:9d0:8"
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
      "00773750",
      "DATA",
      [
        "storage",
        "00bfc9d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00773750",
      "DATA",
      [
        "storage",
        "00bfca80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077374c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/0077372c.md#insn-0077374c)
- 新版 `0077374c`（命令位置の公開資料なし）

~~~diff
- 0077374c ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 0077374c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0077374c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0077374c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0077374c ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 0077374c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0077374c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0077374c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0077374c bytes 08412791
+ 0077374c bytes 08012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2393e88f41f5c4cd6f33910305d14ab"></a>

### [`00773760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/00773760.md) → [`00773760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773760.md) FUN_00773760

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
      "definition_site": "0077376c",
      "incomplete_value": false,
      "site": "0077376c",
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
    "old": {
      "definition_site": "0077376c",
      "incomplete_value": false,
      "site": "0077376c",
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
            "const:9d0:8"
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
      "0077376c",
      "DATA",
      [
        "storage",
        "00bfc9d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0077376c",
      "DATA",
      [
        "storage",
        "00bfca80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00773768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/00773760.md#insn-00773768)
- 新版 `00773768`（命令位置の公開資料なし）

~~~diff
- 00773768 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 00773768 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00773768 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00773768 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00773768 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 00773768 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00773768 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00773768 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00773768 bytes 29412791
+ 00773768 bytes 29012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-743f187c755357b58685546c483040ee"></a>

### [`007737b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/007737b0.md) → [`007737b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007737b0.md) FUN_007737b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007737d4",
      "incomplete_value": false,
      "site": "007737d4",
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
    "old": {
      "definition_site": "007737d4",
      "incomplete_value": false,
      "site": "007737d4",
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
            "const:a60:8"
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
      "007737d4",
      "DATA",
      [
        "storage",
        "00bfca60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007737d4",
      "DATA",
      [
        "storage",
        "00bfcb10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007737d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/007737b0.md#insn-007737d0)
- 新版 `007737d0`（命令位置の公開資料なし）

~~~diff
- 007737d0 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 007737d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007737d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007737d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007737d0 ["COPY", "tmp:0:8", ["const:b10:8"]]
+ 007737d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007737d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007737d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007737d0 bytes 08812991
+ 007737d0 bytes 08412c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc581d5723f129cdcce774178b88c9c6"></a>

### [`007737e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/007737e4.md) → [`007737e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007737e4.md) FUN_007737e4

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
      "definition_site": "007737f0",
      "incomplete_value": false,
      "site": "007737f0",
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
    "old": {
      "definition_site": "007737f0",
      "incomplete_value": false,
      "site": "007737f0",
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
            "const:a60:8"
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
      "007737f0",
      "DATA",
      [
        "storage",
        "00bfca60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007737f0",
      "DATA",
      [
        "storage",
        "00bfcb10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007737ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/007737e4.md#insn-007737ec)
- 新版 `007737ec`（命令位置の公開資料なし）

~~~diff
- 007737ec ["COPY", "tmp:0:8", ["const:a60:8"]]
- 007737ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007737ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007737ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007737ec ["COPY", "tmp:0:8", ["const:b10:8"]]
+ 007737ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007737ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007737ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007737ec bytes 29812991
+ 007737ec bytes 29412c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5c7f3002363de4db23e7278af1897ea"></a>

### [`007738a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/007738a0.md) → [`007738a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007738a0.md) FUN_007738a0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007718f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00771/007718f4.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592ccc.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`007718f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00771/007718f4.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

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
      "definition_site": "007738d8",
      "incomplete_value": false,
      "site": "007738e0",
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
    "old": {
      "definition_site": "007738d8",
      "incomplete_value": false,
      "site": "007738e0",
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
      "007738e0",
      "DATA",
      [
        "storage",
        "00bf3098",
        null,
        "pointer"
      ]
    ],
    [
      "00773998",
      "READ",
      [
        "storage",
        "00bf30a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007738e0",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00773998",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007738d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/007738a0.md#insn-007738d8) · [`007738dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/007738a0.md#insn-007738dc)
- 新版 `007738d8`（命令位置の公開資料なし） · `007738dc`（命令位置の公開資料なし）

~~~diff
- 007738d8 ["COPY", "tmp:0:8", ["const:98:8"]]
- 007738d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007738d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007738d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007738d8 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 007738d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007738d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007738d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007738d8 bytes 08610291
+ 007738d8 bytes 08210591
- 007738dc ["COPY", "register:4098:8", ["register:4000:8"]]
- 007738dc bytes f30300aa
+ 007738dc ["COPY", "register:4098:8", ["register:4000:8"]]
+ 007738dc bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c9a1bc8c97809ed2d34cb934ce95b9a"></a>

### [`00773aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/00773aa8.md) → [`00773aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773aa8.md) FUN_00773aa8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00773ac0",
      "incomplete_value": false,
      "site": "00773ad0",
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
    "old": {
      "definition_site": "00773ac0",
      "incomplete_value": false,
      "site": "00773ad0",
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
            "const:ae0:8"
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
      "00773ad0",
      "DATA",
      [
        "storage",
        "00bfcae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00773ad0",
      "DATA",
      [
        "storage",
        "00bfcb90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00773ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/00773aa8.md#insn-00773ac0)
- 新版 `00773ac0`（命令位置の公開資料なし）

~~~diff
- 00773ac0 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00773ac0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00773ac0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00773ac0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00773ac0 ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 00773ac0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00773ac0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00773ac0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00773ac0 bytes 08812b91
+ 00773ac0 bytes 08412e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c82a2722ebf552770c3ee78ac193180c"></a>

### [`00773b34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/00773b34.md) → [`00773b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773b34.md) FUN_00773b34

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00773b64",
      "incomplete_value": false,
      "site": "00773b64",
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
    "old": {
      "definition_site": "00773b64",
      "incomplete_value": false,
      "site": "00773b64",
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
            "const:ae0:8"
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
      "00773b64",
      "DATA",
      [
        "storage",
        "00bfcae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00773b64",
      "DATA",
      [
        "storage",
        "00bfcb90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00773b5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/00773b34.md#insn-00773b5c)
- 新版 `00773b5c`（命令位置の公開資料なし）

~~~diff
- 00773b5c ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00773b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00773b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00773b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00773b5c ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 00773b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00773b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00773b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00773b5c bytes 08812b91
+ 00773b5c bytes 08412e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e27b6cb3e05d8a06b7f49b03b9af8a0"></a>

### [`00773c3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/00773c3c.md) → [`00773c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773c3c.md) FUN_00773c3c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00773c64",
      "incomplete_value": false,
      "site": "00773c64",
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
    "old": {
      "definition_site": "00773c64",
      "incomplete_value": false,
      "site": "00773c64",
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
            "const:ae0:8"
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
      "00773c64",
      "DATA",
      [
        "storage",
        "00bfcae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00773c64",
      "DATA",
      [
        "storage",
        "00bfcb90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00773c5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/00773c3c.md#insn-00773c5c) · [`00773c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00773/00773c3c.md#insn-00773c60)
- 新版 `00773c5c`（命令位置の公開資料なし） · `00773c60`（命令位置の公開資料なし）

~~~diff
- 00773c5c ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00773c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00773c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00773c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00773c5c ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 00773c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00773c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00773c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00773c5c bytes 08812b91
+ 00773c5c bytes 08412e91
- 00773c60 ["COPY", "register:40a0:8", ["register:4008:8"]]
- 00773c60 bytes f40301aa
+ 00773c60 ["COPY", "register:40a0:8", ["register:4008:8"]]
+ 00773c60 bytes f40301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed2cb9b982c8f70a9dfa00bc52f75ec2"></a>

### [`00774024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774024.md) → [`00774024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774024.md) FUN_00774024

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0077403c",
      "incomplete_value": false,
      "site": "00774048",
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
    "old": {
      "definition_site": "0077403c",
      "incomplete_value": false,
      "site": "00774048",
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
      "00774048",
      "DATA",
      [
        "storage",
        "00bfcb60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774048",
      "DATA",
      [
        "storage",
        "00bfcc10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077403c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774024.md#insn-0077403c)
- 新版 `0077403c`（命令位置の公開資料なし）

~~~diff
- 0077403c ["COPY", "tmp:0:8", ["const:b60:8"]]
- 0077403c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0077403c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0077403c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0077403c ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 0077403c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0077403c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0077403c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0077403c bytes 08812d91
+ 0077403c bytes 08413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-478a62cbd35953ed80622feba350258a"></a>

### [`00774080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774080.md) → [`00774080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774080.md) FUN_00774080

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007740ac",
      "incomplete_value": false,
      "site": "007740ac",
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
    "old": {
      "definition_site": "007740ac",
      "incomplete_value": false,
      "site": "007740ac",
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
      "007740ac",
      "DATA",
      [
        "storage",
        "00bfcb60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007740ac",
      "DATA",
      [
        "storage",
        "00bfcc10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007740a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774080.md#insn-007740a4)
- 新版 `007740a4`（命令位置の公開資料なし）

~~~diff
- 007740a4 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 007740a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007740a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007740a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007740a4 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 007740a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007740a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007740a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007740a4 bytes 08812d91
+ 007740a4 bytes 08413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e825a136e7dfc0ecafb516c65d0521c"></a>

### [`00774108`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774108.md) → [`00774108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774108.md) FUN_00774108

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
      "definition_site": "00774124",
      "incomplete_value": false,
      "site": "00774124",
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
    "old": {
      "definition_site": "00774124",
      "incomplete_value": false,
      "site": "00774124",
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
      "00774124",
      "DATA",
      [
        "storage",
        "00bfcb60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774124",
      "DATA",
      [
        "storage",
        "00bfcc10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774108.md#insn-00774120)
- 新版 `00774120`（命令位置の公開資料なし）

~~~diff
- 00774120 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 00774120 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00774120 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00774120 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00774120 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 00774120 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00774120 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00774120 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00774120 bytes 29812d91
+ 00774120 bytes 29413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-821d85f174620176fa7dc016600bdedf"></a>

### [`007743c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/007743c4.md) → [`007743c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/007743c4.md) FUN_007743c4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "007743dc",
      "incomplete_value": false,
      "site": "007743ec",
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
    "old": {
      "definition_site": "007743dc",
      "incomplete_value": false,
      "site": "007743ec",
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
      "007743ec",
      "DATA",
      [
        "storage",
        "00bfcbe0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007743ec",
      "DATA",
      [
        "storage",
        "00bfcc90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007743dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/007743c4.md#insn-007743dc)
- 新版 `007743dc`（命令位置の公開資料なし）

~~~diff
- 007743dc ["COPY", "tmp:0:8", ["const:be0:8"]]
- 007743dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007743dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007743dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007743dc ["COPY", "tmp:0:8", ["const:c90:8"]]
+ 007743dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007743dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007743dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007743dc bytes 08812f91
+ 007743dc bytes 08413291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14700764735bd822b526c3658100881d"></a>

### [`00774454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774454.md) → [`00774454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774454.md) FUN_00774454

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0077446c",
      "incomplete_value": false,
      "site": "0077447c",
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
    "old": {
      "definition_site": "0077446c",
      "incomplete_value": false,
      "site": "0077447c",
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
      "0077447c",
      "DATA",
      [
        "storage",
        "00bfcbe0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0077447c",
      "DATA",
      [
        "storage",
        "00bfcc90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077446c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774454.md#insn-0077446c)
- 新版 `0077446c`（命令位置の公開資料なし）

~~~diff
- 0077446c ["COPY", "tmp:0:8", ["const:be0:8"]]
- 0077446c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0077446c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0077446c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0077446c ["COPY", "tmp:0:8", ["const:c90:8"]]
+ 0077446c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0077446c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0077446c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0077446c bytes 08812f91
+ 0077446c bytes 08413291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-575a15a849c36b36000c89c4ab82d1a9"></a>

### [`007744e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/007744e0.md) → [`007744e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/007744e0.md) FUN_007744e0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00774510",
      "incomplete_value": false,
      "site": "00774510",
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
    "old": {
      "definition_site": "00774510",
      "incomplete_value": false,
      "site": "00774510",
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
      "00774510",
      "DATA",
      [
        "storage",
        "00bfcbe0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774510",
      "DATA",
      [
        "storage",
        "00bfcc90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774508`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/007744e0.md#insn-00774508)
- 新版 `00774508`（命令位置の公開資料なし）

~~~diff
- 00774508 ["COPY", "tmp:0:8", ["const:be0:8"]]
- 00774508 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00774508 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00774508 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00774508 ["COPY", "tmp:0:8", ["const:c90:8"]]
+ 00774508 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00774508 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00774508 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00774508 bytes 08812f91
+ 00774508 bytes 08413291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e04c39808a3cf25a70f707a7e65a12c2"></a>

### [`007745e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/007745e8.md) → [`007745e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/007745e8.md) FUN_007745e8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00774610",
      "incomplete_value": false,
      "site": "00774610",
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
    "old": {
      "definition_site": "00774610",
      "incomplete_value": false,
      "site": "00774610",
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
      "00774610",
      "DATA",
      [
        "storage",
        "00bfcbe0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774610",
      "DATA",
      [
        "storage",
        "00bfcc90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/007745e8.md#insn-00774608) · [`0077460c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/007745e8.md#insn-0077460c)
- 新版 `00774608`（命令位置の公開資料なし） · `0077460c`（命令位置の公開資料なし）

~~~diff
- 00774608 ["COPY", "tmp:0:8", ["const:be0:8"]]
- 00774608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00774608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00774608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00774608 ["COPY", "tmp:0:8", ["const:c90:8"]]
+ 00774608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00774608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00774608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00774608 bytes 08812f91
+ 00774608 bytes 08413291
- 0077460c ["COPY", "register:40a0:8", ["register:4008:8"]]
- 0077460c bytes f40301aa
+ 0077460c ["COPY", "register:40a0:8", ["register:4008:8"]]
+ 0077460c bytes f40301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12a58cf5416f1cddf5514bf4094edd74"></a>

### [`007749b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/007749b8.md) → [`007749b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/007749b8.md) FUN_007749b8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "007749d0",
      "incomplete_value": false,
      "site": "007749dc",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007749d0",
      "incomplete_value": false,
      "site": "007749dc",
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
      "007749dc",
      "DATA",
      [
        "storage",
        "00bfcc60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007749dc",
      "DATA",
      [
        "storage",
        "00bfcd10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007749d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/007749b8.md#insn-007749d0)
- 新版 `007749d0`（命令位置の公開資料なし）

~~~diff
- 007749d0 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 007749d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007749d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007749d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007749d0 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 007749d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007749d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007749d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007749d0 bytes 08813191
+ 007749d0 bytes 08413491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81613eea0d2dff9b4455e706a4e04803"></a>

### [`00774a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774a14.md) → [`00774a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774a14.md) FUN_00774a14

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00774a40",
      "incomplete_value": false,
      "site": "00774a40",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00774a40",
      "incomplete_value": false,
      "site": "00774a40",
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
      "00774a40",
      "DATA",
      [
        "storage",
        "00bfcc60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774a40",
      "DATA",
      [
        "storage",
        "00bfcd10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774a38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774a14.md#insn-00774a38)
- 新版 `00774a38`（命令位置の公開資料なし）

~~~diff
- 00774a38 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 00774a38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00774a38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00774a38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00774a38 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 00774a38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00774a38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00774a38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00774a38 bytes 08813191
+ 00774a38 bytes 08413491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-550ce65a2c52b722b1ece5208a121a9b"></a>

### [`00774a9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774a9c.md) → [`00774a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774a9c.md) FUN_00774a9c

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
      "definition_site": "00774ab8",
      "incomplete_value": false,
      "site": "00774ab8",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00774ab8",
      "incomplete_value": false,
      "site": "00774ab8",
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
      "00774ab8",
      "DATA",
      [
        "storage",
        "00bfcc60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774ab8",
      "DATA",
      [
        "storage",
        "00bfcd10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774ab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774a9c.md#insn-00774ab4)
- 新版 `00774ab4`（命令位置の公開資料なし）

~~~diff
- 00774ab4 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 00774ab4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00774ab4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00774ab4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00774ab4 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 00774ab4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00774ab4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00774ab4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00774ab4 bytes 29813191
+ 00774ab4 bytes 29413491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c7e8464b96c80ff36a9126a3e6825df"></a>

### [`00774be0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774be0.md) → [`00774be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774be0.md) FUN_00774be0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00770eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00770/00770eb8.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592ccc.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`00770eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/00770eb8.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00774c18",
      "incomplete_value": true,
      "site": "00774c20",
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
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00774c18",
      "incomplete_value": true,
      "site": "00774c20",
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
            "const:98:8"
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
      "00774c20",
      "DATA",
      [
        "storage",
        "00bf3098",
        null,
        "pointer"
      ]
    ],
    [
      "00774cd8",
      "READ",
      [
        "storage",
        "00bf30a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774c20",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00774cd8",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774be0.md#insn-00774c18) · [`00774c1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774be0.md#insn-00774c1c)
- 新版 `00774c18`（命令位置の公開資料なし） · `00774c1c`（命令位置の公開資料なし）

~~~diff
- 00774c18 ["COPY", "tmp:0:8", ["const:98:8"]]
- 00774c18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00774c18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00774c18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00774c18 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 00774c18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00774c18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00774c18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00774c18 bytes 08610291
+ 00774c18 bytes 08210591
- 00774c1c ["COPY", "register:4098:8", ["register:4000:8"]]
- 00774c1c bytes f30300aa
+ 00774c1c ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00774c1c bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81ddf9a6d54dcc3d35b914cc18229437"></a>

### [`00774d58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774d58.md) → [`00774d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774d58.md) FUN_00774d58

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00774d70",
      "incomplete_value": false,
      "site": "00774d80",
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
    "old": {
      "definition_site": "00774d70",
      "incomplete_value": false,
      "site": "00774d80",
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
      "00774d80",
      "DATA",
      [
        "storage",
        "00bfcce0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774d80",
      "DATA",
      [
        "storage",
        "00bfcd90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774d70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774d58.md#insn-00774d70)
- 新版 `00774d70`（命令位置の公開資料なし）

~~~diff
- 00774d70 ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 00774d70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00774d70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00774d70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00774d70 ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 00774d70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00774d70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00774d70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00774d70 bytes 08813391
+ 00774d70 bytes 08413691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7334dc95a60ef6da25f0452845464548"></a>

### [`00774de8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774de8.md) → [`00774de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774de8.md) FUN_00774de8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00774e00",
      "incomplete_value": false,
      "site": "00774e10",
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
    "old": {
      "definition_site": "00774e00",
      "incomplete_value": false,
      "site": "00774e10",
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
      "00774e10",
      "DATA",
      [
        "storage",
        "00bfcce0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774e10",
      "DATA",
      [
        "storage",
        "00bfcd90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774de8.md#insn-00774e00)
- 新版 `00774e00`（命令位置の公開資料なし）

~~~diff
- 00774e00 ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 00774e00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00774e00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00774e00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00774e00 ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 00774e00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00774e00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00774e00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00774e00 bytes 08813391
+ 00774e00 bytes 08413691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c19c4fdf346756b759cfb37be9f0fc4"></a>

### [`00774e74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774e74.md) → [`00774e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774e74.md) FUN_00774e74

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00774ea4",
      "incomplete_value": false,
      "site": "00774ea4",
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
    "old": {
      "definition_site": "00774ea4",
      "incomplete_value": false,
      "site": "00774ea4",
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
      "00774ea4",
      "DATA",
      [
        "storage",
        "00bfcce0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774ea4",
      "DATA",
      [
        "storage",
        "00bfcd90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774e74.md#insn-00774e9c)
- 新版 `00774e9c`（命令位置の公開資料なし）

~~~diff
- 00774e9c ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 00774e9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00774e9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00774e9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00774e9c ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 00774e9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00774e9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00774e9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00774e9c bytes 08813391
+ 00774e9c bytes 08413691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d162e1faf918761591691627583aae8"></a>

### [`00774f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774f7c.md) → [`00774f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774f7c.md) FUN_00774f7c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00774fa4",
      "incomplete_value": false,
      "site": "00774fa4",
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
    "old": {
      "definition_site": "00774fa4",
      "incomplete_value": false,
      "site": "00774fa4",
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
      "00774fa4",
      "DATA",
      [
        "storage",
        "00bfcce0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774fa4",
      "DATA",
      [
        "storage",
        "00bfcd90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774f7c.md#insn-00774f9c) · [`00774fa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00774/00774f7c.md#insn-00774fa0)
- 新版 `00774f9c`（命令位置の公開資料なし） · `00774fa0`（命令位置の公開資料なし）

~~~diff
- 00774f9c ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 00774f9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00774f9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00774f9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00774f9c ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 00774f9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00774f9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00774f9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00774f9c bytes 08813391
+ 00774f9c bytes 08413691
- 00774fa0 ["COPY", "register:40a0:8", ["register:4008:8"]]
- 00774fa0 bytes f40301aa
+ 00774fa0 ["COPY", "register:40a0:8", ["register:4008:8"]]
+ 00774fa0 bytes f40301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70152239631c6f1c2f842931cf2aef57"></a>

### [`00775320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00775/00775320.md) → [`00775320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/00775320.md) FUN_00775320

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
      "definition_site": "0077532c",
      "incomplete_value": false,
      "site": "00775338",
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
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077532c",
      "incomplete_value": false,
      "site": "00775338",
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
            "const:d60:8"
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
      "00775338",
      "DATA",
      [
        "storage",
        "00bfcd60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00775338",
      "DATA",
      [
        "storage",
        "00bfce10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077532c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00775/00775320.md#insn-0077532c)
- 新版 `0077532c`（命令位置の公開資料なし）

~~~diff
- 0077532c ["COPY", "tmp:0:8", ["const:d60:8"]]
- 0077532c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0077532c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0077532c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0077532c ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 0077532c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0077532c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0077532c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0077532c bytes 4a813591
+ 0077532c bytes 4a413891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa51ca8cf1e0bf322b8803dcf3dd4cd9"></a>

### [`00775364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00775/00775364.md) → [`00775364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/00775364.md) FUN_00775364

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0077537c",
      "incomplete_value": false,
      "site": "00775388",
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
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077537c",
      "incomplete_value": false,
      "site": "00775388",
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
            "const:d60:8"
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
      "00775388",
      "DATA",
      [
        "storage",
        "00bfcd60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00775388",
      "DATA",
      [
        "storage",
        "00bfce10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077537c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00775/00775364.md#insn-0077537c)
- 新版 `0077537c`（命令位置の公開資料なし）

~~~diff
- 0077537c ["COPY", "tmp:0:8", ["const:d60:8"]]
- 0077537c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0077537c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0077537c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0077537c ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 0077537c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0077537c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0077537c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0077537c bytes 08813591
+ 0077537c bytes 08413891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46fa543a7c2fa30a88f1a4ef4cab0add"></a>

### [`007753c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00775/007753c0.md) → [`007753c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/007753c0.md) FUN_007753c0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007753ec",
      "incomplete_value": false,
      "site": "007753ec",
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
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007753ec",
      "incomplete_value": false,
      "site": "007753ec",
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
            "const:d60:8"
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
      "007753ec",
      "DATA",
      [
        "storage",
        "00bfcd60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007753ec",
      "DATA",
      [
        "storage",
        "00bfce10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007753e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00775/007753c0.md#insn-007753e4)
- 新版 `007753e4`（命令位置の公開資料なし）

~~~diff
- 007753e4 ["COPY", "tmp:0:8", ["const:d60:8"]]
- 007753e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007753e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007753e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007753e4 ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 007753e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007753e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007753e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007753e4 bytes 08813591
+ 007753e4 bytes 08413891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6472018fb48e25601c68b26315dbb98"></a>

### [`00775448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00775/00775448.md) → [`00775448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/00775448.md) FUN_00775448

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
      "definition_site": "00775464",
      "incomplete_value": false,
      "site": "00775464",
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
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00775464",
      "incomplete_value": false,
      "site": "00775464",
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
            "const:d60:8"
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
      "00775464",
      "DATA",
      [
        "storage",
        "00bfcd60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00775464",
      "DATA",
      [
        "storage",
        "00bfce10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00775460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00775/00775448.md#insn-00775460)
- 新版 `00775460`（命令位置の公開資料なし）

~~~diff
- 00775460 ["COPY", "tmp:0:8", ["const:d60:8"]]
- 00775460 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00775460 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00775460 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00775460 ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 00775460 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00775460 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00775460 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00775460 bytes 29813591
+ 00775460 bytes 29413891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5a806d6216a4ba2abd402967cd62995"></a>

### [`0077558c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00775/0077558c.md) → [`0077558c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/0077558c.md) _INIT_139

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
      "definition_site": "007755c8",
      "incomplete_value": true,
      "site": "007755e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "007755c8",
      "incomplete_value": true,
      "site": "007755e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2e4:8"
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
      "definition_site": "00775648",
      "incomplete_value": true,
      "site": "00775664",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:36e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00775648",
      "incomplete_value": true,
      "site": "00775664",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:2e1:8"
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
      "definition_site": "007757b4",
      "incomplete_value": false,
      "site": "007757c0",
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
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007757b4",
      "incomplete_value": false,
      "site": "007757c0",
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
            "const:f38:8"
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
      "007755c8",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "007755ec",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0077560c",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007755c8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "007755ec",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0077560c",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007755b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00775/0077558c.md#insn-007755b8) · [`007755c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00775/0077558c.md#insn-007755c0)
- 新版 `007755b8`（命令位置の公開資料なし） · `007755c0`（命令位置の公開資料なし）

~~~diff
- 007755b8 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 007755b8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 007755b8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 007755b8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 007755b8 ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 007755b8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 007755b8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 007755b8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 007755b8 bytes 73e23c91
+ 007755b8 bytes 73e23f91
- 007755c0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 007755c0 bytes 89d9ffd0
+ 007755c0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 007755c0 bytes 89d9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-403228f1b3fa34fb2ebcd78deee03aa4"></a>

### [`0077759c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00777/0077759c.md) → [`0077759c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00777/0077759c.md) FUN_0077759c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007773bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00777/007773bc.md) [`00777730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00777/00777730.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`007773bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00777/007773bc.md) [`00777730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00777/00777730.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "007775a8",
      "incomplete_value": false,
      "site": "007775ac",
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
      "definition_site": "007775a8",
      "incomplete_value": false,
      "site": "007775ac",
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
      "007775a8",
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
      "007775a8",
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

- 旧版 [`007775a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00777/0077759c.md#insn-007775a8)
- 新版 `007775a8`（命令位置の公開資料なし）

~~~diff
- 007775a8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007775a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007775a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007775a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007775a8 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 007775a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007775a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007775a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007775a8 bytes 00280c91
+ 007775a8 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f38e08e2ae3154d20f34df4daa51d453"></a>

### [`0077fed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0077f/0077fed4.md) → [`0077fed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0077f/0077fed4.md) _INIT_140

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
      "definition_site": "0077ff10",
      "incomplete_value": true,
      "site": "0077ff2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0077ff10",
      "incomplete_value": true,
      "site": "0077ff2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2e4:8"
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
      "definition_site": "0077ff34",
      "incomplete_value": true,
      "site": "0077ff50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0077ff34",
      "incomplete_value": true,
      "site": "0077ff50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f7:8"
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
      "definition_site": "0077ff54",
      "incomplete_value": true,
      "site": "0077ff70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0077ff54",
      "incomplete_value": true,
      "site": "0077ff70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da:8"
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
      "0077ff10",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0077ff34",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0077ff54",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0077ff10",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0077ff34",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0077ff54",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077fefc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0077f/0077fed4.md#insn-0077fefc) · [`0077ff00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0077f/0077fed4.md#insn-0077ff00) · [`0077ff08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0077f/0077fed4.md#insn-0077ff08)
- 新版 `0077fefc`（命令位置の公開資料なし） · `0077ff00`（命令位置の公開資料なし）

~~~diff
- 0077fefc ["COPY", "register:4098:8", ["const:c27000:8"]]
+ 0077fefc ["COPY", "register:4098:8", ["const:c28000:8"]]
- 0077fefc bytes 53250090
+ 0077fefc bytes 532500b0
- 0077ff00 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 0077ff00 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0077ff00 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0077ff00 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0077ff00 ["COPY", "tmp:0:8", ["const:10:8"]]
+ 0077ff00 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0077ff00 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0077ff00 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0077ff00 bytes 73423d91
+ 0077ff00 bytes 73420091
- 0077ff08 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0077ff08 bytes 49d9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-273b0fa151e53e47fb5836fd4f833d8c"></a>

### [`007802c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00780/007802c0.md) → [`007802c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00780/007802c0.md) FUN_007802c0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078c/0078cd14.md) · 呼出先 51件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00424bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0044b660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b660.md)
- 新版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) · 呼出先 51件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00424bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044b660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b660.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.67% / 新版 87.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 335件, `store_destination` 119件, `store_value` 193件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00780300",
      "incomplete_value": false,
      "site": "00780308",
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
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00780300",
      "incomplete_value": false,
      "site": "00780308",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007804ec",
      "incomplete_value": true,
      "site": "007804ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "007804ec",
      "incomplete_value": true,
      "site": "007804ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:89c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 49,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00780508",
      "incomplete_value": true,
      "site": "00780508",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7ff:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00780508",
      "incomplete_value": true,
      "site": "00780508",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:772:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00780308",
      "DATA",
      [
        "storage",
        "00bfcde0",
        null,
        "pointer"
      ]
    ],
    [
      "007804b4",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "007804d8",
      "READ",
      [
        "storage",
        "002a589c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00780308",
      "DATA",
      [
        "storage",
        "00bfce90",
        null,
        "pointer"
      ]
    ],
    [
      "007804b4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "007804d8",
      "READ",
      [
        "storage",
        "002a5895",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00780300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/assembly/00780/007802c0-007802c0-0078acd8.md#insn-00780300) · [`007804ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/assembly/00780/007802c0-007802c0-0078acd8.md#insn-007804ac) · [`007804b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/assembly/00780/007802c0-007802c0-0078acd8.md#insn-007804b0)
- 新版 `00780300`（命令位置の公開資料なし） · `007804ac`（命令位置の公開資料なし） · `007804b0`（命令位置の公開資料なし）

~~~diff
- 00780300 ["COPY", "tmp:0:8", ["const:de0:8"]]
- 00780300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00780300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00780300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00780300 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00780300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00780300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00780300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00780300 bytes 08813791
+ 00780300 bytes 08413a91
- 007804ac ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 007804ac ["COPY", "register:4040:8", ["const:c25000:8"]]
- 007804ac bytes 28250090
+ 007804ac bytes 282500b0
- 007804b0 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 007804b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007804b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007804b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007804b0 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 007804b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007804b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007804b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007804b0 bytes 08e13d91
+ 007804b0 bytes 08e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16ff0265ac0085506fdf9ea3f08be560"></a>

### [`0078b0ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078b/0078b0ec.md) → [`0078b0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078b/0078b0ec.md) FUN_0078b0ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007802c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00780/007802c0.md) · 呼出先 30件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0044b8ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b8ec.md) [`0044b9cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b9cc.md) [`0044ba98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044ba98.md)
- 新版 呼出元 1件 [`007802c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00780/007802c0.md) · 呼出先 30件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044b8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8ec.md) [`0044b9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b9cc.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.26% / 新版 97.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0078bf58",
      "incomplete_value": true,
      "site": "0078bf70",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:da4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078bf58",
      "incomplete_value": true,
      "site": "0078bf70",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:e38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 316,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0078bfb4",
      "incomplete_value": true,
      "site": "0078bfc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:271:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078bfb4",
      "incomplete_value": true,
      "site": "0078bfc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1e4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 321,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0078bfcc",
      "incomplete_value": true,
      "site": "0078bfcc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0078bfcc",
      "incomplete_value": true,
      "site": "0078bfcc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 322,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0078bf44",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "0078bf58",
      "READ",
      [
        "storage",
        "002ade38",
        null,
        "string"
      ]
    ],
    [
      "0078bfb4",
      "READ",
      [
        "storage",
        "002991e4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0078bf44",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "0078bf58",
      "READ",
      [
        "storage",
        "002adda4",
        null,
        "string"
      ]
    ],
    [
      "0078bfb4",
      "READ",
      [
        "storage",
        "00299271",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078bf3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078b/0078b0ec.md#insn-0078bf3c) · [`0078bf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078b/0078b0ec.md#insn-0078bf40) · [`0078bf54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078b/0078b0ec.md#insn-0078bf54)
- 新版 `0078bf3c`（命令位置の公開資料なし） · `0078bf40`（命令位置の公開資料なし） · `0078bf54`（命令位置の公開資料なし）

~~~diff
- 0078bf3c ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0078bf3c ["COPY", "register:4040:8", ["const:c25000:8"]]
- 0078bf3c bytes c82400b0
+ 0078bf3c bytes c82400d0
- 0078bf40 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 0078bf40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078bf40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078bf40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078bf40 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0078bf40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078bf40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078bf40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078bf40 bytes 08e13d91
+ 0078bf40 bytes 08e10091
- 0078bf54 ["COPY", "tmp:0:8", ["const:e38:8"]]
- 0078bf54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0078bf54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0078bf54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0078bf54 ["COPY", "tmp:0:8", ["const:da4:8"]]
+ 0078bf54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0078bf54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0078bf54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0078bf54 bytes 29e13891
+ 0078bf54 bytes 29913691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f307b8b8314a1346bb43fcd69a3ef39"></a>

### [`0078cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078c/0078cd14.md) → [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) FUN_0078cd14

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 209件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041be0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c8f8.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 209件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.38% / 新版 97.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 30件, `store_destination` 19件, `store_value` 55件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0078d948",
      "incomplete_value": true,
      "site": "0078d958",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0078d948",
      "incomplete_value": true,
      "site": "0078d958",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:135:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 115,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0078e704",
      "incomplete_value": false,
      "site": "0078e704",
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
    "old": {
      "definition_site": "0078e704",
      "incomplete_value": false,
      "site": "0078e704",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "ordinal": 222,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0078e6fc",
      "incomplete_value": true,
      "site": "0078e704",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0078e6fc",
      "incomplete_value": true,
      "site": "0078e704",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 222,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0078d948",
      "READ",
      [
        "storage",
        "002a8135",
        null,
        "string"
      ]
    ],
    [
      "0078e3e8",
      "READ",
      [
        "storage",
        "00c1adb0",
        null,
        "pointer"
      ]
    ],
    [
      "0078e424",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0078d948",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ],
    [
      "0078e3e8",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "0078e424",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/assembly/0078c/0078cd14-0078cd14-007963a8.md#insn-0078e704) · [`0078e708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/assembly/0078c/0078cd14-0078cd14-007963a8.md#insn-0078e708) · [`0078e720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/assembly/0078c/0078cd14-0078cd14-007963a8.md#insn-0078e720)
- 新版 `0078e704`（命令位置の公開資料なし） · `0078e708`（命令位置の公開資料なし） · `0078e720`（命令位置の公開資料なし）

~~~diff
- 0078e704 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a8:8"]]
- 0078e704 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0078e704 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
+ 0078e704 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0078e704 bytes 09d504f9
+ 0078e704 bytes 093505f9
- 0078e708 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b8:8"]]
- 0078e708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 0078e708 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a78:8"]]
+ 0078e708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 0078e708 bytes 6ade04f9
+ 0078e708 bytes 6a3e05f9
- 0078e720 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b8:8"]]
- 0078e720 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
+ 0078e720 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a78:8"]]
+ 0078e720 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0078e720 bytes 75de04f9
+ 0078e720 bytes 753e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ceca7a0c1abeb04c28ad7f54a124bee0"></a>

### [`00796acc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00796/00796acc.md) → [`00796acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00796/00796acc.md) FUN_00796acc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078c/0078cd14.md) [`00abf464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00abf/00abf464.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00464a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`004652a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/004652a0.md)
- 新版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`004652a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/004652a0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.20% / 新版 90.20%

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
      "definition_site": "00796b04",
      "incomplete_value": false,
      "site": "00796b10",
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
    "old": {
      "definition_site": "00796b04",
      "incomplete_value": false,
      "site": "00796b10",
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
            "const:c78:8"
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
      "definition_site": "00796b18",
      "incomplete_value": true,
      "site": "00796b28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f9e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00796b18",
      "incomplete_value": true,
      "site": "00796b28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00796c8c",
      "incomplete_value": true,
      "site": "00796c90",
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
      "definition_site": "00796c8c",
      "incomplete_value": true,
      "site": "00796c90",
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
      "00796b10",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "00796b18",
      "READ",
      [
        "storage",
        "00296f11",
        null,
        "string"
      ]
    ],
    [
      "00796c7c",
      "READ",
      [
        "storage",
        "00c1acc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00796b10",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00796b18",
      "READ",
      [
        "storage",
        "00296f9e",
        null,
        "string"
      ]
    ],
    [
      "00796c7c",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00796b04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00796/00796acc.md#insn-00796b04) · [`00796b08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00796/00796acc.md#insn-00796b08)
- 新版 `00796b04`（命令位置の公開資料なし） · `00796b08`（命令位置の公開資料なし）

~~~diff
- 00796b04 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00796b04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00796b04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00796b04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00796b04 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00796b04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00796b04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00796b04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00796b04 bytes 08e13191
+ 00796b04 bytes 08a13491
- 00796b08 ["COPY", "register:4048:8", ["const:296000:8"]]
- 00796b08 bytes 09d8ff90
+ 00796b08 ["COPY", "register:4048:8", ["const:296000:8"]]
+ 00796b08 bytes 09d8ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20f347652db04cb2f5010e0fbaba42d7"></a>

### [`00796f18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00796/00796f18.md) → [`00796f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00796/00796f18.md) FUN_00796f18

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078c/0078cd14.md) [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) · 呼出先 24件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`006f2f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006f2/006f2f8c.md)
- 新版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 24件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`006f2f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f2/006f2f8c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.36% / 新版 93.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 25件, `store_destination` 14件, `store_value` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00797a08",
      "incomplete_value": false,
      "site": "00797a08",
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
    "old": {
      "definition_site": "00797a08",
      "incomplete_value": false,
      "site": "00797a08",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
    "ordinal": 89,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00797a0c",
      "incomplete_value": false,
      "site": "00797a0c",
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
    "old": {
      "definition_site": "00797a0c",
      "incomplete_value": false,
      "site": "00797a0c",
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
            "const:f40:8"
          ]
        ]
      ]
    },
    "ordinal": 90,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00797a08",
      "incomplete_value": false,
      "site": "00797a0c",
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
    "old": {
      "definition_site": "00797a08",
      "incomplete_value": false,
      "site": "00797a0c",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
    "ordinal": 90,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00796f60",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00796f74",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00796f7c",
      "PARAM",
      [
        "storage",
        "00bf4468",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00796f60",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00796f74",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00796f7c",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00796f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00796/00796f18.md#insn-00796f60) · [`00796f74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00796/00796f18.md#insn-00796f74) · [`00796f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00796/00796f18.md#insn-00796f7c)
- 新版 `00796f60`（命令位置の公開資料なし） · `00796f74`（命令位置の公開資料なし） · `00796f7c`（命令位置の公開資料なし）

~~~diff
- 00796f60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00796f60 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00796f60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00796f60 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00796f60 bytes 00dd44f9
+ 00796f60 bytes 003d45f9
- 00796f74 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00796f74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00796f74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00796f74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00796f74 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00796f74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00796f74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00796f74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00796f74 bytes 21603691
+ 00796f74 bytes 21203991
- 00796f7c ["COPY", "tmp:0:8", ["const:468:8"]]
- 00796f7c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00796f7c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00796f7c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00796f7c ["COPY", "tmp:0:8", ["const:518:8"]]
+ 00796f7c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00796f7c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00796f7c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00796f7c bytes 42a01191
+ 00796f7c bytes 42601491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c042b61517d2cf33b14bb03e7b10a0aa"></a>

### [`00797bfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00797/00797bfc.md) → [`00797bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00797/00797bfc.md) FUN_00797bfc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078c/0078cd14.md) [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) · 呼出先 24件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00467c68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467c68.md) [`00467c70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467c70.md)
- 新版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 24件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00467c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467c68.md) [`00467c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467c70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.01% / 新版 86.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_destination` 14件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00797f40",
      "incomplete_value": false,
      "site": "00797f40",
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
    "old": {
      "definition_site": "00797f40",
      "incomplete_value": false,
      "site": "00797f40",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00797f44",
      "incomplete_value": false,
      "site": "00797f44",
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
    "old": {
      "definition_site": "00797f44",
      "incomplete_value": false,
      "site": "00797f44",
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
            "const:f40:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00797f40",
      "incomplete_value": false,
      "site": "00797f44",
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
    "old": {
      "definition_site": "00797f40",
      "incomplete_value": false,
      "site": "00797f44",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00797cc4",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "00797cf4",
      "PARAM",
      [
        "storage",
        "00c24f40",
        null,
        "undefined8"
      ]
    ],
    [
      "00797cf8",
      "READ",
      [
        "storage",
        "00c1adb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00797cc4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00797cf4",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "00797cf8",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00797cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00797/00797bfc.md#insn-00797cb8) · [`00797cbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00797/00797bfc.md#insn-00797cbc) · [`00797cf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00797/00797bfc.md#insn-00797cf0)
- 新版 `00797cb8`（命令位置の公開資料なし） · `00797cbc`（命令位置の公開資料なし） · `00797cf0`（命令位置の公開資料なし）

~~~diff
- 00797cb8 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 00797cb8 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 00797cb8 bytes 682400b0
+ 00797cb8 bytes 682400d0
- 00797cbc ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00797cbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00797cbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00797cbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00797cbc ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00797cbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00797cbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00797cbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00797cbc bytes 08e13d91
+ 00797cbc bytes 08e10091
- 00797cf0 ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 00797cf0 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 00797cf0 bytes 602400b0
+ 00797cf0 bytes 602400d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a3d60aa1002ff10c5cf726d978cf350"></a>

### [`00798020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00798/00798020.md) → [`00798020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00798/00798020.md) FUN_00798020

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078c/0078cd14.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`007cbf54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbf54.md)
- 新版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`007cbf54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbf54.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.19% / 新版 98.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007983b4",
      "incomplete_value": false,
      "site": "007983b4",
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
    "old": {
      "definition_site": "007983b4",
      "incomplete_value": false,
      "site": "007983b4",
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
            "const:ef8:8"
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00798068",
      "incomplete_value": true,
      "site": "00798068",
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
      "definition_site": "00798068",
      "incomplete_value": true,
      "site": "00798068",
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
      "definition_site": "00798070",
      "incomplete_value": false,
      "site": "00798080",
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
    "old": {
      "definition_site": "00798070",
      "incomplete_value": false,
      "site": "00798080",
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
            "const:d98:8"
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
      "0079805c",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00798070",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00798078",
      "PARAM",
      [
        "storage",
        "00bf4468",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0079805c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00798070",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00798078",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079805c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00798/00798020.md#insn-0079805c) · [`00798070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00798/00798020.md#insn-00798070) · [`00798078`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00798/00798020.md#insn-00798078)
- 新版 `0079805c`（命令位置の公開資料なし） · `00798070`（命令位置の公開資料なし） · `00798078`（命令位置の公開資料なし）

~~~diff
- 0079805c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 0079805c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0079805c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 0079805c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0079805c bytes 00dd44f9
+ 0079805c bytes 003d45f9
- 00798070 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00798070 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00798070 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00798070 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00798070 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00798070 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00798070 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00798070 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00798070 bytes 21603691
+ 00798070 bytes 21203991
- 00798078 ["COPY", "tmp:0:8", ["const:468:8"]]
- 00798078 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00798078 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00798078 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00798078 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 00798078 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00798078 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00798078 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00798078 bytes 42a01191
+ 00798078 bytes 42601491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c47b26b20a42a14f285c82f48faea9e1"></a>

### [`00798650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00798/00798650.md) → [`00798650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00798/00798650.md) FUN_00798650

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078c/0078cd14.md) [`007bdafc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bd/007bdafc.md) · 呼出先 30件 [`0044ab84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044ab84.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00467074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`007bdafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bdafc.md) · 呼出先 30件 [`0044ab84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ab84.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.02% / 新版 92.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 2件, `store_value` 8件

アドレスに依存する影響 `branch_value` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00798914",
      "incomplete_value": true,
      "site": "00798914",
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
      "definition_site": "00798914",
      "incomplete_value": true,
      "site": "00798914",
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
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0079893c",
      "incomplete_value": true,
      "site": "00798940",
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
      "definition_site": "0079893c",
      "incomplete_value": true,
      "site": "00798940",
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
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00798980",
      "incomplete_value": true,
      "site": "00798980",
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
      "definition_site": "00798980",
      "incomplete_value": true,
      "site": "00798980",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007986a0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007986ac",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007986b4",
      "PARAM",
      [
        "storage",
        "00bf4468",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007986a0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007986ac",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007986b4",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007986a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00798/00798650.md#insn-007986a0) · [`007986ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00798/00798650.md#insn-007986ac) · [`007986b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00798/00798650.md#insn-007986b4)
- 新版 `007986a0`（命令位置の公開資料なし） · `007986ac`（命令位置の公開資料なし） · `007986b4`（命令位置の公開資料なし）

~~~diff
- 007986a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 007986a0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007986a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007986a0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007986a0 bytes 00dd44f9
+ 007986a0 bytes 003d45f9
- 007986ac ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007986ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007986ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007986ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007986ac ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007986ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007986ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007986ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007986ac bytes 21603691
+ 007986ac bytes 21203991
- 007986b4 ["COPY", "tmp:0:8", ["const:468:8"]]
- 007986b4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007986b4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007986b4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007986b4 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 007986b4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007986b4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007986b4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007986b4 bytes 42a01191
+ 007986b4 bytes 42601491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-597b1eaacf2e83e4b24e4fa846ff94c3"></a>

### [`00798f70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00798/00798f70.md) → [`00798f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00798/00798f70.md) FUN_00798f70

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078c/0078cd14.md) [`007bdafc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bd/007bdafc.md) · 呼出先 22件 [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00467074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md)
- 新版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`007bdafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bdafc.md) · 呼出先 22件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.98% / 新版 91.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 7件, `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00799218",
      "incomplete_value": true,
      "site": "00799218",
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
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00799218",
      "incomplete_value": true,
      "site": "00799218",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00799358",
      "incomplete_value": false,
      "site": "00799358",
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
    "old": {
      "definition_site": "00799358",
      "incomplete_value": false,
      "site": "00799358",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
    "ordinal": 33,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0079935c",
      "incomplete_value": false,
      "site": "0079935c",
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
    "old": {
      "definition_site": "0079935c",
      "incomplete_value": false,
      "site": "0079935c",
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
            "const:f40:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00798fb0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00798fbc",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00798fc4",
      "PARAM",
      [
        "storage",
        "00bf4468",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00798fb0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00798fbc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00798fc4",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00798fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00798/00798f70.md#insn-00798fb0) · [`00798fbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00798/00798f70.md#insn-00798fbc) · [`00798fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00798/00798f70.md#insn-00798fc4)
- 新版 `00798fb0`（命令位置の公開資料なし） · `00798fbc`（命令位置の公開資料なし） · `00798fc4`（命令位置の公開資料なし）

~~~diff
- 00798fb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00798fb0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00798fb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00798fb0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00798fb0 bytes 00dd44f9
+ 00798fb0 bytes 003d45f9
- 00798fbc ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00798fbc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00798fbc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00798fbc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00798fbc ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00798fbc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00798fbc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00798fbc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00798fbc bytes 21603691
+ 00798fbc bytes 21203991
- 00798fc4 ["COPY", "tmp:0:8", ["const:468:8"]]
- 00798fc4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00798fc4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00798fc4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00798fc4 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 00798fc4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00798fc4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00798fc4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00798fc4 bytes 42a01191
+ 00798fc4 bytes 42601491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d642c49891bdb45b11f1b5986960ae72"></a>

### [`0079942c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00799/0079942c.md) → [`0079942c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00799/0079942c.md) FUN_0079942c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078c/0078cd14.md) [`007bdafc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bd/007bdafc.md) · 呼出先 20件 [`0044ab84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044ab84.md) [`00467074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`007cc71c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc71c.md) [`007cc720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007cc720.md)
- 新版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`007bdafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bdafc.md) · 呼出先 20件 [`0044ab84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ab84.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`007cc71c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc71c.md) [`007cc720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc720.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.60% / 新版 92.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00799764",
      "incomplete_value": true,
      "site": "00799764",
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
      "definition_site": "00799764",
      "incomplete_value": true,
      "site": "00799764",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007997d4",
      "incomplete_value": false,
      "site": "007997d4",
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
    "old": {
      "definition_site": "007997d4",
      "incomplete_value": false,
      "site": "007997d4",
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
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00799854",
      "incomplete_value": true,
      "site": "00799854",
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
      "definition_site": "00799854",
      "incomplete_value": true,
      "site": "00799854",
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
    "ordinal": 38,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00799470",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0079947c",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00799484",
      "PARAM",
      [
        "storage",
        "00bf4468",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00799470",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0079947c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00799484",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00799470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00799/0079942c.md#insn-00799470) · [`0079947c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00799/0079942c.md#insn-0079947c) · [`00799484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00799/0079942c.md#insn-00799484)
- 新版 `00799470`（命令位置の公開資料なし） · `0079947c`（命令位置の公開資料なし） · `00799484`（命令位置の公開資料なし）

~~~diff
- 00799470 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00799470 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00799470 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00799470 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00799470 bytes 00dd44f9
+ 00799470 bytes 003d45f9
- 0079947c ["COPY", "tmp:0:8", ["const:d98:8"]]
- 0079947c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0079947c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0079947c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0079947c ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 0079947c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0079947c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0079947c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0079947c bytes 21603691
+ 0079947c bytes 21203991
- 00799484 ["COPY", "tmp:0:8", ["const:468:8"]]
- 00799484 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00799484 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00799484 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00799484 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 00799484 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00799484 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00799484 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00799484 bytes 42a01191
+ 00799484 bytes 42601491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80b0d64546493e7625a52cd65734199c"></a>

### [`007999cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00799/007999cc.md) → [`007999cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00799/007999cc.md) FUN_007999cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078c/0078cd14.md) [`007bdafc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bd/007bdafc.md) · 呼出先 30件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00467074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`006fdbdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006fd/006fdbdc.md)
- 新版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`007bdafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bdafc.md) · 呼出先 30件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`006fdbdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fdbdc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.21% / 新版 96.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00799c2c",
      "incomplete_value": false,
      "site": "00799c30",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:d30:8"
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
      "definition_site": "00799c2c",
      "incomplete_value": false,
      "site": "00799c30",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:c80:8"
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
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00799eb8",
      "incomplete_value": false,
      "site": "00799ebc",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:d30:8"
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
      "definition_site": "00799eb8",
      "incomplete_value": false,
      "site": "00799ebc",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:c80:8"
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
    "ordinal": 48,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0079a010",
      "incomplete_value": true,
      "site": "0079a014",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:d30:8"
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
      "definition_site": "0079a010",
      "incomplete_value": true,
      "site": "0079a014",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:c80:8"
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
    "ordinal": 60,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00799a34",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00799a40",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00799a48",
      "PARAM",
      [
        "storage",
        "00bf4468",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00799a34",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00799a40",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00799a48",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00799a34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00799/007999cc.md#insn-00799a34) · [`00799a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00799/007999cc.md#insn-00799a40) · [`00799a48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00799/007999cc.md#insn-00799a48)
- 新版 `00799a34`（命令位置の公開資料なし） · `00799a40`（命令位置の公開資料なし） · `00799a48`（命令位置の公開資料なし）

~~~diff
- 00799a34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00799a34 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00799a34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00799a34 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00799a34 bytes 00dd44f9
+ 00799a34 bytes 003d45f9
- 00799a40 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00799a40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00799a40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00799a40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00799a40 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00799a40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00799a40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00799a40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00799a40 bytes 21603691
+ 00799a40 bytes 21203991
- 00799a48 ["COPY", "tmp:0:8", ["const:468:8"]]
- 00799a48 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00799a48 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00799a48 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00799a48 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 00799a48 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00799a48 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00799a48 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00799a48 bytes 42a01191
+ 00799a48 bytes 42601491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1c0e099a4ecad963a597906ae1d3840"></a>

### [`0079a4e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079a/0079a4e4.md) → [`0079a4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079a/0079a4e4.md) FUN_0079a4e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078c/0078cd14.md) [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) · 呼出先 67件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449bac.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md)
- 新版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 67件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.10% / 新版 94.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 10件, `store_value` 23件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0079a53c",
      "incomplete_value": true,
      "site": "0079a548",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bd3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079a53c",
      "incomplete_value": true,
      "site": "0079a548",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bda:8"
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
      "definition_site": "0079a9c8",
      "incomplete_value": true,
      "site": "0079a9dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a57:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079a9c8",
      "incomplete_value": true,
      "site": "0079a9dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a51:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 49,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0079ab0c",
      "incomplete_value": true,
      "site": "0079ab28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a2b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079ab0c",
      "incomplete_value": true,
      "site": "0079ab28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a32:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 58,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0079a53c",
      "READ",
      [
        "storage",
        "002a6bda",
        null,
        "string"
      ]
    ],
    [
      "0079a55c",
      "PARAM",
      [
        "storage",
        "00291e35",
        null,
        "string"
      ]
    ],
    [
      "0079a64c",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0079a53c",
      "READ",
      [
        "storage",
        "002a6bd3",
        null,
        "string"
      ]
    ],
    [
      "0079a55c",
      "PARAM",
      [
        "storage",
        "00291ec2",
        null,
        "string"
      ]
    ],
    [
      "0079a64c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079a534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079a/0079a4e4.md#insn-0079a534) · [`0079a55c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079a/0079a4e4.md#insn-0079a55c) · [`0079a64c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079a/0079a4e4.md#insn-0079a64c)
- 新版 `0079a534`（命令位置の公開資料なし） · `0079a55c`（命令位置の公開資料なし） · `0079a64c`（命令位置の公開資料なし）

~~~diff
- 0079a534 ["COPY", "tmp:0:8", ["const:bda:8"]]
- 0079a534 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079a534 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079a534 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079a534 ["COPY", "tmp:0:8", ["const:bd3:8"]]
+ 0079a534 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079a534 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079a534 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079a534 bytes 29692f91
+ 0079a534 bytes 294d2f91
- 0079a55c ["COPY", "tmp:0:8", ["const:e35:8"]]
- 0079a55c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0079a55c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0079a55c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0079a55c ["COPY", "tmp:0:8", ["const:ec2:8"]]
+ 0079a55c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0079a55c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0079a55c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0079a55c bytes 21d43891
+ 0079a55c bytes 21083b91
- 0079a64c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9b8:8"]]
- 0079a64c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0079a64c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
+ 0079a64c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0079a64c bytes 20dd44f9
+ 0079a64c bytes 203d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ad5249fa5b0e71b20a0b5136ed52dc6"></a>

### [`007ab6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ab/007ab6a0.md) → [`007ab6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ab/007ab6a0.md) FUN_007ab6a0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) · 呼出先 31件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 31件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.35% / 新版 91.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 21件, `store_destination` 14件, `store_value` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ab994",
      "incomplete_value": true,
      "site": "007ab9a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f05:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ab994",
      "incomplete_value": true,
      "site": "007ab9a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e78:8"
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
      "definition_site": "007ab998",
      "incomplete_value": true,
      "site": "007ab9a8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "007ab998",
      "incomplete_value": true,
      "site": "007ab9a8",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007abbc0",
      "incomplete_value": true,
      "site": "007abbcc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:291000:8"
              ],
              [
                "leaf",
                "const:eaf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007abbc0",
      "incomplete_value": true,
      "site": "007abbcc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:291000:8"
              ],
              [
                "leaf",
                "const:e22:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007ab6f0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007ab6fc",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007ab704",
      "PARAM",
      [
        "storage",
        "00bf4468",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007ab6f0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007ab6fc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007ab704",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ab6f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ab/007ab6a0.md#insn-007ab6f0) · [`007ab6fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ab/007ab6a0.md#insn-007ab6fc) · [`007ab704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ab/007ab6a0.md#insn-007ab704)
- 新版 `007ab6f0`（命令位置の公開資料なし） · `007ab6fc`（命令位置の公開資料なし） · `007ab704`（命令位置の公開資料なし）

~~~diff
- 007ab6f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 007ab6f0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007ab6f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007ab6f0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007ab6f0 bytes 00dd44f9
+ 007ab6f0 bytes 003d45f9
- 007ab6fc ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007ab6fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007ab6fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007ab6fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007ab6fc ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007ab6fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007ab6fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007ab6fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007ab6fc bytes 21603691
+ 007ab6fc bytes 21203991
- 007ab704 ["COPY", "tmp:0:8", ["const:468:8"]]
- 007ab704 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007ab704 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007ab704 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007ab704 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 007ab704 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007ab704 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007ab704 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007ab704 bytes 42a01191
+ 007ab704 bytes 42601491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfb45334a00ba006ae001f10ed87859e"></a>

### [`007ac760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ac/007ac760.md) → [`007ac760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007ac760.md) FUN_007ac760

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.55% / 新版 85.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `store_destination` 21件, `store_value` 10件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ac818",
      "incomplete_value": true,
      "site": "007ac818",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:704:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ac818",
      "incomplete_value": true,
      "site": "007ac818",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:70b:8"
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
      "definition_site": "007ac830",
      "incomplete_value": true,
      "site": "007ac830",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4f4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ac830",
      "incomplete_value": true,
      "site": "007ac830",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:588:8"
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
      "definition_site": "007ac834",
      "incomplete_value": true,
      "site": "007ac834",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007ac834",
      "incomplete_value": true,
      "site": "007ac834",
      "value": [
        "LOAD",
        "8",
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
      "007ac794",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007ac7a0",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007ac7a8",
      "PARAM",
      [
        "storage",
        "00bf4468",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007ac794",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007ac7a0",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007ac7a8",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ac794`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ac/007ac760.md#insn-007ac794) · [`007ac7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ac/007ac760.md#insn-007ac7a0) · [`007ac7a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ac/007ac760.md#insn-007ac7a8)
- 新版 `007ac794`（命令位置の公開資料なし） · `007ac7a0`（命令位置の公開資料なし） · `007ac7a8`（命令位置の公開資料なし）

~~~diff
- 007ac794 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 007ac794 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007ac794 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007ac794 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007ac794 bytes 08dd44f9
+ 007ac794 bytes 083d45f9
- 007ac7a0 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007ac7a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007ac7a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007ac7a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007ac7a0 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007ac7a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007ac7a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007ac7a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007ac7a0 bytes 21603691
+ 007ac7a0 bytes 21203991
- 007ac7a8 ["COPY", "tmp:0:8", ["const:468:8"]]
- 007ac7a8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007ac7a8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007ac7a8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007ac7a8 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 007ac7a8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007ac7a8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007ac7a8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007ac7a8 bytes 42a01191
+ 007ac7a8 bytes 42601491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acb5684ab763a82458dba51d8d32dbdf"></a>

### [`007bdafc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bd/007bdafc.md) → [`007bdafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bdafc.md) FUN_007bdafc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007c9cac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9cac.md) [`007c9d9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9d9c.md) · 呼出先 33件 [`00469fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469fac.md) [`005bfb9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005bf/005bfb9c.md) [`005bfe78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005bf/005bfe78.md) [`005c01d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005c0/005c01d4.md) [`005c3468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005c3/005c3468.md)
- 新版 呼出元 2件 [`007c9cac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9cac.md) [`007c9d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9d9c.md) · 呼出先 33件 [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`005bfb9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bf/005bfb9c.md) [`005bfe78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bf/005bfe78.md) [`005c01d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c0/005c01d4.md) [`005c3468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c3/005c3468.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.25% / 新版 95.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007bdbd0",
      "incomplete_value": false,
      "site": "007bdbd8",
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
    "old": {
      "definition_site": "007bdbd0",
      "incomplete_value": false,
      "site": "007bdbd8",
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
            "const:617:8"
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
      "definition_site": "007bdbf8",
      "incomplete_value": false,
      "site": "007bdc04",
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
    "old": {
      "definition_site": "007bdbf8",
      "incomplete_value": false,
      "site": "007bdc04",
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
            "const:9aa:8"
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
      "definition_site": "007bdc30",
      "incomplete_value": false,
      "site": "007bdc34",
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
    "old": {
      "definition_site": "007bdc30",
      "incomplete_value": false,
      "site": "007bdc34",
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
            "const:6a4:8"
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
      "007bdbd8",
      "DATA",
      [
        "storage",
        "0029e617",
        null,
        "string"
      ]
    ],
    [
      "007bdc04",
      "DATA",
      [
        "storage",
        "002a69aa",
        null,
        "string"
      ]
    ],
    [
      "007bdc34",
      "DATA",
      [
        "storage",
        "002a16a4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007bdbd8",
      "DATA",
      [
        "storage",
        "0029e6a4",
        null,
        "string"
      ]
    ],
    [
      "007bdc04",
      "DATA",
      [
        "storage",
        "002a69a3",
        null,
        "string"
      ]
    ],
    [
      "007bdc34",
      "DATA",
      [
        "storage",
        "002a1731",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007bdbd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bd/007bdafc.md#insn-007bdbd0) · [`007bdbd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bd/007bdafc.md#insn-007bdbd4)
- 新版 `007bdbd0`（命令位置の公開資料なし） · `007bdbd4`（命令位置の公開資料なし）

~~~diff
- 007bdbd0 ["COPY", "tmp:0:8", ["const:617:8"]]
- 007bdbd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007bdbd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007bdbd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007bdbd0 ["COPY", "tmp:0:8", ["const:6a4:8"]]
+ 007bdbd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007bdbd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007bdbd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007bdbd0 bytes 085d1891
+ 007bdbd0 bytes 08911a91
- 007bdbd4 ["COPY", "tmp:0:8", ["const:18:8"]]
- 007bdbd4 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 007bdbd4 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 007bdbd4 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 007bdbd4 bytes f4630091
+ 007bdbd4 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 007bdbd4 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
+ 007bdbd4 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
+ 007bdbd4 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
+ 007bdbd4 bytes f4630091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8782ed055085acbf17ca1da3fe60652"></a>

### [`007be3c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007be/007be3c8.md) → [`007be3c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007be3c8.md) FUN_007be3c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007999cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00799/007999cc.md) · 呼出先 7件 [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`009e964c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009e9/009e964c.md) [`009e9b90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009e9/009e9b90.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`007999cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00799/007999cc.md) · 呼出先 7件 [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`009e964c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e964c.md) [`009e9b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e9b90.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.29% / 新版 95.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007be47c",
      "incomplete_value": false,
      "site": "007be480",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:d30:8"
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
      "definition_site": "007be47c",
      "incomplete_value": false,
      "site": "007be480",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:c80:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007be440",
      "READ",
      [
        "storage",
        "00c1b470",
        null,
        "pointer"
      ]
    ],
    [
      "007be454",
      "DATA",
      [
        "storage",
        "00c0bc38",
        null,
        "undefined *"
      ]
    ],
    [
      "007be480",
      "DATA",
      [
        "storage",
        "00c0bc90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007be440",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "007be454",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ],
    [
      "007be480",
      "DATA",
      [
        "storage",
        "00c0bd40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007be440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007be/007be3c8.md#insn-007be440) · [`007be474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007be/007be3c8.md#insn-007be474)
- 新版 `007be440`（命令位置の公開資料なし） · `007be474`（命令位置の公開資料なし）

~~~diff
- 007be440 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:470:8"]]
- 007be440 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 007be440 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:520:8"]]
+ 007be440 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 007be440 bytes 183b42f9
+ 007be440 bytes 189342f9
- 007be474 ["COPY", "tmp:0:8", ["const:c80:8"]]
- 007be474 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007be474 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007be474 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007be474 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 007be474 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007be474 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007be474 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007be474 bytes 08013291
+ 007be474 bytes 08c13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-857a204c111850d835e7cf60bbf46bea"></a>

### [`007be548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007be/007be548.md) → [`007be548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007be548.md) FUN_007be548

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007bea98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007be/007bea98.md) · 呼出先 10件 [`0044b9cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b9cc.md) [`0044c104`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044c/0044c104.md) [`0064c428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0064c/0064c428.md) [`006582c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00658/006582c8.md) [`0065bff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0065b/0065bff4.md)
- 新版 呼出元 1件 [`007bea98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007bea98.md) · 呼出先 10件 [`0044b9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b9cc.md) [`0044c104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c104.md) [`0064c428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064c428.md) [`006582c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006582c8.md) [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.24% / 新版 98.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007be564",
      "incomplete_value": false,
      "site": "007be568",
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
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007be564",
      "incomplete_value": false,
      "site": "007be568",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007bea14",
      "incomplete_value": false,
      "site": "007bea18",
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
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007bea14",
      "incomplete_value": false,
      "site": "007bea18",
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
            "const:d08:8"
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
      "definition_site": "007bea50",
      "incomplete_value": false,
      "site": "007bea54",
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
    "old": {
      "definition_site": "007bea50",
      "incomplete_value": false,
      "site": "007bea54",
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
            "const:1e8:8"
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
      "007be568",
      "DATA",
      [
        "storage",
        "00bfcde0",
        null,
        "pointer"
      ]
    ],
    [
      "007bea18",
      "DATA",
      [
        "storage",
        "00bfad08",
        null,
        "pointer"
      ]
    ],
    [
      "007bea54",
      "DATA",
      [
        "storage",
        "00bf71e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007be568",
      "DATA",
      [
        "storage",
        "00bfce90",
        null,
        "pointer"
      ]
    ],
    [
      "007bea18",
      "DATA",
      [
        "storage",
        "00bfadb8",
        null,
        "pointer"
      ]
    ],
    [
      "007bea54",
      "DATA",
      [
        "storage",
        "00bf7298",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007be564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007be/007be548.md#insn-007be564) · [`007bea14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007be/007be548.md#insn-007bea14) · [`007bea50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007be/007be548.md#insn-007bea50)
- 新版 `007be564`（命令位置の公開資料なし） · `007bea14`（命令位置の公開資料なし） · `007bea50`（命令位置の公開資料なし）

~~~diff
- 007be564 ["COPY", "tmp:0:8", ["const:de0:8"]]
- 007be564 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007be564 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007be564 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007be564 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 007be564 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007be564 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007be564 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007be564 bytes 08813791
+ 007be564 bytes 08413a91
- 007bea14 ["COPY", "tmp:0:8", ["const:d08:8"]]
- 007bea14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007bea14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007bea14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007bea14 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 007bea14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007bea14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007bea14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007bea14 bytes 08213491
+ 007bea14 bytes 08e13691
- 007bea50 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 007bea50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007bea50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007bea50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007bea50 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 007bea50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007bea50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007bea50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007bea50 bytes 08a10791
+ 007bea50 bytes 08610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc95b17ca75cef793f594d0dc6254439"></a>

### [`007bebf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007be/007bebf8.md) → [`007bebf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007bebf8.md) FUN_007bebf8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007beabc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007be/007beabc.md) [`007bebf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007be/007bebf8.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`007beabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007beabc.md) [`007bebf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007bebf8.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.17% / 新版 99.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007bed5c",
      "incomplete_value": false,
      "site": "007bed64",
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
    "old": {
      "definition_site": "007bed5c",
      "incomplete_value": false,
      "site": "007bed64",
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
            "const:311:8"
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
      "definition_site": "007beeb4",
      "incomplete_value": false,
      "site": "007beebc",
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
    "old": {
      "definition_site": "007beeb4",
      "incomplete_value": false,
      "site": "007beebc",
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
            "const:2f5:8"
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
      "definition_site": "007bef5c",
      "incomplete_value": false,
      "site": "007bef68",
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
            "const:867:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007bef5c",
      "incomplete_value": false,
      "site": "007bef68",
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
            "const:7da:8"
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
      "007bed5c",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "007beeb4",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "007bef5c",
      "PARAM",
      [
        "storage",
        "002967da",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "007bed5c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "007beeb4",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "007bef5c",
      "PARAM",
      [
        "storage",
        "00296867",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007bed5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007be/007bebf8.md#insn-007bed5c) · [`007beeb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007be/007bebf8.md#insn-007beeb4) · [`007bef5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007be/007bebf8.md#insn-007bef5c)
- 新版 `007bed5c`（命令位置の公開資料なし） · `007beeb4`（命令位置の公開資料なし） · `007bef5c`（命令位置の公開資料なし）

~~~diff
- 007bed5c ["COPY", "tmp:0:8", ["const:311:8"]]
- 007bed5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007bed5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007bed5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007bed5c ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 007bed5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007bed5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007bed5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007bed5c bytes 21440c91
+ 007bed5c bytes 21280c91
- 007beeb4 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 007beeb4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007beeb4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007beeb4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007beeb4 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 007beeb4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007beeb4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007beeb4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007beeb4 bytes 21d40b91
+ 007beeb4 bytes 21b80b91
- 007bef5c ["COPY", "tmp:0:8", ["const:7da:8"]]
- 007bef5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007bef5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007bef5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007bef5c ["COPY", "tmp:0:8", ["const:867:8"]]
+ 007bef5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007bef5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007bef5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007bef5c bytes 21681f91
+ 007bef5c bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8a4e37c087a2ca9aca0082552d44c4c"></a>

### [`007bfcb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bf/007bfcb4.md) → [`007bfcb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfcb4.md) FUN_007bfcb4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007bf6b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bf/007bf6b8.md) [`008cd26c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd26c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`007bf6b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bf6b8.md) [`008cd26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd26c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "007bfcc0",
      "incomplete_value": false,
      "site": "007bfcc4",
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
      "definition_site": "007bfcc0",
      "incomplete_value": false,
      "site": "007bfcc4",
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
      "007bfcc0",
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
      "007bfcc0",
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

- 旧版 [`007bfcc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bf/007bfcb4.md#insn-007bfcc0)
- 新版 `007bfcc0`（命令位置の公開資料なし）

~~~diff
- 007bfcc0 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007bfcc0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007bfcc0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007bfcc0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007bfcc0 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 007bfcc0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007bfcc0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007bfcc0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007bfcc0 bytes 00280c91
+ 007bfcc0 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb9118e148f31a1fe07918d7aaed5aa4"></a>

### [`007bfcc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bf/007bfcc8.md) → [`007bfcc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfcc8.md) FUN_007bfcc8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0078cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078c/0078cd14.md) [`007da634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007da/007da634.md) [`007dbfcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007db/007dbfcc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`007da634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da634.md) [`007dbfcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007dbfcc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "007bfcd4",
      "incomplete_value": false,
      "site": "007bfcd8",
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
      "definition_site": "007bfcd4",
      "incomplete_value": false,
      "site": "007bfcd8",
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
      "007bfcd4",
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
      "007bfcd4",
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

- 旧版 [`007bfcd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bf/007bfcc8.md#insn-007bfcd4)
- 新版 `007bfcd4`（命令位置の公開資料なし）

~~~diff
- 007bfcd4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007bfcd4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007bfcd4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007bfcd4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007bfcd4 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 007bfcd4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007bfcd4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007bfcd4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007bfcd4 bytes 00280c91
+ 007bfcd4 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-066704c4b8ea50aeef92729a00bbe379"></a>

### [`007bfcdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bf/007bfcdc.md) → [`007bfcdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfcdc.md) FUN_007bfcdc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`0078cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078c/0078cd14.md) [`00796d74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00796/00796d74.md) [`007da86c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007da/007da86c.md) [`007dbc94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007db/007dbc94.md) [`007dc0fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007dc/007dc0fc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 6件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`00796d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00796/00796d74.md) [`007da86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da86c.md) [`007dbc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007dbc94.md) [`007dc0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dc/007dc0fc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "007bfce8",
      "incomplete_value": false,
      "site": "007bfcec",
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
      "definition_site": "007bfce8",
      "incomplete_value": false,
      "site": "007bfcec",
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
      "007bfce8",
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
      "007bfce8",
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

- 旧版 [`007bfce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bf/007bfcdc.md#insn-007bfce8)
- 新版 `007bfce8`（命令位置の公開資料なし）

~~~diff
- 007bfce8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007bfce8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007bfce8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007bfce8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007bfce8 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 007bfce8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007bfce8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007bfce8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007bfce8 bytes 00280c91
+ 007bfce8 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c339a94bf23d37711b2785c794962f1"></a>

### [`007bfcf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bf/007bfcf4.md) → [`007bfcf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfcf4.md) FUN_007bfcf4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007bfd08",
      "incomplete_value": false,
      "site": "007bfd0c",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007bfd08",
      "incomplete_value": false,
      "site": "007bfd0c",
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
            "const:e00:8"
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
      "007bfd0c",
      "DATA",
      [
        "storage",
        "00bfce00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007bfd0c",
      "DATA",
      [
        "storage",
        "00bfceb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007bfd08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bf/007bfcf4.md#insn-007bfd08)
- 新版 `007bfd08`（命令位置の公開資料なし）

~~~diff
- 007bfd08 ["COPY", "tmp:0:8", ["const:e00:8"]]
- 007bfd08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007bfd08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007bfd08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007bfd08 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 007bfd08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007bfd08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007bfd08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007bfd08 bytes 08013891
+ 007bfd08 bytes 08c13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd2b6aef9c7baf6a8f05498d5978cfc1"></a>

### [`007bfd18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bf/007bfd18.md) → [`007bfd18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfd18.md) FUN_007bfd18

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
      "definition_site": "007bfd1c",
      "incomplete_value": false,
      "site": "007bfd20",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007bfd1c",
      "incomplete_value": false,
      "site": "007bfd20",
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
            "const:e00:8"
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
      "007bfd20",
      "DATA",
      [
        "storage",
        "00bfce00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007bfd20",
      "DATA",
      [
        "storage",
        "00bfceb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007bfd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bf/007bfd18.md#insn-007bfd1c)
- 新版 `007bfd1c`（命令位置の公開資料なし）

~~~diff
- 007bfd1c ["COPY", "tmp:0:8", ["const:e00:8"]]
- 007bfd1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007bfd1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007bfd1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007bfd1c ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 007bfd1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007bfd1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007bfd1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007bfd1c bytes 08013891
+ 007bfd1c bytes 08c13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f719b6375e8155454fbab17c27cd85b5"></a>

### [`007bfd30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bf/007bfd30.md) → [`007bfd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfd30.md) FUN_007bfd30

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.63% / 新版 96.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007bfe1c",
      "incomplete_value": true,
      "site": "007bfe30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:112:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007bfe1c",
      "incomplete_value": true,
      "site": "007bfe30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:85:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007bfefc",
      "incomplete_value": false,
      "site": "007bfefc",
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
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007bfefc",
      "incomplete_value": false,
      "site": "007bfefc",
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
            "const:e70:8"
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
      "007bfe1c",
      "READ",
      [
        "storage",
        "00299085",
        null,
        "string"
      ]
    ],
    [
      "007bfe24",
      "READ",
      [
        "storage",
        "00299092",
        null,
        "string"
      ]
    ],
    [
      "007bfefc",
      "DATA",
      [
        "storage",
        "00bfce70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007bfe1c",
      "READ",
      [
        "storage",
        "00299112",
        null,
        "string"
      ]
    ],
    [
      "007bfe24",
      "READ",
      [
        "storage",
        "0029911f",
        null,
        "string"
      ]
    ],
    [
      "007bfefc",
      "DATA",
      [
        "storage",
        "00bfcf20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007bfe18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bf/007bfd30.md#insn-007bfe18) · [`007bfef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bf/007bfd30.md#insn-007bfef4)
- 新版 `007bfe18`（命令位置の公開資料なし） · `007bfef4`（命令位置の公開資料なし）

~~~diff
- 007bfe18 ["COPY", "tmp:0:8", ["const:85:8"]]
- 007bfe18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007bfe18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007bfe18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007bfe18 ["COPY", "tmp:0:8", ["const:112:8"]]
+ 007bfe18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007bfe18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007bfe18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007bfe18 bytes 29150291
+ 007bfe18 bytes 29490491
- 007bfef4 ["COPY", "tmp:0:8", ["const:e70:8"]]
- 007bfef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007bfef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007bfef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007bfef4 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 007bfef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007bfef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007bfef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007bfef4 bytes 08c13991
+ 007bfef4 bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c46ea262dcf835b4814fcc1d492a1bf"></a>

### [`007c015c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c015c.md) → [`007c015c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c015c.md) FUN_007c015c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c0170",
      "incomplete_value": false,
      "site": "007c0174",
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
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0170",
      "incomplete_value": false,
      "site": "007c0174",
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
            "const:e70:8"
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
      "007c0174",
      "DATA",
      [
        "storage",
        "00bfce70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0174",
      "DATA",
      [
        "storage",
        "00bfcf20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c015c.md#insn-007c0170)
- 新版 `007c0170`（命令位置の公開資料なし）

~~~diff
- 007c0170 ["COPY", "tmp:0:8", ["const:e70:8"]]
- 007c0170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c0170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c0170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c0170 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 007c0170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c0170 bytes 08c13991
+ 007c0170 bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bff20f2cdd158e9384512d9680fa462"></a>

### [`007c0180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0180.md) → [`007c0180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0180.md) FUN_007c0180

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
      "definition_site": "007c0184",
      "incomplete_value": false,
      "site": "007c0188",
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
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0184",
      "incomplete_value": false,
      "site": "007c0188",
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
            "const:e70:8"
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
      "007c0188",
      "DATA",
      [
        "storage",
        "00bfce70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0188",
      "DATA",
      [
        "storage",
        "00bfcf20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0180.md#insn-007c0184)
- 新版 `007c0184`（命令位置の公開資料なし）

~~~diff
- 007c0184 ["COPY", "tmp:0:8", ["const:e70:8"]]
- 007c0184 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c0184 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c0184 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c0184 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 007c0184 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0184 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0184 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c0184 bytes 08c13991
+ 007c0184 bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d914aca1b4350fd4a9fb09a2b72187f1"></a>

### [`007c0198`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0198.md) → [`007c0198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0198.md) FUN_007c0198

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 17件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.97% / 新版 98.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007c0360",
      "incomplete_value": false,
      "site": "007c036c",
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
            "const:50f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0360",
      "incomplete_value": false,
      "site": "007c036c",
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
            "const:5a3:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007c03d0",
      "incomplete_value": false,
      "site": "007c03dc",
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
            "const:50f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c03d0",
      "incomplete_value": false,
      "site": "007c03dc",
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
            "const:5a3:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007c0484",
      "incomplete_value": false,
      "site": "007c0490",
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
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0484",
      "incomplete_value": false,
      "site": "007c0490",
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
            "const:9b:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007c0360",
      "PARAM",
      [
        "storage",
        "002a85a3",
        null,
        "string"
      ]
    ],
    [
      "007c03d0",
      "PARAM",
      [
        "storage",
        "002a85a3",
        null,
        "string"
      ]
    ],
    [
      "007c0484",
      "PARAM",
      [
        "storage",
        "0029909b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007c0360",
      "PARAM",
      [
        "storage",
        "002a850f",
        null,
        "string"
      ]
    ],
    [
      "007c03d0",
      "PARAM",
      [
        "storage",
        "002a850f",
        null,
        "string"
      ]
    ],
    [
      "007c0484",
      "PARAM",
      [
        "storage",
        "00299128",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0198.md#insn-007c0360) · [`007c03d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0198.md#insn-007c03d0) · [`007c0484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0198.md#insn-007c0484)
- 新版 `007c0360`（命令位置の公開資料なし） · `007c03d0`（命令位置の公開資料なし） · `007c0484`（命令位置の公開資料なし）

~~~diff
- 007c0360 ["COPY", "tmp:0:8", ["const:5a3:8"]]
- 007c0360 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c0360 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c0360 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c0360 ["COPY", "tmp:0:8", ["const:50f:8"]]
+ 007c0360 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c0360 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c0360 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c0360 bytes 428c1691
+ 007c0360 bytes 423c1491
- 007c03d0 ["COPY", "tmp:0:8", ["const:5a3:8"]]
- 007c03d0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c03d0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c03d0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c03d0 ["COPY", "tmp:0:8", ["const:50f:8"]]
+ 007c03d0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c03d0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c03d0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c03d0 bytes 428c1691
+ 007c03d0 bytes 423c1491
- 007c0484 ["COPY", "tmp:0:8", ["const:9b:8"]]
- 007c0484 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c0484 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c0484 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c0484 ["COPY", "tmp:0:8", ["const:128:8"]]
+ 007c0484 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c0484 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c0484 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c0484 bytes 426c0291
+ 007c0484 bytes 42a00491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-623538d0568088bfab979ac37b6cfcc1"></a>

### [`007c0754`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0754.md) → [`007c0754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0754.md) FUN_007c0754

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c0768",
      "incomplete_value": false,
      "site": "007c076c",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0768",
      "incomplete_value": false,
      "site": "007c076c",
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
      "007c076c",
      "DATA",
      [
        "storage",
        "00bfcf00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c076c",
      "DATA",
      [
        "storage",
        "00bfcfb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0754.md#insn-007c0768)
- 新版 `007c0768`（命令位置の公開資料なし）

~~~diff
- 007c0768 ["COPY", "tmp:0:8", ["const:f00:8"]]
- 007c0768 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c0768 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c0768 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c0768 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 007c0768 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0768 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0768 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c0768 bytes 08013c91
+ 007c0768 bytes 08c13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71d7cc6cf0ace0b04a667d736fa5c2f5"></a>

### [`007c0778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0778.md) → [`007c0778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0778.md) FUN_007c0778

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
      "definition_site": "007c077c",
      "incomplete_value": false,
      "site": "007c0780",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c077c",
      "incomplete_value": false,
      "site": "007c0780",
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
      "007c0780",
      "DATA",
      [
        "storage",
        "00bfcf00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0780",
      "DATA",
      [
        "storage",
        "00bfcfb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c077c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0778.md#insn-007c077c)
- 新版 `007c077c`（命令位置の公開資料なし）

~~~diff
- 007c077c ["COPY", "tmp:0:8", ["const:f00:8"]]
- 007c077c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c077c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c077c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c077c ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 007c077c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c077c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c077c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c077c bytes 08013c91
+ 007c077c bytes 08c13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8342e2497448df0ef63b42c8bbf28b91"></a>

### [`007c0834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0834.md) → [`007c0834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0834.md) FUN_007c0834

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c0858",
      "incomplete_value": false,
      "site": "007c0858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0858",
      "incomplete_value": false,
      "site": "007c0858",
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
            "const:f80:8"
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
      "007c0858",
      "DATA",
      [
        "storage",
        "00bfcf80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0858",
      "DATA",
      [
        "storage",
        "00bfd030",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0834.md#insn-007c0850) · [`007c0854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0834.md#insn-007c0854)
- 新版 `007c0850`（命令位置の公開資料なし） · `007c0854`（命令位置の公開資料なし）

~~~diff
- 007c0850 ["COPY", "register:4040:8", ["const:bfc000:8"]]
+ 007c0850 ["COPY", "register:4040:8", ["const:bfd000:8"]]
- 007c0850 bytes e8210090
+ 007c0850 bytes e82100b0
- 007c0854 ["COPY", "tmp:0:8", ["const:f80:8"]]
- 007c0854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c0854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c0854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c0854 ["COPY", "tmp:0:8", ["const:30:8"]]
+ 007c0854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c0854 bytes 08013e91
+ 007c0854 bytes 08c10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-346d877af69084bdf1988eef7b94d4e6"></a>

### [`007c0868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0868.md) → [`007c0868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0868.md) FUN_007c0868

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
      "definition_site": "007c0874",
      "incomplete_value": false,
      "site": "007c0874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0874",
      "incomplete_value": false,
      "site": "007c0874",
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
      "007c0874",
      "DATA",
      [
        "storage",
        "00bfcf80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0874",
      "DATA",
      [
        "storage",
        "00bfd030",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c086c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0868.md#insn-007c086c) · [`007c0870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0868.md#insn-007c0870)
- 新版 `007c086c`（命令位置の公開資料なし） · `007c0870`（命令位置の公開資料なし）

~~~diff
- 007c086c ["COPY", "register:4048:8", ["const:bfc000:8"]]
+ 007c086c ["COPY", "register:4048:8", ["const:bfd000:8"]]
- 007c086c bytes e9210090
+ 007c086c bytes e92100b0
- 007c0870 ["COPY", "tmp:0:8", ["const:f80:8"]]
- 007c0870 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c0870 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c0870 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c0870 ["COPY", "tmp:0:8", ["const:30:8"]]
+ 007c0870 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c0870 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c0870 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c0870 bytes 29013e91
+ 007c0870 bytes 29c10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-273a8b4dab1a9ee23d392ff0700f02e3"></a>

### [`007c0884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0884.md) → [`007c0884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0884.md) FUN_007c0884

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.31% / 新版 94.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007c0914",
      "incomplete_value": true,
      "site": "007c0928",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:59:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0914",
      "incomplete_value": true,
      "site": "007c0928",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fcc:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c0988",
      "incomplete_value": false,
      "site": "007c0988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0988",
      "incomplete_value": false,
      "site": "007c0988",
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
            "const:ff0:8"
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
      "definition_site": "007c0a64",
      "incomplete_value": false,
      "site": "007c0a68",
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
    "old": {
      "definition_site": "007c0a64",
      "incomplete_value": false,
      "site": "007c0a68",
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
            "const:5d6:8"
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
      "007c0914",
      "READ",
      [
        "storage",
        "00297fcc",
        null,
        "string"
      ]
    ],
    [
      "007c0988",
      "DATA",
      [
        "storage",
        "00bfcff0",
        null,
        "undefined *"
      ]
    ],
    [
      "007c09e0",
      "READ",
      [
        "storage",
        "00bfd010",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007c0914",
      "READ",
      [
        "storage",
        "00298059",
        null,
        "string"
      ]
    ],
    [
      "007c0988",
      "DATA",
      [
        "storage",
        "00bfd0a0",
        null,
        "undefined *"
      ]
    ],
    [
      "007c09e0",
      "READ",
      [
        "storage",
        "00bfd0c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0884.md#insn-007c0908) · [`007c090c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0884.md#insn-007c090c) · [`007c097c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0884.md#insn-007c097c)
- 新版 `007c0908`（命令位置の公開資料なし） · `007c090c`（命令位置の公開資料なし） · `007c097c`（命令位置の公開資料なし）

~~~diff
- 007c0908 ["COPY", "register:4048:8", ["const:297000:8"]]
+ 007c0908 ["COPY", "register:4048:8", ["const:298000:8"]]
- 007c0908 bytes a9d6fff0
+ 007c0908 bytes c9d6ff90
- 007c090c ["COPY", "tmp:0:8", ["const:fcc:8"]]
- 007c090c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c090c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c090c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c090c ["COPY", "tmp:0:8", ["const:59:8"]]
+ 007c090c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c090c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c090c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c090c bytes 29313f91
+ 007c090c bytes 29650191
- 007c097c ["COPY", "register:4040:8", ["const:bfc000:8"]]
+ 007c097c ["COPY", "register:4040:8", ["const:bfd000:8"]]
- 007c097c bytes e8210090
+ 007c097c bytes e82100b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24c9bf1a197d9f87b6aff86a79b57fd1"></a>

### [`007c0b54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0b54.md) → [`007c0b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0b54.md) FUN_007c0b54

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c0b68",
      "incomplete_value": false,
      "site": "007c0b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0b68",
      "incomplete_value": false,
      "site": "007c0b6c",
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
            "const:ff0:8"
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
      "007c0b6c",
      "DATA",
      [
        "storage",
        "00bfcff0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0b6c",
      "DATA",
      [
        "storage",
        "00bfd0a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0b64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0b54.md#insn-007c0b64) · [`007c0b68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0b54.md#insn-007c0b68)
- 新版 `007c0b64`（命令位置の公開資料なし） · `007c0b68`（命令位置の公開資料なし）

~~~diff
- 007c0b64 ["COPY", "register:4040:8", ["const:bfc000:8"]]
+ 007c0b64 ["COPY", "register:4040:8", ["const:bfd000:8"]]
- 007c0b64 bytes e8210090
+ 007c0b64 bytes e82100b0
- 007c0b68 ["COPY", "tmp:0:8", ["const:ff0:8"]]
- 007c0b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c0b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c0b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c0b68 ["COPY", "tmp:0:8", ["const:a0:8"]]
+ 007c0b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c0b68 bytes 08c13f91
+ 007c0b68 bytes 08810291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a8df1b2794101820f93c75045145dc5"></a>

### [`007c0b78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0b78.md) → [`007c0b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0b78.md) FUN_007c0b78

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
      "definition_site": "007c0b7c",
      "incomplete_value": false,
      "site": "007c0b80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0b7c",
      "incomplete_value": false,
      "site": "007c0b80",
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
            "const:ff0:8"
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
      "007c0b80",
      "DATA",
      [
        "storage",
        "00bfcff0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0b80",
      "DATA",
      [
        "storage",
        "00bfd0a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0b78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0b78.md#insn-007c0b78) · [`007c0b7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0b78.md#insn-007c0b7c)
- 新版 `007c0b78`（命令位置の公開資料なし） · `007c0b7c`（命令位置の公開資料なし）

~~~diff
- 007c0b78 ["COPY", "register:4040:8", ["const:bfc000:8"]]
+ 007c0b78 ["COPY", "register:4040:8", ["const:bfd000:8"]]
- 007c0b78 bytes e8210090
+ 007c0b78 bytes e82100b0
- 007c0b7c ["COPY", "tmp:0:8", ["const:ff0:8"]]
- 007c0b7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c0b7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c0b7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c0b7c ["COPY", "tmp:0:8", ["const:a0:8"]]
+ 007c0b7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0b7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0b7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c0b7c bytes 08c13f91
+ 007c0b7c bytes 08810291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-118187a16c647fc09e20ed0d304088f0"></a>

### [`007c0c04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0c04.md) → [`007c0c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0c04.md) FUN_007c0c04

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c0c28",
      "incomplete_value": false,
      "site": "007c0c28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0c28",
      "incomplete_value": false,
      "site": "007c0c28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:80:8"
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
      "007c0c28",
      "DATA",
      [
        "storage",
        "00bfd080",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0c28",
      "DATA",
      [
        "storage",
        "00bfd130",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0c04.md#insn-007c0c24)
- 新版 `007c0c24`（命令位置の公開資料なし）

~~~diff
- 007c0c24 ["COPY", "tmp:0:8", ["const:80:8"]]
- 007c0c24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c0c24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c0c24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c0c24 ["COPY", "tmp:0:8", ["const:130:8"]]
+ 007c0c24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0c24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0c24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c0c24 bytes 08010291
+ 007c0c24 bytes 08c10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a575c0c0f446c9dcd255167eeedf069"></a>

### [`007c0c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0c38.md) → [`007c0c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0c38.md) FUN_007c0c38

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
      "definition_site": "007c0c44",
      "incomplete_value": false,
      "site": "007c0c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0c44",
      "incomplete_value": false,
      "site": "007c0c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:80:8"
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
      "007c0c44",
      "DATA",
      [
        "storage",
        "00bfd080",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0c44",
      "DATA",
      [
        "storage",
        "00bfd130",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0c40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0c38.md#insn-007c0c40)
- 新版 `007c0c40`（命令位置の公開資料なし）

~~~diff
- 007c0c40 ["COPY", "tmp:0:8", ["const:80:8"]]
- 007c0c40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c0c40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c0c40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c0c40 ["COPY", "tmp:0:8", ["const:130:8"]]
+ 007c0c40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c0c40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c0c40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c0c40 bytes 29010291
+ 007c0c40 bytes 29c10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5154cc6aa2ccaf2dfd122ec126fd1466"></a>

### [`007c0e24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0e24.md) → [`007c0e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0e24.md) FUN_007c0e24

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c0e48",
      "incomplete_value": false,
      "site": "007c0e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0e48",
      "incomplete_value": false,
      "site": "007c0e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:100:8"
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
      "007c0e48",
      "DATA",
      [
        "storage",
        "00bfd100",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0e48",
      "DATA",
      [
        "storage",
        "00bfd1b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0e44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0e24.md#insn-007c0e44)
- 新版 `007c0e44`（命令位置の公開資料なし）

~~~diff
- 007c0e44 ["COPY", "tmp:0:8", ["const:100:8"]]
- 007c0e44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c0e44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c0e44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c0e44 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 007c0e44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0e44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0e44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c0e44 bytes 08010491
+ 007c0e44 bytes 08c10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1192cdff2a9fa315b50ca6c6eba59f6"></a>

### [`007c0e58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0e58.md) → [`007c0e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0e58.md) FUN_007c0e58

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
      "definition_site": "007c0e64",
      "incomplete_value": false,
      "site": "007c0e64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0e64",
      "incomplete_value": false,
      "site": "007c0e64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:100:8"
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
      "007c0e64",
      "DATA",
      [
        "storage",
        "00bfd100",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0e64",
      "DATA",
      [
        "storage",
        "00bfd1b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c0/007c0e58.md#insn-007c0e60)
- 新版 `007c0e60`（命令位置の公開資料なし）

~~~diff
- 007c0e60 ["COPY", "tmp:0:8", ["const:100:8"]]
- 007c0e60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c0e60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c0e60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c0e60 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 007c0e60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c0e60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c0e60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c0e60 bytes 29010491
+ 007c0e60 bytes 29c10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f543d9e0d4ce20c073af87a8592e8e6"></a>

### [`007c1068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1068.md) → [`007c1068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1068.md) FUN_007c1068

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c108c",
      "incomplete_value": false,
      "site": "007c108c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c108c",
      "incomplete_value": false,
      "site": "007c108c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:180:8"
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
      "007c108c",
      "DATA",
      [
        "storage",
        "00bfd180",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c108c",
      "DATA",
      [
        "storage",
        "00bfd230",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c1088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1068.md#insn-007c1088)
- 新版 `007c1088`（命令位置の公開資料なし）

~~~diff
- 007c1088 ["COPY", "tmp:0:8", ["const:180:8"]]
- 007c1088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c1088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c1088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c1088 ["COPY", "tmp:0:8", ["const:230:8"]]
+ 007c1088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c1088 bytes 08010691
+ 007c1088 bytes 08c10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ef1b4b79b2e5236636ae026f52bf651"></a>

### [`007c109c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c109c.md) → [`007c109c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c109c.md) FUN_007c109c

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
      "definition_site": "007c10a8",
      "incomplete_value": false,
      "site": "007c10a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c10a8",
      "incomplete_value": false,
      "site": "007c10a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:180:8"
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
      "007c10a8",
      "DATA",
      [
        "storage",
        "00bfd180",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c10a8",
      "DATA",
      [
        "storage",
        "00bfd230",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c10a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c109c.md#insn-007c10a4)
- 新版 `007c10a4`（命令位置の公開資料なし）

~~~diff
- 007c10a4 ["COPY", "tmp:0:8", ["const:180:8"]]
- 007c10a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c10a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c10a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c10a4 ["COPY", "tmp:0:8", ["const:230:8"]]
+ 007c10a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c10a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c10a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c10a4 bytes 29010691
+ 007c10a4 bytes 29c10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a82b4ea54002e4bd543e0b615e75cb36"></a>

### [`007c10b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c10b8.md) → [`007c10b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c10b8.md) FUN_007c10b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`007c133c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c133c.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007c133c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c133c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.05% / 新版 95.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007c117c",
      "incomplete_value": true,
      "site": "007c1190",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:272:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c117c",
      "incomplete_value": true,
      "site": "007c1190",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:279:8"
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
      "definition_site": "007c11a8",
      "incomplete_value": false,
      "site": "007c11b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c11a8",
      "incomplete_value": false,
      "site": "007c11b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
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
      "007c117c",
      "READ",
      [
        "storage",
        "002a4279",
        null,
        "string"
      ]
    ],
    [
      "007c11b0",
      "DATA",
      [
        "storage",
        "00bfd1f0",
        null,
        "undefined *"
      ]
    ],
    [
      "007c11fc",
      "READ",
      [
        "storage",
        "00bfd210",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007c117c",
      "READ",
      [
        "storage",
        "002a4272",
        null,
        "string"
      ]
    ],
    [
      "007c11b0",
      "DATA",
      [
        "storage",
        "00bfd2a0",
        null,
        "undefined *"
      ]
    ],
    [
      "007c11fc",
      "READ",
      [
        "storage",
        "00bfd2c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c1174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c10b8.md#insn-007c1174) · [`007c11a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c10b8.md#insn-007c11a8)
- 新版 `007c1174`（命令位置の公開資料なし） · `007c11a8`（命令位置の公開資料なし）

~~~diff
- 007c1174 ["COPY", "tmp:0:8", ["const:279:8"]]
- 007c1174 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c1174 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c1174 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c1174 ["COPY", "tmp:0:8", ["const:272:8"]]
+ 007c1174 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c1174 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c1174 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c1174 bytes 29e50991
+ 007c1174 bytes 29c90991
- 007c11a8 ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 007c11a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c11a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c11a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c11a8 ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 007c11a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c11a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c11a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c11a8 bytes 08c10791
+ 007c11a8 bytes 08810a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-348e0dd518fc4e7cea732e3d7de494c1"></a>

### [`007c1308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1308.md) → [`007c1308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1308.md) FUN_007c1308

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c131c",
      "incomplete_value": false,
      "site": "007c1320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c131c",
      "incomplete_value": false,
      "site": "007c1320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
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
      "007c1320",
      "DATA",
      [
        "storage",
        "00bfd1f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c1320",
      "DATA",
      [
        "storage",
        "00bfd2a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c131c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1308.md#insn-007c131c)
- 新版 `007c131c`（命令位置の公開資料なし）

~~~diff
- 007c131c ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 007c131c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c131c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c131c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c131c ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 007c131c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c131c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c131c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c131c bytes 08c10791
+ 007c131c bytes 08810a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-939e3cde0ee6ad9f11661bbbbeca79d1"></a>

### [`007c132c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c132c.md) → [`007c132c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c132c.md) FUN_007c132c

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
      "definition_site": "007c1330",
      "incomplete_value": false,
      "site": "007c1334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c1330",
      "incomplete_value": false,
      "site": "007c1334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
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
      "007c1334",
      "DATA",
      [
        "storage",
        "00bfd1f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c1334",
      "DATA",
      [
        "storage",
        "00bfd2a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c1330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c132c.md#insn-007c1330)
- 新版 `007c1330`（命令位置の公開資料なし）

~~~diff
- 007c1330 ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 007c1330 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c1330 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c1330 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c1330 ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 007c1330 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1330 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1330 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c1330 bytes 08c10791
+ 007c1330 bytes 08810a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39661f19c0e3e7b073906840670e39b7"></a>

### [`007c1388`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1388.md) → [`007c1388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1388.md) FUN_007c1388

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c13ac",
      "incomplete_value": false,
      "site": "007c13ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c13ac",
      "incomplete_value": false,
      "site": "007c13ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
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
      "007c13ac",
      "DATA",
      [
        "storage",
        "00bfd280",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c13ac",
      "DATA",
      [
        "storage",
        "00bfd330",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c13a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1388.md#insn-007c13a8)
- 新版 `007c13a8`（命令位置の公開資料なし）

~~~diff
- 007c13a8 ["COPY", "tmp:0:8", ["const:280:8"]]
- 007c13a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c13a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c13a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c13a8 ["COPY", "tmp:0:8", ["const:330:8"]]
+ 007c13a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c13a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c13a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c13a8 bytes 08010a91
+ 007c13a8 bytes 08c10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89514de734e47321197c7ff3733028cb"></a>

### [`007c13bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c13bc.md) → [`007c13bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c13bc.md) FUN_007c13bc

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
      "definition_site": "007c13c8",
      "incomplete_value": false,
      "site": "007c13c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c13c8",
      "incomplete_value": false,
      "site": "007c13c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
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
      "007c13c8",
      "DATA",
      [
        "storage",
        "00bfd280",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c13c8",
      "DATA",
      [
        "storage",
        "00bfd330",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c13c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c13bc.md#insn-007c13c4)
- 新版 `007c13c4`（命令位置の公開資料なし）

~~~diff
- 007c13c4 ["COPY", "tmp:0:8", ["const:280:8"]]
- 007c13c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c13c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c13c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c13c4 ["COPY", "tmp:0:8", ["const:330:8"]]
+ 007c13c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c13c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c13c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c13c4 bytes 29010a91
+ 007c13c4 bytes 29c10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d2299fa278781df20e152b95dd1a4cd"></a>

### [`007c147c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c147c.md) → [`007c147c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c147c.md) FUN_007c147c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c14a0",
      "incomplete_value": false,
      "site": "007c14a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c14a0",
      "incomplete_value": false,
      "site": "007c14a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
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
      "007c14a0",
      "DATA",
      [
        "storage",
        "00bfd300",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c14a0",
      "DATA",
      [
        "storage",
        "00bfd3b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c149c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c147c.md#insn-007c149c)
- 新版 `007c149c`（命令位置の公開資料なし）

~~~diff
- 007c149c ["COPY", "tmp:0:8", ["const:300:8"]]
- 007c149c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c149c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c149c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c149c ["COPY", "tmp:0:8", ["const:3b0:8"]]
+ 007c149c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c149c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c149c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c149c bytes 08010c91
+ 007c149c bytes 08c10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbd1eefdfc7f587f449d50e678d13e01"></a>

### [`007c14b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c14b0.md) → [`007c14b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c14b0.md) FUN_007c14b0

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
      "definition_site": "007c14bc",
      "incomplete_value": false,
      "site": "007c14bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c14bc",
      "incomplete_value": false,
      "site": "007c14bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
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
      "007c14bc",
      "DATA",
      [
        "storage",
        "00bfd300",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c14bc",
      "DATA",
      [
        "storage",
        "00bfd3b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c14b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c14b0.md#insn-007c14b8)
- 新版 `007c14b8`（命令位置の公開資料なし）

~~~diff
- 007c14b8 ["COPY", "tmp:0:8", ["const:300:8"]]
- 007c14b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c14b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c14b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c14b8 ["COPY", "tmp:0:8", ["const:3b0:8"]]
+ 007c14b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c14b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c14b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c14b8 bytes 29010c91
+ 007c14b8 bytes 29c10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3b3f153ce4ce58252b35b979eb5327d"></a>

### [`007c14cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c14cc.md) → [`007c14cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c14cc.md) FUN_007c14cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`007c17bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c17bc.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007c17bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c17bc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.09% / 新版 96.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007c1590",
      "incomplete_value": true,
      "site": "007c15a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:272:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c1590",
      "incomplete_value": true,
      "site": "007c15a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:279:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c15bc",
      "incomplete_value": false,
      "site": "007c15c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c15bc",
      "incomplete_value": false,
      "site": "007c15c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
      "007c1590",
      "READ",
      [
        "storage",
        "002a4279",
        null,
        "string"
      ]
    ],
    [
      "007c15c4",
      "DATA",
      [
        "storage",
        "00bfd370",
        null,
        "undefined *"
      ]
    ],
    [
      "007c1628",
      "READ",
      [
        "storage",
        "00bfd390",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007c1590",
      "READ",
      [
        "storage",
        "002a4272",
        null,
        "string"
      ]
    ],
    [
      "007c15c4",
      "DATA",
      [
        "storage",
        "00bfd420",
        null,
        "undefined *"
      ]
    ],
    [
      "007c1628",
      "READ",
      [
        "storage",
        "00bfd440",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c1588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c14cc.md#insn-007c1588) · [`007c15bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c14cc.md#insn-007c15bc)
- 新版 `007c1588`（命令位置の公開資料なし） · `007c15bc`（命令位置の公開資料なし）

~~~diff
- 007c1588 ["COPY", "tmp:0:8", ["const:279:8"]]
- 007c1588 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c1588 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c1588 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c1588 ["COPY", "tmp:0:8", ["const:272:8"]]
+ 007c1588 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c1588 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c1588 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c1588 bytes 29e50991
+ 007c1588 bytes 29c90991
- 007c15bc ["COPY", "tmp:0:8", ["const:370:8"]]
- 007c15bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c15bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c15bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c15bc ["COPY", "tmp:0:8", ["const:420:8"]]
+ 007c15bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c15bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c15bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c15bc bytes 08c10d91
+ 007c15bc bytes 08811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3de9ed22f609a3e82f8f1a5296e5e1d0"></a>

### [`007c1788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1788.md) → [`007c1788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1788.md) FUN_007c1788

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c179c",
      "incomplete_value": false,
      "site": "007c17a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c179c",
      "incomplete_value": false,
      "site": "007c17a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
      "007c17a0",
      "DATA",
      [
        "storage",
        "00bfd370",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c17a0",
      "DATA",
      [
        "storage",
        "00bfd420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c179c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1788.md#insn-007c179c)
- 新版 `007c179c`（命令位置の公開資料なし）

~~~diff
- 007c179c ["COPY", "tmp:0:8", ["const:370:8"]]
- 007c179c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c179c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c179c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c179c ["COPY", "tmp:0:8", ["const:420:8"]]
+ 007c179c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c179c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c179c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c179c bytes 08c10d91
+ 007c179c bytes 08811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9938c6a395a8a2de7e8e9f380683f713"></a>

### [`007c17ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c17ac.md) → [`007c17ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c17ac.md) FUN_007c17ac

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
      "definition_site": "007c17b0",
      "incomplete_value": false,
      "site": "007c17b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c17b0",
      "incomplete_value": false,
      "site": "007c17b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
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
      "007c17b4",
      "DATA",
      [
        "storage",
        "00bfd370",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c17b4",
      "DATA",
      [
        "storage",
        "00bfd420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c17b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c17ac.md#insn-007c17b0)
- 新版 `007c17b0`（命令位置の公開資料なし）

~~~diff
- 007c17b0 ["COPY", "tmp:0:8", ["const:370:8"]]
- 007c17b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c17b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c17b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c17b0 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 007c17b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c17b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c17b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c17b0 bytes 08c10d91
+ 007c17b0 bytes 08811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-684e2f04a097db44c0f8430d62d97c11"></a>

### [`007c1808`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1808.md) → [`007c1808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1808.md) FUN_007c1808

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c182c",
      "incomplete_value": false,
      "site": "007c182c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c182c",
      "incomplete_value": false,
      "site": "007c182c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:400:8"
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
      "007c182c",
      "DATA",
      [
        "storage",
        "00bfd400",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c182c",
      "DATA",
      [
        "storage",
        "00bfd4b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c1828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1808.md#insn-007c1828)
- 新版 `007c1828`（命令位置の公開資料なし）

~~~diff
- 007c1828 ["COPY", "tmp:0:8", ["const:400:8"]]
- 007c1828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c1828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c1828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c1828 ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 007c1828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c1828 bytes 08011091
+ 007c1828 bytes 08c11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-382e5ceb2ddf720137fc2fba539fb655"></a>

### [`007c183c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c183c.md) → [`007c183c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c183c.md) FUN_007c183c

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
      "definition_site": "007c1848",
      "incomplete_value": false,
      "site": "007c1848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c1848",
      "incomplete_value": false,
      "site": "007c1848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:400:8"
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
      "007c1848",
      "DATA",
      [
        "storage",
        "00bfd400",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c1848",
      "DATA",
      [
        "storage",
        "00bfd4b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c1844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c183c.md#insn-007c1844)
- 新版 `007c1844`（命令位置の公開資料なし）

~~~diff
- 007c1844 ["COPY", "tmp:0:8", ["const:400:8"]]
- 007c1844 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c1844 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c1844 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c1844 ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 007c1844 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c1844 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c1844 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c1844 bytes 29011091
+ 007c1844 bytes 29c11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b96abc83511b99f281029d6dbaeac0a3"></a>

### [`007c1858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1858.md) → [`007c1858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1858.md) FUN_007c1858

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 15件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c19d0",
      "incomplete_value": false,
      "site": "007c19d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c19d0",
      "incomplete_value": false,
      "site": "007c19d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:470:8"
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
      "definition_site": "007c1ab0",
      "incomplete_value": false,
      "site": "007c1ab4",
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
    "old": {
      "definition_site": "007c1ab0",
      "incomplete_value": false,
      "site": "007c1ab4",
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
            "const:5d6:8"
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
      "007c195c",
      "READ",
      [
        "storage",
        "0029e7d3",
        null,
        "string"
      ]
    ],
    [
      "007c1960",
      "READ",
      [
        "storage",
        "0029e7e0",
        null,
        "string"
      ]
    ],
    [
      "007c19d0",
      "DATA",
      [
        "storage",
        "00bfd470",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c195c",
      "READ",
      [
        "storage",
        "0029e860",
        null,
        "string"
      ]
    ],
    [
      "007c1960",
      "READ",
      [
        "storage",
        "0029e86d",
        null,
        "string"
      ]
    ],
    [
      "007c19d0",
      "DATA",
      [
        "storage",
        "00bfd520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c18f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1858.md#insn-007c18f0) · [`007c19c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1858.md#insn-007c19c8) · [`007c19cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1858.md#insn-007c19cc)
- 新版 `007c18f0`（命令位置の公開資料なし） · `007c19c8`（命令位置の公開資料なし）

~~~diff
- 007c18f0 ["COPY", "tmp:0:8", ["const:7d3:8"]]
- 007c18f0 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 007c18f0 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 007c18f0 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 007c18f0 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 007c18f0 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 007c18f0 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 007c18f0 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 007c18f0 bytes d64e1f91
+ 007c18f0 bytes d6822191
- 007c19c8 ["COPY", "tmp:0:8", ["const:470:8"]]
- 007c19c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c19c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c19c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c19c8 ["COPY", "tmp:0:8", ["const:520:8"]]
+ 007c19c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c19c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c19c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c19c8 bytes 08c11191
+ 007c19c8 bytes 08811491
- 007c19cc ["INT_SUB", "register:4098:8", ["register:40e8:8", "const:40:8"]]
- 007c19cc bytes b30301d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5a8fa9e167e26562558f3eedf9e16f9"></a>

### [`007c1ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1ba0.md) → [`007c1ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1ba0.md) FUN_007c1ba0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c1bb4",
      "incomplete_value": false,
      "site": "007c1bb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c1bb4",
      "incomplete_value": false,
      "site": "007c1bb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:470:8"
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
      "007c1bb8",
      "DATA",
      [
        "storage",
        "00bfd470",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c1bb8",
      "DATA",
      [
        "storage",
        "00bfd520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c1bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1ba0.md#insn-007c1bb4)
- 新版 `007c1bb4`（命令位置の公開資料なし）

~~~diff
- 007c1bb4 ["COPY", "tmp:0:8", ["const:470:8"]]
- 007c1bb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c1bb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c1bb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c1bb4 ["COPY", "tmp:0:8", ["const:520:8"]]
+ 007c1bb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1bb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1bb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c1bb4 bytes 08c11191
+ 007c1bb4 bytes 08811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96c1c4e70605c663988841e41b56c6ab"></a>

### [`007c1bc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1bc4.md) → [`007c1bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1bc4.md) FUN_007c1bc4

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
      "definition_site": "007c1bc8",
      "incomplete_value": false,
      "site": "007c1bcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c1bc8",
      "incomplete_value": false,
      "site": "007c1bcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
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
      "007c1bcc",
      "DATA",
      [
        "storage",
        "00bfd470",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c1bcc",
      "DATA",
      [
        "storage",
        "00bfd520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c1bc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1bc4.md#insn-007c1bc8)
- 新版 `007c1bc8`（命令位置の公開資料なし）

~~~diff
- 007c1bc8 ["COPY", "tmp:0:8", ["const:470:8"]]
- 007c1bc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c1bc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c1bc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c1bc8 ["COPY", "tmp:0:8", ["const:520:8"]]
+ 007c1bc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1bc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1bc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c1bc8 bytes 08c11191
+ 007c1bc8 bytes 08811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f88c10798e298dafb06461b6080253b"></a>

### [`007c1c70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1c70.md) → [`007c1c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1c70.md) FUN_007c1c70

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078c/0078cd14.md) · 呼出先 10件 [`006ad590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad590.md) [`006ad854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad854.md) [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`006ad8e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8e8.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md)
- 新版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) · 呼出先 10件 [`006ad590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad590.md) [`006ad854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad854.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`006ad8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8e8.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.48% / 新版 99.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007c1f30",
      "incomplete_value": false,
      "site": "007c1f34",
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
            "const:23:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c1f30",
      "incomplete_value": false,
      "site": "007c1f34",
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
            "const:f96:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007c1f30",
      "PARAM",
      [
        "storage",
        "00299f96",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007c1f30",
      "PARAM",
      [
        "storage",
        "0029a023",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c1f2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1c70.md#insn-007c1f2c) · [`007c1f30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1c70.md#insn-007c1f30)
- 新版 `007c1f2c`（命令位置の公開資料なし） · `007c1f30`（命令位置の公開資料なし）

~~~diff
- 007c1f2c ["COPY", "register:4000:8", ["const:299000:8"]]
+ 007c1f2c ["COPY", "register:4000:8", ["const:29a000:8"]]
- 007c1f2c bytes c0d6ff90
+ 007c1f2c bytes c0d6ffb0
- 007c1f30 ["COPY", "tmp:0:8", ["const:f96:8"]]
- 007c1f30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007c1f30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007c1f30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007c1f30 ["COPY", "tmp:0:8", ["const:23:8"]]
+ 007c1f30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007c1f30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007c1f30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007c1f30 bytes 00583e91
+ 007c1f30 bytes 008c0091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd859cfab768b61a601bd30812e03796"></a>

### [`007c1f74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1f74.md) → [`007c1f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1f74.md) FUN_007c1f74

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078c/0078cd14.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`006ad854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad854.md) [`006add94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006add94.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`006ad854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad854.md) [`006add94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006add94.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.59% / 新版 99.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007c231c",
      "incomplete_value": false,
      "site": "007c2320",
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
            "const:f2f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c231c",
      "incomplete_value": false,
      "site": "007c2320",
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
            "const:ea2:8"
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
      "007c231c",
      "PARAM",
      [
        "storage",
        "00297ea2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007c231c",
      "PARAM",
      [
        "storage",
        "00297f2f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c231c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1f74.md#insn-007c231c)
- 新版 `007c231c`（命令位置の公開資料なし）

~~~diff
- 007c231c ["COPY", "tmp:0:8", ["const:ea2:8"]]
- 007c231c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007c231c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007c231c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007c231c ["COPY", "tmp:0:8", ["const:f2f:8"]]
+ 007c231c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007c231c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007c231c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007c231c bytes 00883a91
+ 007c231c bytes 00bc3c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b5aca4d595ce0522e4432b585edc273"></a>

### [`007c238c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c2/007c238c.md) → [`007c238c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c238c.md) FUN_007c238c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c23b0",
      "incomplete_value": false,
      "site": "007c23b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c23b0",
      "incomplete_value": false,
      "site": "007c23b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:578:8"
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
      "007c23b0",
      "DATA",
      [
        "storage",
        "00bfd578",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c23b0",
      "DATA",
      [
        "storage",
        "00bfd628",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c23ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c2/007c238c.md#insn-007c23ac)
- 新版 `007c23ac`（命令位置の公開資料なし）

~~~diff
- 007c23ac ["COPY", "tmp:0:8", ["const:578:8"]]
- 007c23ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c23ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c23ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c23ac ["COPY", "tmp:0:8", ["const:628:8"]]
+ 007c23ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c23ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c23ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c23ac bytes 08e11591
+ 007c23ac bytes 08a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22e8712df0f9e282446a7a1fd44a3ddf"></a>

### [`007c248c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c2/007c248c.md) → [`007c248c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c248c.md) FUN_007c248c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c24b0",
      "incomplete_value": false,
      "site": "007c24b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c24b0",
      "incomplete_value": false,
      "site": "007c24b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
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
      "007c24b0",
      "DATA",
      [
        "storage",
        "00bfd5f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c24b0",
      "DATA",
      [
        "storage",
        "00bfd6a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c24ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c2/007c248c.md#insn-007c24ac)
- 新版 `007c24ac`（命令位置の公開資料なし）

~~~diff
- 007c24ac ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 007c24ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c24ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c24ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c24ac ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 007c24ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c24ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c24ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c24ac bytes 08e11791
+ 007c24ac bytes 08a11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f71ef805663b9bf4e11eba9388543e16"></a>

### [`007c2574`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c2/007c2574.md) → [`007c2574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c2574.md) FUN_007c2574

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c2598",
      "incomplete_value": false,
      "site": "007c2598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c2598",
      "incomplete_value": false,
      "site": "007c2598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:678:8"
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
      "007c2598",
      "DATA",
      [
        "storage",
        "00bfd678",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c2598",
      "DATA",
      [
        "storage",
        "00bfd728",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c2594`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c2/007c2574.md#insn-007c2594)
- 新版 `007c2594`（命令位置の公開資料なし）

~~~diff
- 007c2594 ["COPY", "tmp:0:8", ["const:678:8"]]
- 007c2594 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c2594 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c2594 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c2594 ["COPY", "tmp:0:8", ["const:728:8"]]
+ 007c2594 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c2594 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c2594 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c2594 bytes 08e11991
+ 007c2594 bytes 08a11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f06cb1bc7b2c7b4bdc5186e16020090c"></a>

### [`007c267c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c2/007c267c.md) → [`007c267c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c267c.md) FUN_007c267c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c26a0",
      "incomplete_value": false,
      "site": "007c26a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c26a0",
      "incomplete_value": false,
      "site": "007c26a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
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
      "007c26a0",
      "DATA",
      [
        "storage",
        "00bfd6f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c26a0",
      "DATA",
      [
        "storage",
        "00bfd7a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c269c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c2/007c267c.md#insn-007c269c)
- 新版 `007c269c`（命令位置の公開資料なし）

~~~diff
- 007c269c ["COPY", "tmp:0:8", ["const:6f8:8"]]
- 007c269c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c269c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c269c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c269c ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 007c269c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c269c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c269c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c269c bytes 08e11b91
+ 007c269c bytes 08a11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b87d144056881914b1bf58c1f3cf8a51"></a>

### [`007c27e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c2/007c27e8.md) → [`007c27e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c27e8.md) FUN_007c27e8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c280c",
      "incomplete_value": false,
      "site": "007c280c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c280c",
      "incomplete_value": false,
      "site": "007c280c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
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
      "007c280c",
      "DATA",
      [
        "storage",
        "00bfd778",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c280c",
      "DATA",
      [
        "storage",
        "00bfd828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c2808`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c2/007c27e8.md#insn-007c2808)
- 新版 `007c2808`（命令位置の公開資料なし）

~~~diff
- 007c2808 ["COPY", "tmp:0:8", ["const:778:8"]]
- 007c2808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c2808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c2808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c2808 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 007c2808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c2808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c2808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c2808 bytes 08e11d91
+ 007c2808 bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29c2e59f11c8f629d21c9fc4579a5bb1"></a>

### [`007c28b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c2/007c28b0.md) → [`007c28b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c28b0.md) FUN_007c28b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c28d4",
      "incomplete_value": false,
      "site": "007c28d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c28d4",
      "incomplete_value": false,
      "site": "007c28d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "007c28d8",
      "DATA",
      [
        "storage",
        "00bfd7f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c28d8",
      "DATA",
      [
        "storage",
        "00bfd8a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c28d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c2/007c28b0.md#insn-007c28d4)
- 新版 `007c28d4`（命令位置の公開資料なし）

~~~diff
- 007c28d4 ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 007c28d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c28d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c28d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c28d4 ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 007c28d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c28d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c28d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c28d4 bytes 08e11f91
+ 007c28d4 bytes 08a12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1eaea77e2dc4072725af26db8415c6e1"></a>

### [`007c2918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c2/007c2918.md) → [`007c2918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c2918.md) FUN_007c2918

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 20件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 20件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.94% / 新版 95.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007c2a1c",
      "incomplete_value": true,
      "site": "007c2a2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8be:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c2a1c",
      "incomplete_value": true,
      "site": "007c2a2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:831:8"
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
      "definition_site": "007c2a20",
      "incomplete_value": true,
      "site": "007c2a30",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007c2a20",
      "incomplete_value": true,
      "site": "007c2a30",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007c2c28",
      "incomplete_value": true,
      "site": "007c2c28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b11:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c2c28",
      "incomplete_value": true,
      "site": "007c2c28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a84:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007c2a1c",
      "READ",
      [
        "storage",
        "0029b831",
        null,
        "string"
      ]
    ],
    [
      "007c2a20",
      "READ",
      [
        "storage",
        "0029b841",
        null,
        "string"
      ]
    ],
    [
      "007c2c14",
      "READ",
      [
        "storage",
        "00293a84",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007c2a1c",
      "READ",
      [
        "storage",
        "0029b8be",
        null,
        "string"
      ]
    ],
    [
      "007c2a20",
      "READ",
      [
        "storage",
        "0029b8ce",
        null,
        "string"
      ]
    ],
    [
      "007c2c14",
      "READ",
      [
        "storage",
        "00293b11",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c2a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c2/007c2918.md#insn-007c2a14) · [`007c2a18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c2/007c2918.md#insn-007c2a18)
- 新版 `007c2a14`（命令位置の公開資料なし） · `007c2a18`（命令位置の公開資料なし）

~~~diff
- 007c2a14 ["COPY", "tmp:0:8", ["const:831:8"]]
- 007c2a14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c2a14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c2a14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c2a14 ["COPY", "tmp:0:8", ["const:8be:8"]]
+ 007c2a14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c2a14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c2a14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c2a14 bytes 08c52091
+ 007c2a14 bytes 08f92291
- 007c2a18 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 007c2a18 bytes 69d7ffd0
+ 007c2a18 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 007c2a18 bytes 69d7ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-214f28cf08ad286198a3fa6062cf778a"></a>

### [`007c2ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c2/007c2ff8.md) → [`007c2ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c2ff8.md) FUN_007c2ff8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c3018",
      "incomplete_value": false,
      "site": "007c301c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3018",
      "incomplete_value": false,
      "site": "007c301c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:868:8"
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
      "007c301c",
      "DATA",
      [
        "storage",
        "00bfd868",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c301c",
      "DATA",
      [
        "storage",
        "00bfd918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c2/007c2ff8.md#insn-007c3018)
- 新版 `007c3018`（命令位置の公開資料なし）

~~~diff
- 007c3018 ["COPY", "tmp:0:8", ["const:868:8"]]
- 007c3018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c3018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c3018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c3018 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 007c3018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c3018 bytes 08a12191
+ 007c3018 bytes 08612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c84259c428089ed4f9b6d19df1e14808"></a>

### [`007c3030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3030.md) → [`007c3030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3030.md) FUN_007c3030

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
      "definition_site": "007c3034",
      "incomplete_value": false,
      "site": "007c3038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3034",
      "incomplete_value": false,
      "site": "007c3038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:868:8"
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
      "007c3038",
      "DATA",
      [
        "storage",
        "00bfd868",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c3038",
      "DATA",
      [
        "storage",
        "00bfd918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3030.md#insn-007c3034)
- 新版 `007c3034`（命令位置の公開資料なし）

~~~diff
- 007c3034 ["COPY", "tmp:0:8", ["const:868:8"]]
- 007c3034 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c3034 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c3034 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c3034 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 007c3034 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3034 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3034 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c3034 bytes 08a12191
+ 007c3034 bytes 08612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

