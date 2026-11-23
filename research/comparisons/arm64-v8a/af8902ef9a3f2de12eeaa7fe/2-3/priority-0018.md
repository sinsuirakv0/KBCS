# v16.0.0 → v16.0.1 · 最優先の変更候補 (18)

[一覧の目次](README.md)

<a id="compare-708607ac87147f580c1e4f75751db659"></a>

### [`00582630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582630.md) → [`00582670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582670.md) FUN_00582670

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589818.md) [`00589ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ba8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589858.md) [`00589be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589be8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582700",
      "incomplete_value": false,
      "site": "0058270c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005826c0",
      "incomplete_value": false,
      "site": "005826cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:110:8"
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
      "0058270c",
      "DATA",
      [
        "storage",
        "00c6c110",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058270c",
      "DATA",
      [
        "storage",
        "00c6c510",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058264c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582630.md#insn-0058264c) · [`00582658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582630.md#insn-00582658) · [`0058266c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582630.md#insn-0058266c)
- 新版 `0058268c`（命令位置の公開資料なし） · `00582698`（命令位置の公開資料なし） · `005826ac`（命令位置の公開資料なし）

~~~diff
- 0058264c ["INT_ADD", "register:40f0:8", ["const:58264c:8", "const:4:8"]]
- 0058264c ["CALL", null, ["callee:00588e6c:8"]]
+ 0058268c ["INT_ADD", "register:40f0:8", ["const:58268c:8", "const:4:8"]]
+ 0058268c ["CALL", null, ["callee:00588e6c:8"]]
- 0058264c bytes f8190094
+ 0058268c bytes f8190094
- 00582658 ["INT_ADD", "register:40f0:8", ["const:582658:8", "const:4:8"]]
- 00582658 ["CALL", null, ["callee:00589858:8"]]
+ 00582698 ["INT_ADD", "register:40f0:8", ["const:582698:8", "const:4:8"]]
+ 00582698 ["CALL", null, ["callee:00589858:8"]]
- 00582658 bytes 701c0094
+ 00582698 bytes 701c0094
- 0058266c ["INT_ADD", "register:40f0:8", ["const:58266c:8", "const:4:8"]]
- 0058266c ["CALL", null, ["callee:00497834:8"]]
+ 005826ac ["INT_ADD", "register:40f0:8", ["const:5826ac:8", "const:4:8"]]
+ 005826ac ["CALL", null, ["callee:00497834:8"]]
- 0058266c bytes 6254fc97
+ 005826ac bytes 6254fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab18ee9e7fbbfc0a14172eca3fb8934a"></a>

### [`00582738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582738.md) → [`00582778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582778.md) FUN_00582778

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
      "definition_site": "00582788",
      "incomplete_value": false,
      "site": "00582790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582748",
      "incomplete_value": false,
      "site": "00582750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:348:8"
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
      "00582790",
      "DATA",
      [
        "storage",
        "00c6c348",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582790",
      "DATA",
      [
        "storage",
        "00c6c748",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582738.md#insn-00582748) · [`00582754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582738.md#insn-00582754)
- 新版 `00582788`（命令位置の公開資料なし） · `00582794`（命令位置の公開資料なし）

~~~diff
- 00582748 ["COPY", "tmp:0:8", ["const:348:8"]]
- 00582748 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00582748 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00582748 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00582788 ["COPY", "tmp:0:8", ["const:748:8"]]
+ 00582788 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00582788 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00582788 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00582748 bytes 08210d91
+ 00582788 bytes 08211d91
- 00582754 ["INT_ADD", "register:40f0:8", ["const:582754:8", "const:4:8"]]
- 00582754 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00582794 ["INT_ADD", "register:40f0:8", ["const:582794:8", "const:4:8"]]
+ 00582794 ["CALL", null, ["callee:00c57ea0:8"]]
- 00582754 bytes d3541b94
+ 00582794 bytes c3551b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11bbb42a8582bc9aad7bac6ae3851bcd"></a>

### [`00582778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582778.md) → [`005827b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005827b8.md) FUN_005827b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005819f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/005819f4.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c589f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589f0.md)
- 新版 呼出元 1件 [`00581a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581a34.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58df0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005827e8",
      "incomplete_value": false,
      "site": "005827e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005827a8",
      "incomplete_value": false,
      "site": "005827a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:398:8"
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
      "005827e8",
      "DATA",
      [
        "storage",
        "00c6c398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005827e8",
      "DATA",
      [
        "storage",
        "00c6c798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582778.md#insn-00582798) · [`005827e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582778.md#insn-005827e0) · [`00582814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582778.md#insn-00582814)
- 新版 `005827d8`（命令位置の公開資料なし） · `00582820`（命令位置の公開資料なし） · `00582854`（命令位置の公開資料なし）

~~~diff
- 00582798 ["COPY", "tmp:0:8", ["const:398:8"]]
- 00582798 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00582798 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00582798 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005827d8 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 005827d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005827d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005827d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00582798 bytes 29610e91
+ 005827d8 bytes 29611e91
- 005827e0 ["INT_ADD", "register:40f0:8", ["const:5827e0:8", "const:4:8"]]
- 005827e0 ["CALL", null, ["callee:00c58df0:8"]]
+ 00582820 ["INT_ADD", "register:40f0:8", ["const:582820:8", "const:4:8"]]
+ 00582820 ["CALL", null, ["callee:00c58df0:8"]]
- 005827e0 bytes 84581b94
+ 00582820 bytes 74591b94
- 00582814 ["INT_ADD", "register:40f0:8", ["const:582814:8", "const:4:8"]]
- 00582814 ["CALL", null, ["callee:00c58df0:8"]]
+ 00582854 ["INT_ADD", "register:40f0:8", ["const:582854:8", "const:4:8"]]
+ 00582854 ["CALL", null, ["callee:00c58df0:8"]]
- 00582814 bytes 77581b94
+ 00582854 bytes 67591b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bdb299025c53bc19b4d6267cffe3bd7"></a>

### [`00582930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582930.md) → [`00582970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582970.md) FUN_00582970

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582980",
      "incomplete_value": false,
      "site": "00582980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582940",
      "incomplete_value": false,
      "site": "00582940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "00582980",
      "DATA",
      [
        "storage",
        "00c6c398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582980",
      "DATA",
      [
        "storage",
        "00c6c798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058293c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582930.md#insn-0058293c)
- 新版 `0058297c`（命令位置の公開資料なし）

~~~diff
- 0058293c ["COPY", "tmp:0:8", ["const:398:8"]]
- 0058293c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058293c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058293c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058297c ["COPY", "tmp:0:8", ["const:798:8"]]
+ 0058297c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058297c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058297c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058293c bytes 29610e91
+ 0058297c bytes 29611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2620395818b9933eb5faed0a2a99828"></a>

### [`00582958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582958.md) → [`00582998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582998.md) FUN_00582998

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005829a4",
      "incomplete_value": false,
      "site": "005829a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582964",
      "incomplete_value": false,
      "site": "00582964",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "005829a4",
      "DATA",
      [
        "storage",
        "00c6c398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005829a4",
      "DATA",
      [
        "storage",
        "00c6c798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582958.md#insn-00582960) · [`00582988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582958.md#insn-00582988)
- 新版 `005829a0`（命令位置の公開資料なし） · `005829c8`（命令位置の公開資料なし）

~~~diff
- 00582960 ["COPY", "tmp:0:8", ["const:398:8"]]
- 00582960 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00582960 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00582960 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005829a0 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 005829a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005829a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005829a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00582960 bytes 29610e91
+ 005829a0 bytes 29611e91
- 00582988 ["COPY", "register:0:8", ["register:4048:8"]]
- 00582988 ["INT_ADD", "register:40f0:8", ["const:582988:8", "const:4:8"]]
- 00582988 ["CALLIND", null, ["register:0:8"]]
+ 005829c8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005829c8 ["INT_ADD", "register:40f0:8", ["const:5829c8:8", "const:4:8"]]
+ 005829c8 ["CALLIND", null, ["register:0:8"]]
- 00582988 bytes 20013fd6
+ 005829c8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16408f7864872f8f2081aeb7f6f0079d"></a>

### [`00582c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582c50.md) → [`00582c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582c90.md) FUN_00582c90

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
      "definition_site": "00582c94",
      "incomplete_value": false,
      "site": "00582c98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582c54",
      "incomplete_value": false,
      "site": "00582c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
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
      "00582c98",
      "DATA",
      [
        "storage",
        "00c6c3f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582c98",
      "DATA",
      [
        "storage",
        "00c6c7f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582c50.md#insn-00582c54)
- 新版 `00582c94`（命令位置の公開資料なし）

~~~diff
- 00582c54 ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 00582c54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00582c54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00582c54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00582c94 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 00582c94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00582c94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00582c94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00582c54 bytes 08c10f91
+ 00582c94 bytes 08c11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-425ca1cebb1b4d1ccf569b1f68c715d7"></a>

### [`00582c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582c60.md) → [`00582ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582ca0.md) FUN_00582ca0

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
      "definition_site": "00582cb0",
      "incomplete_value": false,
      "site": "00582cb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582c70",
      "incomplete_value": false,
      "site": "00582c78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
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
      "00582cb8",
      "DATA",
      [
        "storage",
        "00c6c3f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582cb8",
      "DATA",
      [
        "storage",
        "00c6c7f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582c60.md#insn-00582c70) · [`00582c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582c60.md#insn-00582c7c)
- 新版 `00582cb0`（命令位置の公開資料なし） · `00582cbc`（命令位置の公開資料なし）

~~~diff
- 00582c70 ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 00582c70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00582c70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00582c70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00582cb0 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 00582cb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00582cb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00582cb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00582c70 bytes 08c10f91
+ 00582cb0 bytes 08c11f91
- 00582c7c ["INT_ADD", "register:40f0:8", ["const:582c7c:8", "const:4:8"]]
- 00582c7c ["CALL", null, ["callee:00c57ea0:8"]]
+ 00582cbc ["INT_ADD", "register:40f0:8", ["const:582cbc:8", "const:4:8"]]
+ 00582cbc ["CALL", null, ["callee:00c57ea0:8"]]
- 00582c7c bytes 89531b94
+ 00582cbc bytes 79541b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6051cdc20c5c6093c164a9e324abba17"></a>

### [`00582ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582ca0.md) → [`00582ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582ce0.md) FUN_00582ce0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00581a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581a68.md) · 呼出先 4件 [`004bc9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9c0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a90.md)
- 新版 呼出元 1件 [`00581aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581aa8.md) · 呼出先 4件 [`004bca00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bca00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.53% / 新版 92.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582d18",
      "incomplete_value": false,
      "site": "00582d18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582cd8",
      "incomplete_value": false,
      "site": "00582cd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:440:8"
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
      "definition_site": "00582d48",
      "incomplete_value": true,
      "site": "00582d48",
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
                "const:9b3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582d08",
      "incomplete_value": true,
      "site": "00582d08",
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
                "const:8d7:8"
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
      "definition_site": "00582e04",
      "incomplete_value": true,
      "site": "00582e04",
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
                "const:139:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582dc4",
      "incomplete_value": true,
      "site": "00582dc4",
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
                "const:6c:8"
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
      "00582d18",
      "DATA",
      [
        "storage",
        "00c6c440",
        null,
        "undefined *"
      ]
    ],
    [
      "00582d38",
      "READ",
      [
        "storage",
        "002a78d7",
        null,
        "string"
      ]
    ],
    [
      "00582df0",
      "READ",
      [
        "storage",
        "002a206c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00582d18",
      "DATA",
      [
        "storage",
        "00c6c840",
        null,
        "undefined *"
      ]
    ],
    [
      "00582d38",
      "READ",
      [
        "storage",
        "002a79b3",
        null,
        "string"
      ]
    ],
    [
      "00582df0",
      "READ",
      [
        "storage",
        "002a2139",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582ca0.md#insn-00582ccc) · [`00582cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582ca0.md#insn-00582cf0) · [`00582d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582ca0.md#insn-00582d1c)
- 新版 `00582d0c`（命令位置の公開資料なし） · `00582d30`（命令位置の公開資料なし） · `00582d5c`（命令位置の公開資料なし）

~~~diff
- 00582ccc ["COPY", "tmp:0:8", ["const:440:8"]]
- 00582ccc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00582ccc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00582ccc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00582d0c ["COPY", "tmp:0:8", ["const:840:8"]]
+ 00582d0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00582d0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00582d0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00582ccc bytes 29011191
+ 00582d0c bytes 29012191
- 00582cf0 ["COPY", "tmp:0:8", ["const:8d7:8"]]
- 00582cf0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00582cf0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00582cf0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00582d30 ["COPY", "tmp:0:8", ["const:9b3:8"]]
+ 00582d30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00582d30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00582d30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00582cf0 bytes 295d2391
+ 00582d30 bytes 29cd2691
- 00582d1c ["INT_ADD", "register:40f0:8", ["const:582d1c:8", "const:4:8"]]
- 00582d1c ["CALL", null, ["callee:00c58e90:8"]]
+ 00582d5c ["INT_ADD", "register:40f0:8", ["const:582d5c:8", "const:4:8"]]
+ 00582d5c ["CALL", null, ["callee:00c58e90:8"]]
- 00582d1c bytes 5d571b94
+ 00582d5c bytes 4d581b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98787f86f5aeec207ae5428ef4284e2d"></a>

### [`00582fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582fbc.md) → [`00582ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582ffc.md) FUN_00582ffc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058300c",
      "incomplete_value": false,
      "site": "0058300c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582fcc",
      "incomplete_value": false,
      "site": "00582fcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:440:8"
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
      "0058300c",
      "DATA",
      [
        "storage",
        "00c6c440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058300c",
      "DATA",
      [
        "storage",
        "00c6c840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582fbc.md#insn-00582fc8)
- 新版 `00583008`（命令位置の公開資料なし）

~~~diff
- 00582fc8 ["COPY", "tmp:0:8", ["const:440:8"]]
- 00582fc8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00582fc8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00582fc8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00583008 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 00583008 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00583008 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00583008 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00582fc8 bytes 29011191
+ 00583008 bytes 29012191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e203ad78c850c992d527b464c4729cdb"></a>

### [`00582fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582fe4.md) → [`00583024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583024.md) FUN_00583024

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00583030",
      "incomplete_value": false,
      "site": "00583030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582ff0",
      "incomplete_value": false,
      "site": "00582ff0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:440:8"
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
      "00583030",
      "DATA",
      [
        "storage",
        "00c6c440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00583030",
      "DATA",
      [
        "storage",
        "00c6c840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582fe4.md#insn-00582fec) · [`00583014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582fe4.md#insn-00583014)
- 新版 `0058302c`（命令位置の公開資料なし） · `00583054`（命令位置の公開資料なし）

~~~diff
- 00582fec ["COPY", "tmp:0:8", ["const:440:8"]]
- 00582fec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00582fec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00582fec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058302c ["COPY", "tmp:0:8", ["const:840:8"]]
+ 0058302c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058302c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058302c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00582fec bytes 29011191
+ 0058302c bytes 29012191
- 00583014 ["COPY", "register:0:8", ["register:4048:8"]]
- 00583014 ["INT_ADD", "register:40f0:8", ["const:583014:8", "const:4:8"]]
- 00583014 ["CALLIND", null, ["register:0:8"]]
+ 00583054 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00583054 ["INT_ADD", "register:40f0:8", ["const:583054:8", "const:4:8"]]
+ 00583054 ["CALLIND", null, ["register:0:8"]]
- 00583014 bytes 20013fd6
+ 00583054 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bff1381e99b4885d4cc9a7b48af65852"></a>

### [`00583478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583478.md) → [`005834b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005834b8.md) FUN_005834b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005835e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005835e0.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 1件 [`00583620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583620.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

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
      "definition_site": "005834d8",
      "incomplete_value": false,
      "site": "005834d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583498",
      "incomplete_value": false,
      "site": "00583498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
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
      "005834d8",
      "DATA",
      [
        "storage",
        "00c6c4c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005834d8",
      "DATA",
      [
        "storage",
        "00c6c8c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00583490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583478.md#insn-00583490) · [`005834d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583478.md#insn-005834d4) · [`00583500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583478.md#insn-00583500)
- 新版 `005834d0`（命令位置の公開資料なし） · `00583514`（命令位置の公開資料なし） · `00583540`（命令位置の公開資料なし）

~~~diff
- 00583490 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 00583490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00583490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00583490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005834d0 ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 005834d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005834d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005834d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00583490 bytes 08211391
+ 005834d0 bytes 08212391
- 005834d4 ["INT_ADD", "register:40f0:8", ["const:5834d4:8", "const:4:8"]]
- 005834d4 ["CALL", null, ["callee:0043bb20:8"]]
+ 00583514 ["INT_ADD", "register:40f0:8", ["const:583514:8", "const:4:8"]]
+ 00583514 ["CALL", null, ["callee:0043bb20:8"]]
- 005834d4 bytes 83e1fa97
+ 00583514 bytes 83e1fa97
- 00583500 ["INT_ADD", "register:40f0:8", ["const:583500:8", "const:4:8"]]
- 00583500 ["CALL", null, ["callee:0043bb20:8"]]
+ 00583540 ["INT_ADD", "register:40f0:8", ["const:583540:8", "const:4:8"]]
+ 00583540 ["CALL", null, ["callee:0043bb20:8"]]
- 00583500 bytes 78e1fa97
+ 00583540 bytes 78e1fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-151d30bfdcd54a9c61f878b2ee0fe9b7"></a>

### [`005835e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005835e0.md) → [`00583620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583620.md) FUN_00583620

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00561cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf0.md) · 呼出先 2件 [`00583478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583478.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00561d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d30.md) · 呼出先 2件 [`005834b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005834b8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058365c",
      "incomplete_value": false,
      "site": "00583668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058361c",
      "incomplete_value": false,
      "site": "00583628",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "00583668",
      "DATA",
      [
        "storage",
        "00c6c608",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00583668",
      "DATA",
      [
        "storage",
        "00c6ca08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00583610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005835e0.md#insn-00583610) · [`0058361c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005835e0.md#insn-0058361c) · [`00583640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005835e0.md#insn-00583640)
- 新版 `00583650`（命令位置の公開資料なし） · `0058365c`（命令位置の公開資料なし） · `00583680`（命令位置の公開資料なし）

~~~diff
- 00583610 ["INT_ADD", "register:40f0:8", ["const:583610:8", "const:4:8"]]
- 00583610 ["CALL", null, ["callee:00c57e90:8"]]
+ 00583650 ["INT_ADD", "register:40f0:8", ["const:583650:8", "const:4:8"]]
+ 00583650 ["CALL", null, ["callee:00c57e90:8"]]
- 00583610 bytes 20511b94
+ 00583650 bytes 10521b94
- 0058361c ["COPY", "tmp:0:8", ["const:608:8"]]
- 0058361c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058361c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058361c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058365c ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 0058365c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058365c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058365c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058361c bytes 08211891
+ 0058365c bytes 08212891
- 00583640 ["INT_ADD", "register:40f0:8", ["const:583640:8", "const:4:8"]]
- 00583640 ["CALL", null, ["callee:005834b8:8"]]
+ 00583680 ["INT_ADD", "register:40f0:8", ["const:583680:8", "const:4:8"]]
+ 00583680 ["CALL", null, ["callee:005834b8:8"]]
- 00583640 bytes 8effff97
+ 00583680 bytes 8effff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f995ecc51f6bd6f1a725c2638005702"></a>

### [`0058386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058386c.md) → [`005838ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838ac.md) FUN_005838ac

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00583864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583864.md) [`005848f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/005848f8.md) · 呼出先 25件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00583d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583d98.md) [`005870e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005870e8.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 2件 [`005838a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838a4.md) [`00584938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584938.md) · 呼出先 25件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00583dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583dd8.md) [`00587128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587128.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.01% / 新版 94.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00583934",
      "incomplete_value": true,
      "site": "00583948",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005838f4",
      "incomplete_value": true,
      "site": "00583908",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:660:8"
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
      "definition_site": "00583940",
      "incomplete_value": true,
      "site": "00583950",
      "value": [
        "LOAD",
        "16",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583900",
      "incomplete_value": true,
      "site": "00583910",
      "value": [
        "LOAD",
        "16",
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
                "const:40:8"
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
      "definition_site": "00583940",
      "incomplete_value": true,
      "site": "00583950",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00583900",
      "incomplete_value": true,
      "site": "00583910",
      "value": [
        "LOAD",
        "16",
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
      "00583904",
      "READ",
      [
        "storage",
        "002ad8cf",
        null,
        "string"
      ]
    ],
    [
      "0058390c",
      "READ",
      [
        "storage",
        "002ad8d5",
        null,
        "string"
      ]
    ],
    [
      "00583934",
      "READ",
      [
        "storage",
        "002c2660",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00583904",
      "READ",
      [
        "storage",
        "002ad90f",
        null,
        "string"
      ]
    ],
    [
      "0058390c",
      "READ",
      [
        "storage",
        "002ad915",
        null,
        "string"
      ]
    ],
    [
      "00583934",
      "READ",
      [
        "storage",
        "002c26a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058395c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058386c.md#insn-0058395c) · [`00583c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058386c.md#insn-00583c00) · [`00583c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058386c.md#insn-00583c40)
- 新版 `0058399c`（命令位置の公開資料なし） · `00583c40`（命令位置の公開資料なし） · `00583c80`（命令位置の公開資料なし）

~~~diff
- 0058395c ["INT_ADD", "register:40f0:8", ["const:58395c:8", "const:4:8"]]
- 0058395c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058399c ["INT_ADD", "register:40f0:8", ["const:58399c:8", "const:4:8"]]
+ 0058399c ["CALL", null, ["callee:00c57eb0:8"]]
- 0058395c bytes 55501b94
+ 0058399c bytes 45511b94
- 00583c00 ["INT_ADD", "register:40f0:8", ["const:583c00:8", "const:4:8"]]
- 00583c00 ["CALL", null, ["callee:00587128:8"]]
+ 00583c40 ["INT_ADD", "register:40f0:8", ["const:583c40:8", "const:4:8"]]
+ 00583c40 ["CALL", null, ["callee:00587128:8"]]
- 00583c00 bytes 3a0d0094
+ 00583c40 bytes 3a0d0094
- 00583c40 ["INT_ADD", "register:40f0:8", ["const:583c40:8", "const:4:8"]]
- 00583c40 ["CALL", null, ["callee:00589f08:8"]]
+ 00583c80 ["INT_ADD", "register:40f0:8", ["const:583c80:8", "const:4:8"]]
+ 00583c80 ["CALL", null, ["callee:00589f08:8"]]
- 00583c40 bytes a2180094
+ 00583c80 bytes a2180094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-103f9bf4b3e5be1802456e2efc5c26ba"></a>

### [`00583d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583d98.md) → [`00583dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583dd8.md) FUN_00583dd8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0058386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058386c.md) [`0058416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md) · 呼出先 7件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 2件 [`005838ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838ac.md) [`005841ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md) · 呼出先 7件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.34% / 新版 98.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00583ee8",
      "incomplete_value": false,
      "site": "00583ef0",
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
            "const:1eb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583ea8",
      "incomplete_value": false,
      "site": "00583eb0",
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
            "const:11e:8"
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
      "definition_site": "00583f4c",
      "incomplete_value": false,
      "site": "00583f54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:d6e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583f0c",
      "incomplete_value": false,
      "site": "00583f14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:d2e:8"
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
      "definition_site": "00583fb0",
      "incomplete_value": false,
      "site": "00583fb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:91c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583f70",
      "incomplete_value": false,
      "site": "00583f78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:8dc:8"
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
      "00583ee8",
      "PARAM",
      [
        "storage",
        "002a011e",
        null,
        "string"
      ]
    ],
    [
      "00583f4c",
      "PARAM",
      [
        "storage",
        "002b0d2e",
        null,
        "string"
      ]
    ],
    [
      "00583fb0",
      "PARAM",
      [
        "storage",
        "002ac8dc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00583ee8",
      "PARAM",
      [
        "storage",
        "002a01eb",
        null,
        "string"
      ]
    ],
    [
      "00583f4c",
      "PARAM",
      [
        "storage",
        "002b0d6e",
        null,
        "string"
      ]
    ],
    [
      "00583fb0",
      "PARAM",
      [
        "storage",
        "002ac91c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00583eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583d98.md#insn-00583eb0) · [`00583f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583d98.md#insn-00583f14) · [`00583f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583d98.md#insn-00583f78)
- 新版 `00583ef0`（命令位置の公開資料なし） · `00583f54`（命令位置の公開資料なし） · `00583fb8`（命令位置の公開資料なし）

~~~diff
- 00583eb0 ["INT_ADD", "register:40f0:8", ["const:583eb0:8", "const:4:8"]]
- 00583eb0 ["CALL", null, ["callee:00c57f70:8"]]
+ 00583ef0 ["INT_ADD", "register:40f0:8", ["const:583ef0:8", "const:4:8"]]
+ 00583ef0 ["CALL", null, ["callee:00c57f70:8"]]
- 00583eb0 bytes 304f1b94
+ 00583ef0 bytes 20501b94
- 00583f14 ["INT_ADD", "register:40f0:8", ["const:583f14:8", "const:4:8"]]
- 00583f14 ["CALL", null, ["callee:00c57f70:8"]]
+ 00583f54 ["INT_ADD", "register:40f0:8", ["const:583f54:8", "const:4:8"]]
+ 00583f54 ["CALL", null, ["callee:00c57f70:8"]]
- 00583f14 bytes 174f1b94
+ 00583f54 bytes 07501b94
- 00583f78 ["INT_ADD", "register:40f0:8", ["const:583f78:8", "const:4:8"]]
- 00583f78 ["CALL", null, ["callee:00c57f70:8"]]
+ 00583fb8 ["INT_ADD", "register:40f0:8", ["const:583fb8:8", "const:4:8"]]
+ 00583fb8 ["CALL", null, ["callee:00c57f70:8"]]
- 00583f78 bytes fe4e1b94
+ 00583fb8 bytes ee4f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74509c169c7ed91e0e1b010326e56645"></a>

### [`0058416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md) → [`005841ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md) FUN_005841ac

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00584164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584164.md) · 呼出先 27件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00583d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583d98.md) [`005867d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/005867d0.md) [`00586934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586934.md) [`0058720c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058720c.md)
- 新版 呼出元 1件 [`005841a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841a4.md) · 呼出先 27件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00583dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583dd8.md) [`00586810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586810.md) [`00586974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586974.md) [`0058724c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058724c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.01% / 新版 97.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00584244",
      "incomplete_value": true,
      "site": "00584250",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:6a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00584204",
      "incomplete_value": true,
      "site": "00584210",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:660:8"
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
      "definition_site": "00584520",
      "incomplete_value": false,
      "site": "00584530",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005844e0",
      "incomplete_value": false,
      "site": "005844f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00584210",
      "READ",
      [
        "storage",
        "002ad8cf",
        null,
        "string"
      ]
    ],
    [
      "00584218",
      "READ",
      [
        "storage",
        "002ad8d5",
        null,
        "string"
      ]
    ],
    [
      "00584240",
      "READ",
      [
        "storage",
        "002a430f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00584210",
      "READ",
      [
        "storage",
        "002ad90f",
        null,
        "string"
      ]
    ],
    [
      "00584218",
      "READ",
      [
        "storage",
        "002ad915",
        null,
        "string"
      ]
    ],
    [
      "00584240",
      "READ",
      [
        "storage",
        "002a43dc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005844f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md#insn-005844f0) · [`00584530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md#insn-00584530) · [`005841b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md#insn-005841b8)
- 新版 `00584530`（命令位置の公開資料なし） · `00584570`（命令位置の公開資料なし） · `005841f8`（命令位置の公開資料なし）

~~~diff
- 005844f0 ["INT_ADD", "register:40f0:8", ["const:5844f0:8", "const:4:8"]]
- 005844f0 ["CALL", null, ["callee:0058724c:8"]]
+ 00584530 ["INT_ADD", "register:40f0:8", ["const:584530:8", "const:4:8"]]
+ 00584530 ["CALL", null, ["callee:0058724c:8"]]
- 005844f0 bytes 470b0094
+ 00584530 bytes 470b0094
- 00584530 ["COPY", "register:0:8", ["register:4040:8"]]
- 00584530 ["INT_ADD", "register:40f0:8", ["const:584530:8", "const:4:8"]]
- 00584530 ["CALLIND", null, ["register:0:8"]]
+ 00584570 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584570 ["INT_ADD", "register:40f0:8", ["const:584570:8", "const:4:8"]]
+ 00584570 ["CALLIND", null, ["register:0:8"]]
- 00584530 bytes 00013fd6
+ 00584570 bytes 00013fd6
- 005841b8 ["INT_ADD", "register:40f0:8", ["const:5841b8:8", "const:4:8"]]
- 005841b8 ["CALL", null, ["callee:00588e6c:8"]]
+ 005841f8 ["INT_ADD", "register:40f0:8", ["const:5841f8:8", "const:4:8"]]
+ 005841f8 ["CALL", null, ["callee:00588e6c:8"]]
- 005841b8 bytes 1d130094
+ 005841f8 bytes 1d130094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc3f3b3eea5926c405e8b5c2e574fc56"></a>

### [`005848f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/005848f8.md) → [`00584938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584938.md) FUN_00584938

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`0058386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058386c.md) [`00587428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587428.md) [`00587488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587488.md) [`0058780c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058780c.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`005838ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838ac.md) [`00587468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587468.md) [`005874c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005874c8.md) [`0058784c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058784c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058497c",
      "incomplete_value": false,
      "site": "00584984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058493c",
      "incomplete_value": false,
      "site": "00584944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "definition_site": "005849a8",
      "incomplete_value": false,
      "site": "005849b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00584968",
      "incomplete_value": false,
      "site": "00584970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "definition_site": "00584a18",
      "incomplete_value": false,
      "site": "00584a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005849d8",
      "incomplete_value": false,
      "site": "005849d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00584984",
      "DATA",
      [
        "storage",
        "00c6c658",
        null,
        "pointer"
      ]
    ],
    [
      "005849b0",
      "DATA",
      [
        "storage",
        "00c6c6a8",
        null,
        "pointer"
      ]
    ],
    [
      "00584a18",
      "DATA",
      [
        "storage",
        "00c6c6f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00584984",
      "DATA",
      [
        "storage",
        "00c6ca58",
        null,
        "pointer"
      ]
    ],
    [
      "005849b0",
      "DATA",
      [
        "storage",
        "00c6caa8",
        null,
        "pointer"
      ]
    ],
    [
      "00584a18",
      "DATA",
      [
        "storage",
        "00c6caf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00584930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/005848f8.md#insn-00584930) · [`00584998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/005848f8.md#insn-00584998) · [`0058493c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/005848f8.md#insn-0058493c)
- 新版 `00584970`（命令位置の公開資料なし） · `005849d8`（命令位置の公開資料なし） · `0058497c`（命令位置の公開資料なし）

~~~diff
- 00584930 ["INT_ADD", "register:40f0:8", ["const:584930:8", "const:4:8"]]
- 00584930 ["CALL", null, ["callee:00c57e90:8"]]
+ 00584970 ["INT_ADD", "register:40f0:8", ["const:584970:8", "const:4:8"]]
+ 00584970 ["CALL", null, ["callee:00c57e90:8"]]
- 00584930 bytes 584c1b94
+ 00584970 bytes 484d1b94
- 00584998 ["INT_ADD", "register:40f0:8", ["const:584998:8", "const:4:8"]]
- 00584998 ["CALL", null, ["callee:00c580e0:8"]]
+ 005849d8 ["INT_ADD", "register:40f0:8", ["const:5849d8:8", "const:4:8"]]
+ 005849d8 ["CALL", null, ["callee:00c580e0:8"]]
- 00584998 bytes d24c1b94
+ 005849d8 bytes c24d1b94
- 0058493c ["COPY", "tmp:0:8", ["const:658:8"]]
- 0058493c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058493c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058493c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058497c ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 0058497c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058497c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058497c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058493c bytes 08611991
+ 0058497c bytes 08612991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03898e2912d4e7de854b1678186c60d4"></a>

### [`0058538c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058538c.md) → [`005853cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005853cc.md) FUN_005853cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0058568c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058568c.md) [`0058658c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/0058658c.md) · 呼出先 10件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00587ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587ed4.md) [`00587f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587f24.md) [`005880b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005880b4.md)
- 新版 呼出元 2件 [`005856cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005856cc.md) [`005865cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005865cc.md) · 呼出先 10件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00587f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587f14.md) [`00587f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587f64.md) [`005880f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005880f4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005855f8",
      "incomplete_value": true,
      "site": "005855f8",
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
            "const:320:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005855b8",
      "incomplete_value": true,
      "site": "005855b8",
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
            "const:f20:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005853fc",
      "incomplete_value": true,
      "site": "005853fc",
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
      "definition_site": "005853bc",
      "incomplete_value": true,
      "site": "005853bc",
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
      "definition_site": "0058548c",
      "incomplete_value": true,
      "site": "0058548c",
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
      "definition_site": "0058544c",
      "incomplete_value": true,
      "site": "0058544c",
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
      "005853f8",
      "READ",
      [
        "storage",
        "00ca5f40",
        null,
        "undefined8"
      ]
    ],
    [
      "00585440",
      "READ",
      [
        "storage",
        "00ca5ff0",
        null,
        "undefined8"
      ]
    ],
    [
      "00585464",
      "PARAM",
      [
        "storage",
        "00ca5f38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005853f8",
      "READ",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ],
    [
      "00585440",
      "READ",
      [
        "storage",
        "00ca63f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00585464",
      "PARAM",
      [
        "storage",
        "00ca6338",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058542c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058538c.md#insn-0058542c) · [`005854e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058538c.md#insn-005854e4) · [`00585574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058538c.md#insn-00585574)
- 新版 `0058546c`（命令位置の公開資料なし） · `00585524`（命令位置の公開資料なし） · `005855b4`（命令位置の公開資料なし）

~~~diff
- 0058542c ["INT_ADD", "register:40f0:8", ["const:58542c:8", "const:4:8"]]
- 0058542c ["CALL", null, ["callee:005880f4:8"]]
+ 0058546c ["INT_ADD", "register:40f0:8", ["const:58546c:8", "const:4:8"]]
+ 0058546c ["CALL", null, ["callee:005880f4:8"]]
- 0058542c bytes 220b0094
+ 0058546c bytes 220b0094
- 005854e4 ["INT_ADD", "register:40f0:8", ["const:5854e4:8", "const:4:8"]]
- 005854e4 ["CALL", null, ["callee:00587f64:8"]]
+ 00585524 ["INT_ADD", "register:40f0:8", ["const:585524:8", "const:4:8"]]
+ 00585524 ["CALL", null, ["callee:00587f64:8"]]
- 005854e4 bytes 900a0094
+ 00585524 bytes 900a0094
- 00585574 ["INT_ADD", "register:40f0:8", ["const:585574:8", "const:4:8"]]
- 00585574 ["CALL", null, ["callee:00c57e80:8"]]
+ 005855b4 ["INT_ADD", "register:40f0:8", ["const:5855b4:8", "const:4:8"]]
+ 005855b4 ["CALL", null, ["callee:00c57e80:8"]]
- 00585574 bytes 43491b94
+ 005855b4 bytes 334a1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab30c473dd91dde9bb7a649177f59a75"></a>

### [`0058568c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058568c.md) → [`005856cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005856cc.md) Java_jp_co_ponos_battlecats_MyActivity_newResponse

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`0057e050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e050.md) [`00581dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581dd0.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`0057e090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e090.md) [`00581e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581e10.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 97.75% / 新版 97.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `branch_value` 3件, `store_condition` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00585828",
      "incomplete_value": false,
      "site": "00585834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005857e8",
      "incomplete_value": false,
      "site": "005857f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00585bc8",
      "incomplete_value": true,
      "site": "00585bc8",
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
            "const:320:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00585b88",
      "incomplete_value": true,
      "site": "00585b88",
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
            "const:f20:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00585714",
      "incomplete_value": true,
      "site": "00585714",
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
      "definition_site": "005856d4",
      "incomplete_value": true,
      "site": "005856d4",
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
      "0058570c",
      "READ",
      [
        "storage",
        "00ca5f28",
        null,
        "undefined8"
      ]
    ],
    [
      "00585758",
      "READ",
      [
        "storage",
        "00ca5f78",
        null,
        "undefined8"
      ]
    ],
    [
      "00585834",
      "DATA",
      [
        "storage",
        "00c6c110",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058570c",
      "READ",
      [
        "storage",
        "00ca6328",
        null,
        "undefined8"
      ]
    ],
    [
      "00585758",
      "READ",
      [
        "storage",
        "00ca6378",
        null,
        "undefined8"
      ]
    ],
    [
      "00585834",
      "DATA",
      [
        "storage",
        "00c6c510",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005857b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058568c.md#insn-005857b4) · [`005859b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058568c.md#insn-005859b4) · [`00585a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058568c.md#insn-00585a40)
- 新版 `005857f4`（命令位置の公開資料なし） · `005859f4`（命令位置の公開資料なし） · `00585a80`（命令位置の公開資料なし）

~~~diff
- 005857b4 ["INT_ADD", "register:40f0:8", ["const:5857b4:8", "const:4:8"]]
- 005857b4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005857f4 ["INT_ADD", "register:40f0:8", ["const:5857f4:8", "const:4:8"]]
+ 005857f4 ["CALL", null, ["callee:00c57e90:8"]]
- 005857b4 bytes b7481b94
+ 005857f4 bytes a7491b94
- 005859b4 ["INT_ADD", "register:40f0:8", ["const:5859b4:8", "const:4:8"]]
- 005859b4 ["CALL", null, ["callee:00c53d00:8"]]
+ 005859f4 ["INT_ADD", "register:40f0:8", ["const:5859f4:8", "const:4:8"]]
+ 005859f4 ["CALL", null, ["callee:00c53d00:8"]]
- 005859b4 bytes cb371b94
+ 005859f4 bytes c3381b94
- 00585a40 ["INT_ADD", "register:40f0:8", ["const:585a40:8", "const:4:8"]]
- 00585a40 ["CALL", null, ["callee:00c53d00:8"]]
+ 00585a80 ["INT_ADD", "register:40f0:8", ["const:585a80:8", "const:4:8"]]
+ 00585a80 ["CALL", null, ["callee:00c53d00:8"]]
- 00585a40 bytes a8371b94
+ 00585a80 bytes a0381b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02979f17a9ee3c48f17744128d09c728"></a>

### [`00585ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585ed0.md) → [`00585f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585f10.md) Java_jp_co_ponos_battlecats_MyActivity_onResponseCodeHeaders

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00585d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585d10.md) [`00588314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588314.md) [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00585d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585d50.md) [`00588354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588354.md) [`00589954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.50% / 新版 96.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00585f44",
      "incomplete_value": true,
      "site": "00585f44",
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
      "definition_site": "00585f04",
      "incomplete_value": true,
      "site": "00585f04",
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
      "definition_site": "0058605c",
      "incomplete_value": true,
      "site": "0058605c",
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
      "definition_site": "0058601c",
      "incomplete_value": true,
      "site": "0058601c",
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
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "0058601c"
      ],
      [
        "FALL_THROUGH",
        "0058605c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "0058605c",
      "incomplete_value": true,
      "site": "0058607c",
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
      "definition_site": "0058601c",
      "incomplete_value": true,
      "site": "0058603c",
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
    "ordinal": 13,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00585f3c",
      "READ",
      [
        "storage",
        "00ca5f40",
        null,
        "undefined8"
      ]
    ],
    [
      "00585f98",
      "READ",
      [
        "storage",
        "00ca5f90",
        null,
        "undefined8"
      ]
    ],
    [
      "00586054",
      "READ",
      [
        "storage",
        "00ca5ee0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00585f3c",
      "READ",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ],
    [
      "00585f98",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ],
    [
      "00586054",
      "READ",
      [
        "storage",
        "00ca62e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00586080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585ed0.md#insn-00586080) · [`00585ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585ed0.md#insn-00585ef4) · [`00585ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585ed0.md#insn-00585ef8)
- 新版 `005860c0`（命令位置の公開資料なし） · `00585f34`（命令位置の公開資料なし） · `00585f38`（命令位置の公開資料なし）

~~~diff
- 00586080 ["INT_ADD", "register:40f0:8", ["const:586080:8", "const:4:8"]]
- 00586080 ["CALL", null, ["callee:00c53d00:8"]]
+ 005860c0 ["INT_ADD", "register:40f0:8", ["const:5860c0:8", "const:4:8"]]
+ 005860c0 ["CALL", null, ["callee:00c53d00:8"]]
- 00586080 bytes 18361b94
+ 005860c0 bytes 10371b94
- 00585ef4 ["COPY", "register:4040:8", ["const:ca5000:8"]]
+ 00585f34 ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 00585ef4 bytes 08390090
+ 00585f34 bytes 083900b0
- 00585ef8 ["COPY", "tmp:0:8", ["const:f40:8"]]
- 00585ef8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00585ef8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00585ef8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00585f38 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 00585f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00585f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00585f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00585ef8 bytes 08013d91
+ 00585f38 bytes 08010d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e71a3cb756cce5f38b01059d4656ed48"></a>

### [`005862a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/005862a4.md) → [`005862e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005862e4.md) Java_jp_co_ponos_battlecats_MyActivity_onResponseData

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0057e050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e050.md) [`00581dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581dd0.md) [`00589ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ba8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0057e090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e090.md) [`00581e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581e10.md) [`00589be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589be8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00586314",
      "incomplete_value": true,
      "site": "00586314",
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
      "definition_site": "005862d4",
      "incomplete_value": true,
      "site": "005862d4",
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
      "definition_site": "00586454",
      "incomplete_value": true,
      "site": "00586454",
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
      "definition_site": "00586414",
      "incomplete_value": true,
      "site": "00586414",
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
    "ordinal": 14,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00586414"
      ],
      [
        "FALL_THROUGH",
        "00586454"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00586454",
      "incomplete_value": true,
      "site": "00586474",
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
      "definition_site": "00586414",
      "incomplete_value": true,
      "site": "00586434",
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
      "00586310",
      "READ",
      [
        "storage",
        "00ca5f40",
        null,
        "undefined8"
      ]
    ],
    [
      "00586368",
      "READ",
      [
        "storage",
        "00ca5fc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00586398",
      "DATA",
      [
        "storage",
        "00c6c110",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00586310",
      "READ",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ],
    [
      "00586368",
      "READ",
      [
        "storage",
        "00ca63c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00586398",
      "DATA",
      [
        "storage",
        "00c6c510",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00586478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/005862a4.md#insn-00586478) · [`005862c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/005862a4.md#insn-005862c8) · [`005862cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/005862a4.md#insn-005862cc)
- 新版 `005864b8`（命令位置の公開資料なし） · `00586308`（命令位置の公開資料なし） · `0058630c`（命令位置の公開資料なし）

~~~diff
- 00586478 ["INT_ADD", "register:40f0:8", ["const:586478:8", "const:4:8"]]
- 00586478 ["CALL", null, ["callee:00c53d00:8"]]
+ 005864b8 ["INT_ADD", "register:40f0:8", ["const:5864b8:8", "const:4:8"]]
+ 005864b8 ["CALL", null, ["callee:00c53d00:8"]]
- 00586478 bytes 1a351b94
+ 005864b8 bytes 12361b94
- 005862c8 ["COPY", "register:4040:8", ["const:ca5000:8"]]
+ 00586308 ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 005862c8 bytes e83800f0
+ 00586308 bytes 08390090
- 005862cc ["COPY", "tmp:0:8", ["const:f40:8"]]
- 005862cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005862cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005862cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058630c ["COPY", "tmp:0:8", ["const:340:8"]]
+ 0058630c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058630c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058630c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005862cc bytes 08013d91
+ 0058630c bytes 08010d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14eed827e6fa1f88d363d204203cd40d"></a>

### [`0058659c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/0058659c.md) → [`005865dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005865dc.md) FUN_005865dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058669c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/0058669c.md) · 呼出先 4件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005866dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005866dc.md) · 呼出先 4件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005865f8",
      "incomplete_value": false,
      "site": "005865fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005865b8",
      "incomplete_value": false,
      "site": "005865bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:4e8:8"
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
      "005865fc",
      "DATA",
      [
        "storage",
        "00c6c4e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005865fc",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005865b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/0058659c.md#insn-005865b8) · [`005865f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/0058659c.md#insn-005865f4) · [`00586608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/0058659c.md#insn-00586608)
- 新版 `005865f8`（命令位置の公開資料なし） · `00586634`（命令位置の公開資料なし） · `00586648`（命令位置の公開資料なし）

~~~diff
- 005865b8 ["COPY", "tmp:0:8", ["const:4e8:8"]]
- 005865b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005865b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005865b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005865f8 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 005865f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005865f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005865f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005865b8 bytes 08a11391
+ 005865f8 bytes 08a12391
- 005865f4 ["INT_ADD", "register:40f0:8", ["const:5865f4:8", "const:4:8"]]
- 005865f4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00586634 ["INT_ADD", "register:40f0:8", ["const:586634:8", "const:4:8"]]
+ 00586634 ["CALL", null, ["callee:00c53d00:8"]]
- 005865f4 bytes bb341b94
+ 00586634 bytes b3351b94
- 00586608 ["COPY", "register:0:8", ["register:4040:8"]]
- 00586608 ["INT_ADD", "register:40f0:8", ["const:586608:8", "const:4:8"]]
- 00586608 ["CALLIND", null, ["register:0:8"]]
+ 00586648 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00586648 ["INT_ADD", "register:40f0:8", ["const:586648:8", "const:4:8"]]
+ 00586648 ["CALLIND", null, ["register:0:8"]]
- 00586608 bytes 00013fd6
+ 00586648 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bdba9adfe090be92e79b1b9d4993e2e"></a>

### [`005866c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/005866c0.md) → [`00586700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586700.md) FUN_00586700

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00586718",
      "incomplete_value": false,
      "site": "0058671c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005866d8",
      "incomplete_value": false,
      "site": "005866dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
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
      "0058671c",
      "DATA",
      [
        "storage",
        "00c6c4c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058671c",
      "DATA",
      [
        "storage",
        "00c6c8c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058671c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/005866c0.md#insn-0058671c) · [`005866d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/005866c0.md#insn-005866d8) · [`0058670c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/005866c0.md#insn-0058670c)
- 新版 `0058675c`（命令位置の公開資料なし） · `00586718`（命令位置の公開資料なし） · `0058674c`（命令位置の公開資料なし）

~~~diff
- 0058671c ["INT_ADD", "register:40f0:8", ["const:58671c:8", "const:4:8"]]
- 0058671c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058675c ["INT_ADD", "register:40f0:8", ["const:58675c:8", "const:4:8"]]
+ 0058675c ["CALL", null, ["callee:00c57eb0:8"]]
- 0058671c bytes e5441b94
+ 0058675c bytes d5451b94
- 005866d8 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 005866d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005866d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005866d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00586718 ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 00586718 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00586718 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00586718 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005866d8 bytes 29211391
+ 00586718 bytes 29212391
- 0058670c ["INT_ADD", "register:40f0:8", ["const:58670c:8", "const:4:8"]]
- 0058670c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058674c ["INT_ADD", "register:40f0:8", ["const:58674c:8", "const:4:8"]]
+ 0058674c ["CALL", null, ["callee:00c57eb0:8"]]
- 0058670c bytes e9441b94
+ 0058674c bytes d9451b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eee8cd86594310bec4f907f4cc899ab"></a>

### [`00586748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586748.md) → [`00586788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586788.md) FUN_00586788

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005867a0",
      "incomplete_value": false,
      "site": "005867a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00586760",
      "incomplete_value": false,
      "site": "00586764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
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
      "005867a4",
      "DATA",
      [
        "storage",
        "00c6c4c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005867a4",
      "DATA",
      [
        "storage",
        "00c6c8c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00586760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586748.md#insn-00586760) · [`00586788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586748.md#insn-00586788) · [`005867a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586748.md#insn-005867a0)
- 新版 `005867a0`（命令位置の公開資料なし） · `005867c8`（命令位置の公開資料なし） · `005867e0`（命令位置の公開資料なし）

~~~diff
- 00586760 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 00586760 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00586760 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00586760 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005867a0 ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 005867a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005867a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005867a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00586760 bytes 29211391
+ 005867a0 bytes 29212391
- 00586788 ["INT_ADD", "register:40f0:8", ["const:586788:8", "const:4:8"]]
- 00586788 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005867c8 ["INT_ADD", "register:40f0:8", ["const:5867c8:8", "const:4:8"]]
+ 005867c8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00586788 bytes ca441b94
+ 005867c8 bytes ba451b94
- 005867a0 ["INT_ADD", "register:40f0:8", ["const:5867a0:8", "const:4:8"]]
- 005867a0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005867e0 ["INT_ADD", "register:40f0:8", ["const:5867e0:8", "const:4:8"]]
+ 005867e0 ["CALL", null, ["callee:00c57eb0:8"]]
- 005867a0 bytes c4441b94
+ 005867e0 bytes b4451b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3889bb604545bd2259749f4d559e2f61"></a>

### [`00587098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587098.md) → [`005870d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005870d8.md) FUN_005870d8

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
      "definition_site": "005870dc",
      "incomplete_value": false,
      "site": "005870e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058709c",
      "incomplete_value": false,
      "site": "005870a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "005870e0",
      "DATA",
      [
        "storage",
        "00c6c608",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005870e0",
      "DATA",
      [
        "storage",
        "00c6ca08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058709c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587098.md#insn-0058709c)
- 新版 `005870dc`（命令位置の公開資料なし）

~~~diff
- 0058709c ["COPY", "tmp:0:8", ["const:608:8"]]
- 0058709c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058709c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058709c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005870dc ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 005870dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005870dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005870dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058709c bytes 08211891
+ 005870dc bytes 08212891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46f1eee24eb570b01ab0da8d7da0afc5"></a>

### [`005873e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005873e8.md) → [`00587428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587428.md) FUN_00587428

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
      "definition_site": "0058742c",
      "incomplete_value": false,
      "site": "00587430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005873ec",
      "incomplete_value": false,
      "site": "005873f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "00587430",
      "DATA",
      [
        "storage",
        "00c6c658",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00587430",
      "DATA",
      [
        "storage",
        "00c6ca58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005873ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005873e8.md#insn-005873ec)
- 新版 `0058742c`（命令位置の公開資料なし）

~~~diff
- 005873ec ["COPY", "tmp:0:8", ["const:658:8"]]
- 005873ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005873ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005873ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058742c ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 0058742c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058742c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058742c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005873ec bytes 08611991
+ 0058742c bytes 08612991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba498db297062d6c2ecc14a1e112be3d"></a>

### [`005873f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005873f8.md) → [`00587438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587438.md) FUN_00587438

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
      "definition_site": "00587448",
      "incomplete_value": false,
      "site": "00587450",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587408",
      "incomplete_value": false,
      "site": "00587410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "00587450",
      "DATA",
      [
        "storage",
        "00c6c658",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00587450",
      "DATA",
      [
        "storage",
        "00c6ca58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005873f8.md#insn-00587408) · [`00587414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005873f8.md#insn-00587414)
- 新版 `00587448`（命令位置の公開資料なし） · `00587454`（命令位置の公開資料なし）

~~~diff
- 00587408 ["COPY", "tmp:0:8", ["const:658:8"]]
- 00587408 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587408 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587408 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587448 ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 00587448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587408 bytes 08611991
+ 00587448 bytes 08612991
- 00587414 ["INT_ADD", "register:40f0:8", ["const:587414:8", "const:4:8"]]
- 00587414 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00587454 ["INT_ADD", "register:40f0:8", ["const:587454:8", "const:4:8"]]
+ 00587454 ["CALL", null, ["callee:00c57ea0:8"]]
- 00587414 bytes a3411b94
+ 00587454 bytes 93421b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8acdbd884edaefd122d3dc0eeb23dec4"></a>

### [`00587434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587434.md) → [`00587474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587474.md) FUN_00587474

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

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
      "definition_site": "00587498",
      "incomplete_value": true,
      "site": "00587498",
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
      "definition_site": "00587458",
      "incomplete_value": true,
      "site": "00587458",
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
      "0058748c",
      "READ",
      [
        "storage",
        "00c9a850",
        null,
        "pointer"
      ]
    ],
    [
      "00587498",
      "DATA",
      [
        "storage",
        "00c928d8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0058748c",
      "READ",
      [
        "storage",
        "00c9ac50",
        null,
        "pointer"
      ]
    ],
    [
      "00587498",
      "DATA",
      [
        "storage",
        "00c92cd8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058744c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587434.md#insn-0058744c) · [`0058745c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587434.md#insn-0058745c) · [`00587464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587434.md#insn-00587464)
- 新版 `0058748c`（命令位置の公開資料なし） · `0058749c`（命令位置の公開資料なし） · `005874a4`（命令位置の公開資料なし）

~~~diff
- 0058744c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:850:8"]]
- 0058744c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0058748c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c50:8"]]
+ 0058748c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0058744c bytes 082944f9
+ 0058748c bytes 082946f9
- 0058745c ["INT_ADD", "register:40f0:8", ["const:58745c:8", "const:4:8"]]
- 0058745c ["CALL", null, ["callee:00c580d0:8"]]
+ 0058749c ["INT_ADD", "register:40f0:8", ["const:58749c:8", "const:4:8"]]
+ 0058749c ["CALL", null, ["callee:00c580d0:8"]]
- 0058745c bytes 1d421b94
+ 0058749c bytes 0d431b94
- 00587464 ["INT_ADD", "register:40f0:8", ["const:587464:8", "const:4:8"]]
- 00587464 ["CALL", null, ["callee:00c57e60:8"]]
+ 005874a4 ["INT_ADD", "register:40f0:8", ["const:5874a4:8", "const:4:8"]]
+ 005874a4 ["CALL", null, ["callee:00c57e60:8"]]
- 00587464 bytes 7f411b94
+ 005874a4 bytes 6f421b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-831679c4a4162a8290b00ba4b96ef0f5"></a>

### [`005875a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005875a8.md) → [`005875e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005875e8.md) FUN_005875e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00587428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587428.md) · 呼出先 12件 [`0045a688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a688.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00587468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587468.md) · 呼出先 12件 [`0045a6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6c8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.15% / 新版 93.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058768c",
      "incomplete_value": true,
      "site": "00587690",
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
      "definition_site": "0058764c",
      "incomplete_value": true,
      "site": "00587650",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00587668",
      "incomplete_value": true,
      "site": "00587670",
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
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:c58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587628",
      "incomplete_value": true,
      "site": "00587630",
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
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:858:8"
              ]
            ]
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
      "definition_site": "00587664",
      "incomplete_value": false,
      "site": "00587670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:45a000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587624",
      "incomplete_value": false,
      "site": "00587630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:45a000:8"
          ],
          [
            "leaf",
            "const:688:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00587664",
      "PARAM",
      [
        "storage",
        "0045a688",
        null,
        null
      ]
    ],
    [
      "00587668",
      "READ",
      [
        "storage",
        "00c9a858",
        null,
        "pointer"
      ]
    ],
    [
      "00587668",
      "PARAM",
      [
        "storage",
        "00c928b0",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00587664",
      "PARAM",
      [
        "storage",
        "0045a6c8",
        null,
        null
      ]
    ],
    [
      "00587668",
      "READ",
      [
        "storage",
        "00c9ac58",
        null,
        "pointer"
      ]
    ],
    [
      "00587668",
      "PARAM",
      [
        "storage",
        "00c92cb0",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005875a8.md#insn-00587610) · [`00587630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005875a8.md#insn-00587630) · [`005875e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005875a8.md#insn-005875e8)
- 新版 `00587650`（命令位置の公開資料なし） · `00587670`（命令位置の公開資料なし） · `00587628`（命令位置の公開資料なし）

~~~diff
- 00587610 ["INT_ADD", "register:40f0:8", ["const:587610:8", "const:4:8"]]
- 00587610 ["CALL", null, ["callee:00c58320:8"]]
+ 00587650 ["INT_ADD", "register:40f0:8", ["const:587650:8", "const:4:8"]]
+ 00587650 ["CALL", null, ["callee:00c58320:8"]]
- 00587610 bytes 44421b94
+ 00587650 bytes 34431b94
- 00587630 ["INT_ADD", "register:40f0:8", ["const:587630:8", "const:4:8"]]
- 00587630 ["CALL", null, ["callee:00c58330:8"]]
+ 00587670 ["INT_ADD", "register:40f0:8", ["const:587670:8", "const:4:8"]]
+ 00587670 ["CALL", null, ["callee:00c58330:8"]]
- 00587630 bytes 40421b94
+ 00587670 bytes 30431b94
- 005875e8 ["INT_ADD", "register:40f0:8", ["const:5875e8:8", "const:4:8"]]
- 005875e8 ["CALL", null, ["callee:00c582f0:8"]]
+ 00587628 ["INT_ADD", "register:40f0:8", ["const:587628:8", "const:4:8"]]
+ 00587628 ["CALL", null, ["callee:00c582f0:8"]]
- 005875e8 bytes 42421b94
+ 00587628 bytes 32431b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-203c0a04f5068d7aaeef54323fadb17e"></a>

### [`005876d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005876d0.md) → [`00587710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587710.md) FUN_00587710

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
      "definition_site": "00587724",
      "incomplete_value": false,
      "site": "00587728",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005876e4",
      "incomplete_value": false,
      "site": "005876e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "00587728",
      "DATA",
      [
        "storage",
        "00c6c6f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587728",
      "DATA",
      [
        "storage",
        "00c6caf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005876e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005876d0.md#insn-005876e4) · [`005876f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005876d0.md#insn-005876f8) · [`00587718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005876d0.md#insn-00587718)
- 新版 `00587724`（命令位置の公開資料なし） · `00587738`（命令位置の公開資料なし） · `00587758`（命令位置の公開資料なし）

~~~diff
- 005876e4 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 005876e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005876e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005876e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587724 ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 00587724 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587724 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587724 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005876e4 bytes 08c11b91
+ 00587724 bytes 08c12b91
- 005876f8 ["INT_ADD", "register:40f0:8", ["const:5876f8:8", "const:4:8"]]
- 005876f8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00587738 ["INT_ADD", "register:40f0:8", ["const:587738:8", "const:4:8"]]
+ 00587738 ["CALL", null, ["callee:00c53d00:8"]]
- 005876f8 bytes 7a301b94
+ 00587738 bytes 72311b94
- 00587718 ["COPY", "register:0:8", ["register:4040:8"]]
- 00587718 ["INT_ADD", "register:40f0:8", ["const:587718:8", "const:4:8"]]
- 00587718 ["CALLIND", null, ["register:0:8"]]
+ 00587758 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00587758 ["INT_ADD", "register:40f0:8", ["const:587758:8", "const:4:8"]]
+ 00587758 ["CALLIND", null, ["register:0:8"]]
- 00587718 bytes 00013fd6
+ 00587758 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eba7d3c875d56851726f8a338156cc73"></a>

### [`0058772c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058772c.md) → [`0058776c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058776c.md) FUN_0058776c

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
      "definition_site": "00587784",
      "incomplete_value": false,
      "site": "00587788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587744",
      "incomplete_value": false,
      "site": "00587748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "00587788",
      "DATA",
      [
        "storage",
        "00c6c6f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587788",
      "DATA",
      [
        "storage",
        "00c6caf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058772c.md#insn-00587744) · [`00587758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058772c.md#insn-00587758) · [`0058776c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058772c.md#insn-0058776c)
- 新版 `00587784`（命令位置の公開資料なし） · `00587798`（命令位置の公開資料なし） · `005877ac`（命令位置の公開資料なし）

~~~diff
- 00587744 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 00587744 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587744 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587744 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587784 ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 00587784 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587784 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587784 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587744 bytes 08c11b91
+ 00587784 bytes 08c12b91
- 00587758 ["INT_ADD", "register:40f0:8", ["const:587758:8", "const:4:8"]]
- 00587758 ["CALL", null, ["callee:00c53d00:8"]]
+ 00587798 ["INT_ADD", "register:40f0:8", ["const:587798:8", "const:4:8"]]
+ 00587798 ["CALL", null, ["callee:00c53d00:8"]]
- 00587758 bytes 62301b94
+ 00587798 bytes 5a311b94
- 0058776c ["COPY", "register:0:8", ["register:4040:8"]]
- 0058776c ["INT_ADD", "register:40f0:8", ["const:58776c:8", "const:4:8"]]
- 0058776c ["CALLIND", null, ["register:0:8"]]
+ 005877ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 005877ac ["INT_ADD", "register:40f0:8", ["const:5877ac:8", "const:4:8"]]
+ 005877ac ["CALLIND", null, ["register:0:8"]]
- 0058776c bytes 00013fd6
+ 005877ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ad42ca54382ad465c5a4b5a74b89c6f"></a>

### [`00587788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587788.md) → [`005877c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005877c8.md) FUN_005877c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005877ec",
      "incomplete_value": false,
      "site": "005877ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005877ac",
      "incomplete_value": false,
      "site": "005877ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "005877ec",
      "DATA",
      [
        "storage",
        "00c6c6f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005877ec",
      "DATA",
      [
        "storage",
        "00c6caf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058779c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587788.md#insn-0058779c) · [`005877a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587788.md#insn-005877a8) · [`005877c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587788.md#insn-005877c4)
- 新版 `005877dc`（命令位置の公開資料なし） · `005877e8`（命令位置の公開資料なし） · `00587804`（命令位置の公開資料なし）

~~~diff
- 0058779c ["INT_ADD", "register:40f0:8", ["const:58779c:8", "const:4:8"]]
- 0058779c ["CALL", null, ["callee:00c57e90:8"]]
+ 005877dc ["INT_ADD", "register:40f0:8", ["const:5877dc:8", "const:4:8"]]
+ 005877dc ["CALL", null, ["callee:00c57e90:8"]]
- 0058779c bytes bd401b94
+ 005877dc bytes ad411b94
- 005877a8 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 005877a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005877a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005877a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005877e8 ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 005877e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005877e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005877e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005877a8 bytes 29c11b91
+ 005877e8 bytes 29c12b91
- 005877c4 ["INT_ADD", "register:40f0:8", ["const:5877c4:8", "const:4:8"]]
- 005877c4 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00587804 ["INT_ADD", "register:40f0:8", ["const:587804:8", "const:4:8"]]
+ 00587804 ["CALL", null, ["callee:00c53cd0:8"]]
- 005877c4 bytes 3b301b94
+ 00587804 bytes 33311b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0887ab0545055b6d89f22fd2adf3795"></a>

### [`005877d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005877d8.md) → [`00587818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587818.md) FUN_00587818

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "00587824",
      "incomplete_value": false,
      "site": "00587824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005877e4",
      "incomplete_value": false,
      "site": "005877e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "00587824",
      "DATA",
      [
        "storage",
        "00c6c6f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587824",
      "DATA",
      [
        "storage",
        "00c6caf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005877e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005877d8.md#insn-005877e0) · [`00587800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005877d8.md#insn-00587800)
- 新版 `00587820`（命令位置の公開資料なし） · `00587840`（命令位置の公開資料なし）

~~~diff
- 005877e0 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 005877e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005877e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005877e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00587820 ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 00587820 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00587820 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00587820 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005877e0 bytes 29c11b91
+ 00587820 bytes 29c12b91
- 00587800 ["INT_ADD", "register:40f0:8", ["const:587800:8", "const:4:8"]]
- 00587800 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00587840 ["INT_ADD", "register:40f0:8", ["const:587840:8", "const:4:8"]]
+ 00587840 ["CALL", null, ["callee:00c53cd0:8"]]
- 00587800 bytes 2c301b94
+ 00587840 bytes 24311b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc90be9d85b25f8fbb2b51089815cd3c"></a>

### [`00587d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587d54.md) → [`00587d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587d94.md) FUN_00587d94

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00587c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587c14.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00587c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587c54.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00587da0",
      "incomplete_value": false,
      "site": "00587da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587d60",
      "incomplete_value": false,
      "site": "00587d64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f0c:8"
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
      "00587da0",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00587da0",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587d54.md#insn-00587d64) · [`00587d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587d54.md#insn-00587d60)
- 新版 `00587da4`（命令位置の公開資料なし） · `00587da0`（命令位置の公開資料なし）

~~~diff
- 00587d64 ["INT_ADD", "register:40f0:8", ["const:587d64:8", "const:4:8"]]
- 00587d64 ["CALL", null, ["callee:0043b778:8"]]
+ 00587da4 ["INT_ADD", "register:40f0:8", ["const:587da4:8", "const:4:8"]]
+ 00587da4 ["CALL", null, ["callee:0043b778:8"]]
- 00587d64 bytes 75cefa97
+ 00587da4 bytes 75cefa97
- 00587d60 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00587d60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00587d60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00587d60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00587da0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00587da0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00587da0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00587da0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00587d60 bytes 00303c91
+ 00587da0 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eaa02ea73987fc777decd91431c6006d"></a>

### [`00587d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587d68.md) → [`00587da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587da8.md) FUN_00587da8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005852e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/005852e4.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 1件 [`00585324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585324.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.64% / 新版 88.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00587dc4",
      "incomplete_value": false,
      "site": "00587dc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587d84",
      "incomplete_value": false,
      "site": "00587d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "definition_site": "00587dd0",
      "incomplete_value": false,
      "site": "00587dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587d90",
      "incomplete_value": false,
      "site": "00587d90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:4e8:8"
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
      "00587dc4",
      "DATA",
      [
        "storage",
        "00c6c770",
        null,
        "undefined *"
      ]
    ],
    [
      "00587dd0",
      "DATA",
      [
        "storage",
        "00c6c4e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587dc4",
      "DATA",
      [
        "storage",
        "00c6cb70",
        null,
        "undefined *"
      ]
    ],
    [
      "00587dd0",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587d68.md#insn-00587d7c) · [`00587d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587d68.md#insn-00587d88) · [`00587d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587d68.md#insn-00587d8c)
- 新版 `00587dbc`（命令位置の公開資料なし） · `00587dcc`（命令位置の公開資料なし）

~~~diff
- 00587d7c ["COPY", "tmp:0:8", ["const:770:8"]]
- 00587d7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587d7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587d7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587dbc ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 00587dbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587dbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587dbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587d7c bytes 08c11d91
+ 00587dbc bytes 08c12d91
- 00587d88 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00587d88 bytes 283700b0
- 00587d8c ["COPY", "tmp:0:8", ["const:4e8:8"]]
- 00587d8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587d8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587d8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587dcc ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 00587dcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587dcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587dcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587d8c bytes 08a11391
+ 00587dcc bytes 08a12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf96f026effc102dea8a2d41de6b66a9"></a>

### [`00587e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587e44.md) → [`00587e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587e84.md) FUN_00587e84

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
      "definition_site": "00587e88",
      "incomplete_value": false,
      "site": "00587e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587e48",
      "incomplete_value": false,
      "site": "00587e4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "00587e8c",
      "DATA",
      [
        "storage",
        "00c6c770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587e8c",
      "DATA",
      [
        "storage",
        "00c6cb70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587e44.md#insn-00587e48)
- 新版 `00587e88`（命令位置の公開資料なし）

~~~diff
- 00587e48 ["COPY", "tmp:0:8", ["const:770:8"]]
- 00587e48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587e48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587e48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587e88 ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 00587e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587e48 bytes 08c11d91
+ 00587e88 bytes 08c12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f23efac951c73ee148554262aa3e9849"></a>

### [`00587e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587e54.md) → [`00587e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587e94.md) FUN_00587e94

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00587ea4",
      "incomplete_value": true,
      "site": "00587eac",
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
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587e64",
      "incomplete_value": true,
      "site": "00587e6c",
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
            "const:770:8"
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
      "00587eac",
      "DATA",
      [
        "storage",
        "00c6c770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587eac",
      "DATA",
      [
        "storage",
        "00c6cb70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587e54.md#insn-00587e64) · [`00587e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587e54.md#insn-00587e70)
- 新版 `00587ea4`（命令位置の公開資料なし） · `00587eb0`（命令位置の公開資料なし）

~~~diff
- 00587e64 ["COPY", "tmp:0:8", ["const:770:8"]]
- 00587e64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587e64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587e64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587ea4 ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 00587ea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587ea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587ea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587e64 bytes 08c11d91
+ 00587ea4 bytes 08c12d91
- 00587e70 ["INT_ADD", "register:40f0:8", ["const:587e70:8", "const:4:8"]]
- 00587e70 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00587eb0 ["INT_ADD", "register:40f0:8", ["const:587eb0:8", "const:4:8"]]
+ 00587eb0 ["CALL", null, ["callee:00c57ea0:8"]]
- 00587e70 bytes 0c3f1b94
+ 00587eb0 bytes fc3f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb9dce92d5bfcf9262f99aed379e4f1b"></a>

### [`00587e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587e94.md) → [`00587ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587ed4.md) FUN_00587ed4

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
      "definition_site": "00587ed8",
      "incomplete_value": false,
      "site": "00587edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587e98",
      "incomplete_value": false,
      "site": "00587e9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
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
      "00587edc",
      "DATA",
      [
        "storage",
        "00c6c7c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00587edc",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587e94.md#insn-00587e98)
- 新版 `00587ed8`（命令位置の公開資料なし）

~~~diff
- 00587e98 ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 00587e98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587e98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587e98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587ed8 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 00587ed8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587ed8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587ed8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587e98 bytes 08011f91
+ 00587ed8 bytes 08012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b0c031388813e55517d513ebbc72b8c"></a>

### [`00587ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587ea4.md) → [`00587ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587ee4.md) FUN_00587ee4

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
      "definition_site": "00587ef4",
      "incomplete_value": false,
      "site": "00587efc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587eb4",
      "incomplete_value": false,
      "site": "00587ebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
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
      "00587efc",
      "DATA",
      [
        "storage",
        "00c6c7c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00587efc",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587ea4.md#insn-00587eb4) · [`00587ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587ea4.md#insn-00587ec0)
- 新版 `00587ef4`（命令位置の公開資料なし） · `00587f00`（命令位置の公開資料なし）

~~~diff
- 00587eb4 ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 00587eb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587eb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587eb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587ef4 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 00587ef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587ef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587ef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587eb4 bytes 08011f91
+ 00587ef4 bytes 08012f91
- 00587ec0 ["INT_ADD", "register:40f0:8", ["const:587ec0:8", "const:4:8"]]
- 00587ec0 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00587f00 ["INT_ADD", "register:40f0:8", ["const:587f00:8", "const:4:8"]]
+ 00587f00 ["CALL", null, ["callee:00c57ea0:8"]]
- 00587ec0 bytes f83e1b94
+ 00587f00 bytes e83f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1266652a3da79586642001409155634c"></a>

### [`00587ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587ed4.md) → [`00587f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587f14.md) FUN_00587f14

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0058538c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058538c.md) · 呼出先 2件 [`00587038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587038.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005853cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005853cc.md) · 呼出先 2件 [`00587078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587078.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00587f28",
      "incomplete_value": false,
      "site": "00587f30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587ee8",
      "incomplete_value": false,
      "site": "00587ef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "00587f30",
      "DATA",
      [
        "storage",
        "00c6c498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587f30",
      "DATA",
      [
        "storage",
        "00c6c898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587ed4.md#insn-00587ee8) · [`00587ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587ed4.md#insn-00587ef8)
- 新版 `00587f28`（命令位置の公開資料なし） · `00587f38`（命令位置の公開資料なし）

~~~diff
- 00587ee8 ["COPY", "tmp:0:8", ["const:498:8"]]
- 00587ee8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587ee8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587ee8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587f28 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00587f28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587f28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587f28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587ee8 bytes 08611291
+ 00587f28 bytes 08612291
- 00587ef8 ["INT_ADD", "register:40f0:8", ["const:587ef8:8", "const:4:8"]]
- 00587ef8 ["CALL", null, ["callee:00587078:8"]]
+ 00587f38 ["INT_ADD", "register:40f0:8", ["const:587f38:8", "const:4:8"]]
+ 00587f38 ["CALL", null, ["callee:00587078:8"]]
- 00587ef8 bytes 50fcff97
+ 00587f38 bytes 50fcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18320d7b731912519354ff68e8887a9b"></a>

### [`00587f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587f24.md) → [`00587f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587f64.md) FUN_00587f64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0058538c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058538c.md) · 呼出先 7件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005853cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005853cc.md) · 呼出先 7件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.80% / 新版 97.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00588014",
      "incomplete_value": false,
      "site": "0058801c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587fd4",
      "incomplete_value": false,
      "site": "00587fdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "0058801c",
      "DATA",
      [
        "storage",
        "00c6c498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058801c",
      "DATA",
      [
        "storage",
        "00c6c898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587f24.md#insn-00587f5c) · [`00587fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587f24.md#insn-00587fa8) · [`00587fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587f24.md#insn-00587fc8)
- 新版 `00587f9c`（命令位置の公開資料なし） · `00587fe8`（命令位置の公開資料なし） · `00588008`（命令位置の公開資料なし）

~~~diff
- 00587f5c ["INT_ADD", "register:40f0:8", ["const:587f5c:8", "const:4:8"]]
- 00587f5c ["CALL", null, ["callee:00c57fe0:8"]]
+ 00587f9c ["INT_ADD", "register:40f0:8", ["const:587f9c:8", "const:4:8"]]
+ 00587f9c ["CALL", null, ["callee:00c57fe0:8"]]
- 00587f5c bytes 213f1b94
+ 00587f9c bytes 11401b94
- 00587fa8 ["INT_ADD", "register:40f0:8", ["const:587fa8:8", "const:4:8"]]
- 00587fa8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00587fe8 ["INT_ADD", "register:40f0:8", ["const:587fe8:8", "const:4:8"]]
+ 00587fe8 ["CALL", null, ["callee:00c57e90:8"]]
- 00587fa8 bytes ba3e1b94
+ 00587fe8 bytes aa3f1b94
- 00587fc8 ["INT_ADD", "register:40f0:8", ["const:587fc8:8", "const:4:8"]]
- 00587fc8 ["CALL", null, ["callee:00c58000:8"]]
+ 00588008 ["INT_ADD", "register:40f0:8", ["const:588008:8", "const:4:8"]]
+ 00588008 ["CALL", null, ["callee:00c58000:8"]]
- 00587fc8 bytes 0e3f1b94
+ 00588008 bytes fe3f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac0bac5a503d95c5eb2dc78cd4402fdc"></a>

### [`00588314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588314.md) → [`00588354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588354.md) FUN_00588354

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0058568c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058568c.md) [`00585ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585ed0.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00586bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586bdc.md)
- 新版 呼出元 2件 [`005856cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005856cc.md) [`00585f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585f10.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00586c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586c1c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058836c",
      "incomplete_value": false,
      "site": "00588370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058832c",
      "incomplete_value": false,
      "site": "00588330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
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
      "definition_site": "0058837c",
      "incomplete_value": false,
      "site": "00588388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058833c",
      "incomplete_value": false,
      "site": "00588348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "00588370",
      "DATA",
      [
        "storage",
        "00c6c7c0",
        null,
        "pointer"
      ]
    ],
    [
      "00588388",
      "DATA",
      [
        "storage",
        "00c6c498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00588370",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "pointer"
      ]
    ],
    [
      "00588388",
      "DATA",
      [
        "storage",
        "00c6c898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058832c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588314.md#insn-0058832c) · [`00588338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588314.md#insn-00588338) · [`0058833c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588314.md#insn-0058833c)
- 新版 `0058836c`（命令位置の公開資料なし） · `0058837c`（命令位置の公開資料なし）

~~~diff
- 0058832c ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 0058832c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058832c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058832c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058836c ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 0058836c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058836c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058836c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058832c bytes 29011f91
+ 0058836c bytes 29012f91
- 00588338 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00588338 bytes 28370090
- 0058833c ["COPY", "tmp:0:8", ["const:498:8"]]
- 0058833c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058833c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058833c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058837c ["COPY", "tmp:0:8", ["const:898:8"]]
+ 0058837c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058837c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058837c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058833c bytes 08611291
+ 0058837c bytes 08612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb36b516eca27c50f2ae13d86467e0e7"></a>

### [`005883e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005883e4.md) → [`00588424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588424.md) _INIT_32

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`005832dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005832dc.md) [`0058330c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058330c.md) [`0058333c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058333c.md) [`00583344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583344.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0058331c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058331c.md) [`0058334c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058334c.md) [`0058337c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058337c.md) [`00583384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583384.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)

変更の種類 call, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 29.27% / 新版 29.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 8件, `store_value` 2件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058844c",
      "incomplete_value": false,
      "site": "0058844c",
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
                "const:ca6000:8"
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
      "definition_site": "0058840c",
      "incomplete_value": false,
      "site": "0058840c",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:ec0:8"
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
      "definition_site": "00588468",
      "incomplete_value": false,
      "site": "00588468",
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
                "const:ca6000:8"
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
      "definition_site": "00588428",
      "incomplete_value": false,
      "site": "00588428",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:ef0:8"
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
      "definition_site": "00588488",
      "incomplete_value": false,
      "site": "00588488",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:320:8"
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
      "definition_site": "00588448",
      "incomplete_value": false,
      "site": "00588448",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:f20:8"
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
      "0058843c",
      "PARAM",
      [
        "storage",
        "00ca5ec0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00588404",
      "PARAM",
      [
        "storage",
        "005832dc",
        null,
        null
      ]
    ],
    [
      "00588448",
      "PARAM",
      [
        "storage",
        "00c62b90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058843c",
      "PARAM",
      [
        "storage",
        "00ca62c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00588444",
      "PARAM",
      [
        "storage",
        "0058331c",
        null,
        null
      ]
    ],
    [
      "00588448",
      "PARAM",
      [
        "storage",
        "00c62f90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005883e4.md#insn-00588410) · [`0058842c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005883e4.md#insn-0058842c)
- 新版 `00588450`（命令位置の公開資料なし）

~~~diff
- 00588410 ["INT_ADD", "register:40f0:8", ["const:588410:8", "const:4:8"]]
- 00588410 ["CALL", null, ["callee:00c57e30:8"]]
- 00588410 bytes 883d1b94
- 0058842c ["INT_ADD", "register:40f0:8", ["const:58842c:8", "const:4:8"]]
- 0058842c ["CALL", null, ["callee:00c57e30:8"]]
- 0058842c bytes 813d1b94
+ 00588450 ["INT_ADD", "register:40f0:8", ["const:588450:8", "const:4:8"]]
+ 00588450 ["CALL", null, ["callee:00c57e30:8"]]
+ 00588450 bytes 783e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d00c0e3db531e61eef2bea0d240d86f1"></a>

### [`00588488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588488.md) → [`005884c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005884c8.md) FUN_005884c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005975bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975bc.md) · 呼出先 2件 [`005948f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/005948f8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`005975fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005975fc.md) · 呼出先 2件 [`00594938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594938.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00588500",
      "incomplete_value": false,
      "site": "0058850c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005884c0",
      "incomplete_value": false,
      "site": "005884cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:810:8"
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
      "0058850c",
      "DATA",
      [
        "storage",
        "00c6c810",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058850c",
      "DATA",
      [
        "storage",
        "00c6cc10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005884b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588488.md#insn-005884b4) · [`005884c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588488.md#insn-005884c0) · [`005884dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588488.md#insn-005884dc)
- 新版 `005884f4`（命令位置の公開資料なし） · `00588500`（命令位置の公開資料なし） · `0058851c`（命令位置の公開資料なし）

~~~diff
- 005884b4 ["INT_ADD", "register:40f0:8", ["const:5884b4:8", "const:4:8"]]
- 005884b4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005884f4 ["INT_ADD", "register:40f0:8", ["const:5884f4:8", "const:4:8"]]
+ 005884f4 ["CALL", null, ["callee:00c57e90:8"]]
- 005884b4 bytes 773d1b94
+ 005884f4 bytes 673e1b94
- 005884c0 ["COPY", "tmp:0:8", ["const:810:8"]]
- 005884c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005884c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005884c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00588500 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 00588500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00588500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00588500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005884c0 bytes 08412091
+ 00588500 bytes 08413091
- 005884dc ["INT_ADD", "register:40f0:8", ["const:5884dc:8", "const:4:8"]]
- 005884dc ["CALL", null, ["callee:00594938:8"]]
+ 0058851c ["INT_ADD", "register:40f0:8", ["const:58851c:8", "const:4:8"]]
+ 0058851c ["CALL", null, ["callee:00594938:8"]]
- 005884dc bytes 07310094
+ 0058851c bytes 07310094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f286ab71289e9d508c774fb68405483"></a>

### [`0058851c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/0058851c.md) → [`0058855c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058855c.md) FUN_0058855c

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
      "definition_site": "00588560",
      "incomplete_value": false,
      "site": "00588564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588520",
      "incomplete_value": false,
      "site": "00588524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:810:8"
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
      "00588564",
      "DATA",
      [
        "storage",
        "00c6c810",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00588564",
      "DATA",
      [
        "storage",
        "00c6cc10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/0058851c.md#insn-00588520)
- 新版 `00588560`（命令位置の公開資料なし）

~~~diff
- 00588520 ["COPY", "tmp:0:8", ["const:810:8"]]
- 00588520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00588520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00588520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00588560 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 00588560 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00588560 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00588560 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00588520 bytes 08412091
+ 00588560 bytes 08413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c95f6d64868d3b459f7f15e52ae66d2"></a>

### [`0058852c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/0058852c.md) → [`0058856c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058856c.md) FUN_0058856c

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
      "definition_site": "0058857c",
      "incomplete_value": false,
      "site": "00588584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058853c",
      "incomplete_value": false,
      "site": "00588544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:810:8"
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
      "00588584",
      "DATA",
      [
        "storage",
        "00c6c810",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00588584",
      "DATA",
      [
        "storage",
        "00c6cc10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058853c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/0058852c.md#insn-0058853c) · [`00588548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/0058852c.md#insn-00588548)
- 新版 `0058857c`（命令位置の公開資料なし） · `00588588`（命令位置の公開資料なし）

~~~diff
- 0058853c ["COPY", "tmp:0:8", ["const:810:8"]]
- 0058853c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058853c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058853c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058857c ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 0058857c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058857c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058857c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058853c bytes 08412091
+ 0058857c bytes 08413091
- 00588548 ["INT_ADD", "register:40f0:8", ["const:588548:8", "const:4:8"]]
- 00588548 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00588588 ["INT_ADD", "register:40f0:8", ["const:588588:8", "const:4:8"]]
+ 00588588 ["CALL", null, ["callee:00c57ea0:8"]]
- 00588548 bytes 563d1b94
+ 00588588 bytes 463e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4427064689a4811c9e75a86abe28d9d4"></a>

### [`005885b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005885b8.md) → [`005885f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005885f8.md) FUN_005885f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00588b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588b80.md) · 呼出先 7件 [`00588cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588cac.md) [`0058abe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058abe4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00588bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588bc0.md) · 呼出先 7件 [`00588cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588cec.md) [`0058ac24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ac24.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.03% / 新版 97.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00588628",
      "incomplete_value": false,
      "site": "0058863c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005885e8",
      "incomplete_value": false,
      "site": "005885fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:860:8"
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
      "0058863c",
      "DATA",
      [
        "storage",
        "00c6c860",
        null,
        "undefined *"
      ]
    ],
    [
      "0058870c",
      "DATA",
      [
        "storage",
        "00c6be60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058863c",
      "DATA",
      [
        "storage",
        "00c6cc60",
        null,
        "undefined *"
      ]
    ],
    [
      "0058870c",
      "DATA",
      [
        "storage",
        "00c6c260",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005885e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005885b8.md#insn-005885e8) · [`00588618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005885b8.md#insn-00588618) · [`00588630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005885b8.md#insn-00588630)
- 新版 `00588628`（命令位置の公開資料なし） · `00588658`（命令位置の公開資料なし） · `00588670`（命令位置の公開資料なし）

~~~diff
- 005885e8 ["COPY", "tmp:0:8", ["const:860:8"]]
- 005885e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005885e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005885e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00588628 ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 00588628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00588628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00588628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005885e8 bytes 08812191
+ 00588628 bytes 08813191
- 00588618 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588618 ["INT_ADD", "register:40f0:8", ["const:588618:8", "const:4:8"]]
- 00588618 ["CALLIND", null, ["register:0:8"]]
+ 00588658 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588658 ["INT_ADD", "register:40f0:8", ["const:588658:8", "const:4:8"]]
+ 00588658 ["CALLIND", null, ["register:0:8"]]
- 00588618 bytes 00013fd6
+ 00588658 bytes 00013fd6
- 00588630 ["COPY", "register:0:8", ["register:4048:8"]]
- 00588630 ["INT_ADD", "register:40f0:8", ["const:588630:8", "const:4:8"]]
- 00588630 ["CALLIND", null, ["register:0:8"]]
+ 00588670 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00588670 ["INT_ADD", "register:40f0:8", ["const:588670:8", "const:4:8"]]
+ 00588670 ["CALLIND", null, ["register:0:8"]]
- 00588630 bytes 20013fd6
+ 00588670 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76479f124e2ee0504ba0fbc9091651ce"></a>

### [`005887a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005887a0.md) → [`005887e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005887e0.md) FUN_005887e0

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
      "definition_site": "005887f4",
      "incomplete_value": false,
      "site": "005887f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005887b4",
      "incomplete_value": false,
      "site": "005887b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:860:8"
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
      "005887f8",
      "DATA",
      [
        "storage",
        "00c6c860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005887f8",
      "DATA",
      [
        "storage",
        "00c6cc60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005887b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005887a0.md#insn-005887b4) · [`005887c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005887a0.md#insn-005887c8) · [`005887e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005887a0.md#insn-005887e8)
- 新版 `005887f4`（命令位置の公開資料なし） · `00588808`（命令位置の公開資料なし） · `00588828`（命令位置の公開資料なし）

~~~diff
- 005887b4 ["COPY", "tmp:0:8", ["const:860:8"]]
- 005887b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005887b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005887b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005887f4 ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 005887f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005887f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005887f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005887b4 bytes 08812191
+ 005887f4 bytes 08813191
- 005887c8 ["INT_ADD", "register:40f0:8", ["const:5887c8:8", "const:4:8"]]
- 005887c8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00588808 ["INT_ADD", "register:40f0:8", ["const:588808:8", "const:4:8"]]
+ 00588808 ["CALL", null, ["callee:00c53d00:8"]]
- 005887c8 bytes 462c1b94
+ 00588808 bytes 3e2d1b94
- 005887e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005887e8 ["INT_ADD", "register:40f0:8", ["const:5887e8:8", "const:4:8"]]
- 005887e8 ["CALLIND", null, ["register:0:8"]]
+ 00588828 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588828 ["INT_ADD", "register:40f0:8", ["const:588828:8", "const:4:8"]]
+ 00588828 ["CALLIND", null, ["register:0:8"]]
- 005887e8 bytes 00013fd6
+ 00588828 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-072319635c21a3acb5ac30312193f29a"></a>

### [`005887fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005887fc.md) → [`0058883c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058883c.md) FUN_0058883c

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
      "definition_site": "00588854",
      "incomplete_value": false,
      "site": "00588858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588814",
      "incomplete_value": false,
      "site": "00588818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:860:8"
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
      "00588858",
      "DATA",
      [
        "storage",
        "00c6c860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00588858",
      "DATA",
      [
        "storage",
        "00c6cc60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005887fc.md#insn-00588814) · [`00588828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005887fc.md#insn-00588828) · [`0058883c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005887fc.md#insn-0058883c)
- 新版 `00588854`（命令位置の公開資料なし） · `00588868`（命令位置の公開資料なし） · `0058887c`（命令位置の公開資料なし）

~~~diff
- 00588814 ["COPY", "tmp:0:8", ["const:860:8"]]
- 00588814 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00588814 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00588814 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00588854 ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 00588854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00588854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00588854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00588814 bytes 08812191
+ 00588854 bytes 08813191
- 00588828 ["INT_ADD", "register:40f0:8", ["const:588828:8", "const:4:8"]]
- 00588828 ["CALL", null, ["callee:00c53d00:8"]]
+ 00588868 ["INT_ADD", "register:40f0:8", ["const:588868:8", "const:4:8"]]
+ 00588868 ["CALL", null, ["callee:00c53d00:8"]]
- 00588828 bytes 2e2c1b94
+ 00588868 bytes 262d1b94
- 0058883c ["COPY", "register:0:8", ["register:4040:8"]]
- 0058883c ["INT_ADD", "register:40f0:8", ["const:58883c:8", "const:4:8"]]
- 0058883c ["CALLIND", null, ["register:0:8"]]
+ 0058887c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058887c ["INT_ADD", "register:40f0:8", ["const:58887c:8", "const:4:8"]]
+ 0058887c ["CALLIND", null, ["register:0:8"]]
- 0058883c bytes 00013fd6
+ 0058887c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94ed7fd15f4fa2fe12ad1e2405681f92"></a>

### [`00588b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588b80.md) → [`00588bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588bc0.md) FUN_00588bc0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00588ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588ab8.md) [`005975c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c4.md) · 呼出先 6件 [`005885b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005885b8.md) [`005975bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975bc.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`00588af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588af8.md) [`00597604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597604.md) · 呼出先 6件 [`005885f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005885f8.md) [`005975fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005975fc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00588c10",
      "incomplete_value": false,
      "site": "00588c1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588bd0",
      "incomplete_value": false,
      "site": "00588bdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:540:8"
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
      "00588c1c",
      "DATA",
      [
        "storage",
        "00c6b540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00588c1c",
      "DATA",
      [
        "storage",
        "00c6b940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588b80.md#insn-00588bb4) · [`00588bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588b80.md#insn-00588bc4) · [`00588bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588b80.md#insn-00588bd0)
- 新版 `00588bf4`（命令位置の公開資料なし） · `00588c04`（命令位置の公開資料なし） · `00588c10`（命令位置の公開資料なし）

~~~diff
- 00588bb4 ["INT_ADD", "register:40f0:8", ["const:588bb4:8", "const:4:8"]]
- 00588bb4 ["CALL", null, ["callee:005975fc:8"]]
+ 00588bf4 ["INT_ADD", "register:40f0:8", ["const:588bf4:8", "const:4:8"]]
+ 00588bf4 ["CALL", null, ["callee:005975fc:8"]]
- 00588bb4 bytes 823a0094
+ 00588bf4 bytes 823a0094
- 00588bc4 ["INT_ADD", "register:40f0:8", ["const:588bc4:8", "const:4:8"]]
- 00588bc4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00588c04 ["INT_ADD", "register:40f0:8", ["const:588c04:8", "const:4:8"]]
+ 00588c04 ["CALL", null, ["callee:00c57e90:8"]]
- 00588bc4 bytes b33b1b94
+ 00588c04 bytes a33c1b94
- 00588bd0 ["COPY", "tmp:0:8", ["const:540:8"]]
- 00588bd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00588bd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00588bd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00588c10 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 00588c10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00588c10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00588c10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00588bd0 bytes 08011591
+ 00588c10 bytes 08012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f092ea5dd3c4418e5eb244948d76950"></a>

### [`00588db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588db8.md) → [`00588df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588df8.md) FUN_00588df8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0043aee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043aee4.md) · 呼出先 3件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md) [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c59ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ef0.md)
- 新版 呼出元 1件 [`0043af24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043af24.md) · 呼出先 3件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md) [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c5a2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2f0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 72.41% / 新版 72.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00588e0c",
      "incomplete_value": false,
      "site": "00588e10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588dcc",
      "incomplete_value": false,
      "site": "00588dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00588e38",
      "incomplete_value": true,
      "site": "00588e38",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588df8",
      "incomplete_value": true,
      "site": "00588df8",
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
                "const:20:8"
              ]
            ]
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
      "definition_site": "00588e28",
      "incomplete_value": true,
      "site": "00588e38",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:350:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588de8",
      "incomplete_value": true,
      "site": "00588df8",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:f50:8"
              ]
            ]
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
      "00588e0c",
      "PARAM",
      [
        "storage",
        "00ca3a00",
        null,
        null
      ]
    ],
    [
      "00588e28",
      "READ",
      [
        "storage",
        "00ca5f50",
        null,
        "undefined8"
      ]
    ],
    [
      "00588e44",
      "READ",
      [
        "storage",
        "00ca5f90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00588e0c",
      "PARAM",
      [
        "storage",
        "00ca3e00",
        null,
        null
      ]
    ],
    [
      "00588e28",
      "READ",
      [
        "storage",
        "00ca6350",
        null,
        "undefined8"
      ]
    ],
    [
      "00588e44",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588db8.md#insn-00588dd0) · [`00588df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588db8.md#insn-00588df8) · [`00588e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588db8.md#insn-00588e08)
- 新版 `00588e10`（命令位置の公開資料なし） · `00588e38`（命令位置の公開資料なし） · `00588e48`（命令位置の公開資料なし）

~~~diff
- 00588dd0 ["INT_ADD", "register:40f0:8", ["const:588dd0:8", "const:4:8"]]
- 00588dd0 ["CALL", null, ["callee:00c5a2f0:8"]]
+ 00588e10 ["INT_ADD", "register:40f0:8", ["const:588e10:8", "const:4:8"]]
+ 00588e10 ["CALL", null, ["callee:00c5a2f0:8"]]
- 00588dd0 bytes 48441b94
+ 00588e10 bytes 38451b94
- 00588df8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588df8 ["INT_ADD", "register:40f0:8", ["const:588df8:8", "const:4:8"]]
- 00588df8 ["CALLIND", null, ["register:0:8"]]
+ 00588e38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588e38 ["INT_ADD", "register:40f0:8", ["const:588e38:8", "const:4:8"]]
+ 00588e38 ["CALLIND", null, ["register:0:8"]]
- 00588df8 bytes 00013fd6
+ 00588e38 bytes 00013fd6
- 00588e08 ["INT_ADD", "register:40f0:8", ["const:588e08:8", "const:4:8"]]
- 00588e08 ["CALL", null, ["callee:00c58140:8"]]
+ 00588e48 ["INT_ADD", "register:40f0:8", ["const:588e48:8", "const:4:8"]]
+ 00588e48 ["CALL", null, ["callee:00c58140:8"]]
- 00588e08 bytes ce3b1b94
+ 00588e48 bytes be3c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23c6724f95eda932b8e76359006f0cd0"></a>

### [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) → [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) FUN_00588e6c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 138件 [`00497664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497664.md) [`00497890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497890.md) [`0049b17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md) [`005717c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717c0.md) [`0057192c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/0057192c.md) · 呼出先 2件 [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c59ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ef0.md)
- 新版 呼出元 138件 [`004976a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004976a4.md) [`004978d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004978d0.md) [`0049b1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b1bc.md) [`00571800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571800.md) [`0057196c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/0057196c.md) · 呼出先 2件 [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c5a2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2f0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 70.83% / 新版 70.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00588e7c",
      "incomplete_value": false,
      "site": "00588e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588e3c",
      "incomplete_value": false,
      "site": "00588e40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00588ea8",
      "incomplete_value": true,
      "site": "00588ea8",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588e68",
      "incomplete_value": true,
      "site": "00588e68",
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
                "const:20:8"
              ]
            ]
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
      "definition_site": "00588e9c",
      "incomplete_value": true,
      "site": "00588ea8",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:350:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588e5c",
      "incomplete_value": true,
      "site": "00588e68",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:f50:8"
              ]
            ]
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
      "00588e7c",
      "PARAM",
      [
        "storage",
        "00ca3a00",
        null,
        null
      ]
    ],
    [
      "00588e9c",
      "READ",
      [
        "storage",
        "00ca5f50",
        null,
        "undefined8"
      ]
    ],
    [
      "00588eb4",
      "READ",
      [
        "storage",
        "00ca5f90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00588e7c",
      "PARAM",
      [
        "storage",
        "00ca3e00",
        null,
        null
      ]
    ],
    [
      "00588e9c",
      "READ",
      [
        "storage",
        "00ca6350",
        null,
        "undefined8"
      ]
    ],
    [
      "00588eb4",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md#insn-00588e40) · [`00588e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md#insn-00588e68) · [`00588e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md#insn-00588e78)
- 新版 `00588e80`（命令位置の公開資料なし） · `00588ea8`（命令位置の公開資料なし） · `00588eb8`（命令位置の公開資料なし）

~~~diff
- 00588e40 ["INT_ADD", "register:40f0:8", ["const:588e40:8", "const:4:8"]]
- 00588e40 ["CALL", null, ["callee:00c5a2f0:8"]]
+ 00588e80 ["INT_ADD", "register:40f0:8", ["const:588e80:8", "const:4:8"]]
+ 00588e80 ["CALL", null, ["callee:00c5a2f0:8"]]
- 00588e40 bytes 2c441b94
+ 00588e80 bytes 1c451b94
- 00588e68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588e68 ["INT_ADD", "register:40f0:8", ["const:588e68:8", "const:4:8"]]
- 00588e68 ["CALLIND", null, ["register:0:8"]]
+ 00588ea8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588ea8 ["INT_ADD", "register:40f0:8", ["const:588ea8:8", "const:4:8"]]
+ 00588ea8 ["CALLIND", null, ["register:0:8"]]
- 00588e68 bytes 00013fd6
+ 00588ea8 bytes 00013fd6
- 00588e78 ["INT_ADD", "register:40f0:8", ["const:588e78:8", "const:4:8"]]
- 00588e78 ["CALL", null, ["callee:00c58140:8"]]
+ 00588eb8 ["INT_ADD", "register:40f0:8", ["const:588eb8:8", "const:4:8"]]
+ 00588eb8 ["CALL", null, ["callee:00c58140:8"]]
- 00588e78 bytes b23b1b94
+ 00588eb8 bytes a23c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad6feea4ca2be806118a87b18704393f"></a>

### [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md) → [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md) FUN_00588ecc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 11件 [`00588db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588db8.md) [`00589750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589750.md) [`005897b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005897b4.md) [`00589820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589820.md) [`0058a274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a274.md) · 呼出先 3件 [`0058a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md) [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c59ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ef0.md)
- 新版 呼出元 11件 [`00588df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588df8.md) [`00589790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589790.md) [`005897f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005897f4.md) [`00589860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589860.md) [`0058a2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a2b4.md) · 呼出先 3件 [`0058a94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md) [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c5a2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2f0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00588ef8",
      "incomplete_value": false,
      "site": "00588efc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588eb8",
      "incomplete_value": false,
      "site": "00588ebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00588f24",
      "incomplete_value": true,
      "site": "00588f24",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588ee4",
      "incomplete_value": true,
      "site": "00588ee4",
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
                "const:20:8"
              ]
            ]
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
      "definition_site": "00588f14",
      "incomplete_value": true,
      "site": "00588f24",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:350:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588ed4",
      "incomplete_value": true,
      "site": "00588ee4",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:f50:8"
              ]
            ]
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
      "00588ef8",
      "PARAM",
      [
        "storage",
        "00ca3a00",
        null,
        null
      ]
    ],
    [
      "00588f14",
      "READ",
      [
        "storage",
        "00ca5f50",
        null,
        "undefined8"
      ]
    ],
    [
      "00588f30",
      "READ",
      [
        "storage",
        "00ca5f90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00588ef8",
      "PARAM",
      [
        "storage",
        "00ca3e00",
        null,
        null
      ]
    ],
    [
      "00588f14",
      "READ",
      [
        "storage",
        "00ca6350",
        null,
        "undefined8"
      ]
    ],
    [
      "00588f30",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md#insn-00588ebc) · [`00588ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md#insn-00588ee4) · [`00588ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md#insn-00588ef4)
- 新版 `00588efc`（命令位置の公開資料なし） · `00588f24`（命令位置の公開資料なし） · `00588f34`（命令位置の公開資料なし）

~~~diff
- 00588ebc ["INT_ADD", "register:40f0:8", ["const:588ebc:8", "const:4:8"]]
- 00588ebc ["CALL", null, ["callee:00c5a2f0:8"]]
+ 00588efc ["INT_ADD", "register:40f0:8", ["const:588efc:8", "const:4:8"]]
+ 00588efc ["CALL", null, ["callee:00c5a2f0:8"]]
- 00588ebc bytes 0d441b94
+ 00588efc bytes fd441b94
- 00588ee4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588ee4 ["INT_ADD", "register:40f0:8", ["const:588ee4:8", "const:4:8"]]
- 00588ee4 ["CALLIND", null, ["register:0:8"]]
+ 00588f24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588f24 ["INT_ADD", "register:40f0:8", ["const:588f24:8", "const:4:8"]]
+ 00588f24 ["CALLIND", null, ["register:0:8"]]
- 00588ee4 bytes 00013fd6
+ 00588f24 bytes 00013fd6
- 00588ef4 ["INT_ADD", "register:40f0:8", ["const:588ef4:8", "const:4:8"]]
- 00588ef4 ["CALL", null, ["callee:00c58140:8"]]
+ 00588f34 ["INT_ADD", "register:40f0:8", ["const:588f34:8", "const:4:8"]]
+ 00588f34 ["CALL", null, ["callee:00c58140:8"]]
- 00588ef4 bytes 933b1b94
+ 00588f34 bytes 833c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-164392e601b4fdd0e4773a8e629749d1"></a>

### [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) → [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) FUN_0058915c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 122件 [`00497664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497664.md) [`00497890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497890.md) [`0049b17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md) [`005717c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717c0.md) [`0057192c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/0057192c.md) · 呼出先 0件 
- 新版 呼出元 122件 [`004976a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004976a4.md) [`004978d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004978d0.md) [`0049b1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b1bc.md) [`00571800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571800.md) [`0057196c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/0057196c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00589160",
      "incomplete_value": false,
      "site": "00589164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589120",
      "incomplete_value": false,
      "site": "00589124",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:f58:8"
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
      "00589160",
      "DATA",
      [
        "storage",
        "00ca5f58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00589160",
      "DATA",
      [
        "storage",
        "00ca6358",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md#insn-0058911c) · [`00589120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md#insn-00589120)
- 新版 `0058915c`（命令位置の公開資料なし） · `00589160`（命令位置の公開資料なし）

~~~diff
- 0058911c ["COPY", "register:4000:8", ["const:ca5000:8"]]
+ 0058915c ["COPY", "register:4000:8", ["const:ca6000:8"]]
- 0058911c bytes e0380090
+ 0058915c bytes e03800b0
- 00589120 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 00589120 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00589120 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00589120 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00589160 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 00589160 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00589160 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00589160 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00589120 bytes 00603d91
+ 00589160 bytes 00600d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e1521858ff09919ba495a4dfa26b3bb"></a>

### [`00589128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589128.md) → [`00589168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589168.md) FUN_00589168

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0058d130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d130.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0058d170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d170.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00589174",
      "incomplete_value": false,
      "site": "00589174",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589134",
      "incomplete_value": false,
      "site": "00589134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "00589174",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00589174",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058912c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589128.md#insn-0058912c)
- 新版 `0058916c`（命令位置の公開資料なし）

~~~diff
- 0058912c ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 0058912c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058912c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058912c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058916c ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 0058916c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058916c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058916c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058912c bytes 08a12391
+ 0058916c bytes 08a13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d02ae2d980cb3db44a467da0118edf3"></a>

### [`00589150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589150.md) → [`00589190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589190.md) FUN_00589190

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058a220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a220.md) · 呼出先 4件 [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0058a260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a260.md) · 呼出先 4件 [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005891c0",
      "incomplete_value": false,
      "site": "005891c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589180",
      "incomplete_value": false,
      "site": "00589180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "005891c0",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005891c0",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058917c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589150.md#insn-0058917c) · [`005891a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589150.md#insn-005891a4) · [`00589208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589150.md#insn-00589208)
- 新版 `005891bc`（命令位置の公開資料なし） · `005891e4`（命令位置の公開資料なし） · `00589248`（命令位置の公開資料なし）

~~~diff
- 0058917c ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 0058917c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058917c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058917c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005891bc ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 005891bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005891bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005891bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058917c bytes 08a12391
+ 005891bc bytes 08a13391
- 005891a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005891a4 ["INT_ADD", "register:40f0:8", ["const:5891a4:8", "const:4:8"]]
- 005891a4 ["CALLIND", null, ["register:0:8"]]
+ 005891e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005891e4 ["INT_ADD", "register:40f0:8", ["const:5891e4:8", "const:4:8"]]
+ 005891e4 ["CALLIND", null, ["register:0:8"]]
- 005891a4 bytes 00013fd6
+ 005891e4 bytes 00013fd6
- 00589208 ["INT_ADD", "register:40f0:8", ["const:589208:8", "const:4:8"]]
- 00589208 ["CALL", null, ["callee:00589320:8"]]
+ 00589248 ["INT_ADD", "register:40f0:8", ["const:589248:8", "const:4:8"]]
+ 00589248 ["CALL", null, ["callee:00589320:8"]]
- 00589208 bytes 36000094
+ 00589248 bytes 36000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1fe3d4c9fc0ba7a916cb5116f2b60e6"></a>

### [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) → [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) FUN_00589320

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 130件 [`00497664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497664.md) [`00497890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497890.md) [`0049b17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md) [`005717c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717c0.md) [`0057192c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/0057192c.md) · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0058a96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a96c.md) [`0058aa94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aa94.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 130件 [`004976a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004976a4.md) [`004978d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004978d0.md) [`0049b1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b1bc.md) [`00571800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571800.md) [`0057196c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/0057196c.md) · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0058a9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a9ac.md) [`0058aad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058aad4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.58% / 新版 93.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00589410",
      "incomplete_value": false,
      "site": "00589414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005893d0",
      "incomplete_value": false,
      "site": "005893d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "definition_site": "00589434",
      "incomplete_value": false,
      "site": "00589438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005893f4",
      "incomplete_value": false,
      "site": "005893f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00589460",
      "incomplete_value": true,
      "site": "00589460",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589420",
      "incomplete_value": true,
      "site": "00589420",
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
                "const:20:8"
              ]
            ]
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
      "00589410",
      "PARAM",
      [
        "storage",
        "00ca3a00",
        null,
        null
      ]
    ],
    [
      "00589434",
      "PARAM",
      [
        "storage",
        "00ca3a00",
        null,
        null
      ]
    ],
    [
      "0058944c",
      "READ",
      [
        "storage",
        "00ca5f50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00589410",
      "PARAM",
      [
        "storage",
        "00ca3e00",
        null,
        null
      ]
    ],
    [
      "00589434",
      "PARAM",
      [
        "storage",
        "00ca3e00",
        null,
        null
      ]
    ],
    [
      "0058944c",
      "READ",
      [
        "storage",
        "00ca6350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005893d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md#insn-005893d4) · [`005893f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md#insn-005893f8) · [`00589420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md#insn-00589420)
- 新版 `00589414`（命令位置の公開資料なし） · `00589438`（命令位置の公開資料なし） · `00589460`（命令位置の公開資料なし）

~~~diff
- 005893d4 ["INT_ADD", "register:40f0:8", ["const:5893d4:8", "const:4:8"]]
- 005893d4 ["CALL", null, ["callee:00c5a2f0:8"]]
+ 00589414 ["INT_ADD", "register:40f0:8", ["const:589414:8", "const:4:8"]]
+ 00589414 ["CALL", null, ["callee:00c5a2f0:8"]]
- 005893d4 bytes c7421b94
+ 00589414 bytes b7431b94
- 005893f8 ["INT_ADD", "register:40f0:8", ["const:5893f8:8", "const:4:8"]]
- 005893f8 ["CALL", null, ["callee:00c5a2f0:8"]]
+ 00589438 ["INT_ADD", "register:40f0:8", ["const:589438:8", "const:4:8"]]
+ 00589438 ["CALL", null, ["callee:00c5a2f0:8"]]
- 005893f8 bytes be421b94
+ 00589438 bytes ae431b94
- 00589420 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589420 ["INT_ADD", "register:40f0:8", ["const:589420:8", "const:4:8"]]
- 00589420 ["CALLIND", null, ["register:0:8"]]
+ 00589460 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589460 ["INT_ADD", "register:40f0:8", ["const:589460:8", "const:4:8"]]
+ 00589460 ["CALLIND", null, ["register:0:8"]]
- 00589420 bytes 00013fd6
+ 00589460 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a57ef5948ff5ca05a9f527e2bb125df"></a>

### [`00589750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589750.md) → [`00589790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589790.md) FUN_00589790

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0057e49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e49c.md) [`0057e7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e7f4.md) [`00581f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581f7c.md) · 呼出先 1件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md)
- 新版 呼出元 3件 [`0057e4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e4dc.md) [`0057e834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e834.md) [`00581fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581fbc.md) · 呼出先 1件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005897a8",
      "incomplete_value": false,
      "site": "005897a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589768",
      "incomplete_value": false,
      "site": "00589768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "005897a8",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005897a8",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00589760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589750.md#insn-00589760) · [`00589764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589750.md#insn-00589764) · [`0058978c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589750.md#insn-0058978c)
- 新版 `005897a0`（命令位置の公開資料なし） · `005897cc`（命令位置の公開資料なし）

~~~diff
- 00589760 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 00589760 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00589760 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00589760 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005897a0 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 005897a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005897a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005897a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00589760 bytes 08a12391
+ 005897a0 bytes 08a13391
- 00589764 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00589764 bytes f40300aa
- 0058978c ["INT_ADD", "register:40f0:8", ["const:58978c:8", "const:4:8"]]
- 0058978c ["CALL", null, ["callee:00588ecc:8"]]
+ 005897cc ["INT_ADD", "register:40f0:8", ["const:5897cc:8", "const:4:8"]]
+ 005897cc ["CALL", null, ["callee:00588ecc:8"]]
- 0058978c bytes c0fdff97
+ 005897cc bytes c0fdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7afa95bd0e6b1bf8a8d1aa7de98161f7"></a>

### [`005897b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005897b4.md) → [`005897f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005897f4.md) FUN_005897f4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md) [`0058a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md) [`0058a94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00589808",
      "incomplete_value": false,
      "site": "0058980c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005897c8",
      "incomplete_value": false,
      "site": "005897cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "0058980c",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058980c",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005897c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005897b4.md#insn-005897c8) · [`005897dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005897b4.md#insn-005897dc) · [`005897e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005897b4.md#insn-005897e8)
- 新版 `00589808`（命令位置の公開資料なし） · `0058981c`（命令位置の公開資料なし） · `00589828`（命令位置の公開資料なし）

~~~diff
- 005897c8 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 005897c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005897c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005897c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00589808 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 00589808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00589808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00589808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005897c8 bytes 08a12391
+ 00589808 bytes 08a13391
- 005897dc ["INT_ADD", "register:40f0:8", ["const:5897dc:8", "const:4:8"]]
- 005897dc ["CALL", null, ["callee:00588ecc:8"]]
+ 0058981c ["INT_ADD", "register:40f0:8", ["const:58981c:8", "const:4:8"]]
+ 0058981c ["CALL", null, ["callee:00588ecc:8"]]
- 005897dc bytes acfdff97
+ 0058981c bytes acfdff97
- 005897e8 ["INT_ADD", "register:40f0:8", ["const:5897e8:8", "const:4:8"]]
- 005897e8 ["CALL", null, ["callee:0058a94c:8"]]
+ 00589828 ["INT_ADD", "register:40f0:8", ["const:589828:8", "const:4:8"]]
+ 00589828 ["CALL", null, ["callee:0058a94c:8"]]
- 005897e8 bytes 49040094
+ 00589828 bytes 49040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44c5147ce786106e60d709f1a796215b"></a>

### [`00589890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589890.md) → [`005898d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005898d0.md) FUN_005898d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 55件 [`0049b17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md) [`00571ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571ab4.md) [`00571dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571dd8.md) [`005720b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/005720b8.md) [`0057226c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/0057226c.md) · 呼出先 0件 
- 新版 呼出元 55件 [`0049b1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b1bc.md) [`00571af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571af4.md) [`00571e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571e18.md) [`005720f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005720f8.md) [`005722ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005722ac.md) · 呼出先 0件 

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
      "definition_site": "00589904",
      "incomplete_value": false,
      "site": "00589904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005898c4",
      "incomplete_value": false,
      "site": "005898c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:908:8"
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
      "00589904",
      "DATA",
      [
        "storage",
        "00c6c908",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00589904",
      "DATA",
      [
        "storage",
        "00c6cd08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005898c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589890.md#insn-005898c0) · [`005898e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589890.md#insn-005898e4)
- 新版 `00589900`（命令位置の公開資料なし） · `00589924`（命令位置の公開資料なし）

~~~diff
- 005898c0 ["COPY", "tmp:0:8", ["const:908:8"]]
- 005898c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005898c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005898c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00589900 ["COPY", "tmp:0:8", ["const:d08:8"]]
+ 00589900 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00589900 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00589900 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005898c0 bytes 29212491
+ 00589900 bytes 29213491
- 005898e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005898e4 ["INT_ADD", "register:40f0:8", ["const:5898e4:8", "const:4:8"]]
- 005898e4 ["CALLIND", null, ["register:0:8"]]
+ 00589924 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00589924 ["INT_ADD", "register:40f0:8", ["const:589924:8", "const:4:8"]]
+ 00589924 ["CALLIND", null, ["register:0:8"]]
- 005898e4 bytes 20013fd6
+ 00589924 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d9fa09abd647568cce1627f3e79c2b8"></a>

### [`00589ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ba8.md) → [`00589be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589be8.md) FUN_00589be8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`00580848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580848.md) [`00582198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582198.md) [`00582320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582320.md) [`005824b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/005824b4.md) [`00582630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582630.md) · 呼出先 0件 
- 新版 呼出元 7件 [`00580888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580888.md) [`005821d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005821d8.md) [`00582360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582360.md) [`005824f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005824f4.md) [`00582670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582670.md) · 呼出先 0件 

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
      "definition_site": "00589c08",
      "incomplete_value": false,
      "site": "00589c08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589bc8",
      "incomplete_value": false,
      "site": "00589bc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "00589c08",
      "DATA",
      [
        "storage",
        "00c6c928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00589c08",
      "DATA",
      [
        "storage",
        "00c6cd28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00589bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ba8.md#insn-00589bc4) · [`00589be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ba8.md#insn-00589be8) · [`00589c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ba8.md#insn-00589c04)
- 新版 `00589c04`（命令位置の公開資料なし） · `00589c28`（命令位置の公開資料なし） · `00589c44`（命令位置の公開資料なし）

~~~diff
- 00589bc4 ["COPY", "tmp:0:8", ["const:928:8"]]
- 00589bc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00589bc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00589bc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00589c04 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00589c04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00589c04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00589c04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00589bc4 bytes 08a12491
+ 00589c04 bytes 08a13491
- 00589be8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589be8 ["INT_ADD", "register:40f0:8", ["const:589be8:8", "const:4:8"]]
- 00589be8 ["CALLIND", null, ["register:0:8"]]
+ 00589c28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589c28 ["INT_ADD", "register:40f0:8", ["const:589c28:8", "const:4:8"]]
+ 00589c28 ["CALLIND", null, ["register:0:8"]]
- 00589be8 bytes 00013fd6
+ 00589c28 bytes 00013fd6
- 00589c04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589c04 ["INT_ADD", "register:40f0:8", ["const:589c04:8", "const:4:8"]]
- 00589c04 ["CALLIND", null, ["register:0:8"]]
+ 00589c44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589c44 ["INT_ADD", "register:40f0:8", ["const:589c44:8", "const:4:8"]]
+ 00589c44 ["CALLIND", null, ["register:0:8"]]
- 00589c04 bytes 00013fd6
+ 00589c44 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1a9448add202c6e1d5cc597eba0627e"></a>

### [`00589c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589c44.md) → [`00589c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589c84.md) FUN_00589c84

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00580058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580058.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00580098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580098.md) · 呼出先 0件 

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
      "definition_site": "00589c98",
      "incomplete_value": false,
      "site": "00589ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589c58",
      "incomplete_value": false,
      "site": "00589c60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "00589ca0",
      "DATA",
      [
        "storage",
        "00c6c928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00589ca0",
      "DATA",
      [
        "storage",
        "00c6cd28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00589c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589c44.md#insn-00589c58) · [`00589c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589c44.md#insn-00589c74)
- 新版 `00589c98`（命令位置の公開資料なし） · `00589cb4`（命令位置の公開資料なし）

~~~diff
- 00589c58 ["COPY", "tmp:0:8", ["const:928:8"]]
- 00589c58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00589c58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00589c58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00589c98 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00589c98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00589c98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00589c98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00589c58 bytes 29a12491
+ 00589c98 bytes 29a13491
- 00589c74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589c74 ["INT_ADD", "register:40f0:8", ["const:589c74:8", "const:4:8"]]
- 00589c74 ["CALLIND", null, ["register:0:8"]]
+ 00589cb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589cb4 ["INT_ADD", "register:40f0:8", ["const:589cb4:8", "const:4:8"]]
+ 00589cb4 ["CALLIND", null, ["register:0:8"]]
- 00589c74 bytes 00013fd6
+ 00589cb4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a455fb6a51212c04d7d17320480d9040"></a>

### [`00589c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589c88.md) → [`00589cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589cc8.md) FUN_00589cc8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00582198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582198.md) · 呼出先 0件 
- 新版 呼出元 1件 [`005821d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005821d8.md) · 呼出先 0件 

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
      "definition_site": "00589ce4",
      "incomplete_value": false,
      "site": "00589ce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589ca4",
      "incomplete_value": false,
      "site": "00589ca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "00589ce4",
      "DATA",
      [
        "storage",
        "00c6c928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00589ce4",
      "DATA",
      [
        "storage",
        "00c6cd28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00589c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589c88.md#insn-00589c9c) · [`00589cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589c88.md#insn-00589cd4) · [`00589cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589c88.md#insn-00589cf0)
- 新版 `00589cdc`（命令位置の公開資料なし） · `00589d14`（命令位置の公開資料なし） · `00589d30`（命令位置の公開資料なし）

~~~diff
- 00589c9c ["COPY", "tmp:0:8", ["const:928:8"]]
- 00589c9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00589c9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00589c9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00589cdc ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00589cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00589cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00589cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00589c9c bytes 08a12491
+ 00589cdc bytes 08a13491
- 00589cd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589cd4 ["INT_ADD", "register:40f0:8", ["const:589cd4:8", "const:4:8"]]
- 00589cd4 ["CALLIND", null, ["register:0:8"]]
+ 00589d14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589d14 ["INT_ADD", "register:40f0:8", ["const:589d14:8", "const:4:8"]]
+ 00589d14 ["CALLIND", null, ["register:0:8"]]
- 00589cd4 bytes 00013fd6
+ 00589d14 bytes 00013fd6
- 00589cf0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589cf0 ["INT_ADD", "register:40f0:8", ["const:589cf0:8", "const:4:8"]]
- 00589cf0 ["CALLIND", null, ["register:0:8"]]
+ 00589d30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589d30 ["INT_ADD", "register:40f0:8", ["const:589d30:8", "const:4:8"]]
+ 00589d30 ["CALLIND", null, ["register:0:8"]]
- 00589cf0 bytes 00013fd6
+ 00589d30 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd0fc7beb896ec6314330cf4bf59d63d"></a>

### [`00589ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ec8.md) → [`00589f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589f08.md) FUN_00589f08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 10件 [`00580058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580058.md) [`00580464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580464.md) [`00581454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581454.md) [`00581724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581724.md) [`00582198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582198.md) · 呼出先 2件 [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c59ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ef0.md)
- 新版 呼出元 10件 [`00580098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580098.md) [`005804a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/005804a4.md) [`00581494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581494.md) [`00581764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581764.md) [`005821d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005821d8.md) · 呼出先 2件 [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c5a2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2f0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.08% / 新版 86.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00589f18",
      "incomplete_value": false,
      "site": "00589f20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589ed8",
      "incomplete_value": false,
      "site": "00589ee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00589f28",
      "incomplete_value": false,
      "site": "00589f2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589ee8",
      "incomplete_value": false,
      "site": "00589eec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00589f60",
      "incomplete_value": true,
      "site": "00589f60",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589f20",
      "incomplete_value": true,
      "site": "00589f20",
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
                "const:20:8"
              ]
            ]
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
      "00589f20",
      "DATA",
      [
        "storage",
        "00c6c928",
        null,
        "undefined *"
      ]
    ],
    [
      "00589f28",
      "PARAM",
      [
        "storage",
        "00ca3a00",
        null,
        null
      ]
    ],
    [
      "00589f4c",
      "READ",
      [
        "storage",
        "00ca5f50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00589f20",
      "DATA",
      [
        "storage",
        "00c6cd28",
        null,
        "undefined *"
      ]
    ],
    [
      "00589f28",
      "PARAM",
      [
        "storage",
        "00ca3e00",
        null,
        null
      ]
    ],
    [
      "00589f4c",
      "READ",
      [
        "storage",
        "00ca6350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00589eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ec8.md#insn-00589eec) · [`00589f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ec8.md#insn-00589f20) · [`00589f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ec8.md#insn-00589f2c)
- 新版 `00589f2c`（命令位置の公開資料なし） · `00589f60`（命令位置の公開資料なし） · `00589f6c`（命令位置の公開資料なし）

~~~diff
- 00589eec ["INT_ADD", "register:40f0:8", ["const:589eec:8", "const:4:8"]]
- 00589eec ["CALL", null, ["callee:00c5a2f0:8"]]
+ 00589f2c ["INT_ADD", "register:40f0:8", ["const:589f2c:8", "const:4:8"]]
+ 00589f2c ["CALL", null, ["callee:00c5a2f0:8"]]
- 00589eec bytes 01401b94
+ 00589f2c bytes f1401b94
- 00589f20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589f20 ["INT_ADD", "register:40f0:8", ["const:589f20:8", "const:4:8"]]
- 00589f20 ["CALLIND", null, ["register:0:8"]]
+ 00589f60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589f60 ["INT_ADD", "register:40f0:8", ["const:589f60:8", "const:4:8"]]
+ 00589f60 ["CALLIND", null, ["register:0:8"]]
- 00589f20 bytes 00013fd6
+ 00589f60 bytes 00013fd6
- 00589f2c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 00589f2c ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00589f2c ["INT_ZEXT", "register:4000:8", ["tmp:1:4"]]
+ 00589f6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:390:8"]]
+ 00589f6c ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 00589f6c ["INT_ZEXT", "register:4000:8", ["tmp:1:4"]]
- 00589f2c bytes 00914fb9
+ 00589f6c bytes 009143b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-886263a8fca795af2e4fc8a59d230264"></a>

### [`0058a02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a02c.md) → [`0058a06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a06c.md) FUN_0058a06c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c59ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ef0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c5a2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2f0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0058a080",
      "incomplete_value": false,
      "site": "0058a084",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a040",
      "incomplete_value": false,
      "site": "0058a044",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0058a0ac",
      "incomplete_value": true,
      "site": "0058a0ac",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a06c",
      "incomplete_value": true,
      "site": "0058a06c",
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
                "const:20:8"
              ]
            ]
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
      "definition_site": "0058a0a0",
      "incomplete_value": true,
      "site": "0058a0ac",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:350:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a060",
      "incomplete_value": true,
      "site": "0058a06c",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:f50:8"
              ]
            ]
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
      "0058a080",
      "PARAM",
      [
        "storage",
        "00ca3a00",
        null,
        null
      ]
    ],
    [
      "0058a0a0",
      "READ",
      [
        "storage",
        "00ca5f50",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a0b8",
      "READ",
      [
        "storage",
        "00ca5f90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058a080",
      "PARAM",
      [
        "storage",
        "00ca3e00",
        null,
        null
      ]
    ],
    [
      "0058a0a0",
      "READ",
      [
        "storage",
        "00ca6350",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a0b8",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a02c.md#insn-0058a044) · [`0058a06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a02c.md#insn-0058a06c) · [`0058a07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a02c.md#insn-0058a07c)
- 新版 `0058a084`（命令位置の公開資料なし） · `0058a0ac`（命令位置の公開資料なし） · `0058a0bc`（命令位置の公開資料なし）

~~~diff
- 0058a044 ["INT_ADD", "register:40f0:8", ["const:58a044:8", "const:4:8"]]
- 0058a044 ["CALL", null, ["callee:00c5a2f0:8"]]
+ 0058a084 ["INT_ADD", "register:40f0:8", ["const:58a084:8", "const:4:8"]]
+ 0058a084 ["CALL", null, ["callee:00c5a2f0:8"]]
- 0058a044 bytes ab3f1b94
+ 0058a084 bytes 9b401b94
- 0058a06c ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a06c ["INT_ADD", "register:40f0:8", ["const:58a06c:8", "const:4:8"]]
- 0058a06c ["CALLIND", null, ["register:0:8"]]
+ 0058a0ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a0ac ["INT_ADD", "register:40f0:8", ["const:58a0ac:8", "const:4:8"]]
+ 0058a0ac ["CALLIND", null, ["register:0:8"]]
- 0058a06c bytes 00013fd6
+ 0058a0ac bytes 00013fd6
- 0058a07c ["INT_ADD", "register:40f0:8", ["const:58a07c:8", "const:4:8"]]
- 0058a07c ["CALL", null, ["callee:00c58140:8"]]
+ 0058a0bc ["INT_ADD", "register:40f0:8", ["const:58a0bc:8", "const:4:8"]]
+ 0058a0bc ["CALL", null, ["callee:00c58140:8"]]
- 0058a07c bytes 31371b94
+ 0058a0bc bytes 21381b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f27208ec8bde3772cf38d905bed4a2e1"></a>

### [`0058a09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a09c.md) → [`0058a0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a0dc.md) FUN_0058a0dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c59ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ef0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c5a2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2f0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0058a0f0",
      "incomplete_value": false,
      "site": "0058a0f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a0b0",
      "incomplete_value": false,
      "site": "0058a0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0058a11c",
      "incomplete_value": true,
      "site": "0058a11c",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a0dc",
      "incomplete_value": true,
      "site": "0058a0dc",
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
                "const:20:8"
              ]
            ]
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
      "definition_site": "0058a110",
      "incomplete_value": true,
      "site": "0058a11c",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:350:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a0d0",
      "incomplete_value": true,
      "site": "0058a0dc",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:f50:8"
              ]
            ]
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
      "0058a0f0",
      "PARAM",
      [
        "storage",
        "00ca3a00",
        null,
        null
      ]
    ],
    [
      "0058a110",
      "READ",
      [
        "storage",
        "00ca5f50",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a128",
      "READ",
      [
        "storage",
        "00ca5f90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058a0f0",
      "PARAM",
      [
        "storage",
        "00ca3e00",
        null,
        null
      ]
    ],
    [
      "0058a110",
      "READ",
      [
        "storage",
        "00ca6350",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a128",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a09c.md#insn-0058a0b4) · [`0058a0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a09c.md#insn-0058a0dc) · [`0058a0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a09c.md#insn-0058a0ec)
- 新版 `0058a0f4`（命令位置の公開資料なし） · `0058a11c`（命令位置の公開資料なし） · `0058a12c`（命令位置の公開資料なし）

~~~diff
- 0058a0b4 ["INT_ADD", "register:40f0:8", ["const:58a0b4:8", "const:4:8"]]
- 0058a0b4 ["CALL", null, ["callee:00c5a2f0:8"]]
+ 0058a0f4 ["INT_ADD", "register:40f0:8", ["const:58a0f4:8", "const:4:8"]]
+ 0058a0f4 ["CALL", null, ["callee:00c5a2f0:8"]]
- 0058a0b4 bytes 8f3f1b94
+ 0058a0f4 bytes 7f401b94
- 0058a0dc ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a0dc ["INT_ADD", "register:40f0:8", ["const:58a0dc:8", "const:4:8"]]
- 0058a0dc ["CALLIND", null, ["register:0:8"]]
+ 0058a11c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a11c ["INT_ADD", "register:40f0:8", ["const:58a11c:8", "const:4:8"]]
+ 0058a11c ["CALLIND", null, ["register:0:8"]]
- 0058a0dc bytes 00013fd6
+ 0058a11c bytes 00013fd6
- 0058a0ec ["INT_ADD", "register:40f0:8", ["const:58a0ec:8", "const:4:8"]]
- 0058a0ec ["CALL", null, ["callee:00c58140:8"]]
+ 0058a12c ["INT_ADD", "register:40f0:8", ["const:58a12c:8", "const:4:8"]]
+ 0058a12c ["CALL", null, ["callee:00c58140:8"]]
- 0058a0ec bytes 15371b94
+ 0058a12c bytes 05381b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-864b1cdfaa2d6f02607e8ab0d52c2def"></a>

### [`0058a10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a10c.md) → [`0058a14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a14c.md) FUN_0058a14c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c59ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ef0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c5a2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2f0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.55% / 新版 89.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0058a194",
      "incomplete_value": true,
      "site": "0058a194",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a154",
      "incomplete_value": true,
      "site": "0058a154",
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
                "const:20:8"
              ]
            ]
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
      "definition_site": "0058a184",
      "incomplete_value": true,
      "site": "0058a194",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:350:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a144",
      "incomplete_value": true,
      "site": "0058a154",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:f50:8"
              ]
            ]
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
      "definition_site": "0058a1a0",
      "incomplete_value": true,
      "site": "0058a1a4",
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
      "definition_site": "0058a160",
      "incomplete_value": true,
      "site": "0058a164",
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
      "0058a164",
      "PARAM",
      [
        "storage",
        "00ca3a00",
        null,
        null
      ]
    ],
    [
      "0058a184",
      "READ",
      [
        "storage",
        "00ca5f50",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a1a0",
      "READ",
      [
        "storage",
        "00ca5f90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058a164",
      "PARAM",
      [
        "storage",
        "00ca3e00",
        null,
        null
      ]
    ],
    [
      "0058a184",
      "READ",
      [
        "storage",
        "00ca6350",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a1a0",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a10c.md#insn-0058a124) · [`0058a154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a10c.md#insn-0058a154) · [`0058a164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a10c.md#insn-0058a164)
- 新版 `0058a164`（命令位置の公開資料なし） · `0058a194`（命令位置の公開資料なし） · `0058a1a4`（命令位置の公開資料なし）

~~~diff
- 0058a124 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0058a124 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0058a124 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0058a124 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0058a164 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 0058a164 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0058a164 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0058a164 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0058a124 bytes 00002891
+ 0058a164 bytes 00003891
- 0058a154 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a154 ["INT_ADD", "register:40f0:8", ["const:58a154:8", "const:4:8"]]
- 0058a154 ["CALLIND", null, ["register:0:8"]]
+ 0058a194 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a194 ["INT_ADD", "register:40f0:8", ["const:58a194:8", "const:4:8"]]
+ 0058a194 ["CALLIND", null, ["register:0:8"]]
- 0058a154 bytes 00013fd6
+ 0058a194 bytes 00013fd6
- 0058a164 ["INT_ADD", "register:40f0:8", ["const:58a164:8", "const:4:8"]]
- 0058a164 ["CALL", null, ["callee:00c58140:8"]]
+ 0058a1a4 ["INT_ADD", "register:40f0:8", ["const:58a1a4:8", "const:4:8"]]
+ 0058a1a4 ["CALL", null, ["callee:00c58140:8"]]
- 0058a164 bytes f7361b94
+ 0058a1a4 bytes e7371b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-223e4aa2a5effd7698e9aac07be989e6"></a>

### [`0058a220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a220.md) → [`0058a260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a260.md) FUN_0058a260

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0058386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058386c.md) [`0058416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md) · 呼出先 1件 [`00589150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589150.md)
- 新版 呼出元 2件 [`005838ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838ac.md) [`005841ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md) · 呼出先 1件 [`00589190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a2a0",
      "incomplete_value": false,
      "site": "0058a2a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a260",
      "incomplete_value": false,
      "site": "0058a264",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "definition_site": "0058a27c",
      "incomplete_value": false,
      "site": "0058a288",
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
            "const:7e6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a23c",
      "incomplete_value": false,
      "site": "0058a248",
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
            "const:70a:8"
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
      "0058a27c",
      "PARAM",
      [
        "storage",
        "002a670a",
        null,
        "string"
      ]
    ],
    [
      "0058a2a4",
      "DATA",
      [
        "storage",
        "00c6c960",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a27c",
      "PARAM",
      [
        "storage",
        "002a67e6",
        null,
        "string"
      ]
    ],
    [
      "0058a2a4",
      "DATA",
      [
        "storage",
        "00c6cd60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a220.md#insn-0058a248) · [`0058a23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a220.md#insn-0058a23c) · [`0058a258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a220.md#insn-0058a258)
- 新版 `0058a288`（命令位置の公開資料なし） · `0058a27c`（命令位置の公開資料なし） · `0058a298`（命令位置の公開資料なし）

~~~diff
- 0058a248 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a248 ["INT_ADD", "register:40f0:8", ["const:58a248:8", "const:4:8"]]
- 0058a248 ["CALLIND", null, ["register:0:8"]]
+ 0058a288 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a288 ["INT_ADD", "register:40f0:8", ["const:58a288:8", "const:4:8"]]
+ 0058a288 ["CALLIND", null, ["register:0:8"]]
- 0058a248 bytes 00013fd6
+ 0058a288 bytes 00013fd6
- 0058a23c ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0058a23c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0058a23c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0058a23c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0058a27c ["COPY", "tmp:0:8", ["const:7e6:8"]]
+ 0058a27c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0058a27c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0058a27c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0058a23c bytes 21281c91
+ 0058a27c bytes 21981f91
- 0058a258 ["INT_ADD", "register:40f0:8", ["const:58a258:8", "const:4:8"]]
- 0058a258 ["CALL", null, ["callee:00589190:8"]]
+ 0058a298 ["INT_ADD", "register:40f0:8", ["const:58a298:8", "const:4:8"]]
+ 0058a298 ["CALL", null, ["callee:00589190:8"]]
- 0058a258 bytes befbff97
+ 0058a298 bytes befbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-301d7b255779849799b56ee2380583d4"></a>

### [`0058a274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a274.md) → [`0058a2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a2b4.md) FUN_0058a2b4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0058386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058386c.md) [`0058416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md) · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`0058a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`005838ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838ac.md) [`005841ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md) · 呼出先 7件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`0058a94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.71% / 新版 89.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a31c",
      "incomplete_value": true,
      "site": "0058a324",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ba0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a2dc",
      "incomplete_value": true,
      "site": "0058a2e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b60:8"
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
      "definition_site": "0058a318",
      "incomplete_value": true,
      "site": "0058a328",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:ae0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a2d8",
      "incomplete_value": true,
      "site": "0058a2e8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:aa0:8"
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
      "definition_site": "0058a318",
      "incomplete_value": true,
      "site": "0058a328",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0058a2d8",
      "incomplete_value": true,
      "site": "0058a2e8",
      "value": [
        "LOAD",
        "16",
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
      "0058a318",
      "READ",
      [
        "storage",
        "002bdaa0",
        null,
        "string"
      ]
    ],
    [
      "0058a318",
      "READ",
      [
        "storage",
        "002bdab0",
        null,
        "string"
      ]
    ],
    [
      "0058a31c",
      "READ",
      [
        "storage",
        "002c2b60",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058a318",
      "READ",
      [
        "storage",
        "002bdae0",
        null,
        "string"
      ]
    ],
    [
      "0058a318",
      "READ",
      [
        "storage",
        "002bdaf0",
        null,
        "string"
      ]
    ],
    [
      "0058a31c",
      "READ",
      [
        "storage",
        "002c2ba0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a274.md#insn-0058a324) · [`0058a2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a274.md#insn-0058a2c8) · [`0058a2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a274.md#insn-0058a2d0)
- 新版 `0058a364`（命令位置の公開資料なし） · `0058a308`（命令位置の公開資料なし） · `0058a310`（命令位置の公開資料なし）

~~~diff
- 0058a324 ["INT_ADD", "register:40f0:8", ["const:58a324:8", "const:4:8"]]
- 0058a324 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058a364 ["INT_ADD", "register:40f0:8", ["const:58a364:8", "const:4:8"]]
+ 0058a364 ["CALL", null, ["callee:00c57eb0:8"]]
- 0058a324 bytes e3351b94
+ 0058a364 bytes d3361b94
- 0058a2c8 ["INT_ADD", "register:40f0:8", ["const:58a2c8:8", "const:4:8"]]
- 0058a2c8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0058a308 ["INT_ADD", "register:40f0:8", ["const:58a308:8", "const:4:8"]]
+ 0058a308 ["CALL", null, ["callee:00c57e90:8"]]
- 0058a2c8 bytes f2351b94
+ 0058a308 bytes e2361b94
- 0058a2d0 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 0058a2d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058a2d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058a2d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058a310 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 0058a310 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a310 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a310 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058a2d0 bytes 08812a91
+ 0058a310 bytes 08812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9889307c7f0bb534971e2278eb14e7b4"></a>

### [`0058a504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a504.md) → [`0058a544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a544.md) FUN_0058a544

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00572420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572420.md) [`00578e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578e7c.md) [`0057b124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b124.md) [`0058386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058386c.md) [`0058416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md) · 呼出先 1件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md)
- 新版 呼出元 5件 [`00572460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572460.md) [`00578ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578ebc.md) [`0057b164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b164.md) [`005838ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838ac.md) [`005841ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md) · 呼出先 1件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a5bc",
      "incomplete_value": false,
      "site": "0058a5bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a57c",
      "incomplete_value": false,
      "site": "0058a57c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "definition_site": "0058a5f4",
      "incomplete_value": false,
      "site": "0058a5f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a5b4",
      "incomplete_value": false,
      "site": "0058a5b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:980:8"
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
      "definition_site": "0058a564",
      "incomplete_value": true,
      "site": "0058a574",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a524",
      "incomplete_value": true,
      "site": "0058a534",
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
      "0058a564",
      "PARAM",
      [
        "storage",
        "002aea60",
        null,
        "string"
      ]
    ],
    [
      "0058a584",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "0058a5bc",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a564",
      "PARAM",
      [
        "storage",
        "002aeaa0",
        null,
        "string"
      ]
    ],
    [
      "0058a584",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "0058a5bc",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a504.md#insn-0058a534) · [`0058a550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a504.md#insn-0058a550) · [`0058a574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a504.md#insn-0058a574)
- 新版 `0058a574`（命令位置の公開資料なし） · `0058a590`（命令位置の公開資料なし） · `0058a5b4`（命令位置の公開資料なし）

~~~diff
- 0058a534 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a534 ["INT_ADD", "register:40f0:8", ["const:58a534:8", "const:4:8"]]
- 0058a534 ["CALLIND", null, ["register:0:8"]]
+ 0058a574 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a574 ["INT_ADD", "register:40f0:8", ["const:58a574:8", "const:4:8"]]
+ 0058a574 ["CALLIND", null, ["register:0:8"]]
- 0058a534 bytes 00013fd6
+ 0058a574 bytes 00013fd6
- 0058a550 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a550 ["INT_ADD", "register:40f0:8", ["const:58a550:8", "const:4:8"]]
- 0058a550 ["CALLIND", null, ["register:0:8"]]
+ 0058a590 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a590 ["INT_ADD", "register:40f0:8", ["const:58a590:8", "const:4:8"]]
+ 0058a590 ["CALLIND", null, ["register:0:8"]]
- 0058a550 bytes 00013fd6
+ 0058a590 bytes 00013fd6
- 0058a574 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 0058a574 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058a574 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058a574 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058a5b4 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 0058a5b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a5b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a5b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058a574 bytes 08a12391
+ 0058a5b4 bytes 08a13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c50083de80970e9a6ef7ecdf92ee6bd"></a>

### [`0058a5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a5e4.md) → [`0058a624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a624.md) FUN_0058a624

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00572c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572c28.md) [`00573e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00573/00573e40.md) [`005740a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005740a0.md) · 呼出先 1件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md)
- 新版 呼出元 3件 [`00572c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md) [`00573e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573e80.md) [`005740e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005740e0.md) · 呼出先 1件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a64c",
      "incomplete_value": true,
      "site": "0058a64c",
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
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a60c",
      "incomplete_value": true,
      "site": "0058a60c",
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
            "const:8e8:8"
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
      "definition_site": "0058a674",
      "incomplete_value": false,
      "site": "0058a678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a634",
      "incomplete_value": false,
      "site": "0058a638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:980:8"
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
      "0058a64c",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ],
    [
      "0058a678",
      "DATA",
      [
        "storage",
        "00c6c980",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058a64c",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ],
    [
      "0058a678",
      "DATA",
      [
        "storage",
        "00c6cd80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a5e4.md#insn-0058a600) · [`0058a604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a5e4.md#insn-0058a604) · [`0058a608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a5e4.md#insn-0058a608)
- 新版 `0058a640`（命令位置の公開資料なし）

~~~diff
- 0058a600 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 0058a600 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058a600 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058a600 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058a640 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 0058a640 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058a640 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058a640 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058a600 bytes 29a12391
+ 0058a640 bytes 29a13391
- 0058a604 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 0058a604 bytes f50300aa
- 0058a608 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 0058a608 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-126ef8f46a1a4dedc1a90f49c158acc9"></a>

### [`0058a7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a7b0.md) → [`0058a7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a7f0.md) JNI_OnLoad

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005890cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005890cc.md) [`00c59f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058910c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058910c.md) [`00c5a300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a300.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 84.62% / 新版 84.62%

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
      "definition_site": "0058a804",
      "incomplete_value": false,
      "site": "0058a804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a7c4",
      "incomplete_value": false,
      "site": "0058a7c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0058a80c",
      "incomplete_value": false,
      "site": "0058a810",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a7cc",
      "incomplete_value": false,
      "site": "0058a7d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:f90:8"
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
      "definition_site": "0058a800",
      "incomplete_value": false,
      "site": "0058a810",
      "value": [
        "leaf",
        "const:58910c:8"
      ]
    },
    "old": {
      "definition_site": "0058a7c0",
      "incomplete_value": false,
      "site": "0058a7d0",
      "value": [
        "leaf",
        "const:5890cc:8"
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
      "0058a800",
      "PARAM",
      [
        "storage",
        "005890cc",
        null,
        null
      ]
    ],
    [
      "0058a804",
      "WRITE",
      [
        "storage",
        "00ca5f50",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a80c",
      "PARAM",
      [
        "storage",
        "00ca5f90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058a800",
      "PARAM",
      [
        "storage",
        "0058910c",
        null,
        null
      ]
    ],
    [
      "0058a804",
      "WRITE",
      [
        "storage",
        "00ca6350",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a80c",
      "PARAM",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a7b0.md#insn-0058a7c4) · [`0058a7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a7b0.md#insn-0058a7d0) · [`0058a7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a7b0.md#insn-0058a7b8)
- 新版 `0058a804`（命令位置の公開資料なし） · `0058a810`（命令位置の公開資料なし） · `0058a7f8`（命令位置の公開資料なし）

~~~diff
- 0058a7c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
- 0058a7c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 0058a804 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:350:8"]]
+ 0058a804 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 0058a7c4 bytes 00a907f9
+ 0058a804 bytes 00a901f9
- 0058a7d0 ["INT_ADD", "register:40f0:8", ["const:58a7d0:8", "const:4:8"]]
- 0058a7d0 ["CALL", null, ["callee:00c5a300:8"]]
+ 0058a810 ["INT_ADD", "register:40f0:8", ["const:58a810:8", "const:4:8"]]
+ 0058a810 ["CALL", null, ["callee:00c5a300:8"]]
- 0058a7d0 bytes cc3d1b94
+ 0058a810 bytes bc3e1b94
- 0058a7b8 ["COPY", "register:4040:8", ["const:ca5000:8"]]
+ 0058a7f8 ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 0058a7b8 bytes c83800f0
+ 0058a7f8 bytes e8380090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8044aa6a27ead156774bcb75d639f34a"></a>

### [`0058a7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a7e4.md) → [`0058a824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a824.md) FUN_0058a824

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md) [`0058a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md) [`0058a94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a838",
      "incomplete_value": false,
      "site": "0058a83c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a7f8",
      "incomplete_value": false,
      "site": "0058a7fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "0058a83c",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a83c",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a7e4.md#insn-0058a7f8) · [`0058a80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a7e4.md#insn-0058a80c) · [`0058a818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a7e4.md#insn-0058a818)
- 新版 `0058a838`（命令位置の公開資料なし） · `0058a84c`（命令位置の公開資料なし） · `0058a858`（命令位置の公開資料なし）

~~~diff
- 0058a7f8 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 0058a7f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058a7f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058a7f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058a838 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 0058a838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058a7f8 bytes 08a12391
+ 0058a838 bytes 08a13391
- 0058a80c ["INT_ADD", "register:40f0:8", ["const:58a80c:8", "const:4:8"]]
- 0058a80c ["CALL", null, ["callee:00588ecc:8"]]
+ 0058a84c ["INT_ADD", "register:40f0:8", ["const:58a84c:8", "const:4:8"]]
+ 0058a84c ["CALL", null, ["callee:00588ecc:8"]]
- 0058a80c bytes a0f9ff97
+ 0058a84c bytes a0f9ff97
- 0058a818 ["INT_ADD", "register:40f0:8", ["const:58a818:8", "const:4:8"]]
- 0058a818 ["CALL", null, ["callee:0058a94c:8"]]
+ 0058a858 ["INT_ADD", "register:40f0:8", ["const:58a858:8", "const:4:8"]]
+ 0058a858 ["CALL", null, ["callee:0058a94c:8"]]
- 0058a818 bytes 3d000094
+ 0058a858 bytes 3d000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bdb8cf92fbddaa9cbfb5c49cb75a536"></a>

### [`0058a830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a830.md) → [`0058a870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a870.md) FUN_0058a870

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md) [`0058a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md) [`0058a94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a884",
      "incomplete_value": false,
      "site": "0058a888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a844",
      "incomplete_value": false,
      "site": "0058a848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "0058a888",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a888",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a830.md#insn-0058a844) · [`0058a858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a830.md#insn-0058a858) · [`0058a864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a830.md#insn-0058a864)
- 新版 `0058a884`（命令位置の公開資料なし） · `0058a898`（命令位置の公開資料なし） · `0058a8a4`（命令位置の公開資料なし）

~~~diff
- 0058a844 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 0058a844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058a844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058a844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058a884 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 0058a884 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a884 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a884 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058a844 bytes 08a12391
+ 0058a884 bytes 08a13391
- 0058a858 ["INT_ADD", "register:40f0:8", ["const:58a858:8", "const:4:8"]]
- 0058a858 ["CALL", null, ["callee:00588ecc:8"]]
+ 0058a898 ["INT_ADD", "register:40f0:8", ["const:58a898:8", "const:4:8"]]
+ 0058a898 ["CALL", null, ["callee:00588ecc:8"]]
- 0058a858 bytes 8df9ff97
+ 0058a898 bytes 8df9ff97
- 0058a864 ["INT_ADD", "register:40f0:8", ["const:58a864:8", "const:4:8"]]
- 0058a864 ["CALL", null, ["callee:0058a94c:8"]]
+ 0058a8a4 ["INT_ADD", "register:40f0:8", ["const:58a8a4:8", "const:4:8"]]
+ 0058a8a4 ["CALL", null, ["callee:0058a94c:8"]]
- 0058a864 bytes 2a000094
+ 0058a8a4 bytes 2a000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a381377a76263cc5d3fab16526d95b3"></a>

### [`0058a87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a87c.md) → [`0058a8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a8bc.md) FUN_0058a8bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 65件 [`0049b17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md) [`00571ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571ab4.md) [`00571dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571dd8.md) [`005720b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/005720b8.md) [`0057226c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/0057226c.md) · 呼出先 2件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md) [`0058a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md)
- 新版 呼出元 65件 [`0049b1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b1bc.md) [`00571af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571af4.md) [`00571e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571e18.md) [`005720f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005720f8.md) [`005722ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005722ac.md) · 呼出先 2件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md) [`0058a94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md)

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
      "definition_site": "0058a8d0",
      "incomplete_value": false,
      "site": "0058a8d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a890",
      "incomplete_value": false,
      "site": "0058a894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "0058a8d4",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a8d4",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a87c.md#insn-0058a890) · [`0058a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a87c.md#insn-0058a8a4)
- 新版 `0058a8d0`（命令位置の公開資料なし） · `0058a8e4`（命令位置の公開資料なし）

~~~diff
- 0058a890 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 0058a890 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058a890 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058a890 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058a8d0 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 0058a8d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a8d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a8d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058a890 bytes 08a12391
+ 0058a8d0 bytes 08a13391
- 0058a8a4 ["INT_ADD", "register:40f0:8", ["const:58a8a4:8", "const:4:8"]]
- 0058a8a4 ["CALL", null, ["callee:00588ecc:8"]]
+ 0058a8e4 ["INT_ADD", "register:40f0:8", ["const:58a8e4:8", "const:4:8"]]
+ 0058a8e4 ["CALL", null, ["callee:00588ecc:8"]]
- 0058a8a4 bytes 7af9ff97
+ 0058a8e4 bytes 7af9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8fc654150df0a3317a297dd888867ef"></a>

### [`0058a8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a8c0.md) → [`0058a900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a900.md) FUN_0058a900

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md) [`0058a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md) [`0058a94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a914",
      "incomplete_value": false,
      "site": "0058a918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a8d4",
      "incomplete_value": false,
      "site": "0058a8d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "0058a918",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a918",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a8c0.md#insn-0058a8d4) · [`0058a8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a8c0.md#insn-0058a8e8) · [`0058a8f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a8c0.md#insn-0058a8f4)
- 新版 `0058a914`（命令位置の公開資料なし） · `0058a928`（命令位置の公開資料なし） · `0058a934`（命令位置の公開資料なし）

~~~diff
- 0058a8d4 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 0058a8d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058a8d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058a8d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058a914 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 0058a914 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a914 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a914 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058a8d4 bytes 08a12391
+ 0058a914 bytes 08a13391
- 0058a8e8 ["INT_ADD", "register:40f0:8", ["const:58a8e8:8", "const:4:8"]]
- 0058a8e8 ["CALL", null, ["callee:00588ecc:8"]]
+ 0058a928 ["INT_ADD", "register:40f0:8", ["const:58a928:8", "const:4:8"]]
+ 0058a928 ["CALL", null, ["callee:00588ecc:8"]]
- 0058a8e8 bytes 69f9ff97
+ 0058a928 bytes 69f9ff97
- 0058a8f4 ["INT_ADD", "register:40f0:8", ["const:58a8f4:8", "const:4:8"]]
- 0058a8f4 ["CALL", null, ["callee:0058a94c:8"]]
+ 0058a934 ["INT_ADD", "register:40f0:8", ["const:58a934:8", "const:4:8"]]
+ 0058a934 ["CALL", null, ["callee:0058a94c:8"]]
- 0058a8f4 bytes 06000094
+ 0058a934 bytes 06000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef9ae2570eff315ea39bf90002316d75"></a>

### [`0058aba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aba4.md) → [`0058abe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058abe4.md) _INIT_33

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0058a87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a87c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058a8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a8bc.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 43.75% / 新版 43.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058abfc",
      "incomplete_value": false,
      "site": "0058abfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058abbc",
      "incomplete_value": false,
      "site": "0058abbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:f58:8"
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
      "definition_site": "0058abfc",
      "incomplete_value": false,
      "site": "0058abfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058abbc",
      "incomplete_value": false,
      "site": "0058abbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "definition_site": "0058abfc",
      "incomplete_value": false,
      "site": "0058abfc",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:358:8"
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
      "definition_site": "0058abbc",
      "incomplete_value": false,
      "site": "0058abbc",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:f58:8"
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
      "0058abe8",
      "PARAM",
      [
        "storage",
        "00ca5f58",
        null,
        "undefined8"
      ]
    ],
    [
      "0058abf8",
      "PARAM",
      [
        "storage",
        "0058a87c",
        null,
        null
      ]
    ],
    [
      "0058abfc",
      "WRITE",
      [
        "storage",
        "00ca5f58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058abe8",
      "PARAM",
      [
        "storage",
        "00ca6358",
        null,
        "undefined8"
      ]
    ],
    [
      "0058abf8",
      "PARAM",
      [
        "storage",
        "0058a8bc",
        null,
        null
      ]
    ],
    [
      "0058abfc",
      "WRITE",
      [
        "storage",
        "00ca6358",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058aba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aba4.md#insn-0058aba4) · [`0058aba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aba4.md#insn-0058aba8) · [`0058abb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aba4.md#insn-0058abb0)
- 新版 `0058abe4`（命令位置の公開資料なし） · `0058abe8`（命令位置の公開資料なし） · `0058abf0`（命令位置の公開資料なし）

~~~diff
- 0058aba4 ["COPY", "register:4008:8", ["const:ca5000:8"]]
+ 0058abe4 ["COPY", "register:4008:8", ["const:ca6000:8"]]
- 0058aba4 bytes c13800f0
+ 0058abe4 bytes e1380090
- 0058aba8 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 0058aba8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0058aba8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0058aba8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0058abe8 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 0058abe8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0058abe8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0058abe8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0058aba8 bytes 21603d91
+ 0058abe8 bytes 21600d91
- 0058abb0 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 0058abb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058abb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058abb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058abf0 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 0058abf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058abf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058abf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058abb0 bytes 08a12391
+ 0058abf0 bytes 08a13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dd990311a5aae0d4c6a116303405608"></a>

### [`0058abe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058abe4.md) → [`0058ac24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ac24.md) FUN_0058ac24

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 5件 [`0057ce78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057ce78.md) [`0057d454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d454.md) [`0057ddd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057ddd0.md) [`00580af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580af0.md) [`005885b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005885b8.md) · 呼出先 3件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 5件 [`0057ceb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057ceb8.md) [`0057d494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d494.md) [`0057de10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057de10.md) [`00580b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580b30.md) [`005885f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005885f8.md) · 呼出先 3件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058ac4c",
      "incomplete_value": false,
      "site": "0058ac50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ac0c",
      "incomplete_value": false,
      "site": "0058ac10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
      "0058ac50",
      "DATA",
      [
        "storage",
        "00c6ca10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058ac50",
      "DATA",
      [
        "storage",
        "00c6ce10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ac0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058abe4.md#insn-0058ac0c) · [`0058ac24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058abe4.md#insn-0058ac24) · [`0058ac3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058abe4.md#insn-0058ac3c)
- 新版 `0058ac4c`（命令位置の公開資料なし） · `0058ac64`（命令位置の公開資料なし） · `0058ac7c`（命令位置の公開資料なし）

~~~diff
- 0058ac0c ["COPY", "tmp:0:8", ["const:a10:8"]]
- 0058ac0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058ac0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058ac0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058ac4c ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 0058ac4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ac4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ac4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058ac0c bytes 08412891
+ 0058ac4c bytes 08413891
- 0058ac24 ["INT_ADD", "register:40f0:8", ["const:58ac24:8", "const:4:8"]]
- 0058ac24 ["CALL", null, ["callee:00c57e90:8"]]
+ 0058ac64 ["INT_ADD", "register:40f0:8", ["const:58ac64:8", "const:4:8"]]
+ 0058ac64 ["CALL", null, ["callee:00c57e90:8"]]
- 0058ac24 bytes 9b331b94
+ 0058ac64 bytes 8b341b94
- 0058ac3c ["INT_ADD", "register:40f0:8", ["const:58ac3c:8", "const:4:8"]]
- 0058ac3c ["CALL", null, ["callee:00c58000:8"]]
+ 0058ac7c ["INT_ADD", "register:40f0:8", ["const:58ac7c:8", "const:4:8"]]
+ 0058ac7c ["CALL", null, ["callee:00c58000:8"]]
- 0058ac3c bytes f1331b94
+ 0058ac7c bytes e1341b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50101ec1199c2ac00e8179935500a3bd"></a>

### [`0058b50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b50c.md) → [`0058b54c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b54c.md) FUN_0058b54c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0058b558",
      "incomplete_value": false,
      "site": "0058b55c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b518",
      "incomplete_value": false,
      "site": "0058b51c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
      "0058b55c",
      "DATA",
      [
        "storage",
        "00c6ca10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b55c",
      "DATA",
      [
        "storage",
        "00c6ce10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b50c.md#insn-0058b518)
- 新版 `0058b558`（命令位置の公開資料なし）

~~~diff
- 0058b518 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 0058b518 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058b518 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058b518 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058b558 ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 0058b558 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b558 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b558 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058b518 bytes 29412891
+ 0058b558 bytes 29413891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ec19c89eba7a65953b20352be3fe69c"></a>

### [`0058b530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b530.md) → [`0058b570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b570.md) FUN_0058b570

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
      "definition_site": "0058b578",
      "incomplete_value": false,
      "site": "0058b57c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b538",
      "incomplete_value": false,
      "site": "0058b53c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
      "0058b57c",
      "DATA",
      [
        "storage",
        "00c6ca10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b57c",
      "DATA",
      [
        "storage",
        "00c6ce10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b530.md#insn-0058b538) · [`0058b55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b530.md#insn-0058b55c)
- 新版 `0058b578`（命令位置の公開資料なし） · `0058b59c`（命令位置の公開資料なし）

~~~diff
- 0058b538 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 0058b538 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058b538 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058b538 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058b578 ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 0058b578 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b578 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b578 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058b538 bytes 29412891
+ 0058b578 bytes 29413891
- 0058b55c ["INT_ADD", "register:40f0:8", ["const:58b55c:8", "const:4:8"]]
- 0058b55c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058b59c ["INT_ADD", "register:40f0:8", ["const:58b59c:8", "const:4:8"]]
+ 0058b59c ["CALL", null, ["callee:00c57eb0:8"]]
- 0058b55c bytes 55311b94
+ 0058b59c bytes 45321b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95ab900ceeb6c54305568b35ff9d89dc"></a>

### [`0058b570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b570.md) → [`0058b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b5b0.md) FUN_0058b5b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0058b5bc",
      "incomplete_value": false,
      "site": "0058b5c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b57c",
      "incomplete_value": false,
      "site": "0058b580",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
      "0058b5c0",
      "DATA",
      [
        "storage",
        "00c6ca48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b5c0",
      "DATA",
      [
        "storage",
        "00c6ce48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b570.md#insn-0058b57c)
- 新版 `0058b5bc`（命令位置の公開資料なし）

~~~diff
- 0058b57c ["COPY", "tmp:0:8", ["const:a48:8"]]
- 0058b57c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058b57c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058b57c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058b5bc ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 0058b5bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b5bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b5bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058b57c bytes 29212991
+ 0058b5bc bytes 29213991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-106266508d3dcfaa544317bb337c90e0"></a>

### [`0058b594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b594.md) → [`0058b5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b5d4.md) FUN_0058b5d4

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
      "definition_site": "0058b5dc",
      "incomplete_value": false,
      "site": "0058b5e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b59c",
      "incomplete_value": false,
      "site": "0058b5a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
      "0058b5e0",
      "DATA",
      [
        "storage",
        "00c6ca48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b5e0",
      "DATA",
      [
        "storage",
        "00c6ce48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b594.md#insn-0058b59c) · [`0058b5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b594.md#insn-0058b5c0)
- 新版 `0058b5dc`（命令位置の公開資料なし） · `0058b600`（命令位置の公開資料なし）

~~~diff
- 0058b59c ["COPY", "tmp:0:8", ["const:a48:8"]]
- 0058b59c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058b59c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058b59c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058b5dc ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 0058b5dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b5dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b5dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058b59c bytes 29212991
+ 0058b5dc bytes 29213991
- 0058b5c0 ["INT_ADD", "register:40f0:8", ["const:58b5c0:8", "const:4:8"]]
- 0058b5c0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058b600 ["INT_ADD", "register:40f0:8", ["const:58b600:8", "const:4:8"]]
+ 0058b600 ["CALL", null, ["callee:00c57eb0:8"]]
- 0058b5c0 bytes 3c311b94
+ 0058b600 bytes 2c321b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-257fbab00d2f62a056bb30b30eac913c"></a>

### [`0058b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b5d4.md) → [`0058b614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b614.md) FUN_0058b614

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0058ad2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ad2c.md) [`0058ad88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ad88.md) [`0058aefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aefc.md) · 呼出先 3件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 3件 [`0058ad6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ad6c.md) [`0058adc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058adc8.md) [`0058af3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058af3c.md) · 呼出先 3件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058b63c",
      "incomplete_value": false,
      "site": "0058b644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b5fc",
      "incomplete_value": false,
      "site": "0058b604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:e60:8"
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
      "definition_site": "0058b650",
      "incomplete_value": false,
      "site": "0058b650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b610",
      "incomplete_value": false,
      "site": "0058b610",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
      "0058b644",
      "DATA",
      [
        "storage",
        "00c6be60",
        null,
        "pointer"
      ]
    ],
    [
      "0058b650",
      "DATA",
      [
        "storage",
        "00c6ca10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b644",
      "DATA",
      [
        "storage",
        "00c6c260",
        null,
        "pointer"
      ]
    ],
    [
      "0058b650",
      "DATA",
      [
        "storage",
        "00c6ce10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b5d4.md#insn-0058b5f4) · [`0058b5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b5d4.md#insn-0058b5f8) · [`0058b5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b5d4.md#insn-0058b5fc)
- 新版 `0058b634`（命令位置の公開資料なし） · `0058b638`（命令位置の公開資料なし） · `0058b63c`（命令位置の公開資料なし）

~~~diff
- 0058b5f4 ["INT_ADD", "register:40f0:8", ["const:58b5f4:8", "const:4:8"]]
- 0058b5f4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0058b634 ["INT_ADD", "register:40f0:8", ["const:58b634:8", "const:4:8"]]
+ 0058b634 ["CALL", null, ["callee:00c57e90:8"]]
- 0058b5f4 bytes 27311b94
+ 0058b634 bytes 17321b94
- 0058b5f8 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0058b638 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0058b5f8 bytes 08370090
+ 0058b638 bytes 083700b0
- 0058b5fc ["COPY", "tmp:0:8", ["const:e60:8"]]
- 0058b5fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058b5fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058b5fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058b63c ["COPY", "tmp:0:8", ["const:260:8"]]
+ 0058b63c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b63c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b63c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058b5fc bytes 08813991
+ 0058b63c bytes 08810991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-605987e2365c8b2275490fb7cf1e253c"></a>

### [`0058b7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b7b4.md) → [`0058b7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b7f4.md) FUN_0058b7f4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0058b190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b190.md) [`0058b234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b234.md) [`0058b3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b3a8.md) · 呼出先 3件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 3件 [`0058b1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b1d0.md) [`0058b274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b274.md) [`0058b3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b3e8.md) · 呼出先 3件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058b81c",
      "incomplete_value": false,
      "site": "0058b824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b7dc",
      "incomplete_value": false,
      "site": "0058b7e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "definition_site": "0058b830",
      "incomplete_value": false,
      "site": "0058b830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b7f0",
      "incomplete_value": false,
      "site": "0058b7f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
      "0058b824",
      "DATA",
      [
        "storage",
        "00c6cae8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058b830",
      "DATA",
      [
        "storage",
        "00c6ca48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b824",
      "DATA",
      [
        "storage",
        "00c6cee8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058b830",
      "DATA",
      [
        "storage",
        "00c6ce48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b7b4.md#insn-0058b7d4) · [`0058b7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b7b4.md#insn-0058b7dc) · [`0058b7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b7b4.md#insn-0058b7e0)
- 新版 `0058b814`（命令位置の公開資料なし） · `0058b81c`（命令位置の公開資料なし）

~~~diff
- 0058b7d4 ["INT_ADD", "register:40f0:8", ["const:58b7d4:8", "const:4:8"]]
- 0058b7d4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0058b814 ["INT_ADD", "register:40f0:8", ["const:58b814:8", "const:4:8"]]
+ 0058b814 ["CALL", null, ["callee:00c57e90:8"]]
- 0058b7d4 bytes af301b94
+ 0058b814 bytes 9f311b94
- 0058b7dc ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 0058b7dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058b7dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058b7dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058b81c ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 0058b81c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b81c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b81c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058b7dc bytes 08a12b91
+ 0058b81c bytes 08a13b91
- 0058b7e0 ["COPY", "register:40c0:8", ["register:4000:8"]]
- 0058b7e0 bytes f80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c324722be180a53582febfbb198404dc"></a>

### [`0058b88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b88c.md) → [`0058b8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b8cc.md) FUN_0058b8cc

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
      "definition_site": "0058b8d0",
      "incomplete_value": false,
      "site": "0058b8d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b890",
      "incomplete_value": false,
      "site": "0058b894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "0058b8d4",
      "DATA",
      [
        "storage",
        "00c6cae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b8d4",
      "DATA",
      [
        "storage",
        "00c6cee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b88c.md#insn-0058b890)
- 新版 `0058b8d0`（命令位置の公開資料なし）

~~~diff
- 0058b890 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 0058b890 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058b890 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058b890 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058b8d0 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 0058b8d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b8d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b8d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058b890 bytes 08a12b91
+ 0058b8d0 bytes 08a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc9059a04524a927e9617b2df66c8b30"></a>

### [`0058b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b89c.md) → [`0058b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b8dc.md) FUN_0058b8dc

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
      "definition_site": "0058b8ec",
      "incomplete_value": false,
      "site": "0058b8f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b8ac",
      "incomplete_value": false,
      "site": "0058b8b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "0058b8f4",
      "DATA",
      [
        "storage",
        "00c6cae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b8f4",
      "DATA",
      [
        "storage",
        "00c6cee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b89c.md#insn-0058b8ac) · [`0058b8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b89c.md#insn-0058b8b8)
- 新版 `0058b8ec`（命令位置の公開資料なし） · `0058b8f8`（命令位置の公開資料なし）

~~~diff
- 0058b8ac ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 0058b8ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058b8ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058b8ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058b8ec ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 0058b8ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b8ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b8ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058b8ac bytes 08a12b91
+ 0058b8ec bytes 08a13b91
- 0058b8b8 ["INT_ADD", "register:40f0:8", ["const:58b8b8:8", "const:4:8"]]
- 0058b8b8 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0058b8f8 ["INT_ADD", "register:40f0:8", ["const:58b8f8:8", "const:4:8"]]
+ 0058b8f8 ["CALL", null, ["callee:00c57ea0:8"]]
- 0058b8b8 bytes 7a301b94
+ 0058b8f8 bytes 6a311b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8adbb574968b430fdfa59ab7e2d9fd6d"></a>

### [`0058b904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b904.md) → [`0058b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b944.md) FUN_0058b944

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005975e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975e0.md) · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00597620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597620.md) · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058b998",
      "incomplete_value": true,
      "site": "0058b998",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:a2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b958",
      "incomplete_value": true,
      "site": "0058b958",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:62:8"
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
      "definition_site": "0058b9a0",
      "incomplete_value": true,
      "site": "0058b9a0",
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
      "definition_site": "0058b960",
      "incomplete_value": true,
      "site": "0058b960",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058b99c",
      "incomplete_value": true,
      "site": "0058b9b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fb2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b95c",
      "incomplete_value": true,
      "site": "0058b974",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee5:8"
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
      "0058b980",
      "READ",
      [
        "storage",
        "002b9062",
        null,
        "string"
      ]
    ],
    [
      "0058b988",
      "READ",
      [
        "storage",
        "002b9068",
        null,
        "string"
      ]
    ],
    [
      "0058b99c",
      "READ",
      [
        "storage",
        "002a0ee5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058b980",
      "READ",
      [
        "storage",
        "002b90a2",
        null,
        "string"
      ]
    ],
    [
      "0058b988",
      "READ",
      [
        "storage",
        "002b90a8",
        null,
        "string"
      ]
    ],
    [
      "0058b99c",
      "READ",
      [
        "storage",
        "002a0fb2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b904.md#insn-0058b9a0) · [`0058b928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b904.md#insn-0058b928) · [`0058b930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b904.md#insn-0058b930)
- 新版 `0058b9e0`（命令位置の公開資料なし） · `0058b968`（命令位置の公開資料なし） · `0058b970`（命令位置の公開資料なし）

~~~diff
- 0058b9a0 ["INT_ADD", "register:40f0:8", ["const:58b9a0:8", "const:4:8"]]
- 0058b9a0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058b9e0 ["INT_ADD", "register:40f0:8", ["const:58b9e0:8", "const:4:8"]]
+ 0058b9e0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0058b9a0 bytes 44301b94
+ 0058b9e0 bytes 34311b94
- 0058b928 ["INT_ADD", "register:40f0:8", ["const:58b928:8", "const:4:8"]]
- 0058b928 ["CALL", null, ["callee:00588e6c:8"]]
+ 0058b968 ["INT_ADD", "register:40f0:8", ["const:58b968:8", "const:4:8"]]
+ 0058b968 ["CALL", null, ["callee:00588e6c:8"]]
- 0058b928 bytes 41f5ff97
+ 0058b968 bytes 41f5ff97
- 0058b930 ["INT_ADD", "register:40f0:8", ["const:58b930:8", "const:4:8"]]
- 0058b930 ["CALL", null, ["callee:0058915c:8"]]
+ 0058b970 ["INT_ADD", "register:40f0:8", ["const:58b970:8", "const:4:8"]]
+ 0058b970 ["CALL", null, ["callee:0058915c:8"]]
- 0058b930 bytes fbf5ff97
+ 0058b970 bytes fbf5ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28f71412aa2cce86e16c6479c755732f"></a>

### [`0058ba9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058ba9c.md) → [`0058badc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058badc.md) FUN_0058badc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005975e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975e4.md) · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00597624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597624.md) · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058bb34",
      "incomplete_value": true,
      "site": "0058bb34",
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
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:e9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058baf4",
      "incomplete_value": true,
      "site": "0058baf4",
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
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:e5a:8"
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
      "definition_site": "0058bb48",
      "incomplete_value": true,
      "site": "0058bb58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fb2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058bb08",
      "incomplete_value": true,
      "site": "0058bb18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee5:8"
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
      "0058bb24",
      "READ",
      [
        "storage",
        "002bee5a",
        null,
        "string"
      ]
    ],
    [
      "0058bb48",
      "READ",
      [
        "storage",
        "002a0ee5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058bb24",
      "READ",
      [
        "storage",
        "002bee9a",
        null,
        "string"
      ]
    ],
    [
      "0058bb48",
      "READ",
      [
        "storage",
        "002a0fb2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058bac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058ba9c.md#insn-0058bac0) · [`0058bac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058ba9c.md#insn-0058bac8) · [`0058bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058ba9c.md#insn-0058bae0)
- 新版 `0058bb00`（命令位置の公開資料なし） · `0058bb08`（命令位置の公開資料なし） · `0058bb20`（命令位置の公開資料なし）

~~~diff
- 0058bac0 ["INT_ADD", "register:40f0:8", ["const:58bac0:8", "const:4:8"]]
- 0058bac0 ["CALL", null, ["callee:00588e6c:8"]]
+ 0058bb00 ["INT_ADD", "register:40f0:8", ["const:58bb00:8", "const:4:8"]]
+ 0058bb00 ["CALL", null, ["callee:00588e6c:8"]]
- 0058bac0 bytes dbf4ff97
+ 0058bb00 bytes dbf4ff97
- 0058bac8 ["INT_ADD", "register:40f0:8", ["const:58bac8:8", "const:4:8"]]
- 0058bac8 ["CALL", null, ["callee:0058915c:8"]]
+ 0058bb08 ["INT_ADD", "register:40f0:8", ["const:58bb08:8", "const:4:8"]]
+ 0058bb08 ["CALL", null, ["callee:0058915c:8"]]
- 0058bac8 bytes 95f5ff97
+ 0058bb08 bytes 95f5ff97
- 0058bae0 ["COPY", "tmp:0:8", ["const:e5a:8"]]
- 0058bae0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058bae0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058bae0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058bb20 ["COPY", "tmp:0:8", ["const:e9a:8"]]
+ 0058bb20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058bb20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058bb20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058bae0 bytes 08693991
+ 0058bb20 bytes 08693a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-779b0ed960e6cf58f48450c6f83d1d4d"></a>

### [`0058bc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058bc38.md) → [`0058bc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058bc78.md) FUN_0058bc78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005975e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975e8.md) · 呼出先 11件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00597628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597628.md) · 呼出先 11件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058bccc",
      "incomplete_value": true,
      "site": "0058bccc",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:402:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058bc8c",
      "incomplete_value": true,
      "site": "0058bc8c",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:335:8"
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
      "definition_site": "0058bce0",
      "incomplete_value": true,
      "site": "0058bce8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:c94:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058bca0",
      "incomplete_value": true,
      "site": "0058bca8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:c54:8"
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
      "definition_site": "0058bcec",
      "incomplete_value": true,
      "site": "0058bcec",
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
      "definition_site": "0058bcac",
      "incomplete_value": true,
      "site": "0058bcac",
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
      "0058bcc0",
      "READ",
      [
        "storage",
        "002a4335",
        null,
        "string"
      ]
    ],
    [
      "0058bce0",
      "READ",
      [
        "storage",
        "002b3c54",
        null,
        "string"
      ]
    ],
    [
      "0058bce4",
      "READ",
      [
        "storage",
        "002b3c61",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058bcc0",
      "READ",
      [
        "storage",
        "002a4402",
        null,
        "string"
      ]
    ],
    [
      "0058bce0",
      "READ",
      [
        "storage",
        "002b3c94",
        null,
        "string"
      ]
    ],
    [
      "0058bce4",
      "READ",
      [
        "storage",
        "002b3ca1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058bce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058bc38.md#insn-0058bce8) · [`0058bc5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058bc38.md#insn-0058bc5c) · [`0058bc64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058bc38.md#insn-0058bc64)
- 新版 `0058bd28`（命令位置の公開資料なし） · `0058bc9c`（命令位置の公開資料なし） · `0058bca4`（命令位置の公開資料なし）

~~~diff
- 0058bce8 ["INT_ADD", "register:40f0:8", ["const:58bce8:8", "const:4:8"]]
- 0058bce8 ["CALL", null, ["callee:00589144:8"]]
+ 0058bd28 ["INT_ADD", "register:40f0:8", ["const:58bd28:8", "const:4:8"]]
+ 0058bd28 ["CALL", null, ["callee:00589144:8"]]
- 0058bce8 bytes 07f5ff97
+ 0058bd28 bytes 07f5ff97
- 0058bc5c ["INT_ADD", "register:40f0:8", ["const:58bc5c:8", "const:4:8"]]
- 0058bc5c ["CALL", null, ["callee:00588e6c:8"]]
+ 0058bc9c ["INT_ADD", "register:40f0:8", ["const:58bc9c:8", "const:4:8"]]
+ 0058bc9c ["CALL", null, ["callee:00588e6c:8"]]
- 0058bc5c bytes 74f4ff97
+ 0058bc9c bytes 74f4ff97
- 0058bc64 ["INT_ADD", "register:40f0:8", ["const:58bc64:8", "const:4:8"]]
- 0058bc64 ["CALL", null, ["callee:0058915c:8"]]
+ 0058bca4 ["INT_ADD", "register:40f0:8", ["const:58bca4:8", "const:4:8"]]
+ 0058bca4 ["CALL", null, ["callee:0058915c:8"]]
- 0058bc64 bytes 2ef5ff97
+ 0058bca4 bytes 2ef5ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-538a45a5fd0970aab1a788dc6cef414d"></a>

### [`0058bdfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058bdfc.md) → [`0058be3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058be3c.md) FUN_0058be3c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005975f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975f0.md) · 呼出先 9件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00597630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597630.md) · 呼出先 9件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.36% / 新版 90.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058be84",
      "incomplete_value": true,
      "site": "0058be90",
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
      "definition_site": "0058be44",
      "incomplete_value": true,
      "site": "0058be50",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058be80",
      "incomplete_value": true,
      "site": "0058be98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:145:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058be40",
      "incomplete_value": true,
      "site": "0058be58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:78:8"
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
      "definition_site": "0058be9c",
      "incomplete_value": true,
      "site": "0058beac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058be5c",
      "incomplete_value": true,
      "site": "0058be6c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:260:8"
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
      "0058be80",
      "READ",
      [
        "storage",
        "002a2078",
        null,
        "string"
      ]
    ],
    [
      "0058be84",
      "READ",
      [
        "storage",
        "002a2088",
        null,
        "string"
      ]
    ],
    [
      "0058be9c",
      "READ",
      [
        "storage",
        "002c2260",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058be80",
      "READ",
      [
        "storage",
        "002a2145",
        null,
        "string"
      ]
    ],
    [
      "0058be84",
      "READ",
      [
        "storage",
        "002a2155",
        null,
        "string"
      ]
    ],
    [
      "0058be9c",
      "READ",
      [
        "storage",
        "002c22a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058bdfc.md#insn-0058be98) · [`0058be1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058bdfc.md#insn-0058be1c) · [`0058be24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058bdfc.md#insn-0058be24)
- 新版 `0058bed8`（命令位置の公開資料なし） · `0058be5c`（命令位置の公開資料なし） · `0058be64`（命令位置の公開資料なし）

~~~diff
- 0058be98 ["INT_ADD", "register:40f0:8", ["const:58be98:8", "const:4:8"]]
- 0058be98 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058bed8 ["INT_ADD", "register:40f0:8", ["const:58bed8:8", "const:4:8"]]
+ 0058bed8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0058be98 bytes 062f1b94
+ 0058bed8 bytes f62f1b94
- 0058be1c ["INT_ADD", "register:40f0:8", ["const:58be1c:8", "const:4:8"]]
- 0058be1c ["CALL", null, ["callee:00588e6c:8"]]
+ 0058be5c ["INT_ADD", "register:40f0:8", ["const:58be5c:8", "const:4:8"]]
+ 0058be5c ["CALL", null, ["callee:00588e6c:8"]]
- 0058be1c bytes 04f4ff97
+ 0058be5c bytes 04f4ff97
- 0058be24 ["INT_ADD", "register:40f0:8", ["const:58be24:8", "const:4:8"]]
- 0058be24 ["CALL", null, ["callee:0058915c:8"]]
+ 0058be64 ["INT_ADD", "register:40f0:8", ["const:58be64:8", "const:4:8"]]
+ 0058be64 ["CALL", null, ["callee:0058915c:8"]]
- 0058be24 bytes bef4ff97
+ 0058be64 bytes bef4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cca61331c1382727160bb7d92c2325ca"></a>

### [`0058bf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058bf84.md) → [`0058bfc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058bfc4.md) FUN_0058bfc4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005975ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975ec.md) · 呼出先 11件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`0059762c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059762c.md) · 呼出先 11件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

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
      "definition_site": "0058c02c",
      "incomplete_value": true,
      "site": "0058c034",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:c94:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058bfec",
      "incomplete_value": true,
      "site": "0058bff4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:c54:8"
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
      "definition_site": "0058c038",
      "incomplete_value": true,
      "site": "0058c038",
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
      "definition_site": "0058bff8",
      "incomplete_value": true,
      "site": "0058bff8",
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
      "0058c02c",
      "READ",
      [
        "storage",
        "002b3c54",
        null,
        "string"
      ]
    ],
    [
      "0058c030",
      "READ",
      [
        "storage",
        "002b3c61",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058c02c",
      "READ",
      [
        "storage",
        "002b3c94",
        null,
        "string"
      ]
    ],
    [
      "0058c030",
      "READ",
      [
        "storage",
        "002b3ca1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058c034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058bf84.md#insn-0058c034) · [`0058bfa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058bf84.md#insn-0058bfa8) · [`0058bfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058bf84.md#insn-0058bfb0)
- 新版 `0058c074`（命令位置の公開資料なし） · `0058bfe8`（命令位置の公開資料なし） · `0058bff0`（命令位置の公開資料なし）

~~~diff
- 0058c034 ["INT_ADD", "register:40f0:8", ["const:58c034:8", "const:4:8"]]
- 0058c034 ["CALL", null, ["callee:00589144:8"]]
+ 0058c074 ["INT_ADD", "register:40f0:8", ["const:58c074:8", "const:4:8"]]
+ 0058c074 ["CALL", null, ["callee:00589144:8"]]
- 0058c034 bytes 34f4ff97
+ 0058c074 bytes 34f4ff97
- 0058bfa8 ["INT_ADD", "register:40f0:8", ["const:58bfa8:8", "const:4:8"]]
- 0058bfa8 ["CALL", null, ["callee:00588e6c:8"]]
+ 0058bfe8 ["INT_ADD", "register:40f0:8", ["const:58bfe8:8", "const:4:8"]]
+ 0058bfe8 ["CALL", null, ["callee:00588e6c:8"]]
- 0058bfa8 bytes a1f3ff97
+ 0058bfe8 bytes a1f3ff97
- 0058bfb0 ["INT_ADD", "register:40f0:8", ["const:58bfb0:8", "const:4:8"]]
- 0058bfb0 ["CALL", null, ["callee:0058915c:8"]]
+ 0058bff0 ["INT_ADD", "register:40f0:8", ["const:58bff0:8", "const:4:8"]]
+ 0058bff0 ["CALL", null, ["callee:0058915c:8"]]
- 0058bfb0 bytes 5bf4ff97
+ 0058bff0 bytes 5bf4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ef1d1302d2e034caf21b55247eb8f06"></a>

### [`0058c148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c148.md) → [`0058c188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c188.md) FUN_0058c188

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005975f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975f4.md) · 呼出先 11件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00597634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597634.md) · 呼出先 11件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.73% / 新版 88.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058c1c4",
      "incomplete_value": true,
      "site": "0058c1dc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:d75:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c184",
      "incomplete_value": true,
      "site": "0058c19c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:d35:8"
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
      "definition_site": "0058c1e0",
      "incomplete_value": true,
      "site": "0058c1ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4e1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c1a0",
      "incomplete_value": true,
      "site": "0058c1ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4a1:8"
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
      "definition_site": "0058c1f0",
      "incomplete_value": true,
      "site": "0058c1f0",
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
      "definition_site": "0058c1b0",
      "incomplete_value": true,
      "site": "0058c1b0",
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
      "0058c1c4",
      "READ",
      [
        "storage",
        "002b0d35",
        null,
        "string"
      ]
    ],
    [
      "0058c1e0",
      "READ",
      [
        "storage",
        "002bb4a1",
        null,
        "string"
      ]
    ],
    [
      "0058c1e4",
      "READ",
      [
        "storage",
        "002bb4ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058c1c4",
      "READ",
      [
        "storage",
        "002b0d75",
        null,
        "string"
      ]
    ],
    [
      "0058c1e0",
      "READ",
      [
        "storage",
        "002bb4e1",
        null,
        "string"
      ]
    ],
    [
      "0058c1e4",
      "READ",
      [
        "storage",
        "002bb4ee",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058c16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c148.md#insn-0058c16c) · [`0058c1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c148.md#insn-0058c1f0) · [`0058c174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c148.md#insn-0058c174)
- 新版 `0058c1ac`（命令位置の公開資料なし） · `0058c230`（命令位置の公開資料なし） · `0058c1b4`（命令位置の公開資料なし）

~~~diff
- 0058c16c ["INT_ADD", "register:40f0:8", ["const:58c16c:8", "const:4:8"]]
- 0058c16c ["CALL", null, ["callee:00588e6c:8"]]
+ 0058c1ac ["INT_ADD", "register:40f0:8", ["const:58c1ac:8", "const:4:8"]]
+ 0058c1ac ["CALL", null, ["callee:00588e6c:8"]]
- 0058c16c bytes 30f3ff97
+ 0058c1ac bytes 30f3ff97
- 0058c1f0 ["INT_ADD", "register:40f0:8", ["const:58c1f0:8", "const:4:8"]]
- 0058c1f0 ["CALL", null, ["callee:00589144:8"]]
+ 0058c230 ["INT_ADD", "register:40f0:8", ["const:58c230:8", "const:4:8"]]
+ 0058c230 ["CALL", null, ["callee:00589144:8"]]
- 0058c1f0 bytes c5f3ff97
+ 0058c230 bytes c5f3ff97
- 0058c174 ["INT_ADD", "register:40f0:8", ["const:58c174:8", "const:4:8"]]
- 0058c174 ["CALL", null, ["callee:0058915c:8"]]
+ 0058c1b4 ["INT_ADD", "register:40f0:8", ["const:58c1b4:8", "const:4:8"]]
+ 0058c1b4 ["CALL", null, ["callee:0058915c:8"]]
- 0058c174 bytes eaf3ff97
+ 0058c1b4 bytes eaf3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f800f8889474e36ae5127828b0fd08b4"></a>

### [`0058c2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c2b0.md) → [`0058c2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c2f0.md) FUN_0058c2f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005975f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975f8.md) · 呼出先 8件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00597638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597638.md) · 呼出先 8件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

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
      "definition_site": "0058c340",
      "incomplete_value": true,
      "site": "0058c340",
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
                "const:9bd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c300",
      "incomplete_value": true,
      "site": "0058c300",
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
                "const:8e1:8"
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
      "0058c330",
      "READ",
      [
        "storage",
        "002a78e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058c330",
      "READ",
      [
        "storage",
        "002a79bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058c340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c2b0.md#insn-0058c340) · [`0058c2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c2b0.md#insn-0058c2d4) · [`0058c2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c2b0.md#insn-0058c2dc)
- 新版 `0058c380`（命令位置の公開資料なし） · `0058c314`（命令位置の公開資料なし） · `0058c31c`（命令位置の公開資料なし）

~~~diff
- 0058c340 ["INT_ADD", "register:40f0:8", ["const:58c340:8", "const:4:8"]]
- 0058c340 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058c380 ["INT_ADD", "register:40f0:8", ["const:58c380:8", "const:4:8"]]
+ 0058c380 ["CALL", null, ["callee:00c57eb0:8"]]
- 0058c340 bytes dc2d1b94
+ 0058c380 bytes cc2e1b94
- 0058c2d4 ["INT_ADD", "register:40f0:8", ["const:58c2d4:8", "const:4:8"]]
- 0058c2d4 ["CALL", null, ["callee:00588e6c:8"]]
+ 0058c314 ["INT_ADD", "register:40f0:8", ["const:58c314:8", "const:4:8"]]
+ 0058c314 ["CALL", null, ["callee:00588e6c:8"]]
- 0058c2d4 bytes d6f2ff97
+ 0058c314 bytes d6f2ff97
- 0058c2dc ["INT_ADD", "register:40f0:8", ["const:58c2dc:8", "const:4:8"]]
- 0058c2dc ["CALL", null, ["callee:0058915c:8"]]
+ 0058c31c ["INT_ADD", "register:40f0:8", ["const:58c31c:8", "const:4:8"]]
+ 0058c31c ["CALL", null, ["callee:0058915c:8"]]
- 0058c2dc bytes 90f3ff97
+ 0058c31c bytes 90f3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-412d212c5908266962e4408b7ca0ecb2"></a>

### [`0058c3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c3e8.md) → [`0058c428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c428.md) FUN_0058c428

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00597600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597600.md) · 呼出先 9件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`0057c55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c55c.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 1件 [`00597640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597640.md) · 呼出先 9件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`0057c59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c59c.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0058c450",
      "incomplete_value": false,
      "site": "0058c45c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c410",
      "incomplete_value": false,
      "site": "0058c41c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:f98:8"
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
      "definition_site": "0058c458",
      "incomplete_value": true,
      "site": "0058c45c",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c418",
      "incomplete_value": true,
      "site": "0058c41c",
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
                "const:8:8"
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
      "0058c450",
      "PARAM",
      [
        "storage",
        "00ca5f98",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c458",
      "READ",
      [
        "storage",
        "00ca5fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c460",
      "WRITE",
      [
        "storage",
        "00ca5f98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058c450",
      "PARAM",
      [
        "storage",
        "00ca6398",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c458",
      "READ",
      [
        "storage",
        "00ca63a0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c460",
      "WRITE",
      [
        "storage",
        "00ca6398",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058c41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c3e8.md#insn-0058c41c) · [`0058c400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c3e8.md#insn-0058c400) · [`0058c404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c3e8.md#insn-0058c404)
- 新版 `0058c45c`（命令位置の公開資料なし） · `0058c440`（命令位置の公開資料なし） · `0058c444`（命令位置の公開資料なし）

~~~diff
- 0058c41c ["INT_ADD", "register:40f0:8", ["const:58c41c:8", "const:4:8"]]
- 0058c41c ["CALL", null, ["callee:0057c59c:8"]]
+ 0058c45c ["INT_ADD", "register:40f0:8", ["const:58c45c:8", "const:4:8"]]
+ 0058c45c ["CALL", null, ["callee:0057c59c:8"]]
- 0058c41c bytes 50c0ff97
+ 0058c45c bytes 50c0ff97
- 0058c400 ["COPY", "register:4098:8", ["const:ca5000:8"]]
+ 0058c440 ["COPY", "register:4098:8", ["const:ca6000:8"]]
- 0058c400 bytes d33800b0
+ 0058c440 bytes d33800d0
- 0058c404 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 0058c404 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0058c404 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0058c404 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0058c444 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 0058c444 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0058c444 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0058c444 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0058c404 bytes 73623e91
+ 0058c444 bytes 73620e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf2415baece541d7c00fb300269c7287"></a>

### [`0058c524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c524.md) → [`0058c564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c564.md) FUN_0058c564

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597604.md) · 呼出先 12件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00597644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597644.md) · 呼出先 12件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.50% / 新版 93.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058c5b4",
      "incomplete_value": true,
      "site": "0058c5b4",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:45f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c574",
      "incomplete_value": true,
      "site": "0058c574",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:41f:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "0058c630",
      "incomplete_value": true,
      "site": "0058c630",
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
      "definition_site": "0058c5f0",
      "incomplete_value": true,
      "site": "0058c5f0",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0058c6fc",
      "incomplete_value": false,
      "site": "0058c700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c6bc",
      "incomplete_value": false,
      "site": "0058c6c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
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
      "0058c5a8",
      "READ",
      [
        "storage",
        "002ba41f",
        null,
        "string"
      ]
    ],
    [
      "0058c618",
      "PARAM",
      [
        "storage",
        "00ca5fb0",
        null,
        null
      ]
    ],
    [
      "0058c628",
      "READ",
      [
        "storage",
        "00ca5fa0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058c5a8",
      "READ",
      [
        "storage",
        "002ba45f",
        null,
        "string"
      ]
    ],
    [
      "0058c618",
      "PARAM",
      [
        "storage",
        "00ca63b0",
        null,
        null
      ]
    ],
    [
      "0058c628",
      "READ",
      [
        "storage",
        "00ca63a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058c5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c524.md#insn-0058c5b4) · [`0058c6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c524.md#insn-0058c6c0) · [`0058c54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c524.md#insn-0058c54c)
- 新版 `0058c5f4`（命令位置の公開資料なし） · `0058c700`（命令位置の公開資料なし） · `0058c58c`（命令位置の公開資料なし）

~~~diff
- 0058c5b4 ["INT_ADD", "register:40f0:8", ["const:58c5b4:8", "const:4:8"]]
- 0058c5b4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058c5f4 ["INT_ADD", "register:40f0:8", ["const:58c5f4:8", "const:4:8"]]
+ 0058c5f4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0058c5b4 bytes 3f2d1b94
+ 0058c5f4 bytes 2f2e1b94
- 0058c6c0 ["INT_ADD", "register:40f0:8", ["const:58c6c0:8", "const:4:8"]]
- 0058c6c0 ["CALL", null, ["callee:00c580f0:8"]]
+ 0058c700 ["INT_ADD", "register:40f0:8", ["const:58c700:8", "const:4:8"]]
+ 0058c700 ["CALL", null, ["callee:00c580f0:8"]]
- 0058c6c0 bytes 8c2d1b94
+ 0058c700 bytes 7c2e1b94
- 0058c54c ["INT_ADD", "register:40f0:8", ["const:58c54c:8", "const:4:8"]]
- 0058c54c ["CALL", null, ["callee:00588e6c:8"]]
+ 0058c58c ["INT_ADD", "register:40f0:8", ["const:58c58c:8", "const:4:8"]]
+ 0058c58c ["CALL", null, ["callee:00588e6c:8"]]
- 0058c54c bytes 38f2ff97
+ 0058c58c bytes 38f2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-657dff666661f27bb11ab536f48a59ca"></a>

### [`0058c784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c784.md) → [`0058c7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c7c4.md) FUN_0058c7c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597608.md) · 呼出先 6件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`0057be68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md)
- 新版 呼出元 1件 [`00597648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597648.md) · 呼出先 6件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`0057bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.16% / 新版 94.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058c91c",
      "incomplete_value": true,
      "site": "0058c91c",
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
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c8dc",
      "incomplete_value": true,
      "site": "0058c8dc",
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
            "const:f98:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0058c808",
      "incomplete_value": true,
      "site": "0058c808",
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
      "definition_site": "0058c7c8",
      "incomplete_value": true,
      "site": "0058c7c8",
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
      "definition_site": "0058c918",
      "incomplete_value": true,
      "site": "0058c918",
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
      "definition_site": "0058c8d8",
      "incomplete_value": true,
      "site": "0058c8d8",
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
    "ordinal": 14,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058c7f4",
      "PARAM",
      [
        "storage",
        "00ca5fb0",
        null,
        null
      ]
    ],
    [
      "0058c804",
      "READ",
      [
        "storage",
        "00ca5fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c85c",
      "READ",
      [
        "storage",
        "00ca5ff0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058c7f4",
      "PARAM",
      [
        "storage",
        "00ca63b0",
        null,
        null
      ]
    ],
    [
      "0058c804",
      "READ",
      [
        "storage",
        "00ca63a0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c85c",
      "READ",
      [
        "storage",
        "00ca63f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058c7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c784.md#insn-0058c7b8) · [`0058c898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c784.md#insn-0058c898) · [`0058c8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c784.md#insn-0058c8dc)
- 新版 `0058c7f8`（命令位置の公開資料なし） · `0058c8d8`（命令位置の公開資料なし） · `0058c91c`（命令位置の公開資料なし）

~~~diff
- 0058c7b8 ["INT_ADD", "register:40f0:8", ["const:58c7b8:8", "const:4:8"]]
- 0058c7b8 ["CALL", null, ["callee:00c580e0:8"]]
+ 0058c7f8 ["INT_ADD", "register:40f0:8", ["const:58c7f8:8", "const:4:8"]]
+ 0058c7f8 ["CALL", null, ["callee:00c580e0:8"]]
- 0058c7b8 bytes 4a2d1b94
+ 0058c7f8 bytes 3a2e1b94
- 0058c898 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058c898 ["INT_ADD", "register:40f0:8", ["const:58c898:8", "const:4:8"]]
- 0058c898 ["CALLIND", null, ["register:0:8"]]
+ 0058c8d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058c8d8 ["INT_ADD", "register:40f0:8", ["const:58c8d8:8", "const:4:8"]]
+ 0058c8d8 ["CALLIND", null, ["register:0:8"]]
- 0058c898 bytes 00013fd6
+ 0058c8d8 bytes 00013fd6
- 0058c8dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f98:8"]]
- 0058c8dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0058c91c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:398:8"]]
+ 0058c91c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0058c8dc bytes 28cd07f9
+ 0058c91c bytes 28cd01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f669d2f4a53c4b46e3267f7a8404c100"></a>

### [`0058ca0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058ca0c.md) → [`0058ca4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058ca4c.md) FUN_0058ca4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0059760c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059760c.md) · 呼出先 13件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 1件 [`0059764c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059764c.md) · 呼出先 13件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058caa0",
      "incomplete_value": true,
      "site": "0058caa0",
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
                "const:7f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ca60",
      "incomplete_value": true,
      "site": "0058ca60",
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
                "const:71c:8"
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
      "definition_site": "0058cab4",
      "incomplete_value": true,
      "site": "0058cac4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fb2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ca74",
      "incomplete_value": true,
      "site": "0058ca84",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee5:8"
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
      "0058ca94",
      "READ",
      [
        "storage",
        "002a671c",
        null,
        "string"
      ]
    ],
    [
      "0058cab4",
      "READ",
      [
        "storage",
        "002a0ee5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058ca94",
      "READ",
      [
        "storage",
        "002a67f8",
        null,
        "string"
      ]
    ],
    [
      "0058cab4",
      "READ",
      [
        "storage",
        "002a0fb2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ca30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058ca0c.md#insn-0058ca30) · [`0058ca38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058ca0c.md#insn-0058ca38) · [`0058ca50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058ca0c.md#insn-0058ca50)
- 新版 `0058ca70`（命令位置の公開資料なし） · `0058ca78`（命令位置の公開資料なし） · `0058ca90`（命令位置の公開資料なし）

~~~diff
- 0058ca30 ["INT_ADD", "register:40f0:8", ["const:58ca30:8", "const:4:8"]]
- 0058ca30 ["CALL", null, ["callee:00588e6c:8"]]
+ 0058ca70 ["INT_ADD", "register:40f0:8", ["const:58ca70:8", "const:4:8"]]
+ 0058ca70 ["CALL", null, ["callee:00588e6c:8"]]
- 0058ca30 bytes fff0ff97
+ 0058ca70 bytes fff0ff97
- 0058ca38 ["INT_ADD", "register:40f0:8", ["const:58ca38:8", "const:4:8"]]
- 0058ca38 ["CALL", null, ["callee:0058915c:8"]]
+ 0058ca78 ["INT_ADD", "register:40f0:8", ["const:58ca78:8", "const:4:8"]]
+ 0058ca78 ["CALL", null, ["callee:0058915c:8"]]
- 0058ca38 bytes b9f1ff97
+ 0058ca78 bytes b9f1ff97
- 0058ca50 ["COPY", "tmp:0:8", ["const:71c:8"]]
- 0058ca50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058ca50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058ca50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058ca90 ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 0058ca90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ca90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ca90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058ca50 bytes 08711c91
+ 0058ca90 bytes 08e11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ce635c9187220e950612c34250cb9be"></a>

### [`0058cc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058cc70.md) → [`0058ccb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058ccb0.md) FUN_0058ccb0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00597614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597614.md) · 呼出先 13件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00597654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597654.md) · 呼出先 13件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.79% / 新版 93.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058cd3c",
      "incomplete_value": true,
      "site": "0058cd44",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ccfc",
      "incomplete_value": true,
      "site": "0058cd04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f40:8"
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
      "definition_site": "0058cd38",
      "incomplete_value": true,
      "site": "0058cd48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:61e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ccf8",
      "incomplete_value": true,
      "site": "0058cd08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5de:8"
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
      "definition_site": "0058cd38",
      "incomplete_value": true,
      "site": "0058cd48",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0058ccf8",
      "incomplete_value": true,
      "site": "0058cd08",
      "value": [
        "LOAD",
        "16",
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
      "0058cd38",
      "READ",
      [
        "storage",
        "002ab5de",
        null,
        "string"
      ]
    ],
    [
      "0058cd38",
      "READ",
      [
        "storage",
        "002ab5ee",
        null,
        "string"
      ]
    ],
    [
      "0058cd3c",
      "READ",
      [
        "storage",
        "002c2f40",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058cd38",
      "READ",
      [
        "storage",
        "002ab61e",
        null,
        "string"
      ]
    ],
    [
      "0058cd38",
      "READ",
      [
        "storage",
        "002ab62e",
        null,
        "string"
      ]
    ],
    [
      "0058cd3c",
      "READ",
      [
        "storage",
        "002c2f80",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058cd54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058cc70.md#insn-0058cd54) · [`0058cdd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058cc70.md#insn-0058cdd4) · [`0058ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058cc70.md#insn-0058ccb8)
- 新版 `0058cd94`（命令位置の公開資料なし） · `0058ce14`（命令位置の公開資料なし） · `0058ccf8`（命令位置の公開資料なし）

~~~diff
- 0058cd54 ["INT_ADD", "register:40f0:8", ["const:58cd54:8", "const:4:8"]]
- 0058cd54 ["CALL", null, ["callee:00589144:8"]]
+ 0058cd94 ["INT_ADD", "register:40f0:8", ["const:58cd94:8", "const:4:8"]]
+ 0058cd94 ["CALL", null, ["callee:00589144:8"]]
- 0058cd54 bytes ecf0ff97
+ 0058cd94 bytes ecf0ff97
- 0058cdd4 ["INT_ADD", "register:40f0:8", ["const:58cdd4:8", "const:4:8"]]
- 0058cdd4 ["CALL", null, ["callee:0058f434:8"]]
+ 0058ce14 ["INT_ADD", "register:40f0:8", ["const:58ce14:8", "const:4:8"]]
+ 0058ce14 ["CALL", null, ["callee:0058f434:8"]]
- 0058cdd4 bytes 88090094
+ 0058ce14 bytes 88090094
- 0058ccb8 ["INT_ADD", "register:40f0:8", ["const:58ccb8:8", "const:4:8"]]
- 0058ccb8 ["CALL", null, ["callee:00588e6c:8"]]
+ 0058ccf8 ["INT_ADD", "register:40f0:8", ["const:58ccf8:8", "const:4:8"]]
+ 0058ccf8 ["CALL", null, ["callee:00588e6c:8"]]
- 0058ccb8 bytes 5df0ff97
+ 0058ccf8 bytes 5df0ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ddd9ff99966363510531b3a2ec384db"></a>

### [`0058cf18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058cf18.md) → [`0058cf58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058cf58.md) FUN_0058cf58

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00597618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597618.md) · 呼出先 12件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00597658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597658.md) · 呼出先 12件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058cfac",
      "incomplete_value": true,
      "site": "0058cfac",
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
                "const:2d9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058cf6c",
      "incomplete_value": true,
      "site": "0058cf6c",
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
                "const:20c:8"
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
      "definition_site": "0058cfb8",
      "incomplete_value": true,
      "site": "0058cfc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4e1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058cf78",
      "incomplete_value": true,
      "site": "0058cf88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4a1:8"
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
      "definition_site": "0058cfcc",
      "incomplete_value": true,
      "site": "0058cfcc",
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
      "definition_site": "0058cf8c",
      "incomplete_value": true,
      "site": "0058cf8c",
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
      "0058cf98",
      "READ",
      [
        "storage",
        "002a120c",
        null,
        "string"
      ]
    ],
    [
      "0058cfb8",
      "READ",
      [
        "storage",
        "002bb4a1",
        null,
        "string"
      ]
    ],
    [
      "0058cfc0",
      "READ",
      [
        "storage",
        "002bb4ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058cf98",
      "READ",
      [
        "storage",
        "002a12d9",
        null,
        "string"
      ]
    ],
    [
      "0058cfb8",
      "READ",
      [
        "storage",
        "002bb4e1",
        null,
        "string"
      ]
    ],
    [
      "0058cfc0",
      "READ",
      [
        "storage",
        "002bb4ee",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058cf48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058cf18.md#insn-0058cf48) · [`0058cfc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058cf18.md#insn-0058cfc8) · [`0058d048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058cf18.md#insn-0058d048)
- 新版 `0058cf88`（命令位置の公開資料なし） · `0058d008`（命令位置の公開資料なし） · `0058d088`（命令位置の公開資料なし）

~~~diff
- 0058cf48 ["INT_ADD", "register:40f0:8", ["const:58cf48:8", "const:4:8"]]
- 0058cf48 ["CALL", null, ["callee:0058915c:8"]]
+ 0058cf88 ["INT_ADD", "register:40f0:8", ["const:58cf88:8", "const:4:8"]]
+ 0058cf88 ["CALL", null, ["callee:0058915c:8"]]
- 0058cf48 bytes 75f0ff97
+ 0058cf88 bytes 75f0ff97
- 0058cfc8 ["INT_ADD", "register:40f0:8", ["const:58cfc8:8", "const:4:8"]]
- 0058cfc8 ["CALL", null, ["callee:00589144:8"]]
+ 0058d008 ["INT_ADD", "register:40f0:8", ["const:58d008:8", "const:4:8"]]
+ 0058d008 ["CALL", null, ["callee:00589144:8"]]
- 0058cfc8 bytes 4ff0ff97
+ 0058d008 bytes 4ff0ff97
- 0058d048 ["INT_ADD", "register:40f0:8", ["const:58d048:8", "const:4:8"]]
- 0058d048 ["CALL", null, ["callee:0058f434:8"]]
+ 0058d088 ["INT_ADD", "register:40f0:8", ["const:58d088:8", "const:4:8"]]
+ 0058d088 ["CALL", null, ["callee:0058f434:8"]]
- 0058d048 bytes eb080094
+ 0058d088 bytes eb080094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-050459949ae13fcf0aec3d85f5548e7d"></a>

### [`0058d130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d130.md) → [`0058d170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d170.md) FUN_0058d170

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058ec80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058ec80.md) · 呼出先 15件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`00589128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589128.md)
- 新版 呼出元 1件 [`0058ecc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058ecc0.md) · 呼出先 15件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589168.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.97% / 新版 92.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058d1ec",
      "incomplete_value": true,
      "site": "0058d204",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9ca:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058d1ac",
      "incomplete_value": true,
      "site": "0058d1c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8ee:8"
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
      "definition_site": "0058d224",
      "incomplete_value": true,
      "site": "0058d22c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:ba0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058d1e4",
      "incomplete_value": true,
      "site": "0058d1ec",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:b60:8"
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
      "definition_site": "0058d32c",
      "incomplete_value": true,
      "site": "0058d32c",
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
                "const:1da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058d2ec",
      "incomplete_value": true,
      "site": "0058d2ec",
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
                "const:10d:8"
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
      "0058d1ac",
      "DATA",
      [
        "storage",
        "00c6cb38",
        null,
        "undefined *"
      ]
    ],
    [
      "0058d1ec",
      "READ",
      [
        "storage",
        "002a78ee",
        null,
        "string"
      ]
    ],
    [
      "0058d220",
      "READ",
      [
        "storage",
        "002a1216",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058d1ac",
      "DATA",
      [
        "storage",
        "00c6cf38",
        null,
        "undefined *"
      ]
    ],
    [
      "0058d1ec",
      "READ",
      [
        "storage",
        "002a79ca",
        null,
        "string"
      ]
    ],
    [
      "0058d220",
      "READ",
      [
        "storage",
        "002a12e3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058d22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d130.md#insn-0058d22c) · [`0058d400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d130.md#insn-0058d400) · [`0058d154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d130.md#insn-0058d154)
- 新版 `0058d26c`（命令位置の公開資料なし） · `0058d440`（命令位置の公開資料なし） · `0058d194`（命令位置の公開資料なし）

~~~diff
- 0058d22c ["INT_ADD", "register:40f0:8", ["const:58d22c:8", "const:4:8"]]
- 0058d22c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058d26c ["INT_ADD", "register:40f0:8", ["const:58d26c:8", "const:4:8"]]
+ 0058d26c ["CALL", null, ["callee:00c57eb0:8"]]
- 0058d22c bytes 212a1b94
+ 0058d26c bytes 112b1b94
- 0058d400 ["INT_ADD", "register:40f0:8", ["const:58d400:8", "const:4:8"]]
- 0058d400 ["CALL", null, ["callee:00589840:8"]]
+ 0058d440 ["INT_ADD", "register:40f0:8", ["const:58d440:8", "const:4:8"]]
+ 0058d440 ["CALL", null, ["callee:00589840:8"]]
- 0058d400 bytes 00f1ff97
+ 0058d440 bytes 00f1ff97
- 0058d154 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 0058d154 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058d154 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058d154 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058d194 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 0058d194 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058d194 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058d194 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058d154 bytes 29e12c91
+ 0058d194 bytes 29e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08262d8c7c13279ff6d9b3ad3f839163"></a>

### [`0058d5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d5c4.md) → [`0058d604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d604.md) FUN_0058d604

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058d678",
      "incomplete_value": true,
      "site": "0058d680",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058d638",
      "incomplete_value": true,
      "site": "0058d640",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8e0:8"
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
      "definition_site": "0058d674",
      "incomplete_value": true,
      "site": "0058d684",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:f88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058d634",
      "incomplete_value": true,
      "site": "0058d644",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:f48:8"
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
      "definition_site": "0058d674",
      "incomplete_value": true,
      "site": "0058d684",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0058d634",
      "incomplete_value": true,
      "site": "0058d644",
      "value": [
        "LOAD",
        "16",
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
      "0058d674",
      "READ",
      [
        "storage",
        "002bff48",
        null,
        "string"
      ]
    ],
    [
      "0058d674",
      "READ",
      [
        "storage",
        "002bff58",
        null,
        "string"
      ]
    ],
    [
      "0058d678",
      "READ",
      [
        "storage",
        "002c28e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058d674",
      "READ",
      [
        "storage",
        "002bff88",
        null,
        "string"
      ]
    ],
    [
      "0058d674",
      "READ",
      [
        "storage",
        "002bff98",
        null,
        "string"
      ]
    ],
    [
      "0058d678",
      "READ",
      [
        "storage",
        "002c2920",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058d680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d5c4.md#insn-0058d680) · [`0058d5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d5c4.md#insn-0058d5f0) · [`0058d5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d5c4.md#insn-0058d5f8)
- 新版 `0058d6c0`（命令位置の公開資料なし） · `0058d630`（命令位置の公開資料なし） · `0058d638`（命令位置の公開資料なし）

~~~diff
- 0058d680 ["INT_ADD", "register:40f0:8", ["const:58d680:8", "const:4:8"]]
- 0058d680 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058d6c0 ["INT_ADD", "register:40f0:8", ["const:58d6c0:8", "const:4:8"]]
+ 0058d6c0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0058d680 bytes 0c291b94
+ 0058d6c0 bytes fc291b94
- 0058d5f0 ["INT_ADD", "register:40f0:8", ["const:58d5f0:8", "const:4:8"]]
- 0058d5f0 ["CALL", null, ["callee:00589840:8"]]
+ 0058d630 ["INT_ADD", "register:40f0:8", ["const:58d630:8", "const:4:8"]]
+ 0058d630 ["CALL", null, ["callee:00589840:8"]]
- 0058d5f0 bytes 84f0ff97
+ 0058d630 bytes 84f0ff97
- 0058d5f8 ["INT_ADD", "register:40f0:8", ["const:58d5f8:8", "const:4:8"]]
- 0058d5f8 ["CALL", null, ["callee:00588e6c:8"]]
+ 0058d638 ["INT_ADD", "register:40f0:8", ["const:58d638:8", "const:4:8"]]
+ 0058d638 ["CALL", null, ["callee:00588e6c:8"]]
- 0058d5f8 bytes 0deeff97
+ 0058d638 bytes 0deeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

