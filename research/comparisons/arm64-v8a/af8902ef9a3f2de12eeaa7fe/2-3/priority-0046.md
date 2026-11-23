# v16.0.0 → v16.0.1 · 最優先の変更候補 (46)

[一覧の目次](README.md)

<a id="compare-9e3e9d9e5c1797cab1270c097a29f809"></a>

### [`00882444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882444.md) → [`00882484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882484.md) FUN_00882484

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0088249c",
      "incomplete_value": false,
      "site": "008824a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088245c",
      "incomplete_value": false,
      "site": "00882468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:318:8"
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
      "008824a8",
      "DATA",
      [
        "storage",
        "00c80318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008824a8",
      "DATA",
      [
        "storage",
        "00c80718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088245c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882444.md#insn-0088245c) · [`0088248c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882444.md#insn-0088248c)
- 新版 `0088249c`（命令位置の公開資料なし） · `008824cc`（命令位置の公開資料なし）

~~~diff
- 0088245c ["COPY", "tmp:0:8", ["const:318:8"]]
- 0088245c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088245c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088245c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088249c ["COPY", "tmp:0:8", ["const:718:8"]]
+ 0088249c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088249c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088249c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088245c bytes 08610c91
+ 0088249c bytes 08611c91
- 0088248c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088248c ["INT_ADD", "register:40f0:8", ["const:88248c:8", "const:4:8"]]
- 0088248c ["CALLIND", null, ["register:0:8"]]
+ 008824cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008824cc ["INT_ADD", "register:40f0:8", ["const:8824cc:8", "const:4:8"]]
+ 008824cc ["CALLIND", null, ["register:0:8"]]
- 0088248c bytes 00013fd6
+ 008824cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf1eb9a32affa48f8360c837fa59c6a6"></a>

### [`008824a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/008824a0.md) → [`008824e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008824e0.md) FUN_008824e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0088250c",
      "incomplete_value": false,
      "site": "0088250c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008824cc",
      "incomplete_value": false,
      "site": "008824cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:318:8"
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
      "0088250c",
      "DATA",
      [
        "storage",
        "00c80318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088250c",
      "DATA",
      [
        "storage",
        "00c80718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008824b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/008824a0.md#insn-008824b4) · [`008824c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/008824a0.md#insn-008824c4) · [`008824e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/008824a0.md#insn-008824e8)
- 新版 `008824f4`（命令位置の公開資料なし） · `00882504`（命令位置の公開資料なし） · `00882528`（命令位置の公開資料なし）

~~~diff
- 008824b4 ["INT_ADD", "register:40f0:8", ["const:8824b4:8", "const:4:8"]]
- 008824b4 ["CALL", null, ["callee:00c57e90:8"]]
+ 008824f4 ["INT_ADD", "register:40f0:8", ["const:8824f4:8", "const:4:8"]]
+ 008824f4 ["CALL", null, ["callee:00c57e90:8"]]
- 008824b4 bytes 77550f94
+ 008824f4 bytes 67560f94
- 008824c4 ["COPY", "tmp:0:8", ["const:318:8"]]
- 008824c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008824c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008824c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00882504 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 00882504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00882504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00882504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008824c4 bytes 08610c91
+ 00882504 bytes 08611c91
- 008824e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008824e8 ["INT_ADD", "register:40f0:8", ["const:8824e8:8", "const:4:8"]]
- 008824e8 ["CALLIND", null, ["register:0:8"]]
+ 00882528 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00882528 ["INT_ADD", "register:40f0:8", ["const:882528:8", "const:4:8"]]
+ 00882528 ["CALLIND", null, ["register:0:8"]]
- 008824e8 bytes 00013fd6
+ 00882528 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1febb8d209a2db0e8294db03bb70726a"></a>

### [`00882528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882528.md) → [`00882568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882568.md) FUN_00882568

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00882584",
      "incomplete_value": false,
      "site": "00882584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882544",
      "incomplete_value": false,
      "site": "00882544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:318:8"
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
      "00882584",
      "DATA",
      [
        "storage",
        "00c80318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882584",
      "DATA",
      [
        "storage",
        "00c80718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882528.md#insn-00882540) · [`00882564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882528.md#insn-00882564)
- 新版 `00882580`（命令位置の公開資料なし） · `008825a4`（命令位置の公開資料なし）

~~~diff
- 00882540 ["COPY", "tmp:0:8", ["const:318:8"]]
- 00882540 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00882540 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00882540 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00882580 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 00882580 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00882580 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00882580 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00882540 bytes 29610c91
+ 00882580 bytes 29611c91
- 00882564 ["COPY", "register:0:8", ["register:4048:8"]]
- 00882564 ["INT_ADD", "register:40f0:8", ["const:882564:8", "const:4:8"]]
- 00882564 ["CALLIND", null, ["register:0:8"]]
+ 008825a4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 008825a4 ["INT_ADD", "register:40f0:8", ["const:8825a4:8", "const:4:8"]]
+ 008825a4 ["CALLIND", null, ["register:0:8"]]
- 00882564 bytes 20013fd6
+ 008825a4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e675c2d94b362644815e9ea8eedb7c6"></a>

### [`00882668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882668.md) → [`008826a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008826a8.md) FUN_008826a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "008826bc",
      "incomplete_value": false,
      "site": "008826c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088267c",
      "incomplete_value": false,
      "site": "00882680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:398:8"
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
      "008826c0",
      "DATA",
      [
        "storage",
        "00c80398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008826c0",
      "DATA",
      [
        "storage",
        "00c80798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882668.md#insn-00882674) · [`0088267c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882668.md#insn-0088267c)
- 新版 `008826b4`（命令位置の公開資料なし） · `008826bc`（命令位置の公開資料なし）

~~~diff
- 00882674 ["INT_ADD", "register:40f0:8", ["const:882674:8", "const:4:8"]]
- 00882674 ["CALL", null, ["callee:00c57e90:8"]]
+ 008826b4 ["INT_ADD", "register:40f0:8", ["const:8826b4:8", "const:4:8"]]
+ 008826b4 ["CALL", null, ["callee:00c57e90:8"]]
- 00882674 bytes 07550f94
+ 008826b4 bytes f7550f94
- 0088267c ["COPY", "tmp:0:8", ["const:398:8"]]
- 0088267c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088267c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088267c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008826bc ["COPY", "tmp:0:8", ["const:798:8"]]
+ 008826bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008826bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008826bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088267c bytes 08610e91
+ 008826bc bytes 08611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc539dafaa4c7dca5015a042f42347a9"></a>

### [`0088268c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/0088268c.md) → [`008826cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008826cc.md) FUN_008826cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008826d0",
      "incomplete_value": false,
      "site": "008826d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882690",
      "incomplete_value": false,
      "site": "00882694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:398:8"
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
      "008826d4",
      "DATA",
      [
        "storage",
        "00c80398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008826d4",
      "DATA",
      [
        "storage",
        "00c80798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/0088268c.md#insn-00882690)
- 新版 `008826d0`（命令位置の公開資料なし）

~~~diff
- 00882690 ["COPY", "tmp:0:8", ["const:398:8"]]
- 00882690 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00882690 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00882690 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008826d0 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 008826d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008826d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008826d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00882690 bytes 08610e91
+ 008826d0 bytes 08611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fead15d4208b21387a89f1a5aa006062"></a>

### [`008826a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/008826a4.md) → [`008826e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008826e4.md) FUN_008826e4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ee8.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492f28.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.35% / 新版 91.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00882720",
      "incomplete_value": true,
      "site": "00882728",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:240:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008826e0",
      "incomplete_value": true,
      "site": "008826e8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088271c",
      "incomplete_value": true,
      "site": "0088272c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:70a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008826dc",
      "incomplete_value": true,
      "site": "008826ec",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:6ca:8"
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
      "definition_site": "0088271c",
      "incomplete_value": true,
      "site": "0088272c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "008826dc",
      "incomplete_value": true,
      "site": "008826ec",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00882700",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "0088271c",
      "READ",
      [
        "storage",
        "002b66ca",
        null,
        "string"
      ]
    ],
    [
      "0088271c",
      "READ",
      [
        "storage",
        "002b66da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00882700",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0088271c",
      "READ",
      [
        "storage",
        "002b670a",
        null,
        "string"
      ]
    ],
    [
      "0088271c",
      "READ",
      [
        "storage",
        "002b671a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008826c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/008826a4.md#insn-008826c0) · [`008826cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/008826a4.md#insn-008826cc) · [`008826d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/008826a4.md#insn-008826d4)
- 新版 `00882700`（命令位置の公開資料なし） · `0088270c`（命令位置の公開資料なし） · `00882714`（命令位置の公開資料なし）

~~~diff
- 008826c0 ["INT_ADD", "register:40f0:8", ["const:8826c0:8", "const:4:8"]]
- 008826c0 ["CALL", null, ["ram:48ccb8:8"]]
+ 00882700 ["INT_ADD", "register:40f0:8", ["const:882700:8", "const:4:8"]]
+ 00882700 ["CALL", null, ["ram:48ccf8:8"]]
- 008826c0 bytes 7e29f097
+ 00882700 bytes 7e29f097
- 008826cc ["INT_ADD", "register:40f0:8", ["const:8826cc:8", "const:4:8"]]
- 008826cc ["CALL", null, ["callee:00c57e90:8"]]
+ 0088270c ["INT_ADD", "register:40f0:8", ["const:88270c:8", "const:4:8"]]
+ 0088270c ["CALL", null, ["callee:00c57e90:8"]]
- 008826cc bytes f1540f94
+ 0088270c bytes e1550f94
- 008826d4 ["COPY", "tmp:0:8", ["const:6ca:8"]]
- 008826d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008826d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008826d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00882714 ["COPY", "tmp:0:8", ["const:70a:8"]]
+ 00882714 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00882714 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00882714 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008826d4 bytes 08291b91
+ 00882714 bytes 08291c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7923578156f862a0dd1d74df9d9dc320"></a>

### [`00882924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882924.md) → [`00882964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882964.md) FUN_00882964

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00882978",
      "incomplete_value": false,
      "site": "0088297c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882938",
      "incomplete_value": false,
      "site": "0088293c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:418:8"
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
      "0088297c",
      "DATA",
      [
        "storage",
        "00c80418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088297c",
      "DATA",
      [
        "storage",
        "00c80818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882924.md#insn-00882930) · [`00882938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882924.md#insn-00882938)
- 新版 `00882970`（命令位置の公開資料なし） · `00882978`（命令位置の公開資料なし）

~~~diff
- 00882930 ["INT_ADD", "register:40f0:8", ["const:882930:8", "const:4:8"]]
- 00882930 ["CALL", null, ["callee:00c57e90:8"]]
+ 00882970 ["INT_ADD", "register:40f0:8", ["const:882970:8", "const:4:8"]]
+ 00882970 ["CALL", null, ["callee:00c57e90:8"]]
- 00882930 bytes 58540f94
+ 00882970 bytes 48550f94
- 00882938 ["COPY", "tmp:0:8", ["const:418:8"]]
- 00882938 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00882938 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00882938 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00882978 ["COPY", "tmp:0:8", ["const:818:8"]]
+ 00882978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00882978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00882978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00882938 bytes 08611091
+ 00882978 bytes 08612091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7aa6da259c1d907ca5ade405021843e"></a>

### [`00882948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882948.md) → [`00882988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882988.md) FUN_00882988

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088298c",
      "incomplete_value": false,
      "site": "00882990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088294c",
      "incomplete_value": false,
      "site": "00882950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:418:8"
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
      "00882990",
      "DATA",
      [
        "storage",
        "00c80418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882990",
      "DATA",
      [
        "storage",
        "00c80818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088294c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882948.md#insn-0088294c)
- 新版 `0088298c`（命令位置の公開資料なし）

~~~diff
- 0088294c ["COPY", "tmp:0:8", ["const:418:8"]]
- 0088294c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088294c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088294c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088298c ["COPY", "tmp:0:8", ["const:818:8"]]
+ 0088298c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088298c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088298c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088294c bytes 08611091
+ 0088298c bytes 08612091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b99003061ada01fc9f3221b88c00b9c6"></a>

### [`00882960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882960.md) → [`008829a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008829a0.md) FUN_008829a0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ee8.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492f28.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.35% / 新版 91.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008829dc",
      "incomplete_value": true,
      "site": "008829e4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:240:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088299c",
      "incomplete_value": true,
      "site": "008829a4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008829d8",
      "incomplete_value": true,
      "site": "008829e8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:551:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882998",
      "incomplete_value": true,
      "site": "008829a8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:511:8"
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
      "definition_site": "008829d8",
      "incomplete_value": true,
      "site": "008829e8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00882998",
      "incomplete_value": true,
      "site": "008829a8",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008829bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "008829d8",
      "READ",
      [
        "storage",
        "002b9511",
        null,
        "string"
      ]
    ],
    [
      "008829d8",
      "READ",
      [
        "storage",
        "002b9521",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008829bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "008829d8",
      "READ",
      [
        "storage",
        "002b9551",
        null,
        "string"
      ]
    ],
    [
      "008829d8",
      "READ",
      [
        "storage",
        "002b9561",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088297c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882960.md#insn-0088297c) · [`00882988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882960.md#insn-00882988) · [`00882990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882960.md#insn-00882990)
- 新版 `008829bc`（命令位置の公開資料なし） · `008829c8`（命令位置の公開資料なし） · `008829d0`（命令位置の公開資料なし）

~~~diff
- 0088297c ["INT_ADD", "register:40f0:8", ["const:88297c:8", "const:4:8"]]
- 0088297c ["CALL", null, ["ram:48ccb8:8"]]
+ 008829bc ["INT_ADD", "register:40f0:8", ["const:8829bc:8", "const:4:8"]]
+ 008829bc ["CALL", null, ["ram:48ccf8:8"]]
- 0088297c bytes cf28f097
+ 008829bc bytes cf28f097
- 00882988 ["INT_ADD", "register:40f0:8", ["const:882988:8", "const:4:8"]]
- 00882988 ["CALL", null, ["callee:00c57e90:8"]]
+ 008829c8 ["INT_ADD", "register:40f0:8", ["const:8829c8:8", "const:4:8"]]
+ 008829c8 ["CALL", null, ["callee:00c57e90:8"]]
- 00882988 bytes 42540f94
+ 008829c8 bytes 32550f94
- 00882990 ["COPY", "tmp:0:8", ["const:511:8"]]
- 00882990 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00882990 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00882990 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008829d0 ["COPY", "tmp:0:8", ["const:551:8"]]
+ 008829d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008829d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008829d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00882990 bytes 08451491
+ 008829d0 bytes 08451591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-663a3791db95deb4c9348e9f113ff360"></a>

### [`00882bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882bdc.md) → [`00882c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882c1c.md) FUN_00882c1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00882c24",
      "incomplete_value": false,
      "site": "00882c28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882be4",
      "incomplete_value": false,
      "site": "00882be8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "00882c28",
      "DATA",
      [
        "storage",
        "00c80498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882c28",
      "DATA",
      [
        "storage",
        "00c80898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882bdc.md#insn-00882be4)
- 新版 `00882c24`（命令位置の公開資料なし）

~~~diff
- 00882be4 ["COPY", "tmp:0:8", ["const:498:8"]]
- 00882be4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00882be4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00882be4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00882c24 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00882c24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00882c24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00882c24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00882be4 bytes 29611291
+ 00882c24 bytes 29612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-208d70d32b06f62fa99f937ab9f3e254"></a>

### [`00882bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882bfc.md) → [`00882c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882c3c.md) FUN_00882c3c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00882c44",
      "incomplete_value": false,
      "site": "00882c48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882c04",
      "incomplete_value": false,
      "site": "00882c08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "00882c48",
      "DATA",
      [
        "storage",
        "00c80498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882c48",
      "DATA",
      [
        "storage",
        "00c80898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882bfc.md#insn-00882c04) · [`00882c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882bfc.md#insn-00882c28)
- 新版 `00882c44`（命令位置の公開資料なし） · `00882c68`（命令位置の公開資料なし）

~~~diff
- 00882c04 ["COPY", "tmp:0:8", ["const:498:8"]]
- 00882c04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00882c04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00882c04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00882c44 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00882c44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00882c44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00882c44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00882c04 bytes 29611291
+ 00882c44 bytes 29612291
- 00882c28 ["INT_ADD", "register:40f0:8", ["const:882c28:8", "const:4:8"]]
- 00882c28 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00882c68 ["INT_ADD", "register:40f0:8", ["const:882c68:8", "const:4:8"]]
+ 00882c68 ["CALL", null, ["callee:00c57eb0:8"]]
- 00882c28 bytes a2530f94
+ 00882c68 bytes 92540f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6beac7ba8bae8b6c950feb041be6715c"></a>

### [`00882c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882c3c.md) → [`00882c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882c7c.md) FUN_00882c7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00882ca8",
      "incomplete_value": false,
      "site": "00882ca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882c68",
      "incomplete_value": false,
      "site": "00882c68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "00882ca8",
      "DATA",
      [
        "storage",
        "00c80498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882ca8",
      "DATA",
      [
        "storage",
        "00c80898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882c3c.md#insn-00882c50) · [`00882c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882c3c.md#insn-00882c60) · [`00882c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882c3c.md#insn-00882c88)
- 新版 `00882c90`（命令位置の公開資料なし） · `00882ca0`（命令位置の公開資料なし） · `00882cc8`（命令位置の公開資料なし）

~~~diff
- 00882c50 ["INT_ADD", "register:40f0:8", ["const:882c50:8", "const:4:8"]]
- 00882c50 ["CALL", null, ["callee:00c57e90:8"]]
+ 00882c90 ["INT_ADD", "register:40f0:8", ["const:882c90:8", "const:4:8"]]
+ 00882c90 ["CALL", null, ["callee:00c57e90:8"]]
- 00882c50 bytes 90530f94
+ 00882c90 bytes 80540f94
- 00882c60 ["COPY", "tmp:0:8", ["const:498:8"]]
- 00882c60 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00882c60 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00882c60 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00882ca0 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00882ca0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00882ca0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00882ca0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00882c60 bytes 4a611291
+ 00882ca0 bytes 4a612291
- 00882c88 ["INT_ADD", "register:40f0:8", ["const:882c88:8", "const:4:8"]]
- 00882c88 ["CALL", null, ["callee:0043bb20:8"]]
+ 00882cc8 ["INT_ADD", "register:40f0:8", ["const:882cc8:8", "const:4:8"]]
+ 00882cc8 ["CALL", null, ["callee:0043bb20:8"]]
- 00882c88 bytes 96e3ee97
+ 00882cc8 bytes 96e3ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eac6a67e663444da44689f9eedae278c"></a>

### [`00882cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882cb0.md) → [`00882cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882cf0.md) FUN_00882cf0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00882cf8",
      "incomplete_value": false,
      "site": "00882cf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882cb8",
      "incomplete_value": false,
      "site": "00882cb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "00882cf8",
      "DATA",
      [
        "storage",
        "00c80498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882cf8",
      "DATA",
      [
        "storage",
        "00c80898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882cb0.md#insn-00882cb4)
- 新版 `00882cf4`（命令位置の公開資料なし）

~~~diff
- 00882cb4 ["COPY", "tmp:0:8", ["const:498:8"]]
- 00882cb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00882cb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00882cb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00882cf4 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00882cf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00882cf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00882cf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00882cb4 bytes 08611291
+ 00882cf4 bytes 08612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a1df53f8c904c08b3236ddf3f3dfe76"></a>

### [`00882d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882d34.md) → [`00882d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882d74.md) FUN_00882d74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ee8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492f28.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.77% / 新版 96.77%

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
      "site": "00882d98",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00882d58",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "00882d98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "00882d98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882d34.md#insn-00882d58) · [`00882d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882d34.md#insn-00882d68) · [`00882d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882d34.md#insn-00882d74)
- 新版 `00882d98`（命令位置の公開資料なし） · `00882da8`（命令位置の公開資料なし） · `00882db4`（命令位置の公開資料なし）

~~~diff
- 00882d58 ["INT_ADD", "register:40f0:8", ["const:882d58:8", "const:4:8"]]
- 00882d58 ["CALL", null, ["ram:48ccb8:8"]]
+ 00882d98 ["INT_ADD", "register:40f0:8", ["const:882d98:8", "const:4:8"]]
+ 00882d98 ["CALL", null, ["ram:48ccf8:8"]]
- 00882d58 bytes d827f097
+ 00882d98 bytes d827f097
- 00882d68 ["INT_ADD", "register:40f0:8", ["const:882d68:8", "const:4:8"]]
- 00882d68 ["CALL", null, ["callee:0048ce54:8"]]
+ 00882da8 ["INT_ADD", "register:40f0:8", ["const:882da8:8", "const:4:8"]]
+ 00882da8 ["CALL", null, ["callee:0048ce54:8"]]
- 00882d68 bytes 2b28f097
+ 00882da8 bytes 2b28f097
- 00882d74 ["INT_ADD", "register:40f0:8", ["const:882d74:8", "const:4:8"]]
- 00882d74 ["CALL", null, ["callee:00492f28:8"]]
+ 00882db4 ["INT_ADD", "register:40f0:8", ["const:882db4:8", "const:4:8"]]
+ 00882db4 ["CALL", null, ["callee:00492f28:8"]]
- 00882d74 bytes 5d40f097
+ 00882db4 bytes 5d40f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edf372a7d032685f5aad8d62ca43f82b"></a>

### [`00882e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882e08.md) → [`00882e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882e48.md) FUN_00882e48

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00882e5c",
      "incomplete_value": false,
      "site": "00882e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882e1c",
      "incomplete_value": false,
      "site": "00882e20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "00882e60",
      "DATA",
      [
        "storage",
        "00c80518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882e60",
      "DATA",
      [
        "storage",
        "00c80918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882e08.md#insn-00882e14) · [`00882e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882e08.md#insn-00882e1c)
- 新版 `00882e54`（命令位置の公開資料なし） · `00882e5c`（命令位置の公開資料なし）

~~~diff
- 00882e14 ["INT_ADD", "register:40f0:8", ["const:882e14:8", "const:4:8"]]
- 00882e14 ["CALL", null, ["callee:00c57e90:8"]]
+ 00882e54 ["INT_ADD", "register:40f0:8", ["const:882e54:8", "const:4:8"]]
+ 00882e54 ["CALL", null, ["callee:00c57e90:8"]]
- 00882e14 bytes 1f530f94
+ 00882e54 bytes 0f540f94
- 00882e1c ["COPY", "tmp:0:8", ["const:518:8"]]
- 00882e1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00882e1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00882e1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00882e5c ["COPY", "tmp:0:8", ["const:918:8"]]
+ 00882e5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00882e5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00882e5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00882e1c bytes 08611491
+ 00882e5c bytes 08612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39ab272393f2bacc2cf155841ec2fcb4"></a>

### [`00882e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882e2c.md) → [`00882e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882e6c.md) FUN_00882e6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00882e70",
      "incomplete_value": false,
      "site": "00882e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882e30",
      "incomplete_value": false,
      "site": "00882e34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "00882e74",
      "DATA",
      [
        "storage",
        "00c80518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882e74",
      "DATA",
      [
        "storage",
        "00c80918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882e2c.md#insn-00882e30)
- 新版 `00882e70`（命令位置の公開資料なし）

~~~diff
- 00882e30 ["COPY", "tmp:0:8", ["const:518:8"]]
- 00882e30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00882e30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00882e30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00882e70 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 00882e70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00882e70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00882e70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00882e30 bytes 08611491
+ 00882e70 bytes 08612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-913e0d595ccd7d111b9368938bc639bb"></a>

### [`00882e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882e44.md) → [`00882e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882e84.md) FUN_00882e84

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ee8.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492f28.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.20% / 新版 93.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00882ebc",
      "incomplete_value": true,
      "site": "00882ed0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:690:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882e7c",
      "incomplete_value": true,
      "site": "00882e90",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:650:8"
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
      "definition_site": "00882ec8",
      "incomplete_value": true,
      "site": "00882ed4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:c40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882e88",
      "incomplete_value": true,
      "site": "00882e94",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:c00:8"
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
      "definition_site": "00882ec8",
      "incomplete_value": true,
      "site": "00882ed4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00882e88",
      "incomplete_value": true,
      "site": "00882e94",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00882ea0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "00882ebc",
      "READ",
      [
        "storage",
        "002c2650",
        null,
        null
      ]
    ],
    [
      "00882ec8",
      "READ",
      [
        "storage",
        "002bcc00",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00882ea0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "00882ebc",
      "READ",
      [
        "storage",
        "002c2690",
        null,
        null
      ]
    ],
    [
      "00882ec8",
      "READ",
      [
        "storage",
        "002bcc40",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882e44.md#insn-00882e60) · [`00882ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882e44.md#insn-00882ea0) · [`00882e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882e44.md#insn-00882e6c)
- 新版 `00882ea0`（命令位置の公開資料なし） · `00882ee0`（命令位置の公開資料なし） · `00882eac`（命令位置の公開資料なし）

~~~diff
- 00882e60 ["INT_ADD", "register:40f0:8", ["const:882e60:8", "const:4:8"]]
- 00882e60 ["CALL", null, ["ram:48ccb8:8"]]
+ 00882ea0 ["INT_ADD", "register:40f0:8", ["const:882ea0:8", "const:4:8"]]
+ 00882ea0 ["CALL", null, ["ram:48ccf8:8"]]
- 00882e60 bytes 9627f097
+ 00882ea0 bytes 9627f097
- 00882ea0 ["INT_ADD", "register:40f0:8", ["const:882ea0:8", "const:4:8"]]
- 00882ea0 ["CALL", null, ["callee:0048ce54:8"]]
+ 00882ee0 ["INT_ADD", "register:40f0:8", ["const:882ee0:8", "const:4:8"]]
+ 00882ee0 ["CALL", null, ["callee:0048ce54:8"]]
- 00882ea0 bytes dd27f097
+ 00882ee0 bytes dd27f097
- 00882e6c ["INT_ADD", "register:40f0:8", ["const:882e6c:8", "const:4:8"]]
- 00882e6c ["CALL", null, ["callee:00c57e90:8"]]
+ 00882eac ["INT_ADD", "register:40f0:8", ["const:882eac:8", "const:4:8"]]
+ 00882eac ["CALL", null, ["callee:00c57e90:8"]]
- 00882e6c bytes 09530f94
+ 00882eac bytes f9530f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2753d9f3f25048377cc5da9a913a90b6"></a>

### [`008830c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008830c0.md) → [`00883100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883100.md) FUN_00883100

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00883120",
      "incomplete_value": false,
      "site": "00883124",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008830e0",
      "incomplete_value": false,
      "site": "008830e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:598:8"
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
      "00883124",
      "DATA",
      [
        "storage",
        "00c80598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883124",
      "DATA",
      [
        "storage",
        "00c80998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008830d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008830c0.md#insn-008830d4) · [`008830e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008830c0.md#insn-008830e0)
- 新版 `00883114`（命令位置の公開資料なし） · `00883120`（命令位置の公開資料なし）

~~~diff
- 008830d4 ["INT_ADD", "register:40f0:8", ["const:8830d4:8", "const:4:8"]]
- 008830d4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00883114 ["INT_ADD", "register:40f0:8", ["const:883114:8", "const:4:8"]]
+ 00883114 ["CALL", null, ["callee:00c57e90:8"]]
- 008830d4 bytes 6f520f94
+ 00883114 bytes 5f530f94
- 008830e0 ["COPY", "tmp:0:8", ["const:598:8"]]
- 008830e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008830e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008830e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00883120 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00883120 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00883120 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00883120 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008830e0 bytes 08611691
+ 00883120 bytes 08612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a5a3a88f280ed017a8f575e0b2c7d96"></a>

### [`008830f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008830f8.md) → [`00883138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883138.md) FUN_00883138

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00883140",
      "incomplete_value": false,
      "site": "00883144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00883100",
      "incomplete_value": false,
      "site": "00883104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:598:8"
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
      "00883144",
      "DATA",
      [
        "storage",
        "00c80598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883144",
      "DATA",
      [
        "storage",
        "00c80998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008830f8.md#insn-00883100)
- 新版 `00883140`（命令位置の公開資料なし）

~~~diff
- 00883100 ["COPY", "tmp:0:8", ["const:598:8"]]
- 00883100 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00883100 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00883100 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00883140 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00883140 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00883140 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00883140 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00883100 bytes 29611691
+ 00883140 bytes 29612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-876c7ec622915ef487f3364ead747483"></a>

### [`00883118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883118.md) → [`00883158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883158.md) FUN_00883158

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0049329c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/0049329c.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`004932dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004932dc.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.88% / 新版 93.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008831b8",
      "incomplete_value": true,
      "site": "008831b8",
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
                "const:5c3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00883178",
      "incomplete_value": true,
      "site": "00883178",
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
                "const:4f6:8"
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
      "definition_site": "008831c0",
      "incomplete_value": true,
      "site": "008831c0",
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
                "const:fc2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00883180",
      "incomplete_value": true,
      "site": "00883180",
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
                "const:f82:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008832d0",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00883290",
      "value": [
        "leaf",
        "ram:48ccb8:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008831ac",
      "READ",
      [
        "storage",
        "002a14f6",
        null,
        "string"
      ]
    ],
    [
      "008831b0",
      "READ",
      [
        "storage",
        "002aff82",
        null,
        "string"
      ]
    ],
    [
      "008832d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "008831ac",
      "READ",
      [
        "storage",
        "002a15c3",
        null,
        "string"
      ]
    ],
    [
      "008831b0",
      "READ",
      [
        "storage",
        "002affc2",
        null,
        "string"
      ]
    ],
    [
      "008832d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883118.md#insn-00883290) · [`00883154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883118.md#insn-00883154) · [`00883168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883118.md#insn-00883168)
- 新版 `008832d0`（命令位置の公開資料なし） · `00883194`（命令位置の公開資料なし） · `008831a8`（命令位置の公開資料なし）

~~~diff
- 00883290 ["INT_ADD", "register:40f0:8", ["const:883290:8", "const:4:8"]]
- 00883290 ["CALL", null, ["ram:48ccb8:8"]]
+ 008832d0 ["INT_ADD", "register:40f0:8", ["const:8832d0:8", "const:4:8"]]
+ 008832d0 ["CALL", null, ["ram:48ccf8:8"]]
- 00883290 bytes 8a26f097
+ 008832d0 bytes 8a26f097
- 00883154 ["COPY", "tmp:0:8", ["const:f82:8"]]
- 00883154 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00883154 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00883154 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00883194 ["COPY", "tmp:0:8", ["const:fc2:8"]]
+ 00883194 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00883194 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00883194 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00883154 bytes 29093e91
+ 00883194 bytes 29093f91
- 00883168 ["COPY", "tmp:0:8", ["const:4f6:8"]]
- 00883168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00883168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00883168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008831a8 ["COPY", "tmp:0:8", ["const:5c3:8"]]
+ 008831a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008831a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008831a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00883168 bytes 08d91391
+ 008831a8 bytes 080d1791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13cec8d6bd7fa7f423d20fd76ddd7c42"></a>

### [`008835d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008835d8.md) → [`00883618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883618.md) FUN_00883618

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0088362c",
      "incomplete_value": false,
      "site": "00883630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008835ec",
      "incomplete_value": false,
      "site": "008835f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "00883630",
      "DATA",
      [
        "storage",
        "00c80608",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883630",
      "DATA",
      [
        "storage",
        "00c80a08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008835e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008835d8.md#insn-008835e4) · [`008835ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008835d8.md#insn-008835ec)
- 新版 `00883624`（命令位置の公開資料なし） · `0088362c`（命令位置の公開資料なし）

~~~diff
- 008835e4 ["INT_ADD", "register:40f0:8", ["const:8835e4:8", "const:4:8"]]
- 008835e4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00883624 ["INT_ADD", "register:40f0:8", ["const:883624:8", "const:4:8"]]
+ 00883624 ["CALL", null, ["callee:00c57e90:8"]]
- 008835e4 bytes 2b510f94
+ 00883624 bytes 1b520f94
- 008835ec ["COPY", "tmp:0:8", ["const:608:8"]]
- 008835ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008835ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008835ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088362c ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 0088362c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088362c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088362c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008835ec bytes 08211891
+ 0088362c bytes 08212891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bf5ac5f6c186867f589e8438b68d130"></a>

### [`008835fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008835fc.md) → [`0088363c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/0088363c.md) FUN_0088363c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00883640",
      "incomplete_value": false,
      "site": "00883644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00883600",
      "incomplete_value": false,
      "site": "00883604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "00883644",
      "DATA",
      [
        "storage",
        "00c80608",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883644",
      "DATA",
      [
        "storage",
        "00c80a08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008835fc.md#insn-00883600)
- 新版 `00883640`（命令位置の公開資料なし）

~~~diff
- 00883600 ["COPY", "tmp:0:8", ["const:608:8"]]
- 00883600 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00883600 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00883600 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00883640 ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 00883640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00883640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00883640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00883600 bytes 08211891
+ 00883640 bytes 08212891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d80a119cae829436432b23715d140ff"></a>

### [`00883614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883614.md) → [`00883654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883654.md) FUN_00883654

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0048dc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dc20.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0048dc60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dc60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.24% / 新版 90.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00883698",
      "incomplete_value": true,
      "site": "00883698",
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
                "const:edf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00883658",
      "incomplete_value": true,
      "site": "00883658",
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
                "const:e12:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00883670",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00883630",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "00883670",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "00883684",
      "READ",
      [
        "storage",
        "002a9e12",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00883670",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "00883684",
      "READ",
      [
        "storage",
        "002a9edf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883614.md#insn-00883630) · [`00883670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883614.md#insn-00883670) · [`0088363c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883614.md#insn-0088363c)
- 新版 `00883670`（命令位置の公開資料なし） · `008836b0`（命令位置の公開資料なし） · `0088367c`（命令位置の公開資料なし）

~~~diff
- 00883630 ["INT_ADD", "register:40f0:8", ["const:883630:8", "const:4:8"]]
- 00883630 ["CALL", null, ["ram:48ccb8:8"]]
+ 00883670 ["INT_ADD", "register:40f0:8", ["const:883670:8", "const:4:8"]]
+ 00883670 ["CALL", null, ["ram:48ccf8:8"]]
- 00883630 bytes a225f097
+ 00883670 bytes a225f097
- 00883670 ["INT_ADD", "register:40f0:8", ["const:883670:8", "const:4:8"]]
- 00883670 ["CALL", null, ["callee:0048dc60:8"]]
+ 008836b0 ["INT_ADD", "register:40f0:8", ["const:8836b0:8", "const:4:8"]]
+ 008836b0 ["CALL", null, ["callee:0048dc60:8"]]
- 00883670 bytes 6c29f097
+ 008836b0 bytes 6c29f097
- 0088363c ["COPY", "tmp:0:8", ["const:e12:8"]]
- 0088363c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088363c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088363c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088367c ["COPY", "tmp:0:8", ["const:edf:8"]]
+ 0088367c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088367c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088367c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088363c bytes 29493891
+ 0088367c bytes 297d3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72456ea687472d9f549da05e8e42b8c8"></a>

### [`00883724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883724.md) → [`00883764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883764.md) FUN_00883764

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "0088377c",
      "incomplete_value": false,
      "site": "00883788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088373c",
      "incomplete_value": false,
      "site": "00883748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "00883788",
      "DATA",
      [
        "storage",
        "00c80698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883788",
      "DATA",
      [
        "storage",
        "00c80a98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883724.md#insn-0088373c) · [`0088376c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883724.md#insn-0088376c) · [`00883780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883724.md#insn-00883780)
- 新版 `0088377c`（命令位置の公開資料なし） · `008837ac`（命令位置の公開資料なし） · `008837c0`（命令位置の公開資料なし）

~~~diff
- 0088373c ["COPY", "tmp:0:8", ["const:698:8"]]
- 0088373c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088373c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088373c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088377c ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 0088377c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088377c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088377c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088373c bytes 08611a91
+ 0088377c bytes 08612a91
- 0088376c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088376c ["INT_ADD", "register:40f0:8", ["const:88376c:8", "const:4:8"]]
- 0088376c ["CALLIND", null, ["register:0:8"]]
+ 008837ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 008837ac ["INT_ADD", "register:40f0:8", ["const:8837ac:8", "const:4:8"]]
+ 008837ac ["CALLIND", null, ["register:0:8"]]
- 0088376c bytes 00013fd6
+ 008837ac bytes 00013fd6
- 00883780 ["INT_ADD", "register:40f0:8", ["const:883780:8", "const:4:8"]]
- 00883780 ["CALL", null, ["callee:00c53d00:8"]]
+ 008837c0 ["INT_ADD", "register:40f0:8", ["const:8837c0:8", "const:4:8"]]
+ 008837c0 ["CALL", null, ["callee:00c53d00:8"]]
- 00883780 bytes 58400f94
+ 008837c0 bytes 50410f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ac12d307ad0b3e3ba348adccf11ce2a"></a>

### [`008837b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008837b4.md) → [`008837f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/008837f4.md) FUN_008837f4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0088380c",
      "incomplete_value": false,
      "site": "00883818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008837cc",
      "incomplete_value": false,
      "site": "008837d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "00883818",
      "DATA",
      [
        "storage",
        "00c80698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883818",
      "DATA",
      [
        "storage",
        "00c80a98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008837cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008837b4.md#insn-008837cc) · [`008837fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008837b4.md#insn-008837fc) · [`00883810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008837b4.md#insn-00883810)
- 新版 `0088380c`（命令位置の公開資料なし） · `0088383c`（命令位置の公開資料なし） · `00883850`（命令位置の公開資料なし）

~~~diff
- 008837cc ["COPY", "tmp:0:8", ["const:698:8"]]
- 008837cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008837cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008837cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088380c ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 0088380c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088380c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088380c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008837cc bytes 08611a91
+ 0088380c bytes 08612a91
- 008837fc ["COPY", "register:0:8", ["register:4040:8"]]
- 008837fc ["INT_ADD", "register:40f0:8", ["const:8837fc:8", "const:4:8"]]
- 008837fc ["CALLIND", null, ["register:0:8"]]
+ 0088383c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088383c ["INT_ADD", "register:40f0:8", ["const:88383c:8", "const:4:8"]]
+ 0088383c ["CALLIND", null, ["register:0:8"]]
- 008837fc bytes 00013fd6
+ 0088383c bytes 00013fd6
- 00883810 ["INT_ADD", "register:40f0:8", ["const:883810:8", "const:4:8"]]
- 00883810 ["CALL", null, ["callee:00c53d00:8"]]
+ 00883850 ["INT_ADD", "register:40f0:8", ["const:883850:8", "const:4:8"]]
+ 00883850 ["CALL", null, ["callee:00c53d00:8"]]
- 00883810 bytes 34400f94
+ 00883850 bytes 2c410f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d052033047be79202dfaa3df295dfef"></a>

### [`008838f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008838f0.md) → [`00883930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883930.md) FUN_00883930

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "0088394c",
      "incomplete_value": false,
      "site": "00883958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088390c",
      "incomplete_value": false,
      "site": "00883918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "00883958",
      "DATA",
      [
        "storage",
        "00c80698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883958",
      "DATA",
      [
        "storage",
        "00c80a98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088390c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008838f0.md#insn-0088390c) · [`0088392c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008838f0.md#insn-0088392c) · [`0088394c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008838f0.md#insn-0088394c)
- 新版 `0088394c`（命令位置の公開資料なし） · `0088396c`（命令位置の公開資料なし） · `0088398c`（命令位置の公開資料なし）

~~~diff
- 0088390c ["COPY", "tmp:0:8", ["const:698:8"]]
- 0088390c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088390c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088390c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088394c ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 0088394c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088394c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088394c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088390c bytes 29611a91
+ 0088394c bytes 29612a91
- 0088392c ["INT_ADD", "register:40f0:8", ["const:88392c:8", "const:4:8"]]
- 0088392c ["CALL", null, ["callee:00c53cd0:8"]]
+ 0088396c ["INT_ADD", "register:40f0:8", ["const:88396c:8", "const:4:8"]]
+ 0088396c ["CALL", null, ["callee:00c53cd0:8"]]
- 0088392c bytes e13f0f94
+ 0088396c bytes d9400f94
- 0088394c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088394c ["INT_ADD", "register:40f0:8", ["const:88394c:8", "const:4:8"]]
- 0088394c ["CALLIND", null, ["register:0:8"]]
+ 0088398c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088398c ["INT_ADD", "register:40f0:8", ["const:88398c:8", "const:4:8"]]
+ 0088398c ["CALLIND", null, ["register:0:8"]]
- 0088394c bytes 00013fd6
+ 0088398c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eced5d7e33f18b45d6dd9ccb2430702e"></a>

### [`00883a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883a94.md) → [`00883ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883ad4.md) FUN_00883ad4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`007687b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/007687b0.md) [`00768ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768ba8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00880cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880cb4.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`007687f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/007687f0.md) [`00768be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768be8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00880cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00883cd0",
      "incomplete_value": false,
      "site": "00883cd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00883c90",
      "incomplete_value": false,
      "site": "00883c98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00883d7c",
      "incomplete_value": false,
      "site": "00883d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00883d3c",
      "incomplete_value": false,
      "site": "00883d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00883b80",
      "value": [
        "leaf",
        "ram:768be8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00883b40",
      "value": [
        "leaf",
        "ram:768ba8:8"
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
      "00883b80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768ba8"
      ]
    ],
    [
      "00883b90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007687b0"
      ]
    ],
    [
      "00883cd8",
      "DATA",
      [
        "storage",
        "00c80798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883b80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768be8"
      ]
    ],
    [
      "00883b90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007687f0"
      ]
    ],
    [
      "00883cd8",
      "DATA",
      [
        "storage",
        "00c80b98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883a94.md#insn-00883b40) · [`00883b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883a94.md#insn-00883b50) · [`00883afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883a94.md#insn-00883afc)
- 新版 `00883b80`（命令位置の公開資料なし） · `00883b90`（命令位置の公開資料なし） · `00883b3c`（命令位置の公開資料なし）

~~~diff
- 00883b40 ["INT_ADD", "register:40f0:8", ["const:883b40:8", "const:4:8"]]
- 00883b40 ["CALL", null, ["ram:768ba8:8"]]
+ 00883b80 ["INT_ADD", "register:40f0:8", ["const:883b80:8", "const:4:8"]]
+ 00883b80 ["CALL", null, ["ram:768be8:8"]]
- 00883b40 bytes 1a94fb97
+ 00883b80 bytes 1a94fb97
- 00883b50 ["INT_ADD", "register:40f0:8", ["const:883b50:8", "const:4:8"]]
- 00883b50 ["CALL", null, ["ram:7687b0:8"]]
+ 00883b90 ["INT_ADD", "register:40f0:8", ["const:883b90:8", "const:4:8"]]
+ 00883b90 ["CALL", null, ["ram:7687f0:8"]]
- 00883b50 bytes 1893fb97
+ 00883b90 bytes 1893fb97
- 00883afc ["COPY", "register:0:8", ["register:4040:8"]]
- 00883afc ["INT_ADD", "register:40f0:8", ["const:883afc:8", "const:4:8"]]
- 00883afc ["CALLIND", null, ["register:0:8"]]
+ 00883b3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00883b3c ["INT_ADD", "register:40f0:8", ["const:883b3c:8", "const:4:8"]]
+ 00883b3c ["CALLIND", null, ["register:0:8"]]
- 00883afc bytes 00013fd6
+ 00883b3c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-285acc78e9f52a3fa0a4dd260cf5c80c"></a>

### [`0088406c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/0088406c.md) → [`008840ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008840ac.md) FUN_008840ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "008840c4",
      "incomplete_value": false,
      "site": "008840d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00884084",
      "incomplete_value": false,
      "site": "00884090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "008840d0",
      "DATA",
      [
        "storage",
        "00c80718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008840d0",
      "DATA",
      [
        "storage",
        "00c80b18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00884084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/0088406c.md#insn-00884084) · [`008840b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/0088406c.md#insn-008840b4) · [`008840c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/0088406c.md#insn-008840c8)
- 新版 `008840c4`（命令位置の公開資料なし） · `008840f4`（命令位置の公開資料なし） · `00884108`（命令位置の公開資料なし）

~~~diff
- 00884084 ["COPY", "tmp:0:8", ["const:718:8"]]
- 00884084 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00884084 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00884084 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008840c4 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 008840c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008840c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008840c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00884084 bytes 08611c91
+ 008840c4 bytes 08612c91
- 008840b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008840b4 ["INT_ADD", "register:40f0:8", ["const:8840b4:8", "const:4:8"]]
- 008840b4 ["CALLIND", null, ["register:0:8"]]
+ 008840f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008840f4 ["INT_ADD", "register:40f0:8", ["const:8840f4:8", "const:4:8"]]
+ 008840f4 ["CALLIND", null, ["register:0:8"]]
- 008840b4 bytes 00013fd6
+ 008840f4 bytes 00013fd6
- 008840c8 ["INT_ADD", "register:40f0:8", ["const:8840c8:8", "const:4:8"]]
- 008840c8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00884108 ["INT_ADD", "register:40f0:8", ["const:884108:8", "const:4:8"]]
+ 00884108 ["CALL", null, ["callee:00c53d00:8"]]
- 008840c8 bytes 063e0f94
+ 00884108 bytes fe3e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1919c4081f76521e58454461f9b886b6"></a>

### [`008840fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008840fc.md) → [`0088413c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/0088413c.md) FUN_0088413c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00884154",
      "incomplete_value": false,
      "site": "00884160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00884114",
      "incomplete_value": false,
      "site": "00884120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "00884160",
      "DATA",
      [
        "storage",
        "00c80718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00884160",
      "DATA",
      [
        "storage",
        "00c80b18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00884114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008840fc.md#insn-00884114) · [`00884144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008840fc.md#insn-00884144) · [`00884158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008840fc.md#insn-00884158)
- 新版 `00884154`（命令位置の公開資料なし） · `00884184`（命令位置の公開資料なし） · `00884198`（命令位置の公開資料なし）

~~~diff
- 00884114 ["COPY", "tmp:0:8", ["const:718:8"]]
- 00884114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00884114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00884114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00884154 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 00884154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00884154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00884154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00884114 bytes 08611c91
+ 00884154 bytes 08612c91
- 00884144 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884144 ["INT_ADD", "register:40f0:8", ["const:884144:8", "const:4:8"]]
- 00884144 ["CALLIND", null, ["register:0:8"]]
+ 00884184 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884184 ["INT_ADD", "register:40f0:8", ["const:884184:8", "const:4:8"]]
+ 00884184 ["CALLIND", null, ["register:0:8"]]
- 00884144 bytes 00013fd6
+ 00884184 bytes 00013fd6
- 00884158 ["INT_ADD", "register:40f0:8", ["const:884158:8", "const:4:8"]]
- 00884158 ["CALL", null, ["callee:00c53d00:8"]]
+ 00884198 ["INT_ADD", "register:40f0:8", ["const:884198:8", "const:4:8"]]
+ 00884198 ["CALL", null, ["callee:00c53d00:8"]]
- 00884158 bytes e23d0f94
+ 00884198 bytes da3e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-014d7d80592444133542ee7aa193a92f"></a>

### [`00884188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884188.md) → [`008841c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008841c8.md) FUN_008841c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008841f0",
      "incomplete_value": false,
      "site": "008841f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008841b0",
      "incomplete_value": false,
      "site": "008841b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "008841f4",
      "DATA",
      [
        "storage",
        "00c80718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008841f4",
      "DATA",
      [
        "storage",
        "00c80b18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088419c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884188.md#insn-0088419c) · [`008841b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884188.md#insn-008841b0) · [`008841cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884188.md#insn-008841cc)
- 新版 `008841dc`（命令位置の公開資料なし） · `008841f0`（命令位置の公開資料なし） · `0088420c`（命令位置の公開資料なし）

~~~diff
- 0088419c ["INT_ADD", "register:40f0:8", ["const:88419c:8", "const:4:8"]]
- 0088419c ["CALL", null, ["callee:00c57e90:8"]]
+ 008841dc ["INT_ADD", "register:40f0:8", ["const:8841dc:8", "const:4:8"]]
+ 008841dc ["CALL", null, ["callee:00c57e90:8"]]
- 0088419c bytes 3d4e0f94
+ 008841dc bytes 2d4f0f94
- 008841b0 ["COPY", "tmp:0:8", ["const:718:8"]]
- 008841b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008841b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008841b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008841f0 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 008841f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008841f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008841f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008841b0 bytes 29611c91
+ 008841f0 bytes 29612c91
- 008841cc ["INT_ADD", "register:40f0:8", ["const:8841cc:8", "const:4:8"]]
- 008841cc ["CALL", null, ["callee:00c53cd0:8"]]
+ 0088420c ["INT_ADD", "register:40f0:8", ["const:88420c:8", "const:4:8"]]
+ 0088420c ["CALL", null, ["callee:00c53cd0:8"]]
- 008841cc bytes b93d0f94
+ 0088420c bytes b13e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6c64def47b2732afd0562d981073a71"></a>

### [`00884238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884238.md) → [`00884278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884278.md) FUN_00884278

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "00884294",
      "incomplete_value": false,
      "site": "008842a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00884254",
      "incomplete_value": false,
      "site": "00884260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "008842a0",
      "DATA",
      [
        "storage",
        "00c80718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008842a0",
      "DATA",
      [
        "storage",
        "00c80b18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00884254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884238.md#insn-00884254) · [`00884274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884238.md#insn-00884274) · [`00884294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884238.md#insn-00884294)
- 新版 `00884294`（命令位置の公開資料なし） · `008842b4`（命令位置の公開資料なし） · `008842d4`（命令位置の公開資料なし）

~~~diff
- 00884254 ["COPY", "tmp:0:8", ["const:718:8"]]
- 00884254 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00884254 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00884254 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00884294 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 00884294 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00884294 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00884294 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00884254 bytes 29611c91
+ 00884294 bytes 29612c91
- 00884274 ["INT_ADD", "register:40f0:8", ["const:884274:8", "const:4:8"]]
- 00884274 ["CALL", null, ["callee:00c53cd0:8"]]
+ 008842b4 ["INT_ADD", "register:40f0:8", ["const:8842b4:8", "const:4:8"]]
+ 008842b4 ["CALL", null, ["callee:00c53cd0:8"]]
- 00884274 bytes 8f3d0f94
+ 008842b4 bytes 873e0f94
- 00884294 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884294 ["INT_ADD", "register:40f0:8", ["const:884294:8", "const:4:8"]]
- 00884294 ["CALLIND", null, ["register:0:8"]]
+ 008842d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008842d4 ["INT_ADD", "register:40f0:8", ["const:8842d4:8", "const:4:8"]]
+ 008842d4 ["CALLIND", null, ["register:0:8"]]
- 00884294 bytes 00013fd6
+ 008842d4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a26558b4d32b92c96280d75363e67f87"></a>

### [`00884418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884418.md) → [`00884458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884458.md) FUN_00884458

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "00884470",
      "incomplete_value": false,
      "site": "0088447c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00884430",
      "incomplete_value": false,
      "site": "0088443c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "0088447c",
      "DATA",
      [
        "storage",
        "00c80798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088447c",
      "DATA",
      [
        "storage",
        "00c80b98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00884430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884418.md#insn-00884430) · [`00884460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884418.md#insn-00884460) · [`00884474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884418.md#insn-00884474)
- 新版 `00884470`（命令位置の公開資料なし） · `008844a0`（命令位置の公開資料なし） · `008844b4`（命令位置の公開資料なし）

~~~diff
- 00884430 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00884430 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00884430 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00884430 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00884470 ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 00884470 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00884470 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00884470 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00884430 bytes 08611e91
+ 00884470 bytes 08612e91
- 00884460 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884460 ["INT_ADD", "register:40f0:8", ["const:884460:8", "const:4:8"]]
- 00884460 ["CALLIND", null, ["register:0:8"]]
+ 008844a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008844a0 ["INT_ADD", "register:40f0:8", ["const:8844a0:8", "const:4:8"]]
+ 008844a0 ["CALLIND", null, ["register:0:8"]]
- 00884460 bytes 00013fd6
+ 008844a0 bytes 00013fd6
- 00884474 ["INT_ADD", "register:40f0:8", ["const:884474:8", "const:4:8"]]
- 00884474 ["CALL", null, ["callee:00c53d00:8"]]
+ 008844b4 ["INT_ADD", "register:40f0:8", ["const:8844b4:8", "const:4:8"]]
+ 008844b4 ["CALL", null, ["callee:00c53d00:8"]]
- 00884474 bytes 1b3d0f94
+ 008844b4 bytes 133e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1838e3ed7b566eb3eb7dfbc739a65b71"></a>

### [`008844a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008844a8.md) → [`008844e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008844e8.md) FUN_008844e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00884500",
      "incomplete_value": false,
      "site": "0088450c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008844c0",
      "incomplete_value": false,
      "site": "008844cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "0088450c",
      "DATA",
      [
        "storage",
        "00c80798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088450c",
      "DATA",
      [
        "storage",
        "00c80b98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008844c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008844a8.md#insn-008844c0) · [`008844f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008844a8.md#insn-008844f0) · [`00884504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008844a8.md#insn-00884504)
- 新版 `00884500`（命令位置の公開資料なし） · `00884530`（命令位置の公開資料なし） · `00884544`（命令位置の公開資料なし）

~~~diff
- 008844c0 ["COPY", "tmp:0:8", ["const:798:8"]]
- 008844c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008844c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008844c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00884500 ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 00884500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00884500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00884500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008844c0 bytes 08611e91
+ 00884500 bytes 08612e91
- 008844f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008844f0 ["INT_ADD", "register:40f0:8", ["const:8844f0:8", "const:4:8"]]
- 008844f0 ["CALLIND", null, ["register:0:8"]]
+ 00884530 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884530 ["INT_ADD", "register:40f0:8", ["const:884530:8", "const:4:8"]]
+ 00884530 ["CALLIND", null, ["register:0:8"]]
- 008844f0 bytes 00013fd6
+ 00884530 bytes 00013fd6
- 00884504 ["INT_ADD", "register:40f0:8", ["const:884504:8", "const:4:8"]]
- 00884504 ["CALL", null, ["callee:00c53d00:8"]]
+ 00884544 ["INT_ADD", "register:40f0:8", ["const:884544:8", "const:4:8"]]
+ 00884544 ["CALL", null, ["callee:00c53d00:8"]]
- 00884504 bytes f73c0f94
+ 00884544 bytes ef3d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c4c77f629162f13f7cb08f13fc15c50"></a>

### [`00884534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884534.md) → [`00884574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884574.md) FUN_00884574

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088459c",
      "incomplete_value": false,
      "site": "008845a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088455c",
      "incomplete_value": false,
      "site": "00884560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "008845a0",
      "DATA",
      [
        "storage",
        "00c80798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008845a0",
      "DATA",
      [
        "storage",
        "00c80b98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00884548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884534.md#insn-00884548) · [`0088455c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884534.md#insn-0088455c) · [`00884578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884534.md#insn-00884578)
- 新版 `00884588`（命令位置の公開資料なし） · `0088459c`（命令位置の公開資料なし） · `008845b8`（命令位置の公開資料なし）

~~~diff
- 00884548 ["INT_ADD", "register:40f0:8", ["const:884548:8", "const:4:8"]]
- 00884548 ["CALL", null, ["callee:00c57e90:8"]]
+ 00884588 ["INT_ADD", "register:40f0:8", ["const:884588:8", "const:4:8"]]
+ 00884588 ["CALL", null, ["callee:00c57e90:8"]]
- 00884548 bytes 524d0f94
+ 00884588 bytes 424e0f94
- 0088455c ["COPY", "tmp:0:8", ["const:798:8"]]
- 0088455c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088455c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088455c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088459c ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 0088459c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088459c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088459c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088455c bytes 29611e91
+ 0088459c bytes 29612e91
- 00884578 ["INT_ADD", "register:40f0:8", ["const:884578:8", "const:4:8"]]
- 00884578 ["CALL", null, ["callee:00c53cd0:8"]]
+ 008845b8 ["INT_ADD", "register:40f0:8", ["const:8845b8:8", "const:4:8"]]
+ 008845b8 ["CALL", null, ["callee:00c53cd0:8"]]
- 00884578 bytes ce3c0f94
+ 008845b8 bytes c63d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9776e69db818890d1929c85e9f1b607"></a>

### [`008847c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008847c4.md) → [`00884804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884804.md) FUN_00884804

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "0088481c",
      "incomplete_value": false,
      "site": "00884828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008847dc",
      "incomplete_value": false,
      "site": "008847e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
      "00884828",
      "DATA",
      [
        "storage",
        "00c80828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00884828",
      "DATA",
      [
        "storage",
        "00c80c28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008847dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008847c4.md#insn-008847dc) · [`0088480c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008847c4.md#insn-0088480c) · [`00884820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008847c4.md#insn-00884820)
- 新版 `0088481c`（命令位置の公開資料なし） · `0088484c`（命令位置の公開資料なし） · `00884860`（命令位置の公開資料なし）

~~~diff
- 008847dc ["COPY", "tmp:0:8", ["const:828:8"]]
- 008847dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008847dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008847dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088481c ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 0088481c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088481c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088481c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008847dc bytes 08a12091
+ 0088481c bytes 08a13091
- 0088480c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088480c ["INT_ADD", "register:40f0:8", ["const:88480c:8", "const:4:8"]]
- 0088480c ["CALLIND", null, ["register:0:8"]]
+ 0088484c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088484c ["INT_ADD", "register:40f0:8", ["const:88484c:8", "const:4:8"]]
+ 0088484c ["CALLIND", null, ["register:0:8"]]
- 0088480c bytes 00013fd6
+ 0088484c bytes 00013fd6
- 00884820 ["INT_ADD", "register:40f0:8", ["const:884820:8", "const:4:8"]]
- 00884820 ["CALL", null, ["callee:00c53d00:8"]]
+ 00884860 ["INT_ADD", "register:40f0:8", ["const:884860:8", "const:4:8"]]
+ 00884860 ["CALL", null, ["callee:00c53d00:8"]]
- 00884820 bytes 303c0f94
+ 00884860 bytes 283d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0c3d17131255a97854668016cf4a80d"></a>

### [`00884854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884854.md) → [`00884894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884894.md) FUN_00884894

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "008848ac",
      "incomplete_value": false,
      "site": "008848b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088486c",
      "incomplete_value": false,
      "site": "00884878",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:828:8"
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
      "008848b8",
      "DATA",
      [
        "storage",
        "00c80828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008848b8",
      "DATA",
      [
        "storage",
        "00c80c28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088486c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884854.md#insn-0088486c) · [`0088489c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884854.md#insn-0088489c) · [`008848b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884854.md#insn-008848b0)
- 新版 `008848ac`（命令位置の公開資料なし） · `008848dc`（命令位置の公開資料なし） · `008848f0`（命令位置の公開資料なし）

~~~diff
- 0088486c ["COPY", "tmp:0:8", ["const:828:8"]]
- 0088486c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088486c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088486c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008848ac ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 008848ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008848ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008848ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088486c bytes 08a12091
+ 008848ac bytes 08a13091
- 0088489c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088489c ["INT_ADD", "register:40f0:8", ["const:88489c:8", "const:4:8"]]
- 0088489c ["CALLIND", null, ["register:0:8"]]
+ 008848dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008848dc ["INT_ADD", "register:40f0:8", ["const:8848dc:8", "const:4:8"]]
+ 008848dc ["CALLIND", null, ["register:0:8"]]
- 0088489c bytes 00013fd6
+ 008848dc bytes 00013fd6
- 008848b0 ["INT_ADD", "register:40f0:8", ["const:8848b0:8", "const:4:8"]]
- 008848b0 ["CALL", null, ["callee:00c53d00:8"]]
+ 008848f0 ["INT_ADD", "register:40f0:8", ["const:8848f0:8", "const:4:8"]]
+ 008848f0 ["CALL", null, ["callee:00c53d00:8"]]
- 008848b0 bytes 0c3c0f94
+ 008848f0 bytes 043d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0e62671a1f9362b5fa439d93efa0d6e"></a>

### [`008848e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008848e0.md) → [`00884920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884920.md) FUN_00884920

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00884948",
      "incomplete_value": false,
      "site": "0088494c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00884908",
      "incomplete_value": false,
      "site": "0088490c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:828:8"
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
      "0088494c",
      "DATA",
      [
        "storage",
        "00c80828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088494c",
      "DATA",
      [
        "storage",
        "00c80c28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008848f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008848e0.md#insn-008848f4) · [`00884908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008848e0.md#insn-00884908) · [`00884924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008848e0.md#insn-00884924)
- 新版 `00884934`（命令位置の公開資料なし） · `00884948`（命令位置の公開資料なし） · `00884964`（命令位置の公開資料なし）

~~~diff
- 008848f4 ["INT_ADD", "register:40f0:8", ["const:8848f4:8", "const:4:8"]]
- 008848f4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00884934 ["INT_ADD", "register:40f0:8", ["const:884934:8", "const:4:8"]]
+ 00884934 ["CALL", null, ["callee:00c57e90:8"]]
- 008848f4 bytes 674c0f94
+ 00884934 bytes 574d0f94
- 00884908 ["COPY", "tmp:0:8", ["const:828:8"]]
- 00884908 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00884908 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00884908 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00884948 ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 00884948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00884948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00884948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00884908 bytes 29a12091
+ 00884948 bytes 29a13091
- 00884924 ["INT_ADD", "register:40f0:8", ["const:884924:8", "const:4:8"]]
- 00884924 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00884964 ["INT_ADD", "register:40f0:8", ["const:884964:8", "const:4:8"]]
+ 00884964 ["CALL", null, ["callee:00c53cd0:8"]]
- 00884924 bytes e33b0f94
+ 00884964 bytes db3c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-224541eee61b985386189aad28a60aa9"></a>

### [`00884990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884990.md) → [`008849d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008849d0.md) FUN_008849d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "008849ec",
      "incomplete_value": false,
      "site": "008849f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008849ac",
      "incomplete_value": false,
      "site": "008849b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:828:8"
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
      "008849f8",
      "DATA",
      [
        "storage",
        "00c80828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008849f8",
      "DATA",
      [
        "storage",
        "00c80c28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008849ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884990.md#insn-008849ac) · [`008849cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884990.md#insn-008849cc) · [`008849ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884990.md#insn-008849ec)
- 新版 `008849ec`（命令位置の公開資料なし） · `00884a0c`（命令位置の公開資料なし） · `00884a2c`（命令位置の公開資料なし）

~~~diff
- 008849ac ["COPY", "tmp:0:8", ["const:828:8"]]
- 008849ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008849ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008849ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008849ec ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 008849ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008849ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008849ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008849ac bytes 29a12091
+ 008849ec bytes 29a13091
- 008849cc ["INT_ADD", "register:40f0:8", ["const:8849cc:8", "const:4:8"]]
- 008849cc ["CALL", null, ["callee:00c53cd0:8"]]
+ 00884a0c ["INT_ADD", "register:40f0:8", ["const:884a0c:8", "const:4:8"]]
+ 00884a0c ["CALL", null, ["callee:00c53cd0:8"]]
- 008849cc bytes b93b0f94
+ 00884a0c bytes b13c0f94
- 008849ec ["COPY", "register:0:8", ["register:4040:8"]]
- 008849ec ["INT_ADD", "register:40f0:8", ["const:8849ec:8", "const:4:8"]]
- 008849ec ["CALLIND", null, ["register:0:8"]]
+ 00884a2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884a2c ["INT_ADD", "register:40f0:8", ["const:884a2c:8", "const:4:8"]]
+ 00884a2c ["CALLIND", null, ["register:0:8"]]
- 008849ec bytes 00013fd6
+ 00884a2c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-831a0a7efbf831468eca27597e72dc0d"></a>

### [`00884b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884b34.md) → [`00884b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884b74.md) FUN_00884b74

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 15件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00768174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768174.md) [`007687b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/007687b0.md) [`00768ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768ba8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`007681b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/007681b4.md) [`007687f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/007687f0.md) [`00768be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768be8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 97.60% / 新版 97.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00884d88",
      "incomplete_value": false,
      "site": "00884d90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00884d48",
      "incomplete_value": false,
      "site": "00884d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00884bd0",
      "value": [
        "leaf",
        "ram:7687f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00884b90",
      "value": [
        "leaf",
        "ram:7687b0:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00884b94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00884bd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007687b0"
      ]
    ],
    [
      "unmatched:00884b94",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "00884bdc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768ba8"
      ]
    ]
  ],
  "added": [
    [
      "00884bd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007687f0"
      ]
    ],
    [
      "00884bd4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "00884bdc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768be8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00884b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884b34.md#insn-00884b90) · [`00884b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884b34.md#insn-00884b94) · [`00884b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884b34.md#insn-00884b9c)
- 新版 `00884bd0`（命令位置の公開資料なし） · `00884bdc`（命令位置の公開資料なし）

~~~diff
- 00884b90 ["INT_ADD", "register:40f0:8", ["const:884b90:8", "const:4:8"]]
- 00884b90 ["CALL", null, ["ram:7687b0:8"]]
+ 00884bd0 ["INT_ADD", "register:40f0:8", ["const:884bd0:8", "const:4:8"]]
+ 00884bd0 ["CALL", null, ["ram:7687f0:8"]]
- 00884b90 bytes 088ffb97
+ 00884bd0 bytes 088ffb97
- 00884b94 ["INT_ADD", "register:40f0:8", ["const:884b94:8", "const:4:8"]]
- 00884b94 ["CALL", null, ["callee:008514f8:8"]]
- 00884b94 bytes 4932ff97
- 00884b9c ["INT_ADD", "register:40f0:8", ["const:884b9c:8", "const:4:8"]]
- 00884b9c ["CALL", null, ["ram:768ba8:8"]]
+ 00884bdc ["INT_ADD", "register:40f0:8", ["const:884bdc:8", "const:4:8"]]
+ 00884bdc ["CALL", null, ["ram:768be8:8"]]
- 00884b9c bytes 0390fb97
+ 00884bdc bytes 0390fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fdb04f236c3a36ab15b8ddffefc6e37"></a>

### [`00884fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884fb8.md) → [`00884ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884ff8.md) FUN_00884ff8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "00885010",
      "incomplete_value": false,
      "site": "0088501c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00884fd0",
      "incomplete_value": false,
      "site": "00884fdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "0088501c",
      "DATA",
      [
        "storage",
        "00c80898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088501c",
      "DATA",
      [
        "storage",
        "00c80c98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00884fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884fb8.md#insn-00884fd0) · [`00885000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884fb8.md#insn-00885000) · [`00885014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884fb8.md#insn-00885014)
- 新版 `00885010`（命令位置の公開資料なし） · `00885040`（命令位置の公開資料なし） · `00885054`（命令位置の公開資料なし）

~~~diff
- 00884fd0 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00884fd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00884fd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00884fd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00885010 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 00885010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00885010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00885010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00884fd0 bytes 08612291
+ 00885010 bytes 08613291
- 00885000 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885000 ["INT_ADD", "register:40f0:8", ["const:885000:8", "const:4:8"]]
- 00885000 ["CALLIND", null, ["register:0:8"]]
+ 00885040 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885040 ["INT_ADD", "register:40f0:8", ["const:885040:8", "const:4:8"]]
+ 00885040 ["CALLIND", null, ["register:0:8"]]
- 00885000 bytes 00013fd6
+ 00885040 bytes 00013fd6
- 00885014 ["INT_ADD", "register:40f0:8", ["const:885014:8", "const:4:8"]]
- 00885014 ["CALL", null, ["callee:00c53d00:8"]]
+ 00885054 ["INT_ADD", "register:40f0:8", ["const:885054:8", "const:4:8"]]
+ 00885054 ["CALL", null, ["callee:00c53d00:8"]]
- 00885014 bytes 333a0f94
+ 00885054 bytes 2b3b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2db113fb063fa4e84f2df0a378bd3ed"></a>

### [`00885048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885048.md) → [`00885088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885088.md) FUN_00885088

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "008850a0",
      "incomplete_value": false,
      "site": "008850ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885060",
      "incomplete_value": false,
      "site": "0088506c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "008850ac",
      "DATA",
      [
        "storage",
        "00c80898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008850ac",
      "DATA",
      [
        "storage",
        "00c80c98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885048.md#insn-00885060) · [`00885090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885048.md#insn-00885090) · [`008850a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885048.md#insn-008850a4)
- 新版 `008850a0`（命令位置の公開資料なし） · `008850d0`（命令位置の公開資料なし） · `008850e4`（命令位置の公開資料なし）

~~~diff
- 00885060 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00885060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00885060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00885060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008850a0 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 008850a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008850a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008850a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00885060 bytes 08612291
+ 008850a0 bytes 08613291
- 00885090 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885090 ["INT_ADD", "register:40f0:8", ["const:885090:8", "const:4:8"]]
- 00885090 ["CALLIND", null, ["register:0:8"]]
+ 008850d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008850d0 ["INT_ADD", "register:40f0:8", ["const:8850d0:8", "const:4:8"]]
+ 008850d0 ["CALLIND", null, ["register:0:8"]]
- 00885090 bytes 00013fd6
+ 008850d0 bytes 00013fd6
- 008850a4 ["INT_ADD", "register:40f0:8", ["const:8850a4:8", "const:4:8"]]
- 008850a4 ["CALL", null, ["callee:00c53d00:8"]]
+ 008850e4 ["INT_ADD", "register:40f0:8", ["const:8850e4:8", "const:4:8"]]
+ 008850e4 ["CALL", null, ["callee:00c53d00:8"]]
- 008850a4 bytes 0f3a0f94
+ 008850e4 bytes 073b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73304de76aba06af452334b5f39a0fea"></a>

### [`008850d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008850d4.md) → [`00885114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885114.md) FUN_00885114

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088513c",
      "incomplete_value": false,
      "site": "00885140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008850fc",
      "incomplete_value": false,
      "site": "00885100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00885140",
      "DATA",
      [
        "storage",
        "00c80898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885140",
      "DATA",
      [
        "storage",
        "00c80c98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008850e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008850d4.md#insn-008850e8) · [`008850fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008850d4.md#insn-008850fc) · [`00885118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008850d4.md#insn-00885118)
- 新版 `00885128`（命令位置の公開資料なし） · `0088513c`（命令位置の公開資料なし） · `00885158`（命令位置の公開資料なし）

~~~diff
- 008850e8 ["INT_ADD", "register:40f0:8", ["const:8850e8:8", "const:4:8"]]
- 008850e8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00885128 ["INT_ADD", "register:40f0:8", ["const:885128:8", "const:4:8"]]
+ 00885128 ["CALL", null, ["callee:00c57e90:8"]]
- 008850e8 bytes 6a4a0f94
+ 00885128 bytes 5a4b0f94
- 008850fc ["COPY", "tmp:0:8", ["const:898:8"]]
- 008850fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008850fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008850fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088513c ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 0088513c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088513c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088513c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008850fc bytes 29612291
+ 0088513c bytes 29613291
- 00885118 ["INT_ADD", "register:40f0:8", ["const:885118:8", "const:4:8"]]
- 00885118 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00885158 ["INT_ADD", "register:40f0:8", ["const:885158:8", "const:4:8"]]
+ 00885158 ["CALL", null, ["callee:00c53cd0:8"]]
- 00885118 bytes e6390f94
+ 00885158 bytes de3a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd03d0393f9599cbd2928b7e3b493ca4"></a>

### [`00885184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885184.md) → [`008851c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008851c4.md) FUN_008851c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "008851e0",
      "incomplete_value": false,
      "site": "008851ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008851a0",
      "incomplete_value": false,
      "site": "008851ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "008851ec",
      "DATA",
      [
        "storage",
        "00c80898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008851ec",
      "DATA",
      [
        "storage",
        "00c80c98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008851a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885184.md#insn-008851a0) · [`008851c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885184.md#insn-008851c0) · [`008851e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885184.md#insn-008851e0)
- 新版 `008851e0`（命令位置の公開資料なし） · `00885200`（命令位置の公開資料なし） · `00885220`（命令位置の公開資料なし）

~~~diff
- 008851a0 ["COPY", "tmp:0:8", ["const:898:8"]]
- 008851a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008851a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008851a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008851e0 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 008851e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008851e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008851e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008851a0 bytes 29612291
+ 008851e0 bytes 29613291
- 008851c0 ["INT_ADD", "register:40f0:8", ["const:8851c0:8", "const:4:8"]]
- 008851c0 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00885200 ["INT_ADD", "register:40f0:8", ["const:885200:8", "const:4:8"]]
+ 00885200 ["CALL", null, ["callee:00c53cd0:8"]]
- 008851c0 bytes bc390f94
+ 00885200 bytes b43a0f94
- 008851e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008851e0 ["INT_ADD", "register:40f0:8", ["const:8851e0:8", "const:4:8"]]
- 008851e0 ["CALLIND", null, ["register:0:8"]]
+ 00885220 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885220 ["INT_ADD", "register:40f0:8", ["const:885220:8", "const:4:8"]]
+ 00885220 ["CALLIND", null, ["register:0:8"]]
- 008851e0 bytes 00013fd6
+ 00885220 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-837413814d4bb9579698ffa1748e1c61"></a>

### [`00885364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885364.md) → [`008853a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008853a4.md) FUN_008853a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008853c0",
      "incomplete_value": false,
      "site": "008853c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885380",
      "incomplete_value": false,
      "site": "00885388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "008853c8",
      "DATA",
      [
        "storage",
        "00c80928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008853c8",
      "DATA",
      [
        "storage",
        "00c80d28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885364.md#insn-00885380) · [`00885398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885364.md#insn-00885398) · [`008853ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885364.md#insn-008853ac)
- 新版 `008853c0`（命令位置の公開資料なし） · `008853d8`（命令位置の公開資料なし） · `008853ec`（命令位置の公開資料なし）

~~~diff
- 00885380 ["COPY", "tmp:0:8", ["const:928:8"]]
- 00885380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00885380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00885380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008853c0 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 008853c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008853c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008853c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00885380 bytes 08a12491
+ 008853c0 bytes 08a13491
- 00885398 ["INT_ADD", "register:40f0:8", ["const:885398:8", "const:4:8"]]
- 00885398 ["CALL", null, ["callee:00c53d00:8"]]
+ 008853d8 ["INT_ADD", "register:40f0:8", ["const:8853d8:8", "const:4:8"]]
+ 008853d8 ["CALL", null, ["callee:00c53d00:8"]]
- 00885398 bytes 52390f94
+ 008853d8 bytes 4a3a0f94
- 008853ac ["COPY", "register:0:8", ["register:4040:8"]]
- 008853ac ["INT_ADD", "register:40f0:8", ["const:8853ac:8", "const:4:8"]]
- 008853ac ["CALLIND", null, ["register:0:8"]]
+ 008853ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 008853ec ["INT_ADD", "register:40f0:8", ["const:8853ec:8", "const:4:8"]]
+ 008853ec ["CALLIND", null, ["register:0:8"]]
- 008853ac bytes 00013fd6
+ 008853ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43ef24fe920c8956388f7ac5150fc982"></a>

### [`00885400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885400.md) → [`00885440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885440.md) FUN_00885440

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088545c",
      "incomplete_value": false,
      "site": "00885464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088541c",
      "incomplete_value": false,
      "site": "00885424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "00885464",
      "DATA",
      [
        "storage",
        "00c80928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885464",
      "DATA",
      [
        "storage",
        "00c80d28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088541c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885400.md#insn-0088541c) · [`00885434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885400.md#insn-00885434) · [`00885448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885400.md#insn-00885448)
- 新版 `0088545c`（命令位置の公開資料なし） · `00885474`（命令位置の公開資料なし） · `00885488`（命令位置の公開資料なし）

~~~diff
- 0088541c ["COPY", "tmp:0:8", ["const:928:8"]]
- 0088541c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088541c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088541c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088545c ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 0088545c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088545c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088545c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088541c bytes 08a12491
+ 0088545c bytes 08a13491
- 00885434 ["INT_ADD", "register:40f0:8", ["const:885434:8", "const:4:8"]]
- 00885434 ["CALL", null, ["callee:00c53d00:8"]]
+ 00885474 ["INT_ADD", "register:40f0:8", ["const:885474:8", "const:4:8"]]
+ 00885474 ["CALL", null, ["callee:00c53d00:8"]]
- 00885434 bytes 2b390f94
+ 00885474 bytes 233a0f94
- 00885448 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885448 ["INT_ADD", "register:40f0:8", ["const:885448:8", "const:4:8"]]
- 00885448 ["CALLIND", null, ["register:0:8"]]
+ 00885488 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885488 ["INT_ADD", "register:40f0:8", ["const:885488:8", "const:4:8"]]
+ 00885488 ["CALLIND", null, ["register:0:8"]]
- 00885448 bytes 00013fd6
+ 00885488 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78835731b08af0e15fb005e663957393"></a>

### [`00885494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885494.md) → [`008854d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008854d4.md) FUN_008854d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00885500",
      "incomplete_value": false,
      "site": "00885500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008854c0",
      "incomplete_value": false,
      "site": "008854c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "00885500",
      "DATA",
      [
        "storage",
        "00c80928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885500",
      "DATA",
      [
        "storage",
        "00c80d28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008854a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885494.md#insn-008854a8) · [`008854b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885494.md#insn-008854b8) · [`008854dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885494.md#insn-008854dc)
- 新版 `008854e8`（命令位置の公開資料なし） · `008854f8`（命令位置の公開資料なし） · `0088551c`（命令位置の公開資料なし）

~~~diff
- 008854a8 ["INT_ADD", "register:40f0:8", ["const:8854a8:8", "const:4:8"]]
- 008854a8 ["CALL", null, ["callee:00c57e90:8"]]
+ 008854e8 ["INT_ADD", "register:40f0:8", ["const:8854e8:8", "const:4:8"]]
+ 008854e8 ["CALL", null, ["callee:00c57e90:8"]]
- 008854a8 bytes 7a490f94
+ 008854e8 bytes 6a4a0f94
- 008854b8 ["COPY", "tmp:0:8", ["const:928:8"]]
- 008854b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008854b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008854b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008854f8 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 008854f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008854f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008854f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008854b8 bytes 08a12491
+ 008854f8 bytes 08a13491
- 008854dc ["COPY", "register:0:8", ["register:4040:8"]]
- 008854dc ["INT_ADD", "register:40f0:8", ["const:8854dc:8", "const:4:8"]]
- 008854dc ["CALLIND", null, ["register:0:8"]]
+ 0088551c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088551c ["INT_ADD", "register:40f0:8", ["const:88551c:8", "const:4:8"]]
+ 0088551c ["CALLIND", null, ["register:0:8"]]
- 008854dc bytes 00013fd6
+ 0088551c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68c0aa870746a2daf07fafafb7cf8c33"></a>

### [`0088553c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/0088553c.md) → [`0088557c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/0088557c.md) FUN_0088557c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "0088559c",
      "incomplete_value": false,
      "site": "0088559c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088555c",
      "incomplete_value": false,
      "site": "0088555c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "0088559c",
      "DATA",
      [
        "storage",
        "00c80928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088559c",
      "DATA",
      [
        "storage",
        "00c80d28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088559c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/0088553c.md#insn-0088559c) · [`00885558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/0088553c.md#insn-00885558) · [`00885578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/0088553c.md#insn-00885578)
- 新版 `008855dc`（命令位置の公開資料なし） · `00885598`（命令位置の公開資料なし） · `008855b8`（命令位置の公開資料なし）

~~~diff
- 0088559c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088559c ["INT_ADD", "register:40f0:8", ["const:88559c:8", "const:4:8"]]
- 0088559c ["CALLIND", null, ["register:0:8"]]
+ 008855dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008855dc ["INT_ADD", "register:40f0:8", ["const:8855dc:8", "const:4:8"]]
+ 008855dc ["CALLIND", null, ["register:0:8"]]
- 0088559c bytes 00013fd6
+ 008855dc bytes 00013fd6
- 00885558 ["COPY", "tmp:0:8", ["const:928:8"]]
- 00885558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00885558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00885558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00885598 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00885598 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00885598 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00885598 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00885558 bytes 08a12491
+ 00885598 bytes 08a13491
- 00885578 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885578 ["INT_ADD", "register:40f0:8", ["const:885578:8", "const:4:8"]]
- 00885578 ["CALLIND", null, ["register:0:8"]]
+ 008855b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008855b8 ["INT_ADD", "register:40f0:8", ["const:8855b8:8", "const:4:8"]]
+ 008855b8 ["CALLIND", null, ["register:0:8"]]
- 00885578 bytes 00013fd6
+ 008855b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc3f1e5bc9fc0de2e1bd5a03fe807aec"></a>

### [`008856e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008856e4.md) → [`00885724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885724.md) FUN_00885724

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`007689e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/007689e8.md) [`00768e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768e50.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00880668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880668.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00768a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768a28.md) [`00768e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768e90.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008806a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008806a8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.73% / 新版 97.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008858b8",
      "incomplete_value": false,
      "site": "008858c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885878",
      "incomplete_value": false,
      "site": "00885880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00885794",
      "value": [
        "leaf",
        "ram:768a28:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00885754",
      "value": [
        "leaf",
        "ram:7689e8:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008857d8",
      "value": [
        "leaf",
        "ram:768e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00885798",
      "value": [
        "leaf",
        "ram:768e50:8"
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
      "00885794",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007689e8"
      ]
    ],
    [
      "008857d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768e50"
      ]
    ],
    [
      "008858c0",
      "DATA",
      [
        "storage",
        "00c80998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885794",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768a28"
      ]
    ],
    [
      "008857d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768e90"
      ]
    ],
    [
      "008858c0",
      "DATA",
      [
        "storage",
        "00c80d98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008856e4.md#insn-00885754) · [`00885798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008856e4.md#insn-00885798) · [`0088574c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008856e4.md#insn-0088574c)
- 新版 `00885794`（命令位置の公開資料なし） · `008857d8`（命令位置の公開資料なし） · `0088578c`（命令位置の公開資料なし）

~~~diff
- 00885754 ["INT_ADD", "register:40f0:8", ["const:885754:8", "const:4:8"]]
- 00885754 ["CALL", null, ["ram:7689e8:8"]]
+ 00885794 ["INT_ADD", "register:40f0:8", ["const:885794:8", "const:4:8"]]
+ 00885794 ["CALL", null, ["ram:768a28:8"]]
- 00885754 bytes a58cfb97
+ 00885794 bytes a58cfb97
- 00885798 ["INT_ADD", "register:40f0:8", ["const:885798:8", "const:4:8"]]
- 00885798 ["CALL", null, ["ram:768e50:8"]]
+ 008857d8 ["INT_ADD", "register:40f0:8", ["const:8857d8:8", "const:4:8"]]
+ 008857d8 ["CALL", null, ["ram:768e90:8"]]
- 00885798 bytes ae8dfb97
+ 008857d8 bytes ae8dfb97
- 0088574c ["INT_ADD", "register:40f0:8", ["const:88574c:8", "const:4:8"]]
- 0088574c ["CALL", null, ["callee:008514f8:8"]]
+ 0088578c ["INT_ADD", "register:40f0:8", ["const:88578c:8", "const:4:8"]]
+ 0088578c ["CALL", null, ["callee:008514f8:8"]]
- 0088574c bytes 5b2fff97
+ 0088578c bytes 5b2fff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7fec68a54d1d725bb46f95a67caed5e"></a>

### [`00885ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885ad4.md) → [`00885b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885b14.md) FUN_00885b14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "00885b2c",
      "incomplete_value": false,
      "site": "00885b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885aec",
      "incomplete_value": false,
      "site": "00885af8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "00885b38",
      "DATA",
      [
        "storage",
        "00c80998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885b38",
      "DATA",
      [
        "storage",
        "00c80d98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885ad4.md#insn-00885aec) · [`00885b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885ad4.md#insn-00885b1c) · [`00885b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885ad4.md#insn-00885b30)
- 新版 `00885b2c`（命令位置の公開資料なし） · `00885b5c`（命令位置の公開資料なし） · `00885b70`（命令位置の公開資料なし）

~~~diff
- 00885aec ["COPY", "tmp:0:8", ["const:998:8"]]
- 00885aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00885aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00885aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00885b2c ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 00885b2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00885b2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00885b2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00885aec bytes 08612691
+ 00885b2c bytes 08613691
- 00885b1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00885b1c ["INT_ADD", "register:40f0:8", ["const:885b1c:8", "const:4:8"]]
- 00885b1c ["CALLIND", null, ["register:0:8"]]
+ 00885b5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885b5c ["INT_ADD", "register:40f0:8", ["const:885b5c:8", "const:4:8"]]
+ 00885b5c ["CALLIND", null, ["register:0:8"]]
- 00885b1c bytes 00013fd6
+ 00885b5c bytes 00013fd6
- 00885b30 ["INT_ADD", "register:40f0:8", ["const:885b30:8", "const:4:8"]]
- 00885b30 ["CALL", null, ["callee:00c53d00:8"]]
+ 00885b70 ["INT_ADD", "register:40f0:8", ["const:885b70:8", "const:4:8"]]
+ 00885b70 ["CALL", null, ["callee:00c53d00:8"]]
- 00885b30 bytes 6c370f94
+ 00885b70 bytes 64380f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18f7445eb9ef3a906d5e93716cb07011"></a>

### [`00885b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885b64.md) → [`00885ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885ba4.md) FUN_00885ba4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00885bbc",
      "incomplete_value": false,
      "site": "00885bc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885b7c",
      "incomplete_value": false,
      "site": "00885b88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "00885bc8",
      "DATA",
      [
        "storage",
        "00c80998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885bc8",
      "DATA",
      [
        "storage",
        "00c80d98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885b64.md#insn-00885b7c) · [`00885bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885b64.md#insn-00885bac) · [`00885bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885b64.md#insn-00885bc0)
- 新版 `00885bbc`（命令位置の公開資料なし） · `00885bec`（命令位置の公開資料なし） · `00885c00`（命令位置の公開資料なし）

~~~diff
- 00885b7c ["COPY", "tmp:0:8", ["const:998:8"]]
- 00885b7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00885b7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00885b7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00885bbc ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 00885bbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00885bbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00885bbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00885b7c bytes 08612691
+ 00885bbc bytes 08613691
- 00885bac ["COPY", "register:0:8", ["register:4040:8"]]
- 00885bac ["INT_ADD", "register:40f0:8", ["const:885bac:8", "const:4:8"]]
- 00885bac ["CALLIND", null, ["register:0:8"]]
+ 00885bec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885bec ["INT_ADD", "register:40f0:8", ["const:885bec:8", "const:4:8"]]
+ 00885bec ["CALLIND", null, ["register:0:8"]]
- 00885bac bytes 00013fd6
+ 00885bec bytes 00013fd6
- 00885bc0 ["INT_ADD", "register:40f0:8", ["const:885bc0:8", "const:4:8"]]
- 00885bc0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00885c00 ["INT_ADD", "register:40f0:8", ["const:885c00:8", "const:4:8"]]
+ 00885c00 ["CALL", null, ["callee:00c53d00:8"]]
- 00885bc0 bytes 48370f94
+ 00885c00 bytes 40380f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e8d5fb145ed7834638dcde58d391056"></a>

### [`00885bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885bf0.md) → [`00885c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885c30.md) FUN_00885c30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00885c58",
      "incomplete_value": false,
      "site": "00885c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885c18",
      "incomplete_value": false,
      "site": "00885c1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "00885c5c",
      "DATA",
      [
        "storage",
        "00c80998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885c5c",
      "DATA",
      [
        "storage",
        "00c80d98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885bf0.md#insn-00885c04) · [`00885c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885bf0.md#insn-00885c18) · [`00885c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885bf0.md#insn-00885c34)
- 新版 `00885c44`（命令位置の公開資料なし） · `00885c58`（命令位置の公開資料なし） · `00885c74`（命令位置の公開資料なし）

~~~diff
- 00885c04 ["INT_ADD", "register:40f0:8", ["const:885c04:8", "const:4:8"]]
- 00885c04 ["CALL", null, ["callee:00c57e90:8"]]
+ 00885c44 ["INT_ADD", "register:40f0:8", ["const:885c44:8", "const:4:8"]]
+ 00885c44 ["CALL", null, ["callee:00c57e90:8"]]
- 00885c04 bytes a3470f94
+ 00885c44 bytes 93480f94
- 00885c18 ["COPY", "tmp:0:8", ["const:998:8"]]
- 00885c18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00885c18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00885c18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00885c58 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 00885c58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00885c58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00885c58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00885c18 bytes 29612691
+ 00885c58 bytes 29613691
- 00885c34 ["INT_ADD", "register:40f0:8", ["const:885c34:8", "const:4:8"]]
- 00885c34 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00885c74 ["INT_ADD", "register:40f0:8", ["const:885c74:8", "const:4:8"]]
+ 00885c74 ["CALL", null, ["callee:00c53cd0:8"]]
- 00885c34 bytes 1f370f94
+ 00885c74 bytes 17380f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e7cd60578d59522fedb90d103ce52d3"></a>

### [`00885ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885ca0.md) → [`00885ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885ce0.md) FUN_00885ce0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "00885cfc",
      "incomplete_value": false,
      "site": "00885d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885cbc",
      "incomplete_value": false,
      "site": "00885cc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "00885d08",
      "DATA",
      [
        "storage",
        "00c80998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885d08",
      "DATA",
      [
        "storage",
        "00c80d98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885ca0.md#insn-00885cbc) · [`00885cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885ca0.md#insn-00885cdc) · [`00885cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885ca0.md#insn-00885cfc)
- 新版 `00885cfc`（命令位置の公開資料なし） · `00885d1c`（命令位置の公開資料なし） · `00885d3c`（命令位置の公開資料なし）

~~~diff
- 00885cbc ["COPY", "tmp:0:8", ["const:998:8"]]
- 00885cbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00885cbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00885cbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00885cfc ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 00885cfc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00885cfc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00885cfc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00885cbc bytes 29612691
+ 00885cfc bytes 29613691
- 00885cdc ["INT_ADD", "register:40f0:8", ["const:885cdc:8", "const:4:8"]]
- 00885cdc ["CALL", null, ["callee:00c53cd0:8"]]
+ 00885d1c ["INT_ADD", "register:40f0:8", ["const:885d1c:8", "const:4:8"]]
+ 00885d1c ["CALL", null, ["callee:00c53cd0:8"]]
- 00885cdc bytes f5360f94
+ 00885d1c bytes ed370f94
- 00885cfc ["COPY", "register:0:8", ["register:4040:8"]]
- 00885cfc ["INT_ADD", "register:40f0:8", ["const:885cfc:8", "const:4:8"]]
- 00885cfc ["CALLIND", null, ["register:0:8"]]
+ 00885d3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885d3c ["INT_ADD", "register:40f0:8", ["const:885d3c:8", "const:4:8"]]
+ 00885d3c ["CALLIND", null, ["register:0:8"]]
- 00885cfc bytes 00013fd6
+ 00885d3c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17734fcffef768cbb74b7b097d957782"></a>

### [`00885e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885e80.md) → [`00885ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885ec0.md) FUN_00885ec0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00885ed8",
      "incomplete_value": false,
      "site": "00885ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885e98",
      "incomplete_value": false,
      "site": "00885ea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a28:8"
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
      "00885ee4",
      "DATA",
      [
        "storage",
        "00c80a28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885ee4",
      "DATA",
      [
        "storage",
        "00c80e28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885e80.md#insn-00885e98) · [`00885ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885e80.md#insn-00885ec8)
- 新版 `00885ed8`（命令位置の公開資料なし） · `00885f08`（命令位置の公開資料なし）

~~~diff
- 00885e98 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 00885e98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00885e98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00885e98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00885ed8 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 00885ed8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00885ed8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00885ed8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00885e98 bytes 08a12891
+ 00885ed8 bytes 08a13891
- 00885ec8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885ec8 ["INT_ADD", "register:40f0:8", ["const:885ec8:8", "const:4:8"]]
- 00885ec8 ["CALLIND", null, ["register:0:8"]]
+ 00885f08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885f08 ["INT_ADD", "register:40f0:8", ["const:885f08:8", "const:4:8"]]
+ 00885f08 ["CALLIND", null, ["register:0:8"]]
- 00885ec8 bytes 00013fd6
+ 00885f08 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43350f540ab28ce66c7d2fb08828eb5e"></a>

### [`00885ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885ef0.md) → [`00885f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885f30.md) FUN_00885f30

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00885f48",
      "incomplete_value": false,
      "site": "00885f54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885f08",
      "incomplete_value": false,
      "site": "00885f14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a28:8"
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
      "00885f54",
      "DATA",
      [
        "storage",
        "00c80a28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885f54",
      "DATA",
      [
        "storage",
        "00c80e28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885ef0.md#insn-00885f08) · [`00885f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885ef0.md#insn-00885f38) · [`00885f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885ef0.md#insn-00885f48)
- 新版 `00885f48`（命令位置の公開資料なし） · `00885f78`（命令位置の公開資料なし） · `00885f88`（命令位置の公開資料なし）

~~~diff
- 00885f08 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 00885f08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00885f08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00885f08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00885f48 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 00885f48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00885f48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00885f48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00885f08 bytes 08a12891
+ 00885f48 bytes 08a13891
- 00885f38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885f38 ["INT_ADD", "register:40f0:8", ["const:885f38:8", "const:4:8"]]
- 00885f38 ["CALLIND", null, ["register:0:8"]]
+ 00885f78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885f78 ["INT_ADD", "register:40f0:8", ["const:885f78:8", "const:4:8"]]
+ 00885f78 ["CALLIND", null, ["register:0:8"]]
- 00885f38 bytes 00013fd6
+ 00885f78 bytes 00013fd6
- 00885f48 ["INT_ADD", "register:40f0:8", ["const:885f48:8", "const:4:8"]]
- 00885f48 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00885f88 ["INT_ADD", "register:40f0:8", ["const:885f88:8", "const:4:8"]]
+ 00885f88 ["CALL", null, ["callee:00c57eb0:8"]]
- 00885f48 bytes da460f94
+ 00885f88 bytes ca470f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48d8c455f327c34d77e703a1aab19e1a"></a>

### [`00885f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885f5c.md) → [`00885f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885f9c.md) FUN_00885f9c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00885fd0",
      "incomplete_value": false,
      "site": "00885fd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00885f90",
      "incomplete_value": false,
      "site": "00885f90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a28:8"
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
      "00885fd0",
      "DATA",
      [
        "storage",
        "00c80a28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885fd0",
      "DATA",
      [
        "storage",
        "00c80e28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885f5c.md#insn-00885f74) · [`00885f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885f5c.md#insn-00885f84) · [`00885f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885f5c.md#insn-00885f8c)
- 新版 `00885fb4`（命令位置の公開資料なし） · `00885fc4`（命令位置の公開資料なし）

~~~diff
- 00885f74 ["INT_ADD", "register:40f0:8", ["const:885f74:8", "const:4:8"]]
- 00885f74 ["CALL", null, ["callee:00c57e90:8"]]
+ 00885fb4 ["INT_ADD", "register:40f0:8", ["const:885fb4:8", "const:4:8"]]
+ 00885fb4 ["CALL", null, ["callee:00c57e90:8"]]
- 00885f74 bytes c7460f94
+ 00885fb4 bytes b7470f94
- 00885f84 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 00885f84 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00885f84 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00885f84 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00885fc4 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 00885fc4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00885fc4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00885fc4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00885f84 bytes 4aa12891
+ 00885fc4 bytes 4aa13891
- 00885f8c ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00885f8c bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbc4dc547367f6f7d39e9925dd19b8ac"></a>

### [`00886034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886034.md) → [`00886074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886074.md) FUN_00886074

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00886090",
      "incomplete_value": false,
      "site": "00886090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00886050",
      "incomplete_value": false,
      "site": "00886050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a28:8"
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
      "00886090",
      "DATA",
      [
        "storage",
        "00c80a28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886090",
      "DATA",
      [
        "storage",
        "00c80e28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886034.md#insn-00886048) · [`0088604c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886034.md#insn-0088604c) · [`0088608c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886034.md#insn-0088608c)
- 新版 `00886088`（命令位置の公開資料なし） · `008860cc`（命令位置の公開資料なし）

~~~diff
- 00886048 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 00886048 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00886048 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00886048 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00886088 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 00886088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00886088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00886088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00886048 bytes 08a12891
+ 00886088 bytes 08a13891
- 0088604c ["COPY", "register:40a0:8", ["register:4008:8"]]
- 0088604c bytes f40301aa
- 0088608c ["INT_ADD", "register:40f0:8", ["const:88608c:8", "const:4:8"]]
- 0088608c ["CALL", null, ["callee:0043bb20:8"]]
+ 008860cc ["INT_ADD", "register:40f0:8", ["const:8860cc:8", "const:4:8"]]
+ 008860cc ["CALL", null, ["callee:0043bb20:8"]]
- 0088608c bytes 95d6ee97
+ 008860cc bytes 95d6ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5135e80353b0531038b5ed79640438d4"></a>

### [`008861c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008861c0.md) → [`00886200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886200.md) FUN_00886200

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`0045579c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/0045579c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00764ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764ea0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`004557dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004557dc.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00764ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.52% / 新版 97.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008862e4",
      "incomplete_value": false,
      "site": "008862e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008862a4",
      "incomplete_value": false,
      "site": "008862a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00886240",
      "value": [
        "leaf",
        "ram:764ee0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00886200",
      "value": [
        "leaf",
        "ram:764ea0:8"
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
      "00886240",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ea0"
      ]
    ],
    [
      "008862e4",
      "DATA",
      [
        "storage",
        "00c80a98",
        null,
        "undefined *"
      ]
    ],
    [
      "00886360",
      "READ",
      [
        "storage",
        "00c80ac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886240",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ee0"
      ]
    ],
    [
      "008862e4",
      "DATA",
      [
        "storage",
        "00c80e98",
        null,
        "undefined *"
      ]
    ],
    [
      "00886360",
      "READ",
      [
        "storage",
        "00c80ec0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008861c0.md#insn-00886200) · [`008861f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008861c0.md#insn-008861f0) · [`008861f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008861c0.md#insn-008861f8)
- 新版 `00886240`（命令位置の公開資料なし） · `00886230`（命令位置の公開資料なし） · `00886238`（命令位置の公開資料なし）

~~~diff
- 00886200 ["INT_ADD", "register:40f0:8", ["const:886200:8", "const:4:8"]]
- 00886200 ["CALL", null, ["ram:764ea0:8"]]
+ 00886240 ["INT_ADD", "register:40f0:8", ["const:886240:8", "const:4:8"]]
+ 00886240 ["CALL", null, ["ram:764ee0:8"]]
- 00886200 bytes 287bfb97
+ 00886240 bytes 287bfb97
- 008861f0 ["INT_ADD", "register:40f0:8", ["const:8861f0:8", "const:4:8"]]
- 008861f0 ["CALL", null, ["callee:0044f8e0:8"]]
+ 00886230 ["INT_ADD", "register:40f0:8", ["const:886230:8", "const:4:8"]]
+ 00886230 ["CALL", null, ["callee:0044f8e0:8"]]
- 008861f0 bytes ac25ef97
+ 00886230 bytes ac25ef97
- 008861f8 ["INT_ADD", "register:40f0:8", ["const:8861f8:8", "const:4:8"]]
- 008861f8 ["CALL", null, ["callee:008514f8:8"]]
+ 00886238 ["INT_ADD", "register:40f0:8", ["const:886238:8", "const:4:8"]]
+ 00886238 ["CALL", null, ["callee:008514f8:8"]]
- 008861f8 bytes b02cff97
+ 00886238 bytes b02cff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-794df0dddec29d6feb4f399798079cb4"></a>

### [`008864d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008864d8.md) → [`00886518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886518.md) FUN_00886518

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00886530",
      "incomplete_value": false,
      "site": "0088653c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008864f0",
      "incomplete_value": false,
      "site": "008864fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "0088653c",
      "DATA",
      [
        "storage",
        "00c80a98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088653c",
      "DATA",
      [
        "storage",
        "00c80e98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008864f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008864d8.md#insn-008864f0) · [`00886520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008864d8.md#insn-00886520)
- 新版 `00886530`（命令位置の公開資料なし） · `00886560`（命令位置の公開資料なし）

~~~diff
- 008864f0 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 008864f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008864f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008864f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00886530 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00886530 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00886530 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00886530 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008864f0 bytes 08612a91
+ 00886530 bytes 08613a91
- 00886520 ["COPY", "register:0:8", ["register:4040:8"]]
- 00886520 ["INT_ADD", "register:40f0:8", ["const:886520:8", "const:4:8"]]
- 00886520 ["CALLIND", null, ["register:0:8"]]
+ 00886560 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886560 ["INT_ADD", "register:40f0:8", ["const:886560:8", "const:4:8"]]
+ 00886560 ["CALLIND", null, ["register:0:8"]]
- 00886520 bytes 00013fd6
+ 00886560 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f60003276ecec8e9ba3107c246a14ef8"></a>

### [`008865bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008865bc.md) → [`008865fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008865fc.md) FUN_008865fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00886618",
      "incomplete_value": false,
      "site": "00886618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008865d8",
      "incomplete_value": false,
      "site": "008865d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "00886618",
      "DATA",
      [
        "storage",
        "00c80a98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886618",
      "DATA",
      [
        "storage",
        "00c80e98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008865d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008865bc.md#insn-008865d4) · [`008865f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008865bc.md#insn-008865f8)
- 新版 `00886614`（命令位置の公開資料なし） · `00886638`（命令位置の公開資料なし）

~~~diff
- 008865d4 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 008865d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008865d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008865d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00886614 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00886614 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00886614 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00886614 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008865d4 bytes 29612a91
+ 00886614 bytes 29613a91
- 008865f8 ["COPY", "register:0:8", ["register:4048:8"]]
- 008865f8 ["INT_ADD", "register:40f0:8", ["const:8865f8:8", "const:4:8"]]
- 008865f8 ["CALLIND", null, ["register:0:8"]]
+ 00886638 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00886638 ["INT_ADD", "register:40f0:8", ["const:886638:8", "const:4:8"]]
+ 00886638 ["CALLIND", null, ["register:0:8"]]
- 008865f8 bytes 20013fd6
+ 00886638 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3137f348a4742b4d8833f958fdc29ebc"></a>

### [`00886878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886878.md) → [`008868b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008868b8.md) FUN_008868b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "008868cc",
      "incomplete_value": false,
      "site": "008868d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088688c",
      "incomplete_value": false,
      "site": "00886890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b38:8"
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
      "008868d0",
      "DATA",
      [
        "storage",
        "00c80b38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008868d0",
      "DATA",
      [
        "storage",
        "00c80f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886878.md#insn-0088688c) · [`008868a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886878.md#insn-008868a0) · [`008868c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886878.md#insn-008868c0)
- 新版 `008868cc`（命令位置の公開資料なし） · `008868e0`（命令位置の公開資料なし） · `00886900`（命令位置の公開資料なし）

~~~diff
- 0088688c ["COPY", "tmp:0:8", ["const:b38:8"]]
- 0088688c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088688c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088688c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008868cc ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 008868cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008868cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008868cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088688c bytes 08e12c91
+ 008868cc bytes 08e13c91
- 008868a0 ["INT_ADD", "register:40f0:8", ["const:8868a0:8", "const:4:8"]]
- 008868a0 ["CALL", null, ["callee:00c53d00:8"]]
+ 008868e0 ["INT_ADD", "register:40f0:8", ["const:8868e0:8", "const:4:8"]]
+ 008868e0 ["CALL", null, ["callee:00c53d00:8"]]
- 008868a0 bytes 10340f94
+ 008868e0 bytes 08350f94
- 008868c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008868c0 ["INT_ADD", "register:40f0:8", ["const:8868c0:8", "const:4:8"]]
- 008868c0 ["CALLIND", null, ["register:0:8"]]
+ 00886900 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886900 ["INT_ADD", "register:40f0:8", ["const:886900:8", "const:4:8"]]
+ 00886900 ["CALLIND", null, ["register:0:8"]]
- 008868c0 bytes 00013fd6
+ 00886900 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1e8fc0cd929db34b0c810533e30c895"></a>

### [`008868d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008868d4.md) → [`00886914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886914.md) FUN_00886914

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0088692c",
      "incomplete_value": false,
      "site": "00886930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008868ec",
      "incomplete_value": false,
      "site": "008868f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b38:8"
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
      "00886930",
      "DATA",
      [
        "storage",
        "00c80b38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886930",
      "DATA",
      [
        "storage",
        "00c80f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008868ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008868d4.md#insn-008868ec) · [`00886900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008868d4.md#insn-00886900) · [`00886914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008868d4.md#insn-00886914)
- 新版 `0088692c`（命令位置の公開資料なし） · `00886940`（命令位置の公開資料なし） · `00886954`（命令位置の公開資料なし）

~~~diff
- 008868ec ["COPY", "tmp:0:8", ["const:b38:8"]]
- 008868ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008868ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008868ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088692c ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 0088692c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088692c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088692c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008868ec bytes 08e12c91
+ 0088692c bytes 08e13c91
- 00886900 ["INT_ADD", "register:40f0:8", ["const:886900:8", "const:4:8"]]
- 00886900 ["CALL", null, ["callee:00c53d00:8"]]
+ 00886940 ["INT_ADD", "register:40f0:8", ["const:886940:8", "const:4:8"]]
+ 00886940 ["CALL", null, ["callee:00c53d00:8"]]
- 00886900 bytes f8330f94
+ 00886940 bytes f0340f94
- 00886914 ["COPY", "register:0:8", ["register:4040:8"]]
- 00886914 ["INT_ADD", "register:40f0:8", ["const:886914:8", "const:4:8"]]
- 00886914 ["CALLIND", null, ["register:0:8"]]
+ 00886954 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886954 ["INT_ADD", "register:40f0:8", ["const:886954:8", "const:4:8"]]
+ 00886954 ["CALLIND", null, ["register:0:8"]]
- 00886914 bytes 00013fd6
+ 00886954 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e625ce8f3799e7d4f15e9b1180d725f4"></a>

### [`00886930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886930.md) → [`00886970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886970.md) FUN_00886970

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00886994",
      "incomplete_value": true,
      "site": "00886998",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00886954",
      "incomplete_value": true,
      "site": "00886958",
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
            "const:b38:8"
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
      "00886998",
      "DATA",
      [
        "storage",
        "00c80b38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886998",
      "DATA",
      [
        "storage",
        "00c80f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886930.md#insn-00886944) · [`00886954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886930.md#insn-00886954) · [`00886974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886930.md#insn-00886974)
- 新版 `00886984`（命令位置の公開資料なし） · `00886994`（命令位置の公開資料なし） · `008869b4`（命令位置の公開資料なし）

~~~diff
- 00886944 ["INT_ADD", "register:40f0:8", ["const:886944:8", "const:4:8"]]
- 00886944 ["CALL", null, ["callee:00c57e90:8"]]
+ 00886984 ["INT_ADD", "register:40f0:8", ["const:886984:8", "const:4:8"]]
+ 00886984 ["CALL", null, ["callee:00c57e90:8"]]
- 00886944 bytes 53440f94
+ 00886984 bytes 43450f94
- 00886954 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 00886954 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00886954 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00886954 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00886994 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00886994 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00886994 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00886994 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00886954 bytes 29e12c91
+ 00886994 bytes 29e13c91
- 00886974 ["INT_ADD", "register:40f0:8", ["const:886974:8", "const:4:8"]]
- 00886974 ["CALL", null, ["callee:00c53cd0:8"]]
+ 008869b4 ["INT_ADD", "register:40f0:8", ["const:8869b4:8", "const:4:8"]]
+ 008869b4 ["CALL", null, ["callee:00c53cd0:8"]]
- 00886974 bytes cf330f94
+ 008869b4 bytes c7340f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-378c64967d42ca0b7b93186a7bca1e4c"></a>

### [`00886988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886988.md) → [`008869c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008869c8.md) FUN_008869c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008869d0",
      "incomplete_value": false,
      "site": "008869d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00886990",
      "incomplete_value": false,
      "site": "00886994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b38:8"
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
      "008869d4",
      "DATA",
      [
        "storage",
        "00c80b38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008869d4",
      "DATA",
      [
        "storage",
        "00c80f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886988.md#insn-00886990) · [`008869b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886988.md#insn-008869b8)
- 新版 `008869d0`（命令位置の公開資料なし） · `008869f8`（命令位置の公開資料なし）

~~~diff
- 00886990 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 00886990 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00886990 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00886990 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008869d0 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 008869d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008869d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008869d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00886990 bytes 29e12c91
+ 008869d0 bytes 29e13c91
- 008869b8 ["INT_ADD", "register:40f0:8", ["const:8869b8:8", "const:4:8"]]
- 008869b8 ["CALL", null, ["callee:00c53cd0:8"]]
+ 008869f8 ["INT_ADD", "register:40f0:8", ["const:8869f8:8", "const:4:8"]]
+ 008869f8 ["CALL", null, ["callee:00c53cd0:8"]]
- 008869b8 bytes be330f94
+ 008869f8 bytes b6340f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1470bc529d0e83d03cbd26830cac6df9"></a>

### [`00886a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886a64.md) → [`00886aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886aa4.md) FUN_00886aa4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`004567c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md) [`0046475c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/0046475c.md) [`00886ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886ed0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`00456808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md) [`0046479c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/0046479c.md) [`00886f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886f10.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00886c34",
      "incomplete_value": false,
      "site": "00886c34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00886bf4",
      "incomplete_value": false,
      "site": "00886bf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      "00886c34",
      "DATA",
      [
        "storage",
        "00c80ba8",
        null,
        "undefined *"
      ]
    ],
    [
      "00886c88",
      "READ",
      [
        "storage",
        "00c80bd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886c34",
      "DATA",
      [
        "storage",
        "00c80fa8",
        null,
        "undefined *"
      ]
    ],
    [
      "00886c88",
      "READ",
      [
        "storage",
        "00c80fd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886a64.md#insn-00886b88) · [`00886b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886a64.md#insn-00886b98) · [`00886b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886a64.md#insn-00886b9c)
- 新版 `00886bc8`（命令位置の公開資料なし） · `00886bd8`（命令位置の公開資料なし） · `00886bdc`（命令位置の公開資料なし）

~~~diff
- 00886b88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00886b88 ["INT_ADD", "register:40f0:8", ["const:886b88:8", "const:4:8"]]
- 00886b88 ["CALLIND", null, ["register:0:8"]]
+ 00886bc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886bc8 ["INT_ADD", "register:40f0:8", ["const:886bc8:8", "const:4:8"]]
+ 00886bc8 ["CALLIND", null, ["register:0:8"]]
- 00886b88 bytes 00013fd6
+ 00886bc8 bytes 00013fd6
- 00886b98 ["INT_ADD", "register:40f0:8", ["const:886b98:8", "const:4:8"]]
- 00886b98 ["CALL", null, ["callee:0043bb20:8"]]
+ 00886bd8 ["INT_ADD", "register:40f0:8", ["const:886bd8:8", "const:4:8"]]
+ 00886bd8 ["CALL", null, ["callee:0043bb20:8"]]
- 00886b98 bytes d2d3ee97
+ 00886bd8 bytes d2d3ee97
- 00886b9c ["INT_ADD", "register:40f0:8", ["const:886b9c:8", "const:4:8"]]
- 00886b9c ["CALL", null, ["callee:0044f8e0:8"]]
+ 00886bdc ["INT_ADD", "register:40f0:8", ["const:886bdc:8", "const:4:8"]]
+ 00886bdc ["CALL", null, ["callee:0044f8e0:8"]]
- 00886b9c bytes 4123ef97
+ 00886bdc bytes 4123ef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0d705ab73a71a9c03f4ff2ed7549de4"></a>

### [`00886da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886da0.md) → [`00886de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886de0.md) FUN_00886de0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00886de8",
      "incomplete_value": false,
      "site": "00886dec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00886da8",
      "incomplete_value": false,
      "site": "00886dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
      "00886dec",
      "DATA",
      [
        "storage",
        "00c80ba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886dec",
      "DATA",
      [
        "storage",
        "00c80fa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886da0.md#insn-00886da8)
- 新版 `00886de8`（命令位置の公開資料なし）

~~~diff
- 00886da8 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 00886da8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00886da8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00886da8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00886de8 ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 00886de8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00886de8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00886de8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00886da8 bytes 29a12e91
+ 00886de8 bytes 29a13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d116517787c3869d790c15e9e38457f"></a>

### [`00886dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886dc0.md) → [`00886e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886e00.md) FUN_00886e00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00886e08",
      "incomplete_value": false,
      "site": "00886e0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00886dc8",
      "incomplete_value": false,
      "site": "00886dcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
      "00886e0c",
      "DATA",
      [
        "storage",
        "00c80ba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886e0c",
      "DATA",
      [
        "storage",
        "00c80fa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886dc0.md#insn-00886dc8) · [`00886dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886dc0.md#insn-00886dec)
- 新版 `00886e08`（命令位置の公開資料なし） · `00886e2c`（命令位置の公開資料なし）

~~~diff
- 00886dc8 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 00886dc8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00886dc8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00886dc8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00886e08 ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 00886e08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00886e08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00886e08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00886dc8 bytes 29a12e91
+ 00886e08 bytes 29a13e91
- 00886dec ["INT_ADD", "register:40f0:8", ["const:886dec:8", "const:4:8"]]
- 00886dec ["CALL", null, ["callee:00c57eb0:8"]]
+ 00886e2c ["INT_ADD", "register:40f0:8", ["const:886e2c:8", "const:4:8"]]
+ 00886e2c ["CALL", null, ["callee:00c57eb0:8"]]
- 00886dec bytes 31430f94
+ 00886e2c bytes 21440f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f284fa688e3d277f95eb2623817fbe1"></a>

### [`00886e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886e7c.md) → [`00886ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886ebc.md) FUN_00886ebc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

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
      "definition_site": "00886ec8",
      "incomplete_value": false,
      "site": "00886ec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00886e88",
      "incomplete_value": false,
      "site": "00886e88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
      "00886ec8",
      "DATA",
      [
        "storage",
        "00c80ba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886ec8",
      "DATA",
      [
        "storage",
        "00c80fa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886e7c.md#insn-00886e84)
- 新版 `00886ec4`（命令位置の公開資料なし）

~~~diff
- 00886e84 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 00886e84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00886e84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00886e84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00886ec4 ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 00886ec4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00886ec4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00886ec4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00886e84 bytes 29a12e91
+ 00886ec4 bytes 29a13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-953f1a34c250920f342aa5f63b50e34f"></a>

### [`008870a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/008870a8.md) → [`008870e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008870e8.md) _INIT_164

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.01% / 新版 87.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00887148",
      "incomplete_value": true,
      "site": "00887164",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f39:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00887108",
      "incomplete_value": true,
      "site": "00887124",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:ef9:8"
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
      "definition_site": "00887168",
      "incomplete_value": true,
      "site": "00887184",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:dc2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00887128",
      "incomplete_value": true,
      "site": "00887144",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:d82:8"
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
      "definition_site": "00887188",
      "incomplete_value": true,
      "site": "008871a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f62:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00887148",
      "incomplete_value": true,
      "site": "00887160",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e95:8"
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
      "00887124",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00887148",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00887168",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00887124",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00887148",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00887168",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00887120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/008870a8.md#insn-00887120) · [`00887140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/008870a8.md#insn-00887140) · [`008872dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/008870a8.md#insn-008872dc)
- 新版 `00887160`（命令位置の公開資料なし） · `00887180`（命令位置の公開資料なし） · `0088731c`（命令位置の公開資料なし）

~~~diff
- 00887120 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 00887120 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00887120 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00887120 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00887160 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 00887160 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00887160 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00887160 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00887120 bytes 4a093691
+ 00887160 bytes 4a093791
- 00887140 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00887140 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00887140 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00887140 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00887180 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00887180 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00887180 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00887180 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00887140 bytes 4a553a91
+ 00887180 bytes 4a893d91
- 008872dc ["INT_ADD", "register:40f0:8", ["const:8872dc:8", "const:4:8"]]
- 008872dc ["CALL", null, ["callee:00c57e30:8"]]
+ 0088731c ["INT_ADD", "register:40f0:8", ["const:88731c:8", "const:4:8"]]
+ 0088731c ["CALL", null, ["callee:00c57e30:8"]]
- 008872dc bytes d5410f94
+ 0088731c bytes c5420f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cde581baf6d362b245f18b4a8908d7e"></a>

### [`00887438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887438.md) → [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) FUN_00887478

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 10件 [`0088a790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a790.md) [`0088ad28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088ad28.md) [`0088ae4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088ae4c.md) [`0088af70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088af70.md) [`0088b094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b094.md) · 呼出先 12件 [`00888df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888df0.md) [`00888df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888df4.md) [`00888e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888e3c.md) [`00888ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888ff0.md) [`00888ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888ff4.md)
- 新版 呼出元 10件 [`0088a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a7d0.md) [`0088ad68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ad68.md) [`0088ae8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ae8c.md) [`0088afb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088afb0.md) [`0088b0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b0d4.md) · 呼出先 12件 [`00888e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888e30.md) [`00888e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888e34.md) [`00888e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888e7c.md) [`00889030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889030.md) [`00889034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889034.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008874ac",
      "incomplete_value": false,
      "site": "008874b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088746c",
      "incomplete_value": false,
      "site": "00887470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c38:8"
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
      "definition_site": "008874e8",
      "incomplete_value": false,
      "site": "008874e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008874a8",
      "incomplete_value": false,
      "site": "008874a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:df0:8"
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
      "definition_site": "00887538",
      "incomplete_value": false,
      "site": "00887538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008874f8",
      "incomplete_value": false,
      "site": "008874f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e80:8"
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
      "008874b0",
      "DATA",
      [
        "storage",
        "00c80c38",
        null,
        "pointer"
      ]
    ],
    [
      "008874e8",
      "DATA",
      [
        "storage",
        "00c80df0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088751c",
      "READ",
      [
        "storage",
        "00c80e10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008874b0",
      "DATA",
      [
        "storage",
        "00c81038",
        null,
        "pointer"
      ]
    ],
    [
      "008874e8",
      "DATA",
      [
        "storage",
        "00c811f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088751c",
      "READ",
      [
        "storage",
        "00c81210",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00887468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887438.md#insn-00887468) · [`008874e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887438.md#insn-008874e8) · [`0088746c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887438.md#insn-0088746c)
- 新版 `008874a8`（命令位置の公開資料なし） · `00887528`（命令位置の公開資料なし） · `008874ac`（命令位置の公開資料なし）

~~~diff
- 00887468 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 008874a8 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00887468 bytes c81f00b0
+ 008874a8 bytes c81f00d0
- 008874e8 ["COPY", "tmp:0:8", ["const:e80:8"]]
- 008874e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008874e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008874e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00887528 ["COPY", "tmp:0:8", ["const:280:8"]]
+ 00887528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00887528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00887528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008874e8 bytes 08013a91
+ 00887528 bytes 08010a91
- 0088746c ["COPY", "tmp:0:8", ["const:c38:8"]]
- 0088746c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088746c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088746c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008874ac ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008874ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008874ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008874ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088746c bytes 08e13091
+ 008874ac bytes 08e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-342727618ca61f3b3e3691bcf5405bcd"></a>

### [`008876b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/008876b0.md) → [`008876f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008876f0.md) FUN_008876f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 0件 

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
      "definition_site": "00887704",
      "incomplete_value": false,
      "site": "00887708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:8b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008876c4",
      "incomplete_value": false,
      "site": "008876c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:876:8"
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
      "00887708",
      "DATA",
      [
        "storage",
        "002ba876",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00887708",
      "DATA",
      [
        "storage",
        "002ba8b6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008876c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/008876b0.md#insn-008876c4)
- 新版 `00887704`（命令位置の公開資料なし）

~~~diff
- 008876c4 ["COPY", "tmp:0:8", ["const:876:8"]]
- 008876c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008876c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008876c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00887704 ["COPY", "tmp:0:8", ["const:8b6:8"]]
+ 00887704 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00887704 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00887704 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008876c4 bytes 08d92191
+ 00887704 bytes 08d92291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c09ad2c4b5fdbe115496508a90c3444"></a>

### [`008877a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/008877a0.md) → [`008877e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008877e0.md) FUN_008877e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00a9abdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9abdc.md) · 呼出先 4件 [`00889b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889b5c.md) [`00889b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889b60.md) [`00b36fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36fb4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00a9add8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9a/00a9add8.md) · 呼出先 4件 [`00889b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889b9c.md) [`00889ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889ba0.md) [`00b373dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b373dc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "definition_site": "00887814",
      "incomplete_value": false,
      "site": "00887814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:410:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008877d4",
      "incomplete_value": false,
      "site": "008877d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:10:8"
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
      "00887814",
      "DATA",
      [
        "storage",
        "00c81010",
        null,
        "undefined *"
      ]
    ],
    [
      "00887854",
      "READ",
      [
        "storage",
        "00c81030",
        null,
        "pointer"
      ]
    ],
    [
      "00887854",
      "READ",
      [
        "storage",
        "00c81038",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00887814",
      "DATA",
      [
        "storage",
        "00c81410",
        null,
        "undefined *"
      ]
    ],
    [
      "00887854",
      "READ",
      [
        "storage",
        "00c81430",
        null,
        "pointer"
      ]
    ],
    [
      "00887854",
      "READ",
      [
        "storage",
        "00c81438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008877cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/008877a0.md#insn-008877cc) · [`008877ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/008877a0.md#insn-008877ec) · [`00887818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/008877a0.md#insn-00887818)
- 新版 `0088780c`（命令位置の公開資料なし） · `0088782c`（命令位置の公開資料なし） · `00887858`（命令位置の公開資料なし）

~~~diff
- 008877cc ["COPY", "tmp:0:8", ["const:10:8"]]
- 008877cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008877cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008877cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088780c ["COPY", "tmp:0:8", ["const:410:8"]]
+ 0088780c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088780c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088780c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008877cc bytes 08410091
+ 0088780c bytes 08411091
- 008877ec ["INT_ADD", "register:40f0:8", ["const:8877ec:8", "const:4:8"]]
- 008877ec ["CALL", null, ["callee:00b373dc:8"]]
+ 0088782c ["INT_ADD", "register:40f0:8", ["const:88782c:8", "const:4:8"]]
+ 0088782c ["CALL", null, ["callee:00b373dc:8"]]
- 008877ec bytes f2bd0a94
+ 0088782c bytes ecbe0a94
- 00887818 ["COPY", "register:0:8", ["register:4040:8"]]
- 00887818 ["INT_ADD", "register:40f0:8", ["const:887818:8", "const:4:8"]]
- 00887818 ["CALLIND", null, ["register:0:8"]]
+ 00887858 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00887858 ["INT_ADD", "register:40f0:8", ["const:887858:8", "const:4:8"]]
+ 00887858 ["CALLIND", null, ["register:0:8"]]
- 00887818 bytes 00013fd6
+ 00887858 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b24f150ba97db165f6ac7bc47826ca9b"></a>

### [`00887898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md) → [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) FUN_008878d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`006b37cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b37cc.md) [`0073c8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073c/0073c8f8.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 24件 [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`00597a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a4c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0087ea80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ea80.md) [`00887fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887fec.md)
- 新版 呼出元 7件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`006b380c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b380c.md) [`0073c938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073c/0073c938.md) [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) · 呼出先 24件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0087eac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eac0.md) [`0088802c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088802c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.76% / 新版 99.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00887a28",
      "incomplete_value": true,
      "site": "00887a30",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:680:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008879e8",
      "incomplete_value": true,
      "site": "008879f0",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:280:8"
              ]
            ]
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
      "00887a28",
      "READ",
      [
        "storage",
        "00c9b280",
        null,
        "pointer"
      ]
    ],
    [
      "00887a28",
      "PARAM",
      [
        "storage",
        "011232a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00887a28",
      "READ",
      [
        "storage",
        "00c9b680",
        null,
        "pointer"
      ]
    ],
    [
      "00887a28",
      "PARAM",
      [
        "storage",
        "011236a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008879f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md#insn-008879f0) · [`008879ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md#insn-008879ac) · [`008879d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md#insn-008879d0)
- 新版 `00887a30`（命令位置の公開資料なし） · `008879ec`（命令位置の公開資料なし） · `00887a10`（命令位置の公開資料なし）

~~~diff
- 008879f0 ["INT_ADD", "register:40f0:8", ["const:8879f0:8", "const:4:8"]]
- 008879f0 ["CALL", null, ["callee:0087eac0:8"]]
+ 00887a30 ["INT_ADD", "register:40f0:8", ["const:887a30:8", "const:4:8"]]
+ 00887a30 ["CALL", null, ["callee:0087eac0:8"]]
- 008879f0 bytes 24dcff97
+ 00887a30 bytes 24dcff97
- 008879ac ["INT_ADD", "register:40f0:8", ["const:8879ac:8", "const:4:8"]]
- 008879ac ["CALL", null, ["callee:0088ad68:8"]]
+ 008879ec ["INT_ADD", "register:40f0:8", ["const:8879ec:8", "const:4:8"]]
+ 008879ec ["CALL", null, ["callee:0088ad68:8"]]
- 008879ac bytes df0c0094
+ 008879ec bytes df0c0094
- 008879d0 ["INT_ADD", "register:40f0:8", ["const:8879d0:8", "const:4:8"]]
- 008879d0 ["CALL", null, ["callee:0088a8f0:8"]]
+ 00887a10 ["INT_ADD", "register:40f0:8", ["const:887a10:8", "const:4:8"]]
+ 00887a10 ["CALL", null, ["callee:0088a8f0:8"]]
- 008879d0 bytes b80b0094
+ 00887a10 bytes b80b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a084edbcfef9c95ccb8b801d6d775296"></a>

### [`008883e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/008883e8.md) → [`00888428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888428.md) FUN_00888428

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`006166dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006166dc.md) [`0062622c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/0062622c.md) [`006ff2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff2d8.md) [`007413cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00741/007413cc.md) [`007fd33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd33c.md) · 呼出先 11件 [`0058f3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f3f4.md) [`0088b8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b8f8.md) [`0088b8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b8fc.md) [`0088ba08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088ba08.md) [`0088ba0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088ba0c.md)
- 新版 呼出元 6件 [`0061671c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/0061671c.md) [`0062626c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/0062626c.md) [`006ff318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff318.md) [`0074140c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00741/0074140c.md) [`007fd37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd37c.md) · 呼出先 11件 [`0058f434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f434.md) [`0088b938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b938.md) [`0088b93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b93c.md) [`0088ba48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088ba48.md) [`0088ba4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088ba4c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.43% / 新版 95.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00888588",
      "incomplete_value": false,
      "site": "00888588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00888548",
      "incomplete_value": false,
      "site": "00888548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:440:8"
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
      "definition_site": "008885ac",
      "incomplete_value": false,
      "site": "008885ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088856c",
      "incomplete_value": false,
      "site": "0088856c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
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
      "definition_site": "008885c4",
      "incomplete_value": false,
      "site": "008885c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00888584",
      "incomplete_value": false,
      "site": "00888584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:540:8"
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
      "00888588",
      "DATA",
      [
        "storage",
        "00c81440",
        null,
        "undefined *"
      ]
    ],
    [
      "008885ac",
      "DATA",
      [
        "storage",
        "00c814c0",
        null,
        "undefined *"
      ]
    ],
    [
      "008885c4",
      "DATA",
      [
        "storage",
        "00c81540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00888588",
      "DATA",
      [
        "storage",
        "00c81840",
        null,
        "undefined *"
      ]
    ],
    [
      "008885ac",
      "DATA",
      [
        "storage",
        "00c818c0",
        null,
        "undefined *"
      ]
    ],
    [
      "008885c4",
      "DATA",
      [
        "storage",
        "00c81940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00888544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/008883e8.md#insn-00888544) · [`008884d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/008883e8.md#insn-008884d0) · [`008884fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/008883e8.md#insn-008884fc)
- 新版 `00888584`（命令位置の公開資料なし） · `00888510`（命令位置の公開資料なし） · `0088853c`（命令位置の公開資料なし）

~~~diff
- 00888544 ["COPY", "tmp:0:8", ["const:440:8"]]
- 00888544 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00888544 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00888544 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00888584 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 00888584 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00888584 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00888584 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00888544 bytes 29011191
+ 00888584 bytes 29012191
- 008884d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008884d0 ["INT_ADD", "register:40f0:8", ["const:8884d0:8", "const:4:8"]]
- 008884d0 ["CALLIND", null, ["register:0:8"]]
+ 00888510 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888510 ["INT_ADD", "register:40f0:8", ["const:888510:8", "const:4:8"]]
+ 00888510 ["CALLIND", null, ["register:0:8"]]
- 008884d0 bytes 00013fd6
+ 00888510 bytes 00013fd6
- 008884fc ["COPY", "register:0:8", ["register:4040:8"]]
- 008884fc ["INT_ADD", "register:40f0:8", ["const:8884fc:8", "const:4:8"]]
- 008884fc ["CALLIND", null, ["register:0:8"]]
+ 0088853c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088853c ["INT_ADD", "register:40f0:8", ["const:88853c:8", "const:4:8"]]
+ 0088853c ["CALLIND", null, ["register:0:8"]]
- 008884fc bytes 00013fd6
+ 0088853c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e4e1ebaa004b5268b3bddb7043b112c"></a>

### [`00888814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888814.md) → [`00888854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888854.md) FUN_00888854

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007fd5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd5b0.md) · 呼出先 4件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md)
- 新版 呼出元 1件 [`007fd5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5f0.md) · 呼出先 4件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00888934",
      "incomplete_value": false,
      "site": "00888944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008888f4",
      "incomplete_value": false,
      "site": "00888904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0088893c",
      "incomplete_value": false,
      "site": "00888944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008888fc",
      "incomplete_value": false,
      "site": "00888904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "00888934",
      "PARAM",
      [
        "storage",
        "00c80d28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0088893c",
      "PARAM",
      [
        "storage",
        "00c80d38",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00888934",
      "PARAM",
      [
        "storage",
        "00c81128",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0088893c",
      "PARAM",
      [
        "storage",
        "00c81138",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00888904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888814.md#insn-00888904) · [`00888944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888814.md#insn-00888944) · [`008888f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888814.md#insn-008888f0)
- 新版 `00888944`（命令位置の公開資料なし） · `00888984`（命令位置の公開資料なし） · `00888930`（命令位置の公開資料なし）

~~~diff
- 00888904 ["INT_ADD", "register:40f0:8", ["const:888904:8", "const:4:8"]]
- 00888904 ["CALL", null, ["callee:00c58610:8"]]
+ 00888944 ["INT_ADD", "register:40f0:8", ["const:888944:8", "const:4:8"]]
+ 00888944 ["CALL", null, ["callee:00c58610:8"]]
- 00888904 bytes 433e0f94
+ 00888944 bytes 333f0f94
- 00888944 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888944 ["INT_ADD", "register:40f0:8", ["const:888944:8", "const:4:8"]]
- 00888944 ["CALLIND", null, ["register:0:8"]]
+ 00888984 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888984 ["INT_ADD", "register:40f0:8", ["const:888984:8", "const:4:8"]]
+ 00888984 ["CALLIND", null, ["register:0:8"]]
- 00888944 bytes 00013fd6
+ 00888984 bytes 00013fd6
- 008888f0 ["COPY", "register:4008:8", ["const:c80000:8"]]
+ 00888930 ["COPY", "register:4008:8", ["const:c81000:8"]]
- 008888f0 bytes c11f0090
+ 00888930 bytes c11f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fe336dbfb6281844c1f28527a4ac893"></a>

### [`00888970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888970.md) → [`008889b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008889b0.md) FUN_008889b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`006ff600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff600.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 5件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md)
- 新版 呼出元 2件 [`006ff640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff640.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 5件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.55% / 新版 97.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00888c1c",
      "incomplete_value": false,
      "site": "00888c2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00888bdc",
      "incomplete_value": false,
      "site": "00888bec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00888c24",
      "incomplete_value": false,
      "site": "00888c2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00888be4",
      "incomplete_value": false,
      "site": "00888bec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "definition_site": "00888c74",
      "incomplete_value": false,
      "site": "00888c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00888c34",
      "incomplete_value": false,
      "site": "00888c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
      "00888c1c",
      "PARAM",
      [
        "storage",
        "00c80d28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00888c24",
      "PARAM",
      [
        "storage",
        "00c80db0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00888c74",
      "PARAM",
      [
        "storage",
        "00c80d28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00888c1c",
      "PARAM",
      [
        "storage",
        "00c81128",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00888c24",
      "PARAM",
      [
        "storage",
        "00c811b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00888c74",
      "PARAM",
      [
        "storage",
        "00c81128",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00888bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888970.md#insn-00888bec) · [`00888c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888970.md#insn-00888c44) · [`00888bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888970.md#insn-00888bd8)
- 新版 `00888c2c`（命令位置の公開資料なし） · `00888c84`（命令位置の公開資料なし） · `00888c18`（命令位置の公開資料なし）

~~~diff
- 00888bec ["INT_ADD", "register:40f0:8", ["const:888bec:8", "const:4:8"]]
- 00888bec ["CALL", null, ["callee:00c58610:8"]]
+ 00888c2c ["INT_ADD", "register:40f0:8", ["const:888c2c:8", "const:4:8"]]
+ 00888c2c ["CALL", null, ["callee:00c58610:8"]]
- 00888bec bytes 893d0f94
+ 00888c2c bytes 793e0f94
- 00888c44 ["INT_ADD", "register:40f0:8", ["const:888c44:8", "const:4:8"]]
- 00888c44 ["CALL", null, ["callee:00c58610:8"]]
+ 00888c84 ["INT_ADD", "register:40f0:8", ["const:888c84:8", "const:4:8"]]
+ 00888c84 ["CALL", null, ["callee:00c58610:8"]]
- 00888c44 bytes 733d0f94
+ 00888c84 bytes 633e0f94
- 00888bd8 ["COPY", "register:4008:8", ["const:c80000:8"]]
+ 00888c18 ["COPY", "register:4008:8", ["const:c81000:8"]]
- 00888bd8 bytes c11f0090
+ 00888c18 bytes c11f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-984c152a78d4945010cf5bfeeae0b416"></a>

### [`00888da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888da8.md) → [`00888de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888de8.md) FUN_00888de8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00888e0c",
      "incomplete_value": false,
      "site": "00888e0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00888dcc",
      "incomplete_value": false,
      "site": "00888dcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:df0:8"
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
      "00888e0c",
      "DATA",
      [
        "storage",
        "00c80df0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00888e0c",
      "DATA",
      [
        "storage",
        "00c811f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00888dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888da8.md#insn-00888dbc) · [`00888dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888da8.md#insn-00888dc4) · [`00888dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888da8.md#insn-00888dc8)
- 新版 `00888dfc`（命令位置の公開資料なし） · `00888e04`（命令位置の公開資料なし） · `00888e08`（命令位置の公開資料なし）

~~~diff
- 00888dbc ["INT_ADD", "register:40f0:8", ["const:888dbc:8", "const:4:8"]]
- 00888dbc ["CALL", null, ["callee:00c57e90:8"]]
+ 00888dfc ["INT_ADD", "register:40f0:8", ["const:888dfc:8", "const:4:8"]]
+ 00888dfc ["CALL", null, ["callee:00c57e90:8"]]
- 00888dbc bytes 353b0f94
+ 00888dfc bytes 253c0f94
- 00888dc4 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00888e04 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00888dc4 bytes c81f0090
+ 00888e04 bytes c81f00b0
- 00888dc8 ["COPY", "tmp:0:8", ["const:df0:8"]]
- 00888dc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00888dc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00888dc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00888e08 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 00888e08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00888e08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00888e08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00888dc8 bytes 08c13791
+ 00888e08 bytes 08c10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c66bef8a91918b42d22a84f1e8f0e6e"></a>

### [`00888ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888ddc.md) → [`00888e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888e1c.md) FUN_00888e1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00888e28",
      "incomplete_value": false,
      "site": "00888e28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00888de8",
      "incomplete_value": false,
      "site": "00888de8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:df0:8"
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
      "00888e28",
      "DATA",
      [
        "storage",
        "00c80df0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00888e28",
      "DATA",
      [
        "storage",
        "00c811f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00888de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888ddc.md#insn-00888de0) · [`00888de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888ddc.md#insn-00888de4)
- 新版 `00888e20`（命令位置の公開資料なし） · `00888e24`（命令位置の公開資料なし）

~~~diff
- 00888de0 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 00888e20 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 00888de0 bytes c91f0090
+ 00888e20 bytes c91f00b0
- 00888de4 ["COPY", "tmp:0:8", ["const:df0:8"]]
- 00888de4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00888de4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00888de4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00888e24 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 00888e24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00888e24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00888e24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00888de4 bytes 29c13791
+ 00888e24 bytes 29c10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6821a63b01bef97eb72832abc702cb1"></a>

### [`00888fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888fa8.md) → [`00888fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888fe8.md) FUN_00888fe8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0088900c",
      "incomplete_value": false,
      "site": "0088900c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00888fcc",
      "incomplete_value": false,
      "site": "00888fcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e80:8"
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
      "0088900c",
      "DATA",
      [
        "storage",
        "00c80e80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088900c",
      "DATA",
      [
        "storage",
        "00c81280",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00888fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888fa8.md#insn-00888fbc) · [`00888fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888fa8.md#insn-00888fc4) · [`00888fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888fa8.md#insn-00888fc8)
- 新版 `00888ffc`（命令位置の公開資料なし） · `00889004`（命令位置の公開資料なし） · `00889008`（命令位置の公開資料なし）

~~~diff
- 00888fbc ["INT_ADD", "register:40f0:8", ["const:888fbc:8", "const:4:8"]]
- 00888fbc ["CALL", null, ["callee:00c57e90:8"]]
+ 00888ffc ["INT_ADD", "register:40f0:8", ["const:888ffc:8", "const:4:8"]]
+ 00888ffc ["CALL", null, ["callee:00c57e90:8"]]
- 00888fbc bytes b53a0f94
+ 00888ffc bytes a53b0f94
- 00888fc4 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00889004 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00888fc4 bytes c81f0090
+ 00889004 bytes c81f0090
- 00888fc8 ["COPY", "tmp:0:8", ["const:e80:8"]]
- 00888fc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00888fc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00888fc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00889008 ["COPY", "tmp:0:8", ["const:280:8"]]
+ 00889008 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00889008 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00889008 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00888fc8 bytes 08013a91
+ 00889008 bytes 08010a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a77dad7f4649362e063afff0ea0bc19"></a>

### [`00888fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888fdc.md) → [`0088901c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/0088901c.md) FUN_0088901c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00889028",
      "incomplete_value": false,
      "site": "00889028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00888fe8",
      "incomplete_value": false,
      "site": "00888fe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e80:8"
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
      "00889028",
      "DATA",
      [
        "storage",
        "00c80e80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00889028",
      "DATA",
      [
        "storage",
        "00c81280",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00888fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888fdc.md#insn-00888fe0) · [`00888fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888fdc.md#insn-00888fe4)
- 新版 `00889020`（命令位置の公開資料なし） · `00889024`（命令位置の公開資料なし）

~~~diff
- 00888fe0 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 00889020 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 00888fe0 bytes c91f0090
+ 00889020 bytes c91f0090
- 00888fe4 ["COPY", "tmp:0:8", ["const:e80:8"]]
- 00888fe4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00888fe4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00888fe4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00889024 ["COPY", "tmp:0:8", ["const:280:8"]]
+ 00889024 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00889024 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00889024 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00888fe4 bytes 29013a91
+ 00889024 bytes 29010a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80b3b1de8146113bcdc270b15535b60c"></a>

### [`0088919c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/0088919c.md) → [`008891dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/008891dc.md) FUN_008891dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "008891f0",
      "incomplete_value": false,
      "site": "008891f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008891b0",
      "incomplete_value": false,
      "site": "008891b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:f10:8"
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
      "008891f4",
      "DATA",
      [
        "storage",
        "00c80f10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008891f4",
      "DATA",
      [
        "storage",
        "00c81310",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008891a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/0088919c.md#insn-008891a8) · [`008891ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/0088919c.md#insn-008891ac) · [`008891b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/0088919c.md#insn-008891b0)
- 新版 `008891e8`（命令位置の公開資料なし） · `008891ec`（命令位置の公開資料なし） · `008891f0`（命令位置の公開資料なし）

~~~diff
- 008891a8 ["INT_ADD", "register:40f0:8", ["const:8891a8:8", "const:4:8"]]
- 008891a8 ["CALL", null, ["callee:00c57e90:8"]]
+ 008891e8 ["INT_ADD", "register:40f0:8", ["const:8891e8:8", "const:4:8"]]
+ 008891e8 ["CALL", null, ["callee:00c57e90:8"]]
- 008891a8 bytes 3a3a0f94
+ 008891e8 bytes 2a3b0f94
- 008891ac ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 008891ec ["COPY", "register:4040:8", ["const:c81000:8"]]
- 008891ac bytes a81f00f0
+ 008891ec bytes c81f0090
- 008891b0 ["COPY", "tmp:0:8", ["const:f10:8"]]
- 008891b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008891b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008891b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008891f0 ["COPY", "tmp:0:8", ["const:310:8"]]
+ 008891f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008891f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008891f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008891b0 bytes 08413c91
+ 008891f0 bytes 08410c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d17958de76f5396303bdd0e747349e2"></a>

### [`008891c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/008891c0.md) → [`00889200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889200.md) FUN_00889200

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00889204",
      "incomplete_value": false,
      "site": "00889208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008891c4",
      "incomplete_value": false,
      "site": "008891c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:f10:8"
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
      "00889208",
      "DATA",
      [
        "storage",
        "00c80f10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00889208",
      "DATA",
      [
        "storage",
        "00c81310",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008891c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/008891c0.md#insn-008891c0) · [`008891c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/008891c0.md#insn-008891c4)
- 新版 `00889200`（命令位置の公開資料なし） · `00889204`（命令位置の公開資料なし）

~~~diff
- 008891c0 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00889200 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 008891c0 bytes a81f00f0
+ 00889200 bytes c81f0090
- 008891c4 ["COPY", "tmp:0:8", ["const:f10:8"]]
- 008891c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008891c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008891c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00889204 ["COPY", "tmp:0:8", ["const:310:8"]]
+ 00889204 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00889204 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00889204 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008891c4 bytes 08413c91
+ 00889204 bytes 08410c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dd4a67b0953a1d7b7dc60064cee1af0"></a>

### [`00889698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889698.md) → [`008896d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/008896d8.md) FUN_008896d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "008896fc",
      "incomplete_value": false,
      "site": "008896fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008896bc",
      "incomplete_value": false,
      "site": "008896bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:f90:8"
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
      "008896fc",
      "DATA",
      [
        "storage",
        "00c80f90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008896fc",
      "DATA",
      [
        "storage",
        "00c81390",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008896ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889698.md#insn-008896ac) · [`008896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889698.md#insn-008896b4) · [`008896b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889698.md#insn-008896b8)
- 新版 `008896ec`（命令位置の公開資料なし） · `008896f4`（命令位置の公開資料なし） · `008896f8`（命令位置の公開資料なし）

~~~diff
- 008896ac ["INT_ADD", "register:40f0:8", ["const:8896ac:8", "const:4:8"]]
- 008896ac ["CALL", null, ["callee:00c57e90:8"]]
+ 008896ec ["INT_ADD", "register:40f0:8", ["const:8896ec:8", "const:4:8"]]
+ 008896ec ["CALL", null, ["callee:00c57e90:8"]]
- 008896ac bytes f9380f94
+ 008896ec bytes e9390f94
- 008896b4 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 008896f4 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 008896b4 bytes a81f00f0
+ 008896f4 bytes c81f0090
- 008896b8 ["COPY", "tmp:0:8", ["const:f90:8"]]
- 008896b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008896b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008896b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008896f8 ["COPY", "tmp:0:8", ["const:390:8"]]
+ 008896f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008896f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008896f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008896b8 bytes 08413e91
+ 008896f8 bytes 08410e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-665117d3b5327b824f352ef06cf448a7"></a>

### [`008896cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/008896cc.md) → [`0088970c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/0088970c.md) FUN_0088970c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00889718",
      "incomplete_value": false,
      "site": "00889718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008896d8",
      "incomplete_value": false,
      "site": "008896d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:f90:8"
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
      "00889718",
      "DATA",
      [
        "storage",
        "00c80f90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00889718",
      "DATA",
      [
        "storage",
        "00c81390",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008896d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/008896cc.md#insn-008896d0) · [`008896d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/008896cc.md#insn-008896d4)
- 新版 `00889710`（命令位置の公開資料なし） · `00889714`（命令位置の公開資料なし）

~~~diff
- 008896d0 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 00889710 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 008896d0 bytes a91f00f0
+ 00889710 bytes c91f0090
- 008896d4 ["COPY", "tmp:0:8", ["const:f90:8"]]
- 008896d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008896d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008896d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00889714 ["COPY", "tmp:0:8", ["const:390:8"]]
+ 00889714 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00889714 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00889714 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008896d4 bytes 29413e91
+ 00889714 bytes 29410e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cabe1d249fcf9cdef2e28818cffa00f0"></a>

### [`00889b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889b48.md) → [`00889b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889b88.md) FUN_00889b88

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00889b94",
      "incomplete_value": false,
      "site": "00889b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:410:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889b54",
      "incomplete_value": false,
      "site": "00889b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:10:8"
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
      "00889b94",
      "DATA",
      [
        "storage",
        "00c81010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00889b94",
      "DATA",
      [
        "storage",
        "00c81410",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889b48.md#insn-00889b50)
- 新版 `00889b90`（命令位置の公開資料なし）

~~~diff
- 00889b50 ["COPY", "tmp:0:8", ["const:10:8"]]
- 00889b50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00889b50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00889b50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00889b90 ["COPY", "tmp:0:8", ["const:410:8"]]
+ 00889b90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00889b90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00889b90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00889b50 bytes 29410091
+ 00889b90 bytes 29411091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2acdd1620507fbb406c5b7d3daeba172"></a>

### [`00889b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889b64.md) → [`00889ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889ba4.md) FUN_00889ba4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00889d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889d28.md) [`00889d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889d2c.md) [`0088a124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a124.md) [`0088a128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a128.md) [`00b37760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b37760.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00889d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889d68.md) [`00889d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889d6c.md) [`0088a164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a164.md) [`0088a168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a168.md) [`00b37b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b37b88.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.34% / 新版 94.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00889be8",
      "incomplete_value": false,
      "site": "00889be8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889ba8",
      "incomplete_value": false,
      "site": "00889ba8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:100:8"
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
      "00889bdc",
      "DATA",
      [
        "storage",
        "00c81080",
        null,
        "undefined *"
      ]
    ],
    [
      "00889be8",
      "DATA",
      [
        "storage",
        "00c81100",
        null,
        "undefined *"
      ]
    ],
    [
      "00889c1c",
      "READ",
      [
        "storage",
        "00c81120",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00889bdc",
      "DATA",
      [
        "storage",
        "00c81480",
        null,
        "undefined *"
      ]
    ],
    [
      "00889be8",
      "DATA",
      [
        "storage",
        "00c81500",
        null,
        "undefined *"
      ]
    ],
    [
      "00889c1c",
      "READ",
      [
        "storage",
        "00c81520",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889b64.md#insn-00889b7c) · [`00889ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889b64.md#insn-00889ba4) · [`00889bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889b64.md#insn-00889bb4)
- 新版 `00889bbc`（命令位置の公開資料なし） · `00889be4`（命令位置の公開資料なし） · `00889bf4`（命令位置の公開資料なし）

~~~diff
- 00889b7c ["COPY", "tmp:0:8", ["const:80:8"]]
- 00889b7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00889b7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00889b7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00889bbc ["COPY", "tmp:0:8", ["const:480:8"]]
+ 00889bbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00889bbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00889bbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00889b7c bytes 29010291
+ 00889bbc bytes 29011291
- 00889ba4 ["COPY", "tmp:0:8", ["const:100:8"]]
- 00889ba4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00889ba4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00889ba4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00889be4 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 00889be4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00889be4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00889be4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00889ba4 bytes 29010491
+ 00889be4 bytes 29011491
- 00889bb4 ["INT_ADD", "register:40f0:8", ["const:889bb4:8", "const:4:8"]]
- 00889bb4 ["CALL", null, ["callee:00b37b88:8"]]
+ 00889bf4 ["INT_ADD", "register:40f0:8", ["const:889bf4:8", "const:4:8"]]
+ 00889bf4 ["CALL", null, ["callee:00b37b88:8"]]
- 00889bb4 bytes ebb60a94
+ 00889bf4 bytes e5b70a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fcb3a2ba062944ae03b7383abc9ada6"></a>

### [`00889ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889ce0.md) → [`00889d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889d20.md) FUN_00889d20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00889d44",
      "incomplete_value": false,
      "site": "00889d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889d04",
      "incomplete_value": false,
      "site": "00889d04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "00889d44",
      "DATA",
      [
        "storage",
        "00c81080",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00889d44",
      "DATA",
      [
        "storage",
        "00c81480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889ce0.md#insn-00889cf4) · [`00889d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889ce0.md#insn-00889d00)
- 新版 `00889d34`（命令位置の公開資料なし） · `00889d40`（命令位置の公開資料なし）

~~~diff
- 00889cf4 ["INT_ADD", "register:40f0:8", ["const:889cf4:8", "const:4:8"]]
- 00889cf4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00889d34 ["INT_ADD", "register:40f0:8", ["const:889d34:8", "const:4:8"]]
+ 00889d34 ["CALL", null, ["callee:00c57e90:8"]]
- 00889cf4 bytes 67370f94
+ 00889d34 bytes 57380f94
- 00889d00 ["COPY", "tmp:0:8", ["const:80:8"]]
- 00889d00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00889d00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00889d00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00889d40 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 00889d40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00889d40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00889d40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00889d00 bytes 08010291
+ 00889d40 bytes 08011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-751afce2fcd879a5467b9d1127e91ac9"></a>

### [`00889d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889d14.md) → [`00889d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889d54.md) FUN_00889d54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00889d60",
      "incomplete_value": false,
      "site": "00889d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889d20",
      "incomplete_value": false,
      "site": "00889d20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "00889d60",
      "DATA",
      [
        "storage",
        "00c81080",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00889d60",
      "DATA",
      [
        "storage",
        "00c81480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889d14.md#insn-00889d1c)
- 新版 `00889d5c`（命令位置の公開資料なし）

~~~diff
- 00889d1c ["COPY", "tmp:0:8", ["const:80:8"]]
- 00889d1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00889d1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00889d1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00889d5c ["COPY", "tmp:0:8", ["const:480:8"]]
+ 00889d5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00889d5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00889d5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00889d1c bytes 29010291
+ 00889d5c bytes 29011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddf3ecfb74656a3ddfae5dd16d471d8f"></a>

### [`00889d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889d30.md) → [`00889d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889d70.md) FUN_00889d70

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0052dcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dcc0.md) [`0066d0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d0bc.md) [`006a2b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a2b38.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0052dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md) [`0066d0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d0fc.md) [`006a2b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2b78.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.41% / 新版 96.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00889e08",
      "incomplete_value": true,
      "site": "00889e08",
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
                "const:6af:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889dc8",
      "incomplete_value": true,
      "site": "00889dc8",
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
                "const:5e2:8"
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
      "definition_site": "00889e90",
      "incomplete_value": true,
      "site": "00889e90",
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
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:996:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889e50",
      "incomplete_value": true,
      "site": "00889e50",
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
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:956:8"
              ]
            ]
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
      "00889df8",
      "READ",
      [
        "storage",
        "002a05e2",
        null,
        "string"
      ]
    ],
    [
      "00889e6c",
      "READ",
      [
        "storage",
        "002bb956",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00889df8",
      "READ",
      [
        "storage",
        "002a06af",
        null,
        "string"
      ]
    ],
    [
      "00889e6c",
      "READ",
      [
        "storage",
        "002bb996",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889d30.md#insn-00889d68) · [`00889d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889d30.md#insn-00889d74) · [`00889d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889d30.md#insn-00889d7c)
- 新版 `00889da8`（命令位置の公開資料なし） · `00889db4`（命令位置の公開資料なし） · `00889dbc`（命令位置の公開資料なし）

~~~diff
- 00889d68 ["INT_ADD", "register:40f0:8", ["const:889d68:8", "const:4:8"]]
- 00889d68 ["CALL", null, ["callee:00c580e0:8"]]
+ 00889da8 ["INT_ADD", "register:40f0:8", ["const:889da8:8", "const:4:8"]]
+ 00889da8 ["CALL", null, ["callee:00c580e0:8"]]
- 00889d68 bytes de370f94
+ 00889da8 bytes ce380f94
- 00889d74 ["INT_ADD", "register:40f0:8", ["const:889d74:8", "const:4:8"]]
- 00889d74 ["CALL", null, ["callee:00c58380:8"]]
+ 00889db4 ["INT_ADD", "register:40f0:8", ["const:889db4:8", "const:4:8"]]
+ 00889db4 ["CALL", null, ["callee:00c58380:8"]]
- 00889d74 bytes 83380f94
+ 00889db4 bytes 73390f94
- 00889d7c ["INT_ADD", "register:40f0:8", ["const:889d7c:8", "const:4:8"]]
- 00889d7c ["CALL", null, ["callee:00c580f0:8"]]
+ 00889dbc ["INT_ADD", "register:40f0:8", ["const:889dbc:8", "const:4:8"]]
+ 00889dbc ["CALL", null, ["callee:00c580f0:8"]]
- 00889d7c bytes dd370f94
+ 00889dbc bytes cd380f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e516d55fdb0c5e7919702095ff5fb9fa"></a>

### [`0088a0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a0dc.md) → [`0088a11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a11c.md) FUN_0088a11c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0088a140",
      "incomplete_value": false,
      "site": "0088a140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a100",
      "incomplete_value": false,
      "site": "0088a100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "0088a140",
      "DATA",
      [
        "storage",
        "00c81100",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088a140",
      "DATA",
      [
        "storage",
        "00c81500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a0dc.md#insn-0088a0f0) · [`0088a0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a0dc.md#insn-0088a0fc)
- 新版 `0088a130`（命令位置の公開資料なし） · `0088a13c`（命令位置の公開資料なし）

~~~diff
- 0088a0f0 ["INT_ADD", "register:40f0:8", ["const:88a0f0:8", "const:4:8"]]
- 0088a0f0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0088a130 ["INT_ADD", "register:40f0:8", ["const:88a130:8", "const:4:8"]]
+ 0088a130 ["CALL", null, ["callee:00c57e90:8"]]
- 0088a0f0 bytes 68360f94
+ 0088a130 bytes 58370f94
- 0088a0fc ["COPY", "tmp:0:8", ["const:100:8"]]
- 0088a0fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088a0fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088a0fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088a13c ["COPY", "tmp:0:8", ["const:500:8"]]
+ 0088a13c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a13c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a13c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088a0fc bytes 08010491
+ 0088a13c bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23fa74393d7fc6c2f47bf873ed891b80"></a>

### [`0088a110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a110.md) → [`0088a150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a150.md) FUN_0088a150

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088a15c",
      "incomplete_value": false,
      "site": "0088a15c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a11c",
      "incomplete_value": false,
      "site": "0088a11c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "0088a15c",
      "DATA",
      [
        "storage",
        "00c81100",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088a15c",
      "DATA",
      [
        "storage",
        "00c81500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a110.md#insn-0088a118)
- 新版 `0088a158`（命令位置の公開資料なし）

~~~diff
- 0088a118 ["COPY", "tmp:0:8", ["const:100:8"]]
- 0088a118 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088a118 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088a118 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088a158 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 0088a158 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088a158 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088a158 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088a118 bytes 29010491
+ 0088a158 bytes 29011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea353c12ac3440b7805384bc7bd482c3"></a>

### [`0088a12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a12c.md) → [`0088a16c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a16c.md) FUN_0088a16c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`0048ce10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce10.md) [`0069eed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069e/0069eed4.md) [`006a2b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a2b38.md) [`006a2d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a2d08.md) [`006a2d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a2d0c.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0048ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce50.md) [`0069ef14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069ef14.md) [`006a2b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2b78.md) [`006a2d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2d48.md) [`006a2d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2d4c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088a208",
      "incomplete_value": false,
      "site": "0088a214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a1c8",
      "incomplete_value": false,
      "site": "0088a1d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:170:8"
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
      "definition_site": "0088a1c8",
      "incomplete_value": false,
      "site": "0088a1d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:6a2000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a188",
      "incomplete_value": false,
      "site": "0088a194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:6a2000:8"
          ],
          [
            "leaf",
            "const:d08:8"
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
      "0088a1c8",
      "PARAM",
      [
        "storage",
        "006a2d08",
        null,
        null
      ]
    ],
    [
      "0088a214",
      "DATA",
      [
        "storage",
        "00c81170",
        null,
        "undefined *"
      ]
    ],
    [
      "0088a260",
      "READ",
      [
        "storage",
        "00c81190",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0088a1c8",
      "PARAM",
      [
        "storage",
        "006a2d48",
        null,
        null
      ]
    ],
    [
      "0088a214",
      "DATA",
      [
        "storage",
        "00c81570",
        null,
        "undefined *"
      ]
    ],
    [
      "0088a260",
      "READ",
      [
        "storage",
        "00c81590",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a12c.md#insn-0088a194) · [`0088a15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a12c.md#insn-0088a15c) · [`0088a188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a12c.md#insn-0088a188)
- 新版 `0088a1d4`（命令位置の公開資料なし） · `0088a19c`（命令位置の公開資料なし） · `0088a1c8`（命令位置の公開資料なし）

~~~diff
- 0088a194 ["INT_ADD", "register:40f0:8", ["const:88a194:8", "const:4:8"]]
- 0088a194 ["CALL", null, ["callee:006a2d4c:8"]]
+ 0088a1d4 ["INT_ADD", "register:40f0:8", ["const:88a1d4:8", "const:4:8"]]
+ 0088a1d4 ["CALL", null, ["callee:006a2d4c:8"]]
- 0088a194 bytes de62f897
+ 0088a1d4 bytes de62f897
- 0088a15c ["INT_ADD", "register:40f0:8", ["const:88a15c:8", "const:4:8"]]
- 0088a15c ["CALL", null, ["callee:00c57e90:8"]]
+ 0088a19c ["INT_ADD", "register:40f0:8", ["const:88a19c:8", "const:4:8"]]
+ 0088a19c ["CALL", null, ["callee:00c57e90:8"]]
- 0088a15c bytes 4d360f94
+ 0088a19c bytes 3d370f94
- 0088a188 ["COPY", "tmp:0:8", ["const:d08:8"]]
- 0088a188 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0088a188 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0088a188 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0088a1c8 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 0088a1c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0088a1c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0088a1c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0088a188 bytes 21203491
+ 0088a1c8 bytes 21203591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-687d35bd9e0982a57701f06f7684cd4b"></a>

### [`0088a30c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a30c.md) → [`0088a34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a34c.md) FUN_0088a34c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0088a360",
      "incomplete_value": false,
      "site": "0088a364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a320",
      "incomplete_value": false,
      "site": "0088a324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:170:8"
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
      "0088a364",
      "DATA",
      [
        "storage",
        "00c81170",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088a364",
      "DATA",
      [
        "storage",
        "00c81570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a30c.md#insn-0088a318) · [`0088a320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a30c.md#insn-0088a320)
- 新版 `0088a358`（命令位置の公開資料なし） · `0088a360`（命令位置の公開資料なし）

~~~diff
- 0088a318 ["INT_ADD", "register:40f0:8", ["const:88a318:8", "const:4:8"]]
- 0088a318 ["CALL", null, ["callee:00c57e90:8"]]
+ 0088a358 ["INT_ADD", "register:40f0:8", ["const:88a358:8", "const:4:8"]]
+ 0088a358 ["CALL", null, ["callee:00c57e90:8"]]
- 0088a318 bytes de350f94
+ 0088a358 bytes ce360f94
- 0088a320 ["COPY", "tmp:0:8", ["const:170:8"]]
- 0088a320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088a320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088a320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088a360 ["COPY", "tmp:0:8", ["const:570:8"]]
+ 0088a360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088a320 bytes 08c10591
+ 0088a360 bytes 08c11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-478cb795bd3793cdb88593c7cea5ceb8"></a>

### [`0088a330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a330.md) → [`0088a370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a370.md) FUN_0088a370

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088a374",
      "incomplete_value": false,
      "site": "0088a378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a334",
      "incomplete_value": false,
      "site": "0088a338",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "0088a378",
      "DATA",
      [
        "storage",
        "00c81170",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088a378",
      "DATA",
      [
        "storage",
        "00c81570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a330.md#insn-0088a334)
- 新版 `0088a374`（命令位置の公開資料なし）

~~~diff
- 0088a334 ["COPY", "tmp:0:8", ["const:170:8"]]
- 0088a334 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088a334 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088a334 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088a374 ["COPY", "tmp:0:8", ["const:570:8"]]
+ 0088a374 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a374 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a374 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088a334 bytes 08c10591
+ 0088a374 bytes 08c11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d405c1ac75d35de509c3ade82831f1f5"></a>

### [`0088a790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a790.md) → [`0088a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a7d0.md) FUN_0088a7d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00887898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md) · 呼出先 3件 [`00887438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887438.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)
- 新版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 3件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088a828",
      "incomplete_value": false,
      "site": "0088a82c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a7e8",
      "incomplete_value": false,
      "site": "0088a7ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c58:8"
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
      "definition_site": "0088a844",
      "incomplete_value": false,
      "site": "0088a84c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a804",
      "incomplete_value": false,
      "site": "0088a80c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:fc4:8"
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
      "definition_site": "0088a854",
      "incomplete_value": false,
      "site": "0088a85c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:e76:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a814",
      "incomplete_value": false,
      "site": "0088a81c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:e36:8"
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
      "0088a814",
      "DATA",
      [
        "storage",
        "00c81210",
        null,
        "undefined *"
      ]
    ],
    [
      "0088a82c",
      "DATA",
      [
        "storage",
        "00c80c58",
        null,
        "pointer"
      ]
    ],
    [
      "0088a844",
      "PARAM",
      [
        "storage",
        "002b2fc4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088a814",
      "DATA",
      [
        "storage",
        "00c81610",
        null,
        "undefined *"
      ]
    ],
    [
      "0088a82c",
      "DATA",
      [
        "storage",
        "00c81058",
        null,
        "pointer"
      ]
    ],
    [
      "0088a844",
      "PARAM",
      [
        "storage",
        "002b3004",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a790.md#insn-0088a7dc) · [`0088a80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a790.md#insn-0088a80c) · [`0088a81c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a790.md#insn-0088a81c)
- 新版 `0088a81c`（命令位置の公開資料なし） · `0088a84c`（命令位置の公開資料なし） · `0088a85c`（命令位置の公開資料なし）

~~~diff
- 0088a7dc ["INT_ADD", "register:40f0:8", ["const:88a7dc:8", "const:4:8"]]
- 0088a7dc ["CALL", null, ["callee:00887478:8"]]
+ 0088a81c ["INT_ADD", "register:40f0:8", ["const:88a81c:8", "const:4:8"]]
+ 0088a81c ["CALL", null, ["callee:00887478:8"]]
- 0088a7dc bytes 17f3ff97
+ 0088a81c bytes 17f3ff97
- 0088a80c ["INT_ADD", "register:40f0:8", ["const:88a80c:8", "const:4:8"]]
- 0088a80c ["CALL", null, ["callee:00c58190:8"]]
+ 0088a84c ["INT_ADD", "register:40f0:8", ["const:88a84c:8", "const:4:8"]]
+ 0088a84c ["CALL", null, ["callee:00c58190:8"]]
- 0088a80c bytes 61350f94
+ 0088a84c bytes 51360f94
- 0088a81c ["INT_ADD", "register:40f0:8", ["const:88a81c:8", "const:4:8"]]
- 0088a81c ["CALL", null, ["callee:00c58190:8"]]
+ 0088a85c ["INT_ADD", "register:40f0:8", ["const:88a85c:8", "const:4:8"]]
+ 0088a85c ["CALL", null, ["callee:00c58190:8"]]
- 0088a81c bytes 5d350f94
+ 0088a85c bytes 4d360f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87b03fabdc36bc044d5e04c761132f9c"></a>

### [`0088a864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a864.md) → [`0088a8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a8a4.md) FUN_0088a8a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "0088a8a8",
      "incomplete_value": false,
      "site": "0088a8ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a868",
      "incomplete_value": false,
      "site": "0088a86c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:210:8"
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
      "0088a8ac",
      "DATA",
      [
        "storage",
        "00c81210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088a8ac",
      "DATA",
      [
        "storage",
        "00c81610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a864.md#insn-0088a868)
- 新版 `0088a8a8`（命令位置の公開資料なし）

~~~diff
- 0088a868 ["COPY", "tmp:0:8", ["const:210:8"]]
- 0088a868 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088a868 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088a868 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088a8a8 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 0088a8a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a8a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a8a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088a868 bytes 08410891
+ 0088a8a8 bytes 08411891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-834e393a6a1e9ad6190bf8f8f7ad20b3"></a>

### [`0088a874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a874.md) → [`0088a8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a8b4.md) FUN_0088a8b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0088a8c4",
      "incomplete_value": false,
      "site": "0088a8cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a884",
      "incomplete_value": false,
      "site": "0088a88c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:210:8"
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
      "0088a8cc",
      "DATA",
      [
        "storage",
        "00c81210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088a8cc",
      "DATA",
      [
        "storage",
        "00c81610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a874.md#insn-0088a884) · [`0088a890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a874.md#insn-0088a890)
- 新版 `0088a8c4`（命令位置の公開資料なし） · `0088a8d0`（命令位置の公開資料なし）

~~~diff
- 0088a884 ["COPY", "tmp:0:8", ["const:210:8"]]
- 0088a884 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088a884 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088a884 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088a8c4 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 0088a8c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a8c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a8c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088a884 bytes 08410891
+ 0088a8c4 bytes 08411891
- 0088a890 ["INT_ADD", "register:40f0:8", ["const:88a890:8", "const:4:8"]]
- 0088a890 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0088a8d0 ["INT_ADD", "register:40f0:8", ["const:88a8d0:8", "const:4:8"]]
+ 0088a8d0 ["CALL", null, ["callee:00c57ea0:8"]]
- 0088a890 bytes 84340f94
+ 0088a8d0 bytes 74350f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-041d91708aef05ddb59a423c82d000cd"></a>

### [`0088ad28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088ad28.md) → [`0088ad68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ad68.md) FUN_0088ad68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00887898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md) · 呼出先 3件 [`00887438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887438.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)
- 新版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 3件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088ada0",
      "incomplete_value": false,
      "site": "0088adac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088ad60",
      "incomplete_value": false,
      "site": "0088ad6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:260:8"
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
      "definition_site": "0088adc0",
      "incomplete_value": false,
      "site": "0088adc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088ad80",
      "incomplete_value": false,
      "site": "0088ad84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "definition_site": "0088ade0",
      "incomplete_value": false,
      "site": "0088ade8",
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
            "const:e35:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088ada0",
      "incomplete_value": false,
      "site": "0088ada8",
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
            "const:d59:8"
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
      "0088adac",
      "DATA",
      [
        "storage",
        "00c81260",
        null,
        "undefined *"
      ]
    ],
    [
      "0088adc4",
      "DATA",
      [
        "storage",
        "00c80c78",
        null,
        "pointer"
      ]
    ],
    [
      "0088ade0",
      "PARAM",
      [
        "storage",
        "002a7d59",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088adac",
      "DATA",
      [
        "storage",
        "00c81660",
        null,
        "undefined *"
      ]
    ],
    [
      "0088adc4",
      "DATA",
      [
        "storage",
        "00c81078",
        null,
        "pointer"
      ]
    ],
    [
      "0088ade0",
      "PARAM",
      [
        "storage",
        "002a7e35",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088ada8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088ad28.md#insn-0088ada8) · [`0088adb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088ad28.md#insn-0088adb8) · [`0088ad4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088ad28.md#insn-0088ad4c)
- 新版 `0088ade8`（命令位置の公開資料なし） · `0088adf8`（命令位置の公開資料なし） · `0088ad8c`（命令位置の公開資料なし）

~~~diff
- 0088ada8 ["INT_ADD", "register:40f0:8", ["const:88ada8:8", "const:4:8"]]
- 0088ada8 ["CALL", null, ["callee:00c58190:8"]]
+ 0088ade8 ["INT_ADD", "register:40f0:8", ["const:88ade8:8", "const:4:8"]]
+ 0088ade8 ["CALL", null, ["callee:00c58190:8"]]
- 0088ada8 bytes fa330f94
+ 0088ade8 bytes ea340f94
- 0088adb8 ["INT_ADD", "register:40f0:8", ["const:88adb8:8", "const:4:8"]]
- 0088adb8 ["CALL", null, ["callee:00c58190:8"]]
+ 0088adf8 ["INT_ADD", "register:40f0:8", ["const:88adf8:8", "const:4:8"]]
+ 0088adf8 ["CALL", null, ["callee:00c58190:8"]]
- 0088adb8 bytes f6330f94
+ 0088adf8 bytes e6340f94
- 0088ad4c ["INT_ADD", "register:40f0:8", ["const:88ad4c:8", "const:4:8"]]
- 0088ad4c ["CALL", null, ["callee:00c57e90:8"]]
+ 0088ad8c ["INT_ADD", "register:40f0:8", ["const:88ad8c:8", "const:4:8"]]
+ 0088ad8c ["CALL", null, ["callee:00c57e90:8"]]
- 0088ad4c bytes 51330f94
+ 0088ad8c bytes 41340f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f629d7c989e94d6099441f4d843318ac"></a>

### [`0088ae00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088ae00.md) → [`0088ae40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ae40.md) FUN_0088ae40

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "0088ae44",
      "incomplete_value": false,
      "site": "0088ae48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088ae04",
      "incomplete_value": false,
      "site": "0088ae08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:260:8"
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
      "0088ae48",
      "DATA",
      [
        "storage",
        "00c81260",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088ae48",
      "DATA",
      [
        "storage",
        "00c81660",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088ae04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088ae00.md#insn-0088ae04)
- 新版 `0088ae44`（命令位置の公開資料なし）

~~~diff
- 0088ae04 ["COPY", "tmp:0:8", ["const:260:8"]]
- 0088ae04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088ae04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088ae04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088ae44 ["COPY", "tmp:0:8", ["const:660:8"]]
+ 0088ae44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088ae44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088ae44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088ae04 bytes 08810991
+ 0088ae44 bytes 08811991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8fbadc34f4382a9330954e9087d282d"></a>

### [`0088ae10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088ae10.md) → [`0088ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ae50.md) FUN_0088ae50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0088ae60",
      "incomplete_value": false,
      "site": "0088ae68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088ae20",
      "incomplete_value": false,
      "site": "0088ae28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:260:8"
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
      "0088ae68",
      "DATA",
      [
        "storage",
        "00c81260",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088ae68",
      "DATA",
      [
        "storage",
        "00c81660",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088ae20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088ae10.md#insn-0088ae20) · [`0088ae2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088ae10.md#insn-0088ae2c)
- 新版 `0088ae60`（命令位置の公開資料なし） · `0088ae6c`（命令位置の公開資料なし）

~~~diff
- 0088ae20 ["COPY", "tmp:0:8", ["const:260:8"]]
- 0088ae20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088ae20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088ae20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088ae60 ["COPY", "tmp:0:8", ["const:660:8"]]
+ 0088ae60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088ae60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088ae60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088ae20 bytes 08810991
+ 0088ae60 bytes 08811991
- 0088ae2c ["INT_ADD", "register:40f0:8", ["const:88ae2c:8", "const:4:8"]]
- 0088ae2c ["CALL", null, ["callee:00c57ea0:8"]]
+ 0088ae6c ["INT_ADD", "register:40f0:8", ["const:88ae6c:8", "const:4:8"]]
+ 0088ae6c ["CALL", null, ["callee:00c57ea0:8"]]
- 0088ae2c bytes 1d330f94
+ 0088ae6c bytes 0d340f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f105848813cb4d4961e2ddd3225991e"></a>

### [`0088ae4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088ae4c.md) → [`0088ae8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ae8c.md) FUN_0088ae8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00887898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md) · 呼出先 3件 [`00887438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887438.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)
- 新版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 3件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088aec4",
      "incomplete_value": false,
      "site": "0088aed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088ae84",
      "incomplete_value": false,
      "site": "0088ae90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
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
      "definition_site": "0088aee4",
      "incomplete_value": false,
      "site": "0088aee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088aea4",
      "incomplete_value": false,
      "site": "0088aea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "definition_site": "0088af14",
      "incomplete_value": false,
      "site": "0088af1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:ac2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088aed4",
      "incomplete_value": false,
      "site": "0088aedc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:a82:8"
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
      "0088aed0",
      "DATA",
      [
        "storage",
        "00c812b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088aee8",
      "DATA",
      [
        "storage",
        "00c80c98",
        null,
        "pointer"
      ]
    ],
    [
      "0088af04",
      "PARAM",
      [
        "storage",
        "002b419b",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088aed0",
      "DATA",
      [
        "storage",
        "00c816b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088aee8",
      "DATA",
      [
        "storage",
        "00c81098",
        null,
        "pointer"
      ]
    ],
    [
      "0088af04",
      "PARAM",
      [
        "storage",
        "002b41db",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088aedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088ae4c.md#insn-0088aedc) · [`0088ae70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088ae4c.md#insn-0088ae70) · [`0088ae84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088ae4c.md#insn-0088ae84)
- 新版 `0088af1c`（命令位置の公開資料なし） · `0088aeb0`（命令位置の公開資料なし） · `0088aec4`（命令位置の公開資料なし）

~~~diff
- 0088aedc ["INT_ADD", "register:40f0:8", ["const:88aedc:8", "const:4:8"]]
- 0088aedc ["CALL", null, ["callee:00c58190:8"]]
+ 0088af1c ["INT_ADD", "register:40f0:8", ["const:88af1c:8", "const:4:8"]]
+ 0088af1c ["CALL", null, ["callee:00c58190:8"]]
- 0088aedc bytes ad330f94
+ 0088af1c bytes 9d340f94
- 0088ae70 ["INT_ADD", "register:40f0:8", ["const:88ae70:8", "const:4:8"]]
- 0088ae70 ["CALL", null, ["callee:00c57e90:8"]]
+ 0088aeb0 ["INT_ADD", "register:40f0:8", ["const:88aeb0:8", "const:4:8"]]
+ 0088aeb0 ["CALL", null, ["callee:00c57e90:8"]]
- 0088ae70 bytes 08330f94
+ 0088aeb0 bytes f8330f94
- 0088ae84 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 0088ae84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088ae84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088ae84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088aec4 ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 0088aec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088aec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088aec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088ae84 bytes 08c10a91
+ 0088aec4 bytes 08c11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

